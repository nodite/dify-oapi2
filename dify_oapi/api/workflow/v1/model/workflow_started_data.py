"""Workflow started event data model.

This module defines the data structure for workflow_started streaming events.
"""

from pydantic import BaseModel


class WorkflowStartedData(BaseModel):
    """Data structure for workflow_started streaming event."""

    id: str
    workflow_id: str
    sequence_number: int
    created_at: int

    @staticmethod
    def builder() -> "WorkflowStartedDataBuilder":
        """Create a new WorkflowStartedData builder."""
        return WorkflowStartedDataBuilder()


class WorkflowStartedDataBuilder:
    """Builder for WorkflowStartedData."""

    def __init__(self):
        self._workflow_started_data = WorkflowStartedData(id="", workflow_id="", sequence_number=0, created_at=0)

    def build(self) -> WorkflowStartedData:
        """Build the WorkflowStartedData instance."""
        return self._workflow_started_data

    def id(self, id: str) -> "WorkflowStartedDataBuilder":
        """Set the workflow run ID."""
        self._workflow_started_data.id = id
        return self

    def workflow_id(self, workflow_id: str) -> "WorkflowStartedDataBuilder":
        """Set the workflow ID."""
        self._workflow_started_data.workflow_id = workflow_id
        return self

    def sequence_number(self, sequence_number: int) -> "WorkflowStartedDataBuilder":
        """Set the sequence number."""
        self._workflow_started_data.sequence_number = sequence_number
        return self

    def created_at(self, created_at: int) -> "WorkflowStartedDataBuilder":
        """Set the creation timestamp."""
        self._workflow_started_data.created_at = created_at
        return self
