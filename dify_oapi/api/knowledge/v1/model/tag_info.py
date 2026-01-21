"""Tag information model for Knowledge Base API."""

from pydantic import BaseModel

from .knowledge_types import TagType


class TagInfo(BaseModel):
    """Tag information model with builder pattern."""

    id: str | None = None
    name: str | None = None
    type: TagType | None = None
    binding_count: int | None = None
    created_by: str | None = None
    created_at: float | None = None

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

    def created_at(self, created_at: float) -> "TagInfoBuilder":
        self._tag_info.created_at = created_at
        return self

    def binding_count(self, binding_count: int) -> "TagInfoBuilder":
        self._tag_info.binding_count = binding_count
        return self
