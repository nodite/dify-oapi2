from __future__ import annotations

from dify_oapi.api.chat.v1.model.message_info import MessageInfo
from dify_oapi.core.model.base_response import BaseResponse


class GetMessageHistoryResponse(BaseResponse):
    limit: int | None = None
    has_more: bool | None = None
    data: list[MessageInfo] | None = None
