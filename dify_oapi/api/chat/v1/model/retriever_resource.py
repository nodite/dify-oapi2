"""Retriever resource model for Chat API."""

from __future__ import annotations

from pydantic import BaseModel, Field


class RetrieverResource(BaseModel):
    """Retriever resource model."""

    position: int | None = Field(None, description="Position of the resource")
    dataset_id: str | None = Field(None, description="Dataset ID")
    dataset_name: str | None = Field(None, description="Dataset name")
    document_id: str | None = Field(None, description="Document ID")
    document_name: str | None = Field(None, description="Document name")
    segment_id: str | None = Field(None, description="Segment ID")
    score: float | None = Field(None, description="Relevance score")
    content: str | None = Field(None, description="Content snippet")

    @classmethod
    def builder(cls) -> RetrieverResourceBuilder:
        """Create a RetrieverResource builder."""
        return RetrieverResourceBuilder()


class RetrieverResourceBuilder:
    """Builder for RetrieverResource."""

    def __init__(self) -> None:
        self._retriever_resource = RetrieverResource()

    def position(self, position: int) -> RetrieverResourceBuilder:
        """Set position."""
        self._retriever_resource.position = position
        return self

    def dataset_id(self, dataset_id: str) -> RetrieverResourceBuilder:
        """Set dataset ID."""
        self._retriever_resource.dataset_id = dataset_id
        return self

    def dataset_name(self, dataset_name: str) -> RetrieverResourceBuilder:
        """Set dataset name."""
        self._retriever_resource.dataset_name = dataset_name
        return self

    def document_id(self, document_id: str) -> RetrieverResourceBuilder:
        """Set document ID."""
        self._retriever_resource.document_id = document_id
        return self

    def document_name(self, document_name: str) -> RetrieverResourceBuilder:
        """Set document name."""
        self._retriever_resource.document_name = document_name
        return self

    def segment_id(self, segment_id: str) -> RetrieverResourceBuilder:
        """Set segment ID."""
        self._retriever_resource.segment_id = segment_id
        return self

    def score(self, score: float) -> RetrieverResourceBuilder:
        """Set relevance score."""
        self._retriever_resource.score = score
        return self

    def content(self, content: str) -> RetrieverResourceBuilder:
        """Set content snippet."""
        self._retriever_resource.content = content
        return self

    def build(self) -> RetrieverResource:
        """Build the RetrieverResource instance."""
        return self._retriever_resource
