from __future__ import annotations

from pydantic import BaseModel


class BindResponse(BaseModel):
    result: str

    @staticmethod
    def builder() -> BindResponseBuilder:
        return BindResponseBuilder()


class BindResponseBuilder:
    def __init__(self):
        self._response = BindResponse(result="")

    def build(self) -> BindResponse:
        return self._response

    def result(self, result: str) -> BindResponseBuilder:
        self._response.result = result
        return self