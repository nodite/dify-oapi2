"""Annotation resource tests."""

from unittest.mock import MagicMock, patch

import pytest

from dify_oapi.api.chatflow.v1.resource.annotation import Annotation
from dify_oapi.core.model.request_option import RequestOption


class TestAnnotation:
    """Test Annotation resource."""

    @pytest.fixture
    def annotation(self, mock_config):
        """Create Annotation instance."""
        return Annotation(mock_config)

    @pytest.fixture
    def request_option(self):
        """Create request option."""
        return RequestOption.builder().api_key("test-key").build()

    def test_list(self, annotation, request_option):
        """Test get annotations."""
        with patch("dify_oapi.core.http.transport.Transport.execute") as mock_execute:
            mock_execute.return_value = MagicMock(data=[])
            result = annotation.list(MagicMock(), request_option)
            assert result.data == []

    def test_create(self, annotation, request_option):
        """Test create annotation."""
        with patch("dify_oapi.core.http.transport.Transport.execute") as mock_execute:
            mock_execute.return_value = MagicMock(id="test-id")
            result = annotation.create(MagicMock(), request_option)
            assert result.id == "test-id"

    def test_update(self, annotation, request_option):
        """Test update annotation."""
        with patch("dify_oapi.core.http.transport.Transport.execute") as mock_execute:
            mock_execute.return_value = MagicMock(updated=True)
            result = annotation.update(MagicMock(), request_option)
            assert result.updated is True

    def test_delete(self, annotation, request_option):
        """Test delete annotation."""
        with patch("dify_oapi.core.http.transport.Transport.execute") as mock_execute:
            mock_execute.return_value = MagicMock(result="success")
            result = annotation.delete(MagicMock(), request_option)
            assert result.result == "success"

    def test_reply_settings(self, annotation, request_option):
        """Test reply settings."""
        with patch("dify_oapi.core.http.transport.Transport.execute") as mock_execute:
            mock_execute.return_value = MagicMock(enabled=True)
            result = annotation.reply_settings(MagicMock(), request_option)
            assert result.enabled is True

    def test_reply_status(self, annotation, request_option):
        """Test reply status."""
        with patch("dify_oapi.core.http.transport.Transport.execute") as mock_execute:
            mock_execute.return_value = MagicMock(status="active")
            result = annotation.reply_status(MagicMock(), request_option)
            assert result.status == "active"
