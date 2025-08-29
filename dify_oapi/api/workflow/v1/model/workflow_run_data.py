from __future__ import annotations

from typing import Any

from pydantic import BaseModel

from .workflow_types import WorkflowStatus


class WorkflowRunData(BaseModel):
    id: str | None = None
    workflow_id: str | None = None
    status: WorkflowStatus | None = None
    outputs: dict[str, Any] | None = None
    error: str | None = None
    elapsed_time: float | None = None
    total_tokens: int | None = None
    total_steps: int | None = None
    created_at: int | None = None
    finished_at: int | None = None

    @staticmethod
    def builder() -> WorkflowRunDataBuilder:
        return WorkflowRunDataBuilder()


class WorkflowRunDataBuilder:
    def __init__(self):
        self._workflow_run_data = WorkflowRunData()

    def build(self) -> WorkflowRunData:
        return self._workflow_run_data

    def id(self, id: str) -> WorkflowRunDataBuilder:
        self._workflow_run_data.id = id
        return self

    def workflow_id(self, workflow_id: str) -> WorkflowRunDataBuilder:
        self._workflow_run_data.workflow_id = workflow_id
        return self

    def status(self, status: WorkflowStatus) -> WorkflowRunDataBuilder:
        self._workflow_run_data.status = status
        return self

    def outputs(self, outputs: dict[str, Any]) -> WorkflowRunDataBuilder:
        self._workflow_run_data.outputs = outputs
        return self

    def error(self, error: str) -> WorkflowRunDataBuilder:
        self._workflow_run_data.error = error
        return self

    def elapsed_time(self, elapsed_time: float) -> WorkflowRunDataBuilder:
        self._workflow_run_data.elapsed_time = elapsed_time
        return self

    def total_tokens(self, total_tokens: int) -> WorkflowRunDataBuilder:
        self._workflow_run_data.total_tokens = total_tokens
        return self

    def total_steps(self, total_steps: int) -> WorkflowRunDataBuilder:
        self._workflow_run_data.total_steps = total_steps
        return self

    def created_at(self, created_at: int) -> WorkflowRunDataBuilder:
        self._workflow_run_data.created_at = created_at
        return self

    def finished_at(self, finished_at: int) -> WorkflowRunDataBuilder:
        self._workflow_run_data.finished_at = finished_at
        return self
