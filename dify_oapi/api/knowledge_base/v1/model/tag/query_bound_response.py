from __future__ import annotations

from typing import List

from pydantic import BaseModel

from dify_oapi.api.knowledge_base.v1.model.dataset.tag_info import TagInfo


class QueryBoundTagsResponse(BaseModel):
    data: List[TagInfo] = []
    total: int = 0

    @staticmethod
    def builder() -> QueryBoundTagsResponseBuilder:
        return QueryBoundTagsResponseBuilder()


class QueryBoundTagsResponseBuilder:
    def __init__(self):
        self._response = QueryBoundTagsResponse()

    def build(self) -> QueryBoundTagsResponse:
        return self._response

    def data(self, data: List[TagInfo]) -> QueryBoundTagsResponseBuilder:
        self._response.data = data
        return self

    def total(self, total: int) -> QueryBoundTagsResponseBuilder:
        self._response.total = total
        return self

    def add_tag(self, tag: TagInfo) -> QueryBoundTagsResponseBuilder:
        self._response.data.append(tag)
        return self