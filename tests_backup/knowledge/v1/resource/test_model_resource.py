"""Tests for Model resource class."""

from unittest.mock import patch

import pytest

from dify_oapi.api.knowledge.v1.model.get_text_embedding_models_request import GetTextEmbeddingModelsRequest
from dify_oapi.api.knowledge.v1.model.get_text_embedding_models_response import GetTextEmbeddingModelsResponse
from dify_oapi.api.knowledge.v1.resource.model import Model
from dify_oapi.core.model.config import Config
from dify_oapi.core.model.request_option import RequestOption


class TestModelResource:
    """Test Model resource class."""

    def setup_method(self):
        """Set up test fixtures."""
        self.config = Config()
        self.model_resource = Model(self.config)
        self.request_option = RequestOption()

    @patch("dify_oapi.core.http.transport.Transport.execute")
    def test_embedding_models(self, mock_execute):
        """Test embedding_models method."""
        # Setup mock response
        mock_response = GetTextEmbeddingModelsResponse()
        mock_response.data = []
        mock_execute.return_value = mock_response

        # Create request
        request = GetTextEmbeddingModelsRequest.builder().build()

        # Execute method
        result = self.model_resource.embedding_models(request, self.request_option)

        # Verify
        assert isinstance(result, GetTextEmbeddingModelsResponse)
        mock_execute.assert_called_once_with(
            self.config, request, unmarshal_as=GetTextEmbeddingModelsResponse, option=self.request_option
        )

    @patch("dify_oapi.core.http.transport.ATransport.aexecute")
    @pytest.mark.asyncio
    async def test_aembedding_models(self, mock_aexecute):
        """Test aembedding_models async method."""
        # Setup mock response
        mock_response = GetTextEmbeddingModelsResponse()
        mock_response.data = []
        mock_aexecute.return_value = mock_response

        # Create request
        request = GetTextEmbeddingModelsRequest.builder().build()

        # Execute async method
        result = await self.model_resource.aembedding_models(request, self.request_option)

        # Verify
        assert isinstance(result, GetTextEmbeddingModelsResponse)
        mock_aexecute.assert_called_once_with(
            self.config, request, unmarshal_as=GetTextEmbeddingModelsResponse, option=self.request_option
        )

    def test_model_resource_initialization(self):
        """Test Model resource initialization."""
        assert self.model_resource.config == self.config
        assert isinstance(self.model_resource, Model)

    @patch("dify_oapi.core.http.transport.Transport.execute")
    def test_error_handling(self, mock_execute):
        """Test error handling in model resource methods."""
        # Setup mock to raise exception
        mock_execute.side_effect = Exception("API Error")

        # Create request
        request = GetTextEmbeddingModelsRequest.builder().build()

        # Test that exception is propagated
        with pytest.raises(Exception, match="API Error"):
            self.model_resource.embedding_models(request, self.request_option)
