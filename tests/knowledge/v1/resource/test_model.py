"""Model resource tests."""

from unittest.mock import MagicMock, patch

import pytest

from dify_oapi.api.knowledge.v1.resource.model import Model
from dify_oapi.core.model.request_option import RequestOption


class TestModel:
    """Test Model resource."""

    @pytest.fixture
    def model(self, mock_config):
        """Create Model instance."""
        return Model(mock_config)

    @pytest.fixture
    def request_option(self):
        """Create request option."""
        return RequestOption.builder().api_key("test-key").build()

    def test_embedding_models(self, model, request_option):
        """Test get text embedding models."""
        with patch("dify_oapi.core.http.transport.Transport.execute") as mock_execute:
            mock_execute.return_value = MagicMock(data=[])
            result = model.embedding_models(MagicMock(), request_option)
            assert result.data == []
