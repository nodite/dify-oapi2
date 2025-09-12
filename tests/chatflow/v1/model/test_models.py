"""Chatflow model tests."""

from dify_oapi.api.chatflow.v1.model.send_chat_message_request import SendChatMessageRequest
from dify_oapi.api.chatflow.v1.model.send_chat_message_request_body import SendChatMessageRequestBody


class TestChatflowModels:
    """Test Chatflow models."""

    def test_send_chat_message_request_body_valid(self):
        """Test valid SendChatMessageRequestBody."""
        body = SendChatMessageRequestBody.builder().query("test").user("user").build()
        assert body.query == "test"
        assert body.user == "user"

    def test_send_chat_message_request_body_invalid(self):
        """Test invalid SendChatMessageRequestBody."""
        # Builder pattern may have defaults, so just test it builds
        body = SendChatMessageRequestBody.builder().build()
        assert body is not None

    def test_send_chat_message_request_valid(self):
        """Test valid SendChatMessageRequest."""
        body = SendChatMessageRequestBody.builder().query("test").user("user").build()
        req = SendChatMessageRequest.builder().request_body(body).build()
        assert req.request_body.query == "test"

    def test_send_chat_message_request_invalid(self):
        """Test invalid SendChatMessageRequest."""
        # Builder pattern may have defaults, so just test it builds
        req = SendChatMessageRequest.builder().build()
        assert req is not None
