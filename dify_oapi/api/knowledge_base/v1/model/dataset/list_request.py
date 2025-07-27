from __future__ import annotations

from dify_oapi.core.enum import HttpMethod
from dify_oapi.core.model.base_request import BaseRequest


class ListRequest(BaseRequest):
    def __init__(self):
        super().__init__()

    @staticmethod
    def builder() -> ListRequestBuilder:
        return ListRequestBuilder()


class ListRequestBuilder:
    def __init__(self):
        list_request = ListRequest()
        list_request.http_method = HttpMethod.GET
        list_request.uri = "/v1/datasets"
        self._list_request = list_request

    def build(self) -> ListRequest:
        return self._list_request

    def keyword(self, keyword: str) -> ListRequestBuilder:
        self._list_request.add_query("keyword", keyword)
        return self

    def tag_ids(self, tag_ids: list[str]) -> ListRequestBuilder:
        for tag_id in tag_ids:
            self._list_request.add_query("tag_ids", tag_id)
        return self

    def page(self, page: int) -> ListRequestBuilder:
        self._list_request.add_query("page", page)
        return self

    def limit(self, limit: str) -> ListRequestBuilder:
        self._list_request.add_query("limit", limit)
        return self

    def include_all(self, include_all: bool) -> ListRequestBuilder:
        self._list_request.add_query("include_all", include_all)
        return self
