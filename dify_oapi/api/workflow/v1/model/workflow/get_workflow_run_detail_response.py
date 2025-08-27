from __future__ import annotations

from typing import Any

from dify_oapi.core.model.base_response import BaseResponse

from .workflow_types import WorkflowStatus


class GetWorkflowRunDetailResponse(BaseResponse):
    id: str | None = None
    workflow_id: str | None = None
    status: WorkflowStatus | None = None
    inputs: dict[str, Any] | None = None
    outputs: dict[str, Any] | None = None
    error: str | None = None
    total_steps: int | None = None
    total_tokens: int | None = None
    created_at: int | None = None
    finished_at: int | None = None
    elapsed_time: float | None = None
