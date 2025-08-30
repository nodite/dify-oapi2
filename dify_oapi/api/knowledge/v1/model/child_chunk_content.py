"""Child chunk content model for Knowledge Base API."""

from __future__ import annotations

from pydantic import BaseModel


class ChildChunkContent(BaseModel):
    """Child chunk content model with builder pattern."""

    content: str | None = None
    keywords: list[str] | None = None

    @staticmethod
    def builder() -> ChildChunkContentBuilder:
        return ChildChunkContentBuilder()


class ChildChunkContentBuilder:
    """Builder for ChildChunkContent."""

    def __init__(self) -> None:
        self._child_chunk_content = ChildChunkContent()

    def build(self) -> ChildChunkContent:
        return self._child_chunk_content

    def content(self, content: str) -> ChildChunkContentBuilder:
        self._child_chunk_content.content = content
        return self

    def keywords(self, keywords: list[str]) -> ChildChunkContentBuilder:
        self._child_chunk_content.keywords = keywords
        return self
