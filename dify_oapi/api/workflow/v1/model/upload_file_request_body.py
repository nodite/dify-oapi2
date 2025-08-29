from __future__ import annotations

from pydantic import BaseModel


class UploadFileRequestBody(BaseModel):
    user: str | None = None

    @staticmethod
    def builder() -> UploadFileRequestBodyBuilder:
        return UploadFileRequestBodyBuilder()


class UploadFileRequestBodyBuilder:
    def __init__(self):
        self._upload_file_request_body = UploadFileRequestBody()

    def build(self) -> UploadFileRequestBody:
        return self._upload_file_request_body

    def user(self, user: str) -> UploadFileRequestBodyBuilder:
        self._upload_file_request_body.user = user
        return self
