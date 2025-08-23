from __future__ import annotations

from dify_oapi.core.model.base_response import BaseResponse

from .completion_message_info import CompletionMessageInfo


class SendMessageResponse(CompletionMessageInfo, BaseResponse):
    pass
