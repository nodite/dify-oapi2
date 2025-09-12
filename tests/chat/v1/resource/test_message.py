"""Chat message resource tests."""

from unittest.mock import MagicMock, patch

import pytest

from dify_oapi.api.chat.v1.resource.message import Message


class TestMessage:
    """Test Chat Message resource."""

    @pytest.fixture
    def message(self, mock_config):
        """Create Message instance."""
        return Message(mock_config)

    def test_history(self, message, request_option):
        """Test message history."""
        with patch("dify_oapi.core.http.transport.Transport.execute") as mock_execute:
            mock_execute.return_value = MagicMock(data=[])
            result = message.history(MagicMock(), request_option)
            assert result.data == []

    def test_suggested(self, message, request_option):
        """Test get suggested questions."""
        with patch("dify_oapi.core.http.transport.Transport.execute") as mock_execute:
            mock_execute.return_value = MagicMock(data=[])
            result = message.suggested(MagicMock(), request_option)
            assert result.data == []
