"""Chatflow integration tests."""

from unittest.mock import MagicMock, patch

import pytest

from dify_oapi.api.chatflow.v1.model.send_chat_message_request import SendChatMessageRequest
from dify_oapi.api.chatflow.v1.model.send_chat_message_request_body import SendChatMessageRequestBody
from dify_oapi.client import Client
from dify_oapi.core.model.request_option import RequestOption


class TestChatflowIntegration:
    """Test Chatflow integration."""

    @pytest.fixture
    def client(self):
        """Create client."""
        return Client.builder().domain("https://api.dify.ai").build()

    @pytest.fixture
    def request_option(self):
        """Create request option."""
        return RequestOption.builder().api_key("test-key").build()

    def test_complete_chat_workflow(self, client, request_option):
        """Test complete chat workflow."""
        req_body = SendChatMessageRequestBody.builder().query("test").user("user").build()
        req = SendChatMessageRequest.builder().request_body(req_body).build()

        with patch("dify_oapi.core.http.transport.Transport.execute") as mock_execute:
            mock_execute.return_value = MagicMock(answer="response", conversation_id="conv-123")
            result = client.chatflow.v1.chatflow.send(req, request_option)
            assert result.answer == "response"
            assert result.conversation_id == "conv-123"

    def test_streaming_chat(self, client, request_option):
        """Test streaming chat."""
        req_body = SendChatMessageRequestBody.builder().query("test").user("user").response_mode("streaming").build()
        req = SendChatMessageRequest.builder().request_body(req_body).build()

        with patch("dify_oapi.core.http.transport.Transport.execute") as mock_execute:

            def mock_stream():
                yield "chunk1"
                yield "chunk2"

            mock_execute.return_value = mock_stream()
            result = client.chatflow.v1.chatflow.send(req, request_option, True)
            chunks = list(result)
            assert chunks == ["chunk1", "chunk2"]

    def test_error_handling(self, client, request_option):
        """Test error handling."""
        req_body = SendChatMessageRequestBody.builder().query("test").user("user").build()
        req = SendChatMessageRequest.builder().request_body(req_body).build()

        with patch("dify_oapi.core.http.transport.Transport.execute") as mock_execute:
            mock_execute.side_effect = Exception("API Error")
            with pytest.raises(Exception, match="API Error"):
                client.chatflow.v1.chatflow.send(req, request_option)
