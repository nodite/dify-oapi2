from __future__ import annotations

from dify_oapi.core.model.base_response import BaseResponse

from .workflow_run_info import WorkflowRunInfo


class RunSpecificWorkflowResponse(WorkflowRunInfo, BaseResponse):
    pass
