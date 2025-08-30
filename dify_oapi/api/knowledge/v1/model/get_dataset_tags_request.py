from dify_oapi.core.enum import HttpMethod
from dify_oapi.core.model.base_request import BaseRequest


class GetDatasetTagsRequest(BaseRequest):
    def __init__(self) -> None:
        super().__init__()
        self.dataset_id: str | None = None

    @staticmethod
    def builder() -> "GetDatasetTagsRequestBuilder":
        return GetDatasetTagsRequestBuilder()


class GetDatasetTagsRequestBuilder:
    def __init__(self) -> None:
        get_dataset_tags_request = GetDatasetTagsRequest()
        get_dataset_tags_request.http_method = HttpMethod.GET
        get_dataset_tags_request.uri = "/v1/datasets/:dataset_id/tags"
        self._get_dataset_tags_request = get_dataset_tags_request

    def build(self) -> GetDatasetTagsRequest:
        return self._get_dataset_tags_request

    def dataset_id(self, dataset_id: str) -> "GetDatasetTagsRequestBuilder":
        self._get_dataset_tags_request.dataset_id = dataset_id
        self._get_dataset_tags_request.paths["dataset_id"] = dataset_id
        return self
