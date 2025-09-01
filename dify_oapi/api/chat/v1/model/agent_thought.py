"""Agent thought model for Chat API."""

from __future__ import annotations

from pydantic import BaseModel, Field


class AgentThought(BaseModel):
    """Agent thought model."""

    id: str | None = Field(None, description="Agent thought ID")
    message_id: str | None = Field(None, description="Message ID")
    position: int | None = Field(None, description="Position")
    thought: str | None = Field(None, description="Agent thought")
    observation: str | None = Field(None, description="Observation")
    tool: str | None = Field(None, description="Tool used")
    tool_input: str | None = Field(None, description="Tool input")
    message_files: list[str] | None = Field(None, description="Message file IDs")
    created_at: int | None = Field(None, description="Creation timestamp")

    @classmethod
    def builder(cls) -> AgentThoughtBuilder:
        """Create an AgentThought builder."""
        return AgentThoughtBuilder()


class AgentThoughtBuilder:
    """Builder for AgentThought."""

    def __init__(self) -> None:
        self._agent_thought = AgentThought()

    def id(self, id: str) -> AgentThoughtBuilder:
        """Set agent thought ID."""
        self._agent_thought.id = id
        return self

    def message_id(self, message_id: str) -> AgentThoughtBuilder:
        """Set message ID."""
        self._agent_thought.message_id = message_id
        return self

    def position(self, position: int) -> AgentThoughtBuilder:
        """Set position."""
        self._agent_thought.position = position
        return self

    def thought(self, thought: str) -> AgentThoughtBuilder:
        """Set agent thought."""
        self._agent_thought.thought = thought
        return self

    def observation(self, observation: str) -> AgentThoughtBuilder:
        """Set observation."""
        self._agent_thought.observation = observation
        return self

    def tool(self, tool: str) -> AgentThoughtBuilder:
        """Set tool used."""
        self._agent_thought.tool = tool
        return self

    def tool_input(self, tool_input: str) -> AgentThoughtBuilder:
        """Set tool input."""
        self._agent_thought.tool_input = tool_input
        return self

    def message_files(self, message_files: list[str]) -> AgentThoughtBuilder:
        """Set message file IDs."""
        self._agent_thought.message_files = message_files
        return self

    def created_at(self, created_at: int) -> AgentThoughtBuilder:
        """Set creation timestamp."""
        self._agent_thought.created_at = created_at
        return self

    def build(self) -> AgentThought:
        """Build the AgentThought instance."""
        return self._agent_thought
