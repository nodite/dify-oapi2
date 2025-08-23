from __future__ import annotations

from pydantic import BaseModel

from .completion_types import AppMode
from .metadata import Metadata


class CompletionMessageInfo(BaseModel):
    message_id: str | None = None
    mode: AppMode | None = None
    answer: str | None = None
    metadata: Metadata | None = None
    created_at: int | None = None

    @staticmethod
    def builder() -> CompletionMessageInfoBuilder:
        return CompletionMessageInfoBuilder()


class CompletionMessageInfoBuilder:
    def __init__(self):
        self._completion_message_info = CompletionMessageInfo()

    def build(self) -> CompletionMessageInfo:
        return self._completion_message_info

    def message_id(self, message_id: str) -> CompletionMessageInfoBuilder:
        self._completion_message_info.message_id = message_id
        return self

    def mode(self, mode: AppMode) -> CompletionMessageInfoBuilder:
        self._completion_message_info.mode = mode
        return self

    def answer(self, answer: str) -> CompletionMessageInfoBuilder:
        self._completion_message_info.answer = answer
        return self

    def metadata(self, metadata: Metadata) -> CompletionMessageInfoBuilder:
        self._completion_message_info.metadata = metadata
        return self

    def created_at(self, created_at: int) -> CompletionMessageInfoBuilder:
        self._completion_message_info.created_at = created_at
        return self
