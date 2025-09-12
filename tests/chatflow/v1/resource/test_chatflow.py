"""Chatflow resource tests."""

from unittest.mock import MagicMock, patch

import pytest

from dify_oapi.api.chatflow.v1.model.send_chat_message_request import SendChatMessageRequest
from dify_oapi.api.chatflow.v1.model.send_chat_message_request_body import SendChatMessageRequestBody
from dify_oapi.api.chatflow.v1.resource.chatflow import Chatflow


class TestChatflow:
    """Test Chatflow resource."""

    @pytest.fixture
    def chatflow(self, mock_config):
        """Create Chatflow instance."""
        return Chatflow(mock_config)

    def test_send(self, chatflow, request_option):
        """Test send chat message."""
        req_body = SendChatMessageRequestBody.builder().query("test").user("user").build()
        req = SendChatMessageRequest.builder().request_body(req_body).build()

        with patch("dify_oapi.core.http.transport.Transport.execute") as mock_execute:
            mock_execute.return_value = MagicMock(answer="response")
            result = chatflow.send(req, request_option)
            assert result.answer == "response"

    def test_stop(self, chatflow, request_option):
        """Test stop chat message."""
        with patch("dify_oapi.core.http.transport.Transport.execute") as mock_execute:
            mock_execute.return_value = MagicMock(result="stopped")
            result = chatflow.stop(MagicMock(), request_option)
            assert result.result == "stopped"

    def test_suggested(self, chatflow, request_option):
        """Test get suggested questions."""
        with patch("dify_oapi.core.http.transport.Transport.execute") as mock_execute:
            mock_execute.return_value = MagicMock(data=[])
            result = chatflow.suggested(MagicMock(), request_option)
            assert result.data == []
