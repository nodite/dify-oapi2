from __future__ import annotations

from dify_oapi.core.model.base_response import BaseResponse

from .site_info import SiteInfo


class GetSiteResponse(SiteInfo, BaseResponse):
    pass
