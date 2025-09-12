"""Dataset resource tests."""

from unittest.mock import MagicMock, patch

import pytest

from dify_oapi.api.knowledge.v1.resource.dataset import Dataset


class TestDataset:
    """Test Dataset resource."""

    @pytest.fixture
    def dataset(self, mock_config):
        """Create Dataset instance."""
        return Dataset(mock_config)

    def test_list(self, dataset, request_option):
        """Test list datasets."""
        with patch("dify_oapi.core.http.transport.Transport.execute") as mock_execute:
            mock_execute.return_value = MagicMock(data=[])
            result = dataset.list(MagicMock(), request_option)
            assert result.data == []

    def test_create(self, dataset, request_option):
        """Test create dataset."""
        with patch("dify_oapi.core.http.transport.Transport.execute") as mock_execute:
            mock_execute.return_value = MagicMock(id="dataset-123")
            result = dataset.create(MagicMock(), request_option)
            assert result.id == "dataset-123"

    def test_get(self, dataset, request_option):
        """Test get dataset."""
        with patch("dify_oapi.core.http.transport.Transport.execute") as mock_execute:
            mock_execute.return_value = MagicMock(id="dataset-123")
            result = dataset.get(MagicMock(), request_option)
            assert result.id == "dataset-123"

    def test_update(self, dataset, request_option):
        """Test update dataset."""
        with patch("dify_oapi.core.http.transport.Transport.execute") as mock_execute:
            mock_execute.return_value = MagicMock(updated=True)
            result = dataset.update(MagicMock(), request_option)
            assert result.updated is True

    def test_delete(self, dataset, request_option):
        """Test delete dataset."""
        with patch("dify_oapi.core.http.transport.Transport.execute") as mock_execute:
            mock_execute.return_value = MagicMock(result="success")
            result = dataset.delete(MagicMock(), request_option)
            assert result.result == "success"

    def test_retrieve(self, dataset, request_option):
        """Test retrieve from dataset."""
        with patch("dify_oapi.core.http.transport.Transport.execute") as mock_execute:
            mock_execute.return_value = MagicMock(records=[])
            result = dataset.retrieve(MagicMock(), request_option)
            assert result.records == []
