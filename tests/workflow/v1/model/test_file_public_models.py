from dify_oapi.api.workflow.v1.model.file.file_info import FileInfo


class TestFileInfo:
    def test_builder_pattern(self) -> None:
        """Test FileInfo builder pattern functionality."""
        file_info = (
            FileInfo.builder()
            .id("file-123")
            .name("test_document.pdf")
            .size(1024)
            .extension("pdf")
            .mime_type("application/pdf")
            .created_by("user-456")
            .created_at(1234567890)
            .build()
        )
        assert file_info.id == "file-123"
        assert file_info.name == "test_document.pdf"
        assert file_info.size == 1024
        assert file_info.extension == "pdf"
        assert file_info.mime_type == "application/pdf"
        assert file_info.created_by == "user-456"
        assert file_info.created_at == 1234567890

    def test_field_validation(self) -> None:
        """Test FileInfo field validation."""
        file_info = FileInfo(
            id="file-789",
            name="image.jpg",
            size=2048,
            extension="jpg",
            mime_type="image/jpeg",
            created_by="user-123",
            created_at=1234567891,
        )
        assert file_info.id == "file-789"
        assert file_info.name == "image.jpg"
        assert file_info.size == 2048
        assert file_info.extension == "jpg"
        assert file_info.mime_type == "image/jpeg"
        assert file_info.created_by == "user-123"
        assert file_info.created_at == 1234567891

    def test_serialization(self) -> None:
        """Test FileInfo serialization."""
        file_info = FileInfo(
            id="file-123",
            name="test.pdf",
            size=1024,
            extension="pdf",
            mime_type="application/pdf",
            created_by="user-456",
            created_at=1234567890,
        )
        serialized = file_info.model_dump(exclude_none=True)
        assert serialized["id"] == "file-123"
        assert serialized["name"] == "test.pdf"
        assert serialized["size"] == 1024
        assert serialized["extension"] == "pdf"
        assert serialized["mime_type"] == "application/pdf"
        assert serialized["created_by"] == "user-456"
        assert serialized["created_at"] == 1234567890

    def test_direct_instantiation(self) -> None:
        """Test FileInfo direct instantiation alongside builder."""
        direct = FileInfo(id="file-1", name="doc.txt", size=512)
        builder = FileInfo.builder().id("file-1").name("doc.txt").size(512).build()
        assert direct.id == builder.id
        assert direct.name == builder.name
        assert direct.size == builder.size
