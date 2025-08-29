"""Create child chunk request body model."""

from __future__ import annotations

from pydantic import BaseModel

from .child_chunk_content import ChildChunkContent


class CreateChildChunkRequestBody(BaseModel):
    """Request body model for create child chunk API."""

    chunks: list[ChildChunkContent] | None = None

    @staticmethod
    def builder() -> CreateChildChunkRequestBodyBuilder:
        return CreateChildChunkRequestBodyBuilder()


class CreateChildChunkRequestBodyBuilder:
    """Builder for CreateChildChunkRequestBody."""

    def __init__(self) -> None:
        self._create_child_chunk_request_body = CreateChildChunkRequestBody()

    def build(self) -> CreateChildChunkRequestBody:
        return self._create_child_chunk_request_body

    def chunks(self, chunks: list[ChildChunkContent]) -> CreateChildChunkRequestBodyBuilder:
        self._create_child_chunk_request_body.chunks = chunks
        return self
