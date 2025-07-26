from __future__ import annotations

from typing import Optional

from pydantic import BaseModel

from .retrieval_model import RetrievalModel


class RetrieveDatasetRequest(BaseModel):
    dataset_id: str
    query: str
    retrieval_model: Optional[RetrievalModel] = None
    external_retrieval_model: Optional[dict] = None

    @staticmethod
    def builder() -> RetrieveDatasetRequestBuilder:
        return RetrieveDatasetRequestBuilder()


class RetrieveDatasetRequestBuilder:
    def __init__(self):
        self._request = RetrieveDatasetRequest(dataset_id="", query="")

    def build(self) -> RetrieveDatasetRequest:
        return self._request

    def dataset_id(self, dataset_id: str) -> RetrieveDatasetRequestBuilder:
        self._request.dataset_id = dataset_id
        return self

    def query(self, query: str) -> RetrieveDatasetRequestBuilder:
        self._request.query = query
        return self

    def retrieval_model(self, retrieval_model: RetrievalModel) -> RetrieveDatasetRequestBuilder:
        self._request.retrieval_model = retrieval_model
        return self

    def external_retrieval_model(self, external_retrieval_model: dict) -> RetrieveDatasetRequestBuilder:
        self._request.external_retrieval_model = external_retrieval_model
        return self