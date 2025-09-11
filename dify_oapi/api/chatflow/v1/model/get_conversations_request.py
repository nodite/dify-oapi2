from dify_oapi.core.enum import HttpMethod
from dify_oapi.core.model.base_request import BaseRequest

from .chatflow_types import SortBy


class GetConversationsRequest(BaseRequest):
    def __init__(self):
        super().__init__()

    @staticmethod
    def builder() -> "GetConversationsRequestBuilder":
        return GetConversationsRequestBuilder()


class GetConversationsRequestBuilder:
    def __init__(self):
        get_conversations_request = GetConversationsRequest()
        get_conversations_request.http_method = HttpMethod.GET
        get_conversations_request.uri = "/v1/conversations"
        self._get_conversations_request = get_conversations_request

    def build(self) -> GetConversationsRequest:
        return self._get_conversations_request

    def user(self, user: str) -> "GetConversationsRequestBuilder":
        self._get_conversations_request.add_query("user", user)
        return self

    def last_id(self, last_id: str) -> "GetConversationsRequestBuilder":
        self._get_conversations_request.add_query("last_id", last_id)
        return self

    def limit(self, limit: int) -> "GetConversationsRequestBuilder":
        self._get_conversations_request.add_query("limit", str(limit))
        return self

    def sort_by(self, sort_by: SortBy) -> "GetConversationsRequestBuilder":
        self._get_conversations_request.add_query("sort_by", sort_by)
        return self
