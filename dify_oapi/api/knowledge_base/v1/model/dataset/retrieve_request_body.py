from __future__ import annotations

from typing import Any

from pydantic import BaseModel

from .retrieval_model import RetrievalModel


class RetrieveRequestBody(BaseModel):
    query: str | None = None
    retrieval_model: RetrievalModel | None = None
    external_retrieval_model: dict[str, Any] | None = None

    @staticmethod
    def builder() -> RetrieveRequestBodyBuilder:
        return RetrieveRequestBodyBuilder()


class RetrieveRequestBodyBuilder:
    def __init__(self):
        retrieve_request_body = RetrieveRequestBody()
        self._retrieve_request_body = retrieve_request_body

    def build(self) -> RetrieveRequestBody:
        return self._retrieve_request_body

    def query(self, query: str) -> RetrieveRequestBodyBuilder:
        self._retrieve_request_body.query = query
        return self

    def retrieval_model(self, retrieval_model: RetrievalModel) -> RetrieveRequestBodyBuilder:
        self._retrieve_request_body.retrieval_model = retrieval_model
        return self

    def external_retrieval_model(self, external_retrieval_model: dict[str, Any]) -> RetrieveRequestBodyBuilder:
        self._retrieve_request_body.external_retrieval_model = external_retrieval_model
        return self
