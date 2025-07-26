from __future__ import annotations

from typing import List

from pydantic import BaseModel

from dify_oapi.api.knowledge_base.v1.model.dataset.tag_info import TagInfo


class ListResponse(BaseModel):
    data: List[TagInfo] = []

    @staticmethod
    def builder() -> ListResponseBuilder:
        return ListResponseBuilder()


class ListResponseBuilder:
    def __init__(self):
        self._response = ListResponse()

    def build(self) -> ListResponse:
        return self._response

    def data(self, data: List[TagInfo]) -> ListResponseBuilder:
        self._response.data = data
        return self

    def add_tag(self, tag: TagInfo) -> ListResponseBuilder:
        self._response.data.append(tag)
        return self