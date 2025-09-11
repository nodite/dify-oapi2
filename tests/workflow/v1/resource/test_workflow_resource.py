"""
Workflow Resource Tests

Test core business resources of the workflow module
"""

from unittest.mock import Mock, patch

import pytest

from dify_oapi.api.workflow.v1.resource.workflow import Workflow
from dify_oapi.core.model.config import Config
from dify_oapi.core.model.request_option import RequestOption


class TestWorkflowResource:
    """Workflow Resource Tests"""

    @pytest.fixture
    def config(self):
        return Config()

    @pytest.fixture
    def request_option(self):
        return RequestOption.builder().api_key("test-api-key").build()

    @pytest.fixture
    def workflow_resource(self, config):
        return Workflow(config)

    def test_workflow_resource_init(self, workflow_resource):
        """Test Workflow resource initialization"""
        assert workflow_resource.config is not None
        assert hasattr(workflow_resource, "run")
        assert hasattr(workflow_resource, "arun")
        assert hasattr(workflow_resource, "stop")
        assert hasattr(workflow_resource, "astop")
        assert hasattr(workflow_resource, "detail")
        assert hasattr(workflow_resource, "adetail")
        assert hasattr(workflow_resource, "logs")
        assert hasattr(workflow_resource, "alogs")

    @patch("dify_oapi.core.http.transport.Transport.execute")
    def test_run_method(self, mock_execute, workflow_resource, request_option):
        """Test run method"""
        from dify_oapi.api.workflow.v1.model.run_workflow_request import RunWorkflowRequest

        mock_response = Mock()
        mock_response.workflow_run_id = "run-123"
        mock_execute.return_value = mock_response

        request = RunWorkflowRequest.builder().build()
        response = workflow_resource.run(request, request_option, False)

        assert response.workflow_run_id == "run-123"
        mock_execute.assert_called_once()

    @patch("dify_oapi.core.http.transport.ATransport.aexecute")
    async def test_async_run_method(self, mock_aexecute, workflow_resource, request_option):
        """Test async run method"""
        from dify_oapi.api.workflow.v1.model.run_workflow_request import RunWorkflowRequest

        mock_response = Mock()
        mock_response.workflow_run_id = "async-run-123"
        mock_aexecute.return_value = mock_response

        request = RunWorkflowRequest.builder().build()
        response = await workflow_resource.arun(request, request_option, False)

        assert response.workflow_run_id == "async-run-123"
        mock_aexecute.assert_called_once()

    @patch("dify_oapi.core.http.transport.Transport.execute")
    def test_detail_method(self, mock_execute, workflow_resource, request_option):
        """Test detail method"""
        from dify_oapi.api.workflow.v1.model.get_workflow_run_detail_request import GetWorkflowRunDetailRequest

        mock_response = Mock()
        mock_response.status = "completed"
        mock_execute.return_value = mock_response

        request = GetWorkflowRunDetailRequest.builder().build()
        response = workflow_resource.detail(request, request_option)

        assert response.status == "completed"
        mock_execute.assert_called_once()

    @patch("dify_oapi.core.http.transport.Transport.execute")
    def test_logs_method(self, mock_execute, workflow_resource, request_option):
        """Test logs method"""
        from dify_oapi.api.workflow.v1.model.get_workflow_logs_request import GetWorkflowLogsRequest

        mock_response = Mock()
        mock_response.logs = ["log1", "log2"]
        mock_execute.return_value = mock_response

        request = GetWorkflowLogsRequest.builder().build()
        response = workflow_resource.logs(request, request_option)

        assert response.logs == ["log1", "log2"]
        mock_execute.assert_called_once()

    def test_workflow_resource_methods_exist(self, workflow_resource):
        """Test Workflow resource methods exist"""
        methods = ["run", "arun", "stop", "astop", "detail", "adetail", "logs", "alogs"]

        for method in methods:
            assert hasattr(workflow_resource, method)
            assert callable(getattr(workflow_resource, method))


if __name__ == "__main__":
    pytest.main([__file__])
