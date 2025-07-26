from __future__ import annotations

from pydantic import BaseModel


class UpdateDocumentResponse(BaseModel):
    result: str

    @staticmethod
    def builder() -> UpdateDocumentResponseBuilder:
        return UpdateDocumentResponseBuilder()


class UpdateDocumentResponseBuilder:
    def __init__(self):
        self._response = UpdateDocumentResponse(result="")

    def build(self) -> UpdateDocumentResponse:
        return self._response

    def result(self, result: str) -> UpdateDocumentResponseBuilder:
        self._response.result = result
        return self