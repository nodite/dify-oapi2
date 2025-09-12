"""Chunk resource tests."""

from unittest.mock import MagicMock, patch

import pytest

from dify_oapi.api.knowledge.v1.resource.chunk import Chunk
from dify_oapi.core.model.request_option import RequestOption


class TestChunk:
    """Test Chunk resource."""

    @pytest.fixture
    def chunk(self, mock_config):
        """Create Chunk instance."""
        return Chunk(mock_config)

    @pytest.fixture
    def request_option(self):
        """Create request option."""
        return RequestOption.builder().api_key("test-key").build()

    def test_list(self, chunk, request_option):
        """Test list child chunks."""
        with patch("dify_oapi.core.http.transport.Transport.execute") as mock_execute:
            mock_execute.return_value = MagicMock(data=[])
            result = chunk.list(MagicMock(), request_option)
            assert result.data == []

    def test_create(self, chunk, request_option):
        """Test create child chunk."""
        with patch("dify_oapi.core.http.transport.Transport.execute") as mock_execute:
            mock_execute.return_value = MagicMock(data={"id": "chunk-123"})
            result = chunk.create(MagicMock(), request_option)
            assert result.data["id"] == "chunk-123"

    def test_update(self, chunk, request_option):
        """Test update child chunk."""
        with patch("dify_oapi.core.http.transport.Transport.execute") as mock_execute:
            mock_execute.return_value = MagicMock(data={"id": "chunk-123"})
            result = chunk.update(MagicMock(), request_option)
            assert result.data["id"] == "chunk-123"

    def test_delete(self, chunk, request_option):
        """Test delete child chunk."""
        with patch("dify_oapi.core.http.transport.Transport.execute") as mock_execute:
            mock_execute.return_value = MagicMock(result="success")
            result = chunk.delete(MagicMock(), request_option)
            assert result.result == "success"
