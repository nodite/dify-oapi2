from __future__ import annotations

from dify_oapi.core.enum import HttpMethod
from dify_oapi.core.model.base_request import BaseRequest


class GetUploadFileRequest(BaseRequest):
    """Request model for get upload file API."""

    def __init__(self):
        super().__init__()
        self.dataset_id: str | None = None
        self.document_id: str | None = None

    @staticmethod
    def builder() -> GetUploadFileRequestBuilder:
        return GetUploadFileRequestBuilder()


class GetUploadFileRequestBuilder:
    def __init__(self):
        get_upload_file_request = GetUploadFileRequest()
        get_upload_file_request.http_method = HttpMethod.GET
        get_upload_file_request.uri = "/v1/datasets/:dataset_id/documents/:document_id/upload-file"
        self._get_upload_file_request = get_upload_file_request

    def build(self) -> GetUploadFileRequest:
        return self._get_upload_file_request

    def dataset_id(self, dataset_id: str) -> GetUploadFileRequestBuilder:
        self._get_upload_file_request.dataset_id = dataset_id
        self._get_upload_file_request.paths["dataset_id"] = dataset_id
        return self

    def document_id(self, document_id: str) -> GetUploadFileRequestBuilder:
        self._get_upload_file_request.document_id = document_id
        self._get_upload_file_request.paths["document_id"] = document_id
        return self
