"""Workflow completion response for blocking mode.

This module defines the WorkflowCompletionResponse model for handling
workflow execution results in blocking mode.
"""

from pydantic import BaseModel

from .workflow_run_data import WorkflowRunData


class WorkflowCompletionResponse(BaseModel):
    """Response structure for workflow execution in blocking mode."""

    workflow_run_id: str
    task_id: str
    data: WorkflowRunData

    @staticmethod
    def builder() -> "WorkflowCompletionResponseBuilder":
        """Create a new WorkflowCompletionResponse builder."""
        return WorkflowCompletionResponseBuilder()


class WorkflowCompletionResponseBuilder:
    """Builder for WorkflowCompletionResponse."""

    def __init__(self):
        self._workflow_completion_response = WorkflowCompletionResponse(
            workflow_run_id="", task_id="", data=WorkflowRunData()
        )

    def build(self) -> WorkflowCompletionResponse:
        """Build the WorkflowCompletionResponse instance."""
        return self._workflow_completion_response

    def workflow_run_id(self, workflow_run_id: str) -> "WorkflowCompletionResponseBuilder":
        """Set the workflow run ID."""
        self._workflow_completion_response.workflow_run_id = workflow_run_id
        return self

    def task_id(self, task_id: str) -> "WorkflowCompletionResponseBuilder":
        """Set the task ID."""
        self._workflow_completion_response.task_id = task_id
        return self

    def data(self, data: WorkflowRunData) -> "WorkflowCompletionResponseBuilder":
        """Set the workflow run data."""
        self._workflow_completion_response.data = data
        return self
