from dify_oapi.core.model.base_response import BaseResponse

from .chat_message import ChatMessage


class GetConversationMessagesResponse(BaseResponse):
    limit: int | None = None
    has_more: bool | None = None
    data: list[ChatMessage] | None = None

    @staticmethod
    def builder() -> "GetConversationMessagesResponseBuilder":
        return GetConversationMessagesResponseBuilder()


class GetConversationMessagesResponseBuilder:
    def __init__(self):
        self._get_conversation_messages_response = GetConversationMessagesResponse()

    def build(self) -> GetConversationMessagesResponse:
        return self._get_conversation_messages_response

    def limit(self, limit: int) -> "GetConversationMessagesResponseBuilder":
        self._get_conversation_messages_response.limit = limit
        return self

    def has_more(self, has_more: bool) -> "GetConversationMessagesResponseBuilder":
        self._get_conversation_messages_response.has_more = has_more
        return self

    def data(self, data: list[ChatMessage]) -> "GetConversationMessagesResponseBuilder":
        self._get_conversation_messages_response.data = data
        return self
