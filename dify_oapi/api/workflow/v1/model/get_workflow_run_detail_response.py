from __future__ import annotations

import json
from typing import Any

from pydantic import field_validator

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

    @field_validator("inputs", "outputs", mode="before")
    @classmethod
    def parse_json_fields(cls, v: Any) -> dict[str, Any] | None:
        if v is None:
            return None
        if isinstance(v, str):
            try:
                parsed = json.loads(v)
                return parsed if isinstance(parsed, dict) else {}
            except (json.JSONDecodeError, TypeError):
                return {}
        if isinstance(v, dict):
            return v
        return {}
