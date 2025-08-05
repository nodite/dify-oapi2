from __future__ import annotations

from typing import Literal

from pydantic import BaseModel

from ..metadata.metadata_info import MetadataInfo
from ..tag.tag_info import TagInfo
from .external_knowledge_info import ExternalKnowledgeInfo
from .retrieval_model import RetrievalModel


class DatasetInfo(BaseModel):
    id: str | None = None
    name: str | None = None
    description: str | None = None
    provider: str | None = None
    permission: str | None = None
    data_source_type: str | None = None
    indexing_technique: str | None = None
    app_count: int | None = None
    document_count: int | None = None
    word_count: int | None = None
    created_by: str | None = None
    created_at: int | None = None
    updated_by: str | None = None
    updated_at: int | None = None
    embedding_model: str | None = None
    embedding_model_provider: str | None = None
    embedding_available: bool | None = None
    retrieval_model_dict: RetrievalModel | None = None
    tags: list[TagInfo] | None = None
    doc_form: str | None = None
    external_knowledge_info: ExternalKnowledgeInfo | None = None
    external_retrieval_model: RetrievalModel | None = None
    partial_member_list: list[str] | None = None
    doc_metadata: list[MetadataInfo] | None = None
    built_in_field_enabled: bool | None = None

    @staticmethod
    def builder() -> DatasetInfoBuilder:
        return DatasetInfoBuilder()


class DatasetInfoBuilder:
    def __init__(self):
        self._dataset_info = DatasetInfo()

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

    def indexing_technique(self, indexing_technique: Literal["high_quality", "economy"]) -> DatasetInfoBuilder:
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

    def tags(self, tags: list[TagInfo]) -> DatasetInfoBuilder:
        self._dataset_info.tags = tags
        return self

    def doc_form(self, doc_form: Literal["text_model", "hierarchical_model", "qa_model"]) -> DatasetInfoBuilder:
        self._dataset_info.doc_form = doc_form
        return self

    def external_knowledge_info(self, external_knowledge_info: ExternalKnowledgeInfo) -> DatasetInfoBuilder:
        self._dataset_info.external_knowledge_info = external_knowledge_info
        return self

    def external_retrieval_model(self, external_retrieval_model: RetrievalModel) -> DatasetInfoBuilder:
        self._dataset_info.external_retrieval_model = external_retrieval_model
        return self

    def partial_member_list(self, partial_member_list: list[str]) -> DatasetInfoBuilder:
        self._dataset_info.partial_member_list = partial_member_list
        return self

    def doc_metadata(self, doc_metadata: list[MetadataInfo]) -> DatasetInfoBuilder:
        self._dataset_info.doc_metadata = doc_metadata
        return self

    def built_in_field_enabled(self, built_in_field_enabled: bool) -> DatasetInfoBuilder:
        self._dataset_info.built_in_field_enabled = built_in_field_enabled
        return self
