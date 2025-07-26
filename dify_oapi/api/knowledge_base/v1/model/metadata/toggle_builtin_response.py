from __future__ import annotations

from pydantic import BaseModel


class ToggleBuiltinResponse(BaseModel):
    result: str

    @staticmethod
    def builder() -> ToggleBuiltinResponseBuilder:
        return ToggleBuiltinResponseBuilder()


class ToggleBuiltinResponseBuilder:
    def __init__(self):
        self._response = ToggleBuiltinResponse(result="")

    def build(self) -> ToggleBuiltinResponse:
        return self._response

    def result(self, result: str) -> ToggleBuiltinResponseBuilder:
        self._response.result = result
        return self