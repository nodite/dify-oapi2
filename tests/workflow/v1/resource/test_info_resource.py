"""Tests for info resource."""

from __future__ import annotations

from unittest.mock import AsyncMock, Mock, patch

import pytest

from dify_oapi.api.workflow.v1.model.info.get_info_request import (
    GetInfoRequest,
)
from dify_oapi.api.workflow.v1.model.info.get_info_response import (
    GetInfoResponse,
)
from dify_oapi.api.workflow.v1.model.info.get_parameters_request import (
    GetParametersRequest,
)
from dify_oapi.api.workflow.v1.model.info.get_parameters_response import (
    GetParametersResponse,
)
from dify_oapi.api.workflow.v1.model.info.get_site_request import (
    GetSiteRequest,
)
from dify_oapi.api.workflow.v1.model.info.get_site_response import (
    GetSiteResponse,
)
from dify_oapi.api.workflow.v1.resource.info import Info
from dify_oapi.core.model.config import Config
from dify_oapi.core.model.request_option import RequestOption


class TestInfo:
    """Test cases for Info resource."""

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
    def info_resource(self, config: Config) -> Info:
        """Create info resource instance."""
        return Info(config)

    def test_info_initialization(self, config: Config) -> None:
        """Test info resource initialization."""
        info_resource = Info(config)
        assert info_resource.config == config

    @patch("dify_oapi.core.http.transport.Transport.execute")
    def test_get_info_sync(
        self,
        mock_execute: Mock,
        info_resource: Info,
        request_option: RequestOption,
    ) -> None:
        """Test get info sync."""
        # Arrange
        request = GetInfoRequest.builder().build()
        expected_response = GetInfoResponse()
        mock_execute.return_value = expected_response

        # Act
        result = info_resource.get_info(request, request_option)

        # Assert
        assert result == expected_response
        mock_execute.assert_called_once_with(
            info_resource.config,
            request,
            unmarshal_as=GetInfoResponse,
            option=request_option,
        )

    @patch("dify_oapi.core.http.transport.ATransport.aexecute")
    async def test_aget_info_async(
        self,
        mock_aexecute: AsyncMock,
        info_resource: Info,
        request_option: RequestOption,
    ) -> None:
        """Test get info async."""
        # Arrange
        request = GetInfoRequest.builder().build()
        expected_response = GetInfoResponse()
        mock_aexecute.return_value = expected_response

        # Act
        result = await info_resource.aget_info(request, request_option)

        # Assert
        assert result == expected_response
        mock_aexecute.assert_called_once_with(
            info_resource.config,
            request,
            unmarshal_as=GetInfoResponse,
            option=request_option,
        )

    @patch("dify_oapi.core.http.transport.Transport.execute")
    def test_get_parameters_sync(
        self,
        mock_execute: Mock,
        info_resource: Info,
        request_option: RequestOption,
    ) -> None:
        """Test get parameters sync."""
        # Arrange
        request = GetParametersRequest.builder().build()
        expected_response = GetParametersResponse()
        mock_execute.return_value = expected_response

        # Act
        result = info_resource.get_parameters(request, request_option)

        # Assert
        assert result == expected_response
        mock_execute.assert_called_once_with(
            info_resource.config,
            request,
            unmarshal_as=GetParametersResponse,
            option=request_option,
        )

    @patch("dify_oapi.core.http.transport.ATransport.aexecute")
    async def test_aget_parameters_async(
        self,
        mock_aexecute: AsyncMock,
        info_resource: Info,
        request_option: RequestOption,
    ) -> None:
        """Test get parameters async."""
        # Arrange
        request = GetParametersRequest.builder().build()
        expected_response = GetParametersResponse()
        mock_aexecute.return_value = expected_response

        # Act
        result = await info_resource.aget_parameters(request, request_option)

        # Assert
        assert result == expected_response
        mock_aexecute.assert_called_once_with(
            info_resource.config,
            request,
            unmarshal_as=GetParametersResponse,
            option=request_option,
        )

    @patch("dify_oapi.core.http.transport.Transport.execute")
    def test_get_site_sync(
        self,
        mock_execute: Mock,
        info_resource: Info,
        request_option: RequestOption,
    ) -> None:
        """Test get site sync."""
        # Arrange
        request = GetSiteRequest.builder().build()
        expected_response = GetSiteResponse()
        mock_execute.return_value = expected_response

        # Act
        result = info_resource.get_site(request, request_option)

        # Assert
        assert result == expected_response
        mock_execute.assert_called_once_with(
            info_resource.config,
            request,
            unmarshal_as=GetSiteResponse,
            option=request_option,
        )

    @patch("dify_oapi.core.http.transport.ATransport.aexecute")
    async def test_aget_site_async(
        self,
        mock_aexecute: AsyncMock,
        info_resource: Info,
        request_option: RequestOption,
    ) -> None:
        """Test get site async."""
        # Arrange
        request = GetSiteRequest.builder().build()
        expected_response = GetSiteResponse()
        mock_aexecute.return_value = expected_response

        # Act
        result = await info_resource.aget_site(request, request_option)

        # Assert
        assert result == expected_response
        mock_aexecute.assert_called_once_with(
            info_resource.config,
            request,
            unmarshal_as=GetSiteResponse,
            option=request_option,
        )

    @patch("dify_oapi.core.http.transport.Transport.execute")
    def test_get_info_error_handling(
        self,
        mock_execute: Mock,
        info_resource: Info,
        request_option: RequestOption,
    ) -> None:
        """Test get info error handling."""
        # Arrange
        request = GetInfoRequest.builder().build()
        mock_execute.side_effect = Exception("Info Retrieval Error")

        # Act & Assert
        with pytest.raises(Exception, match="Info Retrieval Error"):
            info_resource.get_info(request, request_option)

    @patch("dify_oapi.core.http.transport.ATransport.aexecute")
    async def test_aget_info_error_handling(
        self,
        mock_aexecute: AsyncMock,
        info_resource: Info,
        request_option: RequestOption,
    ) -> None:
        """Test async get info error handling."""
        # Arrange
        request = GetInfoRequest.builder().build()
        mock_aexecute.side_effect = Exception("Async Info Retrieval Error")

        # Act & Assert
        with pytest.raises(Exception, match="Async Info Retrieval Error"):
            await info_resource.aget_info(request, request_option)

    @patch("dify_oapi.core.http.transport.Transport.execute")
    def test_get_parameters_error_handling(
        self,
        mock_execute: Mock,
        info_resource: Info,
        request_option: RequestOption,
    ) -> None:
        """Test get parameters error handling."""
        # Arrange
        request = GetParametersRequest.builder().build()
        mock_execute.side_effect = Exception("Parameters Retrieval Error")

        # Act & Assert
        with pytest.raises(Exception, match="Parameters Retrieval Error"):
            info_resource.get_parameters(request, request_option)

    @patch("dify_oapi.core.http.transport.ATransport.aexecute")
    async def test_aget_parameters_error_handling(
        self,
        mock_aexecute: AsyncMock,
        info_resource: Info,
        request_option: RequestOption,
    ) -> None:
        """Test async get parameters error handling."""
        # Arrange
        request = GetParametersRequest.builder().build()
        mock_aexecute.side_effect = Exception("Async Parameters Retrieval Error")

        # Act & Assert
        with pytest.raises(Exception, match="Async Parameters Retrieval Error"):
            await info_resource.aget_parameters(request, request_option)

    @patch("dify_oapi.core.http.transport.Transport.execute")
    def test_get_site_error_handling(
        self,
        mock_execute: Mock,
        info_resource: Info,
        request_option: RequestOption,
    ) -> None:
        """Test get site error handling."""
        # Arrange
        request = GetSiteRequest.builder().build()
        mock_execute.side_effect = Exception("Site Retrieval Error")

        # Act & Assert
        with pytest.raises(Exception, match="Site Retrieval Error"):
            info_resource.get_site(request, request_option)

    @patch("dify_oapi.core.http.transport.ATransport.aexecute")
    async def test_aget_site_error_handling(
        self,
        mock_aexecute: AsyncMock,
        info_resource: Info,
        request_option: RequestOption,
    ) -> None:
        """Test async get site error handling."""
        # Arrange
        request = GetSiteRequest.builder().build()
        mock_aexecute.side_effect = Exception("Async Site Retrieval Error")

        # Act & Assert
        with pytest.raises(Exception, match="Async Site Retrieval Error"):
            await info_resource.aget_site(request, request_option)

    def test_method_signatures(self, info_resource: Info) -> None:
        """Test that all methods have correct signatures."""
        import inspect

        # Test sync methods
        assert hasattr(info_resource, "get_info")
        assert hasattr(info_resource, "get_parameters")
        assert hasattr(info_resource, "get_site")

        # Test async methods
        assert hasattr(info_resource, "aget_info")
        assert hasattr(info_resource, "aget_parameters")
        assert hasattr(info_resource, "aget_site")

        # Verify method signatures
        for method_name in ["get_info", "get_parameters", "get_site"]:
            sig = inspect.signature(getattr(info_resource, method_name))
            params = list(sig.parameters.keys())
            assert "request" in params
            assert "request_option" in params

        for method_name in ["aget_info", "aget_parameters", "aget_site"]:
            sig = inspect.signature(getattr(info_resource, method_name))
            params = list(sig.parameters.keys())
            assert "request" in params
            assert "request_option" in params

    def test_info_request_structure(self) -> None:
        """Test info request structure."""
        # Test that all info requests can be built successfully
        info_request = GetInfoRequest.builder().build()
        parameters_request = GetParametersRequest.builder().build()
        site_request = GetSiteRequest.builder().build()

        assert info_request is not None
        assert parameters_request is not None
        assert site_request is not None

    def test_info_response_structure(self) -> None:
        """Test info response structure."""
        # Test that all info responses can be instantiated
        info_response = GetInfoResponse()
        parameters_response = GetParametersResponse()
        site_response = GetSiteResponse()

        assert info_response is not None
        assert parameters_response is not None
        assert site_response is not None

    def test_all_info_endpoints_coverage(self, info_resource: Info) -> None:
        """Test that all info endpoints are covered."""
        # Verify all required methods exist
        required_sync_methods = ["get_info", "get_parameters", "get_site"]
        required_async_methods = ["aget_info", "aget_parameters", "aget_site"]

        for method in required_sync_methods:
            assert hasattr(info_resource, method), f"Missing sync method: {method}"

        for method in required_async_methods:
            assert hasattr(info_resource, method), f"Missing async method: {method}"

    @patch("dify_oapi.core.http.transport.Transport.execute")
    def test_multiple_info_calls_sync(
        self,
        mock_execute: Mock,
        info_resource: Info,
        request_option: RequestOption,
    ) -> None:
        """Test multiple info calls in sync mode."""
        # Arrange
        info_request = GetInfoRequest.builder().build()
        parameters_request = GetParametersRequest.builder().build()
        site_request = GetSiteRequest.builder().build()

        info_response = GetInfoResponse()
        parameters_response = GetParametersResponse()
        site_response = GetSiteResponse()

        mock_execute.side_effect = [info_response, parameters_response, site_response]

        # Act
        info_result = info_resource.get_info(info_request, request_option)
        parameters_result = info_resource.get_parameters(parameters_request, request_option)
        site_result = info_resource.get_site(site_request, request_option)

        # Assert
        assert info_result == info_response
        assert parameters_result == parameters_response
        assert site_result == site_response
        assert mock_execute.call_count == 3

    @patch("dify_oapi.core.http.transport.ATransport.aexecute")
    async def test_multiple_info_calls_async(
        self,
        mock_aexecute: AsyncMock,
        info_resource: Info,
        request_option: RequestOption,
    ) -> None:
        """Test multiple info calls in async mode."""
        # Arrange
        info_request = GetInfoRequest.builder().build()
        parameters_request = GetParametersRequest.builder().build()
        site_request = GetSiteRequest.builder().build()

        info_response = GetInfoResponse()
        parameters_response = GetParametersResponse()
        site_response = GetSiteResponse()

        mock_aexecute.side_effect = [info_response, parameters_response, site_response]

        # Act
        info_result = await info_resource.aget_info(info_request, request_option)
        parameters_result = await info_resource.aget_parameters(parameters_request, request_option)
        site_result = await info_resource.aget_site(site_request, request_option)

        # Assert
        assert info_result == info_response
        assert parameters_result == parameters_response
        assert site_result == site_response
        assert mock_aexecute.call_count == 3
