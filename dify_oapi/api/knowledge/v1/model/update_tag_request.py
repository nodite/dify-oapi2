from dify_oapi.core.enum import HttpMethod
from dify_oapi.core.model.base_request import BaseRequest

from .update_tag_request_body import UpdateTagRequestBody


class UpdateTagRequest(BaseRequest):
    def __init__(self):
        super().__init__()
        self.request_body: UpdateTagRequestBody | None = None

    @staticmethod
    def builder() -> "UpdateTagRequestBuilder":
        return UpdateTagRequestBuilder()


class UpdateTagRequestBuilder:
    def __init__(self):
        update_tag_request = UpdateTagRequest()
        update_tag_request.http_method = HttpMethod.PATCH
        update_tag_request.uri = "/v1/datasets/tags"
        self._update_tag_request = update_tag_request

    def build(self) -> UpdateTagRequest:
        return self._update_tag_request

    def request_body(self, request_body: UpdateTagRequestBody) -> "UpdateTagRequestBuilder":
        self._update_tag_request.request_body = request_body
        self._update_tag_request.body = request_body.model_dump(exclude_none=True, mode="json")
        return self
