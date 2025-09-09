from dify_oapi.core.enum import HttpMethod
from dify_oapi.core.model.base_request import BaseRequest

from .send_chat_message_request_body import SendChatMessageRequestBody


class SendChatMessageRequest(BaseRequest):
    def __init__(self):
        super().__init__()
        self.request_body: SendChatMessageRequestBody | None = None

    @staticmethod
    def builder() -> "SendChatMessageRequestBuilder":
        return SendChatMessageRequestBuilder()


class SendChatMessageRequestBuilder:
    def __init__(self):
        send_chat_message_request = SendChatMessageRequest()
        send_chat_message_request.http_method = HttpMethod.POST
        send_chat_message_request.uri = "/v1/chat-messages"
        self._send_chat_message_request = send_chat_message_request

    def build(self) -> SendChatMessageRequest:
        return self._send_chat_message_request

    def request_body(self, request_body: SendChatMessageRequestBody) -> "SendChatMessageRequestBuilder":
        self._send_chat_message_request.request_body = request_body
        self._send_chat_message_request.body = request_body.model_dump(exclude_none=True, mode="json")
        return self
