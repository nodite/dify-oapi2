"""Chunk workflow event for streaming mode.

This module defines the base structure for workflow streaming events
and specific event data models.
"""

from typing import Any, Optional

from pydantic import BaseModel

from .workflow_types import EventType


class ChunkWorkflowEvent(BaseModel):
    """Base streaming event structure for workflow execution."""

    event: EventType
    task_id: Optional[str] = None
    workflow_run_id: Optional[str] = None
    data: Optional[dict[str, Any]] = None
    message_id: Optional[str] = None
    audio: Optional[str] = None
    created_at: Optional[int] = None

    @staticmethod
    def builder() -> "ChunkWorkflowEventBuilder":
        """Create a new ChunkWorkflowEvent builder."""
        return ChunkWorkflowEventBuilder()


class ChunkWorkflowEventBuilder:
    """Builder for ChunkWorkflowEvent."""

    def __init__(self):
        self._chunk_workflow_event = ChunkWorkflowEvent(event="ping")

    def build(self) -> ChunkWorkflowEvent:
        """Build the ChunkWorkflowEvent instance."""
        return self._chunk_workflow_event

    def event(self, event: EventType) -> "ChunkWorkflowEventBuilder":
        """Set the event type."""
        self._chunk_workflow_event.event = event
        return self

    def task_id(self, task_id: str) -> "ChunkWorkflowEventBuilder":
        """Set the task ID."""
        self._chunk_workflow_event.task_id = task_id
        return self

    def workflow_run_id(self, workflow_run_id: str) -> "ChunkWorkflowEventBuilder":
        """Set the workflow run ID."""
        self._chunk_workflow_event.workflow_run_id = workflow_run_id
        return self

    def data(self, data: dict[str, Any]) -> "ChunkWorkflowEventBuilder":
        """Set the event data."""
        self._chunk_workflow_event.data = data
        return self

    def message_id(self, message_id: str) -> "ChunkWorkflowEventBuilder":
        """Set the message ID (for TTS events)."""
        self._chunk_workflow_event.message_id = message_id
        return self

    def audio(self, audio: str) -> "ChunkWorkflowEventBuilder":
        """Set the audio data (for TTS events)."""
        self._chunk_workflow_event.audio = audio
        return self

    def created_at(self, created_at: int) -> "ChunkWorkflowEventBuilder":
        """Set the creation timestamp."""
        self._chunk_workflow_event.created_at = created_at
        return self
