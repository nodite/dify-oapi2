from dify_oapi.core.enum import HttpMethod
from dify_oapi.core.model.base_request import BaseRequest

from .retrieve_from_dataset_request_body import RetrieveFromDatasetRequestBody


class RetrieveFromDatasetRequest(BaseRequest):
    def __init__(self) -> None:
        super().__init__()
        self.dataset_id: str | None = None
        self.request_body: RetrieveFromDatasetRequestBody | None = None

    @staticmethod
    def builder() -> "RetrieveFromDatasetRequestBuilder":
        return RetrieveFromDatasetRequestBuilder()


class RetrieveFromDatasetRequestBuilder:
    def __init__(self) -> None:
        retrieve_from_dataset_request = RetrieveFromDatasetRequest()
        retrieve_from_dataset_request.http_method = HttpMethod.POST
        retrieve_from_dataset_request.uri = "/v1/datasets/:dataset_id/retrieve"
        self._retrieve_from_dataset_request = retrieve_from_dataset_request

    def build(self) -> RetrieveFromDatasetRequest:
        return self._retrieve_from_dataset_request

    def dataset_id(self, dataset_id: str) -> "RetrieveFromDatasetRequestBuilder":
        self._retrieve_from_dataset_request.dataset_id = dataset_id
        self._retrieve_from_dataset_request.paths["dataset_id"] = dataset_id
        return self

    def request_body(self, request_body: RetrieveFromDatasetRequestBody) -> "RetrieveFromDatasetRequestBuilder":
        self._retrieve_from_dataset_request.request_body = request_body
        self._retrieve_from_dataset_request.body = request_body.model_dump(exclude_none=True, mode="json")
        return self
