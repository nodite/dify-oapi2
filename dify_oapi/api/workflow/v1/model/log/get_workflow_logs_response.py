from __future__ import annotations

from dify_oapi.core.model.base_response import BaseResponse

from .log_info import LogInfo


class GetWorkflowLogsResponse(BaseResponse):
    page: int | None = None
    limit: int | None = None
    total: int | None = None
    has_more: bool | None = None
    data: list[LogInfo] | None = None
