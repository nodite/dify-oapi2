"""
Comprehensive integration tests for segment API functionality.

This module tests all segment-related APIs including core segment operations
and child chunk management with realistic scenarios and error handling.
"""

from unittest.mock import patch

import pytest

from dify_oapi.api.knowledge_base.v1.model.segment.child_chunk_info import ChildChunkInfo
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
from dify_oapi.api.knowledge_base.v1.resource.segment import Segment
from dify_oapi.core.model.config import Config
from dify_oapi.core.model.request_option import RequestOption


class TestSegmentAPIIntegration:
    """Integration tests for segment API functionality."""

    @pytest.fixture
    def config(self) -> Config:
        """Create test config."""
        config = Config()
        config.domain = "https://api.dify.ai"
        return config

    @pytest.fixture
    def request_option(self) -> RequestOption:
        """Create test request option."""
        return RequestOption.builder().api_key("test-api-key").build()

    @pytest.fixture
    def segment_resource(self, config: Config) -> Segment:
        """Create segment resource instance."""
        return Segment(config)

    # ===== COMPLETE SEGMENT LIFECYCLE TESTS =====

    def test_complete_segment_lifecycle_sync(self, segment_resource: Segment, request_option: RequestOption) -> None:
        """Test complete segment lifecycle: create → list → get → update → delete."""
        with patch("dify_oapi.core.http.transport.Transport.execute") as mock_execute:
            # Mock create response
            create_response_data = CreateResponse(
                success=True,
                data=[
                    SegmentInfo(
                        id="segment-123",
                        content="[Example] Test segment content",
                        position=1,
                        document_id="doc-123",
                        status="completed",
                    )
                ],
                doc_form="text_model",
            )

            # Mock list response
            list_response_data = ListResponse(
                success=True,
                data=[
                    SegmentInfo(
                        id="segment-123",
                        content="[Example] Test segment content",
                        position=1,
                        document_id="doc-123",
                        status="completed",
                    )
                ],
                doc_form="text_model",
                has_more=False,
                limit=20,
                total=1,
                page=1,
            )

            # Mock get response
            get_response_data = GetResponse(
                success=True,
                data=SegmentInfo(
                    id="segment-123",
                    content="[Example] Test segment content",
                    position=1,
                    document_id="doc-123",
                    status="completed",
                    word_count=25,
                    tokens=20,
                ),
                doc_form="text_model",
            )

            # Mock update response
            update_response_data = UpdateResponse(
                success=True,
                data=SegmentInfo(
                    id="segment-123",
                    content="[Example] Updated segment content",
                    position=1,
                    document_id="doc-123",
                    status="completed",
                ),
                doc_form="text_model",
            )

            # Mock delete response
            delete_response_data = DeleteResponse(success=True)

            mock_execute.side_effect = [
                create_response_data,
                list_response_data,
                get_response_data,
                update_response_data,
                delete_response_data,
            ]

            # 1. Create segment
            create_body = (
                CreateRequestBody.builder()
                .segments(
                    [
                        SegmentInfo.builder()
                        .content("[Example] Test segment content")
                        .keywords(["test", "example"])
                        .build()
                    ]
                )
                .build()
            )

            create_req = (
                CreateRequest.builder()
                .dataset_id("dataset-123")
                .document_id("doc-123")
                .request_body(create_body)
                .build()
            )

            create_response = segment_resource.create(create_req, request_option)
            assert create_response.success
            assert len(create_response.data) == 1
            assert create_response.data[0].id == "segment-123"

            # 2. List segments
            list_req = ListRequest.builder().dataset_id("dataset-123").document_id("doc-123").limit(20).build()

            list_response = segment_resource.list(list_req, request_option)
            assert list_response.success
            assert len(list_response.data) == 1
            assert list_response.total == 1

            # 3. Get segment details
            get_req = (
                GetRequest.builder().dataset_id("dataset-123").document_id("doc-123").segment_id("segment-123").build()
            )

            get_response = segment_resource.get(get_req, request_option)
            assert get_response.success
            assert get_response.data.id == "segment-123"
            assert get_response.data.word_count == 25

            # 4. Update segment
            update_body = (
                UpdateRequestBody.builder()
                .segment(
                    SegmentData.builder()
                    .content("[Example] Updated segment content")
                    .keywords(["updated", "test"])
                    .build()
                )
                .build()
            )

            update_req = (
                UpdateRequest.builder()
                .dataset_id("dataset-123")
                .document_id("doc-123")
                .segment_id("segment-123")
                .request_body(update_body)
                .build()
            )

            update_response = segment_resource.update(update_req, request_option)
            assert update_response.success
            assert update_response.data.content == "[Example] Updated segment content"

            # 5. Delete segment
            delete_req = (
                DeleteRequest.builder()
                .dataset_id("dataset-123")
                .document_id("doc-123")
                .segment_id("segment-123")
                .build()
            )

            delete_response = segment_resource.delete(delete_req, request_option)
            assert delete_response.success

            # Verify all calls were made
            assert mock_execute.call_count == 5

    @pytest.mark.asyncio
    async def test_complete_segment_lifecycle_async(
        self, segment_resource: Segment, request_option: RequestOption
    ) -> None:
        """Test complete segment lifecycle with async methods."""
        with patch("dify_oapi.core.http.transport.ATransport.aexecute") as mock_aexecute:
            # Mock responses
            create_response_data = CreateResponse(
                success=True,
                data=[SegmentInfo(id="segment-123", content="[Example] Test content")],
                doc_form="text_model",
            )
            delete_response_data = DeleteResponse(success=True)

            mock_aexecute.side_effect = [create_response_data, delete_response_data]

            # Test async create
            create_body = (
                CreateRequestBody.builder()
                .segments([SegmentInfo.builder().content("[Example] Test content").build()])
                .build()
            )

            create_req = (
                CreateRequest.builder()
                .dataset_id("dataset-123")
                .document_id("doc-123")
                .request_body(create_body)
                .build()
            )

            # Properly await async method
            create_response = await segment_resource.acreate(create_req, request_option)
            assert create_response.success

            # Test async delete
            delete_req = (
                DeleteRequest.builder()
                .dataset_id("dataset-123")
                .document_id("doc-123")
                .segment_id("segment-123")
                .build()
            )

            delete_response = await segment_resource.adelete(delete_req, request_option)
            assert delete_response.success

    # ===== CHILD CHUNK MANAGEMENT TESTS =====

    def test_child_chunk_management_lifecycle(self, segment_resource: Segment, request_option: RequestOption) -> None:
        """Test complete child chunk management lifecycle."""
        with patch("dify_oapi.core.http.transport.Transport.execute") as mock_execute:
            # Mock responses
            create_chunk_response = CreateChildChunkResponse(
                success=True,
                data=ChildChunkInfo(
                    id="chunk-123",
                    segment_id="segment-123",
                    content="[Example] Child chunk content",
                    status="completed",
                ),
            )

            list_chunks_response = ListChildChunksResponse(
                success=True,
                data=[
                    ChildChunkInfo(
                        id="chunk-123",
                        segment_id="segment-123",
                        content="[Example] Child chunk content",
                        status="completed",
                    )
                ],
                total=1,
                total_pages=1,
                page=1,
                limit=20,
            )

            update_chunk_response = UpdateChildChunkResponse(
                success=True,
                data=ChildChunkInfo(
                    id="chunk-123",
                    segment_id="segment-123",
                    content="[Example] Updated child chunk content",
                    status="completed",
                ),
            )

            delete_chunk_response = DeleteChildChunkResponse(success=True)

            mock_execute.side_effect = [
                create_chunk_response,
                list_chunks_response,
                update_chunk_response,
                delete_chunk_response,
            ]

            # 1. Create child chunk
            create_chunk_body = CreateChildChunkRequestBody.builder().content("[Example] Child chunk content").build()

            create_chunk_req = (
                CreateChildChunkRequest.builder()
                .dataset_id("dataset-123")
                .document_id("doc-123")
                .segment_id("segment-123")
                .request_body(create_chunk_body)
                .build()
            )

            create_chunk_result = segment_resource.create_child_chunk(create_chunk_req, request_option)
            assert create_chunk_result.success
            assert create_chunk_result.data.id == "chunk-123"

            # 2. List child chunks
            list_chunks_req = (
                ListChildChunksRequest.builder()
                .dataset_id("dataset-123")
                .document_id("doc-123")
                .segment_id("segment-123")
                .limit(20)
                .build()
            )

            list_chunks_result = segment_resource.list_child_chunks(list_chunks_req, request_option)
            assert list_chunks_result.success
            assert len(list_chunks_result.data) == 1
            assert list_chunks_result.total == 1

            # 3. Update child chunk
            update_chunk_body = (
                UpdateChildChunkRequestBody.builder().content("[Example] Updated child chunk content").build()
            )

            update_chunk_req = (
                UpdateChildChunkRequest.builder()
                .dataset_id("dataset-123")
                .document_id("doc-123")
                .segment_id("segment-123")
                .child_chunk_id("chunk-123")
                .request_body(update_chunk_body)
                .build()
            )

            update_chunk_result = segment_resource.update_child_chunk(update_chunk_req, request_option)
            assert update_chunk_result.success
            assert update_chunk_result.data.content == "[Example] Updated child chunk content"

            # 4. Delete child chunk
            delete_chunk_req = (
                DeleteChildChunkRequest.builder()
                .dataset_id("dataset-123")
                .document_id("doc-123")
                .segment_id("segment-123")
                .child_chunk_id("chunk-123")
                .build()
            )

            delete_chunk_result = segment_resource.delete_child_chunk(delete_chunk_req, request_option)
            assert delete_chunk_result.success

            assert mock_execute.call_count == 4

    # ===== CROSS-OPERATION INTEGRATION TESTS =====

    def test_segment_with_child_chunks_integration(
        self, segment_resource: Segment, request_option: RequestOption
    ) -> None:
        """Test creating segment with child chunks and managing both."""
        with patch("dify_oapi.core.http.transport.Transport.execute") as mock_execute:
            # Mock segment creation
            segment_response = CreateResponse(
                success=True,
                data=[SegmentInfo(id="segment-123", content="[Example] Parent segment")],
                doc_form="text_model",
            )

            # Mock child chunk creation
            chunk_response = CreateChildChunkResponse(
                success=True,
                data=ChildChunkInfo(id="chunk-123", segment_id="segment-123", content="[Example] Child chunk"),
            )

            # Mock segment update
            updated_segment_response = UpdateResponse(
                success=True,
                data=SegmentInfo(id="segment-123", content="[Example] Updated parent segment"),
                doc_form="text_model",
            )

            # Mock child chunk update
            updated_chunk_response = UpdateChildChunkResponse(
                success=True,
                data=ChildChunkInfo(id="chunk-123", segment_id="segment-123", content="[Example] Updated child chunk"),
            )

            # Mock deletions
            delete_chunk_response = DeleteChildChunkResponse(success=True)
            delete_segment_response = DeleteResponse(success=True)

            mock_execute.side_effect = [
                segment_response,
                chunk_response,
                updated_segment_response,
                updated_chunk_response,
                delete_chunk_response,
                delete_segment_response,
            ]

            # 1. Create parent segment
            create_body = (
                CreateRequestBody.builder()
                .segments([SegmentInfo.builder().content("[Example] Parent segment").build()])
                .build()
            )

            create_req = (
                CreateRequest.builder()
                .dataset_id("dataset-123")
                .document_id("doc-123")
                .request_body(create_body)
                .build()
            )

            segment_result = segment_resource.create(create_req, request_option)
            assert segment_result.success

            # 2. Create child chunk
            chunk_body = CreateChildChunkRequestBody.builder().content("[Example] Child chunk").build()

            chunk_req = (
                CreateChildChunkRequest.builder()
                .dataset_id("dataset-123")
                .document_id("doc-123")
                .segment_id("segment-123")
                .request_body(chunk_body)
                .build()
            )

            chunk_result = segment_resource.create_child_chunk(chunk_req, request_option)
            assert chunk_result.success

            # 3. Update both segment and child chunk
            update_segment_body = (
                UpdateRequestBody.builder()
                .segment(SegmentData.builder().content("[Example] Updated parent segment").build())
                .build()
            )

            update_segment_req = (
                UpdateRequest.builder()
                .dataset_id("dataset-123")
                .document_id("doc-123")
                .segment_id("segment-123")
                .request_body(update_segment_body)
                .build()
            )

            updated_segment = segment_resource.update(update_segment_req, request_option)
            assert updated_segment.success

            update_chunk_body = UpdateChildChunkRequestBody.builder().content("[Example] Updated child chunk").build()

            update_chunk_req = (
                UpdateChildChunkRequest.builder()
                .dataset_id("dataset-123")
                .document_id("doc-123")
                .segment_id("segment-123")
                .child_chunk_id("chunk-123")
                .request_body(update_chunk_body)
                .build()
            )

            updated_chunk = segment_resource.update_child_chunk(update_chunk_req, request_option)
            assert updated_chunk.success

            # 4. Delete child chunk first, then segment
            delete_chunk_req = (
                DeleteChildChunkRequest.builder()
                .dataset_id("dataset-123")
                .document_id("doc-123")
                .segment_id("segment-123")
                .child_chunk_id("chunk-123")
                .build()
            )

            chunk_delete_result = segment_resource.delete_child_chunk(delete_chunk_req, request_option)
            assert chunk_delete_result.success

            delete_segment_req = (
                DeleteRequest.builder()
                .dataset_id("dataset-123")
                .document_id("doc-123")
                .segment_id("segment-123")
                .build()
            )

            segment_delete_result = segment_resource.delete(delete_segment_req, request_option)
            assert segment_delete_result.success

            assert mock_execute.call_count == 6

    # ===== LIST OPERATIONS WITH FILTERING AND PAGINATION =====

    def test_list_operations_with_filters(self, segment_resource: Segment, request_option: RequestOption) -> None:
        """Test list operations with various filters and pagination."""
        with patch("dify_oapi.core.http.transport.Transport.execute") as mock_execute:
            # Mock filtered list response
            filtered_response = ListResponse(
                success=True,
                data=[
                    SegmentInfo(id="segment-1", content="[Example] First segment", status="completed"),
                    SegmentInfo(id="segment-2", content="[Example] Second segment", status="completed"),
                ],
                doc_form="text_model",
                has_more=True,
                limit=2,
                total=5,
                page=1,
            )

            # Mock paginated response
            paginated_response = ListResponse(
                success=True,
                data=[SegmentInfo(id="segment-3", content="[Example] Third segment", status="completed")],
                doc_form="text_model",
                has_more=False,
                limit=2,
                total=5,
                page=2,
            )

            # Mock child chunks list
            child_chunks_response = ListChildChunksResponse(
                success=True,
                data=[
                    ChildChunkInfo(id="chunk-1", segment_id="segment-1", content="[Example] Chunk 1"),
                    ChildChunkInfo(id="chunk-2", segment_id="segment-1", content="[Example] Chunk 2"),
                ],
                total=2,
                total_pages=1,
                page=1,
                limit=20,
            )

            mock_execute.side_effect = [filtered_response, paginated_response, child_chunks_response]

            # 1. List with keyword filter and pagination
            filtered_req = (
                ListRequest.builder()
                .dataset_id("dataset-123")
                .document_id("doc-123")
                .keyword("Example")
                .status("completed")
                .page(1)
                .limit(2)
                .build()
            )

            filtered_result = segment_resource.list(filtered_req, request_option)
            assert filtered_result.success
            assert len(filtered_result.data) == 2
            assert filtered_result.has_more is True
            assert filtered_result.total == 5

            # 2. Get next page
            paginated_req = (
                ListRequest.builder().dataset_id("dataset-123").document_id("doc-123").page(2).limit(2).build()
            )

            paginated_result = segment_resource.list(paginated_req, request_option)
            assert paginated_result.success
            assert len(paginated_result.data) == 1
            assert paginated_result.has_more is False

            # 3. List child chunks with keyword
            child_chunks_req = (
                ListChildChunksRequest.builder()
                .dataset_id("dataset-123")
                .document_id("doc-123")
                .segment_id("segment-1")
                .keyword("Example")
                .limit(20)
                .build()
            )

            child_chunks_result = segment_resource.list_child_chunks(child_chunks_req, request_option)
            assert child_chunks_result.success
            assert len(child_chunks_result.data) == 2
            assert child_chunks_result.total == 2

            assert mock_execute.call_count == 3

    # ===== ERROR SCENARIOS =====

    def test_error_scenarios(self, segment_resource: Segment, request_option: RequestOption) -> None:
        """Test various error scenarios and edge cases."""
        with patch("dify_oapi.core.http.transport.Transport.execute") as mock_execute:
            # Mock error responses
            not_found_response = GetResponse(success=False, code="404", msg="Segment not found")
            validation_error_response = CreateResponse(success=False, code="400", msg="Invalid segment data")
            permission_error_response = DeleteResponse(success=False, code="403", msg="Permission denied")

            mock_execute.side_effect = [not_found_response, validation_error_response, permission_error_response]

            # 1. Test segment not found
            get_req = (
                GetRequest.builder()
                .dataset_id("dataset-123")
                .document_id("doc-123")
                .segment_id("nonexistent-segment")
                .build()
            )

            get_result = segment_resource.get(get_req, request_option)
            assert not get_result.success
            assert get_result.code == "404"
            assert "not found" in get_result.msg.lower()

            # 2. Test validation error
            invalid_body = (
                CreateRequestBody.builder()
                .segments(
                    [
                        SegmentInfo.builder().content("").build()  # Empty content
                    ]
                )
                .build()
            )

            create_req = (
                CreateRequest.builder()
                .dataset_id("dataset-123")
                .document_id("doc-123")
                .request_body(invalid_body)
                .build()
            )

            create_result = segment_resource.create(create_req, request_option)
            assert not create_result.success
            assert create_result.code == "400"

            # 3. Test permission error
            delete_req = (
                DeleteRequest.builder()
                .dataset_id("dataset-123")
                .document_id("doc-123")
                .segment_id("protected-segment")
                .build()
            )

            delete_result = segment_resource.delete(delete_req, request_option)
            assert not delete_result.success
            assert delete_result.code == "403"

            assert mock_execute.call_count == 3

    def test_network_error_handling(self, segment_resource: Segment, request_option: RequestOption) -> None:
        """Test network error handling."""
        with patch("dify_oapi.core.http.transport.Transport.execute") as mock_execute:
            # Mock network error
            mock_execute.side_effect = Exception("Network connection failed")

            list_req = ListRequest.builder().dataset_id("dataset-123").document_id("doc-123").build()

            with pytest.raises(Exception) as exc_info:
                segment_resource.list(list_req, request_option)

            assert "Network connection failed" in str(exc_info.value)

    # ===== EDGE CASES =====

    def test_empty_responses(self, segment_resource: Segment, request_option: RequestOption) -> None:
        """Test handling of empty responses."""
        with patch("dify_oapi.core.http.transport.Transport.execute") as mock_execute:
            # Mock empty list response
            empty_list_response = ListResponse(
                success=True, data=[], doc_form="text_model", has_more=False, limit=20, total=0, page=1
            )

            # Mock empty child chunks response
            empty_chunks_response = ListChildChunksResponse(
                success=True, data=[], total=0, total_pages=0, page=1, limit=20
            )

            mock_execute.side_effect = [empty_list_response, empty_chunks_response]

            # Test empty segment list
            list_req = ListRequest.builder().dataset_id("dataset-123").document_id("doc-123").build()

            list_result = segment_resource.list(list_req, request_option)
            assert list_result.success
            assert len(list_result.data) == 0
            assert list_result.total == 0

            # Test empty child chunks list
            chunks_req = (
                ListChildChunksRequest.builder()
                .dataset_id("dataset-123")
                .document_id("doc-123")
                .segment_id("segment-123")
                .build()
            )

            chunks_result = segment_resource.list_child_chunks(chunks_req, request_option)
            assert chunks_result.success
            assert len(chunks_result.data) == 0
            assert chunks_result.total == 0

            assert mock_execute.call_count == 2

    def test_large_content_handling(self, segment_resource: Segment, request_option: RequestOption) -> None:
        """Test handling of large content in segments and child chunks."""
        with patch("dify_oapi.core.http.transport.Transport.execute") as mock_execute:
            # Create large content
            large_content = "[Example] " + "Large content " * 1000  # ~13KB content

            # Mock response for large content
            large_content_response = CreateResponse(
                success=True,
                data=[
                    SegmentInfo(
                        id="segment-large", content=large_content, word_count=2000, tokens=1500, status="completed"
                    )
                ],
                doc_form="text_model",
            )

            mock_execute.return_value = large_content_response

            # Test creating segment with large content
            large_body = (
                CreateRequestBody.builder().segments([SegmentInfo.builder().content(large_content).build()]).build()
            )

            create_req = (
                CreateRequest.builder()
                .dataset_id("dataset-123")
                .document_id("doc-123")
                .request_body(large_body)
                .build()
            )

            result = segment_resource.create(create_req, request_option)
            assert result.success
            assert result.data[0].word_count == 2000
            assert result.data[0].tokens == 1500
            assert len(result.data[0].content) > 10000
