from __future__ import annotations

from dify_oapi.core.enum import HttpMethod
from dify_oapi.core.model.base_request import BaseRequest


class GetAppParametersRequest(BaseRequest):
    def __init__(self):
        super().__init__()

    @staticmethod
    def builder() -> GetAppParametersRequestBuilder:
        return GetAppParametersRequestBuilder()


class GetAppParametersRequestBuilder:
    def __init__(self):
        get_app_parameters_request = GetAppParametersRequest()
        get_app_parameters_request.http_method = HttpMethod.GET
        get_app_parameters_request.uri = "/v1/parameters"
        self._get_app_parameters_request = get_app_parameters_request

    def build(self) -> GetAppParametersRequest:
        return self._get_app_parameters_request

    def user(self, user: str) -> GetAppParametersRequestBuilder:
        self._get_app_parameters_request.add_query("user", user)
        return self
