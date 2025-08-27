from __future__ import annotations

from io import BytesIO

from dify_oapi.core.enum import HttpMethod
from dify_oapi.core.model.base_request import BaseRequest

from .upload_file_request_body import UploadFileRequestBody


class UploadFileRequest(BaseRequest):
    def __init__(self) -> None:
        super().__init__()
        self.request_body: UploadFileRequestBody | None = None
        self.file: BytesIO | None = None

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

    def request_body(self, request_body: UploadFileRequestBody) -> UploadFileRequestBuilder:
        self._upload_file_request.request_body = request_body
        if request_body.user:
            self._upload_file_request.body = {"user": request_body.user}
        return self
