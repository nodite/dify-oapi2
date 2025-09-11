from dify_oapi.core.enum import HttpMethod
from dify_oapi.core.model.base_request import BaseRequest


class GetConversationMessagesRequest(BaseRequest):
    def __init__(self):
        super().__init__()

    @staticmethod
    def builder() -> "GetConversationMessagesRequestBuilder":
        return GetConversationMessagesRequestBuilder()


class GetConversationMessagesRequestBuilder:
    def __init__(self):
        get_conversation_messages_request = GetConversationMessagesRequest()
        get_conversation_messages_request.http_method = HttpMethod.GET
        get_conversation_messages_request.uri = "/v1/messages"
        self._get_conversation_messages_request = get_conversation_messages_request

    def build(self) -> GetConversationMessagesRequest:
        return self._get_conversation_messages_request

    def conversation_id(self, conversation_id: str) -> "GetConversationMessagesRequestBuilder":
        self._get_conversation_messages_request.add_query("conversation_id", conversation_id)
        return self

    def user(self, user: str) -> "GetConversationMessagesRequestBuilder":
        self._get_conversation_messages_request.add_query("user", user)
        return self

    def first_id(self, first_id: str) -> "GetConversationMessagesRequestBuilder":
        self._get_conversation_messages_request.add_query("first_id", first_id)
        return self

    def limit(self, limit: int) -> "GetConversationMessagesRequestBuilder":
        self._get_conversation_messages_request.add_query("limit", str(limit))
        return self
