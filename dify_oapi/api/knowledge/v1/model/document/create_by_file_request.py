"""Create document by file request model."""

from __future__ import annotations

from io import BytesIO

from dify_oapi.core.enum import HttpMethod
from dify_oapi.core.model.base_request import BaseRequest

from .create_by_file_request_body import CreateByFileRequestBody


class CreateByFileRequest(BaseRequest):
    """Request model for create document by file API."""

    def __init__(self) -> None:
        super().__init__()
        self.dataset_id: str | None = None
        self.request_body: CreateByFileRequestBody | None = None
        self.file: BytesIO | None = None

    @staticmethod
    def builder() -> CreateByFileRequestBuilder:
        return CreateByFileRequestBuilder()


class CreateByFileRequestBuilder:
    """Builder for CreateByFileRequest."""

    def __init__(self) -> None:
        create_by_file_request = CreateByFileRequest()
        create_by_file_request.http_method = HttpMethod.POST
        create_by_file_request.uri = "/v1/datasets/:dataset_id/document/create-by-file"
        self._create_by_file_request = create_by_file_request

    def build(self) -> CreateByFileRequest:
        return self._create_by_file_request

    def dataset_id(self, dataset_id: str) -> CreateByFileRequestBuilder:
        self._create_by_file_request.dataset_id = dataset_id
        self._create_by_file_request.paths["dataset_id"] = dataset_id
        return self

    def request_body(self, request_body: CreateByFileRequestBody) -> CreateByFileRequestBuilder:
        self._create_by_file_request.request_body = request_body
        self._create_by_file_request.body = request_body.model_dump(exclude_none=True, mode="json")
        return self

    def file(self, file: BytesIO, file_name: str | None = None) -> CreateByFileRequestBuilder:
        self._create_by_file_request.file = file
        file_name = file_name or "upload"
        self._create_by_file_request.files = {"file": (file_name, file)}
        return self
