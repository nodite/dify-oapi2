from __future__ import annotations

from typing import Optional, List

from pydantic import BaseModel

from .retrieval_model import RetrievalModel


class UpdateDatasetRequest(BaseModel):
    dataset_id: str
    name: Optional[str] = None
    indexing_technique: Optional[str] = None
    permission: Optional[str] = None
    embedding_model_provider: Optional[str] = None
    embedding_model: Optional[str] = None
    retrieval_model: Optional[RetrievalModel] = None
    partial_member_list: Optional[List[str]] = None

    @staticmethod
    def builder() -> UpdateDatasetRequestBuilder:
        return UpdateDatasetRequestBuilder()


class UpdateDatasetRequestBuilder:
    def __init__(self):
        self._request = UpdateDatasetRequest(dataset_id="")

    def build(self) -> UpdateDatasetRequest:
        return self._request

    def dataset_id(self, dataset_id: str) -> UpdateDatasetRequestBuilder:
        self._request.dataset_id = dataset_id
        return self

    def name(self, name: str) -> UpdateDatasetRequestBuilder:
        self._request.name = name
        return self

    def indexing_technique(self, indexing_technique: str) -> UpdateDatasetRequestBuilder:
        self._request.indexing_technique = indexing_technique
        return self

    def permission(self, permission: str) -> UpdateDatasetRequestBuilder:
        self._request.permission = permission
        return self

    def embedding_model_provider(self, embedding_model_provider: str) -> UpdateDatasetRequestBuilder:
        self._request.embedding_model_provider = embedding_model_provider
        return self

    def embedding_model(self, embedding_model: str) -> UpdateDatasetRequestBuilder:
        self._request.embedding_model = embedding_model
        return self

    def retrieval_model(self, retrieval_model: RetrievalModel) -> UpdateDatasetRequestBuilder:
        self._request.retrieval_model = retrieval_model
        return self

    def partial_member_list(self, partial_member_list: List[str]) -> UpdateDatasetRequestBuilder:
        self._request.partial_member_list = partial_member_list
        return self