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
        self.config: Config = config

    def get_info(self, request: GetInfoRequest, request_option: RequestOption) -> GetInfoResponse:
        return Transport.execute(self.config, request, unmarshal_as=GetInfoResponse, option=request_option)

    async def aget_info(self, request: GetInfoRequest, request_option: RequestOption) -> GetInfoResponse:
        return await ATransport.aexecute(self.config, request, unmarshal_as=GetInfoResponse, option=request_option)

    def get_parameters(self, request: GetParametersRequest, request_option: RequestOption) -> GetParametersResponse:
        return Transport.execute(self.config, request, unmarshal_as=GetParametersResponse, option=request_option)

    async def aget_parameters(
        self, request: GetParametersRequest, request_option: RequestOption
    ) -> GetParametersResponse:
        return await ATransport.aexecute(
            self.config, request, unmarshal_as=GetParametersResponse, option=request_option
        )

    def get_site(self, request: GetSiteRequest, request_option: RequestOption) -> GetSiteResponse:
        return Transport.execute(self.config, request, unmarshal_as=GetSiteResponse, option=request_option)

    async def aget_site(self, request: GetSiteRequest, request_option: RequestOption) -> GetSiteResponse:
        return await ATransport.aexecute(self.config, request, unmarshal_as=GetSiteResponse, option=request_option)
