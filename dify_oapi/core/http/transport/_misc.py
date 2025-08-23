from dify_oapi.core.const import APPLICATION_JSON, AUTHORIZATION, SLEEP_BASE_TIME, UTF_8
from dify_oapi.core.json import JSON
from dify_oapi.core.log import logger
from dify_oapi.core.misc import HiddenText
from dify_oapi.core.model.base_request import BaseRequest
from dify_oapi.core.model.raw_response import RawResponse
from dify_oapi.core.model.request_option import RequestOption
from dify_oapi.core.type import T


def _build_url(domain: str | None, uri: str | None, paths: dict[str, str] | None) -> str:
    if not domain:
        raise RuntimeError("domain is required")
    if not uri:
        raise RuntimeError("uri is required")

    # Replace path parameters
    for key, value in (paths or {}).items():
        uri = uri.replace(f":{key}", value)

    # Normalize URL joining
    return f"{domain.rstrip('/')}{uri}" if not uri.startswith("/") else f"{domain.rstrip('/')}{uri}"


def _build_header(request: BaseRequest, option: RequestOption) -> dict[str, str]:
    headers = request.headers.copy()

    # Merge option headers
    if option.headers:
        headers.update(option.headers)

    # Add authorization header
    if option.api_key:
        hidden_text = HiddenText(f"Bearer {option.api_key}", redacted="****")
        headers[AUTHORIZATION] = hidden_text.secret

    return headers


def _merge_dicts(*dicts: dict | None) -> dict:
    """Merge multiple dictionaries, ignoring None values."""
    result: dict = {}
    for d in filter(None, dicts):
        result.update(d)
    return result


def _create_no_content_response(unmarshal_as: type[T]) -> T:
    """Create response for 204 No Content status."""
    try:
        # Check if the model has a 'result' field in its annotations
        annotations = getattr(unmarshal_as, "__annotations__", {})
        if "result" in annotations:
            # Only pass result if the specific model supports it
            try:
                return unmarshal_as(result="success")  # type: ignore
            except TypeError:
                # Fallback if constructor doesn't accept result
                pass
        return unmarshal_as()
    except Exception:
        resp = unmarshal_as.__new__(unmarshal_as)
        if hasattr(resp, "result"):
            try:
                object.__setattr__(resp, "result", "success")
            except Exception:
                pass
        return resp


def _handle_json_response(content: str, unmarshal_as: type[T]) -> T:
    """Handle JSON response content."""
    import json

    parsed_json = json.loads(content)

    if isinstance(parsed_json, list):
        return _handle_array_response(parsed_json, unmarshal_as)
    elif isinstance(parsed_json, dict):
        return JSON.unmarshal(content, unmarshal_as)
    else:
        return _handle_primitive_response(parsed_json, unmarshal_as)


def _handle_array_response(data: list, unmarshal_as: type[T]) -> T:
    """Handle array JSON responses."""
    try:
        # Check if the model has a 'data' field in its annotations
        annotations = getattr(unmarshal_as, "__annotations__", {})
        if "data" in annotations:
            try:
                return unmarshal_as(data=data)  # type: ignore
            except TypeError:
                # Fallback if constructor doesn't accept data
                pass
        return unmarshal_as()
    except Exception:
        resp = unmarshal_as.__new__(unmarshal_as)
        if hasattr(resp, "data"):
            try:
                object.__setattr__(resp, "data", data)
            except Exception:
                pass
        return resp


def _handle_primitive_response(value, unmarshal_as: type[T]) -> T:
    """Handle primitive JSON responses."""
    try:
        annotations = getattr(unmarshal_as, "__annotations__", {})
        if "result" in annotations:
            try:
                return unmarshal_as(result=str(value))  # type: ignore
            except TypeError:
                # Fallback if constructor doesn't accept result
                pass
        elif "data" in annotations:
            try:
                return unmarshal_as(data=value)  # type: ignore
            except TypeError:
                # Fallback if constructor doesn't accept data
                pass
        return unmarshal_as()
    except Exception:
        resp = unmarshal_as.__new__(unmarshal_as)
        if hasattr(resp, "result"):
            try:
                object.__setattr__(resp, "result", str(value))
            except Exception:
                pass
        elif hasattr(resp, "data"):
            try:
                object.__setattr__(resp, "data", value)
            except Exception:
                pass
        return resp


def _set_raw_response(resp: T, raw_resp: RawResponse) -> T:
    """Set raw response on the response object."""
    try:
        object.__setattr__(resp, "raw", raw_resp)
    except Exception:
        try:
            resp.raw = raw_resp
        except Exception:
            if hasattr(resp, "model_copy"):
                resp = resp.model_copy(update={"raw": raw_resp})
    return resp


def _unmarshaller(raw_resp: RawResponse, unmarshal_as: type[T]) -> T:
    """Unmarshal raw response to typed response object."""
    if not raw_resp.status_code:
        raise RuntimeError("status_code is required")
    if raw_resp.content is None:
        raise RuntimeError("content is required")

    # Handle 204 No Content
    if raw_resp.status_code == 204:
        resp = _create_no_content_response(unmarshal_as)
    # Handle JSON content
    elif raw_resp.content_type and raw_resp.content_type.startswith(APPLICATION_JSON):
        content = str(raw_resp.content, UTF_8)
        if content:
            try:
                resp = _handle_json_response(content, unmarshal_as)
            except Exception as e:
                logger.error(f"Failed to unmarshal to {unmarshal_as} from {content}")
                raise e
        else:
            resp = unmarshal_as()
    else:
        # Fallback for non-JSON content
        try:
            resp = unmarshal_as()
        except Exception:
            resp = unmarshal_as.__new__(unmarshal_as)

    return _set_raw_response(resp, raw_resp)


def _get_sleep_time(retry_count: int) -> float:
    """Calculate exponential backoff sleep time for retries."""
    return float(SLEEP_BASE_TIME * (2 ** (retry_count - 1)))
