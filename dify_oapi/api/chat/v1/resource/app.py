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
        self.config: Config = config

    def info(self, request: GetAppInfoRequest, option: RequestOption | None = None) -> GetAppInfoResponse:
        return Transport.execute(self.config, request, unmarshal_as=GetAppInfoResponse, option=option)

    async def ainfo(self, request: GetAppInfoRequest, option: RequestOption | None = None) -> GetAppInfoResponse:
        return await ATransport.aexecute(self.config, request, unmarshal_as=GetAppInfoResponse, option=option)

    def parameters(
        self, request: GetAppParametersRequest, option: RequestOption | None = None
    ) -> GetAppParametersResponse:
        return Transport.execute(self.config, request, unmarshal_as=GetAppParametersResponse, option=option)

    async def aparameters(
        self, request: GetAppParametersRequest, option: RequestOption | None = None
    ) -> GetAppParametersResponse:
        return await ATransport.aexecute(self.config, request, unmarshal_as=GetAppParametersResponse, option=option)

    def meta(self, request: GetAppMetaRequest, option: RequestOption | None = None) -> GetAppMetaResponse:
        return Transport.execute(self.config, request, unmarshal_as=GetAppMetaResponse, option=option)

    async def ameta(self, request: GetAppMetaRequest, option: RequestOption | None = None) -> GetAppMetaResponse:
        return await ATransport.aexecute(self.config, request, unmarshal_as=GetAppMetaResponse, option=option)

    def site(self, request: GetSiteSettingsRequest, option: RequestOption | None = None) -> GetSiteSettingsResponse:
        return Transport.execute(self.config, request, unmarshal_as=GetSiteSettingsResponse, option=option)

    async def asite(
        self, request: GetSiteSettingsRequest, option: RequestOption | None = None
    ) -> GetSiteSettingsResponse:
        return await ATransport.aexecute(self.config, request, unmarshal_as=GetSiteSettingsResponse, option=option)
