from dify_oapi.api.workflow.v1.model.workflow.get_workflow_run_detail_request import GetWorkflowRunDetailRequest
from dify_oapi.api.workflow.v1.model.workflow.get_workflow_run_detail_response import GetWorkflowRunDetailResponse
from dify_oapi.api.workflow.v1.model.workflow.run_specific_workflow_request import RunSpecificWorkflowRequest
from dify_oapi.api.workflow.v1.model.workflow.run_specific_workflow_request_body import RunSpecificWorkflowRequestBody
from dify_oapi.api.workflow.v1.model.workflow.run_specific_workflow_response import RunSpecificWorkflowResponse
from dify_oapi.api.workflow.v1.model.workflow.run_workflow_request import RunWorkflowRequest
from dify_oapi.api.workflow.v1.model.workflow.run_workflow_request_body import RunWorkflowRequestBody
from dify_oapi.api.workflow.v1.model.workflow.run_workflow_response import RunWorkflowResponse
from dify_oapi.api.workflow.v1.model.workflow.stop_workflow_request import StopWorkflowRequest
from dify_oapi.api.workflow.v1.model.workflow.stop_workflow_request_body import StopWorkflowRequestBody
from dify_oapi.api.workflow.v1.model.workflow.stop_workflow_response import StopWorkflowResponse
from dify_oapi.api.workflow.v1.model.workflow.workflow_inputs import WorkflowInputs
from dify_oapi.core.enum import HttpMethod
from dify_oapi.core.model.base_response import BaseResponse


class TestRunWorkflowModels:
    def test_request_builder(self) -> None:
        """Test RunWorkflowRequest builder pattern."""
        request = RunWorkflowRequest.builder().build()
        assert request.http_method == HttpMethod.POST
        assert request.uri == "/v1/workflows/run"

    def test_request_validation(self) -> None:
        """Test RunWorkflowRequest validation."""
        inputs = WorkflowInputs.builder().add_input("query", "test").build()
        request_body = (
            RunWorkflowRequestBody.builder().inputs(inputs).response_mode("blocking").user("user-123").build()
        )
        request = RunWorkflowRequest.builder().request_body(request_body).build()
        assert request.request_body is not None
        assert request.body is not None

    def test_request_body_builder(self) -> None:
        """Test RunWorkflowRequestBody builder pattern."""
        inputs = WorkflowInputs.builder().add_input("query", "test").build()
        request_body = (
            RunWorkflowRequestBody.builder().inputs(inputs).response_mode("streaming").user("user-456").build()
        )
        assert request_body.inputs is not None
        assert request_body.response_mode == "streaming"
        assert request_body.user == "user-456"

    def test_request_body_validation(self) -> None:
        """Test RunWorkflowRequestBody validation."""
        request_body = RunWorkflowRequestBody.builder().response_mode("blocking").user("user-123").build()
        assert request_body.response_mode == "blocking"
        assert request_body.user == "user-123"

    def test_response_inheritance(self) -> None:
        """Test RunWorkflowResponse inherits from BaseResponse."""
        response = RunWorkflowResponse()
        assert isinstance(response, BaseResponse)
        assert hasattr(response, "success")
        assert hasattr(response, "code")
        assert hasattr(response, "msg")
        assert hasattr(response, "raw")

    def test_response_data_access(self) -> None:
        """Test RunWorkflowResponse data access."""
        response = RunWorkflowResponse(workflow_run_id="run-123", task_id="task-456")
        assert response.workflow_run_id == "run-123"
        assert response.task_id == "task-456"


class TestRunSpecificWorkflowModels:
    def test_request_builder(self) -> None:
        """Test RunSpecificWorkflowRequest builder pattern."""
        request = RunSpecificWorkflowRequest.builder().workflow_id("workflow-123").build()
        assert request.http_method == HttpMethod.POST
        assert request.uri == "/v1/workflows/:workflow_id/run"
        assert request.workflow_id == "workflow-123"
        assert request.paths["workflow_id"] == "workflow-123"

    def test_request_validation(self) -> None:
        """Test RunSpecificWorkflowRequest validation."""
        inputs = WorkflowInputs.builder().add_input("query", "test").build()
        request_body = (
            RunSpecificWorkflowRequestBody.builder().inputs(inputs).response_mode("blocking").user("user-123").build()
        )
        request = RunSpecificWorkflowRequest.builder().workflow_id("workflow-456").request_body(request_body).build()
        assert request.workflow_id == "workflow-456"
        assert request.request_body is not None

    def test_request_body_builder(self) -> None:
        """Test RunSpecificWorkflowRequestBody builder pattern."""
        inputs = WorkflowInputs.builder().add_input("content", "test content").build()
        request_body = (
            RunSpecificWorkflowRequestBody.builder().inputs(inputs).response_mode("streaming").user("user-456").build()
        )
        assert request_body.inputs is not None
        assert request_body.response_mode == "streaming"
        assert request_body.user == "user-456"

    def test_request_body_validation(self) -> None:
        """Test RunSpecificWorkflowRequestBody validation."""
        request_body = RunSpecificWorkflowRequestBody.builder().response_mode("blocking").user("user-123").build()
        assert request_body.response_mode == "blocking"
        assert request_body.user == "user-123"

    def test_response_inheritance(self) -> None:
        """Test RunSpecificWorkflowResponse inherits from BaseResponse."""
        response = RunSpecificWorkflowResponse()
        assert isinstance(response, BaseResponse)
        assert hasattr(response, "success")
        assert hasattr(response, "code")
        assert hasattr(response, "msg")
        assert hasattr(response, "raw")

    def test_response_data_access(self) -> None:
        """Test RunSpecificWorkflowResponse data access."""
        response = RunSpecificWorkflowResponse(workflow_run_id="run-123", task_id="task-456")
        assert response.workflow_run_id == "run-123"
        assert response.task_id == "task-456"


class TestGetWorkflowRunDetailModels:
    def test_request_builder(self) -> None:
        """Test GetWorkflowRunDetailRequest builder pattern."""
        request = GetWorkflowRunDetailRequest.builder().workflow_run_id("run-123").build()
        assert request.http_method == HttpMethod.GET
        assert request.uri == "/v1/workflows/run/:workflow_run_id"
        assert request.workflow_run_id == "run-123"
        assert request.paths["workflow_run_id"] == "run-123"

    def test_request_validation(self) -> None:
        """Test GetWorkflowRunDetailRequest validation."""
        request = GetWorkflowRunDetailRequest.builder().workflow_run_id("run-456").build()
        assert request.workflow_run_id == "run-456"
        assert "workflow_run_id" in request.paths

    def test_response_inheritance(self) -> None:
        """Test GetWorkflowRunDetailResponse inherits from BaseResponse."""
        response = GetWorkflowRunDetailResponse()
        assert isinstance(response, BaseResponse)
        assert hasattr(response, "success")
        assert hasattr(response, "code")
        assert hasattr(response, "msg")
        assert hasattr(response, "raw")

    def test_response_data_access(self) -> None:
        """Test GetWorkflowRunDetailResponse data access."""
        response = GetWorkflowRunDetailResponse(id="run-123", workflow_id="workflow-456", status="succeeded")
        assert response.id == "run-123"
        assert response.workflow_id == "workflow-456"
        assert response.status == "succeeded"


class TestStopWorkflowModels:
    def test_request_builder(self) -> None:
        """Test StopWorkflowRequest builder pattern."""
        request = StopWorkflowRequest.builder().task_id("task-123").build()
        assert request.http_method == HttpMethod.POST
        assert request.uri == "/v1/workflows/tasks/:task_id/stop"
        assert request.task_id == "task-123"
        assert request.paths["task_id"] == "task-123"

    def test_request_validation(self) -> None:
        """Test StopWorkflowRequest validation."""
        request_body = StopWorkflowRequestBody.builder().user("user-123").build()
        request = StopWorkflowRequest.builder().task_id("task-456").request_body(request_body).build()
        assert request.task_id == "task-456"
        assert request.request_body is not None

    def test_request_body_builder(self) -> None:
        """Test StopWorkflowRequestBody builder pattern."""
        request_body = StopWorkflowRequestBody.builder().user("user-456").build()
        assert request_body.user == "user-456"

    def test_request_body_validation(self) -> None:
        """Test StopWorkflowRequestBody validation."""
        request_body = StopWorkflowRequestBody.builder().user("user-789").build()
        assert request_body.user == "user-789"

    def test_response_inheritance(self) -> None:
        """Test StopWorkflowResponse inherits from BaseResponse."""
        response = StopWorkflowResponse()
        assert isinstance(response, BaseResponse)
        assert hasattr(response, "success")
        assert hasattr(response, "code")
        assert hasattr(response, "msg")
        assert hasattr(response, "raw")

    def test_response_data_access(self) -> None:
        """Test StopWorkflowResponse data access."""
        response = StopWorkflowResponse(result="success")
        assert response.result == "success"
