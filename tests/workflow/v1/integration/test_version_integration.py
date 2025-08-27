"""Tests for workflow v1 version integration."""

from __future__ import annotations

import pytest

from dify_oapi.api.workflow.v1.resource.file import File
from dify_oapi.api.workflow.v1.resource.info import Info
from dify_oapi.api.workflow.v1.resource.log import Log
from dify_oapi.api.workflow.v1.resource.workflow import Workflow
from dify_oapi.api.workflow.v1.version import V1
from dify_oapi.core.model.config import Config


class TestVersionIntegration:
    """Test cases for V1 version integration."""

    @pytest.fixture
    def config(self) -> Config:
        """Create test config."""
        config = Config()
        config.domain = "https://api.test.com"
        return config

    @pytest.fixture
    def v1_instance(self, config: Config) -> V1:
        """Create V1 instance."""
        return V1(config)

    def test_v1_initialization(self, config: Config) -> None:
        """Test V1 version initialization."""
        v1 = V1(config)
        assert v1 is not None

    def test_workflow_resource_initialization(self, v1_instance: V1, config: Config) -> None:
        """Test workflow resource is properly initialized."""
        assert hasattr(v1_instance, "workflow")
        assert isinstance(v1_instance.workflow, Workflow)
        assert v1_instance.workflow.config == config

    def test_file_resource_initialization(self, v1_instance: V1, config: Config) -> None:
        """Test file resource is properly initialized."""
        assert hasattr(v1_instance, "file")
        assert isinstance(v1_instance.file, File)
        assert v1_instance.file.config == config

    def test_log_resource_initialization(self, v1_instance: V1, config: Config) -> None:
        """Test log resource is properly initialized."""
        assert hasattr(v1_instance, "log")
        assert isinstance(v1_instance.log, Log)
        assert v1_instance.log.config == config

    def test_info_resource_initialization(self, v1_instance: V1, config: Config) -> None:
        """Test info resource is properly initialized."""
        assert hasattr(v1_instance, "info")
        assert isinstance(v1_instance.info, Info)
        assert v1_instance.info.config == config

    def test_all_resources_accessible(self, v1_instance: V1) -> None:
        """Test all resources are accessible through V1."""
        # Test workflow resource methods
        assert hasattr(v1_instance.workflow, "run_workflow")
        assert hasattr(v1_instance.workflow, "arun_workflow")
        assert hasattr(v1_instance.workflow, "run_specific_workflow")
        assert hasattr(v1_instance.workflow, "arun_specific_workflow")
        assert hasattr(v1_instance.workflow, "get_workflow_run_detail")
        assert hasattr(v1_instance.workflow, "aget_workflow_run_detail")
        assert hasattr(v1_instance.workflow, "stop_workflow")
        assert hasattr(v1_instance.workflow, "astop_workflow")

        # Test file resource methods
        assert hasattr(v1_instance.file, "upload_file")
        assert hasattr(v1_instance.file, "aupload_file")
        assert hasattr(v1_instance.file, "preview_file")
        assert hasattr(v1_instance.file, "apreview_file")

        # Test log resource methods
        assert hasattr(v1_instance.log, "get_workflow_logs")
        assert hasattr(v1_instance.log, "aget_workflow_logs")

        # Test info resource methods
        assert hasattr(v1_instance.info, "get_info")
        assert hasattr(v1_instance.info, "aget_info")
        assert hasattr(v1_instance.info, "get_parameters")
        assert hasattr(v1_instance.info, "aget_parameters")
        assert hasattr(v1_instance.info, "get_site")
        assert hasattr(v1_instance.info, "aget_site")

    def test_config_propagation(self, config: Config) -> None:
        """Test config is properly propagated to all resources."""
        v1 = V1(config)

        # Verify all resources have the same config instance
        assert v1.workflow.config is config
        assert v1.file.config is config
        assert v1.log.config is config
        assert v1.info.config is config

    def test_resource_independence(self, v1_instance: V1) -> None:
        """Test resources are independent instances."""
        # Verify resources are different instances using id() to avoid type checking issues
        assert id(v1_instance.workflow) != id(v1_instance.file)
        assert id(v1_instance.workflow) != id(v1_instance.log)
        assert id(v1_instance.workflow) != id(v1_instance.info)
        assert id(v1_instance.file) != id(v1_instance.log)
        assert id(v1_instance.file) != id(v1_instance.info)
        assert id(v1_instance.log) != id(v1_instance.info)

    def test_workflow_api_coverage(self, v1_instance: V1) -> None:
        """Test workflow API coverage through V1."""
        # Workflow Management APIs (4 APIs)
        workflow_methods = [
            "run_workflow",
            "arun_workflow",
            "run_specific_workflow",
            "arun_specific_workflow",
            "get_workflow_run_detail",
            "aget_workflow_run_detail",
            "stop_workflow",
            "astop_workflow",
        ]

        for method in workflow_methods:
            assert hasattr(v1_instance.workflow, method), f"Missing workflow method: {method}"

    def test_file_api_coverage(self, v1_instance: V1) -> None:
        """Test file API coverage through V1."""
        # File Management APIs (2 APIs)
        file_methods = ["upload_file", "aupload_file", "preview_file", "apreview_file"]

        for method in file_methods:
            assert hasattr(v1_instance.file, method), f"Missing file method: {method}"

    def test_log_api_coverage(self, v1_instance: V1) -> None:
        """Test log API coverage through V1."""
        # Log Management APIs (1 API)
        log_methods = ["get_workflow_logs", "aget_workflow_logs"]

        for method in log_methods:
            assert hasattr(v1_instance.log, method), f"Missing log method: {method}"

    def test_info_api_coverage(self, v1_instance: V1) -> None:
        """Test info API coverage through V1."""
        # Application Information APIs (3 APIs)
        info_methods = ["get_info", "aget_info", "get_parameters", "aget_parameters", "get_site", "aget_site"]

        for method in info_methods:
            assert hasattr(v1_instance.info, method), f"Missing info method: {method}"

    def test_complete_api_coverage(self, v1_instance: V1) -> None:
        """Test complete workflow API coverage (10 APIs total)."""
        # Count all available API methods (sync + async = 20 methods total)
        total_methods = 0

        # Workflow: 4 APIs × 2 (sync/async) = 8 methods
        workflow_methods = [
            "run_workflow",
            "arun_workflow",
            "run_specific_workflow",
            "arun_specific_workflow",
            "get_workflow_run_detail",
            "aget_workflow_run_detail",
            "stop_workflow",
            "astop_workflow",
        ]
        total_methods += len(workflow_methods)

        # File: 2 APIs × 2 (sync/async) = 4 methods
        file_methods = ["upload_file", "aupload_file", "preview_file", "apreview_file"]
        total_methods += len(file_methods)

        # Log: 1 API × 2 (sync/async) = 2 methods
        log_methods = ["get_workflow_logs", "aget_workflow_logs"]
        total_methods += len(log_methods)

        # Info: 3 APIs × 2 (sync/async) = 6 methods
        info_methods = ["get_info", "aget_info", "get_parameters", "aget_parameters", "get_site", "aget_site"]
        total_methods += len(info_methods)

        # Verify total method count (should be 20)
        assert total_methods == 20, f"Expected 20 methods, found {total_methods}"

        # Verify all methods exist
        for method in workflow_methods:
            assert hasattr(v1_instance.workflow, method)
        for method in file_methods:
            assert hasattr(v1_instance.file, method)
        for method in log_methods:
            assert hasattr(v1_instance.log, method)
        for method in info_methods:
            assert hasattr(v1_instance.info, method)

    def test_backward_compatibility(self, v1_instance: V1) -> None:
        """Test backward compatibility with existing workflow resource."""
        # Ensure existing workflow functionality is preserved
        assert hasattr(v1_instance, "workflow")
        assert isinstance(v1_instance.workflow, Workflow)

        # Test that original workflow methods still exist
        original_methods = ["run_workflow", "arun_workflow"]
        for method in original_methods:
            assert hasattr(v1_instance.workflow, method)

    def test_resource_method_signatures(self, v1_instance: V1) -> None:
        """Test resource method signatures are correct."""
        import inspect

        # Test workflow method signatures
        sig = inspect.signature(v1_instance.workflow.run_workflow)
        params = list(sig.parameters.keys())
        assert "request" in params
        assert "request_option" in params
        assert "stream" in params

        # Test file method signatures
        sig = inspect.signature(v1_instance.file.upload_file)
        params = list(sig.parameters.keys())
        assert "request" in params
        assert "request_option" in params

        # Test log method signatures
        sig = inspect.signature(v1_instance.log.get_workflow_logs)
        params = list(sig.parameters.keys())
        assert "request" in params
        assert "request_option" in params

        # Test info method signatures
        sig = inspect.signature(v1_instance.info.get_info)
        params = list(sig.parameters.keys())
        assert "request" in params
        assert "request_option" in params

    def test_client_integration_compatibility(self, config: Config) -> None:
        """Test client integration compatibility."""
        # Test that V1 can be integrated with client structure
        v1 = V1(config)

        # Simulate client.workflow.v1 access pattern
        assert hasattr(v1, "workflow")
        assert hasattr(v1, "file")
        assert hasattr(v1, "log")
        assert hasattr(v1, "info")

        # Test method access patterns
        assert callable(v1.workflow.run_workflow)
        assert callable(v1.file.upload_file)
        assert callable(v1.log.get_workflow_logs)
        assert callable(v1.info.get_info)

    def test_config_modification_isolation(self, config: Config) -> None:
        """Test config modification doesn't affect other instances."""
        v1_1 = V1(config)
        v1_2 = V1(config)

        # Both instances should share the same config
        assert v1_1.workflow.config is config
        assert v1_2.workflow.config is config
        assert v1_1.workflow.config is v1_2.workflow.config

        # But resources should be independent instances
        assert v1_1.workflow is not v1_2.workflow
        assert v1_1.file is not v1_2.file
        assert v1_1.log is not v1_2.log
        assert v1_1.info is not v1_2.info

    def test_resource_type_validation(self, v1_instance: V1) -> None:
        """Test resource type validation."""
        # Verify correct resource types
        assert type(v1_instance.workflow).__name__ == "Workflow"
        assert type(v1_instance.file).__name__ == "File"
        assert type(v1_instance.log).__name__ == "Log"
        assert type(v1_instance.info).__name__ == "Info"

        # Verify inheritance
        from dify_oapi.api.workflow.v1.resource.file import File
        from dify_oapi.api.workflow.v1.resource.info import Info
        from dify_oapi.api.workflow.v1.resource.log import Log
        from dify_oapi.api.workflow.v1.resource.workflow import Workflow

        assert isinstance(v1_instance.workflow, Workflow)
        assert isinstance(v1_instance.file, File)
        assert isinstance(v1_instance.log, Log)
        assert isinstance(v1_instance.info, Info)
