"""Dataset information model for Knowledge Base API."""

from typing import Optional

from pydantic import BaseModel

from .dataset_metadata import DatasetMetadata
from .external_knowledge_info import ExternalKnowledgeInfo
from .external_retrieval_model import ExternalRetrievalModel
from .knowledge_types import DataSourceType, DocumentForm, IndexingTechnique, Permission
from .retrieval_model import RetrievalModel
from .tag_info import TagInfo


class DatasetInfo(BaseModel):
    """Dataset information model with builder pattern."""

    id: Optional[str] = None
    name: Optional[str] = None
    description: Optional[str] = None
    provider: Optional[str] = None
    permission: Optional[Permission] = None
    data_source_type: Optional[DataSourceType] = None
    indexing_technique: Optional[IndexingTechnique] = None
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
    tags: Optional[list[TagInfo]] = None
    doc_form: Optional[DocumentForm] = None
    external_knowledge_info: Optional[ExternalKnowledgeInfo] = None
    external_retrieval_model: Optional[ExternalRetrievalModel] = None
    doc_metadata: Optional[list[DatasetMetadata]] = None
    built_in_field_enabled: Optional[bool] = None

    @staticmethod
    def builder() -> "DatasetInfoBuilder":
        return DatasetInfoBuilder()


class DatasetInfoBuilder:
    """Builder for DatasetInfo."""

    def __init__(self):
        self._dataset_info = DatasetInfo()

    def build(self) -> DatasetInfo:
        return self._dataset_info

    def id(self, id: str) -> "DatasetInfoBuilder":
        self._dataset_info.id = id
        return self

    def name(self, name: str) -> "DatasetInfoBuilder":
        self._dataset_info.name = name
        return self

    def description(self, description: str) -> "DatasetInfoBuilder":
        self._dataset_info.description = description
        return self

    def indexing_technique(self, indexing_technique: IndexingTechnique) -> "DatasetInfoBuilder":
        self._dataset_info.indexing_technique = indexing_technique
        return self

    def permission(self, permission: Permission) -> "DatasetInfoBuilder":
        self._dataset_info.permission = permission
        return self

    def data_source_type(self, data_source_type: DataSourceType) -> "DatasetInfoBuilder":
        self._dataset_info.data_source_type = data_source_type
        return self

    def provider(self, provider: str) -> "DatasetInfoBuilder":
        self._dataset_info.provider = provider
        return self

    def app_count(self, app_count: int) -> "DatasetInfoBuilder":
        self._dataset_info.app_count = app_count
        return self

    def created_by(self, created_by: str) -> "DatasetInfoBuilder":
        self._dataset_info.created_by = created_by
        return self

    def created_at(self, created_at: int) -> "DatasetInfoBuilder":
        self._dataset_info.created_at = created_at
        return self

    def updated_by(self, updated_by: str) -> "DatasetInfoBuilder":
        self._dataset_info.updated_by = updated_by
        return self

    def updated_at(self, updated_at: int) -> "DatasetInfoBuilder":
        self._dataset_info.updated_at = updated_at
        return self

    def document_count(self, document_count: int) -> "DatasetInfoBuilder":
        self._dataset_info.document_count = document_count
        return self

    def word_count(self, word_count: int) -> "DatasetInfoBuilder":
        self._dataset_info.word_count = word_count
        return self

    def embedding_model(self, embedding_model: str) -> "DatasetInfoBuilder":
        self._dataset_info.embedding_model = embedding_model
        return self

    def embedding_model_provider(self, embedding_model_provider: str) -> "DatasetInfoBuilder":
        self._dataset_info.embedding_model_provider = embedding_model_provider
        return self

    def embedding_available(self, embedding_available: bool) -> "DatasetInfoBuilder":
        self._dataset_info.embedding_available = embedding_available
        return self
