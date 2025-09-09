from __future__ import annotations

from io import BytesIO

from dify_oapi.core.enum import HttpMethod
from dify_oapi.core.model.base_request import BaseRequest


class UploadFileRequest(BaseRequest):
    """Upload file request model."""

    def __init__(self):
        super().__init__()
        self.file: BytesIO | None = None
        self.user: str | None = None

    @staticmethod
    def builder() -> UploadFileRequestBuilder:
        return UploadFileRequestBuilder()


class UploadFileRequestBuilder:
    def __init__(self):
        upload_file_request = UploadFileRequest()
        upload_file_request.http_method = HttpMethod.POST
        upload_file_request.uri = "/v1/files/upload"
        self._upload_file_request = upload_file_request

    def build(self) -> UploadFileRequest:
        return self._upload_file_request

    def file(self, file: BytesIO, file_name: str | None = None) -> UploadFileRequestBuilder:
        self._upload_file_request.file = file
        file_name = file_name or "upload"
        self._upload_file_request.files = {"file": (file_name, file)}
        return self

    def user(self, user: str) -> UploadFileRequestBuilder:
        self._upload_file_request.user = user
        self._upload_file_request.body = {"user": user}
        return self
