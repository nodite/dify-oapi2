from __future__ import annotations

from pydantic import BaseModel


class UpdateRequestBody(BaseModel):
    name: str | None = None

    @staticmethod
    def builder() -> UpdateRequestBodyBuilder:
        return UpdateRequestBodyBuilder()


class UpdateRequestBodyBuilder:
    def __init__(self):
        update_request_body = UpdateRequestBody()
        self._update_request_body = update_request_body

    def build(self) -> UpdateRequestBody:
        return self._update_request_body

    def name(self, name: str) -> UpdateRequestBodyBuilder:
        self._update_request_body.name = name
        return self
