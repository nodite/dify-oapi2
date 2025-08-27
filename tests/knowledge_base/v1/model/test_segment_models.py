"""Unit tests for segment API models."""

from __future__ import annotations

from dify_oapi.api.knowledge_base.v1.model.segment.create_child_chunk_request import CreateChildChunkRequest
from dify_oapi.api.knowledge_base.v1.model.segment.create_child_chunk_request_body import CreateChildChunkRequestBody
from dify_oapi.api.knowledge_base.v1.model.segment.create_child_chunk_response import CreateChildChunkResponse
from dify_oapi.api.knowledge_base.v1.model.segment.create_request import CreateRequest
from dify_oapi.api.knowledge_base.v1.model.segment.create_request_body import CreateRequestBody
from dify_oapi.api.knowledge_base.v1.model.segment.create_response import CreateResponse
from dify_oapi.api.knowledge_base.v1.model.segment.delete_child_chunk_request import DeleteChildChunkRequest
from dify_oapi.api.knowledge_base.v1.model.segment.delete_child_chunk_response import DeleteChildChunkResponse
from dify_oapi.api.knowledge_base.v1.model.segment.delete_request import DeleteRequest
from dify_oapi.api.knowledge_base.v1.model.segment.delete_response import DeleteResponse
from dify_oapi.api.knowledge_base.v1.model.segment.get_request import GetRequest
from dify_oapi.api.knowledge_base.v1.model.segment.get_response import GetResponse
from dify_oapi.api.knowledge_base.v1.model.segment.list_child_chunks_request import ListChildChunksRequest
from dify_oapi.api.knowledge_base.v1.model.segment.list_child_chunks_response import ListChildChunksResponse
from dify_oapi.api.knowledge_base.v1.model.segment.list_request import ListRequest
from dify_oapi.api.knowledge_base.v1.model.segment.list_response import ListResponse
from dify_oapi.api.knowledge_base.v1.model.segment.segment_data import SegmentData
from dify_oapi.api.knowledge_base.v1.model.segment.segment_info import SegmentInfo
from dify_oapi.api.knowledge_base.v1.model.segment.update_child_chunk_request import UpdateChildChunkRequest
from dify_oapi.api.knowledge_base.v1.model.segment.update_child_chunk_request_body import UpdateChildChunkRequestBody
from dify_oapi.api.knowledge_base.v1.model.segment.update_child_chunk_response import UpdateChildChunkResponse
from dify_oapi.api.knowledge_base.v1.model.segment.update_request import UpdateRequest
from dify_oapi.api.knowledge_base.v1.model.segment.update_request_body import UpdateRequestBody
from dify_oapi.api.knowledge_base.v1.model.segment.update_response import UpdateResponse
from dify_oapi.core.enum import HttpMethod
from dify_oapi.core.model.base_response import BaseResponse


class TestCreateModels:
    """Test Create API models."""

    def test_request_builder(self) -> None:
        """Test CreateRequest builder pattern."""
        request = CreateRequest.builder().dataset_id("dataset-123").document_id("doc-456").build()
        assert request.dataset_id == "dataset-123"
        assert request.document_id == "doc-456"
        assert request.paths["dataset_id"] == "dataset-123"
        assert request.paths["document_id"] == "doc-456"

    def test_request_validation(self) -> None:
        """Test CreateRequest validation."""
        request = CreateRequest.builder().build()
        assert request.http_method == HttpMethod.POST
        assert request.uri == "/v1/datasets/:dataset_id/documents/:document_id/segments"

    def test_request_body_builder(self) -> None:
        """Test CreateRequestBody builder pattern."""
        segment = SegmentInfo.builder().content("Test content").build()
        request_body = CreateRequestBody.builder().segments([segment]).build()
        assert request_body.segments is not None
        assert len(request_body.segments) == 1
        assert request_body.segments[0].content == "Test content"

    def test_request_body_validation(self) -> None:
        """Test CreateRequestBody validation."""
        segment = SegmentInfo(content="Test content")
        request_body = CreateRequestBody(segments=[segment])
        assert request_body.segments is not None
        assert len(request_body.segments) == 1

    def test_response_inheritance(self) -> None:
        """Test CreateResponse inherits from BaseResponse."""
        response = CreateResponse()
        assert isinstance(response, BaseResponse)
        assert hasattr(response, "success")
        assert hasattr(response, "code")
        assert hasattr(response, "msg")
        assert hasattr(response, "raw")

    def test_response_data_access(self) -> None:
        """Test CreateResponse data access."""
        response = CreateResponse()
        assert isinstance(response, CreateResponse)


class TestListModels:
    """Test List API models."""

    def test_request_builder(self) -> None:
        """Test ListRequest builder pattern."""
        request = (
            ListRequest.builder()
            .dataset_id("dataset-123")
            .document_id("doc-456")
            .keyword("test")
            .status("completed")
            .page(1)
            .limit(20)
            .build()
        )
        assert request.dataset_id == "dataset-123"
        assert request.document_id == "doc-456"
        assert request.paths["dataset_id"] == "dataset-123"
        assert request.paths["document_id"] == "doc-456"

    def test_request_validation(self) -> None:
        """Test ListRequest validation."""
        request = ListRequest.builder().build()
        assert request.http_method == HttpMethod.GET
        assert request.uri == "/v1/datasets/:dataset_id/documents/:document_id/segments"

    def test_response_inheritance(self) -> None:
        """Test ListResponse inherits from BaseResponse."""
        response = ListResponse()
        assert isinstance(response, BaseResponse)
        assert hasattr(response, "success")
        assert hasattr(response, "code")
        assert hasattr(response, "msg")
        assert hasattr(response, "raw")

    def test_response_data_access(self) -> None:
        """Test ListResponse data access."""
        response = ListResponse(data=[], has_more=False)
        assert response.data == []
        assert response.has_more is False


class TestGetModels:
    """Test Get API models."""

    def test_request_builder(self) -> None:
        """Test GetRequest builder pattern."""
        request = GetRequest.builder().dataset_id("dataset-123").document_id("doc-456").segment_id("seg-789").build()
        assert request.dataset_id == "dataset-123"
        assert request.document_id == "doc-456"
        assert request.segment_id == "seg-789"
        assert request.paths["dataset_id"] == "dataset-123"
        assert request.paths["document_id"] == "doc-456"
        assert request.paths["segment_id"] == "seg-789"

    def test_request_validation(self) -> None:
        """Test GetRequest validation."""
        request = GetRequest.builder().build()
        assert request.http_method == HttpMethod.GET
        assert request.uri == "/v1/datasets/:dataset_id/documents/:document_id/segments/:segment_id"

    def test_response_inheritance(self) -> None:
        """Test GetResponse inherits from BaseResponse."""
        response = GetResponse()
        assert isinstance(response, BaseResponse)
        assert hasattr(response, "success")
        assert hasattr(response, "code")
        assert hasattr(response, "msg")
        assert hasattr(response, "raw")

    def test_response_data_access(self) -> None:
        """Test GetResponse data access."""
        response = GetResponse(data=None)
        assert response.data is None


class TestUpdateModels:
    """Test Update API models."""

    def test_request_builder(self) -> None:
        """Test UpdateRequest builder pattern."""
        segment_data = SegmentData.builder().content("Updated content").build()
        request_body = UpdateRequestBody.builder().segment(segment_data).build()
        request = (
            UpdateRequest.builder()
            .dataset_id("dataset-123")
            .document_id("doc-456")
            .segment_id("seg-789")
            .request_body(request_body)
            .build()
        )
        assert request.dataset_id == "dataset-123"
        assert request.document_id == "doc-456"
        assert request.segment_id == "seg-789"
        assert request.request_body is not None

    def test_request_validation(self) -> None:
        """Test UpdateRequest validation."""
        request = UpdateRequest.builder().build()
        assert request.http_method == HttpMethod.POST
        assert request.uri == "/v1/datasets/:dataset_id/documents/:document_id/segments/:segment_id"

    def test_request_body_builder(self) -> None:
        """Test UpdateRequestBody builder pattern."""
        segment_data = SegmentData.builder().content("Updated content").build()
        request_body = UpdateRequestBody.builder().segment(segment_data).build()
        assert request_body.segment is not None
        assert request_body.segment.content == "Updated content"

    def test_request_body_validation(self) -> None:
        """Test UpdateRequestBody validation."""
        segment_data = SegmentData(content="Updated content")
        request_body = UpdateRequestBody(segment=segment_data)
        assert request_body.segment is not None

    def test_response_inheritance(self) -> None:
        """Test UpdateResponse inherits from BaseResponse."""
        response = UpdateResponse()
        assert isinstance(response, BaseResponse)
        assert hasattr(response, "success")
        assert hasattr(response, "code")
        assert hasattr(response, "msg")
        assert hasattr(response, "raw")

    def test_response_data_access(self) -> None:
        """Test UpdateResponse data access."""
        response = UpdateResponse(data=None)
        assert response.data is None


class TestDeleteModels:
    """Test Delete API models."""

    def test_request_builder(self) -> None:
        """Test DeleteRequest builder pattern."""
        request = DeleteRequest.builder().dataset_id("dataset-123").document_id("doc-456").segment_id("seg-789").build()
        assert request.dataset_id == "dataset-123"
        assert request.document_id == "doc-456"
        assert request.segment_id == "seg-789"
        assert request.paths["dataset_id"] == "dataset-123"
        assert request.paths["document_id"] == "doc-456"
        assert request.paths["segment_id"] == "seg-789"

    def test_request_validation(self) -> None:
        """Test DeleteRequest validation."""
        request = DeleteRequest.builder().build()
        assert request.http_method == HttpMethod.DELETE
        assert request.uri == "/v1/datasets/:dataset_id/documents/:document_id/segments/:segment_id"

    def test_response_inheritance(self) -> None:
        """Test DeleteResponse inherits from BaseResponse."""
        response = DeleteResponse()
        assert isinstance(response, BaseResponse)
        assert hasattr(response, "success")
        assert hasattr(response, "code")
        assert hasattr(response, "msg")
        assert hasattr(response, "raw")

    def test_response_data_access(self) -> None:
        """Test DeleteResponse data access."""
        response = DeleteResponse()
        assert isinstance(response, DeleteResponse)


class TestCreateChildChunkModels:
    """Test CreateChildChunk API models."""

    def test_request_builder(self) -> None:
        """Test CreateChildChunkRequest builder pattern."""
        request = (
            CreateChildChunkRequest.builder()
            .dataset_id("dataset-123")
            .document_id("doc-456")
            .segment_id("seg-789")
            .build()
        )
        assert request.dataset_id == "dataset-123"
        assert request.document_id == "doc-456"
        assert request.segment_id == "seg-789"
        assert request.paths["dataset_id"] == "dataset-123"
        assert request.paths["document_id"] == "doc-456"
        assert request.paths["segment_id"] == "seg-789"

    def test_request_validation(self) -> None:
        """Test CreateChildChunkRequest validation."""
        request = CreateChildChunkRequest.builder().build()
        assert request.http_method == HttpMethod.POST
        assert request.uri == "/v1/datasets/:dataset_id/documents/:document_id/segments/:segment_id/child_chunks"

    def test_request_body_builder(self) -> None:
        """Test CreateChildChunkRequestBody builder pattern."""
        request_body = CreateChildChunkRequestBody.builder().content("Child chunk content").build()
        assert request_body.content == "Child chunk content"

    def test_request_body_validation(self) -> None:
        """Test CreateChildChunkRequestBody validation."""
        request_body = CreateChildChunkRequestBody(content="Child chunk content")
        assert request_body.content == "Child chunk content"

    def test_response_inheritance(self) -> None:
        """Test CreateChildChunkResponse inherits from BaseResponse."""
        response = CreateChildChunkResponse()
        assert isinstance(response, BaseResponse)
        assert hasattr(response, "success")
        assert hasattr(response, "code")
        assert hasattr(response, "msg")
        assert hasattr(response, "raw")

    def test_response_data_access(self) -> None:
        """Test CreateChildChunkResponse data access."""
        response = CreateChildChunkResponse(data=None)
        assert response.data is None


class TestListChildChunksModels:
    """Test ListChildChunks API models."""

    def test_request_builder(self) -> None:
        """Test ListChildChunksRequest builder pattern."""
        request = (
            ListChildChunksRequest.builder()
            .dataset_id("dataset-123")
            .document_id("doc-456")
            .segment_id("seg-789")
            .keyword("test")
            .page(1)
            .limit(20)
            .build()
        )
        assert request.dataset_id == "dataset-123"
        assert request.document_id == "doc-456"
        assert request.segment_id == "seg-789"
        assert request.paths["dataset_id"] == "dataset-123"
        assert request.paths["document_id"] == "doc-456"
        assert request.paths["segment_id"] == "seg-789"

    def test_request_validation(self) -> None:
        """Test ListChildChunksRequest validation."""
        request = ListChildChunksRequest.builder().build()
        assert request.http_method == HttpMethod.GET
        assert request.uri == "/v1/datasets/:dataset_id/documents/:document_id/segments/:segment_id/child_chunks"

    def test_response_inheritance(self) -> None:
        """Test ListChildChunksResponse inherits from BaseResponse."""
        response = ListChildChunksResponse()
        assert isinstance(response, BaseResponse)
        assert hasattr(response, "success")
        assert hasattr(response, "code")
        assert hasattr(response, "msg")
        assert hasattr(response, "raw")

    def test_response_data_access(self) -> None:
        """Test ListChildChunksResponse data access."""
        response = ListChildChunksResponse(data=[], total=0, page=1, limit=20)
        assert response.data == []
        assert response.total == 0
        assert response.page == 1
        assert response.limit == 20


class TestDeleteChildChunkModels:
    """Test DeleteChildChunk API models."""

    def test_request_builder(self) -> None:
        """Test DeleteChildChunkRequest builder pattern."""
        request = (
            DeleteChildChunkRequest.builder()
            .dataset_id("dataset-123")
            .document_id("doc-456")
            .segment_id("seg-789")
            .child_chunk_id("chunk-abc")
            .build()
        )
        assert request.dataset_id == "dataset-123"
        assert request.document_id == "doc-456"
        assert request.segment_id == "seg-789"
        assert request.child_chunk_id == "chunk-abc"
        assert request.paths["dataset_id"] == "dataset-123"
        assert request.paths["document_id"] == "doc-456"
        assert request.paths["segment_id"] == "seg-789"
        assert request.paths["child_chunk_id"] == "chunk-abc"

    def test_request_validation(self) -> None:
        """Test DeleteChildChunkRequest validation."""
        request = DeleteChildChunkRequest.builder().build()
        assert request.http_method == HttpMethod.DELETE
        assert (
            request.uri
            == "/v1/datasets/:dataset_id/documents/:document_id/segments/:segment_id/child_chunks/:child_chunk_id"
        )

    def test_response_inheritance(self) -> None:
        """Test DeleteChildChunkResponse inherits from BaseResponse."""
        response = DeleteChildChunkResponse()
        assert isinstance(response, BaseResponse)
        assert hasattr(response, "success")
        assert hasattr(response, "code")
        assert hasattr(response, "msg")
        assert hasattr(response, "raw")

    def test_response_data_access(self) -> None:
        """Test DeleteChildChunkResponse data access."""
        response = DeleteChildChunkResponse()
        assert isinstance(response, DeleteChildChunkResponse)


class TestUpdateChildChunkModels:
    """Test UpdateChildChunk API models."""

    def test_request_builder(self) -> None:
        """Test UpdateChildChunkRequest builder pattern."""
        request_body = UpdateChildChunkRequestBody.builder().content("Updated content").build()
        request = (
            UpdateChildChunkRequest.builder()
            .dataset_id("dataset-123")
            .document_id("doc-456")
            .segment_id("seg-789")
            .child_chunk_id("chunk-abc")
            .request_body(request_body)
            .build()
        )
        assert request.dataset_id == "dataset-123"
        assert request.document_id == "doc-456"
        assert request.segment_id == "seg-789"
        assert request.child_chunk_id == "chunk-abc"
        assert request.request_body is not None

    def test_request_validation(self) -> None:
        """Test UpdateChildChunkRequest validation."""
        request = UpdateChildChunkRequest.builder().build()
        assert request.http_method == HttpMethod.PATCH
        assert (
            request.uri
            == "/v1/datasets/:dataset_id/documents/:document_id/segments/:segment_id/child_chunks/:child_chunk_id"
        )

    def test_request_body_builder(self) -> None:
        """Test UpdateChildChunkRequestBody builder pattern."""
        request_body = UpdateChildChunkRequestBody.builder().content("Updated content").build()
        assert request_body.content == "Updated content"

    def test_request_body_validation(self) -> None:
        """Test UpdateChildChunkRequestBody validation."""
        request_body = UpdateChildChunkRequestBody(content="Updated content")
        assert request_body.content == "Updated content"

    def test_response_inheritance(self) -> None:
        """Test UpdateChildChunkResponse inherits from BaseResponse."""
        response = UpdateChildChunkResponse()
        assert isinstance(response, BaseResponse)
        assert hasattr(response, "success")
        assert hasattr(response, "code")
        assert hasattr(response, "msg")
        assert hasattr(response, "raw")

    def test_response_data_access(self) -> None:
        """Test UpdateChildChunkResponse data access."""
        response = UpdateChildChunkResponse(data=None)
        assert response.data is None
