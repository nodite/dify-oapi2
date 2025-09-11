"""Workflow finished event data model.

This module defines the data structure for workflow_finished streaming events.
"""

from typing import Any, Optional

from pydantic import BaseModel

from .workflow_types import WorkflowStatus


class WorkflowFinishedData(BaseModel):
    """Data structure for workflow_finished streaming event."""

    id: str
    workflow_id: str
    status: WorkflowStatus
    outputs: Optional[dict[str, Any]] = None
    error: Optional[str] = None
    elapsed_time: Optional[float] = None
    total_tokens: Optional[int] = None
    total_steps: int
    created_at: int
    finished_at: int

    @staticmethod
    def builder() -> "WorkflowFinishedDataBuilder":
        """Create a new WorkflowFinishedData builder."""
        return WorkflowFinishedDataBuilder()


class WorkflowFinishedDataBuilder:
    """Builder for WorkflowFinishedData."""

    def __init__(self):
        self._workflow_finished_data = WorkflowFinishedData(
            id="", workflow_id="", status="succeeded", total_steps=0, created_at=0, finished_at=0
        )

    def build(self) -> WorkflowFinishedData:
        """Build the WorkflowFinishedData instance."""
        return self._workflow_finished_data

    def id(self, id: str) -> "WorkflowFinishedDataBuilder":
        """Set the workflow run ID."""
        self._workflow_finished_data.id = id
        return self

    def workflow_id(self, workflow_id: str) -> "WorkflowFinishedDataBuilder":
        """Set the workflow ID."""
        self._workflow_finished_data.workflow_id = workflow_id
        return self

    def status(self, status: WorkflowStatus) -> "WorkflowFinishedDataBuilder":
        """Set the workflow status."""
        self._workflow_finished_data.status = status
        return self

    def outputs(self, outputs: dict[str, Any]) -> "WorkflowFinishedDataBuilder":
        """Set the workflow outputs."""
        self._workflow_finished_data.outputs = outputs
        return self

    def error(self, error: str) -> "WorkflowFinishedDataBuilder":
        """Set the error message."""
        self._workflow_finished_data.error = error
        return self

    def elapsed_time(self, elapsed_time: float) -> "WorkflowFinishedDataBuilder":
        """Set the elapsed time."""
        self._workflow_finished_data.elapsed_time = elapsed_time
        return self

    def total_tokens(self, total_tokens: int) -> "WorkflowFinishedDataBuilder":
        """Set the total tokens."""
        self._workflow_finished_data.total_tokens = total_tokens
        return self

    def total_steps(self, total_steps: int) -> "WorkflowFinishedDataBuilder":
        """Set the total steps."""
        self._workflow_finished_data.total_steps = total_steps
        return self

    def created_at(self, created_at: int) -> "WorkflowFinishedDataBuilder":
        """Set the creation timestamp."""
        self._workflow_finished_data.created_at = created_at
        return self

    def finished_at(self, finished_at: int) -> "WorkflowFinishedDataBuilder":
        """Set the finish timestamp."""
        self._workflow_finished_data.finished_at = finished_at
        return self
