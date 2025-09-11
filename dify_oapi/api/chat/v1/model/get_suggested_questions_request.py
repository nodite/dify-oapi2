from __future__ import annotations

from dify_oapi.core.enum import HttpMethod
from dify_oapi.core.model.base_request import BaseRequest


class GetSuggestedQuestionsRequest(BaseRequest):
    def __init__(self) -> None:
        super().__init__()
        self.message_id: str | None = None
        self.user: str | None = None

    @staticmethod
    def builder() -> GetSuggestedQuestionsRequestBuilder:
        return GetSuggestedQuestionsRequestBuilder()


class GetSuggestedQuestionsRequestBuilder:
    def __init__(self) -> None:
        get_suggested_questions_request = GetSuggestedQuestionsRequest()
        get_suggested_questions_request.http_method = HttpMethod.GET
        get_suggested_questions_request.uri = "/v1/messages/:message_id/suggested"
        self._get_suggested_questions_request = get_suggested_questions_request

    def message_id(self, message_id: str) -> GetSuggestedQuestionsRequestBuilder:
        self._get_suggested_questions_request.message_id = message_id
        self._get_suggested_questions_request.paths["message_id"] = message_id
        return self

    def user(self, user: str) -> GetSuggestedQuestionsRequestBuilder:
        self._get_suggested_questions_request.user = user
        self._get_suggested_questions_request.add_query("user", user)
        return self

    def build(self) -> GetSuggestedQuestionsRequest:
        return self._get_suggested_questions_request
