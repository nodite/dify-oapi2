"""Conversation resource tests."""

from unittest.mock import MagicMock, patch

import pytest

from dify_oapi.api.chatflow.v1.resource.conversation import Conversation
from dify_oapi.core.model.request_option import RequestOption


class TestConversation:
    """Test Conversation resource."""

    @pytest.fixture
    def conversation(self, mock_config):
        """Create Conversation instance."""
        return Conversation(mock_config)

    @pytest.fixture
    def request_option(self):
        """Create request option."""
        return RequestOption.builder().api_key("test-key").build()

    def test_messages(self, conversation, request_option):
        """Test get conversation messages."""
        with patch("dify_oapi.core.http.transport.Transport.execute") as mock_execute:
            mock_execute.return_value = MagicMock(data=[])
            result = conversation.messages(MagicMock(), request_option)
            assert result.data == []

    def test_list(self, conversation, request_option):
        """Test get conversations."""
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
