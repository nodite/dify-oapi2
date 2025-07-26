from __future__ import annotations

from dify_oapi.core.enum import HttpMethod
from dify_oapi.core.model.base_request import BaseRequest


class QueryBoundTagsRequest(BaseRequest):
    def __init__(self):
        super().__init__()
        self.dataset_id: str | None = None

    @staticmethod
    def builder() -> QueryBoundTagsRequestBuilder:
        return QueryBoundTagsRequestBuilder()


class QueryBoundTagsRequestBuilder:
    def __init__(self):
        query_bound_tags_request = QueryBoundTagsRequest()
        query_bound_tags_request.http_method = HttpMethod.POST
        query_bound_tags_request.uri = "/v1/datasets/:dataset_id/tags"
        self._request = query_bound_tags_request

    def build(self) -> QueryBoundTagsRequest:
        return self._request

    def dataset_id(self, dataset_id: str) -> QueryBoundTagsRequestBuilder:
        self._request.dataset_id = dataset_id
        self._request.paths["dataset_id"] = dataset_id
        return self