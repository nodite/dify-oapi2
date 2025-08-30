"""Child chunk information model for Knowledge Base API."""

from typing import Optional

from pydantic import BaseModel


class ChildChunkInfo(BaseModel):
    """Child chunk information model with builder pattern."""

    id: Optional[str] = None
    content: Optional[str] = None
    keywords: Optional[list[str]] = None
    created_at: Optional[int] = None

    @staticmethod
    def builder() -> "ChildChunkInfoBuilder":
        return ChildChunkInfoBuilder()


class ChildChunkInfoBuilder:
    """Builder for ChildChunkInfo."""

    def __init__(self):
        self._child_chunk_info = ChildChunkInfo()

    def build(self) -> ChildChunkInfo:
        return self._child_chunk_info

    def id(self, id: str) -> "ChildChunkInfoBuilder":
        self._child_chunk_info.id = id
        return self

    def content(self, content: str) -> "ChildChunkInfoBuilder":
        self._child_chunk_info.content = content
        return self

    def keywords(self, keywords: list[str]) -> "ChildChunkInfoBuilder":
        self._child_chunk_info.keywords = keywords
        return self

    def created_at(self, created_at: int) -> "ChildChunkInfoBuilder":
        self._child_chunk_info.created_at = created_at
        return self
