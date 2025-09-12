"""Integration tests for Model API functionality."""

from typing import Any
from unittest.mock import Mock

import pytest

from dify_oapi.api.knowledge.v1.model.get_text_embedding_models_request import GetTextEmbeddingModelsRequest
from dify_oapi.api.knowledge.v1.model.get_text_embedding_models_response import GetTextEmbeddingModelsResponse
from dify_oapi.api.knowledge.v1.resource.model import Model
from dify_oapi.core.model.config import Config
from dify_oapi.core.model.request_option import RequestOption


class TestModelIntegration:
    """Test the 1 Model Resource API."""

    @pytest.fixture
    def model_resource(self) -> Model:
        return Model(Config())

    @pytest.fixture
    def request_option(self) -> RequestOption:
        return RequestOption.builder().api_key("test-api-key").build()

    def test_get_text_embedding_models(
        self, model_resource: Model, request_option: RequestOption, monkeypatch: Any
    ) -> None:
        """Test GET /v1/workspaces/current/models/model-types/text-embedding"""
        response = GetTextEmbeddingModelsResponse(data=[])
        mock_execute = Mock(return_value=response)
        monkeypatch.setattr("dify_oapi.core.http.transport.Transport.execute", mock_execute)

        request = GetTextEmbeddingModelsRequest.builder().build()
        result = model_resource.embedding_models(request, request_option)

        assert result.data == []

    def test_get_text_embedding_models_with_data(
        self, model_resource: Model, request_option: RequestOption, monkeypatch: Any
    ) -> None:
        """Test GET /v1/workspaces/current/models/model-types/text-embedding with model data"""
        from dify_oapi.api.knowledge.v1.model.model_info import EmbeddingModelDetails, ModelIcon, ModelInfo, ModelLabel
        from dify_oapi.api.knowledge.v1.model.model_parameters import ModelParameters

        model_response = GetTextEmbeddingModelsResponse(
            data=[
                ModelInfo(
                    provider="openai",
                    label=ModelLabel(en_US="OpenAI"),
                    icon_small=ModelIcon(en_US="https://example.com/icon.png"),
                    icon_large=ModelIcon(en_US="https://example.com/icon_large.png"),
                    status="active",
                    models=[
                        EmbeddingModelDetails(
                            model="text-embedding-ada-002",
                            label=ModelLabel(en_US="Text Embedding Ada 002"),
                            model_type="text-embedding",
                            features=[],
                            fetch_from="predefined-model",
                            model_properties=ModelParameters(context_size=8191),
                            deprecated=False,
                            status="active",
                            load_balancing_enabled=False,
                        )
                    ],
                )
            ]
        )

        mock_execute = Mock(return_value=model_response)
        monkeypatch.setattr("dify_oapi.core.http.transport.Transport.execute", mock_execute)

        request = GetTextEmbeddingModelsRequest.builder().build()
        result = model_resource.embedding_models(request, request_option)

        assert len(result.data) == 1
        assert result.data[0].provider == "openai"
        assert len(result.data[0].models) == 1
        assert result.data[0].models[0].model == "text-embedding-ada-002"

    def test_error_handling(self, model_resource: Model, request_option: RequestOption, monkeypatch: Any) -> None:
        """Test error handling scenarios"""
        # Mock error response
        mock_execute = Mock(side_effect=Exception("Model API Error"))
        monkeypatch.setattr("dify_oapi.core.http.transport.Transport.execute", mock_execute)

        request = GetTextEmbeddingModelsRequest.builder().build()

        with pytest.raises(Exception) as exc_info:
            model_resource.embedding_models(request, request_option)

        assert str(exc_info.value) == "Model API Error"
