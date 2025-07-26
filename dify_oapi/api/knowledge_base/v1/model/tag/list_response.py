from __future__ import annotations

from typing import List

from pydantic import BaseModel

from dify_oapi.api.knowledge_base.v1.model.dataset.tag_info import TagInfo


class ListTagsResponse(BaseModel):
    data: List[TagInfo] = []

    @staticmethod
    def builder() -> ListTagsResponseBuilder:
        return ListTagsResponseBuilder()


class ListTagsResponseBuilder:
    def __init__(self):
        self._response = ListTagsResponse()

    def build(self) -> ListTagsResponse:
        return self._response

    def data(self, data: List[TagInfo]) -> ListTagsResponseBuilder:
        self._response.data = data
        return self

    def add_tag(self, tag: TagInfo) -> ListTagsResponseBuilder:
        self._response.data.append(tag)
        return self