import httpx
import pytest
import respx

from dify_oapi.api.chat.v1.model.get_suggested_questions_request import GetSuggestedQuestionsRequest
from dify_oapi.api.chat.v1.model.message_history_request import GetMessageHistoryRequest
from dify_oapi.api.chat.v1.resource.message import Message


class TestMessage:
    @pytest.fixture(autouse=True)
    def setup(self, config, request_option):
        self.resource = Message(config)
        self.option = request_option

    @respx.mock
    def test_history(self):
        route = respx.get("https://api.dify.ai/v1/messages").mock(
            return_value=httpx.Response(200, json={"data": [], "has_more": False, "limit": 20})
        )
        result = self.resource.history(
            GetMessageHistoryRequest.builder().conversation_id("conv-123").user("u1").build(),
            self.option,
        )
        assert result.data == []
        assert route.calls.last.request.headers["Authorization"] == "Bearer test-key"

    @respx.mock
    def test_suggested(self):
        route = respx.get(
            url__regex=r"https://api\.dify\.ai/v1/messages/[^/]+/suggested"
        ).mock(
            return_value=httpx.Response(200, json={"result": "success", "data": ["Q1?"]})
        )
        result = self.resource.suggested(
            GetSuggestedQuestionsRequest.builder().message_id("msg-123").user("u1").build(),
            self.option,
        )
        assert result.data == ["Q1?"]
        assert route.calls.last.request.headers["Authorization"] == "Bearer test-key"
