from __future__ import annotations

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
    metadata_list: list[DocumentMetadata]

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

    def metadata_list(self, metadata_list: list[DocumentMetadata]) -> OperationDataBuilder:
        self._operation_data.metadata_list = metadata_list
        return self


class UpdateDocumentRequestBody(BaseModel):
    operation_data: list[OperationData] | None = None

    @staticmethod
    def builder() -> UpdateDocumentRequestBodyBuilder:
        return UpdateDocumentRequestBodyBuilder()


class UpdateDocumentRequestBodyBuilder:
    def __init__(self):
        update_document_request_body = UpdateDocumentRequestBody()
        self._update_document_request_body = update_document_request_body

    def build(self) -> UpdateDocumentRequestBody:
        return self._update_document_request_body

    def operation_data(self, operation_data: list[OperationData]) -> UpdateDocumentRequestBodyBuilder:
        self._update_document_request_body.operation_data = operation_data
        return self
