"""Tag information model for Knowledge Base API."""

from typing import Optional

from pydantic import BaseModel

from .knowledge_types import TagType


class TagInfo(BaseModel):
    """Tag information model with builder pattern."""

    id: Optional[str] = None
    name: Optional[str] = None
    type: Optional[TagType] = None
    created_by: Optional[str] = None
    created_at: Optional[int] = None

    @staticmethod
    def builder() -> "TagInfoBuilder":
        return TagInfoBuilder()


class TagInfoBuilder:
    """Builder for TagInfo."""

    def __init__(self):
        self._tag_info = TagInfo()

    def build(self) -> TagInfo:
        return self._tag_info

    def id(self, id: str) -> "TagInfoBuilder":
        self._tag_info.id = id
        return self

    def name(self, name: str) -> "TagInfoBuilder":
        self._tag_info.name = name
        return self

    def type(self, type: TagType) -> "TagInfoBuilder":
        self._tag_info.type = type
        return self

    def created_by(self, created_by: str) -> "TagInfoBuilder":
        self._tag_info.created_by = created_by
        return self

    def created_at(self, created_at: int) -> "TagInfoBuilder":
        self._tag_info.created_at = created_at
        return self
