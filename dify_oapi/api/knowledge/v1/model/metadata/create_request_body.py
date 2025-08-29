from __future__ import annotations

from typing import Literal

from pydantic import BaseModel


class CreateRequestBody(BaseModel):
    type: Literal["string", "number", "time"] | None = None
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

    def type(self, type: Literal["string", "number", "time"]) -> CreateRequestBodyBuilder:
        self._create_request_body.type = type
        return self

    def name(self, name: str) -> CreateRequestBodyBuilder:
        self._create_request_body.name = name
        return self
