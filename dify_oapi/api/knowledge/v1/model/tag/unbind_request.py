from __future__ import annotations

from dify_oapi.core.enum import HttpMethod
from dify_oapi.core.model.base_request import BaseRequest

from .unbind_request_body import UnbindRequestBody


class UnbindRequest(BaseRequest):
    def __init__(self):
        super().__init__()
        self.request_body: UnbindRequestBody | None = None

    @staticmethod
    def builder() -> UnbindRequestBuilder:
        return UnbindRequestBuilder()


class UnbindRequestBuilder:
    def __init__(self):
        unbind_request = UnbindRequest()
        unbind_request.http_method = HttpMethod.POST
        unbind_request.uri = "/v1/datasets/tags/unbinding"
        self._request = unbind_request

    def build(self) -> UnbindRequest:
        return self._request

    def request_body(self, request_body: UnbindRequestBody) -> UnbindRequestBuilder:
        self._request.request_body = request_body
        self._request.body = request_body.model_dump(exclude_none=True, mode="json")
        return self
