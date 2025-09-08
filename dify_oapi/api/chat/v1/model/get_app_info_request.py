from __future__ import annotations

from dify_oapi.core.enum import HttpMethod
from dify_oapi.core.model.base_request import BaseRequest


class GetAppInfoRequest(BaseRequest):
    def __init__(self):
        super().__init__()

    @staticmethod
    def builder() -> GetAppInfoRequestBuilder:
        return GetAppInfoRequestBuilder()


class GetAppInfoRequestBuilder:
    def __init__(self):
        get_app_info_request = GetAppInfoRequest()
        get_app_info_request.http_method = HttpMethod.GET
        get_app_info_request.uri = "/v1/info"
        self._get_app_info_request = get_app_info_request

    def build(self) -> GetAppInfoRequest:
        return self._get_app_info_request
