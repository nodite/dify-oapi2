"""Document information model for Knowledge Base API."""

from typing import Optional

from pydantic import BaseModel

from .data_source_detail import DataSourceDetailDict
from .data_source_info import DataSourceInfo
from .document_metadata import DocumentMetadata
from .knowledge_types import DataSourceType, DocumentDisplayStatus, DocumentForm, IndexingStatus


class DocumentInfo(BaseModel):
    """Document information model with builder pattern."""

    id: str | None = None
    position: int | None = None
    data_source_type: DataSourceType | None = None
    data_source_info: Optional["DataSourceInfo"] = None
    data_source_detail_dict: DataSourceDetailDict | None = None
    dataset_process_rule_id: str | None = None
    name: str | None = None
    created_from: str | None = None
    created_by: str | None = None
    created_at: int | None = None
    tokens: int | None = None
    indexing_status: IndexingStatus | None = None
    error: str | None = None
    enabled: bool | None = None
    disabled_at: int | None = None
    disabled_by: str | None = None
    archived: bool | None = None
    display_status: DocumentDisplayStatus | None = None
    word_count: int | None = None
    hit_count: int | None = None
    doc_form: DocumentForm | None = None
    doc_metadata: DocumentMetadata | None = None
    updated_at: int | None = None

    @staticmethod
    def builder() -> "DocumentInfoBuilder":
        return DocumentInfoBuilder()


class DocumentInfoBuilder:
    """Builder for DocumentInfo."""

    def __init__(self):
        self._document_info = DocumentInfo()

    def build(self) -> DocumentInfo:
        return self._document_info

    def id(self, id: str) -> "DocumentInfoBuilder":
        self._document_info.id = id
        return self

    def position(self, position: int) -> "DocumentInfoBuilder":
        self._document_info.position = position
        return self

    def data_source_type(self, data_source_type: DataSourceType) -> "DocumentInfoBuilder":
        self._document_info.data_source_type = data_source_type
        return self

    def data_source_info(self, data_source_info: DataSourceInfo) -> "DocumentInfoBuilder":
        self._document_info.data_source_info = data_source_info
        return self

    def data_source_detail_dict(self, data_source_detail_dict: DataSourceDetailDict) -> "DocumentInfoBuilder":
        self._document_info.data_source_detail_dict = data_source_detail_dict
        return self

    def dataset_process_rule_id(self, dataset_process_rule_id: str) -> "DocumentInfoBuilder":
        self._document_info.dataset_process_rule_id = dataset_process_rule_id
        return self

    def name(self, name: str) -> "DocumentInfoBuilder":
        self._document_info.name = name
        return self

    def created_from(self, created_from: str) -> "DocumentInfoBuilder":
        self._document_info.created_from = created_from
        return self

    def created_by(self, created_by: str) -> "DocumentInfoBuilder":
        self._document_info.created_by = created_by
        return self

    def created_at(self, created_at: int) -> "DocumentInfoBuilder":
        self._document_info.created_at = created_at
        return self

    def tokens(self, tokens: int) -> "DocumentInfoBuilder":
        self._document_info.tokens = tokens
        return self

    def indexing_status(self, indexing_status: IndexingStatus) -> "DocumentInfoBuilder":
        self._document_info.indexing_status = indexing_status
        return self

    def error(self, error: str) -> "DocumentInfoBuilder":
        self._document_info.error = error
        return self

    def enabled(self, enabled: bool) -> "DocumentInfoBuilder":
        self._document_info.enabled = enabled
        return self

    def disabled_at(self, disabled_at: int) -> "DocumentInfoBuilder":
        self._document_info.disabled_at = disabled_at
        return self

    def disabled_by(self, disabled_by: str) -> "DocumentInfoBuilder":
        self._document_info.disabled_by = disabled_by
        return self

    def archived(self, archived: bool) -> "DocumentInfoBuilder":
        self._document_info.archived = archived
        return self

    def display_status(self, display_status: DocumentDisplayStatus) -> "DocumentInfoBuilder":
        self._document_info.display_status = display_status
        return self

    def word_count(self, word_count: int) -> "DocumentInfoBuilder":
        self._document_info.word_count = word_count
        return self

    def hit_count(self, hit_count: int) -> "DocumentInfoBuilder":
        self._document_info.hit_count = hit_count
        return self

    def doc_form(self, doc_form: DocumentForm) -> "DocumentInfoBuilder":
        self._document_info.doc_form = doc_form
        return self

    def doc_metadata(self, doc_metadata: DocumentMetadata) -> "DocumentInfoBuilder":
        self._document_info.doc_metadata = doc_metadata
        return self

    def updated_at(self, updated_at: int) -> "DocumentInfoBuilder":
        self._document_info.updated_at = updated_at
        return self
