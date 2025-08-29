from __future__ import annotations

from pydantic import BaseModel


class DeleteRequestBody(BaseModel):
    tag_id: str = ""

    @staticmethod
    def builder() -> DeleteRequestBodyBuilder:
        return DeleteRequestBodyBuilder()


class DeleteRequestBodyBuilder:
    def __init__(self):
        delete_request_body = DeleteRequestBody()
        self._request_body = delete_request_body

    def build(self) -> DeleteRequestBody:
        return self._request_body

    def tag_id(self, tag_id: str) -> DeleteRequestBodyBuilder:
        self._request_body.tag_id = tag_id
        return self
