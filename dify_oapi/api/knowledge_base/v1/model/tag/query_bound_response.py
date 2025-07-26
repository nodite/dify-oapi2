from __future__ import annotations

from typing import List

from pydantic import BaseModel

from dify_oapi.api.knowledge_base.v1.model.dataset.tag_info import TagInfo


class QueryBoundResponse(BaseModel):
    data: List[TagInfo] = []
    total: int = 0

    @staticmethod
    def builder() -> QueryBoundResponseBuilder:
        return QueryBoundResponseBuilder()


class QueryBoundResponseBuilder:
    def __init__(self):
        self._response = QueryBoundResponse()

    def build(self) -> QueryBoundResponse:
        return self._response

    def data(self, data: List[TagInfo]) -> QueryBoundResponseBuilder:
        self._response.data = data
        return self

    def total(self, total: int) -> QueryBoundResponseBuilder:
        self._response.total = total
        return self

    def add_tag(self, tag: TagInfo) -> QueryBoundResponseBuilder:
        self._response.data.append(tag)
        return self