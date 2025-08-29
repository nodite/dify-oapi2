from __future__ import annotations

from typing import Literal

from pydantic import BaseModel

from .retrieval_model import RetrievalModel


class UpdateRequestBody(BaseModel):
    name: str | None = None
    indexing_technique: str | None = None
    permission: str | None = None
    embedding_model_provider: str | None = None
    embedding_model: str | None = None
    retrieval_model: RetrievalModel | None = None
    partial_member_list: list[str] | None = None

    @staticmethod
    def builder() -> UpdateRequestBodyBuilder:
        return UpdateRequestBodyBuilder()


class UpdateRequestBodyBuilder:
    def __init__(self):
        update_request_body = UpdateRequestBody()
        self._update_request_body = update_request_body

    def build(self) -> UpdateRequestBody:
        return self._update_request_body

    def name(self, name: str) -> UpdateRequestBodyBuilder:
        self._update_request_body.name = name
        return self

    def indexing_technique(self, indexing_technique: Literal["high_quality", "economy"]) -> UpdateRequestBodyBuilder:
        self._update_request_body.indexing_technique = indexing_technique
        return self

    def permission(self, permission: str) -> UpdateRequestBodyBuilder:
        self._update_request_body.permission = permission
        return self

    def embedding_model_provider(self, embedding_model_provider: str) -> UpdateRequestBodyBuilder:
        self._update_request_body.embedding_model_provider = embedding_model_provider
        return self

    def embedding_model(self, embedding_model: str) -> UpdateRequestBodyBuilder:
        self._update_request_body.embedding_model = embedding_model
        return self

    def retrieval_model(self, retrieval_model: RetrievalModel) -> UpdateRequestBodyBuilder:
        self._update_request_body.retrieval_model = retrieval_model
        return self

    def partial_member_list(self, partial_member_list: list[str]) -> UpdateRequestBodyBuilder:
        self._update_request_body.partial_member_list = partial_member_list
        return self
