"""Child chunk information model for Knowledge Base API."""

from typing import Optional

from pydantic import BaseModel


class ChildChunkInfo(BaseModel):
    """Child chunk information model with builder pattern."""

    id: Optional[str] = None
    content: Optional[str] = None
    position: Optional[int] = None
    word_count: Optional[int] = None
    tokens: Optional[int] = None
    keywords: Optional[list[str]] = None
    index_node_id: Optional[str] = None
    index_node_hash: Optional[str] = None
    hit_count: Optional[int] = None
    created_by: Optional[str] = None
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

    def position(self, position: int) -> "ChildChunkInfoBuilder":
        self._child_chunk_info.position = position
        return self

    def word_count(self, word_count: int) -> "ChildChunkInfoBuilder":
        self._child_chunk_info.word_count = word_count
        return self

    def tokens(self, tokens: int) -> "ChildChunkInfoBuilder":
        self._child_chunk_info.tokens = tokens
        return self

    def keywords(self, keywords: list[str]) -> "ChildChunkInfoBuilder":
        self._child_chunk_info.keywords = keywords
        return self

    def index_node_id(self, index_node_id: str) -> "ChildChunkInfoBuilder":
        self._child_chunk_info.index_node_id = index_node_id
        return self

    def index_node_hash(self, index_node_hash: str) -> "ChildChunkInfoBuilder":
        self._child_chunk_info.index_node_hash = index_node_hash
        return self

    def hit_count(self, hit_count: int) -> "ChildChunkInfoBuilder":
        self._child_chunk_info.hit_count = hit_count
        return self

    def created_by(self, created_by: str) -> "ChildChunkInfoBuilder":
        self._child_chunk_info.created_by = created_by
        return self

    def created_at(self, created_at: int) -> "ChildChunkInfoBuilder":
        self._child_chunk_info.created_at = created_at
        return self
