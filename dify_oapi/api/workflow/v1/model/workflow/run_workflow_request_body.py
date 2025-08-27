from __future__ import annotations

from pydantic import BaseModel

from .workflow_file_info import WorkflowFileInfo
from .workflow_inputs import WorkflowInputs
from .workflow_types import ResponseMode


class RunWorkflowRequestBody(BaseModel):
    inputs: WorkflowInputs | None = None
    response_mode: ResponseMode | None = None
    user: str | None = None
    files: list[WorkflowFileInfo] | None = None
    trace_id: str | None = None

    @staticmethod
    def builder() -> RunWorkflowRequestBodyBuilder:
        return RunWorkflowRequestBodyBuilder()


class RunWorkflowRequestBodyBuilder:
    def __init__(self) -> None:
        self._run_workflow_request_body = RunWorkflowRequestBody()

    def build(self) -> RunWorkflowRequestBody:
        return self._run_workflow_request_body

    def inputs(self, inputs: WorkflowInputs) -> RunWorkflowRequestBodyBuilder:
        self._run_workflow_request_body.inputs = inputs
        return self

    def response_mode(self, response_mode: ResponseMode) -> RunWorkflowRequestBodyBuilder:
        self._run_workflow_request_body.response_mode = response_mode
        return self

    def user(self, user: str) -> RunWorkflowRequestBodyBuilder:
        self._run_workflow_request_body.user = user
        return self

    def files(self, files: list[WorkflowFileInfo]) -> RunWorkflowRequestBodyBuilder:
        self._run_workflow_request_body.files = files
        return self

    def trace_id(self, trace_id: str) -> RunWorkflowRequestBodyBuilder:
        self._run_workflow_request_body.trace_id = trace_id
        return self
