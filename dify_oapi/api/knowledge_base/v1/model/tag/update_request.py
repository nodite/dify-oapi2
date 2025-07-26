from __future__ import annotations

from pydantic import BaseModel

from dify_oapi.core.enum import HttpMethod
from dify_oapi.core.model.base_request import BaseRequest


class UpdateTagRequestBody(BaseModel):
    name: str = ""
    tag_id: str = ""


class UpdateTagRequest(BaseRequest):
    def __init__(self):
        super().__init__()
        self.request_body: UpdateTagRequestBody | None = None

    @staticmethod
    def builder() -> UpdateTagRequestBuilder:
        return UpdateTagRequestBuilder()


class UpdateTagRequestBuilder:
    def __init__(self):
        update_tag_request = UpdateTagRequest()
        update_tag_request.http_method = HttpMethod.PATCH
        update_tag_request.uri = "/v1/datasets/tags"
        self._request = update_tag_request

    def build(self) -> UpdateTagRequest:
        return self._request

    def name(self, name: str) -> UpdateTagRequestBuilder:
        if self._request.request_body is None:
            self._request.request_body = UpdateTagRequestBody()
        self._request.request_body.name = name
        self._request.body = self._request.request_body.model_dump(exclude_none=True, mode="json")
        return self

    def tag_id(self, tag_id: str) -> UpdateTagRequestBuilder:
        if self._request.request_body is None:
            self._request.request_body = UpdateTagRequestBody()
        self._request.request_body.tag_id = tag_id
        self._request.body = self._request.request_body.model_dump(exclude_none=True, mode="json")
        return self