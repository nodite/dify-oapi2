"""Update status request model for document API."""

from __future__ import annotations

from dify_oapi.core.enum import HttpMethod
from dify_oapi.core.model.base_request import BaseRequest

from .update_status_request_body import UpdateStatusRequestBody


class UpdateStatusRequest(BaseRequest):
    """Request model for updating document status."""

    def __init__(self) -> None:
        super().__init__()
        self.dataset_id: str | None = None
        self.action: str | None = None
        self.request_body: UpdateStatusRequestBody | None = None

    @staticmethod
    def builder() -> UpdateStatusRequestBuilder:
        """Create a new UpdateStatusRequestBuilder instance."""
        return UpdateStatusRequestBuilder()


class UpdateStatusRequestBuilder:
    """Builder for UpdateStatusRequest."""

    def __init__(self) -> None:
        update_status_request = UpdateStatusRequest()
        update_status_request.http_method = HttpMethod.PATCH
        update_status_request.uri = "/v1/datasets/:dataset_id/documents/status/:action"
        self._update_status_request = update_status_request

    def build(self) -> UpdateStatusRequest:
        """Build the UpdateStatusRequest instance."""
        return self._update_status_request

    def dataset_id(self, dataset_id: str) -> UpdateStatusRequestBuilder:
        """Set the dataset ID."""
        self._update_status_request.dataset_id = dataset_id
        self._update_status_request.paths["dataset_id"] = dataset_id
        return self

    def action(self, action: str) -> UpdateStatusRequestBuilder:
        """Set the action."""
        self._update_status_request.action = action
        self._update_status_request.paths["action"] = action
        return self

    def request_body(self, request_body: UpdateStatusRequestBody) -> UpdateStatusRequestBuilder:
        """Set the request body."""
        self._update_status_request.request_body = request_body
        self._update_status_request.body = request_body.model_dump(exclude_none=True, mode="json")
        return self
