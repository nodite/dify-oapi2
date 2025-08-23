from __future__ import annotations

from pydantic import BaseModel


class FeedbackInfo(BaseModel):
    id: str | None = None
    rating: str | None = None
    content: str | None = None
    from_source: str | None = None
    from_end_user_id: str | None = None
    from_account_id: str | None = None
    created_at: int | None = None

    @staticmethod
    def builder() -> FeedbackInfoBuilder:
        return FeedbackInfoBuilder()


class FeedbackInfoBuilder:
    def __init__(self):
        self._feedback_info = FeedbackInfo()

    def build(self) -> FeedbackInfo:
        return self._feedback_info

    def id(self, id: str) -> FeedbackInfoBuilder:
        self._feedback_info.id = id
        return self

    def rating(self, rating: str) -> FeedbackInfoBuilder:
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

    def created_at(self, created_at: int) -> FeedbackInfoBuilder:
        self._feedback_info.created_at = created_at
        return self
