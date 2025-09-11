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


class Application:
    def __init__(self, config: Config) -> None:
        self.config = config

    def info(self, request: GetInfoRequest, request_option: RequestOption) -> GetInfoResponse:
        return Transport.execute(self.config, request, unmarshal_as=GetInfoResponse, option=request_option)

    async def ainfo(self, request: GetInfoRequest, request_option: RequestOption) -> GetInfoResponse:
        return await ATransport.aexecute(self.config, request, unmarshal_as=GetInfoResponse, option=request_option)

    def parameters(self, request: GetParametersRequest, request_option: RequestOption) -> GetParametersResponse:
        return Transport.execute(self.config, request, unmarshal_as=GetParametersResponse, option=request_option)

    async def aparameters(self, request: GetParametersRequest, request_option: RequestOption) -> GetParametersResponse:
        return await ATransport.aexecute(
            self.config, request, unmarshal_as=GetParametersResponse, option=request_option
        )

    def meta(self, request: GetMetaRequest, request_option: RequestOption) -> GetMetaResponse:
        return Transport.execute(self.config, request, unmarshal_as=GetMetaResponse, option=request_option)

    async def ameta(self, request: GetMetaRequest, request_option: RequestOption) -> GetMetaResponse:
        return await ATransport.aexecute(self.config, request, unmarshal_as=GetMetaResponse, option=request_option)

    def site(self, request: GetSiteRequest, request_option: RequestOption) -> GetSiteResponse:
        return Transport.execute(self.config, request, unmarshal_as=GetSiteResponse, option=request_option)

    async def asite(self, request: GetSiteRequest, request_option: RequestOption) -> GetSiteResponse:
        return await ATransport.aexecute(self.config, request, unmarshal_as=GetSiteResponse, option=request_option)
