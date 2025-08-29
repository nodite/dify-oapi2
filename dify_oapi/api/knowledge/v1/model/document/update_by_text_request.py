"""Update document by text request model."""

from __future__ import annotations

from dify_oapi.core.enum import HttpMethod
from dify_oapi.core.model.base_request import BaseRequest

from .update_by_text_request_body import UpdateByTextRequestBody


class UpdateByTextRequest(BaseRequest):
    """Request model for updating document by text."""

    def __init__(self) -> None:
        super().__init__()
        self.dataset_id: str | None = None
        self.document_id: str | None = None
        self.request_body: UpdateByTextRequestBody | None = None

    @staticmethod
    def builder() -> UpdateByTextRequestBuilder:
        """Create a new UpdateByTextRequestBuilder instance."""
        return UpdateByTextRequestBuilder()


class UpdateByTextRequestBuilder:
    """Builder for UpdateByTextRequest."""

    def __init__(self) -> None:
        update_by_text_request = UpdateByTextRequest()
        update_by_text_request.http_method = HttpMethod.POST
        update_by_text_request.uri = "/v1/datasets/:dataset_id/documents/:document_id/update-by-text"
        self._update_by_text_request = update_by_text_request

    def build(self) -> UpdateByTextRequest:
        """Build the UpdateByTextRequest instance."""
        return self._update_by_text_request

    def dataset_id(self, dataset_id: str) -> UpdateByTextRequestBuilder:
        """Set the dataset ID."""
        self._update_by_text_request.dataset_id = dataset_id
        self._update_by_text_request.paths["dataset_id"] = dataset_id
        return self

    def document_id(self, document_id: str) -> UpdateByTextRequestBuilder:
        """Set the document ID."""
        self._update_by_text_request.document_id = document_id
        self._update_by_text_request.paths["document_id"] = document_id
        return self

    def request_body(self, request_body: UpdateByTextRequestBody) -> UpdateByTextRequestBuilder:
        """Set the request body."""
        self._update_by_text_request.request_body = request_body
        self._update_by_text_request.body = request_body.model_dump(exclude_none=True, mode="json")
        return self
