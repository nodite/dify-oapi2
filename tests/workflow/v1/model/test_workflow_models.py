"""Tests for workflow API models."""

from dify_oapi.api.workflow.v1.model.run_workflow_request import RunWorkflowRequest
from dify_oapi.api.workflow.v1.model.run_workflow_request_body import RunWorkflowRequestBody
from dify_oapi.api.workflow.v1.model.run_workflow_response import RunWorkflowResponse
from dify_oapi.api.workflow.v1.model.workflow_file_info import WorkflowFileInfo
from dify_oapi.api.workflow.v1.model.workflow_inputs import WorkflowInputs
from dify_oapi.api.workflow.v1.model.workflow_run_data import WorkflowRunData
from dify_oapi.api.workflow.v1.model.workflow_run_info import WorkflowRunInfo
from dify_oapi.core.enum import HttpMethod
from dify_oapi.core.model.base_response import BaseResponse


class TestRunWorkflowModels:
    """Test Run Workflow API models."""

    def test_request_builder(self) -> None:
        """Test request builder pattern and URI/method setup."""
        request = RunWorkflowRequest.builder().build()

        assert request.http_method == HttpMethod.POST
        assert request.uri == "/v1/workflows/run"
        assert request.request_body is None

    def test_request_validation(self) -> None:
        """Test request structure validation."""
        request_body = RunWorkflowRequestBody.builder().response_mode("streaming").user("test-user").build()

        request = RunWorkflowRequest.builder().request_body(request_body).build()

        assert request.request_body is not None
        assert request.request_body.response_mode == "streaming"
        assert request.request_body.user == "test-user"
        assert request.body is not None

    def test_request_body_builder(self) -> None:
        """Test request body builder methods."""
        inputs = WorkflowInputs.builder().add_input("query", "test query").build()
        file_info = (
            WorkflowFileInfo.builder().type("document").transfer_method("local_file").upload_file_id("file-123").build()
        )

        request_body = (
            RunWorkflowRequestBody.builder()
            .inputs(inputs)
            .response_mode("blocking")
            .user("user-456")
            .files([file_info])
            .trace_id("trace-789")
            .build()
        )

        assert request_body.inputs is not None
        assert request_body.response_mode == "blocking"
        assert request_body.user == "user-456"
        assert request_body.files is not None
        assert len(request_body.files) == 1
        assert request_body.trace_id == "trace-789"

    def test_request_body_validation(self) -> None:
        """Test request body field types and constraints."""
        request_body = RunWorkflowRequestBody.builder().response_mode("streaming").build()
        assert request_body.response_mode == "streaming"

        request_body = RunWorkflowRequestBody.builder().response_mode("blocking").build()
        assert request_body.response_mode == "blocking"

    def test_response_inheritance(self) -> None:
        """Test response inherits from BaseResponse."""
        response = RunWorkflowResponse()

        # Test BaseResponse inheritance
        assert isinstance(response, BaseResponse)
        assert hasattr(response, "success")
        assert hasattr(response, "code")
        assert hasattr(response, "msg")
        assert hasattr(response, "raw")

        # Test WorkflowRunInfo inheritance
        assert isinstance(response, WorkflowRunInfo)
        assert hasattr(response, "workflow_run_id")
        assert hasattr(response, "task_id")
        assert hasattr(response, "data")

    def test_response_data_access(self) -> None:
        """Test response data access patterns."""
        # Create workflow run data
        run_data = (
            WorkflowRunData.builder()
            .id("run-123")
            .workflow_id("workflow-456")
            .status("succeeded")
            .total_tokens(150)
            .build()
        )

        # Create workflow run info
        run_info = WorkflowRunInfo.builder().workflow_run_id("run-123").task_id("task-456").data(run_data).build()

        # Test data access
        assert run_info.workflow_run_id == "run-123"
        assert run_info.task_id == "task-456"
        assert run_info.data is not None
        assert run_info.data.id == "run-123"
        assert run_info.data.status == "succeeded"

    def test_workflow_run_data_builder(self) -> None:
        """Test WorkflowRunData builder pattern."""
        run_data = (
            WorkflowRunData.builder()
            .id("run-123")
            .workflow_id("workflow-456")
            .status("running")
            .outputs({"result": "test output"})
            .elapsed_time(2.5)
            .total_tokens(100)
            .total_steps(5)
            .created_at(1640995200)
            .finished_at(1640995300)
            .build()
        )

        assert run_data.id == "run-123"
        assert run_data.workflow_id == "workflow-456"
        assert run_data.status == "running"
        assert run_data.outputs == {"result": "test output"}
        assert run_data.elapsed_time == 2.5
        assert run_data.total_tokens == 100
        assert run_data.total_steps == 5
        assert run_data.created_at == 1640995200
        assert run_data.finished_at == 1640995300

    def test_workflow_run_data_error_handling(self) -> None:
        """Test WorkflowRunData error field handling."""
        run_data = WorkflowRunData.builder().status("failed").error("Workflow execution failed").build()

        assert run_data.status == "failed"
        assert run_data.error == "Workflow execution failed"

    def test_complete_workflow_request_cycle(self) -> None:
        """Test complete request building cycle."""
        # Build inputs
        inputs = (
            WorkflowInputs.builder()
            .add_input("query", "Translate this text")
            .add_input("target_language", "French")
            .build()
        )

        # Build file info
        file_info = (
            WorkflowFileInfo.builder()
            .type("image")
            .transfer_method("remote_url")
            .url("https://example.com/image.jpg")
            .build()
        )

        # Build request body
        request_body = (
            RunWorkflowRequestBody.builder()
            .inputs(inputs)
            .response_mode("streaming")
            .user("user-workflow-123")
            .files([file_info])
            .build()
        )

        # Build request
        request = RunWorkflowRequest.builder().request_body(request_body).build()

        # Validate complete structure
        assert request.http_method == HttpMethod.POST
        assert request.uri == "/v1/workflows/run"
        assert request.request_body is not None
        assert request.request_body.inputs is not None
        assert request.request_body.response_mode == "streaming"
        assert request.request_body.user == "user-workflow-123"
        assert request.request_body.files is not None
        assert len(request.request_body.files) == 1
        assert request.body is not None
