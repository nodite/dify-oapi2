"""Segment content model for Knowledge Base API."""

from __future__ import annotations

from pydantic import BaseModel


class SegmentContent(BaseModel):
    """Segment content model with builder pattern."""

    content: str | None = None
    answer: str | None = None
    keywords: list[str] | None = None

    @staticmethod
    def builder() -> SegmentContentBuilder:
        return SegmentContentBuilder()


class SegmentContentBuilder:
    """Builder for SegmentContent."""

    def __init__(self) -> None:
        self._segment_content = SegmentContent()

    def build(self) -> SegmentContent:
        return self._segment_content

    def content(self, content: str) -> SegmentContentBuilder:
        self._segment_content.content = content
        return self

    def answer(self, answer: str) -> SegmentContentBuilder:
        self._segment_content.answer = answer
        return self

    def keywords(self, keywords: list[str]) -> SegmentContentBuilder:
        self._segment_content.keywords = keywords
        return self
