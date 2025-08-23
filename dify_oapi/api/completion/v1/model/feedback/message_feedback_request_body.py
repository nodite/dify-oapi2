from __future__ import annotations

from pydantic import BaseModel

from ..completion.completion_types import FeedbackRating


class MessageFeedbackRequestBody(BaseModel):
    rating: FeedbackRating | None = None
    user: str | None = None
    content: str | None = None

    @staticmethod
    def builder() -> MessageFeedbackRequestBodyBuilder:
        return MessageFeedbackRequestBodyBuilder()


class MessageFeedbackRequestBodyBuilder:
    def __init__(self):
        self._message_feedback_request_body = MessageFeedbackRequestBody()

    def build(self) -> MessageFeedbackRequestBody:
        return self._message_feedback_request_body

    def rating(self, rating: FeedbackRating) -> MessageFeedbackRequestBodyBuilder:
        self._message_feedback_request_body.rating = rating
        return self

    def user(self, user: str) -> MessageFeedbackRequestBodyBuilder:
        self._message_feedback_request_body.user = user
        return self

    def content(self, content: str) -> MessageFeedbackRequestBodyBuilder:
        self._message_feedback_request_body.content = content
        return self
