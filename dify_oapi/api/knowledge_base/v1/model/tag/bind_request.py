from __future__ import annotations

from typing import List

from pydantic import BaseModel

from dify_oapi.core.enum import HttpMethod
from dify_oapi.core.model.base_request import BaseRequest


class BindTagsRequestBody(BaseModel):
    tag_ids: List[str] = []
    target_id: str = ""


class BindTagsRequest(BaseRequest):
    def __init__(self):
        super().__init__()
        self.request_body: BindTagsRequestBody | None = None

    @staticmethod
    def builder() -> BindTagsRequestBuilder:
        return BindTagsRequestBuilder()


class BindTagsRequestBuilder:
    def __init__(self):
        bind_tags_request = BindTagsRequest()
        bind_tags_request.http_method = HttpMethod.POST
        bind_tags_request.uri = "/v1/datasets/tags/binding"
        self._request = bind_tags_request

    def build(self) -> BindTagsRequest:
        return self._request

    def tag_ids(self, tag_ids: List[str]) -> BindTagsRequestBuilder:
        if self._request.request_body is None:
            self._request.request_body = BindTagsRequestBody()
        self._request.request_body.tag_ids = tag_ids
        self._request.body = self._request.request_body.model_dump(exclude_none=True, mode="json")
        return self

    def target_id(self, target_id: str) -> BindTagsRequestBuilder:
        if self._request.request_body is None:
            self._request.request_body = BindTagsRequestBody()
        self._request.request_body.target_id = target_id
        self._request.body = self._request.request_body.model_dump(exclude_none=True, mode="json")
        return self