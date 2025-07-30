from __future__ import annotations

from pydantic import BaseModel


class Segment(BaseModel):
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
    def builder() -> SegmentBuilder:
        return SegmentBuilder()


class SegmentBuilder:
    def __init__(self):
        self._segment = Segment()

    def build(self) -> Segment:
        return self._segment

    def id(self, id: str) -> SegmentBuilder:
        self._segment.id = id
        return self

    def position(self, position: int) -> SegmentBuilder:
        self._segment.position = position
        return self

    def document_id(self, document_id: str) -> SegmentBuilder:
        self._segment.document_id = document_id
        return self

    def content(self, content: str) -> SegmentBuilder:
        self._segment.content = content
        return self

    def answer(self, answer: str) -> SegmentBuilder:
        self._segment.answer = answer
        return self

    def word_count(self, word_count: int) -> SegmentBuilder:
        self._segment.word_count = word_count
        return self

    def tokens(self, tokens: int) -> SegmentBuilder:
        self._segment.tokens = tokens
        return self

    def keywords(self, keywords: list[str]) -> SegmentBuilder:
        self._segment.keywords = keywords
        return self

    def index_node_id(self, index_node_id: str) -> SegmentBuilder:
        self._segment.index_node_id = index_node_id
        return self

    def index_node_hash(self, index_node_hash: str) -> SegmentBuilder:
        self._segment.index_node_hash = index_node_hash
        return self

    def hit_count(self, hit_count: int) -> SegmentBuilder:
        self._segment.hit_count = hit_count
        return self

    def enabled(self, enabled: bool) -> SegmentBuilder:
        self._segment.enabled = enabled
        return self

    def disabled_at(self, disabled_at: int) -> SegmentBuilder:
        self._segment.disabled_at = disabled_at
        return self

    def disabled_by(self, disabled_by: str) -> SegmentBuilder:
        self._segment.disabled_by = disabled_by
        return self

    def status(self, status: str) -> SegmentBuilder:
        self._segment.status = status
        return self

    def created_by(self, created_by: str) -> SegmentBuilder:
        self._segment.created_by = created_by
        return self

    def created_at(self, created_at: int) -> SegmentBuilder:
        self._segment.created_at = created_at
        return self

    def indexing_at(self, indexing_at: int) -> SegmentBuilder:
        self._segment.indexing_at = indexing_at
        return self

    def completed_at(self, completed_at: int) -> SegmentBuilder:
        self._segment.completed_at = completed_at
        return self

    def error(self, error: str) -> SegmentBuilder:
        self._segment.error = error
        return self

    def stopped_at(self, stopped_at: int) -> SegmentBuilder:
        self._segment.stopped_at = stopped_at
        return self
