import httpx
import pytest
import respx

from dify_oapi.api.chatflow.v1.model.send_chat_message_request import SendChatMessageRequest
from dify_oapi.api.chatflow.v1.model.send_chat_message_request_body import SendChatMessageRequestBody
from dify_oapi.api.chatflow.v1.model.stop_chat_message_request import StopChatMessageRequest
from dify_oapi.api.chatflow.v1.model.stop_chat_message_request_body import StopChatMessageRequestBody
from dify_oapi.api.chatflow.v1.resource.chatflow import Chatflow


class TestChatflowIntegration:
    @pytest.fixture(autouse=True)
    def setup(self, config, request_option):
        self.resource = Chatflow(config)
        self.option = request_option

    @respx.mock
    def test_send_then_stop(self):
        respx.post("https://api.dify.ai/v1/chat-messages").mock(
            return_value=httpx.Response(200, json={
                "id": "msg-123",
                "conversation_id": "conv-123",
                "task_id": "task-123",
                "answer": "Hello!",
                "created_at": 1234567890,
            })
        )
        body = SendChatMessageRequestBody.builder().query("hi").user("u1").build()
        result = self.resource.send(
            SendChatMessageRequest.builder().request_body(body).build(), self.option
        )
        assert result.id == "msg-123"
        assert result.conversation_id == "conv-123"

        respx.post(
            url__regex=r"https://api\.dify\.ai/v1/chat-messages/[^/]+/stop"
        ).mock(return_value=httpx.Response(200, json={"result": "success"}))
        stop_body = StopChatMessageRequestBody.builder().user("u1").build()
        stop_result = self.resource.stop(
            StopChatMessageRequest.builder().task_id("task-123").request_body(stop_body).build(),
            self.option,
        )
        assert stop_result.result == "success"

    @respx.mock
    def test_send_error_propagates(self):
        respx.post("https://api.dify.ai/v1/chat-messages").mock(
            return_value=httpx.Response(400, json={"code": "bad_request", "message": "Bad Request"})
        )
        body = SendChatMessageRequestBody.builder().query("").user("u1").build()
        result = self.resource.send(
            SendChatMessageRequest.builder().request_body(body).build(), self.option
        )
        assert result.success is False
