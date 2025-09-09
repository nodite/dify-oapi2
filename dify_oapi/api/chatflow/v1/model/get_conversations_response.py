from dify_oapi.core.model.base_response import BaseResponse

from .conversation_info import ConversationInfo


class GetConversationsResponse(BaseResponse):
    limit: int | None = None
    has_more: bool | None = None
    data: list[ConversationInfo] | None = None

    @staticmethod
    def builder() -> "GetConversationsResponseBuilder":
        return GetConversationsResponseBuilder()


class GetConversationsResponseBuilder:
    def __init__(self):
        self._get_conversations_response = GetConversationsResponse()

    def build(self) -> GetConversationsResponse:
        return self._get_conversations_response

    def limit(self, limit: int) -> "GetConversationsResponseBuilder":
        self._get_conversations_response.limit = limit
        return self

    def has_more(self, has_more: bool) -> "GetConversationsResponseBuilder":
        self._get_conversations_response.has_more = has_more
        return self

    def data(self, data: list[ConversationInfo]) -> "GetConversationsResponseBuilder":
        self._get_conversations_response.data = data
        return self
