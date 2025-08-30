"""
Comprehensive integration tests for all 33 Knowledge Base APIs.

This module tests all APIs across the 6 knowledge resources:
- Dataset Resource: 6 APIs
- Document Resource: 10 APIs
- Segment Resource: 5 APIs
- Child Chunks Resource: 4 APIs
- Tag Resource: 7 APIs
- Model Resource: 1 API
"""

from typing import Any
from unittest.mock import AsyncMock, Mock

import pytest

from dify_oapi.api.knowledge.v1.model.bind_tags_to_dataset_request import BindTagsToDatasetRequest
from dify_oapi.api.knowledge.v1.model.bind_tags_to_dataset_request_body import BindTagsToDatasetRequestBody
from dify_oapi.api.knowledge.v1.model.bind_tags_to_dataset_response import BindTagsToDatasetResponse
from dify_oapi.api.knowledge.v1.model.create_child_chunk_request import CreateChildChunkRequest
from dify_oapi.api.knowledge.v1.model.create_child_chunk_request_body import CreateChildChunkRequestBody
from dify_oapi.api.knowledge.v1.model.create_child_chunk_response import CreateChildChunkResponse
from dify_oapi.api.knowledge.v1.model.create_dataset_request import CreateDatasetRequest
from dify_oapi.api.knowledge.v1.model.create_dataset_request_body import CreateDatasetRequestBody
from dify_oapi.api.knowledge.v1.model.create_dataset_response import CreateDatasetResponse
from dify_oapi.api.knowledge.v1.model.create_document_by_file_request import CreateDocumentByFileRequest
from dify_oapi.api.knowledge.v1.model.create_document_by_file_request_body import CreateDocumentByFileRequestBody
from dify_oapi.api.knowledge.v1.model.create_document_by_file_response import CreateDocumentByFileResponse
from dify_oapi.api.knowledge.v1.model.create_document_by_text_request import CreateDocumentByTextRequest
from dify_oapi.api.knowledge.v1.model.create_document_by_text_request_body import CreateDocumentByTextRequestBody
from dify_oapi.api.knowledge.v1.model.create_document_by_text_response import CreateDocumentByTextResponse
from dify_oapi.api.knowledge.v1.model.create_segment_request import CreateSegmentRequest
from dify_oapi.api.knowledge.v1.model.create_segment_request_body import CreateSegmentRequestBody
from dify_oapi.api.knowledge.v1.model.create_segment_response import CreateSegmentResponse
from dify_oapi.api.knowledge.v1.model.create_tag_request import CreateTagRequest
from dify_oapi.api.knowledge.v1.model.create_tag_request_body import CreateTagRequestBody
from dify_oapi.api.knowledge.v1.model.create_tag_response import CreateTagResponse
from dify_oapi.api.knowledge.v1.model.delete_child_chunk_request import DeleteChildChunkRequest
from dify_oapi.api.knowledge.v1.model.delete_child_chunk_response import DeleteChildChunkResponse
from dify_oapi.api.knowledge.v1.model.delete_dataset_request import DeleteDatasetRequest
from dify_oapi.api.knowledge.v1.model.delete_dataset_response import DeleteDatasetResponse
from dify_oapi.api.knowledge.v1.model.delete_document_request import DeleteDocumentRequest
from dify_oapi.api.knowledge.v1.model.delete_document_response import DeleteDocumentResponse
from dify_oapi.api.knowledge.v1.model.delete_segment_request import DeleteSegmentRequest
from dify_oapi.api.knowledge.v1.model.delete_segment_response import DeleteSegmentResponse
from dify_oapi.api.knowledge.v1.model.delete_tag_request import DeleteTagRequest
from dify_oapi.api.knowledge.v1.model.delete_tag_request_body import DeleteTagRequestBody
from dify_oapi.api.knowledge.v1.model.delete_tag_response import DeleteTagResponse
from dify_oapi.api.knowledge.v1.model.get_batch_indexing_status_request import GetBatchIndexingStatusRequest
from dify_oapi.api.knowledge.v1.model.get_batch_indexing_status_response import GetBatchIndexingStatusResponse
from dify_oapi.api.knowledge.v1.model.get_dataset_request import GetDatasetRequest
from dify_oapi.api.knowledge.v1.model.get_dataset_response import GetDatasetResponse
from dify_oapi.api.knowledge.v1.model.get_dataset_tags_request import GetDatasetTagsRequest
from dify_oapi.api.knowledge.v1.model.get_dataset_tags_response import GetDatasetTagsResponse
from dify_oapi.api.knowledge.v1.model.get_document_request import GetDocumentRequest
from dify_oapi.api.knowledge.v1.model.get_document_response import GetDocumentResponse
from dify_oapi.api.knowledge.v1.model.get_segment_request import GetSegmentRequest
from dify_oapi.api.knowledge.v1.model.get_segment_response import GetSegmentResponse
from dify_oapi.api.knowledge.v1.model.get_text_embedding_models_request import GetTextEmbeddingModelsRequest
from dify_oapi.api.knowledge.v1.model.get_text_embedding_models_response import GetTextEmbeddingModelsResponse
from dify_oapi.api.knowledge.v1.model.get_upload_file_info_request import GetUploadFileInfoRequest
from dify_oapi.api.knowledge.v1.model.get_upload_file_info_response import GetUploadFileInfoResponse
from dify_oapi.api.knowledge.v1.model.list_child_chunks_request import ListChildChunksRequest
from dify_oapi.api.knowledge.v1.model.list_child_chunks_response import ListChildChunksResponse
from dify_oapi.api.knowledge.v1.model.list_datasets_request import ListDatasetsRequest
from dify_oapi.api.knowledge.v1.model.list_datasets_response import ListDatasetsResponse
from dify_oapi.api.knowledge.v1.model.list_documents_request import ListDocumentsRequest
from dify_oapi.api.knowledge.v1.model.list_documents_response import ListDocumentsResponse
from dify_oapi.api.knowledge.v1.model.list_segments_request import ListSegmentsRequest
from dify_oapi.api.knowledge.v1.model.list_segments_response import ListSegmentsResponse
from dify_oapi.api.knowledge.v1.model.list_tags_request import ListTagsRequest
from dify_oapi.api.knowledge.v1.model.list_tags_response import ListTagsResponse
from dify_oapi.api.knowledge.v1.model.retrieve_from_dataset_request import RetrieveFromDatasetRequest
from dify_oapi.api.knowledge.v1.model.retrieve_from_dataset_request_body import RetrieveFromDatasetRequestBody
from dify_oapi.api.knowledge.v1.model.retrieve_from_dataset_response import RetrieveFromDatasetResponse
from dify_oapi.api.knowledge.v1.model.unbind_tags_from_dataset_request import UnbindTagsFromDatasetRequest
from dify_oapi.api.knowledge.v1.model.unbind_tags_from_dataset_request_body import UnbindTagsFromDatasetRequestBody
from dify_oapi.api.knowledge.v1.model.unbind_tags_from_dataset_response import UnbindTagsFromDatasetResponse
from dify_oapi.api.knowledge.v1.model.update_child_chunk_request import UpdateChildChunkRequest
from dify_oapi.api.knowledge.v1.model.update_child_chunk_request_body import UpdateChildChunkRequestBody
from dify_oapi.api.knowledge.v1.model.update_child_chunk_response import UpdateChildChunkResponse
from dify_oapi.api.knowledge.v1.model.update_dataset_request import UpdateDatasetRequest
from dify_oapi.api.knowledge.v1.model.update_dataset_request_body import UpdateDatasetRequestBody
from dify_oapi.api.knowledge.v1.model.update_dataset_response import UpdateDatasetResponse
from dify_oapi.api.knowledge.v1.model.update_document_by_file_request import UpdateDocumentByFileRequest
from dify_oapi.api.knowledge.v1.model.update_document_by_file_request_body import UpdateDocumentByFileRequestBody
from dify_oapi.api.knowledge.v1.model.update_document_by_file_response import UpdateDocumentByFileResponse
from dify_oapi.api.knowledge.v1.model.update_document_by_text_request import UpdateDocumentByTextRequest
from dify_oapi.api.knowledge.v1.model.update_document_by_text_request_body import UpdateDocumentByTextRequestBody
from dify_oapi.api.knowledge.v1.model.update_document_by_text_response import UpdateDocumentByTextResponse
from dify_oapi.api.knowledge.v1.model.update_document_status_request import UpdateDocumentStatusRequest
from dify_oapi.api.knowledge.v1.model.update_document_status_request_body import UpdateDocumentStatusRequestBody
from dify_oapi.api.knowledge.v1.model.update_document_status_response import UpdateDocumentStatusResponse
from dify_oapi.api.knowledge.v1.model.update_segment_request import UpdateSegmentRequest
from dify_oapi.api.knowledge.v1.model.update_segment_request_body import UpdateSegmentRequestBody
from dify_oapi.api.knowledge.v1.model.update_segment_response import UpdateSegmentResponse
from dify_oapi.api.knowledge.v1.model.update_tag_request import UpdateTagRequest
from dify_oapi.api.knowledge.v1.model.update_tag_request_body import UpdateTagRequestBody
from dify_oapi.api.knowledge.v1.model.update_tag_response import UpdateTagResponse
from dify_oapi.api.knowledge.v1.resource.chunk import Chunk
from dify_oapi.api.knowledge.v1.resource.dataset import Dataset
from dify_oapi.api.knowledge.v1.resource.document import Document
from dify_oapi.api.knowledge.v1.resource.model import Model
from dify_oapi.api.knowledge.v1.resource.segment import Segment
from dify_oapi.api.knowledge.v1.resource.tag import Tag
from dify_oapi.core.model.config import Config
from dify_oapi.core.model.request_option import RequestOption


class TestDatasetIntegration:
    """Test all 6 Dataset Resource APIs."""

    @pytest.fixture
    def dataset_resource(self) -> Dataset:
        return Dataset(Config())

    @pytest.fixture
    def request_option(self) -> RequestOption:
        return RequestOption.builder().api_key("test-api-key").build()

    def test_create_dataset(self, dataset_resource: Dataset, request_option: RequestOption, monkeypatch: Any) -> None:
        """Test POST /v1/datasets"""
        response = CreateDatasetResponse(id="dataset-id", name="Test Dataset")
        mock_execute = Mock(return_value=response)
        monkeypatch.setattr("dify_oapi.core.http.transport.Transport.execute", mock_execute)

        request_body = CreateDatasetRequestBody.builder().name("Test Dataset").build()
        request = CreateDatasetRequest.builder().request_body(request_body).build()
        result = dataset_resource.create(request, request_option)

        assert result.id == "dataset-id"
        assert result.name == "Test Dataset"

    def test_list_datasets(self, dataset_resource: Dataset, request_option: RequestOption, monkeypatch: Any) -> None:
        """Test GET /v1/datasets"""
        response = ListDatasetsResponse(data=[], has_more=False, limit=20, total=0, page=1)
        mock_execute = Mock(return_value=response)
        monkeypatch.setattr("dify_oapi.core.http.transport.Transport.execute", mock_execute)

        request = ListDatasetsRequest.builder().page(1).limit(20).build()
        result = dataset_resource.list(request, request_option)

        assert result.total == 0
        assert result.page == 1

    def test_get_dataset(self, dataset_resource: Dataset, request_option: RequestOption, monkeypatch: Any) -> None:
        """Test GET /v1/datasets/{dataset_id}"""
        response = GetDatasetResponse(id="dataset-id", name="Test Dataset")
        mock_execute = Mock(return_value=response)
        monkeypatch.setattr("dify_oapi.core.http.transport.Transport.execute", mock_execute)

        request = GetDatasetRequest.builder().dataset_id("dataset-id").build()
        result = dataset_resource.get(request, request_option)

        assert result.id == "dataset-id"

    def test_update_dataset(self, dataset_resource: Dataset, request_option: RequestOption, monkeypatch: Any) -> None:
        """Test PATCH /v1/datasets/{dataset_id}"""
        response = UpdateDatasetResponse(id="dataset-id", name="Updated Dataset")
        mock_execute = Mock(return_value=response)
        monkeypatch.setattr("dify_oapi.core.http.transport.Transport.execute", mock_execute)

        request_body = UpdateDatasetRequestBody.builder().name("Updated Dataset").build()
        request = UpdateDatasetRequest.builder().dataset_id("dataset-id").request_body(request_body).build()
        result = dataset_resource.update(request, request_option)

        assert result.name == "Updated Dataset"

    def test_delete_dataset(self, dataset_resource: Dataset, request_option: RequestOption, monkeypatch: Any) -> None:
        """Test DELETE /v1/datasets/{dataset_id}"""
        response = DeleteDatasetResponse(result="success")
        mock_execute = Mock(return_value=response)
        monkeypatch.setattr("dify_oapi.core.http.transport.Transport.execute", mock_execute)

        request = DeleteDatasetRequest.builder().dataset_id("dataset-id").build()
        result = dataset_resource.delete(request, request_option)

        assert result.result == "success"

    def test_retrieve_from_dataset(
        self, dataset_resource: Dataset, request_option: RequestOption, monkeypatch: Any
    ) -> None:
        """Test POST /v1/datasets/{dataset_id}/retrieve"""
        response = RetrieveFromDatasetResponse(query={"content": "test query"}, records=[])
        mock_execute = Mock(return_value=response)
        monkeypatch.setattr("dify_oapi.core.http.transport.Transport.execute", mock_execute)

        request_body = RetrieveFromDatasetRequestBody.builder().query("test query").build()
        request = RetrieveFromDatasetRequest.builder().dataset_id("dataset-id").request_body(request_body).build()
        result = dataset_resource.retrieve(request, request_option)

        assert result.query["content"] == "test query"


class TestDocumentIntegration:
    """Test all 10 Document Resource APIs."""

    @pytest.fixture
    def document_resource(self) -> Document:
        return Document(Config())

    @pytest.fixture
    def request_option(self) -> RequestOption:
        return RequestOption.builder().api_key("test-api-key").build()

    def test_create_document_by_file(
        self, document_resource: Document, request_option: RequestOption, monkeypatch: Any
    ) -> None:
        """Test POST /v1/datasets/{dataset_id}/document/create-by-file"""
        response = CreateDocumentByFileResponse(document={"id": "doc-id", "name": "test.pdf"}, batch="batch-id")
        mock_execute = Mock(return_value=response)
        monkeypatch.setattr("dify_oapi.core.http.transport.Transport.execute", mock_execute)

        from io import BytesIO

        file_content = BytesIO(b"test file content")
        request_body = CreateDocumentByFileRequestBody.builder().name("test.pdf").build()
        request = (
            CreateDocumentByFileRequest.builder()
            .dataset_id("dataset-id")
            .file(file_content, "test.pdf")
            .request_body(request_body)
            .build()
        )
        result = document_resource.create_by_file(request, request_option)

        assert result.document["id"] == "doc-id"
        assert result.batch == "batch-id"

    def test_create_document_by_text(
        self, document_resource: Document, request_option: RequestOption, monkeypatch: Any
    ) -> None:
        """Test POST /v1/datasets/{dataset_id}/document/create-by-text"""
        response = CreateDocumentByTextResponse(document={"id": "doc-id", "name": "Text Document"}, batch="batch-id")
        mock_execute = Mock(return_value=response)
        monkeypatch.setattr("dify_oapi.core.http.transport.Transport.execute", mock_execute)

        request_body = CreateDocumentByTextRequestBody.builder().name("Text Document").text("Document content").build()
        request = CreateDocumentByTextRequest.builder().dataset_id("dataset-id").request_body(request_body).build()
        result = document_resource.create_by_text(request, request_option)

        assert result.document["id"] == "doc-id"

    def test_list_documents(self, document_resource: Document, request_option: RequestOption, monkeypatch: Any) -> None:
        """Test GET /v1/datasets/{dataset_id}/documents"""
        response = ListDocumentsResponse(data=[], has_more=False, limit=20, total=0, page=1)
        mock_execute = Mock(return_value=response)
        monkeypatch.setattr("dify_oapi.core.http.transport.Transport.execute", mock_execute)

        request = ListDocumentsRequest.builder().dataset_id("dataset-id").build()
        result = document_resource.list(request, request_option)

        assert result.total == 0

    def test_get_document(self, document_resource: Document, request_option: RequestOption, monkeypatch: Any) -> None:
        """Test GET /v1/datasets/{dataset_id}/documents/{document_id}"""
        response = GetDocumentResponse(id="doc-id", name="Test Document")
        mock_execute = Mock(return_value=response)
        monkeypatch.setattr("dify_oapi.core.http.transport.Transport.execute", mock_execute)

        request = GetDocumentRequest.builder().dataset_id("dataset-id").document_id("doc-id").build()
        result = document_resource.get(request, request_option)

        assert result.id == "doc-id"

    def test_update_document_by_file(
        self, document_resource: Document, request_option: RequestOption, monkeypatch: Any
    ) -> None:
        """Test POST /v1/datasets/{dataset_id}/documents/{document_id}/update-by-file"""
        response = UpdateDocumentByFileResponse(document={"id": "doc-id", "name": "updated.pdf"}, batch="batch-id")
        mock_execute = Mock(return_value=response)
        monkeypatch.setattr("dify_oapi.core.http.transport.Transport.execute", mock_execute)

        from io import BytesIO

        file_content = BytesIO(b"updated file content")
        request_body = UpdateDocumentByFileRequestBody.builder().name("updated.pdf").build()
        request = (
            UpdateDocumentByFileRequest.builder()
            .dataset_id("dataset-id")
            .document_id("doc-id")
            .file(file_content, "updated.pdf")
            .request_body(request_body)
            .build()
        )
        result = document_resource.update_by_file(request, request_option)

        assert result.document["name"] == "updated.pdf"

    def test_update_document_by_text(
        self, document_resource: Document, request_option: RequestOption, monkeypatch: Any
    ) -> None:
        """Test POST /v1/datasets/{dataset_id}/documents/{document_id}/update-by-text"""
        response = UpdateDocumentByTextResponse(
            document={"id": "doc-id", "name": "Updated Text Document"}, batch="batch-id"
        )
        mock_execute = Mock(return_value=response)
        monkeypatch.setattr("dify_oapi.core.http.transport.Transport.execute", mock_execute)

        request_body = (
            UpdateDocumentByTextRequestBody.builder().name("Updated Text Document").text("Updated content").build()
        )
        request = (
            UpdateDocumentByTextRequest.builder()
            .dataset_id("dataset-id")
            .document_id("doc-id")
            .request_body(request_body)
            .build()
        )
        result = document_resource.update_by_text(request, request_option)

        assert result.document["name"] == "Updated Text Document"

    def test_delete_document(
        self, document_resource: Document, request_option: RequestOption, monkeypatch: Any
    ) -> None:
        """Test DELETE /v1/datasets/{dataset_id}/documents/{document_id}"""
        response = DeleteDocumentResponse(result="success")
        mock_execute = Mock(return_value=response)
        monkeypatch.setattr("dify_oapi.core.http.transport.Transport.execute", mock_execute)

        request = DeleteDocumentRequest.builder().dataset_id("dataset-id").document_id("doc-id").build()
        result = document_resource.delete(request, request_option)

        assert result.result == "success"

    def test_update_document_status(
        self, document_resource: Document, request_option: RequestOption, monkeypatch: Any
    ) -> None:
        """Test PATCH /v1/datasets/{dataset_id}/documents/status/{action}"""
        response = UpdateDocumentStatusResponse(result="success")
        mock_execute = Mock(return_value=response)
        monkeypatch.setattr("dify_oapi.core.http.transport.Transport.execute", mock_execute)

        request_body = UpdateDocumentStatusRequestBody.builder().document_ids(["doc-id"]).build()
        request = (
            UpdateDocumentStatusRequest.builder()
            .dataset_id("dataset-id")
            .action("enable")
            .request_body(request_body)
            .build()
        )
        result = document_resource.update_status(request, request_option)

        assert result.result == "success"

    def test_get_batch_indexing_status(
        self, document_resource: Document, request_option: RequestOption, monkeypatch: Any
    ) -> None:
        """Test GET /v1/datasets/{dataset_id}/documents/{batch}/indexing-status"""
        response = GetBatchIndexingStatusResponse(id="batch-id", indexing_status="completed")
        mock_execute = Mock(return_value=response)
        monkeypatch.setattr("dify_oapi.core.http.transport.Transport.execute", mock_execute)

        request = GetBatchIndexingStatusRequest.builder().dataset_id("dataset-id").batch("batch-id").build()
        result = document_resource.get_batch_status(request, request_option)

        assert result.indexing_status == "completed"

    def test_get_upload_file_info(
        self, document_resource: Document, request_option: RequestOption, monkeypatch: Any
    ) -> None:
        """Test GET /v1/datasets/{dataset_id}/documents/{document_id}/upload-file"""
        response = GetUploadFileInfoResponse(id="file-id", name="test.pdf", size=1024)
        mock_execute = Mock(return_value=response)
        monkeypatch.setattr("dify_oapi.core.http.transport.Transport.execute", mock_execute)

        request = GetUploadFileInfoRequest.builder().dataset_id("dataset-id").document_id("doc-id").build()
        result = document_resource.file_info(request, request_option)

        assert result.name == "test.pdf"


class TestSegmentIntegration:
    """Test all 5 Segment Resource APIs."""

    @pytest.fixture
    def segment_resource(self) -> Segment:
        return Segment(Config())

    @pytest.fixture
    def request_option(self) -> RequestOption:
        return RequestOption.builder().api_key("test-api-key").build()

    def test_list_segments(self, segment_resource: Segment, request_option: RequestOption, monkeypatch: Any) -> None:
        """Test GET /v1/datasets/{dataset_id}/documents/{document_id}/segments"""
        response = ListSegmentsResponse(data=[])
        mock_execute = Mock(return_value=response)
        monkeypatch.setattr("dify_oapi.core.http.transport.Transport.execute", mock_execute)

        request = ListSegmentsRequest.builder().dataset_id("dataset-id").document_id("doc-id").build()
        result = segment_resource.list(request, request_option)

        assert result.data == []

    def test_create_segment(self, segment_resource: Segment, request_option: RequestOption, monkeypatch: Any) -> None:
        """Test POST /v1/datasets/{dataset_id}/documents/{document_id}/segments"""
        response = CreateSegmentResponse(data=[{"id": "segment-id", "content": "Test segment"}])
        mock_execute = Mock(return_value=response)
        monkeypatch.setattr("dify_oapi.core.http.transport.Transport.execute", mock_execute)

        request_body = CreateSegmentRequestBody.builder().segments([{"content": "Test segment"}]).build()
        request = (
            CreateSegmentRequest.builder()
            .dataset_id("dataset-id")
            .document_id("doc-id")
            .request_body(request_body)
            .build()
        )
        result = segment_resource.create(request, request_option)

        assert result.data[0]["content"] == "Test segment"

    def test_get_segment(self, segment_resource: Segment, request_option: RequestOption, monkeypatch: Any) -> None:
        """Test GET /v1/datasets/{dataset_id}/documents/{document_id}/segments/{segment_id}"""
        response = GetSegmentResponse(id="segment-id", content="Test segment")
        mock_execute = Mock(return_value=response)
        monkeypatch.setattr("dify_oapi.core.http.transport.Transport.execute", mock_execute)

        request = (
            GetSegmentRequest.builder().dataset_id("dataset-id").document_id("doc-id").segment_id("segment-id").build()
        )
        result = segment_resource.get(request, request_option)

        assert result.id == "segment-id"

    def test_update_segment(self, segment_resource: Segment, request_option: RequestOption, monkeypatch: Any) -> None:
        """Test POST /v1/datasets/{dataset_id}/documents/{document_id}/segments/{segment_id}"""
        response = UpdateSegmentResponse(id="segment-id", content="Updated segment")
        mock_execute = Mock(return_value=response)
        monkeypatch.setattr("dify_oapi.core.http.transport.Transport.execute", mock_execute)

        request_body = UpdateSegmentRequestBody.builder().segment({"content": "Updated segment"}).build()
        request = (
            UpdateSegmentRequest.builder()
            .dataset_id("dataset-id")
            .document_id("doc-id")
            .segment_id("segment-id")
            .request_body(request_body)
            .build()
        )
        result = segment_resource.update(request, request_option)

        assert result.content == "Updated segment"

    def test_delete_segment(self, segment_resource: Segment, request_option: RequestOption, monkeypatch: Any) -> None:
        """Test DELETE /v1/datasets/{dataset_id}/documents/{document_id}/segments/{segment_id}"""
        response = DeleteSegmentResponse(result="success")
        mock_execute = Mock(return_value=response)
        monkeypatch.setattr("dify_oapi.core.http.transport.Transport.execute", mock_execute)

        request = (
            DeleteSegmentRequest.builder()
            .dataset_id("dataset-id")
            .document_id("doc-id")
            .segment_id("segment-id")
            .build()
        )
        result = segment_resource.delete(request, request_option)

        assert result.result == "success"


class TestChunkIntegration:
    """Test all 4 Child Chunks Resource APIs."""

    @pytest.fixture
    def chunk_resource(self) -> Chunk:
        return Chunk(Config())

    @pytest.fixture
    def request_option(self) -> RequestOption:
        return RequestOption.builder().api_key("test-api-key").build()

    def test_list_child_chunks(self, chunk_resource: Chunk, request_option: RequestOption, monkeypatch: Any) -> None:
        """Test GET /v1/datasets/{dataset_id}/documents/{document_id}/segments/{segment_id}/child_chunks"""
        response = ListChildChunksResponse(data=[])
        mock_execute = Mock(return_value=response)
        monkeypatch.setattr("dify_oapi.core.http.transport.Transport.execute", mock_execute)

        request = (
            ListChildChunksRequest.builder()
            .dataset_id("dataset-id")
            .document_id("doc-id")
            .segment_id("segment-id")
            .build()
        )
        result = chunk_resource.list(request, request_option)

        assert result.data == []

    def test_create_child_chunk(self, chunk_resource: Chunk, request_option: RequestOption, monkeypatch: Any) -> None:
        """Test POST /v1/datasets/{dataset_id}/documents/{document_id}/segments/{segment_id}/child_chunks"""
        response = CreateChildChunkResponse(data=[{"id": "chunk-id", "content": "Test chunk"}])
        mock_execute = Mock(return_value=response)
        monkeypatch.setattr("dify_oapi.core.http.transport.Transport.execute", mock_execute)

        request_body = CreateChildChunkRequestBody.builder().chunks([{"content": "Test chunk"}]).build()
        request = (
            CreateChildChunkRequest.builder()
            .dataset_id("dataset-id")
            .document_id("doc-id")
            .segment_id("segment-id")
            .request_body(request_body)
            .build()
        )
        result = chunk_resource.create(request, request_option)

        assert result.data[0]["content"] == "Test chunk"

    def test_update_child_chunk(self, chunk_resource: Chunk, request_option: RequestOption, monkeypatch: Any) -> None:
        """Test PATCH /v1/datasets/{dataset_id}/documents/{document_id}/segments/{segment_id}/child_chunks/{child_chunk_id}"""
        response = UpdateChildChunkResponse(id="chunk-id", content="Updated chunk")
        mock_execute = Mock(return_value=response)
        monkeypatch.setattr("dify_oapi.core.http.transport.Transport.execute", mock_execute)

        request_body = UpdateChildChunkRequestBody.builder().content("Updated chunk").build()
        request = (
            UpdateChildChunkRequest.builder()
            .dataset_id("dataset-id")
            .document_id("doc-id")
            .segment_id("segment-id")
            .child_chunk_id("chunk-id")
            .request_body(request_body)
            .build()
        )
        result = chunk_resource.update(request, request_option)

        assert result.content == "Updated chunk"

    def test_delete_child_chunk(self, chunk_resource: Chunk, request_option: RequestOption, monkeypatch: Any) -> None:
        """Test DELETE /v1/datasets/{dataset_id}/documents/{document_id}/segments/{segment_id}/child_chunks/{child_chunk_id}"""
        response = DeleteChildChunkResponse(result="success")
        mock_execute = Mock(return_value=response)
        monkeypatch.setattr("dify_oapi.core.http.transport.Transport.execute", mock_execute)

        request = (
            DeleteChildChunkRequest.builder()
            .dataset_id("dataset-id")
            .document_id("doc-id")
            .segment_id("segment-id")
            .child_chunk_id("chunk-id")
            .build()
        )
        result = chunk_resource.delete(request, request_option)

        assert result.result == "success"


class TestTagIntegration:
    """Test all 7 Tag Resource APIs."""

    @pytest.fixture
    def tag_resource(self) -> Tag:
        return Tag(Config())

    @pytest.fixture
    def request_option(self) -> RequestOption:
        return RequestOption.builder().api_key("test-api-key").build()

    def test_list_tags(self, tag_resource: Tag, request_option: RequestOption, monkeypatch: Any) -> None:
        """Test GET /v1/datasets/tags"""
        response = ListTagsResponse(data=[])
        mock_execute = Mock(return_value=response)
        monkeypatch.setattr("dify_oapi.core.http.transport.Transport.execute", mock_execute)

        request = ListTagsRequest.builder().build()
        result = tag_resource.list(request, request_option)

        assert result.data == []

    def test_create_tag(self, tag_resource: Tag, request_option: RequestOption, monkeypatch: Any) -> None:
        """Test POST /v1/datasets/tags"""
        response = CreateTagResponse(id="tag-id", name="Test Tag", type="knowledge_type", binding_count=0)
        mock_execute = Mock(return_value=response)
        monkeypatch.setattr("dify_oapi.core.http.transport.Transport.execute", mock_execute)

        request_body = CreateTagRequestBody.builder().name("Test Tag").type("knowledge_type").build()
        request = CreateTagRequest.builder().request_body(request_body).build()
        result = tag_resource.create(request, request_option)

        assert result.name == "Test Tag"

    def test_update_tag(self, tag_resource: Tag, request_option: RequestOption, monkeypatch: Any) -> None:
        """Test PATCH /v1/datasets/tags"""
        response = UpdateTagResponse(id="tag-id", name="Updated Tag", type="knowledge_type", binding_count=0)
        mock_execute = Mock(return_value=response)
        monkeypatch.setattr("dify_oapi.core.http.transport.Transport.execute", mock_execute)

        request_body = UpdateTagRequestBody.builder().tag_id("tag-id").name("Updated Tag").build()
        request = UpdateTagRequest.builder().request_body(request_body).build()
        result = tag_resource.update(request, request_option)

        assert result.name == "Updated Tag"

    def test_delete_tag(self, tag_resource: Tag, request_option: RequestOption, monkeypatch: Any) -> None:
        """Test DELETE /v1/datasets/tags"""
        response = DeleteTagResponse(result="success")
        mock_execute = Mock(return_value=response)
        monkeypatch.setattr("dify_oapi.core.http.transport.Transport.execute", mock_execute)

        request_body = DeleteTagRequestBody.builder().tag_id("tag-id").build()
        request = DeleteTagRequest.builder().request_body(request_body).build()
        result = tag_resource.delete(request, request_option)

        assert result.result == "success"

    def test_bind_tags_to_dataset(self, tag_resource: Tag, request_option: RequestOption, monkeypatch: Any) -> None:
        """Test POST /v1/datasets/tags/binding"""
        response = BindTagsToDatasetResponse(result="success")
        mock_execute = Mock(return_value=response)
        monkeypatch.setattr("dify_oapi.core.http.transport.Transport.execute", mock_execute)

        request_body = BindTagsToDatasetRequestBody.builder().dataset_id("dataset-id").tag_ids(["tag-id"]).build()
        request = BindTagsToDatasetRequest.builder().request_body(request_body).build()
        result = tag_resource.bind(request, request_option)

        assert result.result == "success"

    def test_unbind_tags_from_dataset(self, tag_resource: Tag, request_option: RequestOption, monkeypatch: Any) -> None:
        """Test POST /v1/datasets/tags/unbinding"""
        response = UnbindTagsFromDatasetResponse(result="success")
        mock_execute = Mock(return_value=response)
        monkeypatch.setattr("dify_oapi.core.http.transport.Transport.execute", mock_execute)

        request_body = UnbindTagsFromDatasetRequestBody.builder().dataset_id("dataset-id").tag_ids(["tag-id"]).build()
        request = UnbindTagsFromDatasetRequest.builder().request_body(request_body).build()
        result = tag_resource.unbind(request, request_option)

        assert result.result == "success"

    def test_get_dataset_tags(self, tag_resource: Tag, request_option: RequestOption, monkeypatch: Any) -> None:
        """Test POST /v1/datasets/{dataset_id}/tags"""
        response = GetDatasetTagsResponse(data=[])
        mock_execute = Mock(return_value=response)
        monkeypatch.setattr("dify_oapi.core.http.transport.Transport.execute", mock_execute)

        request = GetDatasetTagsRequest.builder().dataset_id("dataset-id").build()
        result = tag_resource.get_dataset_tags(request, request_option)

        assert result.data == []


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


class TestKnowledgeAPIIntegration:
    """Test complete Knowledge API integration across all resources."""

    @pytest.fixture
    def config(self) -> Config:
        return Config()

    @pytest.fixture
    def request_option(self) -> RequestOption:
        return RequestOption.builder().api_key("test-api-key").build()

    @pytest.mark.asyncio
    async def test_all_apis_async(self, config: Config, request_option: RequestOption, monkeypatch: Any) -> None:
        """Test all 33 APIs with async operations."""
        # Initialize all resources
        dataset_resource = Dataset(config)
        document_resource = Document(config)
        segment_resource = Segment(config)
        chunk_resource = Chunk(config)
        tag_resource = Tag(config)
        model_resource = Model(config)

        # Mock async responses for all 33 APIs
        responses = [
            # Dataset APIs (6)
            CreateDatasetResponse(id="dataset-id", name="Test Dataset"),
            ListDatasetsResponse(data=[], has_more=False, limit=20, total=0, page=1),
            GetDatasetResponse(id="dataset-id", name="Test Dataset"),
            UpdateDatasetResponse(id="dataset-id", name="Updated Dataset"),
            DeleteDatasetResponse(result="success"),
            RetrieveFromDatasetResponse(query={"content": "test query"}, records=[]),
            # Document APIs (10)
            CreateDocumentByFileResponse(document={"id": "doc-id"}, batch="batch-id"),
            CreateDocumentByTextResponse(document={"id": "doc-id"}, batch="batch-id"),
            ListDocumentsResponse(data=[], has_more=False, limit=20, total=0, page=1),
            GetDocumentResponse(id="doc-id", name="Test Document"),
            UpdateDocumentByFileResponse(document={"id": "doc-id"}, batch="batch-id"),
            UpdateDocumentByTextResponse(document={"id": "doc-id"}, batch="batch-id"),
            DeleteDocumentResponse(result="success"),
            UpdateDocumentStatusResponse(result="success"),
            GetBatchIndexingStatusResponse(id="batch-id", indexing_status="completed"),
            GetUploadFileInfoResponse(id="file-id", name="test.pdf", size=1024),
            # Segment APIs (5)
            ListSegmentsResponse(data=[]),
            CreateSegmentResponse(data=[{"id": "segment-id"}]),
            GetSegmentResponse(id="segment-id", content="Test segment"),
            UpdateSegmentResponse(id="segment-id", content="Updated segment"),
            DeleteSegmentResponse(result="success"),
            # Chunk APIs (4)
            ListChildChunksResponse(data=[]),
            CreateChildChunkResponse(data=[{"id": "chunk-id"}]),
            UpdateChildChunkResponse(id="chunk-id", content="Updated chunk"),
            DeleteChildChunkResponse(result="success"),
            # Tag APIs (7)
            ListTagsResponse(data=[]),
            CreateTagResponse(id="tag-id", name="Test Tag", type="knowledge_type", binding_count=0),
            UpdateTagResponse(id="tag-id", name="Updated Tag", type="knowledge_type", binding_count=0),
            DeleteTagResponse(result="success"),
            BindTagsToDatasetResponse(result="success"),
            UnbindTagsFromDatasetResponse(result="success"),
            GetDatasetTagsResponse(data=[]),
            # Model APIs (1)
            GetTextEmbeddingModelsResponse(data=[]),
        ]

        mock_aexecute = AsyncMock()
        mock_aexecute.side_effect = responses
        monkeypatch.setattr("dify_oapi.core.http.transport.ATransport.aexecute", mock_aexecute)

        # Test all Dataset APIs
        await dataset_resource.acreate(
            CreateDatasetRequest.builder()
            .request_body(CreateDatasetRequestBody.builder().name("Test Dataset").build())
            .build(),
            request_option,
        )
        await dataset_resource.alist(ListDatasetsRequest.builder().build(), request_option)
        await dataset_resource.aget(GetDatasetRequest.builder().dataset_id("dataset-id").build(), request_option)
        await dataset_resource.aupdate(
            UpdateDatasetRequest.builder()
            .dataset_id("dataset-id")
            .request_body(UpdateDatasetRequestBody.builder().name("Updated Dataset").build())
            .build(),
            request_option,
        )
        await dataset_resource.adelete(DeleteDatasetRequest.builder().dataset_id("dataset-id").build(), request_option)
        await dataset_resource.aretrieve(
            RetrieveFromDatasetRequest.builder()
            .dataset_id("dataset-id")
            .request_body(RetrieveFromDatasetRequestBody.builder().query("test query").build())
            .build(),
            request_option,
        )

        # Test all Document APIs
        from io import BytesIO

        file_content = BytesIO(b"test content")
        await document_resource.acreate_by_file(
            CreateDocumentByFileRequest.builder()
            .dataset_id("dataset-id")
            .file(file_content, "test.pdf")
            .request_body(CreateDocumentByFileRequestBody.builder().name("test.pdf").build())
            .build(),
            request_option,
        )
        await document_resource.acreate_by_text(
            CreateDocumentByTextRequest.builder()
            .dataset_id("dataset-id")
            .request_body(CreateDocumentByTextRequestBody.builder().name("Text Doc").text("content").build())
            .build(),
            request_option,
        )
        await document_resource.alist(ListDocumentsRequest.builder().dataset_id("dataset-id").build(), request_option)
        await document_resource.aget(
            GetDocumentRequest.builder().dataset_id("dataset-id").document_id("doc-id").build(), request_option
        )
        await document_resource.aupdate_by_file(
            UpdateDocumentByFileRequest.builder()
            .dataset_id("dataset-id")
            .document_id("doc-id")
            .file(file_content, "updated.pdf")
            .request_body(UpdateDocumentByFileRequestBody.builder().name("updated.pdf").build())
            .build(),
            request_option,
        )
        await document_resource.aupdate_by_text(
            UpdateDocumentByTextRequest.builder()
            .dataset_id("dataset-id")
            .document_id("doc-id")
            .request_body(
                UpdateDocumentByTextRequestBody.builder().name("Updated Text Doc").text("updated content").build()
            )
            .build(),
            request_option,
        )
        await document_resource.adelete(
            DeleteDocumentRequest.builder().dataset_id("dataset-id").document_id("doc-id").build(), request_option
        )
        await document_resource.aupdate_status(
            UpdateDocumentStatusRequest.builder()
            .dataset_id("dataset-id")
            .action("enable")
            .request_body(UpdateDocumentStatusRequestBody.builder().document_ids(["doc-id"]).build())
            .build(),
            request_option,
        )
        await document_resource.aget_batch_status(
            GetBatchIndexingStatusRequest.builder().dataset_id("dataset-id").batch("batch-id").build(), request_option
        )
        await document_resource.afile_info(
            GetUploadFileInfoRequest.builder().dataset_id("dataset-id").document_id("doc-id").build(), request_option
        )

        # Test all Segment APIs
        await segment_resource.alist(
            ListSegmentsRequest.builder().dataset_id("dataset-id").document_id("doc-id").build(), request_option
        )
        await segment_resource.acreate(
            CreateSegmentRequest.builder()
            .dataset_id("dataset-id")
            .document_id("doc-id")
            .request_body(CreateSegmentRequestBody.builder().segments([{"content": "segment"}]).build())
            .build(),
            request_option,
        )
        await segment_resource.aget(
            GetSegmentRequest.builder().dataset_id("dataset-id").document_id("doc-id").segment_id("segment-id").build(),
            request_option,
        )
        await segment_resource.aupdate(
            UpdateSegmentRequest.builder()
            .dataset_id("dataset-id")
            .document_id("doc-id")
            .segment_id("segment-id")
            .request_body(UpdateSegmentRequestBody.builder().segment({"content": "updated"}).build())
            .build(),
            request_option,
        )
        await segment_resource.adelete(
            DeleteSegmentRequest.builder()
            .dataset_id("dataset-id")
            .document_id("doc-id")
            .segment_id("segment-id")
            .build(),
            request_option,
        )

        # Test all Chunk APIs
        await chunk_resource.alist(
            ListChildChunksRequest.builder()
            .dataset_id("dataset-id")
            .document_id("doc-id")
            .segment_id("segment-id")
            .build(),
            request_option,
        )
        await chunk_resource.acreate(
            CreateChildChunkRequest.builder()
            .dataset_id("dataset-id")
            .document_id("doc-id")
            .segment_id("segment-id")
            .request_body(CreateChildChunkRequestBody.builder().chunks([{"content": "chunk"}]).build())
            .build(),
            request_option,
        )
        await chunk_resource.aupdate(
            UpdateChildChunkRequest.builder()
            .dataset_id("dataset-id")
            .document_id("doc-id")
            .segment_id("segment-id")
            .child_chunk_id("chunk-id")
            .request_body(UpdateChildChunkRequestBody.builder().content("updated chunk").build())
            .build(),
            request_option,
        )
        await chunk_resource.adelete(
            DeleteChildChunkRequest.builder()
            .dataset_id("dataset-id")
            .document_id("doc-id")
            .segment_id("segment-id")
            .child_chunk_id("chunk-id")
            .build(),
            request_option,
        )

        # Test all Tag APIs
        await tag_resource.alist(ListTagsRequest.builder().build(), request_option)
        await tag_resource.acreate(
            CreateTagRequest.builder()
            .request_body(CreateTagRequestBody.builder().name("Test Tag").type("knowledge_type").build())
            .build(),
            request_option,
        )
        await tag_resource.aupdate(
            UpdateTagRequest.builder()
            .request_body(UpdateTagRequestBody.builder().tag_id("tag-id").name("Updated Tag").build())
            .build(),
            request_option,
        )
        await tag_resource.adelete(
            DeleteTagRequest.builder().request_body(DeleteTagRequestBody.builder().tag_id("tag-id").build()).build(),
            request_option,
        )
        await tag_resource.abind(
            BindTagsToDatasetRequest.builder()
            .request_body(BindTagsToDatasetRequestBody.builder().dataset_id("dataset-id").tag_ids(["tag-id"]).build())
            .build(),
            request_option,
        )
        await tag_resource.aunbind(
            UnbindTagsFromDatasetRequest.builder()
            .request_body(
                UnbindTagsFromDatasetRequestBody.builder().dataset_id("dataset-id").tag_ids(["tag-id"]).build()
            )
            .build(),
            request_option,
        )
        await tag_resource.aget_dataset_tags(
            GetDatasetTagsRequest.builder().dataset_id("dataset-id").build(), request_option
        )

        # Test Model API
        await model_resource.aembedding_models(GetTextEmbeddingModelsRequest.builder().build(), request_option)

        # Verify all 33 APIs were called
        assert mock_aexecute.call_count == 33

    def test_error_handling_across_all_resources(
        self, config: Config, request_option: RequestOption, monkeypatch: Any
    ) -> None:
        """Test error handling across all 6 resources."""
        # Initialize all resources
        dataset_resource = Dataset(config)
        document_resource = Document(config)
        segment_resource = Segment(config)
        chunk_resource = Chunk(config)
        tag_resource = Tag(config)
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
            document_resource.list(ListDocumentsRequest.builder().dataset_id("dataset-id").build(), request_option)

        with pytest.raises(Exception, match="API Error"):
            segment_resource.get(
                GetSegmentRequest.builder()
                .dataset_id("dataset-id")
                .document_id("doc-id")
                .segment_id("segment-id")
                .build(),
                request_option,
            )

        with pytest.raises(Exception, match="API Error"):
            chunk_resource.delete(
                DeleteChildChunkRequest.builder()
                .dataset_id("dataset-id")
                .document_id("doc-id")
                .segment_id("segment-id")
                .child_chunk_id("chunk-id")
                .build(),
                request_option,
            )

        with pytest.raises(Exception, match="API Error"):
            tag_resource.create(
                CreateTagRequest.builder()
                .request_body(CreateTagRequestBody.builder().name("Test Tag").type("knowledge_type").build())
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
