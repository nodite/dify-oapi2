"""Create document by file request body model."""

from __future__ import annotations

from pydantic import BaseModel

from .knowledge_types import IndexingTechnique
from .process_rule import ProcessRule


class CreateDocumentByFileRequestBody(BaseModel):
    """Request body model for create document by file API."""

    name: str | None = None
    indexing_technique: IndexingTechnique | None = None
    process_rule: ProcessRule | None = None

    @staticmethod
    def builder() -> CreateDocumentByFileRequestBodyBuilder:
        return CreateDocumentByFileRequestBodyBuilder()


class CreateDocumentByFileRequestBodyBuilder:
    """Builder for CreateDocumentByFileRequestBody."""

    def __init__(self) -> None:
        self._create_document_by_file_request_body = CreateDocumentByFileRequestBody()

    def build(self) -> CreateDocumentByFileRequestBody:
        return self._create_document_by_file_request_body

    def name(self, name: str) -> CreateDocumentByFileRequestBodyBuilder:
        self._create_document_by_file_request_body.name = name
        return self

    def indexing_technique(self, indexing_technique: IndexingTechnique) -> CreateDocumentByFileRequestBodyBuilder:
        self._create_document_by_file_request_body.indexing_technique = indexing_technique
        return self

    def process_rule(self, process_rule: ProcessRule) -> CreateDocumentByFileRequestBodyBuilder:
        self._create_document_by_file_request_body.process_rule = process_rule
        return self
