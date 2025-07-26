from __future__ import annotations

from pydantic import BaseModel


class UnbindTagResponse(BaseModel):
    result: str

    @staticmethod
    def builder() -> UnbindTagResponseBuilder:
        return UnbindTagResponseBuilder()


class UnbindTagResponseBuilder:
    def __init__(self):
        self._response = UnbindTagResponse(result="")

    def build(self) -> UnbindTagResponse:
        return self._response

    def result(self, result: str) -> UnbindTagResponseBuilder:
        self._response.result = result
        return self