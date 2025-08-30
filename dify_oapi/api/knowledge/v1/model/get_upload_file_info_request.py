"""Get upload file info request model."""

from __future__ import annotations

from dify_oapi.core.enum import HttpMethod
from dify_oapi.core.model.base_request import BaseRequest


class GetUploadFileInfoRequest(BaseRequest):
    """Request model for get upload file info API."""

    def __init__(self) -> None:
        super().__init__()
        self.dataset_id: str | None = None
        self.document_id: str | None = None

    @staticmethod
    def builder() -> GetUploadFileInfoRequestBuilder:
        return GetUploadFileInfoRequestBuilder()


class GetUploadFileInfoRequestBuilder:
    """Builder for GetUploadFileInfoRequest."""

    def __init__(self) -> None:
        get_upload_file_info_request = GetUploadFileInfoRequest()
        get_upload_file_info_request.http_method = HttpMethod.GET
        get_upload_file_info_request.uri = "/v1/datasets/:dataset_id/documents/:document_id/upload-file"
        self._get_upload_file_info_request = get_upload_file_info_request

    def build(self) -> GetUploadFileInfoRequest:
        return self._get_upload_file_info_request

    def dataset_id(self, dataset_id: str) -> GetUploadFileInfoRequestBuilder:
        self._get_upload_file_info_request.dataset_id = dataset_id
        self._get_upload_file_info_request.paths["dataset_id"] = dataset_id
        return self

    def document_id(self, document_id: str) -> GetUploadFileInfoRequestBuilder:
        self._get_upload_file_info_request.document_id = document_id
        self._get_upload_file_info_request.paths["document_id"] = document_id
        return self
