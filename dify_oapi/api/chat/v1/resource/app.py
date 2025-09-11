from dify_oapi.core.http.transport import ATransport, Transport
from dify_oapi.core.model.config import Config
from dify_oapi.core.model.request_option import RequestOption

from ..model.get_app_info_request import GetAppInfoRequest
from ..model.get_app_info_response import GetAppInfoResponse
from ..model.get_app_meta_request import GetAppMetaRequest
from ..model.get_app_meta_response import GetAppMetaResponse
from ..model.get_app_parameters_request import GetAppParametersRequest
from ..model.get_app_parameters_response import GetAppParametersResponse
from ..model.get_site_settings_request import GetSiteSettingsRequest
from ..model.get_site_settings_response import GetSiteSettingsResponse


class App:
    def __init__(self, config: Config) -> None:
        self.config = config

    def info(self, request: GetAppInfoRequest, request_option: RequestOption) -> GetAppInfoResponse:
        return Transport.execute(self.config, request, unmarshal_as=GetAppInfoResponse, option=request_option)

    async def ainfo(self, request: GetAppInfoRequest, request_option: RequestOption) -> GetAppInfoResponse:
        return await ATransport.aexecute(self.config, request, unmarshal_as=GetAppInfoResponse, option=request_option)

    def parameters(self, request: GetAppParametersRequest, request_option: RequestOption) -> GetAppParametersResponse:
        return Transport.execute(self.config, request, unmarshal_as=GetAppParametersResponse, option=request_option)

    async def aparameters(
        self, request: GetAppParametersRequest, request_option: RequestOption
    ) -> GetAppParametersResponse:
        return await ATransport.aexecute(
            self.config, request, unmarshal_as=GetAppParametersResponse, option=request_option
        )

    def meta(self, request: GetAppMetaRequest, request_option: RequestOption) -> GetAppMetaResponse:
        return Transport.execute(self.config, request, unmarshal_as=GetAppMetaResponse, option=request_option)

    async def ameta(self, request: GetAppMetaRequest, request_option: RequestOption) -> GetAppMetaResponse:
        return await ATransport.aexecute(self.config, request, unmarshal_as=GetAppMetaResponse, option=request_option)

    def site(self, request: GetSiteSettingsRequest, request_option: RequestOption) -> GetSiteSettingsResponse:
        return Transport.execute(self.config, request, unmarshal_as=GetSiteSettingsResponse, option=request_option)

    async def asite(self, request: GetSiteSettingsRequest, request_option: RequestOption) -> GetSiteSettingsResponse:
        return await ATransport.aexecute(
            self.config, request, unmarshal_as=GetSiteSettingsResponse, option=request_option
        )
