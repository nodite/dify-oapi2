from __future__ import annotations

from pydantic import BaseModel

from .dataset_types import IndexingTechnique
from .retrieval_model import RetrievalModel


class CreateRequestBody(BaseModel):
    name: str | None = None
    description: str | None = None
    indexing_technique: IndexingTechnique | None = None
    permission: str | None = None
    provider: str | None = None
    external_knowledge_api_id: str | None = None
    external_knowledge_id: str | None = None
    embedding_model: str | None = None
    embedding_model_provider: str | None = None
    retrieval_model: RetrievalModel | None = None

    @staticmethod
    def builder() -> CreateRequestBodyBuilder:
        return CreateRequestBodyBuilder()


class CreateRequestBodyBuilder:
    def __init__(self):
        create_request_body = CreateRequestBody()
        self._create_request_body = create_request_body

    def build(self) -> CreateRequestBody:
        return self._create_request_body

    def name(self, name: str) -> CreateRequestBodyBuilder:
        self._create_request_body.name = name
        return self

    def description(self, description: str) -> CreateRequestBodyBuilder:
        self._create_request_body.description = description
        return self

    def indexing_technique(self, indexing_technique: IndexingTechnique) -> CreateRequestBodyBuilder:
        self._create_request_body.indexing_technique = indexing_technique
        return self

    def permission(self, permission: str) -> CreateRequestBodyBuilder:
        self._create_request_body.permission = permission
        return self

    def provider(self, provider: str) -> CreateRequestBodyBuilder:
        self._create_request_body.provider = provider
        return self

    def external_knowledge_api_id(self, external_knowledge_api_id: str) -> CreateRequestBodyBuilder:
        self._create_request_body.external_knowledge_api_id = external_knowledge_api_id
        return self

    def external_knowledge_id(self, external_knowledge_id: str) -> CreateRequestBodyBuilder:
        self._create_request_body.external_knowledge_id = external_knowledge_id
        return self

    def embedding_model(self, embedding_model: str) -> CreateRequestBodyBuilder:
        self._create_request_body.embedding_model = embedding_model
        return self

    def embedding_model_provider(self, embedding_model_provider: str) -> CreateRequestBodyBuilder:
        self._create_request_body.embedding_model_provider = embedding_model_provider
        return self

    def retrieval_model(self, retrieval_model: RetrievalModel) -> CreateRequestBodyBuilder:
        self._create_request_body.retrieval_model = retrieval_model
        return self
