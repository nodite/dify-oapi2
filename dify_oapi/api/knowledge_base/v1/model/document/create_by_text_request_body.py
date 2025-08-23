from __future__ import annotations

from pydantic import BaseModel

from .document_types import DocumentForm, DocumentLanguage, IndexingTechnique
from .process_rule import ProcessRule
from .retrieval_model import RetrievalModel


class CreateByTextRequestBody(BaseModel):
    """Request body model for create document by text API"""

    name: str | None = None
    text: str | None = None
    indexing_technique: IndexingTechnique | None = None
    doc_form: DocumentForm | None = None
    doc_language: DocumentLanguage | None = None
    process_rule: ProcessRule | None = None
    retrieval_model: RetrievalModel | None = None
    embedding_model: str | None = None
    embedding_model_provider: str | None = None

    @staticmethod
    def builder() -> CreateByTextRequestBodyBuilder:
        return CreateByTextRequestBodyBuilder()


class CreateByTextRequestBodyBuilder:
    def __init__(self):
        self._create_by_text_request_body = CreateByTextRequestBody()

    def build(self) -> CreateByTextRequestBody:
        if not self._create_by_text_request_body.name:
            raise ValueError("Name must be provided")

        if not self._create_by_text_request_body.text:
            raise ValueError("Text must be provided")

        return self._create_by_text_request_body

    def name(self, name: str) -> CreateByTextRequestBodyBuilder:
        self._create_by_text_request_body.name = name
        return self

    def text(self, text: str) -> CreateByTextRequestBodyBuilder:
        self._create_by_text_request_body.text = text
        return self

    def indexing_technique(self, indexing_technique: IndexingTechnique) -> CreateByTextRequestBodyBuilder:
        self._create_by_text_request_body.indexing_technique = indexing_technique
        return self

    def doc_form(self, doc_form: DocumentForm) -> CreateByTextRequestBodyBuilder:
        self._create_by_text_request_body.doc_form = doc_form
        return self

    def doc_language(self, doc_language: DocumentLanguage) -> CreateByTextRequestBodyBuilder:
        self._create_by_text_request_body.doc_language = doc_language
        return self

    def process_rule(self, process_rule: ProcessRule) -> CreateByTextRequestBodyBuilder:
        self._create_by_text_request_body.process_rule = process_rule
        return self

    def retrieval_model(self, retrieval_model: RetrievalModel) -> CreateByTextRequestBodyBuilder:
        self._create_by_text_request_body.retrieval_model = retrieval_model
        return self

    def embedding_model(self, embedding_model: str) -> CreateByTextRequestBodyBuilder:
        self._create_by_text_request_body.embedding_model = embedding_model
        return self

    def embedding_model_provider(self, embedding_model_provider: str) -> CreateByTextRequestBodyBuilder:
        self._create_by_text_request_body.embedding_model_provider = embedding_model_provider
        return self
