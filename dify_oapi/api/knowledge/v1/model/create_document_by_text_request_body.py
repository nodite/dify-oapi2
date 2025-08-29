"""Create document by text request body model."""

from __future__ import annotations

from pydantic import BaseModel

from .knowledge_types import IndexingTechnique
from .process_rule import ProcessRule


class CreateDocumentByTextRequestBody(BaseModel):
    """Request body model for create document by text API."""

    name: str | None = None
    text: str | None = None
    indexing_technique: IndexingTechnique | None = None
    process_rule: ProcessRule | None = None

    @staticmethod
    def builder() -> CreateDocumentByTextRequestBodyBuilder:
        return CreateDocumentByTextRequestBodyBuilder()


class CreateDocumentByTextRequestBodyBuilder:
    """Builder for CreateDocumentByTextRequestBody."""

    def __init__(self) -> None:
        self._create_document_by_text_request_body = CreateDocumentByTextRequestBody()

    def build(self) -> CreateDocumentByTextRequestBody:
        return self._create_document_by_text_request_body

    def name(self, name: str) -> CreateDocumentByTextRequestBodyBuilder:
        self._create_document_by_text_request_body.name = name
        return self

    def text(self, text: str) -> CreateDocumentByTextRequestBodyBuilder:
        self._create_document_by_text_request_body.text = text
        return self

    def indexing_technique(self, indexing_technique: IndexingTechnique) -> CreateDocumentByTextRequestBodyBuilder:
        self._create_document_by_text_request_body.indexing_technique = indexing_technique
        return self

    def process_rule(self, process_rule: ProcessRule) -> CreateDocumentByTextRequestBodyBuilder:
        self._create_document_by_text_request_body.process_rule = process_rule
        return self
