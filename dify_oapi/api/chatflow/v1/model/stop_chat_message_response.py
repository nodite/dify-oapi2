from dify_oapi.core.model.base_response import BaseResponse


class StopChatMessageResponse(BaseResponse):
    result: str | None = None
