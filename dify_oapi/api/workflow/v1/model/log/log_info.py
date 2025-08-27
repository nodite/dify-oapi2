from __future__ import annotations

from pydantic import BaseModel

from ..workflow.workflow_types import CreatedByRole, CreatedFrom
from .end_user_info import EndUserInfo
from .workflow_run_log_info import WorkflowRunLogInfo


class LogInfo(BaseModel):
    id: str | None = None
    workflow_run: WorkflowRunLogInfo | None = None
    created_from: CreatedFrom | None = None
    created_by_role: CreatedByRole | None = None
    created_by_account: str | None = None
    created_by_end_user: EndUserInfo | None = None
    created_at: int | None = None

    @staticmethod
    def builder() -> LogInfoBuilder:
        return LogInfoBuilder()


class LogInfoBuilder:
    def __init__(self):
        self._log_info = LogInfo()

    def build(self) -> LogInfo:
        return self._log_info

    def id(self, id: str) -> LogInfoBuilder:
        self._log_info.id = id
        return self

    def workflow_run(self, workflow_run: WorkflowRunLogInfo) -> LogInfoBuilder:
        self._log_info.workflow_run = workflow_run
        return self

    def created_from(self, created_from: CreatedFrom) -> LogInfoBuilder:
        self._log_info.created_from = created_from
        return self

    def created_by_role(self, created_by_role: CreatedByRole) -> LogInfoBuilder:
        self._log_info.created_by_role = created_by_role
        return self

    def created_by_account(self, created_by_account: str) -> LogInfoBuilder:
        self._log_info.created_by_account = created_by_account
        return self

    def created_by_end_user(self, created_by_end_user: EndUserInfo) -> LogInfoBuilder:
        self._log_info.created_by_end_user = created_by_end_user
        return self

    def created_at(self, created_at: int) -> LogInfoBuilder:
        self._log_info.created_at = created_at
        return self
