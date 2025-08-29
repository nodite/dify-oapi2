"""Unit tests for metadata public models."""

from __future__ import annotations

from dify_oapi.api.knowledge.v1.model.metadata.metadata_info import MetadataInfo
from dify_oapi.api.knowledge.v1.model.metadata.update_document_request_body import (
    DocumentMetadata,
    OperationData,
)


class TestMetadataInfo:
    """Test MetadataInfo public model."""

    def test_builder_pattern(self) -> None:
        """Test MetadataInfo builder pattern."""
        metadata = MetadataInfo.builder().id("meta-123").type("string").name("test-metadata").build()
        assert metadata.id == "meta-123"
        assert metadata.type == "string"
        assert metadata.name == "test-metadata"

    def test_field_validation(self) -> None:
        """Test MetadataInfo field validation."""
        metadata = MetadataInfo(id="meta-123", type="string", name="test-metadata")
        assert metadata.id == "meta-123"
        assert metadata.type == "string"
        assert metadata.name == "test-metadata"

    def test_serialization(self) -> None:
        """Test MetadataInfo serialization."""
        metadata = MetadataInfo.builder().id("meta-123").type("string").name("test-metadata").build()
        data = metadata.model_dump(exclude_none=True)
        assert data["id"] == "meta-123"
        assert data["type"] == "string"
        assert data["name"] == "test-metadata"

    def test_direct_instantiation(self) -> None:
        """Test MetadataInfo direct instantiation alongside builder."""
        # Direct instantiation
        direct = MetadataInfo(id="meta-123", type="string", name="test-metadata")

        # Builder instantiation
        builder = MetadataInfo.builder().id("meta-123").type("string").name("test-metadata").build()

        # Both should work and be equivalent
        assert direct.id == builder.id
        assert direct.type == builder.type
        assert direct.name == builder.name

    def test_optional_fields(self) -> None:
        """Test MetadataInfo optional field handling."""
        metadata = MetadataInfo(id="meta-123", name="test-metadata", type="string")
        assert metadata.name == "test-metadata"
        assert metadata.id == "meta-123"
        assert metadata.type == "string"
        assert metadata.use_count is None


class TestDocumentMetadata:
    """Test DocumentMetadata public model."""

    def test_builder_pattern(self) -> None:
        """Test DocumentMetadata builder pattern."""
        metadata = DocumentMetadata.builder().id("meta-123").value("test-value").name("test-name").build()
        assert metadata.id == "meta-123"
        assert metadata.value == "test-value"
        assert metadata.name == "test-name"

    def test_field_validation(self) -> None:
        """Test DocumentMetadata field validation."""
        metadata = DocumentMetadata(id="meta-123", value="test-value", name="test-name")
        assert metadata.id == "meta-123"
        assert metadata.value == "test-value"
        assert metadata.name == "test-name"

    def test_serialization(self) -> None:
        """Test DocumentMetadata serialization."""
        metadata = DocumentMetadata.builder().id("meta-123").value("test-value").name("test-name").build()
        data = metadata.model_dump(exclude_none=True)
        assert data["id"] == "meta-123"
        assert data["value"] == "test-value"
        assert data["name"] == "test-name"

    def test_direct_instantiation(self) -> None:
        """Test DocumentMetadata direct instantiation alongside builder."""
        # Direct instantiation
        direct = DocumentMetadata(id="meta-123", value="test-value", name="test-name")

        # Builder instantiation
        builder = DocumentMetadata.builder().id("meta-123").value("test-value").name("test-name").build()

        # Both should work and be equivalent
        assert direct.id == builder.id
        assert direct.value == builder.value
        assert direct.name == builder.name

    def test_optional_fields(self) -> None:
        """Test DocumentMetadata optional field handling."""
        metadata = DocumentMetadata(id="meta-123", value="test-value", name="test-name")
        assert metadata.value == "test-value"
        assert metadata.id == "meta-123"
        assert metadata.name == "test-name"


class TestOperationData:
    """Test OperationData public model."""

    def test_builder_pattern(self) -> None:
        """Test OperationData builder pattern."""
        metadata = DocumentMetadata(id="meta-123", value="test-value", name="test-name")
        operation_data = OperationData.builder().document_id("doc-123").metadata_list([metadata]).build()
        assert operation_data.document_id == "doc-123"
        assert len(operation_data.metadata_list) == 1
        assert operation_data.metadata_list[0].id == "meta-123"

    def test_field_validation(self) -> None:
        """Test OperationData field validation."""
        metadata = DocumentMetadata(id="meta-123", value="test-value", name="test-name")
        operation_data = OperationData(document_id="doc-123", metadata_list=[metadata])
        assert operation_data.document_id == "doc-123"
        assert len(operation_data.metadata_list) == 1

    def test_serialization(self) -> None:
        """Test OperationData serialization."""
        metadata = DocumentMetadata(id="meta-123", value="test-value", name="test-name")
        operation_data = OperationData.builder().document_id("doc-123").metadata_list([metadata]).build()
        data = operation_data.model_dump(exclude_none=True)
        assert data["document_id"] == "doc-123"
        assert len(data["metadata_list"]) == 1

    def test_direct_instantiation(self) -> None:
        """Test OperationData direct instantiation alongside builder."""
        metadata = DocumentMetadata(id="meta-123", value="test-value", name="test-name")

        # Direct instantiation
        direct = OperationData(document_id="doc-123", metadata_list=[metadata])

        # Builder instantiation
        builder = OperationData.builder().document_id("doc-123").metadata_list([metadata]).build()

        # Both should work and be equivalent
        assert direct.document_id == builder.document_id
        assert len(direct.metadata_list) == len(builder.metadata_list)

    def test_empty_metadata_list(self) -> None:
        """Test OperationData with empty metadata list."""
        operation_data = OperationData(document_id="doc-123", metadata_list=[])
        assert operation_data.document_id == "doc-123"
        assert operation_data.metadata_list == []

    def test_multiple_metadata_items(self) -> None:
        """Test OperationData with multiple metadata items."""
        metadata1 = DocumentMetadata(id="meta-1", value="value-1", name="name-1")
        metadata2 = DocumentMetadata(id="meta-2", value="value-2", name="name-2")
        operation_data = OperationData(document_id="doc-123", metadata_list=[metadata1, metadata2])
        assert operation_data.document_id == "doc-123"
        assert len(operation_data.metadata_list) == 2
        assert operation_data.metadata_list[0].id == "meta-1"
        assert operation_data.metadata_list[1].id == "meta-2"
