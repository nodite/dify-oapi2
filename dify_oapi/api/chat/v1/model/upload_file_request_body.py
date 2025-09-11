"""Upload file request body model."""

from __future__ import annotations

from pydantic import BaseModel


class UploadFileRequestBody(BaseModel):
    """Request body for upload file API."""

    user: str

    @staticmethod
    def builder() -> UploadFileRequestBodyBuilder:
        return UploadFileRequestBodyBuilder()


class UploadFileRequestBodyBuilder:
    """Builder for UploadFileRequestBody."""

    def __init__(self) -> None:
        self._upload_file_request_body = UploadFileRequestBody(user="")

    def build(self) -> UploadFileRequestBody:
        return self._upload_file_request_body

    def user(self, user: str) -> UploadFileRequestBodyBuilder:
        self._upload_file_request_body.user = user
        return self
