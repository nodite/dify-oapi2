from __future__ import annotations

from io import BytesIO

from dify_oapi.core.enum import HttpMethod
from dify_oapi.core.model.base_request import BaseRequest

from .update_by_file_request_body import UpdateByFileRequestBody


class UpdateByFileRequest(BaseRequest):
    def __init__(self) -> None:
        super().__init__()
        self.dataset_id: str | None = None
        self.document_id: str | None = None
        self.request_body: UpdateByFileRequestBody | None = None
        self.file: BytesIO | None = None

    @staticmethod
    def builder() -> UpdateByFileRequestBuilder:
        return UpdateByFileRequestBuilder()


class UpdateByFileRequestBuilder:
    def __init__(self) -> None:
        update_by_file_request = UpdateByFileRequest()
        update_by_file_request.http_method = HttpMethod.POST
        update_by_file_request.uri = "/v1/datasets/:dataset_id/documents/:document_id/update-by-file"
        self._update_by_file_request = update_by_file_request

    def build(self) -> UpdateByFileRequest:
        return self._update_by_file_request

    def dataset_id(self, dataset_id: str) -> UpdateByFileRequestBuilder:
        self._update_by_file_request.dataset_id = dataset_id
        self._update_by_file_request.paths["dataset_id"] = dataset_id
        return self

    def document_id(self, document_id: str) -> UpdateByFileRequestBuilder:
        self._update_by_file_request.document_id = document_id
        self._update_by_file_request.paths["document_id"] = document_id
        return self

    def request_body(self, request_body: UpdateByFileRequestBody) -> UpdateByFileRequestBuilder:
        self._update_by_file_request.request_body = request_body
        self._update_by_file_request.body = request_body.model_dump(exclude_none=True, mode="json")
        return self

    def file(self, file: BytesIO, file_name: str | None = None) -> UpdateByFileRequestBuilder:
        self._update_by_file_request.file = file
        file_name = file_name or "upload"
        self._update_by_file_request.files = {"file": (file_name, file)}
        return self
