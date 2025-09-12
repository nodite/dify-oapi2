"""
Completion Resource Tests

Test core business resources of the completion module
"""

from unittest.mock import Mock, patch

import pytest

from dify_oapi.api.completion.v1.resource.completion import Completion
from dify_oapi.core.model.config import Config
from dify_oapi.core.model.request_option import RequestOption


class TestCompletionResource:
    """Completion Resource Tests"""

    @pytest.fixture
    def config(self):
        return Config()

    @pytest.fixture
    def request_option(self):
        return RequestOption.builder().api_key("test-api-key").build()

    @pytest.fixture
    def completion_resource(self, config):
        return Completion(config)

    def test_completion_resource_init(self, completion_resource):
        """Test Completion resource initialization"""
        assert completion_resource.config is not None
        assert hasattr(completion_resource, "send_message")
        assert hasattr(completion_resource, "asend_message")
        assert hasattr(completion_resource, "stop_response")
        assert hasattr(completion_resource, "astop_response")

    @patch("dify_oapi.core.http.transport.Transport.execute")
    def test_send_message_method(self, mock_execute, completion_resource, request_option):
        """Test send message method"""
        from dify_oapi.api.completion.v1.model.completion.send_message_request import SendMessageRequest

        mock_response = Mock()
        mock_response.answer = "Test completion"
        mock_execute.return_value = mock_response

        request = SendMessageRequest.builder().build()
        response = completion_resource.send_message(request, request_option, False)

        assert response.answer == "Test completion"
        mock_execute.assert_called_once()

    @patch("dify_oapi.core.http.transport.ATransport.aexecute")
    async def test_async_send_message_method(self, mock_aexecute, completion_resource, request_option):
        """Test async send message method"""
        from dify_oapi.api.completion.v1.model.completion.send_message_request import SendMessageRequest

        mock_response = Mock()
        mock_response.answer = "Async test completion"
        mock_aexecute.return_value = mock_response

        request = SendMessageRequest.builder().build()
        response = await completion_resource.asend_message(request, request_option, False)

        assert response.answer == "Async test completion"
        mock_aexecute.assert_called_once()

    def test_completion_resource_methods_exist(self, completion_resource):
        """Test Completion resource methods exist"""
        methods = ["send_message", "asend_message", "stop_response", "astop_response"]

        for method in methods:
            assert hasattr(completion_resource, method)
            assert callable(getattr(completion_resource, method))


if __name__ == "__main__":
    pytest.main([__file__])
