"""Unit tests for segment models."""

from __future__ import annotations

from dify_oapi.api.knowledge_base.v1.model.segment.child_chunk_info import (
    ChildChunkInfo,
    ChildChunkInfoBuilder,
)
from dify_oapi.api.knowledge_base.v1.model.segment.segment_data import (
    SegmentData,
    SegmentDataBuilder,
)
from dify_oapi.api.knowledge_base.v1.model.segment.segment_info import (
    SegmentInfo,
    SegmentInfoBuilder,
)

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
