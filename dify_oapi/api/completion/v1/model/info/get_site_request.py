from __future__ import annotations

from dify_oapi.core.enum import HttpMethod
from dify_oapi.core.model.base_request import BaseRequest


class GetSiteRequest(BaseRequest):
    def __init__(self):
        super().__init__()

    @staticmethod
    def builder() -> GetSiteRequestBuilder:
        return GetSiteRequestBuilder()


class GetSiteRequestBuilder:
    def __init__(self):
        get_site_request = GetSiteRequest()
        get_site_request.http_method = HttpMethod.GET
        get_site_request.uri = "/v1/site"
        self._get_site_request = get_site_request

    def build(self) -> GetSiteRequest:
        return self._get_site_request
