from __future__ import annotations

from pydantic import BaseModel


class CreateChildChunkRequestBody(BaseModel):
    content: str | None = None

    @staticmethod
    def builder() -> CreateChildChunkRequestBodyBuilder:
        return CreateChildChunkRequestBodyBuilder()


class CreateChildChunkRequestBodyBuilder:
    def __init__(self):
        self._create_child_chunk_request_body = CreateChildChunkRequestBody()

    def build(self) -> CreateChildChunkRequestBody:
        return self._create_child_chunk_request_body

    def content(self, content: str) -> CreateChildChunkRequestBodyBuilder:
        self._create_child_chunk_request_body.content = content
        return self
