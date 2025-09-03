from __future__ import annotations

from pydantic import BaseModel, Field


class UpdateAnnotationRequestBody(BaseModel):
    """Request body for updating annotation."""

    question: str = Field(..., description="Updated annotation question")
    answer: str = Field(..., description="Updated annotation answer")

    @classmethod
    def builder(cls) -> UpdateAnnotationRequestBodyBuilder:
        """Create an UpdateAnnotationRequestBody builder."""
        return UpdateAnnotationRequestBodyBuilder()


class UpdateAnnotationRequestBodyBuilder:
    """Builder for UpdateAnnotationRequestBody."""

    def __init__(self) -> None:
        self._update_annotation_request_body = UpdateAnnotationRequestBody(question="", answer="")

    def question(self, question: str) -> UpdateAnnotationRequestBodyBuilder:
        """Set updated annotation question."""
        self._update_annotation_request_body.question = question
        return self

    def answer(self, answer: str) -> UpdateAnnotationRequestBodyBuilder:
        """Set updated annotation answer."""
        self._update_annotation_request_body.answer = answer
        return self

    def build(self) -> UpdateAnnotationRequestBody:
        """Build the UpdateAnnotationRequestBody instance."""
        return self._update_annotation_request_body
