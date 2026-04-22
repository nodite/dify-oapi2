import httpx
import pytest
import respx

from dify_oapi.api.chatflow.v1.model.get_suggested_questions_request import GetSuggestedQuestionsRequest
from dify_oapi.api.chatflow.v1.model.send_chat_message_request import SendChatMessageRequest
from dify_oapi.api.chatflow.v1.model.send_chat_message_request_body import SendChatMessageRequestBody
from dify_oapi.api.chatflow.v1.model.stop_chat_message_request import StopChatMessageRequest
from dify_oapi.api.chatflow.v1.model.stop_chat_message_request_body import StopChatMessageRequestBody
from dify_oapi.api.chatflow.v1.resource.chatflow import Chatflow


class TestChatflow:
    @pytest.fixture(autouse=True)
    def setup(self, config, request_option):
        self.resource = Chatflow(config)
        self.option = request_option

    @respx.mock
    def test_send(self):
        route = respx.post("https://api.dify.ai/v1/chat-messages").mock(
            return_value=httpx.Response(200, json={
                "id": "msg-123",
                "conversation_id": "conv-123",
                "task_id": "task-123",
                "answer": "Hi there!",
                "created_at": 1234567890,
            })
        )
        body = SendChatMessageRequestBody.builder().query("hello").user("u1").build()
        result = self.resource.send(
            SendChatMessageRequest.builder().request_body(body).build(), self.option
        )
        assert result.id == "msg-123"
        assert result.answer == "Hi there!"
        assert route.calls.last.request.headers["Authorization"] == "Bearer test-key"

    @respx.mock
    def test_send_stream(self):
        chunks = b"data: hello\n\ndata: world\n\n"
        route = respx.post("https://api.dify.ai/v1/chat-messages").mock(
            return_value=httpx.Response(200, content=chunks)
        )
        body = SendChatMessageRequestBody.builder().query("hello").user("u1").build()
        gen = self.resource.send(
            SendChatMessageRequest.builder().request_body(body).build(), self.option, stream=True
        )
        collected = b"".join(gen)
        assert b"hello" in collected
        assert route.calls.last.request.headers["Authorization"] == "Bearer test-key"

    @respx.mock
    def test_stop(self):
        route = respx.post(
            url__regex=r"https://api\.dify\.ai/v1/chat-messages/[^/]+/stop"
        ).mock(return_value=httpx.Response(200, json={"result": "success"}))
        body = StopChatMessageRequestBody.builder().user("u1").build()
        result = self.resource.stop(
            StopChatMessageRequest.builder().task_id("task-123").request_body(body).build(),
            self.option,
        )
        assert result.result == "success"
        assert route.calls.last.request.headers["Authorization"] == "Bearer test-key"

    @respx.mock
    def test_suggested(self):
        route = respx.get(
            url__regex=r"https://api\.dify\.ai/v1/messages/[^/]+/suggested"
        ).mock(return_value=httpx.Response(200, json={"result": "success", "data": ["Q1?"]}))
        result = self.resource.suggested(
            GetSuggestedQuestionsRequest.builder().message_id("msg-123").user("u1").build(),
            self.option,
        )
        assert result.data == ["Q1?"]
        assert route.calls.last.request.headers["Authorization"] == "Bearer test-key"
