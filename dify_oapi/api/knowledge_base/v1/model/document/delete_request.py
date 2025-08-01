from __future__ import annotations

from dify_oapi.core.enum import HttpMethod
from dify_oapi.core.model.base_request import BaseRequest


class DeleteRequest(BaseRequest):
    """Request model for delete document API"""

    def __init__(self):
        super().__init__()
        self.dataset_id: str | None = None
        self.document_id: str | None = None

    @staticmethod
    def builder() -> DeleteRequestBuilder:
        return DeleteRequestBuilder()


class DeleteRequestBuilder:
    def __init__(self):
        delete_request = DeleteRequest()
        delete_request.http_method = HttpMethod.DELETE
        delete_request.uri = "/v1/datasets/:dataset_id/documents/:document_id"
        self._delete_request = delete_request

    def build(self) -> DeleteRequest:
        return self._delete_request

    def dataset_id(self, dataset_id: str) -> DeleteRequestBuilder:
        self._delete_request.dataset_id = dataset_id
        self._delete_request.paths["dataset_id"] = dataset_id
        return self

    def document_id(self, document_id: str) -> DeleteRequestBuilder:
        self._delete_request.document_id = document_id
        self._delete_request.paths["document_id"] = document_id
        return self
