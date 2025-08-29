from __future__ import annotations

from dify_oapi.core.enum import HttpMethod
from dify_oapi.core.model.base_request import BaseRequest


class ListRequest(BaseRequest):
    def __init__(self):
        super().__init__()

    @staticmethod
    def builder() -> ListRequestBuilder:
        return ListRequestBuilder()


class ListRequestBuilder:
    def __init__(self):
        list_request = ListRequest()
        list_request.http_method = HttpMethod.GET
        list_request.uri = "/v1/datasets/tags"
        self._request = list_request

    def build(self) -> ListRequest:
        return self._request
