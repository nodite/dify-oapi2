from __future__ import annotations

from pydantic import BaseModel


class FileUploadConfig(BaseModel):
    image: dict | None = None

    @staticmethod
    def builder() -> FileUploadConfigBuilder:
        return FileUploadConfigBuilder()


class FileUploadConfigBuilder:
    def __init__(self):
        self._file_upload_config = FileUploadConfig()

    def build(self) -> FileUploadConfig:
        return self._file_upload_config

    def image(self, image: dict) -> FileUploadConfigBuilder:
        self._file_upload_config.image = image
        return self
