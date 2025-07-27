from __future__ import annotations

from dify_oapi.core.enum import HttpMethod
from dify_oapi.core.model.base_request import BaseRequest

from .create_request_body import CreateRequestBody


class CreateRequest(BaseRequest):
    def __init__(self):
        super().__init__()
        self.request_body: CreateRequestBody | None = None

    @staticmethod
    def builder() -> CreateRequestBuilder:
        return CreateRequestBuilder()


class CreateRequestBuilder:
    def __init__(self):
        create_request = CreateRequest()
        create_request.http_method = HttpMethod.POST
        create_request.uri = "/v1/datasets"
        self._create_request = create_request

    def build(self) -> CreateRequest:
        return self._create_request

    def request_body(self, request_body: CreateRequestBody) -> CreateRequestBuilder:
        self._create_request.request_body = request_body
        self._create_request.body = request_body.model_dump(exclude_none=True, mode="json")
        return self
