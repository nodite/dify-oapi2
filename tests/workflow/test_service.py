"""Workflow service tests."""

import pytest

from dify_oapi.api.workflow.service import WorkflowService
from dify_oapi.api.workflow.v1.version import V1


class TestWorkflowService:
    """Test Workflow service."""

    @pytest.fixture
    def service(self, mock_config):
        """Create WorkflowService instance."""
        return WorkflowService(mock_config)

    def test_service_has_v1(self, service):
        """Test service has v1."""
        assert hasattr(service, "v1")
        assert isinstance(service.v1, V1)

    def test_v1_resources(self, service):
        """Test v1 resources."""
        v1 = service.v1
        assert hasattr(v1, "workflow")
