from __future__ import annotations

from dify_oapi.core.enum import HttpMethod
from dify_oapi.core.model.base_request import BaseRequest


class ListAnnotationsRequest(BaseRequest):
    def __init__(self):
        super().__init__()

    @staticmethod
    def builder() -> ListAnnotationsRequestBuilder:
        return ListAnnotationsRequestBuilder()


class ListAnnotationsRequestBuilder:
    def __init__(self):
        list_annotations_request = ListAnnotationsRequest()
        list_annotations_request.http_method = HttpMethod.GET
        list_annotations_request.uri = "/v1/apps/annotations"
        self._list_annotations_request = list_annotations_request

    def build(self) -> ListAnnotationsRequest:
        return self._list_annotations_request

    def page(self, page: str) -> ListAnnotationsRequestBuilder:
        self._list_annotations_request.add_query("page", page)
        return self

    def limit(self, limit: str) -> ListAnnotationsRequestBuilder:
        self._list_annotations_request.add_query("limit", limit)
        return self
