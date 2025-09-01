"""Conversation variable model for Chat API."""

from __future__ import annotations

from pydantic import BaseModel, Field

from .chat_types import VariableValueType


class ConversationVariable(BaseModel):
    """Conversation variable model."""

    id: str | None = Field(None, description="Variable ID")
    name: str | None = Field(None, description="Variable name")
    value_type: VariableValueType | None = Field(None, description="Variable value type")
    value: str | None = Field(None, description="Variable value")
    description: str | None = Field(None, description="Variable description")
    created_at: int | None = Field(None, description="Creation timestamp")
    updated_at: int | None = Field(None, description="Update timestamp")

    @classmethod
    def builder(cls) -> ConversationVariableBuilder:
        """Create a ConversationVariable builder."""
        return ConversationVariableBuilder()


class ConversationVariableBuilder:
    """Builder for ConversationVariable."""

    def __init__(self) -> None:
        self._conversation_variable = ConversationVariable()

    def id(self, id: str) -> ConversationVariableBuilder:
        """Set variable ID."""
        self._conversation_variable.id = id
        return self

    def name(self, name: str) -> ConversationVariableBuilder:
        """Set variable name."""
        self._conversation_variable.name = name
        return self

    def value_type(self, value_type: VariableValueType) -> ConversationVariableBuilder:
        """Set variable value type."""
        self._conversation_variable.value_type = value_type
        return self

    def value(self, value: str) -> ConversationVariableBuilder:
        """Set variable value."""
        self._conversation_variable.value = value
        return self

    def description(self, description: str) -> ConversationVariableBuilder:
        """Set variable description."""
        self._conversation_variable.description = description
        return self

    def created_at(self, created_at: int) -> ConversationVariableBuilder:
        """Set creation timestamp."""
        self._conversation_variable.created_at = created_at
        return self

    def updated_at(self, updated_at: int) -> ConversationVariableBuilder:
        """Set update timestamp."""
        self._conversation_variable.updated_at = updated_at
        return self

    def build(self) -> ConversationVariable:
        """Build the ConversationVariable instance."""
        return self._conversation_variable
