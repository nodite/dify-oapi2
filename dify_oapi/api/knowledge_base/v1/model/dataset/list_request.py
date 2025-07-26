from __future__ import annotations

from typing import Optional, List

from pydantic import BaseModel


class ListDatasetsRequest(BaseModel):
    keyword: Optional[str] = None
    tag_ids: Optional[List[str]] = None
    page: Optional[int] = None
    limit: Optional[str] = None
    include_all: Optional[bool] = None

    @staticmethod
    def builder() -> ListDatasetsRequestBuilder:
        return ListDatasetsRequestBuilder()


class ListDatasetsRequestBuilder:
    def __init__(self):
        self._request = ListDatasetsRequest()

    def build(self) -> ListDatasetsRequest:
        return self._request

    def keyword(self, keyword: str) -> ListDatasetsRequestBuilder:
        self._request.keyword = keyword
        return self

    def tag_ids(self, tag_ids: List[str]) -> ListDatasetsRequestBuilder:
        self._request.tag_ids = tag_ids
        return self

    def page(self, page: int) -> ListDatasetsRequestBuilder:
        self._request.page = page
        return self

    def limit(self, limit: str) -> ListDatasetsRequestBuilder:
        self._request.limit = limit
        return self

    def include_all(self, include_all: bool) -> ListDatasetsRequestBuilder:
        self._request.include_all = include_all
        return self