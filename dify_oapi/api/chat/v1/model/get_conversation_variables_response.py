from __future__ import annotations

from dify_oapi.api.chat.v1.model.conversation_variable import ConversationVariable
from dify_oapi.core.model.base_response import BaseResponse


class GetConversationVariablesResponse(BaseResponse):
    limit: int | None = None
    has_more: bool | None = None
    data: list[ConversationVariable] | None = None
