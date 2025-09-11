from dify_oapi.core.model.base_response import BaseResponse


class DeleteConversationResponse(BaseResponse):
    """Response for delete conversation operation (No Content - 204)."""

    @staticmethod
    def builder() -> "DeleteConversationResponseBuilder":
        return DeleteConversationResponseBuilder()


class DeleteConversationResponseBuilder:
    def __init__(self):
        self._delete_conversation_response = DeleteConversationResponse()

    def build(self) -> DeleteConversationResponse:
        return self._delete_conversation_response
