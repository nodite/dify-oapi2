from __future__ import annotations

from pydantic import BaseModel

from .workflow_run_data import WorkflowRunData


class WorkflowRunInfo(BaseModel):
    workflow_run_id: str | None = None
    task_id: str | None = None
    data: WorkflowRunData | None = None

    @staticmethod
    def builder() -> WorkflowRunInfoBuilder:
        return WorkflowRunInfoBuilder()


class WorkflowRunInfoBuilder:
    def __init__(self):
        self._workflow_run_info = WorkflowRunInfo()

    def build(self) -> WorkflowRunInfo:
        return self._workflow_run_info

    def workflow_run_id(self, workflow_run_id: str) -> WorkflowRunInfoBuilder:
        self._workflow_run_info.workflow_run_id = workflow_run_id
        return self

    def task_id(self, task_id: str) -> WorkflowRunInfoBuilder:
        self._workflow_run_info.task_id = task_id
        return self

    def data(self, data: WorkflowRunData) -> WorkflowRunInfoBuilder:
        self._workflow_run_info.data = data
        return self
