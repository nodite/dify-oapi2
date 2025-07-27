from __future__ import annotations

from pydantic import BaseModel


class UnbindRequestBody(BaseModel):
    tag_id: str = ""
    target_id: str = ""

    @staticmethod
    def builder() -> UnbindRequestBodyBuilder:
        return UnbindRequestBodyBuilder()


class UnbindRequestBodyBuilder:
    def __init__(self):
        unbind_request_body = UnbindRequestBody()
        self._request_body = unbind_request_body

    def build(self) -> UnbindRequestBody:
        return self._request_body

    def tag_id(self, tag_id: str) -> UnbindRequestBodyBuilder:
        self._request_body.tag_id = tag_id
        return self

    def target_id(self, target_id: str) -> UnbindRequestBodyBuilder:
        self._request_body.target_id = target_id
        return self
