from __future__ import annotations

from typing import Optional, List

from pydantic import BaseModel

from .external_knowledge_info import ExternalKnowledgeInfo
from .retrieval_model import RetrievalModel
from .tag_info import TagInfo


class DatasetInfo(BaseModel):
    id: str
    name: str
    description: Optional[str] = None
    provider: Optional[str] = None
    permission: Optional[str] = None
    data_source_type: Optional[str] = None
    indexing_technique: Optional[str] = None
    app_count: Optional[int] = None
    document_count: Optional[int] = None
    word_count: Optional[int] = None
    created_by: Optional[str] = None
    created_at: Optional[int] = None
    updated_by: Optional[str] = None
    updated_at: Optional[int] = None
    embedding_model: Optional[str] = None
    embedding_model_provider: Optional[str] = None
    embedding_available: Optional[bool] = None
    retrieval_model_dict: Optional[RetrievalModel] = None
    tags: Optional[List[TagInfo]] = None
    doc_form: Optional[str] = None
    external_knowledge_info: Optional[ExternalKnowledgeInfo] = None
    external_retrieval_model: Optional[RetrievalModel] = None
    partial_member_list: Optional[List[str]] = None

    @staticmethod
    def builder() -> DatasetInfoBuilder:
        return DatasetInfoBuilder()


class DatasetInfoBuilder:
    def __init__(self):
        self._dataset_info = DatasetInfo(id="", name="")

    def build(self) -> DatasetInfo:
        return self._dataset_info

    def id(self, id: str) -> DatasetInfoBuilder:
        self._dataset_info.id = id
        return self

    def name(self, name: str) -> DatasetInfoBuilder:
        self._dataset_info.name = name
        return self

    def description(self, description: str) -> DatasetInfoBuilder:
        self._dataset_info.description = description
        return self

    def provider(self, provider: str) -> DatasetInfoBuilder:
        self._dataset_info.provider = provider
        return self

    def permission(self, permission: str) -> DatasetInfoBuilder:
        self._dataset_info.permission = permission
        return self

    def data_source_type(self, data_source_type: str) -> DatasetInfoBuilder:
        self._dataset_info.data_source_type = data_source_type
        return self

    def indexing_technique(self, indexing_technique: str) -> DatasetInfoBuilder:
        self._dataset_info.indexing_technique = indexing_technique
        return self

    def app_count(self, app_count: int) -> DatasetInfoBuilder:
        self._dataset_info.app_count = app_count
        return self

    def document_count(self, document_count: int) -> DatasetInfoBuilder:
        self._dataset_info.document_count = document_count
        return self

    def word_count(self, word_count: int) -> DatasetInfoBuilder:
        self._dataset_info.word_count = word_count
        return self

    def created_by(self, created_by: str) -> DatasetInfoBuilder:
        self._dataset_info.created_by = created_by
        return self

    def created_at(self, created_at: int) -> DatasetInfoBuilder:
        self._dataset_info.created_at = created_at
        return self

    def updated_by(self, updated_by: str) -> DatasetInfoBuilder:
        self._dataset_info.updated_by = updated_by
        return self

    def updated_at(self, updated_at: int) -> DatasetInfoBuilder:
        self._dataset_info.updated_at = updated_at
        return self

    def embedding_model(self, embedding_model: str) -> DatasetInfoBuilder:
        self._dataset_info.embedding_model = embedding_model
        return self

    def embedding_model_provider(self, embedding_model_provider: str) -> DatasetInfoBuilder:
        self._dataset_info.embedding_model_provider = embedding_model_provider
        return self

    def embedding_available(self, embedding_available: bool) -> DatasetInfoBuilder:
        self._dataset_info.embedding_available = embedding_available
        return self

    def retrieval_model_dict(self, retrieval_model_dict: RetrievalModel) -> DatasetInfoBuilder:
        self._dataset_info.retrieval_model_dict = retrieval_model_dict
        return self

    def tags(self, tags: List[TagInfo]) -> DatasetInfoBuilder:
        self._dataset_info.tags = tags
        return self

    def doc_form(self, doc_form: str) -> DatasetInfoBuilder:
        self._dataset_info.doc_form = doc_form
        return self

    def external_knowledge_info(self, external_knowledge_info: ExternalKnowledgeInfo) -> DatasetInfoBuilder:
        self._dataset_info.external_knowledge_info = external_knowledge_info
        return self

    def external_retrieval_model(self, external_retrieval_model: RetrievalModel) -> DatasetInfoBuilder:
        self._dataset_info.external_retrieval_model = external_retrieval_model
        return self

    def partial_member_list(self, partial_member_list: List[str]) -> DatasetInfoBuilder:
        self._dataset_info.partial_member_list = partial_member_list
        return self