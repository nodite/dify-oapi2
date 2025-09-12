"""Knowledge integration tests."""

from unittest.mock import MagicMock, patch

import pytest

from dify_oapi.api.knowledge.v1.model.create_dataset_request import CreateDatasetRequest
from dify_oapi.api.knowledge.v1.model.create_dataset_request_body import CreateDatasetRequestBody
from dify_oapi.client import Client
from dify_oapi.core.model.request_option import RequestOption


class TestKnowledgeIntegration:
    """Test Knowledge integration."""

    @pytest.fixture
    def client(self):
        """Create client."""
        return Client.builder().domain("https://api.dify.ai").build()

    @pytest.fixture
    def request_option(self):
        """Create request option."""
        return RequestOption.builder().api_key("test-key").build()

    def test_dataset_workflow(self, client, request_option):
        """Test dataset workflow."""
        req_body = CreateDatasetRequestBody.builder().name("test-dataset").build()
        req = CreateDatasetRequest.builder().request_body(req_body).build()

        with patch("dify_oapi.core.http.transport.Transport.execute") as mock_execute:
            mock_execute.return_value = MagicMock(id="dataset-123", name="test-dataset")
            result = client.knowledge.v1.dataset.create(req, request_option)
            assert hasattr(result, "id")
            assert hasattr(result, "name")

    def test_document_workflow(self, client, request_option):
        """Test document workflow."""
        with patch("dify_oapi.core.http.transport.Transport.execute") as mock_execute:
            mock_execute.return_value = MagicMock(document={"id": "doc-123"})
            result = client.knowledge.v1.document.create_by_text(MagicMock(), request_option)
            assert result.document["id"] == "doc-123"

    def test_error_handling(self, client, request_option):
        """Test error handling."""
        req_body = CreateDatasetRequestBody.builder().name("test").build()
        req = CreateDatasetRequest.builder().request_body(req_body).build()

        with patch("dify_oapi.core.http.transport.Transport.execute") as mock_execute:
            mock_execute.side_effect = Exception("API Error")
            with pytest.raises(Exception, match="API Error"):
                client.knowledge.v1.dataset.create(req, request_option)
