from __future__ import annotations

from pydantic import BaseModel


class SegmentInfo(BaseModel):
    id: str | None = None
    position: int | None = None
    document_id: str | None = None
    content: str | None = None
    answer: str | None = None
    word_count: int | None = None
    tokens: int | None = None
    keywords: list[str] | None = None
    index_node_id: str | None = None
    index_node_hash: str | None = None
    hit_count: int | None = None
    enabled: bool | None = None
    disabled_at: int | None = None
    disabled_by: str | None = None
    status: str | None = None
    created_by: str | None = None
    created_at: int | None = None
    indexing_at: int | None = None
    completed_at: int | None = None
    error: str | None = None
    stopped_at: int | None = None

    @staticmethod
    def builder() -> SegmentInfoBuilder:
        return SegmentInfoBuilder()


class SegmentInfoBuilder:
    def __init__(self):
        self._segment_info = SegmentInfo()

    def build(self) -> SegmentInfo:
        return self._segment_info

    def id(self, id: str) -> SegmentInfoBuilder:
        self._segment_info.id = id
        return self

    def position(self, position: int) -> SegmentInfoBuilder:
        self._segment_info.position = position
        return self

    def document_id(self, document_id: str) -> SegmentInfoBuilder:
        self._segment_info.document_id = document_id
        return self

    def content(self, content: str) -> SegmentInfoBuilder:
        self._segment_info.content = content
        return self

    def answer(self, answer: str) -> SegmentInfoBuilder:
        self._segment_info.answer = answer
        return self

    def word_count(self, word_count: int) -> SegmentInfoBuilder:
        self._segment_info.word_count = word_count
        return self

    def tokens(self, tokens: int) -> SegmentInfoBuilder:
        self._segment_info.tokens = tokens
        return self

    def keywords(self, keywords: list[str]) -> SegmentInfoBuilder:
        self._segment_info.keywords = keywords
        return self

    def index_node_id(self, index_node_id: str) -> SegmentInfoBuilder:
        self._segment_info.index_node_id = index_node_id
        return self

    def index_node_hash(self, index_node_hash: str) -> SegmentInfoBuilder:
        self._segment_info.index_node_hash = index_node_hash
        return self

    def hit_count(self, hit_count: int) -> SegmentInfoBuilder:
        self._segment_info.hit_count = hit_count
        return self

    def enabled(self, enabled: bool) -> SegmentInfoBuilder:
        self._segment_info.enabled = enabled
        return self

    def disabled_at(self, disabled_at: int) -> SegmentInfoBuilder:
        self._segment_info.disabled_at = disabled_at
        return self

    def disabled_by(self, disabled_by: str) -> SegmentInfoBuilder:
        self._segment_info.disabled_by = disabled_by
        return self

    def status(self, status: str) -> SegmentInfoBuilder:
        self._segment_info.status = status
        return self

    def created_by(self, created_by: str) -> SegmentInfoBuilder:
        self._segment_info.created_by = created_by
        return self

    def created_at(self, created_at: int) -> SegmentInfoBuilder:
        self._segment_info.created_at = created_at
        return self

    def indexing_at(self, indexing_at: int) -> SegmentInfoBuilder:
        self._segment_info.indexing_at = indexing_at
        return self

    def completed_at(self, completed_at: int) -> SegmentInfoBuilder:
        self._segment_info.completed_at = completed_at
        return self

    def error(self, error: str) -> SegmentInfoBuilder:
        self._segment_info.error = error
        return self

    def stopped_at(self, stopped_at: int) -> SegmentInfoBuilder:
        self._segment_info.stopped_at = stopped_at
        return self
