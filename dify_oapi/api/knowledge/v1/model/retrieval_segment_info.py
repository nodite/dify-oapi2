"""Retrieval segment information model for Knowledge Base API."""

from typing import Optional

from pydantic import BaseModel

from .segment_document_info import SegmentDocumentInfo


class RetrievalSegmentInfo(BaseModel):
    """Retrieval segment information model with builder pattern."""

    id: Optional[str] = None
    content: Optional[str] = None
    document: Optional[SegmentDocumentInfo] = None

    @staticmethod
    def builder() -> "RetrievalSegmentInfoBuilder":
        return RetrievalSegmentInfoBuilder()


class RetrievalSegmentInfoBuilder:
    """Builder for RetrievalSegmentInfo."""

    def __init__(self):
        self._retrieval_segment_info = RetrievalSegmentInfo()

    def build(self) -> RetrievalSegmentInfo:
        return self._retrieval_segment_info

    def id(self, id: str) -> "RetrievalSegmentInfoBuilder":
        self._retrieval_segment_info.id = id
        return self

    def content(self, content: str) -> "RetrievalSegmentInfoBuilder":
        self._retrieval_segment_info.content = content
        return self

    def document(self, document: SegmentDocumentInfo) -> "RetrievalSegmentInfoBuilder":
        self._retrieval_segment_info.document = document
        return self
