from __future__ import annotations

from typing import Optional

from pydantic import BaseModel


class TagInfo(BaseModel):
    id: str
    name: str
    type: Optional[str] = None
    binding_count: Optional[int] = None

    @staticmethod
    def builder() -> TagInfoBuilder:
        return TagInfoBuilder()


class TagInfoBuilder:
    def __init__(self):
        self._tag_info = TagInfo(id="", name="")

    def build(self) -> TagInfo:
        return self._tag_info

    def id(self, id: str) -> TagInfoBuilder:
        self._tag_info.id = id
        return self

    def name(self, name: str) -> TagInfoBuilder:
        self._tag_info.name = name
        return self

    def type(self, type: str) -> TagInfoBuilder:
        self._tag_info.type = type
        return self

    def binding_count(self, binding_count: int) -> TagInfoBuilder:
        self._tag_info.binding_count = binding_count
        return self