import httpx
import pytest
import respx

from dify_oapi.api.chat.v1.model.chat_request import ChatRequest
from dify_oapi.api.chat.v1.model.chat_request_body import ChatRequestBody
from dify_oapi.api.chat.v1.model.get_suggested_questions_request import GetSuggestedQuestionsRequest
from dify_oapi.api.chat.v1.model.stop_chat_request import StopChatRequest
from dify_oapi.api.chat.v1.model.stop_chat_request_body import StopChatRequestBody
from dify_oapi.api.chat.v1.resource.chat import Chat


class TestChatAsync:
    @pytest.fixture(autouse=True)
    def setup(self, config, request_option):
        self.resource = Chat(config)
        self.option = request_option

    @respx.mock
    async def test_achat(self):
        route = respx.post("https://api.dify.ai/v1/chat-messages").mock(
            return_value=httpx.Response(200, json={
                "message_id": "msg-123",
                "conversation_id": "conv-123",
                "answer": "Hello!",
                "mode": "chat",
                "created_at": 1234567890,
            })
        )
        body = ChatRequestBody.builder().query("hi").user("u1").build()
        result = await self.resource.achat(
            ChatRequest.builder().request_body(body).build(), self.option
        )
        assert result.answer == "Hello!"
        assert result.message_id == "msg-123"
        assert route.calls.last.request.headers["Authorization"] == "Bearer test-key"

    @respx.mock
    async def test_astop(self):
        route = respx.post(
            url__regex=r"https://api\.dify\.ai/v1/chat-messages/[^/]+/stop"
        ).mock(return_value=httpx.Response(200, json={"result": "success"}))
        body = StopChatRequestBody.builder().user("u1").build()
        result = await self.resource.astop(
            StopChatRequest.builder().task_id("task-123").request_body(body).build(),
            self.option,
        )
        assert result.result == "success"
        assert route.calls.last.request.headers["Authorization"] == "Bearer test-key"

    @respx.mock
    async def test_asuggested(self):
        route = respx.get(
            url__regex=r"https://api\.dify\.ai/v1/messages/[^/]+/suggested"
        ).mock(return_value=httpx.Response(200, json={"data": ["Follow up?"]}))
        result = await self.resource.asuggested(
            GetSuggestedQuestionsRequest.builder().message_id("msg-123").user("u1").build(),
            self.option,
        )
        assert result.data == ["Follow up?"]
        assert route.calls.last.request.headers["Authorization"] == "Bearer test-key"
