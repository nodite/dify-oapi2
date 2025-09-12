"""Workflow resource tests."""

from unittest.mock import MagicMock, patch

import pytest

from dify_oapi.api.workflow.v1.resource.workflow import Workflow
from dify_oapi.core.model.request_option import RequestOption


class TestWorkflow:
    """Test Workflow resource."""

    @pytest.fixture
    def workflow(self, mock_config):
        """Create Workflow instance."""
        return Workflow(mock_config)

    @pytest.fixture
    def request_option(self):
        """Create request option."""
        return RequestOption.builder().api_key("test-key").build()

    def test_run(self, workflow, request_option):
        """Test run workflow."""
        with patch("dify_oapi.core.http.transport.Transport.execute") as mock_execute:
            mock_execute.return_value = MagicMock(workflow_run_id="run-123")
            result = workflow.run(MagicMock(), request_option)
            assert result.workflow_run_id == "run-123"

    def test_stop(self, workflow, request_option):
        """Test stop workflow."""
        with patch("dify_oapi.core.http.transport.Transport.execute") as mock_execute:
            mock_execute.return_value = MagicMock(result="stopped")
            result = workflow.stop(MagicMock(), request_option)
            assert result.result == "stopped"

    def test_detail(self, workflow, request_option):
        """Test get workflow run detail."""
        with patch("dify_oapi.core.http.transport.Transport.execute") as mock_execute:
            mock_execute.return_value = MagicMock(id="run-123")
            result = workflow.detail(MagicMock(), request_option)
            assert result.id == "run-123"

    def test_logs(self, workflow, request_option):
        """Test get workflow logs."""
        with patch("dify_oapi.core.http.transport.Transport.execute") as mock_execute:
            mock_execute.return_value = MagicMock(data=[])
            result = workflow.logs(MagicMock(), request_option)
            assert result.data == []
