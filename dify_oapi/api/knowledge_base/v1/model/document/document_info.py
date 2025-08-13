from __future__ import annotations

from typing import Literal

from pydantic import BaseModel

from .data_source_info import DataSourceInfo


class DocumentInfo(BaseModel):
    """Document information model containing all document-related fields."""

    id: str | None = None
    position: int | None = None
    data_source_type: str | None = None
    data_source_info: DataSourceInfo | None = None
    dataset_process_rule_id: str | None = None
    name: str | None = None
    created_from: str | None = None
    created_by: str | None = None
    created_at: int | None = None
    tokens: int | None = None
    indexing_status: str | None = None
    error: str | None = None
    enabled: bool | None = None
    disabled_at: int | None = None
    disabled_by: str | None = None
    archived: bool | None = None
    display_status: str | None = None
    word_count: int | None = None
    hit_count: int | None = None
    doc_form: str | None = None
    doc_language: str | None = None
    completed_at: int | None = None
    updated_at: int | None = None
    indexing_latency: float | None = None
    segment_count: int | None = None
    average_segment_length: int | None = None
    dataset_process_rule: dict | None = None
    document_process_rule: dict | None = None

    @staticmethod
    def builder() -> DocumentInfoBuilder:
        return DocumentInfoBuilder()


class DocumentInfoBuilder:
    def __init__(self):
        self._document_info = DocumentInfo()

    def build(self) -> DocumentInfo:
        return self._document_info

    def id(self, id: str) -> DocumentInfoBuilder:
        self._document_info.id = id
        return self

    def position(self, position: int) -> DocumentInfoBuilder:
        self._document_info.position = position
        return self

    def data_source_type(self, data_source_type: str) -> DocumentInfoBuilder:
        self._document_info.data_source_type = data_source_type
        return self

    def data_source_info(self, data_source_info: DataSourceInfo) -> DocumentInfoBuilder:
        self._document_info.data_source_info = data_source_info
        return self

    def dataset_process_rule_id(self, dataset_process_rule_id: str) -> DocumentInfoBuilder:
        self._document_info.dataset_process_rule_id = dataset_process_rule_id
        return self

    def name(self, name: str) -> DocumentInfoBuilder:
        self._document_info.name = name
        return self

    def created_from(self, created_from: str) -> DocumentInfoBuilder:
        self._document_info.created_from = created_from
        return self

    def created_by(self, created_by: str) -> DocumentInfoBuilder:
        self._document_info.created_by = created_by
        return self

    def created_at(self, created_at: int) -> DocumentInfoBuilder:
        self._document_info.created_at = created_at
        return self

    def tokens(self, tokens: int) -> DocumentInfoBuilder:
        self._document_info.tokens = tokens
        return self

    def indexing_status(self, indexing_status: str) -> DocumentInfoBuilder:
        self._document_info.indexing_status = indexing_status
        return self

    def error(self, error: str) -> DocumentInfoBuilder:
        self._document_info.error = error
        return self

    def enabled(self, enabled: bool) -> DocumentInfoBuilder:
        self._document_info.enabled = enabled
        return self

    def disabled_at(self, disabled_at: int) -> DocumentInfoBuilder:
        self._document_info.disabled_at = disabled_at
        return self

    def disabled_by(self, disabled_by: str) -> DocumentInfoBuilder:
        self._document_info.disabled_by = disabled_by
        return self

    def archived(self, archived: bool) -> DocumentInfoBuilder:
        self._document_info.archived = archived
        return self

    def display_status(self, display_status: str) -> DocumentInfoBuilder:
        self._document_info.display_status = display_status
        return self

    def word_count(self, word_count: int) -> DocumentInfoBuilder:
        self._document_info.word_count = word_count
        return self

    def hit_count(self, hit_count: int) -> DocumentInfoBuilder:
        self._document_info.hit_count = hit_count
        return self

    def doc_form(self, doc_form: Literal["text_model", "hierarchical_model", "qa_model"]) -> DocumentInfoBuilder:
        self._document_info.doc_form = doc_form
        return self

    def doc_language(self, doc_language: str) -> DocumentInfoBuilder:
        self._document_info.doc_language = doc_language
        return self

    def completed_at(self, completed_at: int) -> DocumentInfoBuilder:
        self._document_info.completed_at = completed_at
        return self

    def updated_at(self, updated_at: int) -> DocumentInfoBuilder:
        self._document_info.updated_at = updated_at
        return self

    def indexing_latency(self, indexing_latency: float) -> DocumentInfoBuilder:
        self._document_info.indexing_latency = indexing_latency
        return self

    def segment_count(self, segment_count: int) -> DocumentInfoBuilder:
        self._document_info.segment_count = segment_count
        return self

    def average_segment_length(self, average_segment_length: int) -> DocumentInfoBuilder:
        self._document_info.average_segment_length = average_segment_length
        return self

    def dataset_process_rule(self, dataset_process_rule: dict) -> DocumentInfoBuilder:
        self._document_info.dataset_process_rule = dataset_process_rule
        return self

    def document_process_rule(self, document_process_rule: dict) -> DocumentInfoBuilder:
        self._document_info.document_process_rule = document_process_rule
        return self
