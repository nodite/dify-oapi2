"""Dify file resource tests."""

from unittest.mock import MagicMock, patch

import pytest

from dify_oapi.api.dify.v1.resource.file import File


class TestFile:
    """Test Dify File resource."""

    @pytest.fixture
    def file(self, mock_config):
        """Create File instance."""
        return File(mock_config)

    def test_upload(self, file, request_option):
        """Test upload file."""
        with patch("dify_oapi.core.http.transport.Transport.execute") as mock_execute:
            mock_execute.return_value = MagicMock(id="file-123", name="test.txt")
            result = file.upload(MagicMock(), request_option)
            assert hasattr(result, "id")
            assert hasattr(result, "name")
