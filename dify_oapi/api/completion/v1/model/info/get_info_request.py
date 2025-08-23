from __future__ import annotations

from dify_oapi.core.enum import HttpMethod
from dify_oapi.core.model.base_request import BaseRequest


class GetInfoRequest(BaseRequest):
    def __init__(self):
        super().__init__()

    @staticmethod
    def builder() -> GetInfoRequestBuilder:
        return GetInfoRequestBuilder()


class GetInfoRequestBuilder:
    def __init__(self):
        get_info_request = GetInfoRequest()
        get_info_request.http_method = HttpMethod.GET
        get_info_request.uri = "/v1/info"
        self._get_info_request = get_info_request

    def build(self) -> GetInfoRequest:
        return self._get_info_request
