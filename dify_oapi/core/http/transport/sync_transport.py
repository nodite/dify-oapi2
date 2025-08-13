import json
import os
import time
from collections.abc import Generator
from typing import Literal, overload

import httpx

from dify_oapi.core.enum import HttpMethod
from dify_oapi.core.json import JSON
from dify_oapi.core.log import logger
from dify_oapi.core.model.base_request import BaseRequest
from dify_oapi.core.model.base_response import BaseResponse
from dify_oapi.core.model.config import Config
from dify_oapi.core.model.raw_response import RawResponse
from dify_oapi.core.model.request_option import RequestOption
from dify_oapi.core.type import T

from ._misc import _build_header, _build_url, _get_sleep_time, _merge_dicts, _unmarshaller


def _format_log_details(
    method: str, url: str, headers: dict, queries: list[tuple[str, str]] | dict, body_data: dict | None
) -> str:
    """Format log details"""
    details = [f"{method} {url}"]
    if headers:
        details.append(f"headers: {JSON.marshal(headers)}")
    if queries:
        queries_dict = dict(queries) if isinstance(queries, list) else queries
        details.append(f"params: {JSON.marshal(queries_dict)}")
    if body_data:
        details.append(f"body: {JSON.marshal(body_data)}")
    return ", ".join(details)


def _handle_stream_error(response: httpx.Response) -> bytes:
    """Handle streaming response errors"""
    try:
        error_detail = response.read()
        error_message = error_detail.decode("utf-8", errors="ignore").strip()
    except Exception:
        error_message = f"Error response with status code {response.status_code}"
    logger.warning(f"Streaming request failed: {response.status_code}, detail: {error_message}")
    return f"data: [ERROR] {error_message}\n\n".encode()


def _stream_generator(
    conf: Config,
    req: BaseRequest,
    *,
    url: str,
    headers: dict[str, str],
    json_: dict | None,
    data: dict | None,
    files: dict | None,
    http_method: HttpMethod,
) -> Generator[bytes, None, None]:
    method_name = http_method.name
    body_data = _merge_dicts(json_, files, data)

    for retry in range(conf.max_retry_count + 1):
        if retry > 0:
            sleep_time = _get_sleep_time(retry)
            logger.info(f"in-request: sleep {sleep_time}s")
            time.sleep(sleep_time)

        try:
            with (
                httpx.Client() as client,
                client.stream(
                    method_name,
                    url,
                    headers=headers,
                    params=tuple(req.queries),
                    json=json_,
                    data=data,
                    files=files,
                    timeout=conf.timeout,
                ) as response,
            ):
                logger.debug(
                    f"{_format_log_details(method_name, url, headers, req.queries, body_data)}, stream response"
                )

                if response.status_code != 200:
                    yield _handle_stream_error(response)
                    return

                try:
                    yield from response.iter_bytes()
                except Exception as e:
                    logger.exception("Streaming failed during chunk reading")
                    yield f"data: [ERROR] Stream interrupted: {str(e)}\n\n".encode()
                return

        except httpx.RequestError as e:
            err_msg = f"{e.__class__.__name__}: {e!r}"
            log_details = _format_log_details(method_name, url, headers, req.queries, body_data)

            if retry < conf.max_retry_count:
                logger.info(f"in-request: retrying ({retry + 1}/{conf.max_retry_count}) {log_details}, exp: {err_msg}")
                continue
            logger.info(
                f"in-request: request failed, retried ({retry}/{conf.max_retry_count}) {log_details}, exp: {err_msg}"
            )
            raise


class Transport:
    @staticmethod
    @overload
    def execute(
        conf: Config,
        req: BaseRequest,
        *,
        stream: Literal[True],
        option: RequestOption | None,
    ) -> Generator[bytes, None, None]: ...

    @staticmethod
    @overload
    def execute(conf: Config, req: BaseRequest) -> BaseResponse: ...

    @staticmethod
    @overload
    def execute(conf: Config, req: BaseRequest, *, option: RequestOption | None) -> BaseResponse: ...

    @staticmethod
    @overload
    def execute(
        conf: Config,
        req: BaseRequest,
        *,
        unmarshal_as: type[T],
        option: RequestOption | None,
    ) -> T: ...

    @staticmethod
    def execute(
        conf: Config,
        req: BaseRequest,
        *,
        stream: bool = False,
        unmarshal_as: type[T] | type[BaseResponse] | None = None,
        option: RequestOption | None = None,
    ):
        unmarshal_as = unmarshal_as or BaseResponse
        option = option or RequestOption()

        if req.http_method is None:
            raise RuntimeError("HTTP method is required")

        url = _build_url(conf.domain, req.uri, req.paths)
        headers = _build_header(req, option)

        # Prepare request body
        json_, files, data = None, None, None
        if req.files:
            files = req.files
            if req.body is not None:
                data = json.loads(JSON.marshal(req.body))
        elif req.body is not None:
            json_ = json.loads(JSON.marshal(req.body))

        if stream:
            return _stream_generator(
                conf, req, url=url, headers=headers, json_=json_, data=data, files=files, http_method=req.http_method
            )

        # Set local proxy
        original_no_proxy = os.environ.get("NO_PROXY", "")
        if "localhost" not in original_no_proxy:
            os.environ["NO_PROXY"] = f"{original_no_proxy},localhost,127.0.0.1".strip(",")

        method_name = req.http_method.name
        body_data = _merge_dicts(json_, files, data)

        with httpx.Client() as client:
            for retry in range(conf.max_retry_count + 1):
                if retry > 0:
                    sleep_time = _get_sleep_time(retry)
                    logger.info(f"in-request: sleep {sleep_time}s")
                    time.sleep(sleep_time)

                try:
                    response = client.request(
                        method_name,
                        url,
                        headers=headers,
                        params=tuple(req.queries),
                        json=json_,
                        data=data,
                        files=files,
                        timeout=conf.timeout,
                    )
                    break
                except httpx.RequestError as e:
                    err_msg = f"{e.__class__.__name__}: {e!r}"
                    log_details = _format_log_details(method_name, url, headers, req.queries, body_data)

                    if retry < conf.max_retry_count:
                        logger.info(
                            f"in-request: retrying ({retry + 1}/{conf.max_retry_count}) {log_details}, exp: {err_msg}"
                        )
                        continue
                    logger.info(
                        f"in-request: request failed, retried ({retry}/{conf.max_retry_count}) {log_details}, exp: {err_msg}"
                    )
                    raise

            logger.debug(
                f"{_format_log_details(method_name, url, headers, req.queries, body_data)} {response.status_code}"
            )

            raw_resp = RawResponse()
            raw_resp.status_code = response.status_code
            raw_resp.headers = dict(response.headers)
            raw_resp.content = response.content
            return _unmarshaller(raw_resp, unmarshal_as)
