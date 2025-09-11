from dify_oapi.core.model.base_response import BaseResponse

from .chat_message import ChatMessage


class SendChatMessageResponse(ChatMessage, BaseResponse):
    pass
