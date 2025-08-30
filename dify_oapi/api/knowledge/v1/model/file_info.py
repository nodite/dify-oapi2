"""File information model for Knowledge Base API."""

from typing import Optional

from pydantic import BaseModel

from .knowledge_types import FileType


class FileInfo(BaseModel):
    """File information model with builder pattern."""

    id: Optional[str] = None
    name: Optional[str] = None
    size: Optional[int] = None
    extension: Optional[str] = None
    mime_type: Optional[str] = None
    type: Optional[FileType] = None
    created_by: Optional[str] = None
    created_at: Optional[float] = None
    upload_file_id: Optional[str] = None

    @staticmethod
    def builder() -> "FileInfoBuilder":
        return FileInfoBuilder()


class FileInfoBuilder:
    """Builder for FileInfo."""

    def __init__(self):
        self._file_info = FileInfo()

    def build(self) -> FileInfo:
        return self._file_info

    def id(self, id: str) -> "FileInfoBuilder":
        self._file_info.id = id
        return self

    def name(self, name: str) -> "FileInfoBuilder":
        self._file_info.name = name
        return self

    def size(self, size: int) -> "FileInfoBuilder":
        self._file_info.size = size
        return self

    def extension(self, extension: str) -> "FileInfoBuilder":
        self._file_info.extension = extension
        return self

    def mime_type(self, mime_type: str) -> "FileInfoBuilder":
        self._file_info.mime_type = mime_type
        return self

    def type(self, type: FileType) -> "FileInfoBuilder":
        self._file_info.type = type
        return self

    def created_by(self, created_by: str) -> "FileInfoBuilder":
        self._file_info.created_by = created_by
        return self

    def created_at(self, created_at: float) -> "FileInfoBuilder":
        self._file_info.created_at = created_at
        return self

    def upload_file_id(self, upload_file_id: str) -> "FileInfoBuilder":
        self._file_info.upload_file_id = upload_file_id
        return self
