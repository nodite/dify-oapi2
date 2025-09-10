from dify_oapi.core.enum import HttpMethod
from dify_oapi.core.model.base_request import BaseRequest


class GetConversationVariablesRequest(BaseRequest):
    def __init__(self):
        super().__init__()
        self.conversation_id: str | None = None

    @staticmethod
    def builder() -> "GetConversationVariablesRequestBuilder":
        return GetConversationVariablesRequestBuilder()


class GetConversationVariablesRequestBuilder:
    def __init__(self):
        get_conversation_variables_request = GetConversationVariablesRequest()
        get_conversation_variables_request.http_method = HttpMethod.GET
        get_conversation_variables_request.uri = "/v1/conversations/:conversation_id/variables"
        self._get_conversation_variables_request = get_conversation_variables_request

    def build(self) -> GetConversationVariablesRequest:
        return self._get_conversation_variables_request

    def conversation_id(self, conversation_id: str) -> "GetConversationVariablesRequestBuilder":
        self._get_conversation_variables_request.conversation_id = conversation_id
        self._get_conversation_variables_request.paths["conversation_id"] = conversation_id
        return self

    def user(self, user: str) -> "GetConversationVariablesRequestBuilder":
        self._get_conversation_variables_request.add_query("user", user)
        return self

    def last_id(self, last_id: str) -> "GetConversationVariablesRequestBuilder":
        self._get_conversation_variables_request.add_query("last_id", last_id)
        return self

    def limit(self, limit: int) -> "GetConversationVariablesRequestBuilder":
        self._get_conversation_variables_request.add_query("limit", str(limit))
        return self

    def variable_name(self, variable_name: str) -> "GetConversationVariablesRequestBuilder":
        self._get_conversation_variables_request.add_query("variable_name", variable_name)
        return self
