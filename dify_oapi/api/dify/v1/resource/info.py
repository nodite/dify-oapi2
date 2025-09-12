from dify_oapi.core.http.transport import ATransport, Transport
from dify_oapi.core.model.config import Config
from dify_oapi.core.model.request_option import RequestOption

from ..model.get_info_request import GetInfoRequest
from ..model.get_info_response import GetInfoResponse
from ..model.get_meta_request import GetMetaRequest
from ..model.get_meta_response import GetMetaResponse
from ..model.get_parameters_request import GetParametersRequest
from ..model.get_parameters_response import GetParametersResponse
from ..model.get_site_request import GetSiteRequest
from ..model.get_site_response import GetSiteResponse


class Info:
    def __init__(self, config: Config) -> None:
        self.config: Config = config

    def get(self, request: GetInfoRequest, option: RequestOption | None = None) -> GetInfoResponse:
        """Get application information"""
        return Transport.execute(self.config, request, unmarshal_as=GetInfoResponse, option=option)

    async def aget(self, request: GetInfoRequest, option: RequestOption | None = None) -> GetInfoResponse:
        """Get application information - async version"""
        return await ATransport.aexecute(self.config, request, unmarshal_as=GetInfoResponse, option=option)

    def parameters(self, request: GetParametersRequest, option: RequestOption | None = None) -> GetParametersResponse:
        """Get application parameters"""
        return Transport.execute(self.config, request, unmarshal_as=GetParametersResponse, option=option)

    async def aparameters(
        self, request: GetParametersRequest, option: RequestOption | None = None
    ) -> GetParametersResponse:
        """Get application parameters - async version"""
        return await ATransport.aexecute(self.config, request, unmarshal_as=GetParametersResponse, option=option)

    def meta(self, request: GetMetaRequest, option: RequestOption | None = None) -> GetMetaResponse:
        """Get application metadata"""
        return Transport.execute(self.config, request, unmarshal_as=GetMetaResponse, option=option)

    async def ameta(self, request: GetMetaRequest, option: RequestOption | None = None) -> GetMetaResponse:
        """Get application metadata - async version"""
        return await ATransport.aexecute(self.config, request, unmarshal_as=GetMetaResponse, option=option)

    def site(self, request: GetSiteRequest, option: RequestOption | None = None) -> GetSiteResponse:
        """Get site settings"""
        return Transport.execute(self.config, request, unmarshal_as=GetSiteResponse, option=option)

    async def asite(self, request: GetSiteRequest, option: RequestOption | None = None) -> GetSiteResponse:
        """Get site settings - async version"""
        return await ATransport.aexecute(self.config, request, unmarshal_as=GetSiteResponse, option=option)
