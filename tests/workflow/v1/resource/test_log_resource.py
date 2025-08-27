"""Tests for log resource."""

from __future__ import annotations

from unittest.mock import AsyncMock, Mock, patch

import pytest

from dify_oapi.api.workflow.v1.model.log.get_workflow_logs_request import (
    GetWorkflowLogsRequest,
)
from dify_oapi.api.workflow.v1.model.log.get_workflow_logs_response import (
    GetWorkflowLogsResponse,
)
from dify_oapi.api.workflow.v1.resource.log import Log
from dify_oapi.core.model.config import Config
from dify_oapi.core.model.request_option import RequestOption


class TestLog:
    """Test cases for Log resource."""

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
    def log_resource(self, config: Config) -> Log:
        """Create log resource instance."""
        return Log(config)

    def test_log_initialization(self, config: Config) -> None:
        """Test log resource initialization."""
        log_resource = Log(config)
        assert log_resource.config == config

    @patch("dify_oapi.core.http.transport.Transport.execute")
    def test_get_workflow_logs_sync(
        self,
        mock_execute: Mock,
        log_resource: Log,
        request_option: RequestOption,
    ) -> None:
        """Test get workflow logs sync."""
        # Arrange
        request = GetWorkflowLogsRequest.builder().build()
        expected_response = GetWorkflowLogsResponse()
        mock_execute.return_value = expected_response

        # Act
        result = log_resource.get_workflow_logs(request, request_option)

        # Assert
        assert result == expected_response
        mock_execute.assert_called_once_with(
            log_resource.config,
            request,
            unmarshal_as=GetWorkflowLogsResponse,
            option=request_option,
        )

    @patch("dify_oapi.core.http.transport.ATransport.aexecute")
    async def test_aget_workflow_logs_async(
        self,
        mock_aexecute: AsyncMock,
        log_resource: Log,
        request_option: RequestOption,
    ) -> None:
        """Test get workflow logs async."""
        # Arrange
        request = GetWorkflowLogsRequest.builder().build()
        expected_response = GetWorkflowLogsResponse()
        mock_aexecute.return_value = expected_response

        # Act
        result = await log_resource.aget_workflow_logs(request, request_option)

        # Assert
        assert result == expected_response
        mock_aexecute.assert_called_once_with(
            log_resource.config,
            request,
            unmarshal_as=GetWorkflowLogsResponse,
            option=request_option,
        )

    @patch("dify_oapi.core.http.transport.Transport.execute")
    def test_get_workflow_logs_with_keyword_filter(
        self,
        mock_execute: Mock,
        log_resource: Log,
        request_option: RequestOption,
    ) -> None:
        """Test get workflow logs with keyword filter."""
        # Arrange
        request = GetWorkflowLogsRequest.builder().keyword("test-keyword").build()
        expected_response = GetWorkflowLogsResponse()
        mock_execute.return_value = expected_response

        # Act
        result = log_resource.get_workflow_logs(request, request_option)

        # Assert
        assert result == expected_response
        mock_execute.assert_called_once_with(
            log_resource.config,
            request,
            unmarshal_as=GetWorkflowLogsResponse,
            option=request_option,
        )

    @patch("dify_oapi.core.http.transport.Transport.execute")
    def test_get_workflow_logs_with_status_filter(
        self,
        mock_execute: Mock,
        log_resource: Log,
        request_option: RequestOption,
    ) -> None:
        """Test get workflow logs with status filter."""
        # Arrange
        request = GetWorkflowLogsRequest.builder().status("succeeded").build()
        expected_response = GetWorkflowLogsResponse()
        mock_execute.return_value = expected_response

        # Act
        result = log_resource.get_workflow_logs(request, request_option)

        # Assert
        assert result == expected_response
        mock_execute.assert_called_once_with(
            log_resource.config,
            request,
            unmarshal_as=GetWorkflowLogsResponse,
            option=request_option,
        )

    @patch("dify_oapi.core.http.transport.Transport.execute")
    def test_get_workflow_logs_with_pagination(
        self,
        mock_execute: Mock,
        log_resource: Log,
        request_option: RequestOption,
    ) -> None:
        """Test get workflow logs with pagination."""
        # Arrange
        request = GetWorkflowLogsRequest.builder().page(2).limit(50).build()
        expected_response = GetWorkflowLogsResponse()
        mock_execute.return_value = expected_response

        # Act
        result = log_resource.get_workflow_logs(request, request_option)

        # Assert
        assert result == expected_response
        mock_execute.assert_called_once_with(
            log_resource.config,
            request,
            unmarshal_as=GetWorkflowLogsResponse,
            option=request_option,
        )

    @patch("dify_oapi.core.http.transport.Transport.execute")
    def test_get_workflow_logs_with_user_filters(
        self,
        mock_execute: Mock,
        log_resource: Log,
        request_option: RequestOption,
    ) -> None:
        """Test get workflow logs with user filters."""
        # Arrange
        request = (
            GetWorkflowLogsRequest.builder()
            .created_by_end_user_session_id("session-123")
            .created_by_account("user@example.com")
            .build()
        )
        expected_response = GetWorkflowLogsResponse()
        mock_execute.return_value = expected_response

        # Act
        result = log_resource.get_workflow_logs(request, request_option)

        # Assert
        assert result == expected_response
        mock_execute.assert_called_once_with(
            log_resource.config,
            request,
            unmarshal_as=GetWorkflowLogsResponse,
            option=request_option,
        )

    @patch("dify_oapi.core.http.transport.Transport.execute")
    def test_get_workflow_logs_with_all_parameters(
        self,
        mock_execute: Mock,
        log_resource: Log,
        request_option: RequestOption,
    ) -> None:
        """Test get workflow logs with all query parameters."""
        # Arrange
        request = (
            GetWorkflowLogsRequest.builder()
            .keyword("search-term")
            .status("failed")
            .page(1)
            .limit(20)
            .created_by_end_user_session_id("session-456")
            .created_by_account("admin@example.com")
            .build()
        )
        expected_response = GetWorkflowLogsResponse()
        mock_execute.return_value = expected_response

        # Act
        result = log_resource.get_workflow_logs(request, request_option)

        # Assert
        assert result == expected_response
        mock_execute.assert_called_once_with(
            log_resource.config,
            request,
            unmarshal_as=GetWorkflowLogsResponse,
            option=request_option,
        )

    @patch("dify_oapi.core.http.transport.Transport.execute")
    def test_get_workflow_logs_error_handling(
        self,
        mock_execute: Mock,
        log_resource: Log,
        request_option: RequestOption,
    ) -> None:
        """Test get workflow logs error handling."""
        # Arrange
        request = GetWorkflowLogsRequest.builder().build()
        mock_execute.side_effect = Exception("Log Retrieval Error")

        # Act & Assert
        with pytest.raises(Exception, match="Log Retrieval Error"):
            log_resource.get_workflow_logs(request, request_option)

    @patch("dify_oapi.core.http.transport.ATransport.aexecute")
    async def test_aget_workflow_logs_error_handling(
        self,
        mock_aexecute: AsyncMock,
        log_resource: Log,
        request_option: RequestOption,
    ) -> None:
        """Test async get workflow logs error handling."""
        # Arrange
        request = GetWorkflowLogsRequest.builder().build()
        mock_aexecute.side_effect = Exception("Async Log Retrieval Error")

        # Act & Assert
        with pytest.raises(Exception, match="Async Log Retrieval Error"):
            await log_resource.aget_workflow_logs(request, request_option)

    def test_method_signatures(self, log_resource: Log) -> None:
        """Test that all methods have correct signatures."""
        import inspect

        # Test sync methods
        assert hasattr(log_resource, "get_workflow_logs")

        # Test async methods
        assert hasattr(log_resource, "aget_workflow_logs")

        # Verify method signatures
        sig = inspect.signature(log_resource.get_workflow_logs)
        params = list(sig.parameters.keys())
        assert "request" in params
        assert "request_option" in params

        sig = inspect.signature(log_resource.aget_workflow_logs)
        params = list(sig.parameters.keys())
        assert "request" in params
        assert "request_option" in params

    def test_query_parameter_handling(self) -> None:
        """Test query parameter handling in log requests."""
        # Test that all query parameters can be set
        request = (
            GetWorkflowLogsRequest.builder()
            .keyword("test")
            .status("succeeded")
            .page(1)
            .limit(10)
            .created_by_end_user_session_id("session")
            .created_by_account("account")
            .build()
        )

        # Verify the request was built successfully
        assert request is not None
        assert hasattr(request, "queries")

    def test_log_status_filtering(self) -> None:
        """Test log status filtering functionality."""
        # Test different status values
        statuses = ["succeeded", "failed", "stopped"]

        for status in statuses:
            request = GetWorkflowLogsRequest.builder().status(status).build()
            assert request is not None

    def test_pagination_parameters(self) -> None:
        """Test pagination parameter validation."""
        # Test valid pagination parameters
        request = GetWorkflowLogsRequest.builder().page(1).limit(20).build()
        assert request is not None

        # Test different page and limit values
        request = GetWorkflowLogsRequest.builder().page(5).limit(100).build()
        assert request is not None

    @patch("dify_oapi.core.http.transport.ATransport.aexecute")
    async def test_async_log_retrieval_with_filters(
        self,
        mock_aexecute: AsyncMock,
        log_resource: Log,
        request_option: RequestOption,
    ) -> None:
        """Test async log retrieval with various filters."""
        # Arrange
        request = GetWorkflowLogsRequest.builder().keyword("async-test").status("succeeded").page(1).limit(25).build()
        expected_response = GetWorkflowLogsResponse()
        mock_aexecute.return_value = expected_response

        # Act
        result = await log_resource.aget_workflow_logs(request, request_option)

        # Assert
        assert result == expected_response
        mock_aexecute.assert_called_once_with(
            log_resource.config,
            request,
            unmarshal_as=GetWorkflowLogsResponse,
            option=request_option,
        )
