from pydantic import BaseModel

from .chatflow_types import VariableValueType


class ConversationVariable(BaseModel):
    """Conversation variable model."""

    id: str | None = None
    name: str | None = None
    value_type: VariableValueType | None = None
    value: str | None = None
    description: str | None = None
    created_at: int | None = None
    updated_at: int | None = None

    @staticmethod
    def builder() -> "ConversationVariableBuilder":
        return ConversationVariableBuilder()


class ConversationVariableBuilder:
    def __init__(self):
        self._conversation_variable = ConversationVariable()

    def build(self) -> ConversationVariable:
        return self._conversation_variable

    def id(self, id: str) -> "ConversationVariableBuilder":
        self._conversation_variable.id = id
        return self

    def name(self, name: str) -> "ConversationVariableBuilder":
        self._conversation_variable.name = name
        return self

    def value_type(self, value_type: VariableValueType) -> "ConversationVariableBuilder":
        self._conversation_variable.value_type = value_type
        return self

    def value(self, value: str) -> "ConversationVariableBuilder":
        self._conversation_variable.value = value
        return self

    def description(self, description: str) -> "ConversationVariableBuilder":
        self._conversation_variable.description = description
        return self

    def created_at(self, created_at: int) -> "ConversationVariableBuilder":
        self._conversation_variable.created_at = created_at
        return self

    def updated_at(self, updated_at: int) -> "ConversationVariableBuilder":
        self._conversation_variable.updated_at = updated_at
        return self
