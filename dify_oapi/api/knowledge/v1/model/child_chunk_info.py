"""Child chunk information model for Knowledge Base API."""

from pydantic import BaseModel

from .knowledge_types import ChunkStatus


class ChildChunkInfo(BaseModel):
    """Child chunk information model with builder pattern."""

    id: str | None = None
    segment_id: str | None = None
    content: str | None = None
    word_count: int | None = None
    tokens: int | None = None
    keywords: list[str] | None = None
    index_node_id: str | None = None
    index_node_hash: str | None = None
    status: ChunkStatus | None = None
    created_by: str | None = None
    created_at: float | None = None
    indexing_at: float | None = None
    completed_at: float | None = None
    error: str | None = None
    stopped_at: float | None = None

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

    def segment_id(self, segment_id: str) -> "ChildChunkInfoBuilder":
        self._child_chunk_info.segment_id = segment_id
        return self

    def word_count(self, word_count: int) -> "ChildChunkInfoBuilder":
        self._child_chunk_info.word_count = word_count
        return self

    def tokens(self, tokens: int) -> "ChildChunkInfoBuilder":
        self._child_chunk_info.tokens = tokens
        return self

    def index_node_id(self, index_node_id: str) -> "ChildChunkInfoBuilder":
        self._child_chunk_info.index_node_id = index_node_id
        return self

    def index_node_hash(self, index_node_hash: str) -> "ChildChunkInfoBuilder":
        self._child_chunk_info.index_node_hash = index_node_hash
        return self

    def status(self, status: ChunkStatus) -> "ChildChunkInfoBuilder":
        self._child_chunk_info.status = status
        return self

    def created_by(self, created_by: str) -> "ChildChunkInfoBuilder":
        self._child_chunk_info.created_by = created_by
        return self

    def created_at(self, created_at: float) -> "ChildChunkInfoBuilder":
        self._child_chunk_info.created_at = created_at
        return self

    def indexing_at(self, indexing_at: float) -> "ChildChunkInfoBuilder":
        self._child_chunk_info.indexing_at = indexing_at
        return self

    def completed_at(self, completed_at: float) -> "ChildChunkInfoBuilder":
        self._child_chunk_info.completed_at = completed_at
        return self

    def error(self, error: str) -> "ChildChunkInfoBuilder":
        self._child_chunk_info.error = error
        return self

    def stopped_at(self, stopped_at: float) -> "ChildChunkInfoBuilder":
        self._child_chunk_info.stopped_at = stopped_at
        return self
