"""Tests for Model API models."""

from dify_oapi.api.knowledge.v1.model.get_text_embedding_models_request import (
    GetTextEmbeddingModelsRequest,
    GetTextEmbeddingModelsRequestBuilder,
)
from dify_oapi.api.knowledge.v1.model.get_text_embedding_models_response import GetTextEmbeddingModelsResponse
from dify_oapi.core.enum import HttpMethod
from dify_oapi.core.model.base_response import BaseResponse


class TestGetTextEmbeddingModelsModels:
    """Test Get Text Embedding Models API models."""

    def test_request_builder(self):
        """Test request builder pattern and configuration."""
        builder = GetTextEmbeddingModelsRequest.builder()
        assert isinstance(builder, GetTextEmbeddingModelsRequestBuilder)

        request = builder.build()
        assert isinstance(request, GetTextEmbeddingModelsRequest)
        assert request.http_method == HttpMethod.GET
        assert request.uri == "/v1/workspaces/current/models/model-types/text-embedding"

    def test_request_validation(self):
        """Test request structure and validation."""
        request = GetTextEmbeddingModelsRequest()
        assert request.http_method is None
        assert request.uri is None

        # Test builder creates proper request
        request = GetTextEmbeddingModelsRequest.builder().build()
        assert request.http_method == HttpMethod.GET
        assert request.uri == "/v1/workspaces/current/models/model-types/text-embedding"

    def test_response_inheritance(self):
        """Test response inherits from BaseResponse."""
        response = GetTextEmbeddingModelsResponse()
        assert isinstance(response, BaseResponse)
        assert hasattr(response, "success")
        assert hasattr(response, "code")
        assert hasattr(response, "msg")
        assert hasattr(response, "raw")

    def test_response_data_structure(self):
        """Test response data structure."""
        response = GetTextEmbeddingModelsResponse()
        assert hasattr(response, "data")
        assert response.data is None

        # Test with data
        response.data = []
        assert response.data == []
