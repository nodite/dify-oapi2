"""Chat conversation resource tests."""

from unittest.mock import MagicMock, patch

import pytest

from dify_oapi.api.chat.v1.resource.conversation import Conversation


class TestConversation:
    """Test Chat Conversation resource."""

    @pytest.fixture
    def conversation(self, mock_config):
        """Create Conversation instance."""
        return Conversation(mock_config)

    def test_history(self, conversation, request_option):
        """Test get conversation messages."""
        with patch("dify_oapi.core.http.transport.Transport.execute") as mock_execute:
            mock_execute.return_value = MagicMock(data=[])
            result = conversation.history(MagicMock(), request_option)
            assert result.data == []

    def test_list(self, conversation, request_option):
        """Test list conversations."""
        with patch("dify_oapi.core.http.transport.Transport.execute") as mock_execute:
            mock_execute.return_value = MagicMock(data=[])
            result = conversation.list(MagicMock(), request_option)
            assert result.data == []

    def test_delete(self, conversation, request_option):
        """Test delete conversation."""
        with patch("dify_oapi.core.http.transport.Transport.execute") as mock_execute:
            mock_execute.return_value = MagicMock(result="success")
            result = conversation.delete(MagicMock(), request_option)
            assert result.result == "success"

    def test_rename(self, conversation, request_option):
        """Test rename conversation."""
        with patch("dify_oapi.core.http.transport.Transport.execute") as mock_execute:
            mock_execute.return_value = MagicMock(result="success")
            result = conversation.rename(MagicMock(), request_option)
            assert result.result == "success"

    def test_variables(self, conversation, request_option):
        """Test get conversation variables."""
        with patch("dify_oapi.core.http.transport.Transport.execute") as mock_execute:
            mock_execute.return_value = MagicMock(data={})
            result = conversation.variables(MagicMock(), request_option)
            assert result.data == {}
