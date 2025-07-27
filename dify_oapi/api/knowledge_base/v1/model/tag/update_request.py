from __future__ import annotations

from dify_oapi.core.enum import HttpMethod
from dify_oapi.core.model.base_request import BaseRequest

from .update_request_body import UpdateRequestBody


class UpdateRequest(BaseRequest):
    def __init__(self):
        super().__init__()
        self.request_body: UpdateRequestBody | None = None

    @staticmethod
    def builder() -> UpdateRequestBuilder:
        return UpdateRequestBuilder()


class UpdateRequestBuilder:
    def __init__(self):
        update_request = UpdateRequest()
        update_request.http_method = HttpMethod.PATCH
        update_request.uri = "/v1/datasets/tags"
        self._request = update_request

    def build(self) -> UpdateRequest:
        return self._request

    def request_body(self, request_body: UpdateRequestBody) -> UpdateRequestBuilder:
        self._request.request_body = request_body
        self._request.body = request_body.model_dump(exclude_none=True, mode="json")
        return self
