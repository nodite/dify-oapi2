"""Document information model for Knowledge Base API."""

from typing import Optional

from pydantic import BaseModel

from .knowledge_types import DataSourceType, DocumentStatus


class DocumentInfo(BaseModel):
    """Document information model with builder pattern."""

    id: Optional[str] = None
    name: Optional[str] = None
    character_count: Optional[int] = None
    tokens: Optional[int] = None
    status: Optional[DocumentStatus] = None
    error: Optional[str] = None
    enabled: Optional[bool] = None
    disabled_at: Optional[int] = None
    disabled_by: Optional[str] = None
    archived: Optional[bool] = None
    display_status: Optional[str] = None
    word_count: Optional[int] = None
    hit_count: Optional[int] = None
    doc_form: Optional[str] = None
    data_source_type: Optional[DataSourceType] = None
    data_source_info: Optional[dict] = None
    dataset_process_rule_id: Optional[str] = None
    processing_started_at: Optional[int] = None
    parsing_completed_at: Optional[int] = None
    cleaning_completed_at: Optional[int] = None
    splitting_completed_at: Optional[int] = None
    indexing_completed_at: Optional[int] = None
    completed_at: Optional[int] = None
    paused_by: Optional[str] = None
    paused_at: Optional[int] = None
    error_at: Optional[int] = None
    stopped_at: Optional[int] = None
    indexing_latency: Optional[float] = None
    created_by: Optional[str] = None
    created_at: Optional[int] = None
    updated_at: Optional[int] = None

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

    def name(self, name: str) -> "DocumentInfoBuilder":
        self._document_info.name = name
        return self

    def character_count(self, character_count: int) -> "DocumentInfoBuilder":
        self._document_info.character_count = character_count
        return self

    def tokens(self, tokens: int) -> "DocumentInfoBuilder":
        self._document_info.tokens = tokens
        return self

    def status(self, status: DocumentStatus) -> "DocumentInfoBuilder":
        self._document_info.status = status
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

    def data_source_type(self, data_source_type: DataSourceType) -> "DocumentInfoBuilder":
        self._document_info.data_source_type = data_source_type
        return self

    def data_source_info(self, data_source_info: dict) -> "DocumentInfoBuilder":
        self._document_info.data_source_info = data_source_info
        return self

    def dataset_process_rule_id(self, dataset_process_rule_id: str) -> "DocumentInfoBuilder":
        self._document_info.dataset_process_rule_id = dataset_process_rule_id
        return self

    def processing_started_at(self, processing_started_at: int) -> "DocumentInfoBuilder":
        self._document_info.processing_started_at = processing_started_at
        return self

    def parsing_completed_at(self, parsing_completed_at: int) -> "DocumentInfoBuilder":
        self._document_info.parsing_completed_at = parsing_completed_at
        return self

    def cleaning_completed_at(self, cleaning_completed_at: int) -> "DocumentInfoBuilder":
        self._document_info.cleaning_completed_at = cleaning_completed_at
        return self

    def splitting_completed_at(self, splitting_completed_at: int) -> "DocumentInfoBuilder":
        self._document_info.splitting_completed_at = splitting_completed_at
        return self

    def indexing_completed_at(self, indexing_completed_at: int) -> "DocumentInfoBuilder":
        self._document_info.indexing_completed_at = indexing_completed_at
        return self

    def completed_at(self, completed_at: int) -> "DocumentInfoBuilder":
        self._document_info.completed_at = completed_at
        return self

    def paused_by(self, paused_by: str) -> "DocumentInfoBuilder":
        self._document_info.paused_by = paused_by
        return self

    def paused_at(self, paused_at: int) -> "DocumentInfoBuilder":
        self._document_info.paused_at = paused_at
        return self

    def error_at(self, error_at: int) -> "DocumentInfoBuilder":
        self._document_info.error_at = error_at
        return self

    def stopped_at(self, stopped_at: int) -> "DocumentInfoBuilder":
        self._document_info.stopped_at = stopped_at
        return self

    def indexing_latency(self, indexing_latency: float) -> "DocumentInfoBuilder":
        self._document_info.indexing_latency = indexing_latency
        return self

    def created_by(self, created_by: str) -> "DocumentInfoBuilder":
        self._document_info.created_by = created_by
        return self

    def created_at(self, created_at: int) -> "DocumentInfoBuilder":
        self._document_info.created_at = created_at
        return self

    def updated_at(self, updated_at: int) -> "DocumentInfoBuilder":
        self._document_info.updated_at = updated_at
        return self
