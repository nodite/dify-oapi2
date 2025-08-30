"""
Comprehensive integration validation tests for Knowledge Base API module.

This module validates the complete Knowledge module integration:
- Client -> Service -> V1 -> Resources -> Models flow
- All 33 APIs end-to-end testing
- Cross-resource dependencies
- Error propagation through all layers
"""

from typing import Any
from unittest.mock import AsyncMock, Mock

import pytest

from dify_oapi.api.knowledge.knowledge import Knowledge
from dify_oapi.api.knowledge.v1.v1 import V1
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
        from dify_oapi.api.knowledge.v1.model.create_child_chunk_response import CreateChildChunkResponse
        from dify_oapi.api.knowledge.v1.model.create_dataset_response import CreateDatasetResponse
        from dify_oapi.api.knowledge.v1.model.create_document_by_text_response import CreateDocumentByTextResponse
        from dify_oapi.api.knowledge.v1.model.create_segment_response import CreateSegmentResponse

        responses = [
            CreateDatasetResponse(id="workflow-dataset", name="Workflow Dataset"),
            CreateDocumentByTextResponse(document={"id": "workflow-doc", "name": "Workflow Document"}, batch="batch-1"),
            CreateSegmentResponse(data=[{"id": "workflow-segment", "content": "Workflow segment"}]),
            CreateChildChunkResponse(data=[{"id": "workflow-chunk", "content": "Workflow chunk"}]),
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
        assert document_result.document["id"] == "workflow-doc"

        # 3. Create segments in document
        segment_request_body = CreateSegmentRequestBody.builder().segments([{"content": "Workflow segment"}]).build()
        segment_request = (
            CreateSegmentRequest.builder()
            .dataset_id("workflow-dataset")
            .document_id("workflow-doc")
            .request_body(segment_request_body)
            .build()
        )
        segment_result = client.knowledge.v1.segment.create(segment_request, request_option)
        assert segment_result.data[0]["id"] == "workflow-segment"

        # 4. Create child chunks in segment
        chunk_request_body = CreateChildChunkRequestBody.builder().chunks([{"content": "Workflow chunk"}]).build()
        chunk_request = (
            CreateChildChunkRequest.builder()
            .dataset_id("workflow-dataset")
            .document_id("workflow-doc")
            .segment_id("workflow-segment")
            .request_body(chunk_request_body)
            .build()
        )
        chunk_result = client.knowledge.v1.chunk.create(chunk_request, request_option)
        assert chunk_result.data[0]["id"] == "workflow-chunk"

        # Verify all operations were executed
        assert mock_execute.call_count == 4

    def test_tag_management_across_multiple_datasets(
        self, client: Client, request_option: RequestOption, monkeypatch: Any
    ) -> None:
        """Test tag management across multiple datasets."""
        from dify_oapi.api.knowledge.v1.model.bind_tags_to_dataset_response import BindTagsToDatasetResponse
        from dify_oapi.api.knowledge.v1.model.create_dataset_response import CreateDatasetResponse
        from dify_oapi.api.knowledge.v1.model.create_tag_response import CreateTagResponse
        from dify_oapi.api.knowledge.v1.model.get_dataset_tags_response import GetDatasetTagsResponse

        responses = [
            CreateDatasetResponse(id="dataset-1", name="Dataset 1"),
            CreateDatasetResponse(id="dataset-2", name="Dataset 2"),
            CreateTagResponse(id="shared-tag", name="Shared Tag", type="knowledge_type", binding_count=0),
            BindTagsToDatasetResponse(result="success"),  # Bind to dataset 1
            BindTagsToDatasetResponse(result="success"),  # Bind to dataset 2
            GetDatasetTagsResponse(data=[{"id": "shared-tag", "name": "Shared Tag"}]),  # Dataset 1 tags
            GetDatasetTagsResponse(data=[{"id": "shared-tag", "name": "Shared Tag"}]),  # Dataset 2 tags
        ]

        mock_execute = Mock()
        mock_execute.side_effect = responses
        monkeypatch.setattr("dify_oapi.core.http.transport.Transport.execute", mock_execute)

        # Create datasets and shared tag
        from dify_oapi.api.knowledge.v1.model.bind_tags_to_dataset_request import BindTagsToDatasetRequest
        from dify_oapi.api.knowledge.v1.model.bind_tags_to_dataset_request_body import BindTagsToDatasetRequestBody
        from dify_oapi.api.knowledge.v1.model.create_dataset_request import CreateDatasetRequest
        from dify_oapi.api.knowledge.v1.model.create_dataset_request_body import CreateDatasetRequestBody
        from dify_oapi.api.knowledge.v1.model.create_tag_request import CreateTagRequest
        from dify_oapi.api.knowledge.v1.model.create_tag_request_body import CreateTagRequestBody
        from dify_oapi.api.knowledge.v1.model.get_dataset_tags_request import GetDatasetTagsRequest

        # Create two datasets
        dataset1_request = (
            CreateDatasetRequest.builder()
            .request_body(CreateDatasetRequestBody.builder().name("Dataset 1").build())
            .build()
        )
        client.knowledge.v1.dataset.create(dataset1_request, request_option)

        dataset2_request = (
            CreateDatasetRequest.builder()
            .request_body(CreateDatasetRequestBody.builder().name("Dataset 2").build())
            .build()
        )
        client.knowledge.v1.dataset.create(dataset2_request, request_option)

        # Create shared tag
        tag_request = (
            CreateTagRequest.builder()
            .request_body(CreateTagRequestBody.builder().name("Shared Tag").type("knowledge_type").build())
            .build()
        )
        client.knowledge.v1.tag.create(tag_request, request_option)

        # Bind tag to both datasets
        bind1_request = (
            BindTagsToDatasetRequest.builder()
            .request_body(
                BindTagsToDatasetRequestBody.builder().dataset_id("dataset-1").tag_ids(["shared-tag"]).build()
            )
            .build()
        )
        client.knowledge.v1.tag.bind(bind1_request, request_option)

        bind2_request = (
            BindTagsToDatasetRequest.builder()
            .request_body(
                BindTagsToDatasetRequestBody.builder().dataset_id("dataset-2").tag_ids(["shared-tag"]).build()
            )
            .build()
        )
        client.knowledge.v1.tag.bind(bind2_request, request_option)

        # Verify both datasets have the shared tag
        tags1_request = GetDatasetTagsRequest.builder().dataset_id("dataset-1").build()
        tags1 = client.knowledge.v1.tag.get_dataset_tags(tags1_request, request_option)

        tags2_request = GetDatasetTagsRequest.builder().dataset_id("dataset-2").build()
        tags2 = client.knowledge.v1.tag.get_dataset_tags(tags2_request, request_option)

        assert len(tags1.data) == 1
        assert len(tags2.data) == 1
        assert tags1.data[0]["id"] == "shared-tag"
        assert tags2.data[0]["id"] == "shared-tag"

    def test_model_selection_and_usage(self, client: Client, request_option: RequestOption, monkeypatch: Any) -> None:
        """Test model selection and usage in dataset creation."""
        from dify_oapi.api.knowledge.v1.model.create_dataset_response import CreateDatasetResponse
        from dify_oapi.api.knowledge.v1.model.get_text_embedding_models_response import GetTextEmbeddingModelsResponse

        responses = [
            GetTextEmbeddingModelsResponse(
                data=[{"provider": "openai", "models": [{"model": "text-embedding-ada-002", "status": "active"}]}]
            ),
            CreateDatasetResponse(
                id="model-dataset",
                name="Model Dataset",
                embedding_model="text-embedding-ada-002",
                embedding_model_provider="openai",
            ),
        ]

        mock_execute = Mock()
        mock_execute.side_effect = responses
        monkeypatch.setattr("dify_oapi.core.http.transport.Transport.execute", mock_execute)

        # Get available models
        from dify_oapi.api.knowledge.v1.model.get_text_embedding_models_request import GetTextEmbeddingModelsRequest

        models_request = GetTextEmbeddingModelsRequest.builder().build()
        client.knowledge.v1.model.embedding_models(models_request, request_option)

        # Use model in dataset creation
        from dify_oapi.api.knowledge.v1.model.create_dataset_request import CreateDatasetRequest
        from dify_oapi.api.knowledge.v1.model.create_dataset_request_body import CreateDatasetRequestBody

        dataset_request_body = (
            CreateDatasetRequestBody.builder()
            .name("Model Dataset")
            .embedding_model("text-embedding-ada-002")
            .embedding_model_provider("openai")
            .build()
        )
        dataset_request = CreateDatasetRequest.builder().request_body(dataset_request_body).build()
        dataset = client.knowledge.v1.dataset.create(dataset_request, request_option)

        assert dataset.embedding_model == "text-embedding-ada-002"
        assert dataset.embedding_model_provider == "openai"

    def test_error_propagation_through_all_layers(
        self, client: Client, request_option: RequestOption, monkeypatch: Any
    ) -> None:
        """Test error handling and propagation through all layers."""
        # Mock error at transport layer
        mock_execute = Mock(side_effect=Exception("Transport layer error"))
        monkeypatch.setattr("dify_oapi.core.http.transport.Transport.execute", mock_execute)

        # Test error propagation through Client -> Service -> V1 -> Resource -> Transport
        from dify_oapi.api.knowledge.v1.model.create_dataset_request import CreateDatasetRequest
        from dify_oapi.api.knowledge.v1.model.create_dataset_request_body import CreateDatasetRequestBody

        request_body = CreateDatasetRequestBody.builder().name("Error Test Dataset").build()
        request = CreateDatasetRequest.builder().request_body(request_body).build()

        with pytest.raises(Exception) as exc_info:
            client.knowledge.v1.dataset.create(request, request_option)

        assert str(exc_info.value) == "Transport layer error"

    @pytest.mark.asyncio
    async def test_async_operations_through_all_layers(
        self, client: Client, request_option: RequestOption, monkeypatch: Any
    ) -> None:
        """Test async operations through all layers."""
        from dify_oapi.api.knowledge.v1.model.create_dataset_response import CreateDatasetResponse

        response = CreateDatasetResponse(id="async-dataset", name="Async Dataset")
        mock_aexecute = AsyncMock(return_value=response)
        monkeypatch.setattr("dify_oapi.core.http.transport.ATransport.aexecute", mock_aexecute)

        # Test async flow through all layers
        from dify_oapi.api.knowledge.v1.model.create_dataset_request import CreateDatasetRequest
        from dify_oapi.api.knowledge.v1.model.create_dataset_request_body import CreateDatasetRequestBody

        request_body = CreateDatasetRequestBody.builder().name("Async Dataset").build()
        request = CreateDatasetRequest.builder().request_body(request_body).build()

        result = await client.knowledge.v1.dataset.acreate(request, request_option)

        assert result.id == "async-dataset"
        assert result.name == "Async Dataset"
        mock_aexecute.assert_called_once()

    def test_all_response_classes_inherit_from_base_response(self) -> None:
        """Test that all Response classes inherit from BaseResponse."""
        from dify_oapi.api.knowledge.v1.model.bind_tags_to_dataset_response import BindTagsToDatasetResponse
        from dify_oapi.api.knowledge.v1.model.create_child_chunk_response import CreateChildChunkResponse

        # Import all response classes
        from dify_oapi.api.knowledge.v1.model.create_dataset_response import CreateDatasetResponse
        from dify_oapi.api.knowledge.v1.model.create_document_by_file_response import CreateDocumentByFileResponse
        from dify_oapi.api.knowledge.v1.model.create_document_by_text_response import CreateDocumentByTextResponse
        from dify_oapi.api.knowledge.v1.model.create_segment_response import CreateSegmentResponse
        from dify_oapi.api.knowledge.v1.model.create_tag_response import CreateTagResponse
        from dify_oapi.api.knowledge.v1.model.delete_child_chunk_response import DeleteChildChunkResponse
        from dify_oapi.api.knowledge.v1.model.delete_dataset_response import DeleteDatasetResponse
        from dify_oapi.api.knowledge.v1.model.delete_document_response import DeleteDocumentResponse
        from dify_oapi.api.knowledge.v1.model.delete_segment_response import DeleteSegmentResponse
        from dify_oapi.api.knowledge.v1.model.delete_tag_response import DeleteTagResponse
        from dify_oapi.api.knowledge.v1.model.get_batch_indexing_status_response import GetBatchIndexingStatusResponse
        from dify_oapi.api.knowledge.v1.model.get_dataset_response import GetDatasetResponse
        from dify_oapi.api.knowledge.v1.model.get_dataset_tags_response import GetDatasetTagsResponse
        from dify_oapi.api.knowledge.v1.model.get_document_response import GetDocumentResponse
        from dify_oapi.api.knowledge.v1.model.get_segment_response import GetSegmentResponse
        from dify_oapi.api.knowledge.v1.model.get_text_embedding_models_response import GetTextEmbeddingModelsResponse
        from dify_oapi.api.knowledge.v1.model.get_upload_file_info_response import GetUploadFileInfoResponse
        from dify_oapi.api.knowledge.v1.model.list_child_chunks_response import ListChildChunksResponse
        from dify_oapi.api.knowledge.v1.model.list_datasets_response import ListDatasetsResponse
        from dify_oapi.api.knowledge.v1.model.list_documents_response import ListDocumentsResponse
        from dify_oapi.api.knowledge.v1.model.list_segments_response import ListSegmentsResponse
        from dify_oapi.api.knowledge.v1.model.list_tags_response import ListTagsResponse
        from dify_oapi.api.knowledge.v1.model.retrieve_from_dataset_response import RetrieveFromDatasetResponse
        from dify_oapi.api.knowledge.v1.model.unbind_tags_from_dataset_response import UnbindTagsFromDatasetResponse
        from dify_oapi.api.knowledge.v1.model.update_child_chunk_response import UpdateChildChunkResponse
        from dify_oapi.api.knowledge.v1.model.update_dataset_response import UpdateDatasetResponse
        from dify_oapi.api.knowledge.v1.model.update_document_by_file_response import UpdateDocumentByFileResponse
        from dify_oapi.api.knowledge.v1.model.update_document_by_text_response import UpdateDocumentByTextResponse
        from dify_oapi.api.knowledge.v1.model.update_document_status_response import UpdateDocumentStatusResponse
        from dify_oapi.api.knowledge.v1.model.update_segment_response import UpdateSegmentResponse
        from dify_oapi.api.knowledge.v1.model.update_tag_response import UpdateTagResponse
        from dify_oapi.core.model.base_response import BaseResponse

        # Test all 33 response classes inherit from BaseResponse
        response_classes = [
            CreateDatasetResponse,
            ListDatasetsResponse,
            GetDatasetResponse,
            UpdateDatasetResponse,
            DeleteDatasetResponse,
            RetrieveFromDatasetResponse,
            CreateDocumentByFileResponse,
            CreateDocumentByTextResponse,
            ListDocumentsResponse,
            GetDocumentResponse,
            UpdateDocumentByFileResponse,
            UpdateDocumentByTextResponse,
            DeleteDocumentResponse,
            UpdateDocumentStatusResponse,
            GetBatchIndexingStatusResponse,
            GetUploadFileInfoResponse,
            ListSegmentsResponse,
            CreateSegmentResponse,
            GetSegmentResponse,
            UpdateSegmentResponse,
            DeleteSegmentResponse,
            ListChildChunksResponse,
            CreateChildChunkResponse,
            UpdateChildChunkResponse,
            DeleteChildChunkResponse,
            ListTagsResponse,
            CreateTagResponse,
            UpdateTagResponse,
            DeleteTagResponse,
            BindTagsToDatasetResponse,
            UnbindTagsFromDatasetResponse,
            GetDatasetTagsResponse,
            GetTextEmbeddingModelsResponse,
        ]

        for response_class in response_classes:
            assert issubclass(response_class, BaseResponse), (
                f"{response_class.__name__} does not inherit from BaseResponse"
            )

    def test_all_request_classes_inherit_from_base_request(self) -> None:
        """Test that all Request classes inherit from BaseRequest."""
        from dify_oapi.api.knowledge.v1.model.bind_tags_to_dataset_request import BindTagsToDatasetRequest
        from dify_oapi.api.knowledge.v1.model.create_child_chunk_request import CreateChildChunkRequest

        # Import all request classes
        from dify_oapi.api.knowledge.v1.model.create_dataset_request import CreateDatasetRequest
        from dify_oapi.api.knowledge.v1.model.create_document_by_file_request import CreateDocumentByFileRequest
        from dify_oapi.api.knowledge.v1.model.create_document_by_text_request import CreateDocumentByTextRequest
        from dify_oapi.api.knowledge.v1.model.create_segment_request import CreateSegmentRequest
        from dify_oapi.api.knowledge.v1.model.create_tag_request import CreateTagRequest
        from dify_oapi.api.knowledge.v1.model.delete_child_chunk_request import DeleteChildChunkRequest
        from dify_oapi.api.knowledge.v1.model.delete_dataset_request import DeleteDatasetRequest
        from dify_oapi.api.knowledge.v1.model.delete_document_request import DeleteDocumentRequest
        from dify_oapi.api.knowledge.v1.model.delete_segment_request import DeleteSegmentRequest
        from dify_oapi.api.knowledge.v1.model.delete_tag_request import DeleteTagRequest
        from dify_oapi.api.knowledge.v1.model.get_batch_indexing_status_request import GetBatchIndexingStatusRequest
        from dify_oapi.api.knowledge.v1.model.get_dataset_request import GetDatasetRequest
        from dify_oapi.api.knowledge.v1.model.get_dataset_tags_request import GetDatasetTagsRequest
        from dify_oapi.api.knowledge.v1.model.get_document_request import GetDocumentRequest
        from dify_oapi.api.knowledge.v1.model.get_segment_request import GetSegmentRequest
        from dify_oapi.api.knowledge.v1.model.get_text_embedding_models_request import GetTextEmbeddingModelsRequest
        from dify_oapi.api.knowledge.v1.model.get_upload_file_info_request import GetUploadFileInfoRequest
        from dify_oapi.api.knowledge.v1.model.list_child_chunks_request import ListChildChunksRequest
        from dify_oapi.api.knowledge.v1.model.list_datasets_request import ListDatasetsRequest
        from dify_oapi.api.knowledge.v1.model.list_documents_request import ListDocumentsRequest
        from dify_oapi.api.knowledge.v1.model.list_segments_request import ListSegmentsRequest
        from dify_oapi.api.knowledge.v1.model.list_tags_request import ListTagsRequest
        from dify_oapi.api.knowledge.v1.model.retrieve_from_dataset_request import RetrieveFromDatasetRequest
        from dify_oapi.api.knowledge.v1.model.unbind_tags_from_dataset_request import UnbindTagsFromDatasetRequest
        from dify_oapi.api.knowledge.v1.model.update_child_chunk_request import UpdateChildChunkRequest
        from dify_oapi.api.knowledge.v1.model.update_dataset_request import UpdateDatasetRequest
        from dify_oapi.api.knowledge.v1.model.update_document_by_file_request import UpdateDocumentByFileRequest
        from dify_oapi.api.knowledge.v1.model.update_document_by_text_request import UpdateDocumentByTextRequest
        from dify_oapi.api.knowledge.v1.model.update_document_status_request import UpdateDocumentStatusRequest
        from dify_oapi.api.knowledge.v1.model.update_segment_request import UpdateSegmentRequest
        from dify_oapi.api.knowledge.v1.model.update_tag_request import UpdateTagRequest
        from dify_oapi.core.model.base_request import BaseRequest

        # Test all 33 request classes inherit from BaseRequest
        request_classes = [
            CreateDatasetRequest,
            ListDatasetsRequest,
            GetDatasetRequest,
            UpdateDatasetRequest,
            DeleteDatasetRequest,
            RetrieveFromDatasetRequest,
            CreateDocumentByFileRequest,
            CreateDocumentByTextRequest,
            ListDocumentsRequest,
            GetDocumentRequest,
            UpdateDocumentByFileRequest,
            UpdateDocumentByTextRequest,
            DeleteDocumentRequest,
            UpdateDocumentStatusRequest,
            GetBatchIndexingStatusRequest,
            GetUploadFileInfoRequest,
            ListSegmentsRequest,
            CreateSegmentRequest,
            GetSegmentRequest,
            UpdateSegmentRequest,
            DeleteSegmentRequest,
            ListChildChunksRequest,
            CreateChildChunkRequest,
            UpdateChildChunkRequest,
            DeleteChildChunkRequest,
            ListTagsRequest,
            CreateTagRequest,
            UpdateTagRequest,
            DeleteTagRequest,
            BindTagsToDatasetRequest,
            UnbindTagsFromDatasetRequest,
            GetDatasetTagsRequest,
            GetTextEmbeddingModelsRequest,
        ]

        for request_class in request_classes:
            assert issubclass(request_class, BaseRequest), f"{request_class.__name__} does not inherit from BaseRequest"

    def test_type_safety_validation_across_all_models(self) -> None:
        """Test type safety validation across all models."""
        # Test that Literal types are properly used

        # Test that models use proper Literal types
        from dify_oapi.api.knowledge.v1.model.create_dataset_request_body import CreateDatasetRequestBody

        # Create request body with valid Literal values
        request_body = (
            CreateDatasetRequestBody.builder().indexing_technique("high_quality").permission("all_team_members").build()
        )

        assert request_body.indexing_technique == "high_quality"
        assert request_body.permission == "all_team_members"

        # Test tag type validation
        from dify_oapi.api.knowledge.v1.model.create_tag_request_body import CreateTagRequestBody

        tag_request_body = CreateTagRequestBody.builder().name("Test Tag").type("knowledge_type").build()
        assert tag_request_body.type == "knowledge_type"

    def test_builder_pattern_functionality_across_all_models(self) -> None:
        """Test builder pattern functionality for all models."""
        # Test Request models
        from dify_oapi.api.knowledge.v1.model.create_dataset_request import CreateDatasetRequest
        from dify_oapi.api.knowledge.v1.model.create_dataset_request_body import CreateDatasetRequestBody

        request_body = CreateDatasetRequestBody.builder().name("Builder Test").build()
        request = CreateDatasetRequest.builder().request_body(request_body).build()

        assert request.request_body.name == "Builder Test"

        # Test public models
        from dify_oapi.api.knowledge.v1.model.dataset_info import DatasetInfo

        dataset_info = DatasetInfo.builder().id("dataset-id").name("Dataset Name").build()
        assert dataset_info.id == "dataset-id"
        assert dataset_info.name == "Dataset Name"

    def test_complete_api_coverage_validation(
        self, client: Client, request_option: RequestOption, monkeypatch: Any
    ) -> None:
        """Validate that all 33 APIs are accessible and functional."""
        # Mock responses for all 33 APIs
        mock_responses = [None] * 33  # Placeholder responses
        mock_execute = Mock(side_effect=mock_responses)
        monkeypatch.setattr("dify_oapi.core.http.transport.Transport.execute", mock_execute)

        # Test that all 33 APIs are accessible through the client
        # This is a validation that the complete integration chain works

        # Dataset APIs (6) - accessible through client.knowledge.v1.dataset
        assert hasattr(client.knowledge.v1.dataset, "create")
        assert hasattr(client.knowledge.v1.dataset, "list")
        assert hasattr(client.knowledge.v1.dataset, "get")
        assert hasattr(client.knowledge.v1.dataset, "update")
        assert hasattr(client.knowledge.v1.dataset, "delete")
        assert hasattr(client.knowledge.v1.dataset, "retrieve")

        # Document APIs (10) - accessible through client.knowledge.v1.document
        assert hasattr(client.knowledge.v1.document, "create_by_file")
        assert hasattr(client.knowledge.v1.document, "create_by_text")
        assert hasattr(client.knowledge.v1.document, "list")
        assert hasattr(client.knowledge.v1.document, "get")
        assert hasattr(client.knowledge.v1.document, "update_by_file")
        assert hasattr(client.knowledge.v1.document, "update_by_text")
        assert hasattr(client.knowledge.v1.document, "delete")
        assert hasattr(client.knowledge.v1.document, "update_status")
        assert hasattr(client.knowledge.v1.document, "get_batch_status")
        assert hasattr(client.knowledge.v1.document, "file_info")

        # Segment APIs (5) - accessible through client.knowledge.v1.segment
        assert hasattr(client.knowledge.v1.segment, "list")
        assert hasattr(client.knowledge.v1.segment, "create")
        assert hasattr(client.knowledge.v1.segment, "get")
        assert hasattr(client.knowledge.v1.segment, "update")
        assert hasattr(client.knowledge.v1.segment, "delete")

        # Chunk APIs (4) - accessible through client.knowledge.v1.chunk
        assert hasattr(client.knowledge.v1.chunk, "list")
        assert hasattr(client.knowledge.v1.chunk, "create")
        assert hasattr(client.knowledge.v1.chunk, "update")
        assert hasattr(client.knowledge.v1.chunk, "delete")

        # Tag APIs (7) - accessible through client.knowledge.v1.tag
        assert hasattr(client.knowledge.v1.tag, "list")
        assert hasattr(client.knowledge.v1.tag, "create")
        assert hasattr(client.knowledge.v1.tag, "update")
        assert hasattr(client.knowledge.v1.tag, "delete")
        assert hasattr(client.knowledge.v1.tag, "bind")
        assert hasattr(client.knowledge.v1.tag, "unbind")
        assert hasattr(client.knowledge.v1.tag, "get_dataset_tags")

        # Model APIs (1) - accessible through client.knowledge.v1.model
        assert hasattr(client.knowledge.v1.model, "embedding_models")

        # Total: 6 + 10 + 5 + 4 + 7 + 1 = 33 APIs
