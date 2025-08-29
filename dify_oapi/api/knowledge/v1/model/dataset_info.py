"""Dataset information model for Knowledge Base API."""

from typing import Optional

from pydantic import BaseModel

from .knowledge_types import DataSourceType, IndexingTechnique, Permission


class DatasetInfo(BaseModel):
    """Dataset information model with builder pattern."""

    id: Optional[str] = None
    name: Optional[str] = None
    description: Optional[str] = None
    indexing_technique: Optional[IndexingTechnique] = None
    permission: Optional[Permission] = None
    data_source_type: Optional[DataSourceType] = None
    provider: Optional[str] = None
    model: Optional[str] = None
    created_by: Optional[str] = None
    created_at: Optional[int] = None
    updated_at: Optional[int] = None
    document_count: Optional[int] = None
    word_count: Optional[int] = None

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

    def model(self, model: str) -> "DatasetInfoBuilder":
        self._dataset_info.model = model
        return self

    def created_by(self, created_by: str) -> "DatasetInfoBuilder":
        self._dataset_info.created_by = created_by
        return self

    def created_at(self, created_at: int) -> "DatasetInfoBuilder":
        self._dataset_info.created_at = created_at
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
