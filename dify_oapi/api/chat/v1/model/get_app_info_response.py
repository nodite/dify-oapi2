from dify_oapi.core.model.base_response import BaseResponse

from .app_info import AppInfo


class GetAppInfoResponse(AppInfo, BaseResponse):
    """Response for get application basic information API."""

    pass
