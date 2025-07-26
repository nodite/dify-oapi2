from __future__ import annotations

from pydantic import BaseModel


class CreateRequestBody(BaseModel):
    type: str | None = None
    name: str | None = None

    @staticmethod
    def builder() -> CreateRequestBodyBuilder:
        return CreateRequestBodyBuilder()


class CreateRequestBodyBuilder:
    def __init__(self):
        create_request_body = CreateRequestBody()
        self._create_request_body = create_request_body

    def build(self) -> CreateRequestBody:
        return self._create_request_body

    def type(self, type: str) -> CreateRequestBodyBuilder:
        self._create_request_body.type = type
        return self

    def name(self, name: str) -> CreateRequestBodyBuilder:
        self._create_request_body.name = name
        return self