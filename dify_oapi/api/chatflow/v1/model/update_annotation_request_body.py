from pydantic import BaseModel


class UpdateAnnotationRequestBody(BaseModel):
    """Request body for updating annotation."""

    question: str | None = None
    answer: str | None = None

    @staticmethod
    def builder() -> "UpdateAnnotationRequestBodyBuilder":
        return UpdateAnnotationRequestBodyBuilder()


class UpdateAnnotationRequestBodyBuilder:
    def __init__(self):
        self._update_annotation_request_body = UpdateAnnotationRequestBody()

    def build(self) -> UpdateAnnotationRequestBody:
        return self._update_annotation_request_body

    def question(self, question: str) -> "UpdateAnnotationRequestBodyBuilder":
        self._update_annotation_request_body.question = question
        return self

    def answer(self, answer: str) -> "UpdateAnnotationRequestBodyBuilder":
        self._update_annotation_request_body.answer = answer
        return self
