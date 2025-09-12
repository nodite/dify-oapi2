"""
Chat Resource Tests

Test core business resources of the chat module
"""

from unittest.mock import Mock, patch

import pytest

from dify_oapi.api.chat.v1.resource.chat import Chat
from dify_oapi.core.model.config import Config
from dify_oapi.core.model.request_option import RequestOption


class TestChatResource:
    """Chat Resource Tests"""

    @pytest.fixture
    def config(self):
        return Config()

    @pytest.fixture
    def request_option(self):
        return RequestOption.builder().api_key("test-api-key").build()

    @pytest.fixture
    def chat_resource(self, config):
        return Chat(config)

    def test_chat_resource_init(self, chat_resource):
        """Test Chat resource initialization"""
        assert chat_resource.config is not None
        assert hasattr(chat_resource, "chat")
        assert hasattr(chat_resource, "achat")
        assert hasattr(chat_resource, "stop")
        assert hasattr(chat_resource, "astop")

    @patch("dify_oapi.core.http.transport.Transport.execute")
    def test_chat_method(self, mock_execute, chat_resource, request_option):
        """Test chat method"""
        from dify_oapi.api.chat.v1.model.chat_request import ChatRequest

        mock_response = Mock()
        mock_response.answer = "Test response"
        mock_execute.return_value = mock_response

        request = ChatRequest.builder().build()
        response = chat_resource.chat(request, request_option, False)

        assert response.answer == "Test response"
        mock_execute.assert_called_once()

    @patch("dify_oapi.core.http.transport.ATransport.aexecute")
    async def test_async_chat_method(self, mock_aexecute, chat_resource, request_option):
        """Test async chat method"""
        from dify_oapi.api.chat.v1.model.chat_request import ChatRequest

        mock_response = Mock()
        mock_response.answer = "Async test response"
        mock_aexecute.return_value = mock_response

        request = ChatRequest.builder().build()
        response = await chat_resource.achat(request, request_option, False)

        assert response.answer == "Async test response"
        mock_aexecute.assert_called_once()

    def test_chat_resource_methods_exist(self, chat_resource):
        """Test Chat resource methods exist"""
        methods = ["chat", "achat", "stop", "astop", "suggested", "asuggested"]

        for method in methods:
            assert hasattr(chat_resource, method)
            assert callable(getattr(chat_resource, method))


if __name__ == "__main__":
    pytest.main([__file__])
