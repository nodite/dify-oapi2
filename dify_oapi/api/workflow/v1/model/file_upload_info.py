from __future__ import annotations

from pydantic import BaseModel


class FileUploadInfo(BaseModel):
    id: str | None = None
    name: str | None = None
    size: int | None = None
    extension: str | None = None
    mime_type: str | None = None
    created_by: str | None = None
    created_at: int | None = None

    @staticmethod
    def builder() -> FileUploadInfoBuilder:
        return FileUploadInfoBuilder()


class FileUploadInfoBuilder:
    def __init__(self):
        self._file_upload_info = FileUploadInfo()

    def build(self) -> FileUploadInfo:
        return self._file_upload_info

    def id(self, id: str) -> FileUploadInfoBuilder:
        self._file_upload_info.id = id
        return self

    def name(self, name: str) -> FileUploadInfoBuilder:
        self._file_upload_info.name = name
        return self

    def size(self, size: int) -> FileUploadInfoBuilder:
        self._file_upload_info.size = size
        return self

    def extension(self, extension: str) -> FileUploadInfoBuilder:
        self._file_upload_info.extension = extension
        return self

    def mime_type(self, mime_type: str) -> FileUploadInfoBuilder:
        self._file_upload_info.mime_type = mime_type
        return self

    def created_by(self, created_by: str) -> FileUploadInfoBuilder:
        self._file_upload_info.created_by = created_by
        return self

    def created_at(self, created_at: int) -> FileUploadInfoBuilder:
        self._file_upload_info.created_at = created_at
        return self
