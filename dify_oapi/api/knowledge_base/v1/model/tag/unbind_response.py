from __future__ import annotations

from pydantic import BaseModel


class UnbindResponse(BaseModel):
    result: str

    @staticmethod
    def builder() -> UnbindResponseBuilder:
        return UnbindResponseBuilder()


class UnbindResponseBuilder:
    def __init__(self):
        self._response = UnbindResponse(result="")

    def build(self) -> UnbindResponse:
        return self._response

    def result(self, result: str) -> UnbindResponseBuilder:
        self._response.result = result
        return self