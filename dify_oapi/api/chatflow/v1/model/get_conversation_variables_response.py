from dify_oapi.core.model.base_response import BaseResponse

from .conversation_variable import ConversationVariable


class GetConversationVariablesResponse(BaseResponse):
    limit: int | None = None
    has_more: bool | None = None
    data: list[ConversationVariable] | None = None

    @staticmethod
    def builder() -> "GetConversationVariablesResponseBuilder":
        return GetConversationVariablesResponseBuilder()


class GetConversationVariablesResponseBuilder:
    def __init__(self):
        self._get_conversation_variables_response = GetConversationVariablesResponse()

    def build(self) -> GetConversationVariablesResponse:
        return self._get_conversation_variables_response

    def limit(self, limit: int) -> "GetConversationVariablesResponseBuilder":
        self._get_conversation_variables_response.limit = limit
        return self

    def has_more(self, has_more: bool) -> "GetConversationVariablesResponseBuilder":
        self._get_conversation_variables_response.has_more = has_more
        return self

    def data(self, data: list[ConversationVariable]) -> "GetConversationVariablesResponseBuilder":
        self._get_conversation_variables_response.data = data
        return self
