"""Message file model for Chat API."""

from __future__ import annotations

from pydantic import BaseModel, Field

from .chat_types import MessageBelongsTo


class MessageFile(BaseModel):
    """Message file model."""

    id: str | None = Field(None, description="File ID")
    type: str | None = Field(None, description="File type")
    url: str | None = Field(None, description="File URL")
    belongs_to: MessageBelongsTo | None = Field(None, description="Who the file belongs to")

    @classmethod
    def builder(cls) -> MessageFileBuilder:
        """Create a MessageFile builder."""
        return MessageFileBuilder()


class MessageFileBuilder:
    """Builder for MessageFile."""

    def __init__(self) -> None:
        self._message_file = MessageFile()

    def id(self, id: str) -> MessageFileBuilder:
        """Set file ID."""
        self._message_file.id = id
        return self

    def type(self, type: str) -> MessageFileBuilder:
        """Set file type."""
        self._message_file.type = type
        return self

    def url(self, url: str) -> MessageFileBuilder:
        """Set file URL."""
        self._message_file.url = url
        return self

    def belongs_to(self, belongs_to: MessageBelongsTo) -> MessageFileBuilder:
        """Set who the file belongs to."""
        self._message_file.belongs_to = belongs_to
        return self

    def build(self) -> MessageFile:
        """Build the MessageFile instance."""
        return self._message_file
