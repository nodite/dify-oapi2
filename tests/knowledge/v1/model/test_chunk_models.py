"""Tests for child chunks API models."""

from dify_oapi.api.knowledge.v1.model.child_chunk_info import ChildChunkInfo
from dify_oapi.api.knowledge.v1.model.create_child_chunk_request import CreateChildChunkRequest
from dify_oapi.api.knowledge.v1.model.create_child_chunk_request_body import CreateChildChunkRequestBody
from dify_oapi.api.knowledge.v1.model.create_child_chunk_response import CreateChildChunkResponse
from dify_oapi.api.knowledge.v1.model.delete_child_chunk_request import DeleteChildChunkRequest
from dify_oapi.api.knowledge.v1.model.delete_child_chunk_response import DeleteChildChunkResponse
from dify_oapi.api.knowledge.v1.model.list_child_chunks_request import ListChildChunksRequest
from dify_oapi.api.knowledge.v1.model.list_child_chunks_response import ListChildChunksResponse
from dify_oapi.api.knowledge.v1.model.update_child_chunk_request import UpdateChildChunkRequest
from dify_oapi.api.knowledge.v1.model.update_child_chunk_request_body import UpdateChildChunkRequestBody
from dify_oapi.api.knowledge.v1.model.update_child_chunk_response import UpdateChildChunkResponse
from dify_oapi.core.enum import HttpMethod
from dify_oapi.core.model.base_response import BaseResponse


class TestListChildChunksModels:
    """Test List Child Chunks API models."""

    def test_request_builder(self) -> None:
        """Test ListChildChunksRequest builder pattern."""
        request = (
            ListChildChunksRequest.builder()
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
        chunk1 = ChildChunkInfo(id="chunk1", content="Content 1")
        chunk2 = ChildChunkInfo(id="chunk2", content="Content 2")
        response = ListChildChunksResponse(data=[chunk1, chunk2])

        assert response.data is not None
        assert len(response.data) == 2
        assert response.data[0].id == "chunk1"
        assert response.data[1].id == "chunk2"


class TestCreateChildChunkModels:
    """Test Create Child Chunk API models."""

    def test_request_builder(self) -> None:
        """Test CreateChildChunkRequest builder pattern."""
        request_body = (
            CreateChildChunkRequestBody.builder()
            .chunks([{"content": "Test chunk content", "keywords": ["test", "chunk"]}])
            .build()
        )

        request = (
            CreateChildChunkRequest.builder()
            .dataset_id("dataset-123")
            .document_id("doc-456")
            .segment_id("seg-789")
            .request_body(request_body)
            .build()
        )
        assert request.dataset_id == "dataset-123"
        assert request.document_id == "doc-456"
        assert request.segment_id == "seg-789"
        assert request.paths["dataset_id"] == "dataset-123"
        assert request.paths["document_id"] == "doc-456"
        assert request.paths["segment_id"] == "seg-789"
        assert request.request_body is not None
        assert request.request_body.chunks is not None
        assert len(request.request_body.chunks) == 1

    def test_request_validation(self) -> None:
        """Test CreateChildChunkRequest validation."""
        request = CreateChildChunkRequest.builder().build()
        assert request.http_method == HttpMethod.POST
        assert request.uri == "/v1/datasets/:dataset_id/documents/:document_id/segments/:segment_id/child_chunks"

    def test_request_body_builder(self) -> None:
        """Test CreateChildChunkRequestBody builder pattern."""
        request_body = (
            CreateChildChunkRequestBody.builder().chunks([{"content": "Test content", "keywords": ["test"]}]).build()
        )
        assert request_body.chunks is not None
        assert len(request_body.chunks) == 1
        assert request_body.chunks[0]["content"] == "Test content"

    def test_request_body_validation(self) -> None:
        """Test CreateChildChunkRequestBody validation."""
        from dify_oapi.api.knowledge.v1.model.create_child_chunk_request_body import ChunkContent

        chunk_content = ChunkContent(content="Test content", keywords=["test"])
        request_body = CreateChildChunkRequestBody(chunks=[chunk_content])
        assert request_body.chunks is not None
        assert len(request_body.chunks) == 1
        assert request_body.chunks[0].content == "Test content"

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
        chunk = ChildChunkInfo(id="chunk1", content="Content 1")
        response = CreateChildChunkResponse(data=[chunk])
        assert response.data is not None
        assert len(response.data) == 1
        assert response.data[0].id == "chunk1"


class TestUpdateChildChunkModels:
    """Test Update Child Chunk API models."""

    def test_request_builder(self) -> None:
        """Test UpdateChildChunkRequest builder pattern."""
        request_body = (
            UpdateChildChunkRequestBody.builder().content("Updated content").keywords(["updated", "test"]).build()
        )

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
        assert request.paths["dataset_id"] == "dataset-123"
        assert request.paths["document_id"] == "doc-456"
        assert request.paths["segment_id"] == "seg-789"
        assert request.paths["child_chunk_id"] == "chunk-abc"
        assert request.request_body is not None
        assert request.request_body.content == "Updated content"

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
        request_body = UpdateChildChunkRequestBody.builder().content("Updated content").keywords(["updated"]).build()
        assert request_body.content == "Updated content"
        assert request_body.keywords == ["updated"]

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
        chunk = ChildChunkInfo(id="chunk1", content="Updated content")
        response = UpdateChildChunkResponse(data=chunk)
        assert response.data is not None
        assert response.data.id == "chunk1"
        assert response.data.content == "Updated content"


class TestDeleteChildChunkModels:
    """Test Delete Child Chunk API models."""

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
        response = DeleteChildChunkResponse(result="success")
        assert response.result == "success"
