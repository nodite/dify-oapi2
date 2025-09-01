"""Feedback information model for Chat API."""

from __future__ import annotations

from pydantic import BaseModel, Field

from .chat_types import Rating


class FeedbackInfo(BaseModel):
    """Feedback information model."""

    id: str | None = Field(None, description="Feedback ID")
    app_id: str | None = Field(None, description="Application ID")
    conversation_id: str | None = Field(None, description="Conversation ID")
    message_id: str | None = Field(None, description="Message ID")
    rating: Rating | None = Field(None, description="Feedback rating")
    content: str | None = Field(None, description="Feedback content")
    from_source: str | None = Field(None, description="Feedback source")
    from_end_user_id: str | None = Field(None, description="End user ID")
    from_account_id: str | None = Field(None, description="Account ID")
    created_at: str | None = Field(None, description="Creation timestamp")
    updated_at: str | None = Field(None, description="Update timestamp")

    @classmethod
    def builder(cls) -> FeedbackInfoBuilder:
        """Create a FeedbackInfo builder."""
        return FeedbackInfoBuilder()


class FeedbackInfoBuilder:
    """Builder for FeedbackInfo."""

    def __init__(self) -> None:
        self._feedback_info = FeedbackInfo()

    def id(self, id: str) -> FeedbackInfoBuilder:
        """Set feedback ID."""
        self._feedback_info.id = id
        return self

    def app_id(self, app_id: str) -> FeedbackInfoBuilder:
        """Set application ID."""
        self._feedback_info.app_id = app_id
        return self

    def conversation_id(self, conversation_id: str) -> FeedbackInfoBuilder:
        """Set conversation ID."""
        self._feedback_info.conversation_id = conversation_id
        return self

    def message_id(self, message_id: str) -> FeedbackInfoBuilder:
        """Set message ID."""
        self._feedback_info.message_id = message_id
        return self

    def rating(self, rating: Rating) -> FeedbackInfoBuilder:
        """Set feedback rating."""
        self._feedback_info.rating = rating
        return self

    def content(self, content: str) -> FeedbackInfoBuilder:
        """Set feedback content."""
        self._feedback_info.content = content
        return self

    def from_source(self, from_source: str) -> FeedbackInfoBuilder:
        """Set feedback source."""
        self._feedback_info.from_source = from_source
        return self

    def from_end_user_id(self, from_end_user_id: str) -> FeedbackInfoBuilder:
        """Set end user ID."""
        self._feedback_info.from_end_user_id = from_end_user_id
        return self

    def from_account_id(self, from_account_id: str) -> FeedbackInfoBuilder:
        """Set account ID."""
        self._feedback_info.from_account_id = from_account_id
        return self

    def created_at(self, created_at: str) -> FeedbackInfoBuilder:
        """Set creation timestamp."""
        self._feedback_info.created_at = created_at
        return self

    def updated_at(self, updated_at: str) -> FeedbackInfoBuilder:
        """Set update timestamp."""
        self._feedback_info.updated_at = updated_at
        return self

    def build(self) -> FeedbackInfo:
        """Build the FeedbackInfo instance."""
        return self._feedback_info
