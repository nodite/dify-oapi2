from __future__ import annotations

from dify_oapi.core.http.transport import ATransport, Transport
from dify_oapi.core.model.config import Config
from dify_oapi.core.model.request_option import RequestOption

from ..model.info.get_info_request import GetInfoRequest
from ..model.info.get_info_response import GetInfoResponse
from ..model.info.get_parameters_request import GetParametersRequest
from ..model.info.get_parameters_response import GetParametersResponse
from ..model.info.get_site_request import GetSiteRequest
from ..model.info.get_site_response import GetSiteResponse


class Info:
    def __init__(self, config: Config) -> None:
        self.config = config

    def get_info(self, request: GetInfoRequest, request_option: RequestOption) -> GetInfoResponse:
        """Get application basic information.

        Args:
            request: The get info request
            request_option: Request options including API key

        Returns:
            GetInfoResponse with application information
        """
        return Transport.execute(self.config, request, unmarshal_as=GetInfoResponse, option=request_option)

    async def aget_info(self, request: GetInfoRequest, request_option: RequestOption) -> GetInfoResponse:
        """Get application basic information asynchronously.

        Args:
            request: The get info request
            request_option: Request options including API key

        Returns:
            GetInfoResponse with application information
        """
        return await ATransport.aexecute(self.config, request, unmarshal_as=GetInfoResponse, option=request_option)

    def get_parameters(self, request: GetParametersRequest, request_option: RequestOption) -> GetParametersResponse:
        """Get application parameters.

        Args:
            request: The get parameters request
            request_option: Request options including API key

        Returns:
            GetParametersResponse with application parameters
        """
        return Transport.execute(self.config, request, unmarshal_as=GetParametersResponse, option=request_option)

    async def aget_parameters(
        self, request: GetParametersRequest, request_option: RequestOption
    ) -> GetParametersResponse:
        """Get application parameters asynchronously.

        Args:
            request: The get parameters request
            request_option: Request options including API key

        Returns:
            GetParametersResponse with application parameters
        """
        return await ATransport.aexecute(
            self.config, request, unmarshal_as=GetParametersResponse, option=request_option
        )

    def get_site(self, request: GetSiteRequest, request_option: RequestOption) -> GetSiteResponse:
        """Get WebApp settings.

        Args:
            request: The get site request
            request_option: Request options including API key

        Returns:
            GetSiteResponse with WebApp settings
        """
        return Transport.execute(self.config, request, unmarshal_as=GetSiteResponse, option=request_option)

    async def aget_site(self, request: GetSiteRequest, request_option: RequestOption) -> GetSiteResponse:
        """Get WebApp settings asynchronously.

        Args:
            request: The get site request
            request_option: Request options including API key

        Returns:
            GetSiteResponse with WebApp settings
        """
        return await ATransport.aexecute(self.config, request, unmarshal_as=GetSiteResponse, option=request_option)
