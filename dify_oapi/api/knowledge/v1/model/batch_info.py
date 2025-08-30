"""Batch information model for Knowledge Base API."""

from typing import Optional

from pydantic import BaseModel

from .knowledge_types import IndexingStatus


class BatchInfo(BaseModel):
    """Batch information model with builder pattern."""

    id: Optional[str] = None
    indexing_status: Optional[IndexingStatus] = None
    processing_started_at: Optional[float] = None
    parsing_completed_at: Optional[float] = None
    cleaning_completed_at: Optional[float] = None
    splitting_completed_at: Optional[float] = None
    completed_at: Optional[float] = None
    paused_at: Optional[float] = None
    error: Optional[str] = None
    stopped_at: Optional[float] = None
    completed_segments: Optional[int] = None
    total_segments: Optional[int] = None

    @staticmethod
    def builder() -> "BatchInfoBuilder":
        return BatchInfoBuilder()


class BatchInfoBuilder:
    """Builder for BatchInfo."""

    def __init__(self):
        self._batch_info = BatchInfo()

    def build(self) -> BatchInfo:
        return self._batch_info

    def id(self, id: str) -> "BatchInfoBuilder":
        self._batch_info.id = id
        return self

    def indexing_status(self, indexing_status: IndexingStatus) -> "BatchInfoBuilder":
        self._batch_info.indexing_status = indexing_status
        return self

    def processing_started_at(self, processing_started_at: float) -> "BatchInfoBuilder":
        self._batch_info.processing_started_at = processing_started_at
        return self

    def parsing_completed_at(self, parsing_completed_at: float) -> "BatchInfoBuilder":
        self._batch_info.parsing_completed_at = parsing_completed_at
        return self

    def cleaning_completed_at(self, cleaning_completed_at: float) -> "BatchInfoBuilder":
        self._batch_info.cleaning_completed_at = cleaning_completed_at
        return self

    def splitting_completed_at(self, splitting_completed_at: float) -> "BatchInfoBuilder":
        self._batch_info.splitting_completed_at = splitting_completed_at
        return self

    def completed_at(self, completed_at: float) -> "BatchInfoBuilder":
        self._batch_info.completed_at = completed_at
        return self

    def paused_at(self, paused_at: float) -> "BatchInfoBuilder":
        self._batch_info.paused_at = paused_at
        return self

    def error(self, error: str) -> "BatchInfoBuilder":
        self._batch_info.error = error
        return self

    def stopped_at(self, stopped_at: float) -> "BatchInfoBuilder":
        self._batch_info.stopped_at = stopped_at
        return self

    def completed_segments(self, completed_segments: int) -> "BatchInfoBuilder":
        self._batch_info.completed_segments = completed_segments
        return self

    def total_segments(self, total_segments: int) -> "BatchInfoBuilder":
        self._batch_info.total_segments = total_segments
        return self
