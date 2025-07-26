from __future__ import annotations

from typing import Optional

from pydantic import BaseModel

from dify_oapi.api.knowledge_base.v1.model.dataset.tag_info import TagInfo


class CreateTagResponse(BaseModel):
    id: str
    name: str
    type: str
    binding_count: int

    @staticmethod
    def builder() -> CreateTagResponseBuilder:
        return CreateTagResponseBuilder()

    def to_tag_info(self) -> TagInfo:
        return TagInfo(id=self.id, name=self.name, type=self.type, binding_count=self.binding_count)


class CreateTagResponseBuilder:
    def __init__(self):
        self._response = CreateTagResponse(id="", name="", type="", binding_count=0)

    def build(self) -> CreateTagResponse:
        return self._response

    def id(self, id: str) -> CreateTagResponseBuilder:
        self._response.id = id
        return self

    def name(self, name: str) -> CreateTagResponseBuilder:
        self._response.name = name
        return self

    def type(self, type: str) -> CreateTagResponseBuilder:
        self._response.type = type
        return self

    def binding_count(self, binding_count: int) -> CreateTagResponseBuilder:
        self._response.binding_count = binding_count
        return self