from __future__ import annotations

from dify_oapi.core.enum import HttpMethod
from dify_oapi.core.model.base_request import BaseRequest


class GetSiteSettingsRequest(BaseRequest):
    def __init__(self):
        super().__init__()

    @staticmethod
    def builder() -> GetSiteSettingsRequestBuilder:
        return GetSiteSettingsRequestBuilder()


class GetSiteSettingsRequestBuilder:
    def __init__(self):
        get_site_settings_request = GetSiteSettingsRequest()
        get_site_settings_request.http_method = HttpMethod.GET
        get_site_settings_request.uri = "/v1/site"
        self._get_site_settings_request = get_site_settings_request

    def build(self) -> GetSiteSettingsRequest:
        return self._get_site_settings_request
