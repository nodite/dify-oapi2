"""Edge cases and boundary tests."""

from unittest.mock import MagicMock, patch

import pytest

from dify_oapi.api.chat.v1.model.chat_request import ChatRequest
from dify_oapi.api.chat.v1.model.chat_request_body import ChatRequestBody
from dify_oapi.api.chat.v1.resource.chat import Chat


class TestEdgeCases:
    """Test boundary conditions and edge cases."""

    @pytest.fixture
    def chat(self, mock_config):
        """Create Chat instance."""
        return Chat(mock_config)

    def test_empty_query(self, chat, request_option):
        """Test empty query handling."""
        req_body = ChatRequestBody.builder().query("").user("user").build()
        req = ChatRequest.builder().request_body(req_body).build()

        with patch("dify_oapi.core.http.transport.Transport.execute") as mock_execute:
            mock_execute.return_value = MagicMock(answer="")
            result = chat.chat(req, request_option)
            assert result.answer == ""

    def test_very_long_query(self, chat, request_option):
        """Test very long query handling."""
        long_query = "x" * 10000  # 10k characters
        req_body = ChatRequestBody.builder().query(long_query).user("user").build()
        req = ChatRequest.builder().request_body(req_body).build()

        with patch("dify_oapi.core.http.transport.Transport.execute") as mock_execute:
            mock_execute.return_value = MagicMock(answer="response")
            result = chat.chat(req, request_option)
            assert result.answer == "response"

    def test_special_characters(self, chat, request_option):
        """Test special characters in query."""
        special_query = "Hello! @#$%^&*()_+{}|:<>?[]\\;'\",./"
        req_body = ChatRequestBody.builder().query(special_query).user("user").build()
        req = ChatRequest.builder().request_body(req_body).build()

        with patch("dify_oapi.core.http.transport.Transport.execute") as mock_execute:
            mock_execute.return_value = MagicMock(answer="response")
            result = chat.chat(req, request_option)
            assert result.answer == "response"

    def test_unicode_characters(self, chat, request_option):
        """Test unicode characters in query."""
        unicode_query = "你好世界 🌍 こんにちは العالم"
        req_body = ChatRequestBody.builder().query(unicode_query).user("user").build()
        req = ChatRequest.builder().request_body(req_body).build()

        with patch("dify_oapi.core.http.transport.Transport.execute") as mock_execute:
            mock_execute.return_value = MagicMock(answer="response")
            result = chat.chat(req, request_option)
            assert result.answer == "response"

    def test_null_values(self, chat, request_option):
        """Test null value handling."""
        with patch("dify_oapi.core.http.transport.Transport.execute") as mock_execute:
            mock_execute.return_value = MagicMock(answer=None)
            result = chat.chat(MagicMock(), request_option)
            assert result.answer is None
