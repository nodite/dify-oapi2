from __future__ import annotations

from pydantic import BaseModel


class CreateAnnotationRequestBody(BaseModel):
    """Request body for creating annotation."""

    question: str = ""
    answer: str = ""

    @staticmethod
    def builder() -> CreateAnnotationRequestBodyBuilder:
        return CreateAnnotationRequestBodyBuilder()


class CreateAnnotationRequestBodyBuilder:
    """Builder for CreateAnnotationRequestBody."""

    def __init__(self):
        self._create_annotation_request_body = CreateAnnotationRequestBody()

    def build(self) -> CreateAnnotationRequestBody:
        return self._create_annotation_request_body

    def question(self, question: str) -> CreateAnnotationRequestBodyBuilder:
        self._create_annotation_request_body.question = question
        return self

    def answer(self, answer: str) -> CreateAnnotationRequestBodyBuilder:
        self._create_annotation_request_body.answer = answer
        return self
