from __future__ import annotations

from dify_oapi.core.enum import HttpMethod
from dify_oapi.core.model.base_request import BaseRequest

from .run_specific_workflow_request_body import RunSpecificWorkflowRequestBody


class RunSpecificWorkflowRequest(BaseRequest):
    def __init__(self) -> None:
        super().__init__()
        self.workflow_id: str | None = None
        self.request_body: RunSpecificWorkflowRequestBody | None = None

    @staticmethod
    def builder() -> RunSpecificWorkflowRequestBuilder:
        return RunSpecificWorkflowRequestBuilder()


class RunSpecificWorkflowRequestBuilder:
    def __init__(self):
        run_specific_workflow_request = RunSpecificWorkflowRequest()
        run_specific_workflow_request.http_method = HttpMethod.POST
        run_specific_workflow_request.uri = "/v1/workflows/:workflow_id/run"
        self._run_specific_workflow_request = run_specific_workflow_request

    def build(self) -> RunSpecificWorkflowRequest:
        return self._run_specific_workflow_request

    def workflow_id(self, workflow_id: str) -> RunSpecificWorkflowRequestBuilder:
        self._run_specific_workflow_request.workflow_id = workflow_id
        self._run_specific_workflow_request.paths["workflow_id"] = workflow_id
        return self

    def request_body(self, request_body: RunSpecificWorkflowRequestBody) -> RunSpecificWorkflowRequestBuilder:
        self._run_specific_workflow_request.request_body = request_body
        self._run_specific_workflow_request.body = request_body.model_dump(exclude_none=True, mode="json")
        return self
