from __future__ import annotations

from pydantic import BaseModel


class IndexingStatusInfo(BaseModel):
    """Indexing status information model for document processing status."""

    id: str | None = None
    indexing_status: str | None = None
    processing_started_at: float | None = None
    parsing_completed_at: float | None = None
    cleaning_completed_at: float | None = None
    splitting_completed_at: float | None = None
    completed_at: float | None = None
    paused_at: float | None = None
    error: str | None = None
    stopped_at: float | None = None
    completed_segments: int | None = None
    total_segments: int | None = None

    @staticmethod
    def builder() -> IndexingStatusInfoBuilder:
        return IndexingStatusInfoBuilder()


class IndexingStatusInfoBuilder:
    def __init__(self):
        self._indexing_status_info = IndexingStatusInfo()

    def build(self) -> IndexingStatusInfo:
        return self._indexing_status_info

    def id(self, id: str) -> IndexingStatusInfoBuilder:
        self._indexing_status_info.id = id
        return self

    def indexing_status(self, indexing_status: str) -> IndexingStatusInfoBuilder:
        self._indexing_status_info.indexing_status = indexing_status
        return self

    def processing_started_at(self, processing_started_at: float) -> IndexingStatusInfoBuilder:
        self._indexing_status_info.processing_started_at = processing_started_at
        return self

    def parsing_completed_at(self, parsing_completed_at: float) -> IndexingStatusInfoBuilder:
        self._indexing_status_info.parsing_completed_at = parsing_completed_at
        return self

    def cleaning_completed_at(self, cleaning_completed_at: float) -> IndexingStatusInfoBuilder:
        self._indexing_status_info.cleaning_completed_at = cleaning_completed_at
        return self

    def splitting_completed_at(self, splitting_completed_at: float) -> IndexingStatusInfoBuilder:
        self._indexing_status_info.splitting_completed_at = splitting_completed_at
        return self

    def completed_at(self, completed_at: float) -> IndexingStatusInfoBuilder:
        self._indexing_status_info.completed_at = completed_at
        return self

    def paused_at(self, paused_at: float) -> IndexingStatusInfoBuilder:
        self._indexing_status_info.paused_at = paused_at
        return self

    def error(self, error: str) -> IndexingStatusInfoBuilder:
        self._indexing_status_info.error = error
        return self

    def stopped_at(self, stopped_at: float) -> IndexingStatusInfoBuilder:
        self._indexing_status_info.stopped_at = stopped_at
        return self

    def completed_segments(self, completed_segments: int) -> IndexingStatusInfoBuilder:
        self._indexing_status_info.completed_segments = completed_segments
        return self

    def total_segments(self, total_segments: int) -> IndexingStatusInfoBuilder:
        self._indexing_status_info.total_segments = total_segments
        return self
