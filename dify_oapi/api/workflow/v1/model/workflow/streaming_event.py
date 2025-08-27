from __future__ import annotations

from typing import Any

from pydantic import BaseModel

from .workflow_types import EventType


class StreamingEvent(BaseModel):
    event: EventType | None = None
    task_id: str | None = None
    workflow_run_id: str | None = None
    data: dict[str, Any] | None = None

    @staticmethod
    def builder() -> StreamingEventBuilder:
        return StreamingEventBuilder()


class StreamingEventBuilder:
    def __init__(self):
        self._streaming_event = StreamingEvent()

    def build(self) -> StreamingEvent:
        return self._streaming_event

    def event(self, event: EventType) -> StreamingEventBuilder:
        self._streaming_event.event = event
        return self

    def task_id(self, task_id: str) -> StreamingEventBuilder:
        self._streaming_event.task_id = task_id
        return self

    def workflow_run_id(self, workflow_run_id: str) -> StreamingEventBuilder:
        self._streaming_event.workflow_run_id = workflow_run_id
        return self

    def data(self, data: dict[str, Any]) -> StreamingEventBuilder:
        self._streaming_event.data = data
        return self
