from __future__ import annotations

from pydantic import BaseModel


class UpdateChildChunkRequestBody(BaseModel):
    content: str | None = None

    @staticmethod
    def builder() -> UpdateChildChunkRequestBodyBuilder:
        return UpdateChildChunkRequestBodyBuilder()


class UpdateChildChunkRequestBodyBuilder:
    def __init__(self):
        self._update_child_chunk_request_body = UpdateChildChunkRequestBody()

    def build(self) -> UpdateChildChunkRequestBody:
        return self._update_child_chunk_request_body

    def content(self, content: str) -> UpdateChildChunkRequestBodyBuilder:
        self._update_child_chunk_request_body.content = content
        return self
