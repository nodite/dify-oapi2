"""Segment document information model for Knowledge Base API."""

from typing import Optional

from pydantic import BaseModel

from .knowledge_types import DataSourceType


class SegmentDocumentInfo(BaseModel):
    """Segment document information model with builder pattern."""

    id: Optional[str] = None
    data_source_type: Optional[DataSourceType] = None
    name: Optional[str] = None

    @staticmethod
    def builder() -> "SegmentDocumentInfoBuilder":
        return SegmentDocumentInfoBuilder()


class SegmentDocumentInfoBuilder:
    """Builder for SegmentDocumentInfo."""

    def __init__(self):
        self._segment_document_info = SegmentDocumentInfo()

    def build(self) -> SegmentDocumentInfo:
        return self._segment_document_info

    def id(self, id: str) -> "SegmentDocumentInfoBuilder":
        self._segment_document_info.id = id
        return self

    def data_source_type(self, data_source_type: DataSourceType) -> "SegmentDocumentInfoBuilder":
        self._segment_document_info.data_source_type = data_source_type
        return self

    def name(self, name: str) -> "SegmentDocumentInfoBuilder":
        self._segment_document_info.name = name
        return self
