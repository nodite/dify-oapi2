from __future__ import annotations

from pydantic import BaseModel


class UploadFileInfo(BaseModel):
    """Upload file information model for document file details."""

    id: str | None = None
    name: str | None = None
    size: int | None = None
    extension: str | None = None
    url: str | None = None
    download_url: str | None = None
    mime_type: str | None = None
    created_by: str | None = None
    created_at: float | None = None

    @staticmethod
    def builder() -> UploadFileInfoBuilder:
        return UploadFileInfoBuilder()


class UploadFileInfoBuilder:
    def __init__(self):
        self._upload_file_info = UploadFileInfo()

    def build(self) -> UploadFileInfo:
        return self._upload_file_info

    def id(self, id: str) -> UploadFileInfoBuilder:
        self._upload_file_info.id = id
        return self

    def name(self, name: str) -> UploadFileInfoBuilder:
        self._upload_file_info.name = name
        return self

    def size(self, size: int) -> UploadFileInfoBuilder:
        self._upload_file_info.size = size
        return self

    def extension(self, extension: str) -> UploadFileInfoBuilder:
        self._upload_file_info.extension = extension
        return self

    def url(self, url: str) -> UploadFileInfoBuilder:
        self._upload_file_info.url = url
        return self

    def download_url(self, download_url: str) -> UploadFileInfoBuilder:
        self._upload_file_info.download_url = download_url
        return self

    def mime_type(self, mime_type: str) -> UploadFileInfoBuilder:
        self._upload_file_info.mime_type = mime_type
        return self

    def created_by(self, created_by: str) -> UploadFileInfoBuilder:
        self._upload_file_info.created_by = created_by
        return self

    def created_at(self, created_at: float) -> UploadFileInfoBuilder:
        self._upload_file_info.created_at = created_at
        return self
