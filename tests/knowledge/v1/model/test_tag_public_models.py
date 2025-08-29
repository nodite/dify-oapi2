"""Unit tests for tag public models."""

from __future__ import annotations

from dify_oapi.api.knowledge.v1.model.tag.tag_info import TagInfo


class TestTagInfo:
    """Test TagInfo public model."""

    def test_builder_pattern(self) -> None:
        """Test TagInfo builder pattern."""
        tag = TagInfo.builder().id("tag-123").name("test-tag").type("knowledge").binding_count(5).build()
        assert tag.id == "tag-123"
        assert tag.name == "test-tag"
        assert tag.type == "knowledge"
        assert tag.binding_count == 5

    def test_field_validation(self) -> None:
        """Test TagInfo field validation."""
        tag = TagInfo(id="tag-123", name="test-tag", type="knowledge", binding_count=5)
        assert tag.id == "tag-123"
        assert tag.name == "test-tag"
        assert tag.type == "knowledge"
        assert tag.binding_count == 5

    def test_serialization(self) -> None:
        """Test TagInfo serialization."""
        tag = TagInfo.builder().id("tag-123").name("test-tag").type("knowledge").binding_count(5).build()
        data = tag.model_dump(exclude_none=True)
        assert data["id"] == "tag-123"
        assert data["name"] == "test-tag"
        assert data["type"] == "knowledge"
        assert data["binding_count"] == 5

    def test_direct_instantiation(self) -> None:
        """Test TagInfo direct instantiation alongside builder."""
        # Direct instantiation
        direct = TagInfo(id="tag-123", name="test-tag", type="knowledge", binding_count=5)

        # Builder instantiation
        builder = TagInfo.builder().id("tag-123").name("test-tag").type("knowledge").binding_count(5).build()

        # Both should work and be equivalent
        assert direct.id == builder.id
        assert direct.name == builder.name
        assert direct.type == builder.type
        assert direct.binding_count == builder.binding_count

    def test_optional_fields(self) -> None:
        """Test TagInfo optional field handling."""
        tag = TagInfo(id="tag-123", name="test-tag")
        assert tag.name == "test-tag"
        assert tag.id == "tag-123"
        assert tag.type is None
        assert tag.binding_count is None

    def test_binding_count_validation(self) -> None:
        """Test TagInfo binding count field validation."""
        # Test with zero binding count
        tag = TagInfo(id="tag-123", name="test-tag", binding_count=0)
        assert tag.binding_count == 0

        # Test with positive binding count
        tag = TagInfo(id="tag-123", name="test-tag", binding_count=10)
        assert tag.binding_count == 10

        # Test with None binding count
        tag = TagInfo(id="tag-123", name="test-tag", binding_count=None)
        assert tag.binding_count is None

    def test_type_field_validation(self) -> None:
        """Test TagInfo type field validation."""
        # Test with knowledge type
        tag = TagInfo(id="tag-123", name="test-tag", type="knowledge")
        assert tag.type == "knowledge"

        # Test with other type values
        tag = TagInfo(id="tag-123", name="test-tag", type="custom")
        assert tag.type == "custom"

        # Test with None type
        tag = TagInfo(id="tag-123", name="test-tag", type=None)
        assert tag.type is None
