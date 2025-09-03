from __future__ import annotations

from dify_oapi.api.chat.v1.model.conversation_info import ConversationInfo
from dify_oapi.core.model.base_response import BaseResponse


class GetConversationsResponse(BaseResponse):
    limit: int | None = None
    has_more: bool | None = None
    data: list[ConversationInfo] | None = None
