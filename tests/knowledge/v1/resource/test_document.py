"""Document resource tests."""

from unittest.mock import MagicMock, patch

import pytest

from dify_oapi.api.knowledge.v1.resource.document import Document
from dify_oapi.core.model.request_option import RequestOption


class TestDocument:
    """Test Document resource."""

    @pytest.fixture
    def document(self, mock_config):
        """Create Document instance."""
        return Document(mock_config)

    @pytest.fixture
    def request_option(self):
        """Create request option."""
        return RequestOption.builder().api_key("test-key").build()

    def test_list(self, document, request_option):
        """Test list documents."""
        with patch("dify_oapi.core.http.transport.Transport.execute") as mock_execute:
            mock_execute.return_value = MagicMock(data=[])
            result = document.list(MagicMock(), request_option)
            assert result.data == []

    def test_create_by_text(self, document, request_option):
        """Test create document by text."""
        with patch("dify_oapi.core.http.transport.Transport.execute") as mock_execute:
            mock_execute.return_value = MagicMock(document={"id": "doc-123"})
            result = document.create_by_text(MagicMock(), request_option)
            assert result.document["id"] == "doc-123"

    def test_create_by_file(self, document, request_option):
        """Test create document by file."""
        with patch("dify_oapi.core.http.transport.Transport.execute") as mock_execute:
            mock_execute.return_value = MagicMock(document={"id": "doc-123"})
            result = document.create_by_file(MagicMock(), request_option)
            assert result.document["id"] == "doc-123"

    def test_get(self, document, request_option):
        """Test get document."""
        with patch("dify_oapi.core.http.transport.Transport.execute") as mock_execute:
            mock_execute.return_value = MagicMock(id="doc-123")
            result = document.get(MagicMock(), request_option)
            assert result.id == "doc-123"

    def test_update_by_text(self, document, request_option):
        """Test update document by text."""
        with patch("dify_oapi.core.http.transport.Transport.execute") as mock_execute:
            mock_execute.return_value = MagicMock(document={"id": "doc-123"})
            result = document.update_by_text(MagicMock(), request_option)
            assert result.document["id"] == "doc-123"

    def test_update_by_file(self, document, request_option):
        """Test update document by file."""
        with patch("dify_oapi.core.http.transport.Transport.execute") as mock_execute:
            mock_execute.return_value = MagicMock(document={"id": "doc-123"})
            result = document.update_by_file(MagicMock(), request_option)
            assert result.document["id"] == "doc-123"

    def test_delete(self, document, request_option):
        """Test delete document."""
        with patch("dify_oapi.core.http.transport.Transport.execute") as mock_execute:
            mock_execute.return_value = MagicMock(result="success")
            result = document.delete(MagicMock(), request_option)
            assert result.result == "success"

    def test_get_batch_status(self, document, request_option):
        """Test get batch indexing status."""
        with patch("dify_oapi.core.http.transport.Transport.execute") as mock_execute:
            mock_execute.return_value = MagicMock(batch={"status": "completed"})
            result = document.get_batch_status(MagicMock(), request_option)
            assert result.batch["status"] == "completed"

    def test_update_status(self, document, request_option):
        """Test update document status."""
        with patch("dify_oapi.core.http.transport.Transport.execute") as mock_execute:
            mock_execute.return_value = MagicMock(result="success")
            result = document.update_status(MagicMock(), request_option)
            assert result.result == "success"
