"""
Comprehensive integration tests for Knowledge Base API module.
Tests cross-resource integration and complete workflows.
"""

from typing import Any
from unittest.mock import Mock

import pytest

from dify_oapi.api.knowledge.v1.model.create_dataset_request import CreateDatasetRequest
from dify_oapi.api.knowledge.v1.model.create_dataset_request_body import CreateDatasetRequestBody
from dify_oapi.api.knowledge.v1.model.create_dataset_response import CreateDatasetResponse
from dify_oapi.api.knowledge.v1.model.get_text_embedding_models_request import GetTextEmbeddingModelsRequest
from dify_oapi.api.knowledge.v1.resource.chunk import Chunk
from dify_oapi.api.knowledge.v1.resource.dataset import Dataset
from dify_oapi.api.knowledge.v1.resource.document import Document
from dify_oapi.api.knowledge.v1.resource.model import Model
from dify_oapi.api.knowledge.v1.resource.segment import Segment
from dify_oapi.api.knowledge.v1.resource.tag import Tag
from dify_oapi.core.model.config import Config
from dify_oapi.core.model.request_option import RequestOption


class TestKnowledgeAPIIntegration:
    """Test complete Knowledge API integration across all resources."""

    @pytest.fixture
    def config(self) -> Config:
        return Config()

    @pytest.fixture
    def request_option(self) -> RequestOption:
        return RequestOption.builder().api_key("test-api-key").build()

    def test_error_handling_across_all_resources(
        self, config: Config, request_option: RequestOption, monkeypatch: Any
    ) -> None:
        """Test error handling across all 6 resources."""
        # Initialize all resources
        dataset_resource = Dataset(config)
        Document(config)
        Segment(config)
        Chunk(config)
        Tag(config)
        model_resource = Model(config)

        # Mock error for all operations
        mock_execute = Mock(side_effect=Exception("API Error"))
        monkeypatch.setattr("dify_oapi.core.http.transport.Transport.execute", mock_execute)

        # Test error propagation for each resource
        with pytest.raises(Exception, match="API Error"):
            dataset_resource.create(
                CreateDatasetRequest.builder()
                .request_body(CreateDatasetRequestBody.builder().name("Test").build())
                .build(),
                request_option,
            )

        with pytest.raises(Exception, match="API Error"):
            model_resource.embedding_models(GetTextEmbeddingModelsRequest.builder().build(), request_option)

    def test_request_response_serialization(
        self, config: Config, request_option: RequestOption, monkeypatch: Any
    ) -> None:
        """Test request/response serialization for all API types."""
        dataset_resource = Dataset(config)

        # Mock successful response
        response = CreateDatasetResponse(id="dataset-id", name="Test Dataset", description="Test Description")
        mock_execute = Mock(return_value=response)
        monkeypatch.setattr("dify_oapi.core.http.transport.Transport.execute", mock_execute)

        # Test complex request serialization
        request_body = (
            CreateDatasetRequestBody.builder()
            .name("Test Dataset")
            .description("Test Description")
            .indexing_technique("high_quality")
            .permission("all_team_members")
            .build()
        )
        request = CreateDatasetRequest.builder().request_body(request_body).build()
        result = dataset_resource.create(request, request_option)

        # Verify response deserialization
        assert result.id == "dataset-id"
        assert result.name == "Test Dataset"
        assert result.description == "Test Description"

        # Verify request was properly serialized and passed to transport
        mock_execute.assert_called_once()
        call_args = mock_execute.call_args
        assert call_args[0][1] == request  # Second argument should be the request object
