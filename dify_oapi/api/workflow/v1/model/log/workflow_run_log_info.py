from __future__ import annotations

from pydantic import BaseModel

from ..workflow.workflow_types import LogStatus


class WorkflowRunLogInfo(BaseModel):
    id: str | None = None
    version: str | None = None
    status: LogStatus | None = None
    error: str | None = None
    elapsed_time: float | None = None
    total_tokens: int | None = None
    total_steps: int | None = None
    created_at: int | None = None
    finished_at: int | None = None

    @staticmethod
    def builder() -> WorkflowRunLogInfoBuilder:
        return WorkflowRunLogInfoBuilder()


class WorkflowRunLogInfoBuilder:
    def __init__(self):
        self._workflow_run_log_info = WorkflowRunLogInfo()

    def build(self) -> WorkflowRunLogInfo:
        return self._workflow_run_log_info

    def id(self, id: str) -> WorkflowRunLogInfoBuilder:
        self._workflow_run_log_info.id = id
        return self

    def version(self, version: str) -> WorkflowRunLogInfoBuilder:
        self._workflow_run_log_info.version = version
        return self

    def status(self, status: LogStatus) -> WorkflowRunLogInfoBuilder:
        self._workflow_run_log_info.status = status
        return self

    def error(self, error: str) -> WorkflowRunLogInfoBuilder:
        self._workflow_run_log_info.error = error
        return self

    def elapsed_time(self, elapsed_time: float) -> WorkflowRunLogInfoBuilder:
        self._workflow_run_log_info.elapsed_time = elapsed_time
        return self

    def total_tokens(self, total_tokens: int) -> WorkflowRunLogInfoBuilder:
        self._workflow_run_log_info.total_tokens = total_tokens
        return self

    def total_steps(self, total_steps: int) -> WorkflowRunLogInfoBuilder:
        self._workflow_run_log_info.total_steps = total_steps
        return self

    def created_at(self, created_at: int) -> WorkflowRunLogInfoBuilder:
        self._workflow_run_log_info.created_at = created_at
        return self

    def finished_at(self, finished_at: int) -> WorkflowRunLogInfoBuilder:
        self._workflow_run_log_info.finished_at = finished_at
        return self
