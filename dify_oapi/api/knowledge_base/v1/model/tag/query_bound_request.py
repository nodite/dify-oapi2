from __future__ import annotations

from dify_oapi.core.enum import HttpMethod
from dify_oapi.core.model.base_request import BaseRequest


class QueryBoundRequest(BaseRequest):
    def __init__(self):
        super().__init__()
        self.dataset_id: str | None = None

    @staticmethod
    def builder() -> QueryBoundRequestBuilder:
        return QueryBoundRequestBuilder()


class QueryBoundRequestBuilder:
    def __init__(self):
        query_bound_request = QueryBoundRequest()
        query_bound_request.http_method = HttpMethod.GET
        query_bound_request.uri = "/v1/datasets/:dataset_id/tags"
        self._request = query_bound_request

    def build(self) -> QueryBoundRequest:
        return self._request

    def dataset_id(self, dataset_id: str) -> QueryBoundRequestBuilder:
        self._request.dataset_id = dataset_id
        self._request.paths["dataset_id"] = dataset_id
        return self
