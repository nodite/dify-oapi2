from __future__ import annotations

from typing import List

from pydantic import BaseModel

from .dataset_info import DatasetInfo


class ListResponse(BaseModel):
    data: List[DatasetInfo]
    has_more: bool
    limit: int
    total: int
    page: int

    @staticmethod
    def builder() -> ListResponseBuilder:
        return ListResponseBuilder()


class ListResponseBuilder:
    def __init__(self):
        self._response = ListResponse(
            data=[],
            has_more=False,
            limit=20,
            total=0,
            page=1
        )

    def build(self) -> ListResponse:
        return self._response

    def data(self, data: List[DatasetInfo]) -> ListResponseBuilder:
        self._response.data = data
        return self

    def has_more(self, has_more: bool) -> ListResponseBuilder:
        self._response.has_more = has_more
        return self

    def limit(self, limit: int) -> ListResponseBuilder:
        self._response.limit = limit
        return self

    def total(self, total: int) -> ListResponseBuilder:
        self._response.total = total
        return self

    def page(self, page: int) -> ListResponseBuilder:
        self._response.page = page
        return self