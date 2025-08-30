"""Create child chunk request body model."""

from __future__ import annotations

from pydantic import BaseModel


class ChunkContent(BaseModel):
    """Individual chunk content for creation."""

    content: str | None = None
    keywords: list[str] | None = None


class CreateChildChunkRequestBody(BaseModel):
    """Request body model for create child chunk API."""

    chunks: list[ChunkContent] | None = None

    @staticmethod
    def builder() -> CreateChildChunkRequestBodyBuilder:
        return CreateChildChunkRequestBodyBuilder()


class CreateChildChunkRequestBodyBuilder:
    """Builder for CreateChildChunkRequestBody."""

    def __init__(self) -> None:
        self._create_child_chunk_request_body = CreateChildChunkRequestBody()

    def build(self) -> CreateChildChunkRequestBody:
        return self._create_child_chunk_request_body

    def chunks(self, chunks: list[ChunkContent]) -> CreateChildChunkRequestBodyBuilder:
        self._create_child_chunk_request_body.chunks = chunks
        return self

    def add_chunk(self, content: str, keywords: list[str] | None = None) -> CreateChildChunkRequestBodyBuilder:
        """Convenience method to add a single chunk."""
        chunk = ChunkContent(content=content, keywords=keywords)
        if self._create_child_chunk_request_body.chunks is None:
            self._create_child_chunk_request_body.chunks = []
        self._create_child_chunk_request_body.chunks.append(chunk)
        return self
