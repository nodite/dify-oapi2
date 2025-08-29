from dify_oapi.core.enum import HttpMethod
from dify_oapi.core.model.base_request import BaseRequest

from .create_tag_request_body import CreateTagRequestBody


class CreateTagRequest(BaseRequest):
    def __init__(self):
        super().__init__()
        self.request_body: CreateTagRequestBody | None = None

    @staticmethod
    def builder() -> "CreateTagRequestBuilder":
        return CreateTagRequestBuilder()


class CreateTagRequestBuilder:
    def __init__(self):
        create_tag_request = CreateTagRequest()
        create_tag_request.http_method = HttpMethod.POST
        create_tag_request.uri = "/v1/datasets/tags"
        self._create_tag_request = create_tag_request

    def build(self) -> CreateTagRequest:
        return self._create_tag_request

    def request_body(self, request_body: CreateTagRequestBody) -> "CreateTagRequestBuilder":
        self._create_tag_request.request_body = request_body
        self._create_tag_request.body = request_body.model_dump(exclude_none=True, mode="json")
        return self
