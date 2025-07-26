from __future__ import annotations

from pydantic import BaseModel

from dify_oapi.core.enum import HttpMethod
from dify_oapi.core.model.base_request import BaseRequest


class UnbindTagRequestBody(BaseModel):
    tag_id: str = ""
    target_id: str = ""


class UnbindTagRequest(BaseRequest):
    def __init__(self):
        super().__init__()
        self.request_body: UnbindTagRequestBody | None = None

    @staticmethod
    def builder() -> UnbindTagRequestBuilder:
        return UnbindTagRequestBuilder()


class UnbindTagRequestBuilder:
    def __init__(self):
        unbind_tag_request = UnbindTagRequest()
        unbind_tag_request.http_method = HttpMethod.POST
        unbind_tag_request.uri = "/v1/datasets/tags/unbinding"
        self._request = unbind_tag_request

    def build(self) -> UnbindTagRequest:
        return self._request

    def tag_id(self, tag_id: str) -> UnbindTagRequestBuilder:
        if self._request.request_body is None:
            self._request.request_body = UnbindTagRequestBody()
        self._request.request_body.tag_id = tag_id
        self._request.body = self._request.request_body.model_dump(exclude_none=True, mode="json")
        return self

    def target_id(self, target_id: str) -> UnbindTagRequestBuilder:
        if self._request.request_body is None:
            self._request.request_body = UnbindTagRequestBody()
        self._request.request_body.target_id = target_id
        self._request.body = self._request.request_body.model_dump(exclude_none=True, mode="json")
        return self