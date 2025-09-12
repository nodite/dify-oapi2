from typing import Literal

from pydantic import BaseModel

Rating = Literal["like", "dislike"]


class SubmitFeedbackRequestBody(BaseModel):
    rating: Rating | None = None
    user: str
    content: str | None = None

    @staticmethod
    def builder() -> "SubmitFeedbackRequestBodyBuilder":
        return SubmitFeedbackRequestBodyBuilder()


class SubmitFeedbackRequestBodyBuilder:
    def __init__(self) -> None:
        self._submit_feedback_request_body = SubmitFeedbackRequestBody(user="")

    def rating(self, rating: Rating | None) -> "SubmitFeedbackRequestBodyBuilder":
        self._submit_feedback_request_body.rating = rating
        return self

    def user(self, user: str) -> "SubmitFeedbackRequestBodyBuilder":
        self._submit_feedback_request_body.user = user
        return self

    def content(self, content: str | None) -> "SubmitFeedbackRequestBodyBuilder":
        self._submit_feedback_request_body.content = content
        return self

    def build(self) -> SubmitFeedbackRequestBody:
        return self._submit_feedback_request_body
