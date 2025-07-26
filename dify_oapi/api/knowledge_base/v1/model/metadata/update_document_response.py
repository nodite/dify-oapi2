from __future__ import annotations

from pydantic import BaseModel


class UpdateDocumentMetadataResponse(BaseModel):
    result: str

    @staticmethod
    def builder() -> UpdateDocumentMetadataResponseBuilder:
        return UpdateDocumentMetadataResponseBuilder()


class UpdateDocumentMetadataResponseBuilder:
    def __init__(self):
        self._response = UpdateDocumentMetadataResponse(result="")

    def build(self) -> UpdateDocumentMetadataResponse:
        return self._response

    def result(self, result: str) -> UpdateDocumentMetadataResponseBuilder:
        self._response.result = result
        return self