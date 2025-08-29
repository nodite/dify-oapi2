"""Tests for consolidated Workflow resource class."""

from unittest.mock import Mock

import pytest

from dify_oapi.api.workflow.v1.model.get_info_request import GetInfoRequest
from dify_oapi.api.workflow.v1.model.get_info_response import GetInfoResponse
from dify_oapi.api.workflow.v1.model.get_parameters_request import GetParametersRequest
from dify_oapi.api.workflow.v1.model.get_parameters_response import GetParametersResponse
from dify_oapi.api.workflow.v1.model.get_site_request import GetSiteRequest
from dify_oapi.api.workflow.v1.model.get_site_response import GetSiteResponse
from dify_oapi.api.workflow.v1.model.get_workflow_logs_request import GetWorkflowLogsRequest
from dify_oapi.api.workflow.v1.model.get_workflow_logs_response import GetWorkflowLogsResponse
from dify_oapi.api.workflow.v1.model.get_workflow_run_detail_request import GetWorkflowRunDetailRequest
from dify_oapi.api.workflow.v1.model.get_workflow_run_detail_response import GetWorkflowRunDetailResponse
from dify_oapi.api.workflow.v1.model.run_workflow_request import RunWorkflowRequest
from dify_oapi.api.workflow.v1.model.run_workflow_response import RunWorkflowResponse
from dify_oapi.api.workflow.v1.model.stop_workflow_request import StopWorkflowRequest
from dify_oapi.api.workflow.v1.model.stop_workflow_response import StopWorkflowResponse
from dify_oapi.api.workflow.v1.model.upload_file_request import UploadFileRequest
from dify_oapi.api.workflow.v1.model.upload_file_response import UploadFileResponse
from dify_oapi.api.workflow.v1.resource.workflow import Workflow
from dify_oapi.core.model.config import Config
from dify_oapi.core.model.request_option import RequestOption


class TestWorkflowResource:
    """Test consolidated Workflow resource class."""

    @pytest.fixture
    def workflow_resource(self) -> Workflow:
        """Create workflow resource instance."""
        config = Mock(spec=Config)
        return Workflow(config)

    @pytest.fixture
    def request_option(self) -> RequestOption:
        """Create request option."""
        return RequestOption.builder().api_key("test-api-key").build()

    def test_run_workflow_sync(self, workflow_resource: Workflow, request_option: RequestOption) -> None:
        """Test sync workflow execution."""
        request = RunWorkflowRequest.builder().build()

        with pytest.MonkeyPatch().context() as m:
            mock_transport = Mock()
            mock_transport.execute.return_value = RunWorkflowResponse()
            m.setattr("dify_oapi.api.workflow.v1.resource.workflow.Transport", mock_transport)

            result = workflow_resource.run_workflow(request, request_option, False)

            assert isinstance(result, RunWorkflowResponse)
            mock_transport.execute.assert_called_once()

    def test_get_workflow_run_detail(self, workflow_resource: Workflow, request_option: RequestOption) -> None:
        """Test get workflow run detail."""
        request = GetWorkflowRunDetailRequest.builder().workflow_run_id("run-123").build()

        with pytest.MonkeyPatch().context() as m:
            mock_transport = Mock()
            mock_transport.execute.return_value = GetWorkflowRunDetailResponse()
            m.setattr("dify_oapi.api.workflow.v1.resource.workflow.Transport", mock_transport)

            result = workflow_resource.get_workflow_run_detail(request, request_option)

            assert isinstance(result, GetWorkflowRunDetailResponse)
            mock_transport.execute.assert_called_once()

    def test_stop_workflow(self, workflow_resource: Workflow, request_option: RequestOption) -> None:
        """Test stop workflow."""
        request = StopWorkflowRequest.builder().task_id("task-123").build()

        with pytest.MonkeyPatch().context() as m:
            mock_transport = Mock()
            mock_transport.execute.return_value = StopWorkflowResponse()
            m.setattr("dify_oapi.api.workflow.v1.resource.workflow.Transport", mock_transport)

            result = workflow_resource.stop_workflow(request, request_option)

            assert isinstance(result, StopWorkflowResponse)
            mock_transport.execute.assert_called_once()

    def test_upload_file(self, workflow_resource: Workflow, request_option: RequestOption) -> None:
        """Test file upload."""
        request = UploadFileRequest.builder().build()

        with pytest.MonkeyPatch().context() as m:
            mock_transport = Mock()
            mock_transport.execute.return_value = UploadFileResponse()
            m.setattr("dify_oapi.api.workflow.v1.resource.workflow.Transport", mock_transport)

            result = workflow_resource.upload_file(request, request_option)

            assert isinstance(result, UploadFileResponse)
            mock_transport.execute.assert_called_once()

    def test_get_workflow_logs(self, workflow_resource: Workflow, request_option: RequestOption) -> None:
        """Test get workflow logs."""
        request = GetWorkflowLogsRequest.builder().build()

        with pytest.MonkeyPatch().context() as m:
            mock_transport = Mock()
            mock_transport.execute.return_value = GetWorkflowLogsResponse()
            m.setattr("dify_oapi.api.workflow.v1.resource.workflow.Transport", mock_transport)

            result = workflow_resource.get_workflow_logs(request, request_option)

            assert isinstance(result, GetWorkflowLogsResponse)
            mock_transport.execute.assert_called_once()

    def test_get_info(self, workflow_resource: Workflow, request_option: RequestOption) -> None:
        """Test get application info."""
        request = GetInfoRequest.builder().build()

        with pytest.MonkeyPatch().context() as m:
            mock_transport = Mock()
            mock_transport.execute.return_value = GetInfoResponse()
            m.setattr("dify_oapi.api.workflow.v1.resource.workflow.Transport", mock_transport)

            result = workflow_resource.get_info(request, request_option)

            assert isinstance(result, GetInfoResponse)
            mock_transport.execute.assert_called_once()

    def test_get_parameters(self, workflow_resource: Workflow, request_option: RequestOption) -> None:
        """Test get application parameters."""
        request = GetParametersRequest.builder().build()

        with pytest.MonkeyPatch().context() as m:
            mock_transport = Mock()
            mock_transport.execute.return_value = GetParametersResponse()
            m.setattr("dify_oapi.api.workflow.v1.resource.workflow.Transport", mock_transport)

            result = workflow_resource.get_parameters(request, request_option)

            assert isinstance(result, GetParametersResponse)
            mock_transport.execute.assert_called_once()

    def test_get_site(self, workflow_resource: Workflow, request_option: RequestOption) -> None:
        """Test get site settings."""
        request = GetSiteRequest.builder().build()

        with pytest.MonkeyPatch().context() as m:
            mock_transport = Mock()
            mock_transport.execute.return_value = GetSiteResponse()
            m.setattr("dify_oapi.api.workflow.v1.resource.workflow.Transport", mock_transport)

            result = workflow_resource.get_site(request, request_option)

            assert isinstance(result, GetSiteResponse)
            mock_transport.execute.assert_called_once()
