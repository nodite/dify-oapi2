from typing import Any

from pydantic import BaseModel

from .agent_thought import AgentThought
from .feedback_info import FeedbackInfo
from .message_file import MessageFile
from .retriever_resource import RetrieverResource


class MessageInfo(BaseModel):
    id: str | None = None
    conversation_id: str | None = None
    inputs: dict[str, Any] | None = None
    query: str | None = None
    answer: str | None = None
    message_files: list[MessageFile] | None = None
    feedback: FeedbackInfo | None = None
    retriever_resources: list[RetrieverResource] | None = None
    agent_thoughts: list[AgentThought] | None = None
    created_at: int | None = None

    @staticmethod
    def builder() -> "MessageInfoBuilder":
        return MessageInfoBuilder()


class MessageInfoBuilder:
    def __init__(self):
        self._message_info = MessageInfo()

    def id(self, id: str) -> "MessageInfoBuilder":
        self._message_info.id = id
        return self

    def conversation_id(self, conversation_id: str) -> "MessageInfoBuilder":
        self._message_info.conversation_id = conversation_id
        return self

    def inputs(self, inputs: dict[str, Any]) -> "MessageInfoBuilder":
        self._message_info.inputs = inputs
        return self

    def query(self, query: str) -> "MessageInfoBuilder":
        self._message_info.query = query
        return self

    def answer(self, answer: str) -> "MessageInfoBuilder":
        self._message_info.answer = answer
        return self

    def message_files(self, message_files: list[MessageFile]) -> "MessageInfoBuilder":
        self._message_info.message_files = message_files
        return self

    def feedback(self, feedback: FeedbackInfo) -> "MessageInfoBuilder":
        self._message_info.feedback = feedback
        return self

    def retriever_resources(self, retriever_resources: list[RetrieverResource]) -> "MessageInfoBuilder":
        self._message_info.retriever_resources = retriever_resources
        return self

    def agent_thoughts(self, agent_thoughts: list[AgentThought]) -> "MessageInfoBuilder":
        self._message_info.agent_thoughts = agent_thoughts
        return self

    def created_at(self, created_at: int) -> "MessageInfoBuilder":
        self._message_info.created_at = created_at
        return self

    def build(self) -> MessageInfo:
        return self._message_info
