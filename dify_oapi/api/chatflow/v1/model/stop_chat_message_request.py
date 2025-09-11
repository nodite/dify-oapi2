from dify_oapi.core.enum import HttpMethod
from dify_oapi.core.model.base_request import BaseRequest

from .stop_chat_message_request_body import StopChatMessageRequestBody


class StopChatMessageRequest(BaseRequest):
    def __init__(self):
        super().__init__()
        self.request_body: StopChatMessageRequestBody | None = None
        self.task_id: str | None = None

    @staticmethod
    def builder() -> "StopChatMessageRequestBuilder":
        return StopChatMessageRequestBuilder()


class StopChatMessageRequestBuilder:
    def __init__(self):
        stop_chat_message_request = StopChatMessageRequest()
        stop_chat_message_request.http_method = HttpMethod.POST
        stop_chat_message_request.uri = "/v1/chat-messages/:task_id/stop"
        self._stop_chat_message_request = stop_chat_message_request

    def build(self) -> StopChatMessageRequest:
        return self._stop_chat_message_request

    def task_id(self, task_id: str) -> "StopChatMessageRequestBuilder":
        self._stop_chat_message_request.task_id = task_id
        self._stop_chat_message_request.paths["task_id"] = task_id
        return self

    def request_body(self, request_body: StopChatMessageRequestBody) -> "StopChatMessageRequestBuilder":
        self._stop_chat_message_request.request_body = request_body
        self._stop_chat_message_request.body = request_body.model_dump(exclude_none=True, mode="json")
        return self
