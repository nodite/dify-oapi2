"""Completion resource tests."""

from unittest.mock import MagicMock, patch

import pytest

from dify_oapi.api.completion.v1.resource.completion import Completion
from dify_oapi.core.model.request_option import RequestOption


class TestCompletion:
    """Test Completion resource."""

    @pytest.fixture
    def completion(self, mock_config):
        """Create Completion instance."""
        return Completion(mock_config)

    @pytest.fixture
    def request_option(self):
        """Create request option."""
        return RequestOption.builder().api_key("test-key").build()

    def test_send_message(self, completion, request_option):
        """Test send message."""
        with patch("dify_oapi.core.http.transport.Transport.execute") as mock_execute:
            mock_execute.return_value = MagicMock(answer="response")
            result = completion.send_message(MagicMock(), request_option)
            assert result.answer == "response"

    def test_stop_response(self, completion, request_option):
        """Test stop response."""
        with patch("dify_oapi.core.http.transport.Transport.execute") as mock_execute:
            mock_execute.return_value = MagicMock(result="stopped")
            result = completion.stop_response(MagicMock(), request_option)
            assert result.result == "stopped"
