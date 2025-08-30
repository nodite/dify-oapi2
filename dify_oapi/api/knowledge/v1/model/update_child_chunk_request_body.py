"""Update child chunk request body model."""

from __future__ import annotations

from pydantic import BaseModel


class UpdateChildChunkRequestBody(BaseModel):
    """Request body model for update child chunk API."""

    content: str | None = None
    keywords: list[str] | None = None

    @staticmethod
    def builder() -> UpdateChildChunkRequestBodyBuilder:
        return UpdateChildChunkRequestBodyBuilder()


class UpdateChildChunkRequestBodyBuilder:
    """Builder for UpdateChildChunkRequestBody."""

    def __init__(self) -> None:
        self._update_child_chunk_request_body = UpdateChildChunkRequestBody()

    def build(self) -> UpdateChildChunkRequestBody:
        return self._update_child_chunk_request_body

    def content(self, content: str) -> UpdateChildChunkRequestBodyBuilder:
        self._update_child_chunk_request_body.content = content
        return self

    def keywords(self, keywords: list[str]) -> UpdateChildChunkRequestBodyBuilder:
        self._update_child_chunk_request_body.keywords = keywords
        return self
