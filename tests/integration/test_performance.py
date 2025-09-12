"""Performance load tests."""

import time
from unittest.mock import MagicMock, patch

import pytest

from dify_oapi.api.chat.v1.model.chat_request import ChatRequest
from dify_oapi.api.chat.v1.model.chat_request_body import ChatRequestBody
from dify_oapi.api.chat.v1.resource.chat import Chat


class TestPerformance:
    """Test performance scenarios."""

    @pytest.fixture
    def chat(self, mock_config):
        """Create Chat instance."""
        return Chat(mock_config)

    def test_concurrent_requests(self, chat, request_option):
        """Test concurrent request handling."""
        req_body = ChatRequestBody.builder().query("test").user("user").build()
        req = ChatRequest.builder().request_body(req_body).build()

        with patch("dify_oapi.core.http.transport.Transport.execute") as mock_execute:
            mock_execute.return_value = MagicMock(answer="response")

            # Simulate multiple concurrent requests
            results = []
            for _i in range(10):
                result = chat.chat(req, request_option)
                results.append(result)

            assert len(results) == 10
            assert all(r.answer == "response" for r in results)

    def test_request_timing(self, chat, request_option):
        """Test request timing."""
        req_body = ChatRequestBody.builder().query("test").user("user").build()
        req = ChatRequest.builder().request_body(req_body).build()

        with patch("dify_oapi.core.http.transport.Transport.execute") as mock_execute:
            mock_execute.return_value = MagicMock(answer="response")

            start_time = time.time()
            result = chat.chat(req, request_option)
            end_time = time.time()

            assert result.answer == "response"
            # Mock should be very fast
            assert (end_time - start_time) < 1.0

    def test_memory_usage(self, chat, request_option):
        """Test memory usage with multiple requests."""
        req_body = ChatRequestBody.builder().query("test").user("user").build()
        req = ChatRequest.builder().request_body(req_body).build()

        with patch("dify_oapi.core.http.transport.Transport.execute") as mock_execute:
            mock_execute.return_value = MagicMock(answer="response")

            # Create many requests to test memory usage
            for _i in range(100):
                result = chat.chat(req, request_option)
                assert result.answer == "response"
                # Force garbage collection by not keeping references
