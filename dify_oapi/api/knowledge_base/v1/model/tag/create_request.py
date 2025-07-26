from __future__ import annotations

from pydantic import BaseModel

from dify_oapi.core.enum import HttpMethod
from dify_oapi.core.model.base_request import BaseRequest


class CreateTagRequestBody(BaseModel):
    name: str = ""


class CreateTagRequest(BaseRequest):
    def __init__(self):
        super().__init__()
        self.request_body: CreateTagRequestBody | None = None

    @staticmethod
    def builder() -> CreateTagRequestBuilder:
        return CreateTagRequestBuilder()


class CreateTagRequestBuilder:
    def __init__(self):
        create_tag_request = CreateTagRequest()
        create_tag_request.http_method = HttpMethod.POST
        create_tag_request.uri = "/v1/datasets/tags"
        self._request = create_tag_request

    def build(self) -> CreateTagRequest:
        return self._request

    def name(self, name: str) -> CreateTagRequestBuilder:
        if self._request.request_body is None:
            self._request.request_body = CreateTagRequestBody()
        self._request.request_body.name = name
        self._request.body = self._request.request_body.model_dump(exclude_none=True, mode="json")
        return self