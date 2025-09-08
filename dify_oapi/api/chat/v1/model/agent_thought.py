"""Agent thought model for Chat API."""

from __future__ import annotations

from pydantic import BaseModel


class AgentThought(BaseModel):
    """Agent thought model."""

    id: str | None = None
    message_id: str | None = None
    position: int | None = None
    thought: str | None = None
    observation: str | None = None
    tool: str | None = None
    tool_input: str | None = None
    message_files: list[str] | None = None
    created_at: int | None = None

    @staticmethod
    def builder() -> AgentThoughtBuilder:
        return AgentThoughtBuilder()


class AgentThoughtBuilder:
    """Builder for AgentThought."""

    def __init__(self):
        self._agent_thought = AgentThought()

    def build(self) -> AgentThought:
        return self._agent_thought

    def id(self, id: str) -> AgentThoughtBuilder:
        self._agent_thought.id = id
        return self

    def message_id(self, message_id: str) -> AgentThoughtBuilder:
        self._agent_thought.message_id = message_id
        return self

    def position(self, position: int) -> AgentThoughtBuilder:
        self._agent_thought.position = position
        return self

    def thought(self, thought: str) -> AgentThoughtBuilder:
        self._agent_thought.thought = thought
        return self

    def observation(self, observation: str) -> AgentThoughtBuilder:
        self._agent_thought.observation = observation
        return self

    def tool(self, tool: str) -> AgentThoughtBuilder:
        self._agent_thought.tool = tool
        return self

    def tool_input(self, tool_input: str) -> AgentThoughtBuilder:
        self._agent_thought.tool_input = tool_input
        return self

    def message_files(self, message_files: list[str]) -> AgentThoughtBuilder:
        self._agent_thought.message_files = message_files
        return self

    def created_at(self, created_at: int) -> AgentThoughtBuilder:
        self._agent_thought.created_at = created_at
        return self
