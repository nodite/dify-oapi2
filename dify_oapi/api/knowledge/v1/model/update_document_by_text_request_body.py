"""Update document by text request body model."""

from __future__ import annotations

from pydantic import BaseModel

from .knowledge_types import IndexingTechnique
from .process_rule import ProcessRule


class UpdateDocumentByTextRequestBody(BaseModel):
    """Request body model for update document by text API."""

    name: str | None = None
    text: str | None = None
    indexing_technique: IndexingTechnique | None = None
    process_rule: ProcessRule | None = None

    @staticmethod
    def builder() -> UpdateDocumentByTextRequestBodyBuilder:
        return UpdateDocumentByTextRequestBodyBuilder()


class UpdateDocumentByTextRequestBodyBuilder:
    """Builder for UpdateDocumentByTextRequestBody."""

    def __init__(self) -> None:
        self._update_document_by_text_request_body = UpdateDocumentByTextRequestBody()

    def build(self) -> UpdateDocumentByTextRequestBody:
        return self._update_document_by_text_request_body

    def name(self, name: str) -> UpdateDocumentByTextRequestBodyBuilder:
        self._update_document_by_text_request_body.name = name
        return self

    def text(self, text: str) -> UpdateDocumentByTextRequestBodyBuilder:
        self._update_document_by_text_request_body.text = text
        return self

    def indexing_technique(self, indexing_technique: IndexingTechnique) -> UpdateDocumentByTextRequestBodyBuilder:
        self._update_document_by_text_request_body.indexing_technique = indexing_technique
        return self

    def process_rule(self, process_rule: ProcessRule) -> UpdateDocumentByTextRequestBodyBuilder:
        self._update_document_by_text_request_body.process_rule = process_rule
        return self
