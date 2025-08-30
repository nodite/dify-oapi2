from collections.abc import AsyncGenerator, Generator
from typing import Literal, overload

from dify_oapi.core.http.transport import ATransport, Transport
from dify_oapi.core.model.config import Config
from dify_oapi.core.model.request_option import RequestOption

from ..model.get_info_request import GetInfoRequest
from ..model.get_info_response import GetInfoResponse
from ..model.get_parameters_request import GetParametersRequest
from ..model.get_parameters_response import GetParametersResponse
from ..model.get_site_request import GetSiteRequest
from ..model.get_site_response import GetSiteResponse
from ..model.get_workflow_logs_request import GetWorkflowLogsRequest
from ..model.get_workflow_logs_response import GetWorkflowLogsResponse
from ..model.get_workflow_run_detail_request import GetWorkflowRunDetailRequest
from ..model.get_workflow_run_detail_response import GetWorkflowRunDetailResponse
from ..model.run_workflow_request import RunWorkflowRequest
from ..model.run_workflow_response import RunWorkflowResponse
from ..model.stop_workflow_request import StopWorkflowRequest
from ..model.stop_workflow_response import StopWorkflowResponse
from ..model.upload_file_request import UploadFileRequest
from ..model.upload_file_response import UploadFileResponse


class Workflow:
    def __init__(self, config: Config) -> None:
        self.config = config

    @overload
    def run(
        self,
        request: RunWorkflowRequest,
        request_option: RequestOption,
        stream: Literal[True],
    ) -> Generator[bytes, None, None]: ...

    @overload
    def run(
        self,
        request: RunWorkflowRequest,
        request_option: RequestOption,
        stream: Literal[False] = False,
    ) -> RunWorkflowResponse: ...

    def run(
        self,
        request: RunWorkflowRequest,
        request_option: RequestOption,
        stream: bool = False,
    ) -> RunWorkflowResponse | Generator[bytes, None, None]:
        if stream:
            return Transport.execute(self.config, request, stream=True, option=request_option)
        return Transport.execute(self.config, request, unmarshal_as=RunWorkflowResponse, option=request_option)

    @overload
    async def arun(
        self,
        request: RunWorkflowRequest,
        request_option: RequestOption,
        stream: Literal[True],
    ) -> AsyncGenerator[bytes, None]: ...

    @overload
    async def arun(
        self,
        request: RunWorkflowRequest,
        request_option: RequestOption,
        stream: Literal[False] = False,
    ) -> RunWorkflowResponse: ...

    async def arun(
        self,
        request: RunWorkflowRequest,
        request_option: RequestOption,
        stream: bool = False,
    ) -> RunWorkflowResponse | AsyncGenerator[bytes, None]:
        if stream:
            return await ATransport.aexecute(self.config, request, stream=True, option=request_option)
        return await ATransport.aexecute(self.config, request, unmarshal_as=RunWorkflowResponse, option=request_option)

    def detail(
        self, request: GetWorkflowRunDetailRequest, request_option: RequestOption
    ) -> GetWorkflowRunDetailResponse:
        return Transport.execute(self.config, request, unmarshal_as=GetWorkflowRunDetailResponse, option=request_option)

    async def adetail(
        self, request: GetWorkflowRunDetailRequest, request_option: RequestOption
    ) -> GetWorkflowRunDetailResponse:
        return await ATransport.aexecute(
            self.config, request, unmarshal_as=GetWorkflowRunDetailResponse, option=request_option
        )

    def stop(self, request: StopWorkflowRequest, request_option: RequestOption) -> StopWorkflowResponse:
        return Transport.execute(self.config, request, unmarshal_as=StopWorkflowResponse, option=request_option)

    async def astop(self, request: StopWorkflowRequest, request_option: RequestOption) -> StopWorkflowResponse:
        return await ATransport.aexecute(self.config, request, unmarshal_as=StopWorkflowResponse, option=request_option)

    def upload(self, request: UploadFileRequest, request_option: RequestOption) -> UploadFileResponse:
        return Transport.execute(self.config, request, unmarshal_as=UploadFileResponse, option=request_option)

    async def aupload(self, request: UploadFileRequest, request_option: RequestOption) -> UploadFileResponse:
        return await ATransport.aexecute(self.config, request, unmarshal_as=UploadFileResponse, option=request_option)

    def logs(self, request: GetWorkflowLogsRequest, request_option: RequestOption) -> GetWorkflowLogsResponse:
        return Transport.execute(self.config, request, unmarshal_as=GetWorkflowLogsResponse, option=request_option)

    async def alogs(self, request: GetWorkflowLogsRequest, request_option: RequestOption) -> GetWorkflowLogsResponse:
        return await ATransport.aexecute(
            self.config, request, unmarshal_as=GetWorkflowLogsResponse, option=request_option
        )

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

    def site(self, request: GetSiteRequest, request_option: RequestOption) -> GetSiteResponse:
        return Transport.execute(self.config, request, unmarshal_as=GetSiteResponse, option=request_option)

    async def asite(self, request: GetSiteRequest, request_option: RequestOption) -> GetSiteResponse:
        return await ATransport.aexecute(self.config, request, unmarshal_as=GetSiteResponse, option=request_option)
