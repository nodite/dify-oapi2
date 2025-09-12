"""Tests for version integration after migration."""

from unittest.mock import Mock

from dify_oapi.api.workflow.service import WorkflowService
from dify_oapi.api.workflow.v1.resource.workflow import Workflow
from dify_oapi.api.workflow.v1.version import V1
from dify_oapi.core.model.config import Config


class TestVersionIntegration:
    """Test version integration after migration."""

    def test_v1_workflow_resource_access(self) -> None:
        """Test consolidated resource accessibility."""
        config = Mock(spec=Config)
        v1 = V1(config)

        # Test that only workflow resource is exposed
        assert hasattr(v1, "workflow")
        assert isinstance(v1.workflow, Workflow)

        # Test that old resources are no longer exposed
        assert not hasattr(v1, "file")
        assert not hasattr(v1, "log")
        assert not hasattr(v1, "info")

    def test_workflow_service_integration(self) -> None:
        """Test service integration after migration."""
        config = Mock(spec=Config)
        service = WorkflowService(config)

        # Test service has v1 version
        assert hasattr(service, "v1")
        assert isinstance(service.v1, V1)

        # Test v1 has consolidated workflow resource
        assert hasattr(service.v1, "workflow")
        assert isinstance(service.v1.workflow, Workflow)

    def test_consolidated_workflow_methods(self) -> None:
        """Test all methods available in consolidated workflow resource."""
        config = Mock(spec=Config)
        workflow = Workflow(config)

        # Test workflow execution methods
        assert hasattr(workflow, "run")
        assert hasattr(workflow, "arun")
        assert hasattr(workflow, "detail")
        assert hasattr(workflow, "adetail")
        assert hasattr(workflow, "stop")
        assert hasattr(workflow, "astop")

        # Test file methods (migrated from File resource)
        assert hasattr(workflow, "upload")
        assert hasattr(workflow, "aupload")

        # Test log methods (migrated from Log resource)
        assert hasattr(workflow, "logs")
        assert hasattr(workflow, "alogs")

        # Test info methods (migrated from Info resource)
        assert hasattr(workflow, "info")
        assert hasattr(workflow, "ainfo")
        assert hasattr(workflow, "parameters")
        assert hasattr(workflow, "aparameters")
        assert hasattr(workflow, "site")
        assert hasattr(workflow, "asite")

    def test_migration_completeness(self) -> None:
        """Test migration completeness - all expected methods present."""
        config = Mock(spec=Config)
        workflow = Workflow(config)

        # Expected method count: 14 methods (7 sync + 7 async)
        expected_methods = [
            "run",
            "arun",
            "detail",
            "adetail",
            "stop",
            "astop",
            "upload",
            "aupload",
            "logs",
            "alogs",
            "info",
            "ainfo",
            "parameters",
            "aparameters",
            "site",
            "asite",
        ]

        for method_name in expected_methods:
            assert hasattr(workflow, method_name), f"Missing method: {method_name}"
            assert callable(getattr(workflow, method_name)), f"Method not callable: {method_name}"
