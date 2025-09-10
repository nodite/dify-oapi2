from dify_oapi.core.model.base_response import BaseResponse


class RenameConversationResponse(BaseResponse):
    """Response for rename conversation operation with updated conversation info."""

    id: str | None = None
    name: str | None = None
    inputs: dict[str, str] | None = None
    status: str | None = None
    introduction: str | None = None
    created_at: int | None = None
    updated_at: int | None = None

    @staticmethod
    def builder() -> "RenameConversationResponseBuilder":
        return RenameConversationResponseBuilder()


class RenameConversationResponseBuilder:
    def __init__(self):
        self._rename_conversation_response = RenameConversationResponse()

    def build(self) -> RenameConversationResponse:
        return self._rename_conversation_response

    def id(self, id: str) -> "RenameConversationResponseBuilder":
        self._rename_conversation_response.id = id
        return self

    def name(self, name: str) -> "RenameConversationResponseBuilder":
        self._rename_conversation_response.name = name
        return self

    def inputs(self, inputs: dict[str, str]) -> "RenameConversationResponseBuilder":
        self._rename_conversation_response.inputs = inputs
        return self

    def status(self, status: str) -> "RenameConversationResponseBuilder":
        self._rename_conversation_response.status = status
        return self

    def introduction(self, introduction: str) -> "RenameConversationResponseBuilder":
        self._rename_conversation_response.introduction = introduction
        return self

    def created_at(self, created_at: int) -> "RenameConversationResponseBuilder":
        self._rename_conversation_response.created_at = created_at
        return self

    def updated_at(self, updated_at: int) -> "RenameConversationResponseBuilder":
        self._rename_conversation_response.updated_at = updated_at
        return self
