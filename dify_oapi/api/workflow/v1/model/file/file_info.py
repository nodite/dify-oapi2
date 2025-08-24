from __future__ import annotations

from pydantic import BaseModel


class FileInfo(BaseModel):
    id: str | None = None
    name: str | None = None
    size: int | None = None
    extension: str | None = None
    mime_type: str | None = None
    created_by: str | None = None
    created_at: int | None = None

    @staticmethod
    def builder() -> FileInfoBuilder:
        return FileInfoBuilder()


class FileInfoBuilder:
    def __init__(self):
        self._file_info = FileInfo()

    def build(self) -> FileInfo:
        return self._file_info

    def id(self, id: str) -> FileInfoBuilder:
        self._file_info.id = id
        return self

    def name(self, name: str) -> FileInfoBuilder:
        self._file_info.name = name
        return self

    def size(self, size: int) -> FileInfoBuilder:
        self._file_info.size = size
        return self

    def extension(self, extension: str) -> FileInfoBuilder:
        self._file_info.extension = extension
        return self

    def mime_type(self, mime_type: str) -> FileInfoBuilder:
        self._file_info.mime_type = mime_type
        return self

    def created_by(self, created_by: str) -> FileInfoBuilder:
        self._file_info.created_by = created_by
        return self

    def created_at(self, created_at: int) -> FileInfoBuilder:
        self._file_info.created_at = created_at
        return self
