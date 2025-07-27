from __future__ import annotations

from dify_oapi.core.enum import HttpMethod
from dify_oapi.core.model.base_request import BaseRequest

from .delete_request_body import DeleteRequestBody


class DeleteRequest(BaseRequest):
    def __init__(self):
        super().__init__()
        self.request_body: DeleteRequestBody | None = None

    @staticmethod
    def builder() -> DeleteRequestBuilder:
        return DeleteRequestBuilder()


class DeleteRequestBuilder:
    def __init__(self):
        delete_request = DeleteRequest()
        delete_request.http_method = HttpMethod.DELETE
        delete_request.uri = "/v1/datasets/tags"
        self._request = delete_request

    def build(self) -> DeleteRequest:
        return self._request

    def request_body(self, request_body: DeleteRequestBody) -> DeleteRequestBuilder:
        self._request.request_body = request_body
        self._request.body = request_body.model_dump(exclude_none=True, mode="json")
        return self
