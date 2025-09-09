from pydantic import BaseModel


class DeleteConversationRequestBody(BaseModel):
    user: str | None = None

    @staticmethod
    def builder() -> "DeleteConversationRequestBodyBuilder":
        return DeleteConversationRequestBodyBuilder()


class DeleteConversationRequestBodyBuilder:
    def __init__(self):
        self._delete_conversation_request_body = DeleteConversationRequestBody()

    def build(self) -> DeleteConversationRequestBody:
        return self._delete_conversation_request_body

    def user(self, user: str) -> "DeleteConversationRequestBodyBuilder":
        self._delete_conversation_request_body.user = user
        return self
