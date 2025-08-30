"""
Comprehensive integration tests for Knowledge Base API module.
Tests cross-resource dependencies and complete workflows across all 6 resources.
"""

from typing import Any
from unittest.mock import AsyncMock, Mock

import pytest

from dify_oapi.api.knowledge.service import Knowledge
from dify_oapi.api.knowledge.v1.version import V1
from dify_oapi.client import Client
from dify_oapi.core.model.config import Config
from dify_oapi.core.model.request_option import RequestOption


class TestComprehensiveIntegrationValidation:
    """Test complete Knowledge module integration validation."""

    @pytest.fixture
    def client(self) -> Client:
        return Client.builder().domain("https://api.dify.ai").build()

    @pytest.fixture
    def config(self) -> Config:
        return Config()

    @pytest.fixture
    def request_option(self) -> RequestOption:
        return RequestOption.builder().api_key("test-api-key").build()

    def test_client_to_service_to_v1_to_resources_flow(
        self, client: Client, request_option: RequestOption, monkeypatch: Any
    ) -> None:
        """Test complete flow: Client -> Service -> V1 -> Resources -> Models."""
        # Mock successful dataset creation response
        from dify_oapi.api.knowledge.v1.model.create_dataset_response import CreateDatasetResponse

        response = CreateDatasetResponse(id="integration-dataset-id", name="Integration Test Dataset")
        mock_execute = Mock(return_value=response)
        monkeypatch.setattr("dify_oapi.core.http.transport.Transport.execute", mock_execute)

        # Test complete flow through all layers
        from dify_oapi.api.knowledge.v1.model.create_dataset_request import CreateDatasetRequest
        from dify_oapi.api.knowledge.v1.model.create_dataset_request_body import CreateDatasetRequestBody

        request_body = CreateDatasetRequestBody.builder().name("Integration Test Dataset").build()
        request = CreateDatasetRequest.builder().request_body(request_body).build()

        # Access through client -> knowledge service -> v1 -> dataset resource
        result = client.knowledge.v1.dataset.create(request, request_option)

        # Verify the complete chain worked
        assert result.id == "integration-dataset-id"
        assert result.name == "Integration Test Dataset"
        mock_execute.assert_called_once()

    def test_all_six_resources_accessible_through_v1(self, config: Config) -> None:
        """Test that all 6 resources are accessible through V1 class."""
        v1 = V1(config)

        # Verify all 6 resources are accessible
        assert hasattr(v1, "dataset")
        assert hasattr(v1, "document")
        assert hasattr(v1, "segment")
        assert hasattr(v1, "chunk")
        assert hasattr(v1, "tag")
        assert hasattr(v1, "model")

        # Verify resource types
        from dify_oapi.api.knowledge.v1.resource.chunk import Chunk
        from dify_oapi.api.knowledge.v1.resource.dataset import Dataset
        from dify_oapi.api.knowledge.v1.resource.document import Document
        from dify_oapi.api.knowledge.v1.resource.model import Model
        from dify_oapi.api.knowledge.v1.resource.segment import Segment
        from dify_oapi.api.knowledge.v1.resource.tag import Tag

        assert isinstance(v1.dataset, Dataset)
        assert isinstance(v1.document, Document)
        assert isinstance(v1.segment, Segment)
        assert isinstance(v1.chunk, Chunk)
        assert isinstance(v1.tag, Tag)
        assert isinstance(v1.model, Model)

    def test_knowledge_service_integration(self, config: Config) -> None:
        """Test Knowledge service integration."""
        knowledge_service = Knowledge(config)

        # Verify V1 integration
        assert hasattr(knowledge_service, "v1")
        assert isinstance(knowledge_service.v1, V1)

        # Verify all resources are accessible through service
        assert hasattr(knowledge_service.v1, "dataset")
        assert hasattr(knowledge_service.v1, "document")
        assert hasattr(knowledge_service.v1, "segment")
        assert hasattr(knowledge_service.v1, "chunk")
        assert hasattr(knowledge_service.v1, "tag")
        assert hasattr(knowledge_service.v1, "model")

    def test_cross_resource_workflow_integration(
        self, client: Client, request_option: RequestOption, monkeypatch: Any
    ) -> None:
        """Test complete workflow: create dataset -> add document -> create segments -> manage chunks."""
        # Mock responses for complete workflow
        from dify_oapi.api.knowledge.v1.model.child_chunk_info import ChildChunkInfo
        from dify_oapi.api.knowledge.v1.model.create_child_chunk_response import CreateChildChunkResponse
        from dify_oapi.api.knowledge.v1.model.create_dataset_response import CreateDatasetResponse
        from dify_oapi.api.knowledge.v1.model.create_document_by_text_response import CreateDocumentByTextResponse
        from dify_oapi.api.knowledge.v1.model.create_segment_response import CreateSegmentResponse
        from dify_oapi.api.knowledge.v1.model.document_info import DocumentInfo
        from dify_oapi.api.knowledge.v1.model.segment_info import SegmentInfo

        responses = [
            CreateDatasetResponse(id="workflow-dataset", name="Workflow Dataset"),
            CreateDocumentByTextResponse(
                document=DocumentInfo(id="workflow-doc", name="Workflow Document"), batch="batch-1"
            ),
            CreateSegmentResponse(data=[SegmentInfo(id="workflow-segment", content="Workflow segment")]),
            CreateChildChunkResponse(data=[ChildChunkInfo(id="workflow-chunk", content="Workflow chunk")]),
        ]

        mock_execute = Mock()
        mock_execute.side_effect = responses
        monkeypatch.setattr("dify_oapi.core.http.transport.Transport.execute", mock_execute)

        # Execute complete workflow
        from dify_oapi.api.knowledge.v1.model.create_child_chunk_request import CreateChildChunkRequest
        from dify_oapi.api.knowledge.v1.model.create_child_chunk_request_body import CreateChildChunkRequestBody
        from dify_oapi.api.knowledge.v1.model.create_dataset_request import CreateDatasetRequest
        from dify_oapi.api.knowledge.v1.model.create_dataset_request_body import CreateDatasetRequestBody
        from dify_oapi.api.knowledge.v1.model.create_document_by_text_request import CreateDocumentByTextRequest
        from dify_oapi.api.knowledge.v1.model.create_document_by_text_request_body import (
            CreateDocumentByTextRequestBody,
        )
        from dify_oapi.api.knowledge.v1.model.create_segment_request import CreateSegmentRequest
        from dify_oapi.api.knowledge.v1.model.create_segment_request_body import CreateSegmentRequestBody

        # 1. Create dataset
        dataset_request_body = CreateDatasetRequestBody.builder().name("Workflow Dataset").build()
        dataset_request = CreateDatasetRequest.builder().request_body(dataset_request_body).build()
        dataset_result = client.knowledge.v1.dataset.create(dataset_request, request_option)
        assert dataset_result.id == "workflow-dataset"

        # 2. Add document to dataset
        document_request_body = (
            CreateDocumentByTextRequestBody.builder().name("Workflow Document").text("Document content").build()
        )
        document_request = (
            CreateDocumentByTextRequest.builder()
            .dataset_id("workflow-dataset")
            .request_body(document_request_body)
            .build()
        )
        document_result = client.knowledge.v1.document.create_by_text(document_request, request_option)
        assert document_result.document.id == "workflow-doc"

        # 3. Create segments in document
        from dify_oapi.api.knowledge.v1.model.create_segment_request_body import SegmentContent

        segment_content = SegmentContent(content="Workflow segment")
        segment_request_body = CreateSegmentRequestBody.builder().segments([segment_content]).build()
        segment_request = (
            CreateSegmentRequest.builder()
            .dataset_id("workflow-dataset")
            .document_id("workflow-doc")
            .request_body(segment_request_body)
            .build()
        )
        segment_result = client.knowledge.v1.segment.create(segment_request, request_option)
        assert segment_result.data[0].id == "workflow-segment"

        # 4. Create child chunks in segment
        from dify_oapi.api.knowledge.v1.model.create_child_chunk_request_body import ChunkContent

        chunk_content = ChunkContent(content="Workflow chunk")
        chunk_request_body = CreateChildChunkRequestBody.builder().chunks([chunk_content]).build()
        chunk_request = (
            CreateChildChunkRequest.builder()
            .dataset_id("workflow-dataset")
            .document_id("workflow-doc")
            .segment_id("workflow-segment")
            .request_body(chunk_request_body)
            .build()
        )
        chunk_result = client.knowledge.v1.chunk.create(chunk_request, request_option)
        assert chunk_result.data[0].id == "workflow-chunk"

        # Verify all operations were executed
        assert mock_execute.call_count == 4

    def test_tag_management_across_multiple_datasets(
        self, client: Client, request_option: RequestOption, monkeypatch: Any
    ) -> None:
        """Test tag management across multiple datasets."""
        # Mock responses for tag management workflow
        from dify_oapi.api.knowledge.v1.model.bind_tags_to_dataset_response import BindTagsToDatasetResponse
        from dify_oapi.api.knowledge.v1.model.create_dataset_response import CreateDatasetResponse
        from dify_oapi.api.knowledge.v1.model.create_tag_response import CreateTagResponse
        from dify_oapi.api.knowledge.v1.model.get_dataset_tags_response import GetDatasetTagsResponse
        from dify_oapi.api.knowledge.v1.model.tag_info import TagInfo

        responses = [
            CreateDatasetResponse(id="dataset-1", name="Dataset 1"),
            CreateDatasetResponse(id="dataset-2", name="Dataset 2"),
            CreateTagResponse(id="shared-tag", name="Shared Tag", type="knowledge", binding_count=0),
            BindTagsToDatasetResponse(result="success"),
            BindTagsToDatasetResponse(result="success"),
            GetDatasetTagsResponse(data=[TagInfo(id="shared-tag", name="Shared Tag", type="knowledge")]),
            GetDatasetTagsResponse(data=[TagInfo(id="shared-tag", name="Shared Tag", type="knowledge")]),
        ]

        mock_execute = Mock()
        mock_execute.side_effect = responses
        monkeypatch.setattr("dify_oapi.core.http.transport.Transport.execute", mock_execute)

        # Execute tag management workflow
        from dify_oapi.api.knowledge.v1.model.bind_tags_to_dataset_request import BindTagsToDatasetRequest
        from dify_oapi.api.knowledge.v1.model.bind_tags_to_dataset_request_body import BindTagsToDatasetRequestBody
        from dify_oapi.api.knowledge.v1.model.create_dataset_request import CreateDatasetRequest
        from dify_oapi.api.knowledge.v1.model.create_dataset_request_body import CreateDatasetRequestBody
        from dify_oapi.api.knowledge.v1.model.create_tag_request import CreateTagRequest
        from dify_oapi.api.knowledge.v1.model.create_tag_request_body import CreateTagRequestBody
        from dify_oapi.api.knowledge.v1.model.get_dataset_tags_request import GetDatasetTagsRequest

        # 1. Create two datasets
        dataset1_request_body = CreateDatasetRequestBody.builder().name("Dataset 1").build()
        dataset1_request = CreateDatasetRequest.builder().request_body(dataset1_request_body).build()
        dataset1_result = client.knowledge.v1.dataset.create(dataset1_request, request_option)
        assert dataset1_result.id == "dataset-1"

        dataset2_request_body = CreateDatasetRequestBody.builder().name("Dataset 2").build()
        dataset2_request = CreateDatasetRequest.builder().request_body(dataset2_request_body).build()
        dataset2_result = client.knowledge.v1.dataset.create(dataset2_request, request_option)
        assert dataset2_result.id == "dataset-2"

        # 2. Create shared tag
        tag_request_body = CreateTagRequestBody.builder().name("Shared Tag").type("knowledge").build()
        tag_request = CreateTagRequest.builder().request_body(tag_request_body).build()
        tag_result = client.knowledge.v1.tag.create(tag_request, request_option)
        assert tag_result.id == "shared-tag"

        # 3. Bind tag to both datasets
        bind1_request_body = (
            BindTagsToDatasetRequestBody.builder().target_id("dataset-1").tag_ids(["shared-tag"]).build()
        )
        bind1_request = BindTagsToDatasetRequest.builder().request_body(bind1_request_body).build()
        bind1_result = client.knowledge.v1.tag.bind(bind1_request, request_option)
        assert bind1_result.result == "success"

        bind2_request_body = (
            BindTagsToDatasetRequestBody.builder().target_id("dataset-2").tag_ids(["shared-tag"]).build()
        )
        bind2_request = BindTagsToDatasetRequest.builder().request_body(bind2_request_body).build()
        bind2_result = client.knowledge.v1.tag.bind(bind2_request, request_option)
        assert bind2_result.result == "success"

        # 4. Verify both datasets have the shared tag
        get_tags1_request = GetDatasetTagsRequest.builder().dataset_id("dataset-1").build()
        tags1_result = client.knowledge.v1.tag.get_dataset_tags(get_tags1_request, request_option)
        assert len(tags1_result.data) == 1
        assert tags1_result.data[0].id == "shared-tag"

        get_tags2_request = GetDatasetTagsRequest.builder().dataset_id("dataset-2").build()
        tags2_result = client.knowledge.v1.tag.get_dataset_tags(get_tags2_request, request_option)
        assert len(tags2_result.data) == 1
        assert tags2_result.data[0].id == "shared-tag"

        # Verify all operations were executed
        assert mock_execute.call_count == 7

    def test_model_resource_integration(self, client: Client, request_option: RequestOption, monkeypatch: Any) -> None:
        """Test model resource integration."""
        # Mock model response
        from dify_oapi.api.knowledge.v1.model.get_text_embedding_models_response import GetTextEmbeddingModelsResponse
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

        # Test model resource
        from dify_oapi.api.knowledge.v1.model.get_text_embedding_models_request import GetTextEmbeddingModelsRequest

        model_request = GetTextEmbeddingModelsRequest.builder().build()
        model_result = client.knowledge.v1.model.embedding_models(model_request, request_option)

        assert len(model_result.data) == 1
        assert model_result.data[0].provider == "openai"
        assert len(model_result.data[0].models) == 1
        assert model_result.data[0].models[0].model == "text-embedding-ada-002"

        mock_execute.assert_called_once()

    @pytest.mark.asyncio
    async def test_async_operations_across_resources(
        self, client: Client, request_option: RequestOption, monkeypatch: Any
    ) -> None:
        """Test async operations across all resources."""
        # Mock async responses
        from dify_oapi.api.knowledge.v1.model.create_dataset_response import CreateDatasetResponse
        from dify_oapi.api.knowledge.v1.model.create_tag_response import CreateTagResponse
        from dify_oapi.api.knowledge.v1.model.get_text_embedding_models_response import GetTextEmbeddingModelsResponse

        responses = [
            CreateDatasetResponse(id="async-dataset", name="Async Dataset"),
            CreateTagResponse(id="async-tag", name="Async Tag", type="knowledge", binding_count=0),
            GetTextEmbeddingModelsResponse(data=[]),
        ]

        mock_aexecute = AsyncMock()
        mock_aexecute.side_effect = responses
        monkeypatch.setattr("dify_oapi.core.http.transport.ATransport.aexecute", mock_aexecute)

        # Execute async operations
        from dify_oapi.api.knowledge.v1.model.create_dataset_request import CreateDatasetRequest
        from dify_oapi.api.knowledge.v1.model.create_dataset_request_body import CreateDatasetRequestBody
        from dify_oapi.api.knowledge.v1.model.create_tag_request import CreateTagRequest
        from dify_oapi.api.knowledge.v1.model.create_tag_request_body import CreateTagRequestBody
        from dify_oapi.api.knowledge.v1.model.get_text_embedding_models_request import GetTextEmbeddingModelsRequest

        # Async dataset creation
        dataset_request_body = CreateDatasetRequestBody.builder().name("Async Dataset").build()
        dataset_request = CreateDatasetRequest.builder().request_body(dataset_request_body).build()
        dataset_result = await client.knowledge.v1.dataset.acreate(dataset_request, request_option)
        assert dataset_result.id == "async-dataset"

        # Async tag creation
        tag_request_body = CreateTagRequestBody.builder().name("Async Tag").type("knowledge").build()
        tag_request = CreateTagRequest.builder().request_body(tag_request_body).build()
        tag_result = await client.knowledge.v1.tag.acreate(tag_request, request_option)
        assert tag_result.id == "async-tag"

        # Async model retrieval
        model_request = GetTextEmbeddingModelsRequest.builder().build()
        model_result = await client.knowledge.v1.model.aembedding_models(model_request, request_option)
        assert len(model_result.data) == 0

        # Verify all async operations were executed
        assert mock_aexecute.call_count == 3

    def test_error_handling_across_resources(
        self, client: Client, request_option: RequestOption, monkeypatch: Any
    ) -> None:
        """Test error handling and propagation across resources."""
        # Mock error responses
        mock_execute = Mock(side_effect=Exception("API Error"))
        monkeypatch.setattr("dify_oapi.core.http.transport.Transport.execute", mock_execute)

        # Test error propagation in dataset operations
        from dify_oapi.api.knowledge.v1.model.create_dataset_request import CreateDatasetRequest
        from dify_oapi.api.knowledge.v1.model.create_dataset_request_body import CreateDatasetRequestBody

        dataset_request_body = CreateDatasetRequestBody.builder().name("Error Dataset").build()
        dataset_request = CreateDatasetRequest.builder().request_body(dataset_request_body).build()

        with pytest.raises(Exception) as exc_info:
            client.knowledge.v1.dataset.create(dataset_request, request_option)
        assert str(exc_info.value) == "API Error"

        # Test error propagation in tag operations
        from dify_oapi.api.knowledge.v1.model.create_tag_request import CreateTagRequest
        from dify_oapi.api.knowledge.v1.model.create_tag_request_body import CreateTagRequestBody

        tag_request_body = CreateTagRequestBody.builder().name("Error Tag").type("knowledge").build()
        tag_request = CreateTagRequest.builder().request_body(tag_request_body).build()

        with pytest.raises(Exception) as exc_info:
            client.knowledge.v1.tag.create(tag_request, request_option)
        assert str(exc_info.value) == "API Error"

    def test_resource_isolation_and_independence(self, config: Config) -> None:
        """Test that resources are properly isolated and independent."""
        v1 = V1(config)

        # Verify each resource has its own instance
        assert v1.dataset is not v1.document
        assert v1.document is not v1.segment
        assert v1.segment is not v1.chunk
        assert v1.chunk is not v1.tag
        assert v1.tag is not v1.model

        # Verify each resource has the same config
        assert v1.dataset.config is config
        assert v1.document.config is config
        assert v1.segment.config is config
        assert v1.chunk.config is config
        assert v1.tag.config is config
        assert v1.model.config is config

    def test_complete_api_coverage_validation(self, config: Config) -> None:
        """Test that all 33 APIs are accessible through the resource structure."""
        v1 = V1(config)

        # Dataset resource (6 methods)
        dataset_methods = ["create", "list", "get", "update", "delete", "retrieve"]
        for method in dataset_methods:
            assert hasattr(v1.dataset, method), f"Dataset resource missing method: {method}"
            assert hasattr(v1.dataset, f"a{method}"), f"Dataset resource missing async method: a{method}"

        # Document resource (10 methods)
        document_methods = [
            "create_by_file",
            "create_by_text",
            "list",
            "get",
            "update_by_file",
            "update_by_text",
            "delete",
            "update_status",
            "get_batch_status",
            "file_info",
        ]
        for method in document_methods:
            assert hasattr(v1.document, method), f"Document resource missing method: {method}"
            assert hasattr(v1.document, f"a{method}"), f"Document resource missing async method: a{method}"

        # Segment resource (5 methods)
        segment_methods = ["list", "create", "get", "update", "delete"]
        for method in segment_methods:
            assert hasattr(v1.segment, method), f"Segment resource missing method: {method}"
            assert hasattr(v1.segment, f"a{method}"), f"Segment resource missing async method: a{method}"

        # Chunk resource (4 methods)
        chunk_methods = ["list", "create", "update", "delete"]
        for method in chunk_methods:
            assert hasattr(v1.chunk, method), f"Chunk resource missing method: {method}"
            assert hasattr(v1.chunk, f"a{method}"), f"Chunk resource missing async method: a{method}"

        # Tag resource (7 methods)
        tag_methods = ["list", "create", "update", "delete", "bind", "unbind", "get_dataset_tags"]
        for method in tag_methods:
            assert hasattr(v1.tag, method), f"Tag resource missing method: {method}"
            assert hasattr(v1.tag, f"a{method}"), f"Tag resource missing async method: a{method}"

        # Model resource (1 method)
        model_methods = ["embedding_models"]
        for method in model_methods:
            assert hasattr(v1.model, method), f"Model resource missing method: {method}"
            assert hasattr(v1.model, f"a{method}"), f"Model resource missing async method: a{method}"

        # Total: 6 + 10 + 5 + 4 + 7 + 1 = 33 APIs
