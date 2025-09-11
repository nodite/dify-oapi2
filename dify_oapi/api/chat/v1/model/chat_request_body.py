from __future__ import annotations

from typing import Any

from pydantic import BaseModel

from .chat_file import ChatFile
from .chat_types import ResponseMode


class ChatRequestBody(BaseModel):
    """Chat request body model."""

    query: str | None = None
    inputs: dict[str, Any] | None = None
    response_mode: ResponseMode | None = "streaming"
    user: str | None = None
    conversation_id: str | None = None
    files: list[ChatFile] | None = None
    auto_generate_name: bool | None = None

    @classmethod
    def builder(cls) -> ChatRequestBodyBuilder:
        return ChatRequestBodyBuilder()


class ChatRequestBodyBuilder:
    """Builder for ChatRequestBody."""

    def __init__(self) -> None:
        self._chat_request_body = ChatRequestBody()

    def query(self, query: str) -> ChatRequestBodyBuilder:
        """Set user query."""
        self._chat_request_body.query = query
        return self

    def inputs(self, inputs: dict[str, Any]) -> ChatRequestBodyBuilder:
        """Set input parameters."""
        self._chat_request_body.inputs = inputs
        return self

    def response_mode(self, response_mode: ResponseMode) -> ChatRequestBodyBuilder:
        """Set response mode."""
        self._chat_request_body.response_mode = response_mode
        return self

    def user(self, user: str) -> ChatRequestBodyBuilder:
        """Set user identifier."""
        self._chat_request_body.user = user
        return self

    def conversation_id(self, conversation_id: str) -> ChatRequestBodyBuilder:
        """Set conversation ID."""
        self._chat_request_body.conversation_id = conversation_id
        return self

    def files(self, files: list[ChatFile]) -> ChatRequestBodyBuilder:
        """Set files."""
        self._chat_request_body.files = files
        return self

    def auto_generate_name(self, auto_generate_name: bool) -> ChatRequestBodyBuilder:
        """Set auto generate name flag."""
        self._chat_request_body.auto_generate_name = auto_generate_name
        return self

    def build(self) -> ChatRequestBody:
        """Build the ChatRequestBody instance."""
        return self._chat_request_body
