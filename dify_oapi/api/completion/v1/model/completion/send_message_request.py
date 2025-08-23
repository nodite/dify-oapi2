from __future__ import annotations

from dify_oapi.core.enum import HttpMethod
from dify_oapi.core.model.base_request import BaseRequest

from .send_message_request_body import SendMessageRequestBody


class SendMessageRequest(BaseRequest):
    def __init__(self) -> None:
        super().__init__()
        self.request_body: SendMessageRequestBody | None = None

    @staticmethod
    def builder() -> SendMessageRequestBuilder:
        return SendMessageRequestBuilder()


class SendMessageRequestBuilder:
    def __init__(self) -> None:
        send_message_request = SendMessageRequest()
        send_message_request.http_method = HttpMethod.POST
        send_message_request.uri = "/v1/completion-messages"
        self._send_message_request: SendMessageRequest = send_message_request

    def request_body(self, request_body: SendMessageRequestBody) -> SendMessageRequestBuilder:
        self._send_message_request.request_body = request_body
        self._send_message_request.body = request_body.model_dump(exclude_none=True, mode="json")
        return self

    def build(self) -> SendMessageRequest:
        return self._send_message_request
