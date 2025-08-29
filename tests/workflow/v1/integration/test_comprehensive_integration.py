"""Comprehensive integration tests for workflow API including migration validation."""

from io import BytesIO
from unittest.mock import Mock, patch

from dify_oapi.api.workflow.v1.model.get_workflow_logs_request import GetWorkflowLogsRequest
from dify_oapi.api.workflow.v1.model.get_workflow_logs_response import GetWorkflowLogsResponse
from dify_oapi.api.workflow.v1.model.get_workflow_run_detail_request import GetWorkflowRunDetailRequest
from dify_oapi.api.workflow.v1.model.get_workflow_run_detail_response import GetWorkflowRunDetailResponse
from dify_oapi.api.workflow.v1.model.run_workflow_request import RunWorkflowRequest
from dify_oapi.api.workflow.v1.model.run_workflow_request_body import RunWorkflowRequestBody
from dify_oapi.api.workflow.v1.model.run_workflow_response import RunWorkflowResponse
from dify_oapi.api.workflow.v1.model.stop_workflow_request import StopWorkflowRequest
from dify_oapi.api.workflow.v1.model.stop_workflow_request_body import StopWorkflowRequestBody
from dify_oapi.api.workflow.v1.model.stop_workflow_response import StopWorkflowResponse
from dify_oapi.api.workflow.v1.model.upload_file_request import UploadFileRequest
from dify_oapi.api.workflow.v1.model.upload_file_request_body import UploadFileRequestBody
from dify_oapi.api.workflow.v1.model.upload_file_response import UploadFileResponse
from dify_oapi.api.workflow.v1.model.workflow_inputs import WorkflowInputs
from dify_oapi.api.workflow.v1.resource.workflow import Workflow
from dify_oapi.core.model.config import Config
from dify_oapi.core.model.request_option import RequestOption


class TestComprehensiveIntegration:
    """Comprehensive integration tests for workflow API."""

    def setup_method(self) -> None:
        """Set up test fixtures."""
        self.config = Config()
        self.workflow = Workflow(self.config)
        self.request_option = RequestOption.builder().api_key("test-key").build()

    @patch("dify_oapi.core.http.transport.Transport.execute")
    def test_complete_workflow_cycle(self, mock_execute: Mock) -> None:
        """Test complete workflow cycle: Run → Detail → Stop."""
        # Mock responses
        run_response = RunWorkflowResponse(workflow_run_id="test-run-id", task_id="test-task-id")

        detail_response = GetWorkflowRunDetailResponse(status="running", id="test-run-id")

        stop_response = StopWorkflowResponse(result="success")

        mock_execute.side_effect = [run_response, detail_response, stop_response]

        # 1. Run workflow
        inputs = WorkflowInputs.builder().build()
        run_req_body = (
            RunWorkflowRequestBody.builder().inputs(inputs).response_mode("blocking").user("test-user").build()
        )
        run_req = RunWorkflowRequest.builder().request_body(run_req_body).build()

        run_result = self.workflow.run_workflow(run_req, self.request_option, False)
        assert run_result.workflow_run_id == "test-run-id"

        # 2. Get workflow detail
        detail_req = GetWorkflowRunDetailRequest.builder().workflow_run_id("test-run-id").build()
        detail_result = self.workflow.get_workflow_run_detail(detail_req, self.request_option)
        assert detail_result.status == "running"

        # 3. Stop workflow
        stop_req_body = StopWorkflowRequestBody.builder().user("test-user").build()
        stop_req = StopWorkflowRequest.builder().task_id("test-task-id").request_body(stop_req_body).build()
        stop_result = self.workflow.stop_workflow(stop_req, self.request_option)
        assert stop_result.result == "success"

    @patch("dify_oapi.core.http.transport.Transport.execute")
    def test_file_upload_and_workflow(self, mock_execute: Mock) -> None:
        """Test file upload and use in workflow."""
        # Mock responses
        upload_response = UploadFileResponse(id="test-file-id", name="test.txt")

        run_response = RunWorkflowResponse(workflow_run_id="test-run-id")

        mock_execute.side_effect = [upload_response, run_response]

        # 1. Upload file
        file_content = b"test content"
        file_stream = BytesIO(file_content)
        upload_req_body = UploadFileRequestBody.builder().user("test-user").build()
        upload_req = UploadFileRequest.builder().file(file_stream, "test.txt").request_body(upload_req_body).build()

        upload_result = self.workflow.upload_file(upload_req, self.request_option)
        assert upload_result.id == "test-file-id"

        # 2. Use file in workflow
        inputs = WorkflowInputs.builder().build()
        run_req_body = (
            RunWorkflowRequestBody.builder().inputs(inputs).response_mode("blocking").user("test-user").build()
        )
        run_req = RunWorkflowRequest.builder().request_body(run_req_body).build()

        run_result = self.workflow.run_workflow(run_req, self.request_option, False)
        assert run_result.workflow_run_id is not None

    @patch("dify_oapi.core.http.transport.Transport.execute")
    def test_workflow_monitoring(self, mock_execute: Mock) -> None:
        """Test workflow monitoring with logs and status tracking."""
        # Mock log response
        log_response = GetWorkflowLogsResponse(total=5, page=1, limit=10, has_more=False, data=[])

        mock_execute.return_value = log_response

        # Get workflow logs
        logs_req = GetWorkflowLogsRequest.builder().page(1).limit(10).build()
        logs_result = self.workflow.get_workflow_logs(logs_req, self.request_option)

        assert logs_result.total == 5
        assert logs_result.page == 1
        assert not logs_result.has_more

    def test_migrated_functionality(self) -> None:
        """Verify all migrated methods are available in consolidated resource."""
        # Check all 8 API methods exist
        assert hasattr(self.workflow, "run_workflow")
        assert hasattr(self.workflow, "arun_workflow")
        assert hasattr(self.workflow, "get_workflow_run_detail")
        assert hasattr(self.workflow, "aget_workflow_run_detail")
        assert hasattr(self.workflow, "stop_workflow")
        assert hasattr(self.workflow, "astop_workflow")
        assert hasattr(self.workflow, "upload_file")
        assert hasattr(self.workflow, "aupload_file")
        assert hasattr(self.workflow, "get_workflow_logs")
        assert hasattr(self.workflow, "aget_workflow_logs")
        assert hasattr(self.workflow, "get_info")
        assert hasattr(self.workflow, "aget_info")
        assert hasattr(self.workflow, "get_parameters")
        assert hasattr(self.workflow, "aget_parameters")
        assert hasattr(self.workflow, "get_site")
        assert hasattr(self.workflow, "aget_site")

    def test_import_path_migration(self) -> None:
        """Ensure all imports work with flat structure."""
        # Test that all model imports work from flat structure
        from dify_oapi.api.workflow.v1.model.get_info_request import GetInfoRequest
        from dify_oapi.api.workflow.v1.model.get_workflow_logs_request import GetWorkflowLogsRequest
        from dify_oapi.api.workflow.v1.model.run_workflow_request import RunWorkflowRequest
        from dify_oapi.api.workflow.v1.model.upload_file_request import UploadFileRequest

        # Verify classes can be instantiated
        assert RunWorkflowRequest.builder().build() is not None
        assert UploadFileRequest.builder().build() is not None
        assert GetWorkflowLogsRequest.builder().build() is not None
        assert GetInfoRequest.builder().build() is not None

    def test_no_regression(self) -> None:
        """Verify existing functionality unchanged."""
        # Test that all request builders work
        run_req = RunWorkflowRequest.builder().build()
        assert run_req.http_method.name == "POST"
        assert run_req.uri == "/v1/workflows/run"

        detail_req = GetWorkflowRunDetailRequest.builder().workflow_run_id("test-id").build()
        assert detail_req.http_method.name == "GET"
        assert detail_req.uri == "/v1/workflows/run/:workflow_run_id"
        assert detail_req.paths["workflow_run_id"] == "test-id"

        stop_req = StopWorkflowRequest.builder().task_id("test-task").build()
        assert stop_req.http_method.name == "POST"
        assert stop_req.uri == "/v1/workflows/tasks/:task_id/stop"
        assert stop_req.paths["task_id"] == "test-task"
