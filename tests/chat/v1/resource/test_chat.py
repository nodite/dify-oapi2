"""Chat resource tests."""

from unittest.mock import MagicMock, patch

import pytest

from dify_oapi.api.chat.v1.resource.chat import Chat
from dify_oapi.core.model.request_option import RequestOption


class TestChat:
    """Test Chat resource."""

    @pytest.fixture
    def chat(self, mock_config):
        """Create Chat instance."""
        return Chat(mock_config)

    @pytest.fixture
    def request_option(self):
        """Create request option."""
        return RequestOption.builder().api_key("test-key").build()

    def test_chat(self, chat, request_option):
        """Test chat."""
        with patch("dify_oapi.core.http.transport.Transport.execute") as mock_execute:
            mock_execute.return_value = MagicMock(answer="response")
            result = chat.chat(MagicMock(), request_option)
            assert result.answer == "response"

    def test_stop(self, chat, request_option):
        """Test stop chat."""
        with patch("dify_oapi.core.http.transport.Transport.execute") as mock_execute:
            mock_execute.return_value = MagicMock(result="stopped")
            result = chat.stop(MagicMock(), request_option)
            assert result.result == "stopped"

    def test_suggested(self, chat, request_option):
        """Test get suggested questions."""
        with patch("dify_oapi.core.http.transport.Transport.execute") as mock_execute:
            mock_execute.return_value = MagicMock(data=[])
            result = chat.suggested(MagicMock(), request_option)
            assert result.data == []
