"""Dify feedback resource tests."""

from unittest.mock import MagicMock, patch

import pytest

from dify_oapi.api.dify.v1.resource.feedback import Feedback


class TestFeedback:
    """Test Dify Feedback resource."""

    @pytest.fixture
    def feedback(self, mock_config):
        """Create Feedback instance."""
        return Feedback(mock_config)

    def test_submit(self, feedback, request_option):
        """Test submit feedback."""
        with patch("dify_oapi.core.http.transport.Transport.execute") as mock_execute:
            mock_execute.return_value = MagicMock(result="success")
            result = feedback.submit(MagicMock(), request_option)
            assert result.result == "success"

    def test_list(self, feedback, request_option):
        """Test list feedbacks."""
        with patch("dify_oapi.core.http.transport.Transport.execute") as mock_execute:
            mock_execute.return_value = MagicMock(data=[])
            result = feedback.list(MagicMock(), request_option)
            assert result.data == []
