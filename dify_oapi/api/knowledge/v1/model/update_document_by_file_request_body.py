"""Update document by file request body model."""

from __future__ import annotations

from pydantic import BaseModel

from .knowledge_types import IndexingTechnique
from .process_rule import ProcessRule


class UpdateDocumentByFileRequestBody(BaseModel):
    """Request body model for update document by file API."""

    name: str | None = None
    indexing_technique: IndexingTechnique | None = None
    process_rule: ProcessRule | None = None

    @staticmethod
    def builder() -> UpdateDocumentByFileRequestBodyBuilder:
        return UpdateDocumentByFileRequestBodyBuilder()


class UpdateDocumentByFileRequestBodyBuilder:
    """Builder for UpdateDocumentByFileRequestBody."""

    def __init__(self) -> None:
        self._update_document_by_file_request_body = UpdateDocumentByFileRequestBody()

    def build(self) -> UpdateDocumentByFileRequestBody:
        return self._update_document_by_file_request_body

    def name(self, name: str) -> UpdateDocumentByFileRequestBodyBuilder:
        self._update_document_by_file_request_body.name = name
        return self

    def indexing_technique(self, indexing_technique: IndexingTechnique) -> UpdateDocumentByFileRequestBodyBuilder:
        self._update_document_by_file_request_body.indexing_technique = indexing_technique
        return self

    def process_rule(self, process_rule: ProcessRule) -> UpdateDocumentByFileRequestBodyBuilder:
        self._update_document_by_file_request_body.process_rule = process_rule
        return self
