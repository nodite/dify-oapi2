"""Create document by file request body model."""

from __future__ import annotations

from typing import Literal

from pydantic import BaseModel

from .process_rule import ProcessRule
from .retrieval_model import RetrievalModel


class CreateByFileRequestBodyData(BaseModel):
    """Request body model for create document by file API."""

    file: str | None = None
    original_document_id: str | None = None
    indexing_technique: str | None = None
    doc_form: str | None = None
    doc_language: str | None = None
    process_rule: ProcessRule | None = None
    retrieval_model: RetrievalModel | None = None
    embedding_model: str | None = None
    embedding_model_provider: str | None = None

    @staticmethod
    def builder() -> CreateByFileRequestBodyBuilder:
        return CreateByFileRequestBodyBuilder()


class CreateByFileRequestBodyBuilder:
    """Builder for CreateByFileRequestBody."""

    def __init__(self) -> None:
        self._create_by_file_request_body_data = CreateByFileRequestBodyData()

    def build(self) -> CreateByFileRequestBodyData:
        return self._create_by_file_request_body_data

    def file(self, file: str) -> CreateByFileRequestBodyBuilder:
        self._create_by_file_request_body_data.file = file
        return self

    def original_document_id(self, original_document_id: str) -> CreateByFileRequestBodyBuilder:
        self._create_by_file_request_body_data.original_document_id = original_document_id
        return self

    def indexing_technique(
        self, indexing_technique: Literal["high_quality", "economy"]
    ) -> CreateByFileRequestBodyBuilder:
        self._create_by_file_request_body_data.indexing_technique = indexing_technique
        return self

    def doc_form(
        self, doc_form: Literal["text_model", "hierarchical_model", "qa_model"]
    ) -> CreateByFileRequestBodyBuilder:
        self._create_by_file_request_body_data.doc_form = doc_form
        return self

    def doc_language(self, doc_language: str) -> CreateByFileRequestBodyBuilder:
        self._create_by_file_request_body_data.doc_language = doc_language
        return self

    def process_rule(self, process_rule: ProcessRule) -> CreateByFileRequestBodyBuilder:
        self._create_by_file_request_body_data.process_rule = process_rule
        return self

    def retrieval_model(self, retrieval_model: RetrievalModel) -> CreateByFileRequestBodyBuilder:
        self._create_by_file_request_body_data.retrieval_model = retrieval_model
        return self

    def embedding_model(self, embedding_model: str) -> CreateByFileRequestBodyBuilder:
        self._create_by_file_request_body_data.embedding_model = embedding_model
        return self

    def embedding_model_provider(self, embedding_model_provider: str) -> CreateByFileRequestBodyBuilder:
        self._create_by_file_request_body_data.embedding_model_provider = embedding_model_provider
        return self
