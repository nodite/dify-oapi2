"""Tests for workflow resource."""

from __future__ import annotations

from collections.abc import AsyncGenerator
from unittest.mock import AsyncMock, Mock, patch

import pytest

from dify_oapi.api.workflow.v1.model.workflow.get_workflow_run_detail_request import (
    GetWorkflowRunDetailRequest,
)
from dify_oapi.api.workflow.v1.model.workflow.get_workflow_run_detail_response import (
    GetWorkflowRunDetailResponse,
)
from dify_oapi.api.workflow.v1.model.workflow.run_specific_workflow_request import (
    RunSpecificWorkflowRequest,
)
from dify_oapi.api.workflow.v1.model.workflow.run_specific_workflow_response import (
    RunSpecificWorkflowResponse,
)
from dify_oapi.api.workflow.v1.model.workflow.run_workflow_request import (
    RunWorkflowRequest,
)
from dify_oapi.api.workflow.v1.model.workflow.run_workflow_response import (
    RunWorkflowResponse,
)
from dify_oapi.api.workflow.v1.model.workflow.stop_workflow_request import (
    StopWorkflowRequest,
)
from dify_oapi.api.workflow.v1.model.workflow.stop_workflow_response import (
    StopWorkflowResponse,
)
from dify_oapi.api.workflow.v1.resource.workflow import Workflow
from dify_oapi.core.model.config import Config
from dify_oapi.core.model.request_option import RequestOption


class TestWorkflow:
    """Test cases for Workflow resource."""

    @pytest.fixture
    def config(self) -> Config:
        """Create test config."""
        config = Config()
        config.domain = "https://api.test.com"
        return config

    @pytest.fixture
    def request_option(self) -> RequestOption:
        """Create test request option."""
        return RequestOption.builder().api_key("test-api-key").build()

    @pytest.fixture
    def workflow_resource(self, config: Config) -> Workflow:
        """Create workflow resource instance."""
        return Workflow(config)

    def test_workflow_initialization(self, config: Config) -> None:
        """Test workflow resource initialization."""
        workflow = Workflow(config)
        assert workflow.config == config

    @patch("dify_oapi.core.http.transport.Transport.execute")
    def test_run_workflow_sync_blocking(
        self,
        mock_execute: Mock,
        workflow_resource: Workflow,
        request_option: RequestOption,
    ) -> None:
        """Test run workflow sync blocking mode."""
        # Arrange
        request = RunWorkflowRequest.builder().build()
        expected_response = RunWorkflowResponse()
        mock_execute.return_value = expected_response

        # Act
        result = workflow_resource.run_workflow(request, request_option, stream=False)

        # Assert
        assert result == expected_response
        mock_execute.assert_called_once_with(
            workflow_resource.config,
            request,
            unmarshal_as=RunWorkflowResponse,
            option=request_option,
        )

    @patch("dify_oapi.core.http.transport.Transport.execute")
    def test_run_workflow_sync_streaming(
        self,
        mock_execute: Mock,
        workflow_resource: Workflow,
        request_option: RequestOption,
    ) -> None:
        """Test run workflow sync streaming mode."""
        # Arrange
        request = RunWorkflowRequest.builder().build()
        expected_stream = (b"chunk" + str(i).encode() for i in range(3))
        mock_execute.return_value = expected_stream

        # Act
        result = workflow_resource.run_workflow(request, request_option, stream=True)

        # Assert
        assert result is expected_stream
        mock_execute.assert_called_once_with(workflow_resource.config, request, stream=True, option=request_option)

    @patch("dify_oapi.core.http.transport.ATransport.aexecute")
    async def test_arun_workflow_async_blocking(
        self,
        mock_aexecute: AsyncMock,
        workflow_resource: Workflow,
        request_option: RequestOption,
    ) -> None:
        """Test run workflow async blocking mode."""
        # Arrange
        request = RunWorkflowRequest.builder().build()
        expected_response = RunWorkflowResponse()
        mock_aexecute.return_value = expected_response

        # Act
        result = await workflow_resource.arun_workflow(request, request_option, stream=False)

        # Assert
        assert result == expected_response
        mock_aexecute.assert_called_once_with(
            workflow_resource.config,
            request,
            unmarshal_as=RunWorkflowResponse,
            option=request_option,
        )

    @patch("dify_oapi.core.http.transport.ATransport.aexecute")
    async def test_arun_workflow_async_streaming(
        self,
        mock_aexecute: AsyncMock,
        workflow_resource: Workflow,
        request_option: RequestOption,
    ) -> None:
        """Test run workflow async streaming mode."""
        # Arrange
        request = RunWorkflowRequest.builder().build()

        async def async_generator() -> AsyncGenerator[bytes, None]:
            for i in range(3):
                yield b"chunk" + str(i).encode()

        expected_stream = async_generator()
        mock_aexecute.return_value = expected_stream

        # Act
        result = await workflow_resource.arun_workflow(request, request_option, stream=True)

        # Assert
        assert result is expected_stream
        mock_aexecute.assert_called_once_with(workflow_resource.config, request, stream=True, option=request_option)

    @patch("dify_oapi.core.http.transport.Transport.execute")
    def test_run_specific_workflow_sync_blocking(
        self,
        mock_execute: Mock,
        workflow_resource: Workflow,
        request_option: RequestOption,
    ) -> None:
        """Test run specific workflow sync blocking mode."""
        # Arrange
        request = RunSpecificWorkflowRequest.builder().workflow_id("test-id").build()
        expected_response = RunSpecificWorkflowResponse()
        mock_execute.return_value = expected_response

        # Act
        result = workflow_resource.run_specific_workflow(request, request_option, stream=False)

        # Assert
        assert result == expected_response
        mock_execute.assert_called_once_with(
            workflow_resource.config,
            request,
            unmarshal_as=RunSpecificWorkflowResponse,
            option=request_option,
        )

    @patch("dify_oapi.core.http.transport.Transport.execute")
    def test_run_specific_workflow_sync_streaming(
        self,
        mock_execute: Mock,
        workflow_resource: Workflow,
        request_option: RequestOption,
    ) -> None:
        """Test run specific workflow sync streaming mode."""
        # Arrange
        request = RunSpecificWorkflowRequest.builder().workflow_id("test-id").build()
        expected_stream = (b"chunk" + str(i).encode() for i in range(2))
        mock_execute.return_value = expected_stream

        # Act
        result = workflow_resource.run_specific_workflow(request, request_option, stream=True)

        # Assert
        assert result is expected_stream
        mock_execute.assert_called_once_with(workflow_resource.config, request, stream=True, option=request_option)

    @patch("dify_oapi.core.http.transport.ATransport.aexecute")
    async def test_arun_specific_workflow_async_blocking(
        self,
        mock_aexecute: AsyncMock,
        workflow_resource: Workflow,
        request_option: RequestOption,
    ) -> None:
        """Test run specific workflow async blocking mode."""
        # Arrange
        request = RunSpecificWorkflowRequest.builder().workflow_id("test-id").build()
        expected_response = RunSpecificWorkflowResponse()
        mock_aexecute.return_value = expected_response

        # Act
        result = await workflow_resource.arun_specific_workflow(request, request_option, stream=False)

        # Assert
        assert result == expected_response
        mock_aexecute.assert_called_once_with(
            workflow_resource.config,
            request,
            unmarshal_as=RunSpecificWorkflowResponse,
            option=request_option,
        )

    @patch("dify_oapi.core.http.transport.ATransport.aexecute")
    async def test_arun_specific_workflow_async_streaming(
        self,
        mock_aexecute: AsyncMock,
        workflow_resource: Workflow,
        request_option: RequestOption,
    ) -> None:
        """Test run specific workflow async streaming mode."""
        # Arrange
        request = RunSpecificWorkflowRequest.builder().workflow_id("test-id").build()

        async def async_generator() -> AsyncGenerator[bytes, None]:
            for i in range(2):
                yield b"chunk" + str(i).encode()

        expected_stream = async_generator()
        mock_aexecute.return_value = expected_stream

        # Act
        result = await workflow_resource.arun_specific_workflow(request, request_option, stream=True)

        # Assert
        assert result is expected_stream
        mock_aexecute.assert_called_once_with(workflow_resource.config, request, stream=True, option=request_option)

    @patch("dify_oapi.core.http.transport.Transport.execute")
    def test_get_workflow_run_detail_sync(
        self,
        mock_execute: Mock,
        workflow_resource: Workflow,
        request_option: RequestOption,
    ) -> None:
        """Test get workflow run detail sync."""
        # Arrange
        request = GetWorkflowRunDetailRequest.builder().workflow_run_id("test-run-id").build()
        expected_response = GetWorkflowRunDetailResponse()
        mock_execute.return_value = expected_response

        # Act
        result = workflow_resource.get_workflow_run_detail(request, request_option)

        # Assert
        assert result == expected_response
        mock_execute.assert_called_once_with(
            workflow_resource.config,
            request,
            unmarshal_as=GetWorkflowRunDetailResponse,
            option=request_option,
        )

    @patch("dify_oapi.core.http.transport.ATransport.aexecute")
    async def test_aget_workflow_run_detail_async(
        self,
        mock_aexecute: AsyncMock,
        workflow_resource: Workflow,
        request_option: RequestOption,
    ) -> None:
        """Test get workflow run detail async."""
        # Arrange
        request = GetWorkflowRunDetailRequest.builder().workflow_run_id("test-run-id").build()
        expected_response = GetWorkflowRunDetailResponse()
        mock_aexecute.return_value = expected_response

        # Act
        result = await workflow_resource.aget_workflow_run_detail(request, request_option)

        # Assert
        assert result == expected_response
        mock_aexecute.assert_called_once_with(
            workflow_resource.config,
            request,
            unmarshal_as=GetWorkflowRunDetailResponse,
            option=request_option,
        )

    @patch("dify_oapi.core.http.transport.Transport.execute")
    def test_stop_workflow_sync(
        self,
        mock_execute: Mock,
        workflow_resource: Workflow,
        request_option: RequestOption,
    ) -> None:
        """Test stop workflow sync."""
        # Arrange
        request = StopWorkflowRequest.builder().task_id("test-task-id").build()
        expected_response = StopWorkflowResponse()
        mock_execute.return_value = expected_response

        # Act
        result = workflow_resource.stop_workflow(request, request_option)

        # Assert
        assert result == expected_response
        mock_execute.assert_called_once_with(
            workflow_resource.config,
            request,
            unmarshal_as=StopWorkflowResponse,
            option=request_option,
        )

    @patch("dify_oapi.core.http.transport.ATransport.aexecute")
    async def test_astop_workflow_async(
        self,
        mock_aexecute: AsyncMock,
        workflow_resource: Workflow,
        request_option: RequestOption,
    ) -> None:
        """Test stop workflow async."""
        # Arrange
        request = StopWorkflowRequest.builder().task_id("test-task-id").build()
        expected_response = StopWorkflowResponse()
        mock_aexecute.return_value = expected_response

        # Act
        result = await workflow_resource.astop_workflow(request, request_option)

        # Assert
        assert result == expected_response
        mock_aexecute.assert_called_once_with(
            workflow_resource.config,
            request,
            unmarshal_as=StopWorkflowResponse,
            option=request_option,
        )

    @patch("dify_oapi.core.http.transport.Transport.execute")
    def test_run_workflow_error_handling(
        self,
        mock_execute: Mock,
        workflow_resource: Workflow,
        request_option: RequestOption,
    ) -> None:
        """Test run workflow error handling."""
        # Arrange
        request = RunWorkflowRequest.builder().build()
        mock_execute.side_effect = Exception("API Error")

        # Act & Assert
        with pytest.raises(Exception, match="API Error"):
            workflow_resource.run_workflow(request, request_option, stream=False)

    @patch("dify_oapi.core.http.transport.ATransport.aexecute")
    async def test_arun_workflow_error_handling(
        self,
        mock_aexecute: AsyncMock,
        workflow_resource: Workflow,
        request_option: RequestOption,
    ) -> None:
        """Test async run workflow error handling."""
        # Arrange
        request = RunWorkflowRequest.builder().build()
        mock_aexecute.side_effect = Exception("Async API Error")

        # Act & Assert
        with pytest.raises(Exception, match="Async API Error"):
            await workflow_resource.arun_workflow(request, request_option, stream=False)

    def test_streaming_return_types(self, workflow_resource: Workflow) -> None:
        """Test streaming return type annotations."""
        # This test verifies that the method signatures are correct
        # by checking the return type annotations
        from typing import get_type_hints

        # Check sync streaming method
        hints = get_type_hints(workflow_resource.run_workflow)
        assert "return" in hints

        # Check async streaming method
        hints = get_type_hints(workflow_resource.arun_workflow)
        assert "return" in hints

    def test_method_signatures(self, workflow_resource: Workflow) -> None:
        """Test that all methods have correct signatures."""
        import inspect

        # Test sync methods
        assert hasattr(workflow_resource, "run_workflow")
        assert hasattr(workflow_resource, "run_specific_workflow")
        assert hasattr(workflow_resource, "get_workflow_run_detail")
        assert hasattr(workflow_resource, "stop_workflow")

        # Test async methods
        assert hasattr(workflow_resource, "arun_workflow")
        assert hasattr(workflow_resource, "arun_specific_workflow")
        assert hasattr(workflow_resource, "aget_workflow_run_detail")
        assert hasattr(workflow_resource, "astop_workflow")

        # Verify method signatures
        sig = inspect.signature(workflow_resource.run_workflow)
        params = list(sig.parameters.keys())
        assert "request" in params
        assert "request_option" in params
        assert "stream" in params
