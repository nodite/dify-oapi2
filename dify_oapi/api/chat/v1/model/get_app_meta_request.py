from __future__ import annotations

from dify_oapi.core.enum import HttpMethod
from dify_oapi.core.model.base_request import BaseRequest


class GetAppMetaRequest(BaseRequest):
    def __init__(self):
        super().__init__()

    @staticmethod
    def builder() -> GetAppMetaRequestBuilder:
        return GetAppMetaRequestBuilder()


class GetAppMetaRequestBuilder:
    def __init__(self):
        get_app_meta_request = GetAppMetaRequest()
        get_app_meta_request.http_method = HttpMethod.GET
        get_app_meta_request.uri = "/v1/meta"
        self._get_app_meta_request = get_app_meta_request

    def build(self) -> GetAppMetaRequest:
        return self._get_app_meta_request
