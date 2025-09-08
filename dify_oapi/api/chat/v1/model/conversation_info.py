from __future__ import annotations

from typing import Any

from pydantic import BaseModel

from .chat_types import ConversationStatus


class ConversationInfo(BaseModel):
    id: str | None = None
    name: str | None = None
    inputs: dict[str, Any] | None = None
    status: ConversationStatus | None = None
    introduction: str | None = None
    created_at: int | None = None
    updated_at: int | None = None

    @staticmethod
    def builder() -> ConversationInfoBuilder:
        return ConversationInfoBuilder()


class ConversationInfoBuilder:
    def __init__(self):
        self._conversation_info = ConversationInfo()

    def id(self, id: str) -> ConversationInfoBuilder:
        self._conversation_info.id = id
        return self

    def name(self, name: str) -> ConversationInfoBuilder:
        self._conversation_info.name = name
        return self

    def inputs(self, inputs: dict[str, Any]) -> ConversationInfoBuilder:
        self._conversation_info.inputs = inputs
        return self

    def status(self, status: ConversationStatus) -> ConversationInfoBuilder:
        self._conversation_info.status = status
        return self

    def introduction(self, introduction: str) -> ConversationInfoBuilder:
        self._conversation_info.introduction = introduction
        return self

    def created_at(self, created_at: int) -> ConversationInfoBuilder:
        self._conversation_info.created_at = created_at
        return self

    def updated_at(self, updated_at: int) -> ConversationInfoBuilder:
        self._conversation_info.updated_at = updated_at
        return self

    def build(self) -> ConversationInfo:
        return self._conversation_info
