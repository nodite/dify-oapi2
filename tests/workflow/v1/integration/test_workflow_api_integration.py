"""Comprehensive integration tests for workflow API functionality."""

from __future__ import annotations

from unittest.mock import AsyncMock, Mock, patch

import pytest

from dify_oapi.api.workflow.v1.model.file.file_info import FileInfo
from dify_oapi.api.workflow.v1.model.file.preview_file_request import PreviewFileRequest
from dify_oapi.api.workflow.v1.model.file.preview_file_response import PreviewFileResponse
from dify_oapi.api.workflow.v1.model.file.upload_file_request import UploadFileRequest
from dify_oapi.api.workflow.v1.model.file.upload_file_request_body import UploadFileRequestBody
from dify_oapi.api.workflow.v1.model.file.upload_file_response import UploadFileResponse
from dify_oapi.api.workflow.v1.model.info.get_info_request import GetInfoRequest
from dify_oapi.api.workflow.v1.model.info.get_info_response import GetInfoResponse
from dify_oapi.api.workflow.v1.model.info.get_parameters_request import GetParametersRequest
from dify_oapi.api.workflow.v1.model.info.get_parameters_response import GetParametersResponse
from dify_oapi.api.workflow.v1.model.info.get_site_request import GetSiteRequest
from dify_oapi.api.workflow.v1.model.info.get_site_response import GetSiteResponse
from dify_oapi.api.workflow.v1.model.log.get_workflow_logs_request import GetWorkflowLogsRequest
from dify_oapi.api.workflow.v1.model.log.get_workflow_logs_response import GetWorkflowLogsResponse
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
from dify_oapi.api.workflow.v1.version import V1
from dify_oapi.core.model.config import Config
from dify_oapi.core.model.request_option import RequestOption


class TestWorkflowAPIIntegration:
    """Comprehensive integration tests for workflow API functionality."""

    @pytest.fixture
    def config(self) -> Config:
        """Create test config."""
        config = Config()
        config.domain = "https://api.dify.ai"
        return config

    @pytest.fixture
    def request_option(self) -> RequestOption:
        """Create test request option."""
        return RequestOption.builder().api_key("test-api-key").build()

    @pytest.fixture
    def workflow_v1(self, config: Config) -> V1:
        """Create workflow V1 instance."""
        return V1(config)

    # ===== COMPLETE WORKFLOW LIFECYCLE TESTS =====

    @patch("dify_oapi.core.http.transport.sync_transport.Transport.execute")
    def test_complete_workflow_lifecycle_sync(
        self, mock_execute: Mock, workflow_v1: V1, request_option: RequestOption
    ) -> None:
        """Test complete workflow lifecycle synchronously."""
        # Mock run workflow response
        run_response = RunWorkflowResponse()
        run_response.workflow_run_id = "test-run-id"
        run_response.task_id = "test-task-id"
        run_response.code = None  # None means success
        mock_execute.return_value = run_response

        # Test run workflow
        inputs = WorkflowInputs.builder().build()
        request_body = (
            RunWorkflowRequestBody.builder().inputs(inputs).response_mode("blocking").user("test-user").build()
        )
        request = RunWorkflowRequest.builder().request_body(request_body).build()

        result = workflow_v1.workflow.run_workflow(request, request_option, False)
        assert result.success is True
        assert result.workflow_run_id == "test-run-id"

        # Mock get workflow run detail response
        detail_response = GetWorkflowRunDetailResponse()
        detail_response.id = "test-run-id"
        detail_response.status = "succeeded"
        detail_response.code = None  # None means success
        mock_execute.return_value = detail_response

        # Test get workflow run detail
        detail_request = GetWorkflowRunDetailRequest.builder().workflow_run_id("test-run-id").build()
        detail_result = workflow_v1.workflow.get_workflow_run_detail(detail_request, request_option)
        assert detail_result.success is True
        assert detail_result.id == "test-run-id"
        assert detail_result.status == "succeeded"

        # Mock stop workflow response
        stop_response = StopWorkflowResponse()
        stop_response.result = "success"
        stop_response.code = None  # None means success
        mock_execute.return_value = stop_response

        # Test stop workflow
        stop_request_body = StopWorkflowRequestBody.builder().user("test-user").build()
        stop_request = StopWorkflowRequest.builder().task_id("test-task-id").request_body(stop_request_body).build()
        stop_result = workflow_v1.workflow.stop_workflow(stop_request, request_option)
        assert stop_result.success is True
        assert stop_result.result == "success"

    @patch("dify_oapi.core.http.transport.async_transport.ATransport.aexecute")
    @pytest.mark.asyncio
    async def test_complete_workflow_lifecycle_async(
        self, mock_aexecute: AsyncMock, workflow_v1: V1, request_option: RequestOption
    ) -> None:
        """Test complete workflow lifecycle asynchronously."""
        # Mock run workflow response
        run_response = RunWorkflowResponse()
        run_response.workflow_run_id = "test-run-id"
        run_response.task_id = "test-task-id"
        run_response.code = None  # None means success
        mock_aexecute.return_value = run_response

        # Test run workflow
        inputs = WorkflowInputs.builder().build()
        request_body = (
            RunWorkflowRequestBody.builder().inputs(inputs).response_mode("blocking").user("test-user").build()
        )
        request = RunWorkflowRequest.builder().request_body(request_body).build()

        result = await workflow_v1.workflow.arun_workflow(request, request_option, False)
        assert result.success is True
        assert result.workflow_run_id == "test-run-id"

    @patch("dify_oapi.core.http.transport.sync_transport.Transport.execute")
    def test_run_specific_workflow_version(
        self, mock_execute: Mock, workflow_v1: V1, request_option: RequestOption
    ) -> None:
        """Test running specific workflow version."""
        # Mock response
        response = RunSpecificWorkflowResponse()
        response.workflow_run_id = "specific-run-id"
        response.code = None  # None means success
        mock_execute.return_value = response

        # Test run specific workflow
        inputs = WorkflowInputs.builder().build()
        request_body = (
            RunSpecificWorkflowRequestBody.builder().inputs(inputs).response_mode("blocking").user("test-user").build()
        )
        request = (
            RunSpecificWorkflowRequest.builder().workflow_id("test-workflow-id").request_body(request_body).build()
        )

        result = workflow_v1.workflow.run_specific_workflow(request, request_option, False)
        assert result.success is True
        assert result.workflow_run_id == "specific-run-id"

    # ===== FILE MANAGEMENT TESTS =====

    @patch("dify_oapi.core.http.transport.sync_transport.Transport.execute")
    def test_file_management_lifecycle(
        self, mock_execute: Mock, workflow_v1: V1, request_option: RequestOption
    ) -> None:
        """Test complete file management lifecycle."""
        # Mock upload file response
        upload_response = UploadFileResponse()
        upload_response.id = "test-file-id"
        upload_response.name = "test-file.txt"
        upload_response.code = None  # None means success
        mock_execute.return_value = upload_response

        # Test file upload
        from io import BytesIO

        file_content = BytesIO(b"test file content")
        request_body = UploadFileRequestBody.builder().user("test-user").build()
        upload_request = (
            UploadFileRequest.builder().file(file_content, "test-file.txt").request_body(request_body).build()
        )

        upload_result = workflow_v1.file.upload_file(upload_request, request_option)
        assert upload_result.success is True
        assert upload_result.id == "test-file-id"

        # Mock preview file response
        preview_response = PreviewFileResponse()
        preview_response.content_type = "text/plain"
        preview_response.code = None  # None means success
        mock_execute.return_value = preview_response

        # Test file preview
        preview_request = PreviewFileRequest.builder().file_id("test-file-id").as_attachment(False).build()
        preview_result = workflow_v1.file.preview_file(preview_request, request_option)
        assert preview_result.success is True
        assert preview_result.content_type == "text/plain"

    @patch("dify_oapi.core.http.transport.async_transport.ATransport.aexecute")
    @pytest.mark.asyncio
    async def test_file_upload_async(
        self, mock_aexecute: AsyncMock, workflow_v1: V1, request_option: RequestOption
    ) -> None:
        """Test file upload asynchronously."""
        # Mock response
        response = UploadFileResponse()
        response.id = "async-file-id"
        response.code = None  # None means success
        mock_aexecute.return_value = response

        # Test async file upload
        from io import BytesIO

        file_content = BytesIO(b"async test content")
        request_body = UploadFileRequestBody.builder().user("test-user").build()
        request = UploadFileRequest.builder().file(file_content, "async-test.txt").request_body(request_body).build()

        result = await workflow_v1.file.aupload_file(request, request_option)
        assert result.success is True
        assert result.id == "async-file-id"

    # ===== WORKFLOW MONITORING TESTS =====

    @patch("dify_oapi.core.http.transport.sync_transport.Transport.execute")
    def test_workflow_monitoring(self, mock_execute: Mock, workflow_v1: V1, request_option: RequestOption) -> None:
        """Test workflow execution monitoring."""
        # Mock get workflow logs response
        logs_response = GetWorkflowLogsResponse()
        logs_response.page = 1
        logs_response.limit = 20
        logs_response.total = 100
        logs_response.has_more = True
        logs_response.code = None  # None means success
        mock_execute.return_value = logs_response

        # Test get workflow logs
        logs_request = GetWorkflowLogsRequest.builder().keyword("test").status("succeeded").page(1).limit(20).build()
        logs_result = workflow_v1.log.get_workflow_logs(logs_request, request_option)
        assert logs_result.success is True
        assert logs_result.page == 1
        assert logs_result.total == 100

    @patch("dify_oapi.core.http.transport.async_transport.ATransport.aexecute")
    @pytest.mark.asyncio
    async def test_workflow_logs_async(
        self, mock_aexecute: AsyncMock, workflow_v1: V1, request_option: RequestOption
    ) -> None:
        """Test workflow logs retrieval asynchronously."""
        # Mock response
        response = GetWorkflowLogsResponse()
        response.page = 1
        response.code = None  # None means success
        mock_aexecute.return_value = response

        # Test async logs retrieval
        request = GetWorkflowLogsRequest.builder().page(1).build()
        result = await workflow_v1.log.aget_workflow_logs(request, request_option)
        assert result.success is True
        assert result.page == 1

    # ===== APPLICATION CONFIGURATION TESTS =====

    @patch("dify_oapi.core.http.transport.sync_transport.Transport.execute")
    def test_application_configuration(
        self, mock_execute: Mock, workflow_v1: V1, request_option: RequestOption
    ) -> None:
        """Test application configuration retrieval."""
        # Mock get info response
        info_response = GetInfoResponse()
        info_response.name = "Test App"
        info_response.mode = "workflow"
        info_response.code = None  # None means success
        mock_execute.return_value = info_response

        # Test get info
        info_request = GetInfoRequest.builder().build()
        info_result = workflow_v1.info.get_info(info_request, request_option)
        assert info_result.success is True
        assert info_result.name == "Test App"
        assert info_result.mode == "workflow"

        # Mock get parameters response
        params_response = GetParametersResponse()
        params_response.code = None  # None means success
        mock_execute.return_value = params_response

        # Test get parameters
        params_request = GetParametersRequest.builder().build()
        params_result = workflow_v1.info.get_parameters(params_request, request_option)
        assert params_result.success is True

        # Mock get site response
        site_response = GetSiteResponse()
        site_response.title = "Test Site"
        site_response.code = None  # None means success
        mock_execute.return_value = site_response

        # Test get site
        site_request = GetSiteRequest.builder().build()
        site_result = workflow_v1.info.get_site(site_request, request_option)
        assert site_result.success is True
        assert site_result.title == "Test Site"

    @patch("dify_oapi.core.http.transport.async_transport.ATransport.aexecute")
    @pytest.mark.asyncio
    async def test_application_info_async(
        self, mock_aexecute: AsyncMock, workflow_v1: V1, request_option: RequestOption
    ) -> None:
        """Test application info retrieval asynchronously."""
        # Mock response
        response = GetInfoResponse()
        response.name = "Async Test App"
        response.code = None  # None means success
        mock_aexecute.return_value = response

        # Test async info retrieval
        request = GetInfoRequest.builder().build()
        result = await workflow_v1.info.aget_info(request, request_option)
        assert result.success is True
        assert result.name == "Async Test App"

    # ===== ERROR SCENARIOS TESTS =====

    @patch("dify_oapi.core.http.transport.sync_transport.Transport.execute")
    def test_invalid_api_key_error(self, mock_execute: Mock, workflow_v1: V1) -> None:
        """Test invalid API key error handling."""
        # Mock error response
        error_response = RunWorkflowResponse()
        error_response.code = "401"
        error_response.msg_ = "Invalid API key"
        mock_execute.return_value = error_response

        # Test with invalid API key
        invalid_option = RequestOption.builder().api_key("invalid-key").build()
        inputs = WorkflowInputs.builder().build()
        request_body = (
            RunWorkflowRequestBody.builder().inputs(inputs).response_mode("blocking").user("test-user").build()
        )
        request = RunWorkflowRequest.builder().request_body(request_body).build()

        result = workflow_v1.workflow.run_workflow(request, invalid_option, False)
        assert result.success is False
        assert result.code == "401"
        assert result.msg == "Invalid API key"

    @patch("dify_oapi.core.http.transport.sync_transport.Transport.execute")
    def test_missing_required_fields_error(
        self, mock_execute: Mock, workflow_v1: V1, request_option: RequestOption
    ) -> None:
        """Test missing required fields error handling."""
        # Mock error response
        error_response = RunWorkflowResponse()
        error_response.code = "400"
        error_response.msg_ = "Missing required field: user"
        mock_execute.return_value = error_response

        # Test with missing required fields
        inputs = WorkflowInputs.builder().build()
        request_body = (
            RunWorkflowRequestBody.builder()
            .inputs(inputs)
            .response_mode("blocking")
            # Missing user field
            .build()
        )
        request = RunWorkflowRequest.builder().request_body(request_body).build()

        result = workflow_v1.workflow.run_workflow(request, request_option, False)
        assert result.success is False
        assert result.code == "400"
        assert result.msg is not None and "Missing required field" in result.msg

    @patch("dify_oapi.core.http.transport.sync_transport.Transport.execute")
    def test_network_error_handling(self, mock_execute: Mock, workflow_v1: V1, request_option: RequestOption) -> None:
        """Test network error handling."""
        # Mock network error
        mock_execute.side_effect = Exception("Network connection failed")

        # Test network error handling
        inputs = WorkflowInputs.builder().build()
        request_body = (
            RunWorkflowRequestBody.builder().inputs(inputs).response_mode("blocking").user("test-user").build()
        )
        request = RunWorkflowRequest.builder().request_body(request_body).build()

        with pytest.raises(Exception) as exc_info:
            workflow_v1.workflow.run_workflow(request, request_option, False)
        assert "Network connection failed" in str(exc_info.value)

    @patch("dify_oapi.core.http.transport.sync_transport.Transport.execute")
    def test_permission_error_handling(
        self, mock_execute: Mock, workflow_v1: V1, request_option: RequestOption
    ) -> None:
        """Test permission error handling."""
        # Mock permission error response
        error_response = GetWorkflowLogsResponse()
        error_response.code = "403"
        error_response.msg_ = "Permission denied"
        mock_execute.return_value = error_response

        # Test permission error
        request = GetWorkflowLogsRequest.builder().build()
        result = workflow_v1.log.get_workflow_logs(request, request_option)
        assert result.success is False
        assert result.code == "403"
        assert result.msg == "Permission denied"

    # ===== STREAMING FUNCTIONALITY TESTS =====

    @patch("dify_oapi.core.http.transport.sync_transport.Transport.execute")
    def test_streaming_workflow_execution(
        self, mock_execute: Mock, workflow_v1: V1, request_option: RequestOption
    ) -> None:
        """Test streaming workflow execution."""
        # Mock streaming response
        mock_execute.return_value = iter([b"chunk1", b"chunk2", b"chunk3"])

        # Test streaming workflow
        inputs = WorkflowInputs.builder().build()
        request_body = (
            RunWorkflowRequestBody.builder().inputs(inputs).response_mode("streaming").user("test-user").build()
        )
        request = RunWorkflowRequest.builder().request_body(request_body).build()

        result = workflow_v1.workflow.run_workflow(request, request_option, True)
        chunks = list(result)
        assert chunks == [b"chunk1", b"chunk2", b"chunk3"]

    @patch("dify_oapi.core.http.transport.async_transport.ATransport.aexecute")
    @pytest.mark.asyncio
    async def test_streaming_workflow_execution_async(
        self, mock_aexecute: AsyncMock, workflow_v1: V1, request_option: RequestOption
    ) -> None:
        """Test streaming workflow execution asynchronously."""

        # Mock async streaming response
        async def async_generator():
            for chunk in [b"async_chunk1", b"async_chunk2"]:
                yield chunk

        mock_aexecute.return_value = async_generator()

        # Test async streaming workflow
        inputs = WorkflowInputs.builder().build()
        request_body = (
            RunWorkflowRequestBody.builder().inputs(inputs).response_mode("streaming").user("test-user").build()
        )
        request = RunWorkflowRequest.builder().request_body(request_body).build()

        result = await workflow_v1.workflow.arun_workflow(request, request_option, True)
        chunks = []
        async for chunk in result:
            chunks.append(chunk)
        assert chunks == [b"async_chunk1", b"async_chunk2"]

    # ===== INTEGRATION WITH FILES IN WORKFLOWS =====

    @patch("dify_oapi.core.http.transport.sync_transport.Transport.execute")
    def test_workflow_with_file_inputs(
        self, mock_execute: Mock, workflow_v1: V1, request_option: RequestOption
    ) -> None:
        """Test workflow execution with file inputs."""
        # Mock file upload first
        upload_response = UploadFileResponse()
        upload_response.id = "file-for-workflow"
        upload_response.code = None  # None means success
        mock_execute.return_value = upload_response

        # Upload file
        from io import BytesIO

        file_content = BytesIO(b"workflow input file")
        request_body = UploadFileRequestBody.builder().user("test-user").build()
        upload_request = UploadFileRequest.builder().file(file_content, "input.txt").request_body(request_body).build()
        upload_result = workflow_v1.file.upload_file(upload_request, request_option)
        assert upload_result.success is True

        # Mock workflow execution with file
        workflow_response = RunWorkflowResponse()
        workflow_response.workflow_run_id = "workflow-with-file"
        workflow_response.code = None  # None means success
        mock_execute.return_value = workflow_response

        # Run workflow with file input
        file_info = FileInfo.builder().id("file-for-workflow").name("input.txt").build()
        inputs = WorkflowInputs.builder().build()
        workflow_request_body = (
            RunWorkflowRequestBody.builder()
            .inputs(inputs)
            .response_mode("blocking")
            .user("test-user")
            .files([file_info])
            .build()
        )
        workflow_request = RunWorkflowRequest.builder().request_body(workflow_request_body).build()

        workflow_result = workflow_v1.workflow.run_workflow(workflow_request, request_option, False)
        assert workflow_result.success is True
        assert workflow_result.workflow_run_id == "workflow-with-file"

    # ===== END-TO-END INTEGRATION TEST =====

    @patch("dify_oapi.core.http.transport.sync_transport.Transport.execute")
    def test_end_to_end_workflow_integration(
        self, mock_execute: Mock, workflow_v1: V1, request_option: RequestOption
    ) -> None:
        """Test complete end-to-end workflow integration."""
        self._test_app_info_and_params(mock_execute, workflow_v1, request_option)
        self._test_file_upload_and_workflow(mock_execute, workflow_v1, request_option)
        self._test_workflow_details_and_logs(mock_execute, workflow_v1, request_option)

    def _test_app_info_and_params(self, mock_execute: Mock, workflow_v1: V1, request_option: RequestOption) -> None:
        """Test application info and parameters retrieval."""
        # Step 1: Get application info
        info_response = GetInfoResponse()
        info_response.name = "Integration Test App"
        info_response.mode = "workflow"
        info_response.code = None
        mock_execute.return_value = info_response

        info_request = GetInfoRequest.builder().build()
        info_result = workflow_v1.info.get_info(info_request, request_option)
        assert info_result.success is True

        # Step 2: Get application parameters
        params_response = GetParametersResponse()
        params_response.code = None
        mock_execute.return_value = params_response

        params_request = GetParametersRequest.builder().build()
        params_result = workflow_v1.info.get_parameters(params_request, request_option)
        assert params_result.success is True

    def _test_file_upload_and_workflow(
        self, mock_execute: Mock, workflow_v1: V1, request_option: RequestOption
    ) -> None:
        """Test file upload and workflow execution."""
        from io import BytesIO

        # Step 3: Upload file for workflow
        upload_response = UploadFileResponse()
        upload_response.id = "integration-file"
        upload_response.code = None
        mock_execute.return_value = upload_response

        file_content = BytesIO(b"integration test file")
        upload_request_body = UploadFileRequestBody.builder().user("integration-user").build()
        upload_request = (
            UploadFileRequest.builder().file(file_content, "integration.txt").request_body(upload_request_body).build()
        )
        upload_result = workflow_v1.file.upload_file(upload_request, request_option)
        assert upload_result.success is True

        # Step 4: Run workflow with uploaded file
        workflow_response = RunWorkflowResponse()
        workflow_response.workflow_run_id = "integration-run"
        workflow_response.task_id = "integration-task"
        workflow_response.code = None
        mock_execute.return_value = workflow_response

        file_info = FileInfo.builder().id("integration-file").build()
        inputs = WorkflowInputs.builder().build()
        workflow_request_body = (
            RunWorkflowRequestBody.builder()
            .inputs(inputs)
            .response_mode("blocking")
            .user("integration-user")
            .files([file_info])
            .build()
        )
        workflow_request = RunWorkflowRequest.builder().request_body(workflow_request_body).build()
        workflow_result = workflow_v1.workflow.run_workflow(workflow_request, request_option, False)
        assert workflow_result.success is True

    def _test_workflow_details_and_logs(
        self, mock_execute: Mock, workflow_v1: V1, request_option: RequestOption
    ) -> None:
        """Test workflow details and logs retrieval."""
        # Step 5: Get workflow execution details
        detail_response = GetWorkflowRunDetailResponse()
        detail_response.id = "integration-run"
        detail_response.status = "succeeded"
        detail_response.code = None
        mock_execute.return_value = detail_response

        detail_request = GetWorkflowRunDetailRequest.builder().workflow_run_id("integration-run").build()
        detail_result = workflow_v1.workflow.get_workflow_run_detail(detail_request, request_option)
        assert detail_result.success is True
        assert detail_result.status == "succeeded"

        # Step 6: Get workflow logs
        logs_response = GetWorkflowLogsResponse()
        logs_response.total = 1
        logs_response.code = None
        mock_execute.return_value = logs_response

        logs_request = GetWorkflowLogsRequest.builder().build()
        logs_result = workflow_v1.log.get_workflow_logs(logs_request, request_option)
        assert logs_result.success is True
        assert logs_result.total == 1
