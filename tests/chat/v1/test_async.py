"""Chat async tests."""

from unittest.mock import MagicMock, patch

import pytest

from dify_oapi.api.chat.v1.model.chat_request import ChatRequest
from dify_oapi.api.chat.v1.model.chat_request_body import ChatRequestBody
from dify_oapi.api.chat.v1.resource.chat import Chat


class TestChatAsync:
    """Test Chat async operations."""

    @pytest.fixture
    def chat(self, mock_config):
        """Create Chat instance."""
        return Chat(mock_config)

    @pytest.mark.asyncio
    async def test_achat(self, chat, request_option):
        """Test async chat."""
        req_body = ChatRequestBody.builder().query("test").user("user").build()
        req = ChatRequest.builder().request_body(req_body).build()

        with patch("dify_oapi.core.http.transport.ATransport.aexecute") as mock_execute:
            mock_execute.return_value = MagicMock(answer="response")
            result = await chat.achat(req, request_option)
            assert result.answer == "response"

    @pytest.mark.asyncio
    async def test_astop(self, chat, request_option):
        """Test async stop."""
        with patch("dify_oapi.core.http.transport.ATransport.aexecute") as mock_execute:
            mock_execute.return_value = MagicMock(result="stopped")
            result = await chat.astop(MagicMock(), request_option)
            assert result.result == "stopped"

    @pytest.mark.asyncio
    async def test_asuggested(self, chat, request_option):
        """Test async suggested."""
        with patch("dify_oapi.core.http.transport.ATransport.aexecute") as mock_execute:
            mock_execute.return_value = MagicMock(data=[])
            result = await chat.asuggested(MagicMock(), request_option)
            assert result.data == []
