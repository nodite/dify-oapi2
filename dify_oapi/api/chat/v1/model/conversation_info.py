"""Conversation information model for Chat API."""

from __future__ import annotations

from typing import Any

from pydantic import BaseModel, Field

from .chat_types import ConversationStatus


class ConversationInfo(BaseModel):
    """Conversation information model."""

    id: str | None = Field(None, description="Conversation ID")
    name: str | None = Field(None, description="Conversation name")
    inputs: dict[str, Any] | None = Field(None, description="Input parameters")
    status: ConversationStatus | None = Field(None, description="Conversation status")
    introduction: str | None = Field(None, description="Conversation introduction")
    created_at: int | None = Field(None, description="Creation timestamp")
    updated_at: int | None = Field(None, description="Update timestamp")

    @classmethod
    def builder(cls) -> ConversationInfoBuilder:
        """Create a ConversationInfo builder."""
        return ConversationInfoBuilder()


class ConversationInfoBuilder:
    """Builder for ConversationInfo."""

    def __init__(self) -> None:
        self._conversation_info = ConversationInfo()

    def id(self, id: str) -> ConversationInfoBuilder:
        """Set conversation ID."""
        self._conversation_info.id = id
        return self

    def name(self, name: str) -> ConversationInfoBuilder:
        """Set conversation name."""
        self._conversation_info.name = name
        return self

    def inputs(self, inputs: dict[str, Any]) -> ConversationInfoBuilder:
        """Set input parameters."""
        self._conversation_info.inputs = inputs
        return self

    def status(self, status: ConversationStatus) -> ConversationInfoBuilder:
        """Set conversation status."""
        self._conversation_info.status = status
        return self

    def introduction(self, introduction: str) -> ConversationInfoBuilder:
        """Set conversation introduction."""
        self._conversation_info.introduction = introduction
        return self

    def created_at(self, created_at: int) -> ConversationInfoBuilder:
        """Set creation timestamp."""
        self._conversation_info.created_at = created_at
        return self

    def updated_at(self, updated_at: int) -> ConversationInfoBuilder:
        """Set update timestamp."""
        self._conversation_info.updated_at = updated_at
        return self

    def build(self) -> ConversationInfo:
        """Build the ConversationInfo instance."""
        return self._conversation_info
