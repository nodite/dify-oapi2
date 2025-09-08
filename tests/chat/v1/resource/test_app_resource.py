from unittest.mock import Mock

import pytest

from dify_oapi.api.chat.v1.model.get_app_info_request import GetAppInfoRequest
from dify_oapi.api.chat.v1.model.get_app_info_response import GetAppInfoResponse
from dify_oapi.api.chat.v1.model.get_app_meta_request import GetAppMetaRequest
from dify_oapi.api.chat.v1.model.get_app_meta_response import GetAppMetaResponse
from dify_oapi.api.chat.v1.model.get_app_parameters_request import GetAppParametersRequest
from dify_oapi.api.chat.v1.model.get_app_parameters_response import GetAppParametersResponse
from dify_oapi.api.chat.v1.model.get_site_settings_request import GetSiteSettingsRequest
from dify_oapi.api.chat.v1.model.get_site_settings_response import GetSiteSettingsResponse
from dify_oapi.api.chat.v1.resource.app import App
from dify_oapi.core.http.transport import ATransport, Transport
from dify_oapi.core.model.config import Config
from dify_oapi.core.model.request_option import RequestOption


class TestAppResource:
    @pytest.fixture
    def app_resource(self):
        config = Config()
        return App(config)

    @pytest.fixture
    def mock_transport(self, monkeypatch):
        mock = Mock()
        monkeypatch.setattr(Transport, "execute", mock)
        return mock

    @pytest.fixture
    def mock_atransport(self, monkeypatch):
        from unittest.mock import AsyncMock

        mock = AsyncMock()
        monkeypatch.setattr(ATransport, "aexecute", mock)
        return mock

    def test_get_app_info(self, app_resource, mock_transport):
        """Test get application information"""
        request = GetAppInfoRequest.builder().build()
        option = RequestOption.builder().build()

        mock_transport.return_value = GetAppInfoResponse(name="Test App", description="Test Description", tags=["ai"])
        result = app_resource.info(request, option)

        assert isinstance(result, GetAppInfoResponse)
        mock_transport.assert_called_once_with(
            app_resource.config, request, unmarshal_as=GetAppInfoResponse, option=option
        )

    def test_get_app_parameters(self, app_resource, mock_transport):
        """Test get application parameters"""
        request = GetAppParametersRequest.builder().user("test-user").build()
        option = RequestOption.builder().build()

        mock_transport.return_value = GetAppParametersResponse()
        result = app_resource.parameters(request, option)

        assert isinstance(result, GetAppParametersResponse)
        mock_transport.assert_called_once_with(
            app_resource.config, request, unmarshal_as=GetAppParametersResponse, option=option
        )

    def test_get_app_meta(self, app_resource, mock_transport):
        """Test get application meta information"""
        request = GetAppMetaRequest.builder().build()
        option = RequestOption.builder().build()

        mock_transport.return_value = GetAppMetaResponse()
        result = app_resource.meta(request, option)

        assert isinstance(result, GetAppMetaResponse)
        mock_transport.assert_called_once_with(
            app_resource.config, request, unmarshal_as=GetAppMetaResponse, option=option
        )

    def test_get_site_settings(self, app_resource, mock_transport):
        """Test get site settings"""
        request = GetSiteSettingsRequest.builder().build()
        option = RequestOption.builder().build()

        mock_transport.return_value = GetSiteSettingsResponse()
        result = app_resource.site(request, option)

        assert isinstance(result, GetSiteSettingsResponse)
        mock_transport.assert_called_once_with(
            app_resource.config, request, unmarshal_as=GetSiteSettingsResponse, option=option
        )

    @pytest.mark.asyncio
    async def test_async_get_app_info(self, app_resource, mock_atransport):
        """Test async get application information"""
        request = GetAppInfoRequest.builder().build()
        option = RequestOption.builder().build()

        mock_atransport.return_value = GetAppInfoResponse(name="Test App", description="Test Description", tags=["ai"])
        result = await app_resource.ainfo(request, option)

        assert isinstance(result, GetAppInfoResponse)
        mock_atransport.assert_called_once_with(
            app_resource.config, request, unmarshal_as=GetAppInfoResponse, option=option
        )

    @pytest.mark.asyncio
    async def test_async_get_app_parameters(self, app_resource, mock_atransport):
        """Test async get application parameters"""
        request = GetAppParametersRequest.builder().user("test-user").build()
        option = RequestOption.builder().build()

        mock_atransport.return_value = GetAppParametersResponse()
        result = await app_resource.aparameters(request, option)

        assert isinstance(result, GetAppParametersResponse)
        mock_atransport.assert_called_once_with(
            app_resource.config, request, unmarshal_as=GetAppParametersResponse, option=option
        )

    @pytest.mark.asyncio
    async def test_async_get_app_meta(self, app_resource, mock_atransport):
        """Test async get application meta information"""
        request = GetAppMetaRequest.builder().build()
        option = RequestOption.builder().build()

        mock_atransport.return_value = GetAppMetaResponse()
        result = await app_resource.ameta(request, option)

        assert isinstance(result, GetAppMetaResponse)
        mock_atransport.assert_called_once_with(
            app_resource.config, request, unmarshal_as=GetAppMetaResponse, option=option
        )

    @pytest.mark.asyncio
    async def test_async_get_site_settings(self, app_resource, mock_atransport):
        """Test async get site settings"""
        request = GetSiteSettingsRequest.builder().build()
        option = RequestOption.builder().build()

        mock_atransport.return_value = GetSiteSettingsResponse()
        result = await app_resource.asite(request, option)

        assert isinstance(result, GetSiteSettingsResponse)
        mock_atransport.assert_called_once_with(
            app_resource.config, request, unmarshal_as=GetSiteSettingsResponse, option=option
        )
