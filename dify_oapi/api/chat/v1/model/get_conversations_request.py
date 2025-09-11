from __future__ import annotations

from dify_oapi.api.chat.v1.model.chat_types import SortBy
from dify_oapi.core.enum import HttpMethod
from dify_oapi.core.model.base_request import BaseRequest


class GetConversationsRequest(BaseRequest):
    def __init__(self):
        super().__init__()
        self.user: str | None = None
        self.last_id: str | None = None
        self.limit: int | None = None
        self.sort_by: SortBy | None = None

    @staticmethod
    def builder() -> GetConversationsRequestBuilder:
        return GetConversationsRequestBuilder()


class GetConversationsRequestBuilder:
    def __init__(self):
        get_conversations_request = GetConversationsRequest()
        get_conversations_request.http_method = HttpMethod.GET
        get_conversations_request.uri = "/v1/conversations"
        self._get_conversations_request = get_conversations_request

    def user(self, user: str) -> GetConversationsRequestBuilder:
        self._get_conversations_request.user = user
        self._get_conversations_request.add_query("user", user)
        return self

    def last_id(self, last_id: str) -> GetConversationsRequestBuilder:
        self._get_conversations_request.last_id = last_id
        self._get_conversations_request.add_query("last_id", last_id)
        return self

    def limit(self, limit: int) -> GetConversationsRequestBuilder:
        self._get_conversations_request.limit = limit
        self._get_conversations_request.add_query("limit", limit)
        return self

    def sort_by(self, sort_by: SortBy) -> GetConversationsRequestBuilder:
        self._get_conversations_request.sort_by = sort_by
        self._get_conversations_request.add_query("sort_by", sort_by)
        return self

    def build(self) -> GetConversationsRequest:
        return self._get_conversations_request
