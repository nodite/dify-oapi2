from __future__ import annotations

from pydantic import BaseModel, Field


class CreateAnnotationRequestBody(BaseModel):
    """Request body for creating annotation."""

    question: str = Field(..., description="Annotation question")
    answer: str = Field(..., description="Annotation answer")

    @classmethod
    def builder(cls) -> CreateAnnotationRequestBodyBuilder:
        """Create a CreateAnnotationRequestBody builder."""
        return CreateAnnotationRequestBodyBuilder()


class CreateAnnotationRequestBodyBuilder:
    """Builder for CreateAnnotationRequestBody."""

    def __init__(self) -> None:
        self._create_annotation_request_body = CreateAnnotationRequestBody(question="", answer="")

    def question(self, question: str) -> CreateAnnotationRequestBodyBuilder:
        """Set annotation question."""
        self._create_annotation_request_body.question = question
        return self

    def answer(self, answer: str) -> CreateAnnotationRequestBodyBuilder:
        """Set annotation answer."""
        self._create_annotation_request_body.answer = answer
        return self

    def build(self) -> CreateAnnotationRequestBody:
        """Build the CreateAnnotationRequestBody instance."""
        return self._create_annotation_request_body
