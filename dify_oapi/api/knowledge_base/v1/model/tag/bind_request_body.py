from __future__ import annotations

from pydantic import BaseModel


class BindRequestBody(BaseModel):
    tag_ids: list[str] = []
    target_id: str = ""

    @staticmethod
    def builder() -> BindRequestBodyBuilder:
        return BindRequestBodyBuilder()


class BindRequestBodyBuilder:
    def __init__(self):
        bind_request_body = BindRequestBody()
        self._request_body = bind_request_body

    def build(self) -> BindRequestBody:
        return self._request_body

    def tag_ids(self, tag_ids: list[str]) -> BindRequestBodyBuilder:
        self._request_body.tag_ids = tag_ids
        return self

    def target_id(self, target_id: str) -> BindRequestBodyBuilder:
        self._request_body.target_id = target_id
        return self
