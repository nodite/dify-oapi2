from dify_oapi.core.model.base_response import BaseResponse

from .site_settings import SiteSettings


class GetSiteSettingsResponse(SiteSettings, BaseResponse):
    """Response for get site settings API."""

    pass
