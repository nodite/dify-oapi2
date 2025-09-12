"""Knowledge async tests."""

from unittest.mock import MagicMock, patch

import pytest

from dify_oapi.api.knowledge.v1.model.create_dataset_request import CreateDatasetRequest
from dify_oapi.api.knowledge.v1.model.create_dataset_request_body import CreateDatasetRequestBody
from dify_oapi.api.knowledge.v1.resource.dataset import Dataset


class TestKnowledgeAsync:
    """Test Knowledge async operations."""

    @pytest.fixture
    def dataset(self, mock_config):
        """Create Dataset instance."""
        return Dataset(mock_config)

    @pytest.mark.asyncio
    async def test_alist(self, dataset, request_option):
        """Test async list."""
        with patch("dify_oapi.core.http.transport.ATransport.aexecute") as mock_execute:
            mock_execute.return_value = MagicMock(data=[])
            result = await dataset.alist(MagicMock(), request_option)
            assert result.data == []

    @pytest.mark.asyncio
    async def test_acreate(self, dataset, request_option):
        """Test async create."""
        req_body = CreateDatasetRequestBody.builder().name("test").build()
        req = CreateDatasetRequest.builder().request_body(req_body).build()

        with patch("dify_oapi.core.http.transport.ATransport.aexecute") as mock_execute:
            mock_execute.return_value = MagicMock(id="dataset-123")
            result = await dataset.acreate(req, request_option)
            assert hasattr(result, "id")

    @pytest.mark.asyncio
    async def test_aget(self, dataset, request_option):
        """Test async get."""
        with patch("dify_oapi.core.http.transport.ATransport.aexecute") as mock_execute:
            mock_execute.return_value = MagicMock(id="dataset-123")
            result = await dataset.aget(MagicMock(), request_option)
            assert hasattr(result, "id")
