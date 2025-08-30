from dify_oapi.core.enum import HttpMethod
from dify_oapi.core.model.base_request import BaseRequest


class GetDatasetRequest(BaseRequest):
    def __init__(self) -> None:
        super().__init__()
        self.dataset_id: str | None = None

    @staticmethod
    def builder() -> "GetDatasetRequestBuilder":
        return GetDatasetRequestBuilder()


class GetDatasetRequestBuilder:
    def __init__(self) -> None:
        get_dataset_request = GetDatasetRequest()
        get_dataset_request.http_method = HttpMethod.GET
        get_dataset_request.uri = "/v1/datasets/:dataset_id"
        self._get_dataset_request = get_dataset_request

    def build(self) -> GetDatasetRequest:
        return self._get_dataset_request

    def dataset_id(self, dataset_id: str) -> "GetDatasetRequestBuilder":
        self._get_dataset_request.dataset_id = dataset_id
        self._get_dataset_request.paths["dataset_id"] = dataset_id
        return self
