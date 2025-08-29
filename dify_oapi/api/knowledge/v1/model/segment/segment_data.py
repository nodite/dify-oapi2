from __future__ import annotations

from pydantic import BaseModel


class SegmentData(BaseModel):
    content: str | None = None
    answer: str | None = None
    keywords: list[str] | None = None
    enabled: bool | None = None
    regenerate_child_chunks: bool | None = None

    @staticmethod
    def builder() -> SegmentDataBuilder:
        return SegmentDataBuilder()


class SegmentDataBuilder:
    def __init__(self):
        self._segment_data = SegmentData()

    def build(self) -> SegmentData:
        return self._segment_data

    def content(self, content: str) -> SegmentDataBuilder:
        self._segment_data.content = content
        return self

    def answer(self, answer: str) -> SegmentDataBuilder:
        self._segment_data.answer = answer
        return self

    def keywords(self, keywords: list[str]) -> SegmentDataBuilder:
        self._segment_data.keywords = keywords
        return self

    def enabled(self, enabled: bool) -> SegmentDataBuilder:
        self._segment_data.enabled = enabled
        return self

    def regenerate_child_chunks(self, regenerate_child_chunks: bool) -> SegmentDataBuilder:
        self._segment_data.regenerate_child_chunks = regenerate_child_chunks
        return self
