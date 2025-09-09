from __future__ import annotations

from typing import TYPE_CHECKING

from pydantic import BaseModel

from .chatflow_types import FeedbackRating, MessageFileBelongsTo
from .retriever_resource import RetrieverResource

if TYPE_CHECKING:
    pass


class MessageFile(BaseModel):
    """Message file attachment model."""

    id: str | None = None
    type: str | None = None
    url: str | None = None
    belongs_to: MessageFileBelongsTo | None = None


class MessageFeedback(BaseModel):
    """Message feedback model."""

    rating: FeedbackRating | None = None


class ChatMessage(BaseModel):
    """Core chat message model."""

    id: str | None = None
    conversation_id: str | None = None
    inputs: dict[str, str] | None = None
    query: str | None = None
    answer: str | None = None
    message_files: list[MessageFile] | None = None
    feedback: MessageFeedback | None = None
    retriever_resources: list[RetrieverResource] | None = None
    created_at: int | None = None

    @staticmethod
    def builder() -> ChatMessageBuilder:
        return ChatMessageBuilder()


class ChatMessageBuilder:
    def __init__(self):
        self._chat_message = ChatMessage()

    def build(self) -> ChatMessage:
        return self._chat_message

    def id(self, id: str) -> ChatMessageBuilder:
        self._chat_message.id = id
        return self

    def conversation_id(self, conversation_id: str) -> ChatMessageBuilder:
        self._chat_message.conversation_id = conversation_id
        return self

    def inputs(self, inputs: dict[str, str]) -> ChatMessageBuilder:
        self._chat_message.inputs = inputs
        return self

    def query(self, query: str) -> ChatMessageBuilder:
        self._chat_message.query = query
        return self

    def answer(self, answer: str) -> ChatMessageBuilder:
        self._chat_message.answer = answer
        return self

    def message_files(self, message_files: list[MessageFile]) -> ChatMessageBuilder:
        self._chat_message.message_files = message_files
        return self

    def feedback(self, feedback: MessageFeedback) -> ChatMessageBuilder:
        self._chat_message.feedback = feedback
        return self

    def retriever_resources(self, retriever_resources: list[RetrieverResource]) -> ChatMessageBuilder:
        self._chat_message.retriever_resources = retriever_resources
        return self

    def created_at(self, created_at: int) -> ChatMessageBuilder:
        self._chat_message.created_at = created_at
        return self
