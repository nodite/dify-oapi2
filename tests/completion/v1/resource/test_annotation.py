"""Completion annotation resource tests."""

from unittest.mock import MagicMock, patch

import pytest

from dify_oapi.api.completion.v1.resource.annotation import Annotation


class TestAnnotation:
    """Test Completion Annotation resource."""

    @pytest.fixture
    def annotation(self, mock_config):
        """Create Annotation instance."""
        return Annotation(mock_config)

    def test_list_annotations(self, annotation, request_option):
        """Test list annotations."""
        with patch("dify_oapi.core.http.transport.Transport.execute") as mock_execute:
            mock_execute.return_value = MagicMock(data=[])
            result = annotation.list_annotations(MagicMock(), request_option)
            assert result.data == []

    def test_create_annotation(self, annotation, request_option):
        """Test create annotation."""
        with patch("dify_oapi.core.http.transport.Transport.execute") as mock_execute:
            mock_execute.return_value = MagicMock(id="test-id")
            result = annotation.create_annotation(MagicMock(), request_option)
            assert result.id == "test-id"

    def test_update_annotation(self, annotation, request_option):
        """Test update annotation."""
        with patch("dify_oapi.core.http.transport.Transport.execute") as mock_execute:
            mock_execute.return_value = MagicMock(updated=True)
            result = annotation.update_annotation(MagicMock(), request_option)
            assert result.updated is True

    def test_delete_annotation(self, annotation, request_option):
        """Test delete annotation."""
        with patch("dify_oapi.core.http.transport.Transport.execute") as mock_execute:
            mock_execute.return_value = MagicMock(result="success")
            result = annotation.delete_annotation(MagicMock(), request_option)
            assert result.result == "success"
