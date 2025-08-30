from __future__ import annotations

from dify_oapi.core.enum import HttpMethod
from dify_oapi.core.model.base_request import BaseRequest


class GetParametersRequest(BaseRequest):
    def __init__(self):
        super().__init__()

    @staticmethod
    def builder() -> GetParametersRequestBuilder:
        return GetParametersRequestBuilder()


class GetParametersRequestBuilder:
    def __init__(self):
        get_parameters_request = GetParametersRequest()
        get_parameters_request.http_method = HttpMethod.GET
        get_parameters_request.uri = "/v1/parameters"
        self._get_parameters_request = get_parameters_request

    def build(self) -> GetParametersRequest:
        return self._get_parameters_request
