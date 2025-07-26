from __future__ import annotations

from typing import List

from pydantic import BaseModel


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


class UpdateDocumentMetadataRequest(BaseModel):
    dataset_id: str
    operation_data: List[OperationData]

    @staticmethod
    def builder() -> UpdateDocumentMetadataRequestBuilder:
        return UpdateDocumentMetadataRequestBuilder()


class UpdateDocumentMetadataRequestBuilder:
    def __init__(self):
        self._request = UpdateDocumentMetadataRequest(dataset_id="", operation_data=[])

    def build(self) -> UpdateDocumentMetadataRequest:
        return self._request

    def dataset_id(self, dataset_id: str) -> UpdateDocumentMetadataRequestBuilder:
        self._request.dataset_id = dataset_id
        return self

    def operation_data(self, operation_data: List[OperationData]) -> UpdateDocumentMetadataRequestBuilder:
        self._request.operation_data = operation_data
        return self