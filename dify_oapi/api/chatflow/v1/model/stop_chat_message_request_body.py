from pydantic import BaseModel


class StopChatMessageRequestBody(BaseModel):
    user: str | None = None

    @staticmethod
    def builder() -> "StopChatMessageRequestBodyBuilder":
        return StopChatMessageRequestBodyBuilder()


class StopChatMessageRequestBodyBuilder:
    def __init__(self):
        self._stop_chat_message_request_body = StopChatMessageRequestBody()

    def build(self) -> StopChatMessageRequestBody:
        return self._stop_chat_message_request_body

    def user(self, user: str) -> "StopChatMessageRequestBodyBuilder":
        self._stop_chat_message_request_body.user = user
        return self
