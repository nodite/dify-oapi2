from __future__ import annotations

from dify_oapi.core.enum import HttpMethod
from dify_oapi.core.model.base_request import BaseRequest


class GetWorkflowRunDetailRequest(BaseRequest):
    def __init__(self) -> None:
        super().__init__()
        self.workflow_run_id: str | None = None

    @staticmethod
    def builder() -> GetWorkflowRunDetailRequestBuilder:
        return GetWorkflowRunDetailRequestBuilder()


class GetWorkflowRunDetailRequestBuilder:
    def __init__(self):
        get_workflow_run_detail_request = GetWorkflowRunDetailRequest()
        get_workflow_run_detail_request.http_method = HttpMethod.GET
        get_workflow_run_detail_request.uri = "/v1/workflows/run/:workflow_run_id"
        self._get_workflow_run_detail_request = get_workflow_run_detail_request

    def build(self) -> GetWorkflowRunDetailRequest:
        return self._get_workflow_run_detail_request

    def workflow_run_id(self, workflow_run_id: str) -> GetWorkflowRunDetailRequestBuilder:
        self._get_workflow_run_detail_request.workflow_run_id = workflow_run_id
        self._get_workflow_run_detail_request.paths["workflow_run_id"] = workflow_run_id
        return self
