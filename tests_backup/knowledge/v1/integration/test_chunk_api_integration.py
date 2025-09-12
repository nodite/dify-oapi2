"""Integration tests for Chunk API functionality."""

from typing import Any
from unittest.mock import Mock

import pytest

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
from dify_oapi.api.knowledge.v1.resource.chunk import Chunk
from dify_oapi.core.model.config import Config
from dify_oapi.core.model.request_option import RequestOption


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
        response = CreateChildChunkResponse(data=[ChildChunkInfo(id="chunk-id", content="Test chunk")])
        mock_execute = Mock(return_value=response)
        monkeypatch.setattr("dify_oapi.core.http.transport.Transport.execute", mock_execute)

        from dify_oapi.api.knowledge.v1.model.create_child_chunk_request_body import ChunkContent

        chunk_content = ChunkContent(content="Test chunk")
        request_body = CreateChildChunkRequestBody.builder().chunks([chunk_content]).build()
        request = (
            CreateChildChunkRequest.builder()
            .dataset_id("dataset-id")
            .document_id("doc-id")
            .segment_id("segment-id")
            .request_body(request_body)
            .build()
        )
        result = chunk_resource.create(request, request_option)

        assert result.data[0].content == "Test chunk"

    def test_update_child_chunk(self, chunk_resource: Chunk, request_option: RequestOption, monkeypatch: Any) -> None:
        """Test PATCH /v1/datasets/{dataset_id}/documents/{document_id}/segments/{segment_id}/child_chunks/{child_chunk_id}"""
        response = UpdateChildChunkResponse(data=ChildChunkInfo(id="chunk-id", content="Updated chunk"))
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

        assert result.data.content == "Updated chunk"

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

    def test_chunk_lifecycle_sync(self, chunk_resource: Chunk, request_option: RequestOption, monkeypatch: Any) -> None:
        """Test complete chunk lifecycle: create → list → update → delete"""
        dataset_id = "test-dataset-id"
        document_id = "test-document-id"
        segment_id = "test-segment-id"
        chunk_id = "test-chunk-id"

        # Mock responses for each step
        create_response = CreateChildChunkResponse(
            data=[ChildChunkInfo(id=chunk_id, content="Test chunk", segment_id=segment_id)]
        )
        list_response = ListChildChunksResponse(
            data=[ChildChunkInfo(id=chunk_id, content="Test chunk", segment_id=segment_id)]
        )
        update_response = UpdateChildChunkResponse(
            data=ChildChunkInfo(id=chunk_id, content="Updated chunk", segment_id=segment_id)
        )
        delete_response = DeleteChildChunkResponse(result="success")

        mock_execute = Mock()
        mock_execute.side_effect = [create_response, list_response, update_response, delete_response]
        monkeypatch.setattr("dify_oapi.core.http.transport.Transport.execute", mock_execute)

        # 1. Create chunk
        from dify_oapi.api.knowledge.v1.model.create_child_chunk_request_body import ChunkContent

        chunk_content = ChunkContent(content="Test chunk")
        create_request_body = CreateChildChunkRequestBody.builder().chunks([chunk_content]).build()
        create_request = (
            CreateChildChunkRequest.builder()
            .dataset_id(dataset_id)
            .document_id(document_id)
            .segment_id(segment_id)
            .request_body(create_request_body)
            .build()
        )
        created = chunk_resource.create(create_request, request_option)
        assert created.data[0].id == chunk_id
        assert created.data[0].content == "Test chunk"

        # 2. List chunks
        list_request = (
            ListChildChunksRequest.builder()
            .dataset_id(dataset_id)
            .document_id(document_id)
            .segment_id(segment_id)
            .build()
        )
        listed = chunk_resource.list(list_request, request_option)
        assert len(listed.data) == 1
        assert listed.data[0].id == chunk_id

        # 3. Update chunk
        update_request_body = UpdateChildChunkRequestBody.builder().content("Updated chunk").build()
        update_request = (
            UpdateChildChunkRequest.builder()
            .dataset_id(dataset_id)
            .document_id(document_id)
            .segment_id(segment_id)
            .child_chunk_id(chunk_id)
            .request_body(update_request_body)
            .build()
        )
        updated = chunk_resource.update(update_request, request_option)
        assert updated.data.content == "Updated chunk"

        # 4. Delete chunk
        delete_request = (
            DeleteChildChunkRequest.builder()
            .dataset_id(dataset_id)
            .document_id(document_id)
            .segment_id(segment_id)
            .child_chunk_id(chunk_id)
            .build()
        )
        chunk_resource.delete(delete_request, request_option)

        # Verify all calls were made
        assert mock_execute.call_count == 4

    def test_error_handling(self, chunk_resource: Chunk, request_option: RequestOption, monkeypatch: Any) -> None:
        """Test error handling scenarios"""
        # Mock error response
        mock_execute = Mock(side_effect=Exception("Chunk API Error"))
        monkeypatch.setattr("dify_oapi.core.http.transport.Transport.execute", mock_execute)

        from dify_oapi.api.knowledge.v1.model.create_child_chunk_request_body import ChunkContent

        chunk_content = ChunkContent(content="Error chunk")
        request_body = CreateChildChunkRequestBody.builder().chunks([chunk_content]).build()
        request = (
            CreateChildChunkRequest.builder()
            .dataset_id("dataset-id")
            .document_id("doc-id")
            .segment_id("segment-id")
            .request_body(request_body)
            .build()
        )

        with pytest.raises(Exception) as exc_info:
            chunk_resource.create(request, request_option)

        assert str(exc_info.value) == "Chunk API Error"

    def test_edge_cases(self, chunk_resource: Chunk, request_option: RequestOption, monkeypatch: Any) -> None:
        """Test edge cases and boundary conditions"""
        # Test empty chunk list
        empty_list_response = ListChildChunksResponse(data=[])
        mock_execute = Mock(return_value=empty_list_response)
        monkeypatch.setattr("dify_oapi.core.http.transport.Transport.execute", mock_execute)

        list_request = (
            ListChildChunksRequest.builder()
            .dataset_id("dataset-id")
            .document_id("doc-id")
            .segment_id("segment-id")
            .build()
        )
        result = chunk_resource.list(list_request, request_option)

        assert len(result.data) == 0

        # Test chunk with large content
        large_content = "Large content " * 1000  # ~13KB content
        create_response = CreateChildChunkResponse(
            data=[ChildChunkInfo(id="large-chunk", content=large_content, segment_id="segment-id")]
        )
        mock_execute.return_value = create_response

        from dify_oapi.api.knowledge.v1.model.create_child_chunk_request_body import ChunkContent

        chunk_content = ChunkContent(content=large_content)
        create_request_body = CreateChildChunkRequestBody.builder().chunks([chunk_content]).build()
        create_request = (
            CreateChildChunkRequest.builder()
            .dataset_id("dataset-id")
            .document_id("doc-id")
            .segment_id("segment-id")
            .request_body(create_request_body)
            .build()
        )
        result = chunk_resource.create(create_request, request_option)

        assert len(result.data[0].content) > 10000
        assert result.data[0].id == "large-chunk"
