from dify_oapi.core.enum import HttpMethod
from dify_oapi.core.model.base_request import BaseRequest


class ListDatasetsRequest(BaseRequest):
    def __init__(self) -> None:
        super().__init__()

    @staticmethod
    def builder() -> "ListDatasetsRequestBuilder":
        return ListDatasetsRequestBuilder()


class ListDatasetsRequestBuilder:
    def __init__(self) -> None:
        list_datasets_request = ListDatasetsRequest()
        list_datasets_request.http_method = HttpMethod.GET
        list_datasets_request.uri = "/v1/datasets"
        self._list_datasets_request = list_datasets_request

    def build(self) -> ListDatasetsRequest:
        return self._list_datasets_request

    def page(self, page: int) -> "ListDatasetsRequestBuilder":
        self._list_datasets_request.add_query("page", str(page))
        return self

    def limit(self, limit: int) -> "ListDatasetsRequestBuilder":
        self._list_datasets_request.add_query("limit", str(limit))
        return self
