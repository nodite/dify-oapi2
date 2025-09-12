"""Core streaming tests."""

from unittest.mock import patch

import pytest

from dify_oapi.api.chat.v1.model.chat_request import ChatRequest
from dify_oapi.api.chat.v1.model.chat_request_body import ChatRequestBody
from dify_oapi.api.chat.v1.resource.chat import Chat


class TestStreaming:
    """Test streaming functionality."""

    @pytest.fixture
    def chat(self, mock_config):
        """Create Chat instance."""
        return Chat(mock_config)

    def test_streaming_chat(self, chat, request_option):
        """Test streaming chat."""
        req_body = ChatRequestBody.builder().query("test").user("user").build()
        req = ChatRequest.builder().request_body(req_body).build()

        def mock_generator():
            yield b'{"event": "message", "data": "chunk1"}'
            yield b'{"event": "message", "data": "chunk2"}'
            yield b'{"event": "message_end", "data": ""}'

        with patch("dify_oapi.core.http.transport.Transport.execute") as mock_execute:
            mock_execute.return_value = mock_generator()
            result = chat.chat(req, request_option, stream=True)
            chunks = list(result)
            assert len(chunks) == 3

    @pytest.mark.asyncio
    async def test_async_streaming_chat(self, chat, request_option):
        """Test async streaming chat."""
        req_body = ChatRequestBody.builder().query("test").user("user").build()
        req = ChatRequest.builder().request_body(req_body).build()

        async def mock_async_generator():
            yield b'{"event": "message", "data": "chunk1"}'
            yield b'{"event": "message", "data": "chunk2"}'
            yield b'{"event": "message_end", "data": ""}'

        with patch("dify_oapi.core.http.transport.ATransport.aexecute") as mock_execute:
            mock_execute.return_value = mock_async_generator()
            result = await chat.achat(req, request_option, stream=True)
            chunks = []
            async for chunk in result:
                chunks.append(chunk)
            assert len(chunks) == 3
