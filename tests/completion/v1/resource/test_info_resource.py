from __future__ import annotations

from unittest.mock import AsyncMock, patch

import pytest

from dify_oapi.api.completion.v1.model.info.get_info_request import GetInfoRequest
from dify_oapi.api.completion.v1.model.info.get_info_response import GetInfoResponse
from dify_oapi.api.completion.v1.model.info.get_parameters_request import GetParametersRequest
from dify_oapi.api.completion.v1.model.info.get_parameters_response import GetParametersResponse
from dify_oapi.api.completion.v1.model.info.get_site_request import GetSiteRequest
from dify_oapi.api.completion.v1.model.info.get_site_response import GetSiteResponse
from dify_oapi.api.completion.v1.resource.info import Info
from dify_oapi.core.model.config import Config
from dify_oapi.core.model.request_option import RequestOption


class TestInfoResource:
    @pytest.fixture
    def config(self) -> Config:
        config = Config()
        config.domain = "https://api.dify.ai"
        return config

    @pytest.fixture
    def request_option(self) -> RequestOption:
        return RequestOption.builder().api_key("test-api-key").build()

    @pytest.fixture
    def info_resource(self, config: Config) -> Info:
        return Info(config)

    @pytest.fixture
    def get_info_request(self) -> GetInfoRequest:
        return GetInfoRequest.builder().build()

    @pytest.fixture
    def get_parameters_request(self) -> GetParametersRequest:
        return GetParametersRequest.builder().build()

    @pytest.fixture
    def get_site_request(self) -> GetSiteRequest:
        return GetSiteRequest.builder().build()

    def test_get_info_sync(
        self, info_resource: Info, get_info_request: GetInfoRequest, request_option: RequestOption
    ) -> None:
        mock_response = GetInfoResponse(
            name="Test App", description="Test Description", mode="completion", author_name="Test Author"
        )

        with patch("dify_oapi.core.http.transport.Transport.execute", return_value=mock_response) as mock_execute:
            response = info_resource.get_info(get_info_request, request_option)

            assert response == mock_response
            mock_execute.assert_called_once_with(
                info_resource.config, get_info_request, unmarshal_as=GetInfoResponse, option=request_option
            )

    @pytest.mark.asyncio
    async def test_get_info_async(
        self, info_resource: Info, get_info_request: GetInfoRequest, request_option: RequestOption
    ) -> None:
        mock_response = GetInfoResponse(
            name="Test App", description="Test Description", mode="completion", author_name="Test Author"
        )

        with patch(
            "dify_oapi.core.http.transport.ATransport.aexecute", new_callable=AsyncMock, return_value=mock_response
        ) as mock_aexecute:
            response = await info_resource.aget_info(get_info_request, request_option)

            assert response == mock_response
            mock_aexecute.assert_called_once_with(
                info_resource.config, get_info_request, unmarshal_as=GetInfoResponse, option=request_option
            )

    def test_get_parameters_sync(
        self, info_resource: Info, get_parameters_request: GetParametersRequest, request_option: RequestOption
    ) -> None:
        mock_response = GetParametersResponse(opening_statement="Welcome", suggested_questions=["What can you do?"])

        with patch("dify_oapi.core.http.transport.Transport.execute", return_value=mock_response) as mock_execute:
            response = info_resource.get_parameters(get_parameters_request, request_option)

            assert response == mock_response
            mock_execute.assert_called_once_with(
                info_resource.config, get_parameters_request, unmarshal_as=GetParametersResponse, option=request_option
            )

    @pytest.mark.asyncio
    async def test_get_parameters_async(
        self, info_resource: Info, get_parameters_request: GetParametersRequest, request_option: RequestOption
    ) -> None:
        mock_response = GetParametersResponse(opening_statement="Welcome", suggested_questions=["What can you do?"])

        with patch(
            "dify_oapi.core.http.transport.ATransport.aexecute", new_callable=AsyncMock, return_value=mock_response
        ) as mock_aexecute:
            response = await info_resource.aget_parameters(get_parameters_request, request_option)

            assert response == mock_response
            mock_aexecute.assert_called_once_with(
                info_resource.config, get_parameters_request, unmarshal_as=GetParametersResponse, option=request_option
            )

    def test_get_site_sync(
        self, info_resource: Info, get_site_request: GetSiteRequest, request_option: RequestOption
    ) -> None:
        mock_response = GetSiteResponse(
            title="Test Site", description="Test Site Description", icon_type="emoji", icon="🤖"
        )

        with patch("dify_oapi.core.http.transport.Transport.execute", return_value=mock_response) as mock_execute:
            response = info_resource.get_site(get_site_request, request_option)

            assert response == mock_response
            mock_execute.assert_called_once_with(
                info_resource.config, get_site_request, unmarshal_as=GetSiteResponse, option=request_option
            )

    @pytest.mark.asyncio
    async def test_get_site_async(
        self, info_resource: Info, get_site_request: GetSiteRequest, request_option: RequestOption
    ) -> None:
        mock_response = GetSiteResponse(
            title="Test Site", description="Test Site Description", icon_type="emoji", icon="🤖"
        )

        with patch(
            "dify_oapi.core.http.transport.ATransport.aexecute", new_callable=AsyncMock, return_value=mock_response
        ) as mock_aexecute:
            response = await info_resource.aget_site(get_site_request, request_option)

            assert response == mock_response
            mock_aexecute.assert_called_once_with(
                info_resource.config, get_site_request, unmarshal_as=GetSiteResponse, option=request_option
            )

    def test_get_info_error_handling(
        self, info_resource: Info, get_info_request: GetInfoRequest, request_option: RequestOption
    ) -> None:
        with patch("dify_oapi.core.http.transport.Transport.execute", side_effect=Exception("API Error")):
            with pytest.raises(Exception, match="API Error"):
                info_resource.get_info(get_info_request, request_option)

    @pytest.mark.asyncio
    async def test_get_info_async_error_handling(
        self, info_resource: Info, get_info_request: GetInfoRequest, request_option: RequestOption
    ) -> None:
        with patch(
            "dify_oapi.core.http.transport.ATransport.aexecute",
            new_callable=AsyncMock,
            side_effect=Exception("API Error"),
        ):
            with pytest.raises(Exception, match="API Error"):
                await info_resource.aget_info(get_info_request, request_option)

    def test_get_parameters_error_handling(
        self, info_resource: Info, get_parameters_request: GetParametersRequest, request_option: RequestOption
    ) -> None:
        with patch("dify_oapi.core.http.transport.Transport.execute", side_effect=Exception("API Error")):
            with pytest.raises(Exception, match="API Error"):
                info_resource.get_parameters(get_parameters_request, request_option)

    @pytest.mark.asyncio
    async def test_get_parameters_async_error_handling(
        self, info_resource: Info, get_parameters_request: GetParametersRequest, request_option: RequestOption
    ) -> None:
        with patch(
            "dify_oapi.core.http.transport.ATransport.aexecute",
            new_callable=AsyncMock,
            side_effect=Exception("API Error"),
        ):
            with pytest.raises(Exception, match="API Error"):
                await info_resource.aget_parameters(get_parameters_request, request_option)

    def test_get_site_error_handling(
        self, info_resource: Info, get_site_request: GetSiteRequest, request_option: RequestOption
    ) -> None:
        with patch("dify_oapi.core.http.transport.Transport.execute", side_effect=Exception("API Error")):
            with pytest.raises(Exception, match="API Error"):
                info_resource.get_site(get_site_request, request_option)

    @pytest.mark.asyncio
    async def test_get_site_async_error_handling(
        self, info_resource: Info, get_site_request: GetSiteRequest, request_option: RequestOption
    ) -> None:
        with patch(
            "dify_oapi.core.http.transport.ATransport.aexecute",
            new_callable=AsyncMock,
            side_effect=Exception("API Error"),
        ):
            with pytest.raises(Exception, match="API Error"):
                await info_resource.aget_site(get_site_request, request_option)
