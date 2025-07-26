from __future__ import annotations

from typing import Optional, List

from pydantic import BaseModel

from .retrieval_model import RetrievalModel


class UpdateRequestBody(BaseModel):
    name: Optional[str] = None
    indexing_technique: Optional[str] = None
    permission: Optional[str] = None
    embedding_model_provider: Optional[str] = None
    embedding_model: Optional[str] = None
    retrieval_model: Optional[RetrievalModel] = None
    partial_member_list: Optional[List[str]] = None

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

    def indexing_technique(self, indexing_technique: str) -> UpdateRequestBodyBuilder:
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

    def partial_member_list(self, partial_member_list: List[str]) -> UpdateRequestBodyBuilder:
        self._update_request_body.partial_member_list = partial_member_list
        return self