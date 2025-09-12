"""Segment resource tests."""

from unittest.mock import MagicMock, patch

import pytest

from dify_oapi.api.knowledge.v1.resource.segment import Segment
from dify_oapi.core.model.request_option import RequestOption


class TestSegment:
    """Test Segment resource."""

    @pytest.fixture
    def segment(self, mock_config):
        """Create Segment instance."""
        return Segment(mock_config)

    @pytest.fixture
    def request_option(self):
        """Create request option."""
        return RequestOption.builder().api_key("test-key").build()

    def test_list(self, segment, request_option):
        """Test list segments."""
        with patch("dify_oapi.core.http.transport.Transport.execute") as mock_execute:
            mock_execute.return_value = MagicMock(data=[])
            result = segment.list(MagicMock(), request_option)
            assert result.data == []

    def test_create(self, segment, request_option):
        """Test create segment."""
        with patch("dify_oapi.core.http.transport.Transport.execute") as mock_execute:
            mock_execute.return_value = MagicMock(data={"id": "seg-123"})
            result = segment.create(MagicMock(), request_option)
            assert result.data["id"] == "seg-123"

    def test_get(self, segment, request_option):
        """Test get segment."""
        with patch("dify_oapi.core.http.transport.Transport.execute") as mock_execute:
            mock_execute.return_value = MagicMock(id="seg-123")
            result = segment.get(MagicMock(), request_option)
            assert result.id == "seg-123"

    def test_update(self, segment, request_option):
        """Test update segment."""
        with patch("dify_oapi.core.http.transport.Transport.execute") as mock_execute:
            mock_execute.return_value = MagicMock(data={"id": "seg-123"})
            result = segment.update(MagicMock(), request_option)
            assert result.data["id"] == "seg-123"

    def test_delete(self, segment, request_option):
        """Test delete segment."""
        with patch("dify_oapi.core.http.transport.Transport.execute") as mock_execute:
            mock_execute.return_value = MagicMock(result="success")
            result = segment.delete(MagicMock(), request_option)
            assert result.result == "success"
