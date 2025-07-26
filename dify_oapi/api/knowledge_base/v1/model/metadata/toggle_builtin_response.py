from __future__ import annotations

from pydantic import BaseModel


class ToggleBuiltinMetadataResponse(BaseModel):
    result: str

    @staticmethod
    def builder() -> ToggleBuiltinMetadataResponseBuilder:
        return ToggleBuiltinMetadataResponseBuilder()


class ToggleBuiltinMetadataResponseBuilder:
    def __init__(self):
        self._response = ToggleBuiltinMetadataResponse(result="")

    def build(self) -> ToggleBuiltinMetadataResponse:
        return self._response

    def result(self, result: str) -> ToggleBuiltinMetadataResponseBuilder:
        self._response.result = result
        return self