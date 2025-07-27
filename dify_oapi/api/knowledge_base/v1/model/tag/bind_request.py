from __future__ import annotations

from dify_oapi.core.enum import HttpMethod
from dify_oapi.core.model.base_request import BaseRequest

from .bind_request_body import BindRequestBody


class BindRequest(BaseRequest):
    def __init__(self):
        super().__init__()
        self.request_body: BindRequestBody | None = None

    @staticmethod
    def builder() -> BindRequestBuilder:
        return BindRequestBuilder()


class BindRequestBuilder:
    def __init__(self):
        bind_request = BindRequest()
        bind_request.http_method = HttpMethod.POST
        bind_request.uri = "/v1/datasets/tags/binding"
        self._request = bind_request

    def build(self) -> BindRequest:
        return self._request

    def request_body(self, request_body: BindRequestBody) -> BindRequestBuilder:
        self._request.request_body = request_body
        self._request.body = request_body.model_dump(exclude_none=True, mode="json")
        return self
