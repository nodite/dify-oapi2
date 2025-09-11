from __future__ import annotations

from dify_oapi.core.enum import HttpMethod
from dify_oapi.core.model.base_request import BaseRequest


class GetMessageHistoryRequest(BaseRequest):
    def __init__(self):
        super().__init__()
        self.conversation_id: str | None = None
        self.user: str | None = None
        self.first_id: str | None = None
        self.limit: int | None = None

    @staticmethod
    def builder() -> GetMessageHistoryRequestBuilder:
        return GetMessageHistoryRequestBuilder()


class GetMessageHistoryRequestBuilder:
    def __init__(self):
        get_message_history_request = GetMessageHistoryRequest()
        get_message_history_request.http_method = HttpMethod.GET
        get_message_history_request.uri = "/v1/messages"
        self._get_message_history_request = get_message_history_request

    def conversation_id(self, conversation_id: str) -> GetMessageHistoryRequestBuilder:
        self._get_message_history_request.conversation_id = conversation_id
        self._get_message_history_request.add_query("conversation_id", conversation_id)
        return self

    def user(self, user: str) -> GetMessageHistoryRequestBuilder:
        self._get_message_history_request.user = user
        self._get_message_history_request.add_query("user", user)
        return self

    def first_id(self, first_id: str) -> GetMessageHistoryRequestBuilder:
        self._get_message_history_request.first_id = first_id
        self._get_message_history_request.add_query("first_id", first_id)
        return self

    def limit(self, limit: int) -> GetMessageHistoryRequestBuilder:
        self._get_message_history_request.limit = limit
        self._get_message_history_request.add_query("limit", limit)
        return self

    def build(self) -> GetMessageHistoryRequest:
        return self._get_message_history_request
