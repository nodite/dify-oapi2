"""Batch information model for Knowledge Base API."""

from typing import Optional

from pydantic import BaseModel


class BatchInfo(BaseModel):
    """Batch information model with builder pattern."""

    batch: Optional[str] = None
    data: Optional[list[dict]] = None
    total: Optional[int] = None
    completed: Optional[int] = None
    failed: Optional[int] = None
    processing: Optional[int] = None

    @staticmethod
    def builder() -> "BatchInfoBuilder":
        return BatchInfoBuilder()


class BatchInfoBuilder:
    """Builder for BatchInfo."""

    def __init__(self):
        self._batch_info = BatchInfo()

    def build(self) -> BatchInfo:
        return self._batch_info

    def batch(self, batch: str) -> "BatchInfoBuilder":
        self._batch_info.batch = batch
        return self

    def data(self, data: list[dict]) -> "BatchInfoBuilder":
        self._batch_info.data = data
        return self

    def total(self, total: int) -> "BatchInfoBuilder":
        self._batch_info.total = total
        return self

    def completed(self, completed: int) -> "BatchInfoBuilder":
        self._batch_info.completed = completed
        return self

    def failed(self, failed: int) -> "BatchInfoBuilder":
        self._batch_info.failed = failed
        return self

    def processing(self, processing: int) -> "BatchInfoBuilder":
        self._batch_info.processing = processing
        return self
