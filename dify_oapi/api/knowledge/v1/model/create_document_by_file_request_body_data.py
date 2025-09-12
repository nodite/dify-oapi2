"""Create document by file request body model."""

from __future__ import annotations

from pydantic import BaseModel

from .knowledge_types import DocumentForm, IndexingTechnique
from .process_rule import ProcessRule
from .retrieval_model import RetrievalModel


class CreateDocumentByFileRequestBodyData(BaseModel):
    """Request body model for create document by file API."""

    name: str | None = None
    original_document_id: str | None = None  # UUID for re-upload/modify
    indexing_technique: IndexingTechnique | None = None
    doc_form: DocumentForm | None = None
    doc_language: str | None = None
    process_rule: ProcessRule | None = None
    retrieval_model: RetrievalModel | None = None
    embedding_model: str | None = None
    embedding_model_provider: str | None = None

    @staticmethod
    def builder() -> CreateDocumentByFileRequestBodyDataBuilder:
        return CreateDocumentByFileRequestBodyDataBuilder()


class CreateDocumentByFileRequestBodyDataBuilder:
    """Builder for CreateDocumentByFileRequestBodyData."""

    def __init__(self) -> None:
        self._create_document_by_file_request_body = CreateDocumentByFileRequestBodyData()

    def build(self) -> CreateDocumentByFileRequestBodyData:
        return self._create_document_by_file_request_body

    def name(self, name: str) -> CreateDocumentByFileRequestBodyDataBuilder:
        self._create_document_by_file_request_body.name = name
        return self

    def indexing_technique(self, indexing_technique: IndexingTechnique) -> CreateDocumentByFileRequestBodyDataBuilder:
        self._create_document_by_file_request_body.indexing_technique = indexing_technique
        return self

    def process_rule(self, process_rule: ProcessRule) -> CreateDocumentByFileRequestBodyDataBuilder:
        self._create_document_by_file_request_body.process_rule = process_rule
        return self

    def original_document_id(self, original_document_id: str) -> CreateDocumentByFileRequestBodyDataBuilder:
        self._create_document_by_file_request_body.original_document_id = original_document_id
        return self

    def doc_form(self, doc_form: DocumentForm) -> CreateDocumentByFileRequestBodyDataBuilder:
        self._create_document_by_file_request_body.doc_form = doc_form
        return self

    def doc_language(self, doc_language: str) -> CreateDocumentByFileRequestBodyDataBuilder:
        self._create_document_by_file_request_body.doc_language = doc_language
        return self

    def retrieval_model(self, retrieval_model: RetrievalModel) -> CreateDocumentByFileRequestBodyDataBuilder:
        self._create_document_by_file_request_body.retrieval_model = retrieval_model
        return self

    def embedding_model(self, embedding_model: str) -> CreateDocumentByFileRequestBodyDataBuilder:
        self._create_document_by_file_request_body.embedding_model = embedding_model
        return self

    def embedding_model_provider(self, embedding_model_provider: str) -> CreateDocumentByFileRequestBodyDataBuilder:
        self._create_document_by_file_request_body.embedding_model_provider = embedding_model_provider
        return self
