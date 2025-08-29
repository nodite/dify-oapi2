from __future__ import annotations

from typing import Any

from pydantic import BaseModel


class FileUploadConfig(BaseModel):
    document: dict[str, Any] | None = None
    image: dict[str, Any] | None = None
    audio: dict[str, Any] | None = None
    video: dict[str, Any] | None = None
    custom: dict[str, Any] | None = None

    @staticmethod
    def builder() -> FileUploadConfigBuilder:
        return FileUploadConfigBuilder()


class FileUploadConfigBuilder:
    def __init__(self):
        self._file_upload_config = FileUploadConfig()

    def build(self) -> FileUploadConfig:
        return self._file_upload_config

    def document(self, document: dict[str, Any]) -> FileUploadConfigBuilder:
        self._file_upload_config.document = document
        return self

    def image(self, image: dict[str, Any]) -> FileUploadConfigBuilder:
        self._file_upload_config.image = image
        return self

    def audio(self, audio: dict[str, Any]) -> FileUploadConfigBuilder:
        self._file_upload_config.audio = audio
        return self

    def video(self, video: dict[str, Any]) -> FileUploadConfigBuilder:
        self._file_upload_config.video = video
        return self

    def custom(self, custom: dict[str, Any]) -> FileUploadConfigBuilder:
        self._file_upload_config.custom = custom
        return self
