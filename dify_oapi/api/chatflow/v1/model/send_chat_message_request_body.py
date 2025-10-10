from typing import Any

from pydantic import BaseModel

from .chat_file import ChatFile
from .chatflow_types import ResponseMode


class SendChatMessageRequestBody(BaseModel):
    query: str | None = None
    #TODO: Create a more specific models for inputs values
    inputs: dict[str, Any] | None = None
    response_mode: ResponseMode | None = None
    user: str | None = None
    conversation_id: str | None = None
    files: list[ChatFile] | None = None
    auto_generate_name: bool | None = None

    @staticmethod
    def builder() -> "SendChatMessageRequestBodyBuilder":
        return SendChatMessageRequestBodyBuilder()


class SendChatMessageRequestBodyBuilder:
    def __init__(self):
        self._send_chat_message_request_body = SendChatMessageRequestBody()

    def build(self) -> SendChatMessageRequestBody:
        return self._send_chat_message_request_body

    def query(self, query: str) -> "SendChatMessageRequestBodyBuilder":
        self._send_chat_message_request_body.query = query
        return self

    def inputs(self, inputs: dict[str, str]) -> "SendChatMessageRequestBodyBuilder":
        self._send_chat_message_request_body.inputs = inputs
        return self

    def response_mode(self, response_mode: ResponseMode) -> "SendChatMessageRequestBodyBuilder":
        self._send_chat_message_request_body.response_mode = response_mode
        return self

    def user(self, user: str) -> "SendChatMessageRequestBodyBuilder":
        self._send_chat_message_request_body.user = user
        return self

    def conversation_id(self, conversation_id: str) -> "SendChatMessageRequestBodyBuilder":
        self._send_chat_message_request_body.conversation_id = conversation_id
        return self

    def files(self, files: list[ChatFile]) -> "SendChatMessageRequestBodyBuilder":
        self._send_chat_message_request_body.files = files
        return self

    def auto_generate_name(self, auto_generate_name: bool) -> "SendChatMessageRequestBodyBuilder":
        self._send_chat_message_request_body.auto_generate_name = auto_generate_name
        return self
