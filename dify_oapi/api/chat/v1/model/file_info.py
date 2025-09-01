"""File information model for Chat API."""

from __future__ import annotations

from pydantic import BaseModel, Field


class FileInfo(BaseModel):
    """File information model."""

    id: str | None = Field(None, description="File ID")
    name: str | None = Field(None, description="File name")
    size: int | None = Field(None, description="File size in bytes")
    extension: str | None = Field(None, description="File extension")
    mime_type: str | None = Field(None, description="MIME type")
    created_by: str | None = Field(None, description="User ID who created the file")
    created_at: int | None = Field(None, description="Creation timestamp")

    @classmethod
    def builder(cls) -> FileInfoBuilder:
        """Create a FileInfo builder."""
        return FileInfoBuilder()


class FileInfoBuilder:
    """Builder for FileInfo."""

    def __init__(self) -> None:
        self._file_info = FileInfo()

    def id(self, id: str) -> FileInfoBuilder:
        """Set file ID."""
        self._file_info.id = id
        return self

    def name(self, name: str) -> FileInfoBuilder:
        """Set file name."""
        self._file_info.name = name
        return self

    def size(self, size: int) -> FileInfoBuilder:
        """Set file size."""
        self._file_info.size = size
        return self

    def extension(self, extension: str) -> FileInfoBuilder:
        """Set file extension."""
        self._file_info.extension = extension
        return self

    def mime_type(self, mime_type: str) -> FileInfoBuilder:
        """Set MIME type."""
        self._file_info.mime_type = mime_type
        return self

    def created_by(self, created_by: str) -> FileInfoBuilder:
        """Set creator user ID."""
        self._file_info.created_by = created_by
        return self

    def created_at(self, created_at: int) -> FileInfoBuilder:
        """Set creation timestamp."""
        self._file_info.created_at = created_at
        return self

    def build(self) -> FileInfo:
        """Build the FileInfo instance."""
        return self._file_info
