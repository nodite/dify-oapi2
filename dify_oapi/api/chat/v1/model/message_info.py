"""Message information model for Chat API."""

from typing import Any

from pydantic import BaseModel, Field

from .agent_thought import AgentThought
from .feedback_info import FeedbackInfo
from .message_file import MessageFile
from .retriever_resource import RetrieverResource


class MessageInfo(BaseModel):
    """Message information model."""

    id: str | None = Field(None, description="Message ID")
    conversation_id: str | None = Field(None, description="Conversation ID")
    inputs: dict[str, Any] | None = Field(None, description="Input parameters")
    query: str | None = Field(None, description="User query")
    answer: str | None = Field(None, description="Assistant answer")
    message_files: list[MessageFile] | None = Field(None, description="Message files")
    feedback: FeedbackInfo | None = Field(None, description="Message feedback")
    retriever_resources: list[RetrieverResource] | None = Field(None, description="Retriever resources")
    agent_thoughts: list[AgentThought] | None = Field(None, description="Agent thoughts")
    created_at: int | None = Field(None, description="Creation timestamp")

    @classmethod
    def builder(cls) -> "MessageInfoBuilder":
        """Create a MessageInfo builder."""
        return MessageInfoBuilder()


class MessageInfoBuilder:
    """Builder for MessageInfo."""

    def __init__(self) -> None:
        self._message_info = MessageInfo()

    def id(self, id: str) -> "MessageInfoBuilder":
        """Set message ID."""
        self._message_info.id = id
        return self

    def conversation_id(self, conversation_id: str) -> "MessageInfoBuilder":
        """Set conversation ID."""
        self._message_info.conversation_id = conversation_id
        return self

    def inputs(self, inputs: dict[str, Any]) -> "MessageInfoBuilder":
        """Set input parameters."""
        self._message_info.inputs = inputs
        return self

    def query(self, query: str) -> "MessageInfoBuilder":
        """Set user query."""
        self._message_info.query = query
        return self

    def answer(self, answer: str) -> "MessageInfoBuilder":
        """Set assistant answer."""
        self._message_info.answer = answer
        return self

    def message_files(self, message_files: list[MessageFile]) -> "MessageInfoBuilder":
        """Set message files."""
        self._message_info.message_files = message_files
        return self

    def feedback(self, feedback: FeedbackInfo) -> "MessageInfoBuilder":
        """Set message feedback."""
        self._message_info.feedback = feedback
        return self

    def retriever_resources(self, retriever_resources: list[RetrieverResource]) -> "MessageInfoBuilder":
        """Set retriever resources."""
        self._message_info.retriever_resources = retriever_resources
        return self

    def agent_thoughts(self, agent_thoughts: list[AgentThought]) -> "MessageInfoBuilder":
        """Set agent thoughts."""
        self._message_info.agent_thoughts = agent_thoughts
        return self

    def created_at(self, created_at: int) -> "MessageInfoBuilder":
        """Set creation timestamp."""
        self._message_info.created_at = created_at
        return self

    def build(self) -> MessageInfo:
        """Build the MessageInfo instance."""
        return self._message_info
