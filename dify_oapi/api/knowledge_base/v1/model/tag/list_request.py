from __future__ import annotations

from dify_oapi.core.enum import HttpMethod
from dify_oapi.core.model.base_request import BaseRequest


class ListTagsRequest(BaseRequest):
    def __init__(self):
        super().__init__()

    @staticmethod
    def builder() -> ListTagsRequestBuilder:
        return ListTagsRequestBuilder()


class ListTagsRequestBuilder:
    def __init__(self):
        list_tags_request = ListTagsRequest()
        list_tags_request.http_method = HttpMethod.GET
        list_tags_request.uri = "/v1/datasets/tags"
        self._request = list_tags_request

    def build(self) -> ListTagsRequest:
        return self._request