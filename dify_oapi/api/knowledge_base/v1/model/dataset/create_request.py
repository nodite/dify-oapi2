from __future__ import annotations

from typing import Optional

from pydantic import BaseModel

from .retrieval_model import RetrievalModel


class CreateDatasetRequest(BaseModel):
    name: str
    description: Optional[str] = None
    indexing_technique: Optional[str] = None
    permission: Optional[str] = None
    provider: Optional[str] = None
    external_knowledge_api_id: Optional[str] = None
    external_knowledge_id: Optional[str] = None
    embedding_model: Optional[str] = None
    embedding_model_provider: Optional[str] = None
    retrieval_model: Optional[RetrievalModel] = None

    @staticmethod
    def builder() -> CreateDatasetRequestBuilder:
        return CreateDatasetRequestBuilder()


class CreateDatasetRequestBuilder:
    def __init__(self):
        self._request = CreateDatasetRequest(name="")

    def build(self) -> CreateDatasetRequest:
        return self._request

    def name(self, name: str) -> CreateDatasetRequestBuilder:
        self._request.name = name
        return self

    def description(self, description: str) -> CreateDatasetRequestBuilder:
        self._request.description = description
        return self

    def indexing_technique(self, indexing_technique: str) -> CreateDatasetRequestBuilder:
        self._request.indexing_technique = indexing_technique
        return self

    def permission(self, permission: str) -> CreateDatasetRequestBuilder:
        self._request.permission = permission
        return self

    def provider(self, provider: str) -> CreateDatasetRequestBuilder:
        self._request.provider = provider
        return self

    def external_knowledge_api_id(self, external_knowledge_api_id: str) -> CreateDatasetRequestBuilder:
        self._request.external_knowledge_api_id = external_knowledge_api_id
        return self

    def external_knowledge_id(self, external_knowledge_id: str) -> CreateDatasetRequestBuilder:
        self._request.external_knowledge_id = external_knowledge_id
        return self

    def embedding_model(self, embedding_model: str) -> CreateDatasetRequestBuilder:
        self._request.embedding_model = embedding_model
        return self

    def embedding_model_provider(self, embedding_model_provider: str) -> CreateDatasetRequestBuilder:
        self._request.embedding_model_provider = embedding_model_provider
        return self

    def retrieval_model(self, retrieval_model: RetrievalModel) -> CreateDatasetRequestBuilder:
        self._request.retrieval_model = retrieval_model
        return self