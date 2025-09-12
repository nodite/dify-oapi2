"""Core error handling tests."""

from unittest.mock import patch

import pytest

try:
    from requests.exceptions import (
        ConnectionError as RequestsConnectionError,
    )
    from requests.exceptions import (
        HTTPError,
    )
    from requests.exceptions import (
        Timeout as RequestTimeoutError,
    )
except ImportError:
    # Fallback for testing without requests
    class RequestsError(Exception):
        pass

    class HTTPError(RequestsError):
        pass

    class RequestsConnectionError(RequestsError):
        pass

    class RequestTimeoutError(RequestsError):
        pass


from dify_oapi.api.chat.v1.model.chat_request import ChatRequest
from dify_oapi.api.chat.v1.model.chat_request_body import ChatRequestBody
from dify_oapi.api.chat.v1.resource.chat import Chat


class TestErrorHandling:
    """Test error handling."""

    @pytest.fixture
    def chat(self, mock_config):
        """Create Chat instance."""
        return Chat(mock_config)

    def test_http_error(self, chat, request_option):
        """Test HTTP error handling."""
        req_body = ChatRequestBody.builder().query("test").user("user").build()
        req = ChatRequest.builder().request_body(req_body).build()

        with patch("dify_oapi.core.http.transport.Transport.execute") as mock_execute:
            mock_execute.side_effect = HTTPError("HTTP 500 Error")
            with pytest.raises(HTTPError):
                chat.chat(req, request_option)

    def test_connection_error(self, chat, request_option):
        """Test connection error handling."""
        req_body = ChatRequestBody.builder().query("test").user("user").build()
        req = ChatRequest.builder().request_body(req_body).build()

        with patch("dify_oapi.core.http.transport.Transport.execute") as mock_execute:
            mock_execute.side_effect = RequestsConnectionError("Connection failed")
            with pytest.raises(RequestsConnectionError):
                chat.chat(req, request_option)

    def test_timeout_error(self, chat, request_option):
        """Test timeout error handling."""
        req_body = ChatRequestBody.builder().query("test").user("user").build()
        req = ChatRequest.builder().request_body(req_body).build()

        with patch("dify_oapi.core.http.transport.Transport.execute") as mock_execute:
            mock_execute.side_effect = RequestTimeoutError("Request timeout")
            with pytest.raises(RequestTimeoutError):
                chat.chat(req, request_option)

    def test_generic_request_error(self, chat, request_option):
        """Test generic request error handling."""
        req_body = ChatRequestBody.builder().query("test").user("user").build()
        req = ChatRequest.builder().request_body(req_body).build()

        with patch("dify_oapi.core.http.transport.Transport.execute") as mock_execute:
            mock_execute.side_effect = RequestsError("Request failed")
            with pytest.raises(RequestsError):
                chat.chat(req, request_option)
