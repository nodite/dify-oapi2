"""
Chatflow Resource Tests

Test core business resources of the chatflow module
"""

from unittest.mock import Mock, patch

import pytest

from dify_oapi.api.chatflow.v1.resource.chatflow import Chatflow
from dify_oapi.core.model.config import Config
from dify_oapi.core.model.request_option import RequestOption


class TestChatflowResource:
    """Chatflow Resource Tests"""

    @pytest.fixture
    def config(self):
        return Config()

    @pytest.fixture
    def request_option(self):
        return RequestOption.builder().api_key("test-api-key").build()

    @pytest.fixture
    def chatflow_resource(self, config):
        return Chatflow(config)

    def test_chatflow_resource_init(self, chatflow_resource):
        """Test Chatflow resource initialization"""
        assert chatflow_resource.config is not None
        assert hasattr(chatflow_resource, "send")
        assert hasattr(chatflow_resource, "asend")
        assert hasattr(chatflow_resource, "stop")
        assert hasattr(chatflow_resource, "astop")

    @patch("dify_oapi.core.http.transport.Transport.execute")
    def test_send_method(self, mock_execute, chatflow_resource, request_option):
        """Test send method"""
        from dify_oapi.api.chatflow.v1.model.send_chat_message_request import SendChatMessageRequest

        mock_response = Mock()
        mock_response.answer = "Test chatflow response"
        mock_execute.return_value = mock_response

        request = SendChatMessageRequest.builder().build()
        response = chatflow_resource.send(request, request_option, False)

        assert response.answer == "Test chatflow response"
        mock_execute.assert_called_once()

    @patch("dify_oapi.core.http.transport.ATransport.aexecute")
    async def test_async_send_method(self, mock_aexecute, chatflow_resource, request_option):
        """Test async send method"""
        from dify_oapi.api.chatflow.v1.model.send_chat_message_request import SendChatMessageRequest

        mock_response = Mock()
        mock_response.answer = "Async test chatflow response"
        mock_aexecute.return_value = mock_response

        request = SendChatMessageRequest.builder().build()
        response = await chatflow_resource.asend(request, request_option, False)

        assert response.answer == "Async test chatflow response"
        mock_aexecute.assert_called_once()

    def test_chatflow_resource_methods_exist(self, chatflow_resource):
        """Test Chatflow resource methods exist"""
        methods = ["send", "asend", "stop", "astop", "suggested", "asuggested"]

        for method in methods:
            assert hasattr(chatflow_resource, method)
            assert callable(getattr(chatflow_resource, method))


if __name__ == "__main__":
    pytest.main([__file__])
