from __future__ import annotations

from pydantic import BaseModel


class UpdateRequestBody(BaseModel):
    name: str = ""
    tag_id: str = ""

    @staticmethod
    def builder() -> UpdateRequestBodyBuilder:
        return UpdateRequestBodyBuilder()


class UpdateRequestBodyBuilder:
    def __init__(self):
        update_request_body = UpdateRequestBody()
        self._request_body = update_request_body

    def build(self) -> UpdateRequestBody:
        return self._request_body

    def name(self, name: str) -> UpdateRequestBodyBuilder:
        self._request_body.name = name
        return self

    def tag_id(self, tag_id: str) -> UpdateRequestBodyBuilder:
        self._request_body.tag_id = tag_id
        return self
