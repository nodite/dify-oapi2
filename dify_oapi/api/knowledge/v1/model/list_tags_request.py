from dify_oapi.core.enum import HttpMethod
from dify_oapi.core.model.base_request import BaseRequest

from .knowledge_types import TagType


class ListTagsRequest(BaseRequest):
    def __init__(self):
        super().__init__()

    @staticmethod
    def builder() -> "ListTagsRequestBuilder":
        return ListTagsRequestBuilder()


class ListTagsRequestBuilder:
    def __init__(self):
        list_tags_request = ListTagsRequest()
        list_tags_request.http_method = HttpMethod.GET
        list_tags_request.uri = "/v1/datasets/tags"
        self._list_tags_request = list_tags_request

    def build(self) -> ListTagsRequest:
        return self._list_tags_request

    def type(self, type_value: TagType) -> "ListTagsRequestBuilder":
        self._list_tags_request.add_query("type", type_value)
        return self
