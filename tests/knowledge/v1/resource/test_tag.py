"""Tag resource tests."""

from unittest.mock import MagicMock, patch

import pytest

from dify_oapi.api.knowledge.v1.resource.tag import Tag
from dify_oapi.core.model.request_option import RequestOption


class TestTag:
    """Test Tag resource."""

    @pytest.fixture
    def tag(self, mock_config):
        """Create Tag instance."""
        return Tag(mock_config)

    @pytest.fixture
    def request_option(self):
        """Create request option."""
        return RequestOption.builder().api_key("test-key").build()

    def test_list(self, tag, request_option):
        """Test list tags."""
        with patch("dify_oapi.core.http.transport.Transport.execute") as mock_execute:
            mock_execute.return_value = MagicMock(data=[])
            result = tag.list(MagicMock(), request_option)
            assert result.data == []

    def test_create(self, tag, request_option):
        """Test create tag."""
        with patch("dify_oapi.core.http.transport.Transport.execute") as mock_execute:
            mock_execute.return_value = MagicMock(id="tag-123")
            result = tag.create(MagicMock(), request_option)
            assert result.id == "tag-123"

    def test_update(self, tag, request_option):
        """Test update tag."""
        with patch("dify_oapi.core.http.transport.Transport.execute") as mock_execute:
            mock_execute.return_value = MagicMock(updated=True)
            result = tag.update(MagicMock(), request_option)
            assert result.updated is True

    def test_delete(self, tag, request_option):
        """Test delete tag."""
        with patch("dify_oapi.core.http.transport.Transport.execute") as mock_execute:
            mock_execute.return_value = MagicMock(result="success")
            result = tag.delete(MagicMock(), request_option)
            assert result.result == "success"

    def test_get_dataset_tags(self, tag, request_option):
        """Test get dataset tags."""
        with patch("dify_oapi.core.http.transport.Transport.execute") as mock_execute:
            mock_execute.return_value = MagicMock(data=[])
            result = tag.get_dataset_tags(MagicMock(), request_option)
            assert result.data == []

    def test_bind(self, tag, request_option):
        """Test bind tags to dataset."""
        with patch("dify_oapi.core.http.transport.Transport.execute") as mock_execute:
            mock_execute.return_value = MagicMock(result="success")
            result = tag.bind(MagicMock(), request_option)
            assert result.result == "success"

    def test_unbind(self, tag, request_option):
        """Test unbind tags from dataset."""
        with patch("dify_oapi.core.http.transport.Transport.execute") as mock_execute:
            mock_execute.return_value = MagicMock(result="success")
            result = tag.unbind(MagicMock(), request_option)
            assert result.result == "success"
