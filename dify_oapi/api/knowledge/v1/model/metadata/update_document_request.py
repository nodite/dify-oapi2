from __future__ import annotations

from dify_oapi.core.enum import HttpMethod
from dify_oapi.core.model.base_request import BaseRequest

from .update_document_request_body import UpdateDocumentRequestBody


class UpdateDocumentRequest(BaseRequest):
    def __init__(self):
        super().__init__()
        self.dataset_id: str | None = None
        self.request_body: UpdateDocumentRequestBody | None = None

    @staticmethod
    def builder() -> UpdateDocumentRequestBuilder:
        return UpdateDocumentRequestBuilder()


class UpdateDocumentRequestBuilder:
    def __init__(self):
        update_document_request = UpdateDocumentRequest()
        update_document_request.http_method = HttpMethod.POST
        update_document_request.uri = "/v1/datasets/:dataset_id/documents/metadata"
        self._update_document_request = update_document_request

    def build(self) -> UpdateDocumentRequest:
        return self._update_document_request

    def dataset_id(self, dataset_id: str) -> UpdateDocumentRequestBuilder:
        self._update_document_request.dataset_id = dataset_id
        self._update_document_request.paths["dataset_id"] = dataset_id
        return self

    def request_body(self, request_body: UpdateDocumentRequestBody) -> UpdateDocumentRequestBuilder:
        self._update_document_request.request_body = request_body
        self._update_document_request.body = request_body.model_dump(exclude_none=True, mode="json")
        return self
