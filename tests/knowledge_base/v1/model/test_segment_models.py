"""Unit tests for segment models."""

from __future__ import annotations

from dify_oapi.api.knowledge_base.v1.model.segment.child_chunk_info import (
    ChildChunkInfo,
    ChildChunkInfoBuilder,
)
from dify_oapi.api.knowledge_base.v1.model.segment.create_request import (
    CreateRequest,
    CreateRequestBuilder,
)
from dify_oapi.api.knowledge_base.v1.model.segment.create_request_body import (
    CreateRequestBody,
    CreateRequestBodyBuilder,
)
from dify_oapi.api.knowledge_base.v1.model.segment.create_response import CreateResponse
from dify_oapi.api.knowledge_base.v1.model.segment.delete_request import (
    DeleteRequest,
)
from dify_oapi.api.knowledge_base.v1.model.segment.delete_response import DeleteResponse
from dify_oapi.api.knowledge_base.v1.model.segment.get_request import (
    GetRequest,
)
from dify_oapi.api.knowledge_base.v1.model.segment.get_response import GetResponse
from dify_oapi.api.knowledge_base.v1.model.segment.list_request import (
    ListRequest,
    ListRequestBuilder,
)
from dify_oapi.api.knowledge_base.v1.model.segment.list_response import ListResponse
from dify_oapi.api.knowledge_base.v1.model.segment.segment_data import (
    SegmentData,
    SegmentDataBuilder,
)
from dify_oapi.api.knowledge_base.v1.model.segment.segment_info import (
    SegmentInfo,
    SegmentInfoBuilder,
)
from dify_oapi.api.knowledge_base.v1.model.segment.update_request import (
    UpdateRequest,
    UpdateRequestBuilder,
)
from dify_oapi.api.knowledge_base.v1.model.segment.update_request_body import (
    UpdateRequestBody,
    UpdateRequestBodyBuilder,
)
from dify_oapi.api.knowledge_base.v1.model.segment.update_response import UpdateResponse
from dify_oapi.core.enum import HttpMethod

# ===== SHARED SEGMENT MODELS TESTS =====


def test_segment_info_creation() -> None:
    """Test valid segment info creation."""
    segment = SegmentInfo(
        id="test-id",
        content="Test content",
        answer="Test answer",
        keywords=["test", "keyword"],
        enabled=True,
    )

    assert segment.id == "test-id"
    assert segment.content == "Test content"
    assert segment.answer == "Test answer"
    assert segment.keywords == ["test", "keyword"]
    assert segment.enabled is True


def test_segment_info_builder_pattern() -> None:
    """Test builder pattern functionality."""
    segment = (
        SegmentInfo.builder()
        .id("test-id")
        .content("Test content")
        .answer("Test answer")
        .keywords(["test", "keyword"])
        .enabled(True)
        .position(1)
        .word_count(100)
        .tokens(50)
        .build()
    )

    assert segment.id == "test-id"
    assert segment.content == "Test content"
    assert segment.answer == "Test answer"
    assert segment.keywords == ["test", "keyword"]
    assert segment.enabled is True
    assert segment.position == 1
    assert segment.word_count == 100
    assert segment.tokens == 50


def test_segment_info_builder_chaining() -> None:
    """Test builder method chaining."""
    builder = SegmentInfo.builder()
    result = builder.id("test").content("content").answer("answer")

    assert isinstance(result, SegmentInfoBuilder)
    assert result is builder  # Should return same instance for chaining


def test_segment_info_serialization() -> None:
    """Test serialization with model_dump."""
    segment = SegmentInfo.builder().id("test-id").content("Test content").enabled(True).build()

    data = segment.model_dump(exclude_none=True)

    assert data["id"] == "test-id"
    assert data["content"] == "Test content"
    assert data["enabled"] is True
    assert "position" not in data  # Should exclude None values


def test_child_chunk_info_creation() -> None:
    """Test valid child chunk info creation."""
    chunk = ChildChunkInfo(
        id="chunk-id",
        segment_id="segment-id",
        content="Chunk content",
        word_count=25,
        tokens=20,
        status="completed",
    )

    assert chunk.id == "chunk-id"
    assert chunk.segment_id == "segment-id"
    assert chunk.content == "Chunk content"
    assert chunk.word_count == 25
    assert chunk.tokens == 20
    assert chunk.status == "completed"


def test_child_chunk_info_builder_pattern() -> None:
    """Test child chunk info builder pattern."""
    chunk = (
        ChildChunkInfo.builder()
        .id("chunk-id")
        .segment_id("segment-id")
        .content("Chunk content")
        .word_count(25)
        .tokens(20)
        .status("completed")
        .build()
    )

    assert chunk.id == "chunk-id"
    assert chunk.segment_id == "segment-id"
    assert chunk.content == "Chunk content"
    assert chunk.word_count == 25
    assert chunk.tokens == 20
    assert chunk.status == "completed"


def test_child_chunk_info_builder_chaining() -> None:
    """Test child chunk builder method chaining."""
    builder = ChildChunkInfo.builder()
    result = builder.id("test").content("content").status("completed")

    assert isinstance(result, ChildChunkInfoBuilder)
    assert result is builder


def test_segment_data_creation() -> None:
    """Test segment data creation for updates."""
    data = SegmentData(
        content="Updated content",
        answer="Updated answer",
        keywords=["updated", "keywords"],
        enabled=False,
        regenerate_child_chunks=True,
    )

    assert data.content == "Updated content"
    assert data.answer == "Updated answer"
    assert data.keywords == ["updated", "keywords"]
    assert data.enabled is False
    assert data.regenerate_child_chunks is True


def test_segment_data_builder() -> None:
    """Test segment data builder pattern."""
    data = (
        SegmentData.builder()
        .content("Updated content")
        .answer("Updated answer")
        .keywords(["updated", "keywords"])
        .enabled(False)
        .regenerate_child_chunks(True)
        .build()
    )

    assert data.content == "Updated content"
    assert data.answer == "Updated answer"
    assert data.keywords == ["updated", "keywords"]
    assert data.enabled is False
    assert data.regenerate_child_chunks is True


def test_segment_data_builder_chaining() -> None:
    """Test segment data builder method chaining."""
    builder = SegmentData.builder()
    result = builder.content("test").enabled(True).regenerate_child_chunks(False)

    assert isinstance(result, SegmentDataBuilder)
    assert result is builder


def test_optional_field_handling() -> None:
    """Test optional field handling across all models."""
    # Test SegmentInfo with minimal fields
    segment = SegmentInfo(content="Test")
    assert segment.content == "Test"
    assert segment.id is None
    assert segment.keywords is None

    # Test ChildChunkInfo with minimal fields
    chunk = ChildChunkInfo(content="Chunk")
    assert chunk.content == "Chunk"
    assert chunk.id is None
    assert chunk.segment_id is None

    # Test SegmentData with minimal fields
    data = SegmentData(content="Data")
    assert data.content == "Data"
    assert data.enabled is None
    assert data.regenerate_child_chunks is None


def test_array_field_validation() -> None:
    """Test array field validation for keywords."""
    # Valid keywords array
    segment = SegmentInfo(keywords=["keyword1", "keyword2"])
    assert segment.keywords == ["keyword1", "keyword2"]

    # Empty keywords array
    segment = SegmentInfo(keywords=[])
    assert segment.keywords == []

    # None keywords
    segment = SegmentInfo(keywords=None)
    assert segment.keywords is None


def test_model_serialization_deserialization() -> None:
    """Test model serialization and deserialization."""
    original_segment = (
        SegmentInfo.builder()
        .id("test-id")
        .content("Test content")
        .keywords(["test"])
        .enabled(True)
        .word_count(100)
        .build()
    )

    # Serialize
    data = original_segment.model_dump()

    # Deserialize
    restored_segment = SegmentInfo(**data)

    assert restored_segment.id == original_segment.id
    assert restored_segment.content == original_segment.content
    assert restored_segment.keywords == original_segment.keywords
    assert restored_segment.enabled == original_segment.enabled
    assert restored_segment.word_count == original_segment.word_count


def test_edge_cases_and_validation() -> None:
    """Test edge cases and validation scenarios."""
    # Test with empty strings
    segment = SegmentInfo(content="", answer="")
    assert segment.content == ""
    assert segment.answer == ""

    # Test with zero values
    chunk = ChildChunkInfo(word_count=0, tokens=0)
    assert chunk.word_count == 0
    assert chunk.tokens == 0

    # Test boolean fields
    data = SegmentData(enabled=False, regenerate_child_chunks=False)
    assert data.enabled is False
    assert data.regenerate_child_chunks is False


# ===== CORE SEGMENT API MODELS TESTS =====


def test_create_request_builder() -> None:
    """Test CreateRequest builder pattern."""
    request = CreateRequest.builder().dataset_id("dataset-123").document_id("doc-456").build()

    assert request.dataset_id == "dataset-123"
    assert request.document_id == "doc-456"
    assert request.http_method == HttpMethod.POST
    assert request.uri == "/v1/datasets/:dataset_id/documents/:document_id/segments"
    assert request.paths["dataset_id"] == "dataset-123"
    assert request.paths["document_id"] == "doc-456"


def test_create_request_body_validation() -> None:
    """Test CreateRequestBody validation and builder."""
    segment = SegmentInfo.builder().content("Test content").build()

    request_body = CreateRequestBody.builder().segments([segment]).build()

    assert request_body.segments is not None
    assert len(request_body.segments) == 1
    assert request_body.segments[0].content == "Test content"


def test_create_request_with_body() -> None:
    """Test CreateRequest with request body."""
    segment = SegmentInfo.builder().content("Test content").build()
    request_body = CreateRequestBody.builder().segments([segment]).build()

    request = (
        CreateRequest.builder().dataset_id("dataset-123").document_id("doc-456").request_body(request_body).build()
    )

    assert request.request_body is not None
    assert request.body is not None
    assert isinstance(request.body, dict)


def test_list_request_query_params() -> None:
    """Test ListRequest query parameter handling."""
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
    assert request.http_method == HttpMethod.GET
    assert request.uri == "/v1/datasets/:dataset_id/documents/:document_id/segments"
    assert request.paths["dataset_id"] == "dataset-123"
    assert request.paths["document_id"] == "doc-456"


def test_get_request_path_params() -> None:
    """Test GetRequest path parameter handling."""
    request = GetRequest.builder().dataset_id("dataset-123").document_id("doc-456").segment_id("seg-789").build()

    assert request.dataset_id == "dataset-123"
    assert request.document_id == "doc-456"
    assert request.segment_id == "seg-789"
    assert request.http_method == HttpMethod.GET
    assert request.uri == "/v1/datasets/:dataset_id/documents/:document_id/segments/:segment_id"
    assert request.paths["dataset_id"] == "dataset-123"
    assert request.paths["document_id"] == "doc-456"
    assert request.paths["segment_id"] == "seg-789"


def test_update_request_builder() -> None:
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
    assert request.http_method == HttpMethod.POST
    assert request.uri == "/v1/datasets/:dataset_id/documents/:document_id/segments/:segment_id"
    assert request.request_body is not None
    assert request.body is not None


def test_delete_request_builder() -> None:
    """Test DeleteRequest builder pattern."""
    request = DeleteRequest.builder().dataset_id("dataset-123").document_id("doc-456").segment_id("seg-789").build()

    assert request.dataset_id == "dataset-123"
    assert request.document_id == "doc-456"
    assert request.segment_id == "seg-789"
    assert request.http_method == HttpMethod.DELETE
    assert request.uri == "/v1/datasets/:dataset_id/documents/:document_id/segments/:segment_id"


def test_response_models_inheritance() -> None:
    """Test all Response models inherit from BaseResponse."""
    # Test CreateResponse
    create_response = CreateResponse()
    assert hasattr(create_response, "success")
    assert hasattr(create_response, "code")
    assert hasattr(create_response, "msg")
    assert hasattr(create_response, "raw")

    # Test ListResponse
    list_response = ListResponse()
    assert hasattr(list_response, "success")
    assert hasattr(list_response, "data")
    assert hasattr(list_response, "has_more")

    # Test GetResponse
    get_response = GetResponse()
    assert hasattr(get_response, "success")
    assert hasattr(get_response, "data")

    # Test UpdateResponse
    update_response = UpdateResponse()
    assert hasattr(update_response, "success")
    assert hasattr(update_response, "data")

    # Test DeleteResponse
    delete_response = DeleteResponse()
    assert hasattr(delete_response, "success")


def test_request_builder_chaining() -> None:
    """Test request builder method chaining."""
    # Test CreateRequest chaining
    builder = CreateRequest.builder()
    result = builder.dataset_id("test").document_id("test")
    assert isinstance(result, CreateRequestBuilder)
    assert result is builder

    # Test ListRequest chaining
    builder = ListRequest.builder()
    result = builder.dataset_id("test").keyword("test").page(1)
    assert isinstance(result, ListRequestBuilder)
    assert result is builder

    # Test UpdateRequest chaining
    builder = UpdateRequest.builder()
    result = builder.dataset_id("test").document_id("test").segment_id("test")
    assert isinstance(result, UpdateRequestBuilder)
    assert result is builder


def test_request_body_builder_chaining() -> None:
    """Test request body builder method chaining."""
    # Test CreateRequestBody chaining
    builder = CreateRequestBody.builder()
    result = builder.segments([])
    assert isinstance(result, CreateRequestBodyBuilder)
    assert result is builder

    # Test UpdateRequestBody chaining
    builder = UpdateRequestBody.builder()
    segment_data = SegmentData.builder().content("test").build()
    result = builder.segment(segment_data)
    assert isinstance(result, UpdateRequestBodyBuilder)
    assert result is builder


def test_http_method_configuration() -> None:
    """Test HTTP method and URI configuration."""
    # Test POST methods
    create_request = CreateRequest.builder().build()
    assert create_request.http_method == HttpMethod.POST

    update_request = UpdateRequest.builder().build()
    assert update_request.http_method == HttpMethod.POST

    # Test GET methods
    list_request = ListRequest.builder().build()
    assert list_request.http_method == HttpMethod.GET

    get_request = GetRequest.builder().build()
    assert get_request.http_method == HttpMethod.GET

    # Test DELETE method
    delete_request = DeleteRequest.builder().build()
    assert delete_request.http_method == HttpMethod.DELETE
