from dify_oapi.core.enum import HttpMethod
from dify_oapi.core.model.base_request import BaseRequest

from .update_dataset_request_body import UpdateDatasetRequestBody


class UpdateDatasetRequest(BaseRequest):
    def __init__(self) -> None:
        super().__init__()
        self.dataset_id: str | None = None
        self.request_body: UpdateDatasetRequestBody | None = None

    @staticmethod
    def builder() -> "UpdateDatasetRequestBuilder":
        return UpdateDatasetRequestBuilder()


class UpdateDatasetRequestBuilder:
    def __init__(self) -> None:
        update_dataset_request = UpdateDatasetRequest()
        update_dataset_request.http_method = HttpMethod.PATCH
        update_dataset_request.uri = "/v1/datasets/:dataset_id"
        self._update_dataset_request = update_dataset_request

    def build(self) -> UpdateDatasetRequest:
        return self._update_dataset_request

    def dataset_id(self, dataset_id: str) -> "UpdateDatasetRequestBuilder":
        self._update_dataset_request.dataset_id = dataset_id
        self._update_dataset_request.paths["dataset_id"] = dataset_id
        return self

    def request_body(self, request_body: UpdateDatasetRequestBody) -> "UpdateDatasetRequestBuilder":
        self._update_dataset_request.request_body = request_body
        self._update_dataset_request.body = request_body.model_dump(exclude_none=True, mode="json")
        return self
