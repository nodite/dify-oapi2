"""Document information model for Knowledge Base API."""

from datetime import datetime
from typing import Optional

from pydantic import BaseModel

from .knowledge_types import DataSourceType, DocumentStatus, IndexingTechnique


class DocumentInfo(BaseModel):
    """Document information model with builder pattern."""

    id: Optional[str] = None
    position: Optional[int] = None
    data_source_type: Optional[DataSourceType] = None
    data_source_info: Optional[dict] = None
    dataset_process_rule_id: Optional[str] = None
    name: Optional[str] = None
    created_from: Optional[str] = None
    created_by: Optional[str] = None
    created_at: Optional[datetime] = None
    tokens: Optional[int] = None
    indexing_status: Optional[DocumentStatus] = None
    error: Optional[str] = None
    enabled: Optional[bool] = None
    disabled_at: Optional[datetime] = None
    disabled_by: Optional[str] = None
    archived: Optional[bool] = None
    display_status: Optional[str] = None
    word_count: Optional[int] = None
    hit_count: Optional[int] = None
    doc_form: Optional[str] = None
    parsing_completed_at: Optional[datetime] = None
    cleaning_completed_at: Optional[datetime] = None
    splitting_completed_at: Optional[datetime] = None
    indexing_completed_at: Optional[datetime] = None
    completed_at: Optional[datetime] = None
    paused_by: Optional[str] = None
    paused_at: Optional[datetime] = None
    stopped_at: Optional[datetime] = None
    indexing_technique: Optional[IndexingTechnique] = None
    batch: Optional[str] = None
    segment_count: Optional[int] = None

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

    def data_source_info(self, data_source_info: dict) -> "DocumentInfoBuilder":
        self._document_info.data_source_info = data_source_info
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

    def created_at(self, created_at: datetime) -> "DocumentInfoBuilder":
        self._document_info.created_at = created_at
        return self

    def tokens(self, tokens: int) -> "DocumentInfoBuilder":
        self._document_info.tokens = tokens
        return self

    def indexing_status(self, indexing_status: DocumentStatus) -> "DocumentInfoBuilder":
        self._document_info.indexing_status = indexing_status
        return self

    def error(self, error: str) -> "DocumentInfoBuilder":
        self._document_info.error = error
        return self

    def enabled(self, enabled: bool) -> "DocumentInfoBuilder":
        self._document_info.enabled = enabled
        return self

    def disabled_at(self, disabled_at: datetime) -> "DocumentInfoBuilder":
        self._document_info.disabled_at = disabled_at
        return self

    def disabled_by(self, disabled_by: str) -> "DocumentInfoBuilder":
        self._document_info.disabled_by = disabled_by
        return self

    def archived(self, archived: bool) -> "DocumentInfoBuilder":
        self._document_info.archived = archived
        return self

    def display_status(self, display_status: str) -> "DocumentInfoBuilder":
        self._document_info.display_status = display_status
        return self

    def word_count(self, word_count: int) -> "DocumentInfoBuilder":
        self._document_info.word_count = word_count
        return self

    def hit_count(self, hit_count: int) -> "DocumentInfoBuilder":
        self._document_info.hit_count = hit_count
        return self

    def doc_form(self, doc_form: str) -> "DocumentInfoBuilder":
        self._document_info.doc_form = doc_form
        return self

    def indexing_technique(self, indexing_technique: IndexingTechnique) -> "DocumentInfoBuilder":
        self._document_info.indexing_technique = indexing_technique
        return self

    def batch(self, batch: str) -> "DocumentInfoBuilder":
        self._document_info.batch = batch
        return self

    def segment_count(self, segment_count: int) -> "DocumentInfoBuilder":
        self._document_info.segment_count = segment_count
        return self
