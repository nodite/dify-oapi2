from __future__ import annotations

from dify_oapi.core.model.base_response import BaseResponse

from .app_info import AppInfo


class GetInfoResponse(AppInfo, BaseResponse):
    pass
