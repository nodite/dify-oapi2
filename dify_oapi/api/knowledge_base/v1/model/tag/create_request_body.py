from __future__ import annotations

from pydantic import BaseModel


class CreateRequestBody(BaseModel):
    name: str = ""

    @staticmethod
    def builder() -> CreateRequestBodyBuilder:
        return CreateRequestBodyBuilder()


class CreateRequestBodyBuilder:
    def __init__(self):
        create_request_body = CreateRequestBody()
        self._request_body = create_request_body

    def build(self) -> CreateRequestBody:
        return self._request_body

    def name(self, name: str) -> CreateRequestBodyBuilder:
        self._request_body.name = name
        return self
