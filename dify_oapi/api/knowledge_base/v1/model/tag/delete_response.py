from __future__ import annotations

from pydantic import BaseModel


class DeleteResponse(BaseModel):
    result: str

    @staticmethod
    def builder() -> DeleteResponseBuilder:
        return DeleteResponseBuilder()


class DeleteResponseBuilder:
    def __init__(self):
        self._response = DeleteResponse(result="")

    def build(self) -> DeleteResponse:
        return self._response

    def result(self, result: str) -> DeleteResponseBuilder:
        self._response.result = result
        return self