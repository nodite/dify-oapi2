"""Update document by file request body model."""

from __future__ import annotations

from pydantic import BaseModel

from .knowledge_types import IndexingTechnique
from .process_rule import ProcessRule
from .retrieval_model import RetrievalModel


class UpdateDocumentByFileRequestBodyData(BaseModel):
    """Request body model for update document by file API."""

    name: str | None = None
    indexing_technique: IndexingTechnique | None = None
    doc_form: str | None = None
    doc_language: str | None = None
    process_rule: ProcessRule | None = None
    retrieval_model: RetrievalModel | None = None
    embedding_model: str | None = None
    embedding_model_provider: str | None = None

    @staticmethod
    def builder() -> UpdateDocumentByFileRequestBodyDataBuilder:
        return UpdateDocumentByFileRequestBodyDataBuilder()


class UpdateDocumentByFileRequestBodyDataBuilder:
    """Builder for UpdateDocumentByFileRequestBodyData."""

    def __init__(self) -> None:
        self._update_document_by_file_request_body = UpdateDocumentByFileRequestBodyData()

    def build(self) -> UpdateDocumentByFileRequestBodyData:
        return self._update_document_by_file_request_body

    def name(self, name: str) -> UpdateDocumentByFileRequestBodyDataBuilder:
        self._update_document_by_file_request_body.name = name
        return self

    def indexing_technique(self, indexing_technique: IndexingTechnique) -> UpdateDocumentByFileRequestBodyDataBuilder:
        self._update_document_by_file_request_body.indexing_technique = indexing_technique
        return self

    def process_rule(self, process_rule: ProcessRule) -> UpdateDocumentByFileRequestBodyDataBuilder:
        self._update_document_by_file_request_body.process_rule = process_rule
        return self

    def doc_form(self, doc_form: str) -> UpdateDocumentByFileRequestBodyDataBuilder:
        self._update_document_by_file_request_body.doc_form = doc_form
        return self

    def doc_language(self, doc_language: str) -> UpdateDocumentByFileRequestBodyDataBuilder:
        self._update_document_by_file_request_body.doc_language = doc_language
        return self

    def retrieval_model(self, retrieval_model: RetrievalModel) -> UpdateDocumentByFileRequestBodyDataBuilder:
        self._update_document_by_file_request_body.retrieval_model = retrieval_model
        return self

    def embedding_model(self, embedding_model: str) -> UpdateDocumentByFileRequestBodyDataBuilder:
        self._update_document_by_file_request_body.embedding_model = embedding_model
        return self

    def embedding_model_provider(self, embedding_model_provider: str) -> UpdateDocumentByFileRequestBodyDataBuilder:
        self._update_document_by_file_request_body.embedding_model_provider = embedding_model_provider
        return self
