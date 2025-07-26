from __future__ import annotations

from typing import List

from pydantic import BaseModel

from dify_oapi.core.enum import HttpMethod
from dify_oapi.core.model.base_request import BaseRequest


class DocumentMetadata(BaseModel):
    id: str
    value: str
    name: str

    @staticmethod
    def builder() -> DocumentMetadataBuilder:
        return DocumentMetadataBuilder()


class DocumentMetadataBuilder:
    def __init__(self):
        self._metadata = DocumentMetadata(id="", value="", name="")

    def build(self) -> DocumentMetadata:
        return self._metadata

    def id(self, id: str) -> DocumentMetadataBuilder:
        self._metadata.id = id
        return self

    def value(self, value: str) -> DocumentMetadataBuilder:
        self._metadata.value = value
        return self

    def name(self, name: str) -> DocumentMetadataBuilder:
        self._metadata.name = name
        return self


class OperationData(BaseModel):
    document_id: str
    metadata_list: List[DocumentMetadata]

    @staticmethod
    def builder() -> OperationDataBuilder:
        return OperationDataBuilder()


class OperationDataBuilder:
    def __init__(self):
        self._operation_data = OperationData(document_id="", metadata_list=[])

    def build(self) -> OperationData:
        return self._operation_data

    def document_id(self, document_id: str) -> OperationDataBuilder:
        self._operation_data.document_id = document_id
        return self

    def metadata_list(self, metadata_list: List[DocumentMetadata]) -> OperationDataBuilder:
        self._operation_data.metadata_list = metadata_list
        return self


class UpdateDocumentMetadataRequestBody(BaseModel):
    operation_data: List[OperationData] = []


class UpdateDocumentMetadataRequest(BaseRequest):
    def __init__(self):
        super().__init__()
        self.dataset_id: str | None = None
        self.request_body: UpdateDocumentMetadataRequestBody | None = None

    @staticmethod
    def builder() -> UpdateDocumentMetadataRequestBuilder:
        return UpdateDocumentMetadataRequestBuilder()


class UpdateDocumentMetadataRequestBuilder:
    def __init__(self):
        update_document_metadata_request = UpdateDocumentMetadataRequest()
        update_document_metadata_request.http_method = HttpMethod.POST
        update_document_metadata_request.uri = "/v1/datasets/:dataset_id/documents/metadata"
        self._request = update_document_metadata_request

    def build(self) -> UpdateDocumentMetadataRequest:
        return self._request

    def dataset_id(self, dataset_id: str) -> UpdateDocumentMetadataRequestBuilder:
        self._request.dataset_id = dataset_id
        self._request.paths["dataset_id"] = dataset_id
        return self

    def operation_data(self, operation_data: List[OperationData]) -> UpdateDocumentMetadataRequestBuilder:
        if self._request.request_body is None:
            self._request.request_body = UpdateDocumentMetadataRequestBody()
        self._request.request_body.operation_data = operation_data
        self._request.body = self._request.request_body.model_dump(exclude_none=True, mode="json")
        return self