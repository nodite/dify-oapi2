from dify_oapi.core.model.base_response import BaseResponse

from .webapp_settings import WebAppSettings


class GetSiteResponse(WebAppSettings, BaseResponse):
    pass
