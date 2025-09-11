"""Message file model for Chat API."""

from __future__ import annotations

from pydantic import BaseModel

from .chat_types import MessageBelongsTo


class MessageFile(BaseModel):
    """Message file model."""

    id: str | None = None
    type: str | None = None
    url: str | None = None
    belongs_to: MessageBelongsTo | None = None

    @staticmethod
    def builder() -> MessageFileBuilder:
        return MessageFileBuilder()


class MessageFileBuilder:
    """Builder for MessageFile."""

    def __init__(self):
        self._message_file = MessageFile()

    def build(self) -> MessageFile:
        return self._message_file

    def id(self, id: str) -> MessageFileBuilder:
        self._message_file.id = id
        return self

    def type(self, type: str) -> MessageFileBuilder:
        self._message_file.type = type
        return self

    def url(self, url: str) -> MessageFileBuilder:
        self._message_file.url = url
        return self

    def belongs_to(self, belongs_to: MessageBelongsTo) -> MessageFileBuilder:
        self._message_file.belongs_to = belongs_to
        return self
