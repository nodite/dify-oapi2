"""Annotation information model for Chat API."""

from __future__ import annotations

from pydantic import BaseModel, Field


class AnnotationInfo(BaseModel):
    """Annotation information model."""

    id: str | None = Field(None, description="Annotation ID")
    question: str | None = Field(None, description="Annotation question")
    answer: str | None = Field(None, description="Annotation answer")
    hit_count: int | None = Field(None, description="Hit count")
    created_at: int | None = Field(None, description="Creation timestamp")

    @classmethod
    def builder(cls) -> AnnotationInfoBuilder:
        """Create an AnnotationInfo builder."""
        return AnnotationInfoBuilder()


class AnnotationInfoBuilder:
    """Builder for AnnotationInfo."""

    def __init__(self) -> None:
        self._annotation_info = AnnotationInfo()

    def id(self, id: str) -> AnnotationInfoBuilder:
        """Set annotation ID."""
        self._annotation_info.id = id
        return self

    def question(self, question: str) -> AnnotationInfoBuilder:
        """Set annotation question."""
        self._annotation_info.question = question
        return self

    def answer(self, answer: str) -> AnnotationInfoBuilder:
        """Set annotation answer."""
        self._annotation_info.answer = answer
        return self

    def hit_count(self, hit_count: int) -> AnnotationInfoBuilder:
        """Set hit count."""
        self._annotation_info.hit_count = hit_count
        return self

    def created_at(self, created_at: int) -> AnnotationInfoBuilder:
        """Set creation timestamp."""
        self._annotation_info.created_at = created_at
        return self

    def build(self) -> AnnotationInfo:
        """Build the AnnotationInfo instance."""
        return self._annotation_info
