"""Unit tests for segment public models."""

from __future__ import annotations

from dify_oapi.api.knowledge.v1.model.segment.child_chunk_info import ChildChunkInfo
from dify_oapi.api.knowledge.v1.model.segment.segment_data import SegmentData
from dify_oapi.api.knowledge.v1.model.segment.segment_info import SegmentInfo


class TestSegmentInfo:
    """Test SegmentInfo public model."""

    def test_builder_pattern(self) -> None:
        """Test SegmentInfo builder pattern."""
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

    def test_field_validation(self) -> None:
        """Test SegmentInfo field validation."""
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

    def test_serialization(self) -> None:
        """Test SegmentInfo serialization."""
        segment = SegmentInfo.builder().id("test-id").content("Test content").enabled(True).build()
        data = segment.model_dump(exclude_none=True)
        assert data["id"] == "test-id"
        assert data["content"] == "Test content"
        assert data["enabled"] is True
        assert "position" not in data  # Should exclude None values

    def test_direct_instantiation(self) -> None:
        """Test SegmentInfo direct instantiation alongside builder."""
        # Direct instantiation
        direct = SegmentInfo(content="Test content", enabled=True)

        # Builder instantiation
        builder = SegmentInfo.builder().content("Test content").enabled(True).build()

        # Both should work and be equivalent
        assert direct.content == builder.content
        assert direct.enabled == builder.enabled

    def test_optional_fields(self) -> None:
        """Test SegmentInfo optional field handling."""
        segment = SegmentInfo(content="Test")
        assert segment.content == "Test"
        assert segment.id is None
        assert segment.keywords is None
        assert segment.enabled is None

    def test_keywords_array_validation(self) -> None:
        """Test keywords array field validation."""
        # Valid keywords array
        segment = SegmentInfo(keywords=["keyword1", "keyword2"])
        assert segment.keywords == ["keyword1", "keyword2"]

        # Empty keywords array
        segment = SegmentInfo(keywords=[])
        assert segment.keywords == []

        # None keywords
        segment = SegmentInfo(keywords=None)
        assert segment.keywords is None


class TestChildChunkInfo:
    """Test ChildChunkInfo public model."""

    def test_builder_pattern(self) -> None:
        """Test ChildChunkInfo builder pattern."""
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

    def test_field_validation(self) -> None:
        """Test ChildChunkInfo field validation."""
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

    def test_serialization(self) -> None:
        """Test ChildChunkInfo serialization."""
        chunk = ChildChunkInfo.builder().id("chunk-id").content("Chunk content").status("completed").build()
        data = chunk.model_dump(exclude_none=True)
        assert data["id"] == "chunk-id"
        assert data["content"] == "Chunk content"
        assert data["status"] == "completed"

    def test_direct_instantiation(self) -> None:
        """Test ChildChunkInfo direct instantiation alongside builder."""
        # Direct instantiation
        direct = ChildChunkInfo(content="Chunk content", status="completed")

        # Builder instantiation
        builder = ChildChunkInfo.builder().content("Chunk content").status("completed").build()

        # Both should work and be equivalent
        assert direct.content == builder.content
        assert direct.status == builder.status

    def test_optional_fields(self) -> None:
        """Test ChildChunkInfo optional field handling."""
        chunk = ChildChunkInfo(content="Chunk")
        assert chunk.content == "Chunk"
        assert chunk.id is None
        assert chunk.segment_id is None
        assert chunk.word_count is None

    def test_numeric_fields(self) -> None:
        """Test ChildChunkInfo numeric field handling."""
        # Test with zero values
        chunk = ChildChunkInfo(word_count=0, tokens=0)
        assert chunk.word_count == 0
        assert chunk.tokens == 0

        # Test with positive values
        chunk = ChildChunkInfo(word_count=100, tokens=50)
        assert chunk.word_count == 100
        assert chunk.tokens == 50


class TestSegmentData:
    """Test SegmentData public model."""

    def test_builder_pattern(self) -> None:
        """Test SegmentData builder pattern."""
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

    def test_field_validation(self) -> None:
        """Test SegmentData field validation."""
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

    def test_serialization(self) -> None:
        """Test SegmentData serialization."""
        data = SegmentData.builder().content("Updated content").enabled(False).build()
        serialized = data.model_dump(exclude_none=True)
        assert serialized["content"] == "Updated content"
        assert serialized["enabled"] is False

    def test_direct_instantiation(self) -> None:
        """Test SegmentData direct instantiation alongside builder."""
        # Direct instantiation
        direct = SegmentData(content="Updated content", enabled=False)

        # Builder instantiation
        builder = SegmentData.builder().content("Updated content").enabled(False).build()

        # Both should work and be equivalent
        assert direct.content == builder.content
        assert direct.enabled == builder.enabled

    def test_optional_fields(self) -> None:
        """Test SegmentData optional field handling."""
        data = SegmentData(content="Data")
        assert data.content == "Data"
        assert data.enabled is None
        assert data.regenerate_child_chunks is None
        assert data.keywords is None

    def test_boolean_fields(self) -> None:
        """Test SegmentData boolean field handling."""
        # Test False values
        data = SegmentData(enabled=False, regenerate_child_chunks=False)
        assert data.enabled is False
        assert data.regenerate_child_chunks is False

        # Test True values
        data = SegmentData(enabled=True, regenerate_child_chunks=True)
        assert data.enabled is True
        assert data.regenerate_child_chunks is True

    def test_keywords_array_handling(self) -> None:
        """Test SegmentData keywords array handling."""
        # Valid keywords array
        data = SegmentData(keywords=["keyword1", "keyword2"])
        assert data.keywords == ["keyword1", "keyword2"]

        # Empty keywords array
        data = SegmentData(keywords=[])
        assert data.keywords == []

        # None keywords
        data = SegmentData(keywords=None)
        assert data.keywords is None
