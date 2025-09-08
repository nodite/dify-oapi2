from __future__ import annotations

from pydantic import BaseModel

from .chat_types import Rating


class FeedbackInfo(BaseModel):
    id: str | None = None
    app_id: str | None = None
    conversation_id: str | None = None
    message_id: str | None = None
    rating: Rating | None = None
    content: str | None = None
    from_source: str | None = None
    from_end_user_id: str | None = None
    from_account_id: str | None = None
    created_at: str | None = None
    updated_at: str | None = None

    @staticmethod
    def builder() -> FeedbackInfoBuilder:
        return FeedbackInfoBuilder()


class FeedbackInfoBuilder:
    def __init__(self):
        self._feedback_info = FeedbackInfo()

    def id(self, id: str) -> FeedbackInfoBuilder:
        self._feedback_info.id = id
        return self

    def app_id(self, app_id: str) -> FeedbackInfoBuilder:
        self._feedback_info.app_id = app_id
        return self

    def conversation_id(self, conversation_id: str) -> FeedbackInfoBuilder:
        self._feedback_info.conversation_id = conversation_id
        return self

    def message_id(self, message_id: str) -> FeedbackInfoBuilder:
        self._feedback_info.message_id = message_id
        return self

    def rating(self, rating: Rating) -> FeedbackInfoBuilder:
        self._feedback_info.rating = rating
        return self

    def content(self, content: str) -> FeedbackInfoBuilder:
        self._feedback_info.content = content
        return self

    def from_source(self, from_source: str) -> FeedbackInfoBuilder:
        self._feedback_info.from_source = from_source
        return self

    def from_end_user_id(self, from_end_user_id: str) -> FeedbackInfoBuilder:
        self._feedback_info.from_end_user_id = from_end_user_id
        return self

    def from_account_id(self, from_account_id: str) -> FeedbackInfoBuilder:
        self._feedback_info.from_account_id = from_account_id
        return self

    def created_at(self, created_at: str) -> FeedbackInfoBuilder:
        self._feedback_info.created_at = created_at
        return self

    def updated_at(self, updated_at: str) -> FeedbackInfoBuilder:
        self._feedback_info.updated_at = updated_at
        return self

    def build(self) -> FeedbackInfo:
        return self._feedback_info
