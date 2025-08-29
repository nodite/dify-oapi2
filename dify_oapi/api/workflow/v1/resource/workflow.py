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
    def run_workflow(
        self,
        request: RunWorkflowRequest,
        request_option: RequestOption,
        stream: Literal[True],
    ) -> Generator[bytes, None, None]: ...

    @overload
    def run_workflow(
        self,
        request: RunWorkflowRequest,
        request_option: RequestOption,
        stream: Literal[False] = False,
    ) -> RunWorkflowResponse: ...

    def run_workflow(
        self,
        request: RunWorkflowRequest,
        request_option: RequestOption,
        stream: bool = False,
    ) -> RunWorkflowResponse | Generator[bytes, None, None]:
        """Execute workflow.

        Args:
            request: The run workflow request
            request_option: Request options including API key
            stream: Whether to use streaming mode

        Returns:
            RunWorkflowResponse for blocking mode or Generator[bytes, None, None] for streaming mode
        """
        if stream:
            return Transport.execute(self.config, request, stream=True, option=request_option)
        return Transport.execute(self.config, request, unmarshal_as=RunWorkflowResponse, option=request_option)

    @overload
    async def arun_workflow(
        self,
        request: RunWorkflowRequest,
        request_option: RequestOption,
        stream: Literal[True],
    ) -> AsyncGenerator[bytes, None]: ...

    @overload
    async def arun_workflow(
        self,
        request: RunWorkflowRequest,
        request_option: RequestOption,
        stream: Literal[False] = False,
    ) -> RunWorkflowResponse: ...

    async def arun_workflow(
        self,
        request: RunWorkflowRequest,
        request_option: RequestOption,
        stream: bool = False,
    ) -> RunWorkflowResponse | AsyncGenerator[bytes, None]:
        """Execute workflow asynchronously.

        Args:
            request: The run workflow request
            request_option: Request options including API key
            stream: Whether to use streaming mode

        Returns:
            RunWorkflowResponse for blocking mode or AsyncGenerator[bytes, None] for streaming mode
        """
        if stream:
            return await ATransport.aexecute(self.config, request, stream=True, option=request_option)
        return await ATransport.aexecute(self.config, request, unmarshal_as=RunWorkflowResponse, option=request_option)

    def get_workflow_run_detail(
        self, request: GetWorkflowRunDetailRequest, request_option: RequestOption
    ) -> GetWorkflowRunDetailResponse:
        """Get workflow execution details.

        Args:
            request: The get workflow run detail request
            request_option: Request options including API key

        Returns:
            GetWorkflowRunDetailResponse with workflow execution details
        """
        return Transport.execute(self.config, request, unmarshal_as=GetWorkflowRunDetailResponse, option=request_option)

    async def aget_workflow_run_detail(
        self, request: GetWorkflowRunDetailRequest, request_option: RequestOption
    ) -> GetWorkflowRunDetailResponse:
        """Get workflow execution details asynchronously.

        Args:
            request: The get workflow run detail request
            request_option: Request options including API key

        Returns:
            GetWorkflowRunDetailResponse with workflow execution details
        """
        return await ATransport.aexecute(
            self.config, request, unmarshal_as=GetWorkflowRunDetailResponse, option=request_option
        )

    def stop_workflow(self, request: StopWorkflowRequest, request_option: RequestOption) -> StopWorkflowResponse:
        """Stop workflow execution.

        Args:
            request: The stop workflow request
            request_option: Request options including API key

        Returns:
            StopWorkflowResponse with stop result
        """
        return Transport.execute(self.config, request, unmarshal_as=StopWorkflowResponse, option=request_option)

    async def astop_workflow(self, request: StopWorkflowRequest, request_option: RequestOption) -> StopWorkflowResponse:
        """Stop workflow execution asynchronously.

        Args:
            request: The stop workflow request
            request_option: Request options including API key

        Returns:
            StopWorkflowResponse with stop result
        """
        return await ATransport.aexecute(self.config, request, unmarshal_as=StopWorkflowResponse, option=request_option)

    def upload_file(self, request: UploadFileRequest, request_option: RequestOption) -> UploadFileResponse:
        """Upload file for multimodal support.

        Args:
            request: The upload file request
            request_option: Request options including API key

        Returns:
            UploadFileResponse with file information
        """
        return Transport.execute(self.config, request, unmarshal_as=UploadFileResponse, option=request_option)

    async def aupload_file(self, request: UploadFileRequest, request_option: RequestOption) -> UploadFileResponse:
        """Upload file for multimodal support asynchronously.

        Args:
            request: The upload file request
            request_option: Request options including API key

        Returns:
            UploadFileResponse with file information
        """
        return await ATransport.aexecute(self.config, request, unmarshal_as=UploadFileResponse, option=request_option)

    def get_workflow_logs(
        self, request: GetWorkflowLogsRequest, request_option: RequestOption
    ) -> GetWorkflowLogsResponse:
        """Get workflow execution logs.

        Args:
            request: The get workflow logs request
            request_option: Request options including API key

        Returns:
            GetWorkflowLogsResponse with workflow logs
        """
        return Transport.execute(self.config, request, unmarshal_as=GetWorkflowLogsResponse, option=request_option)

    async def aget_workflow_logs(
        self, request: GetWorkflowLogsRequest, request_option: RequestOption
    ) -> GetWorkflowLogsResponse:
        """Get workflow execution logs asynchronously.

        Args:
            request: The get workflow logs request
            request_option: Request options including API key

        Returns:
            GetWorkflowLogsResponse with workflow logs
        """
        return await ATransport.aexecute(
            self.config, request, unmarshal_as=GetWorkflowLogsResponse, option=request_option
        )

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
            request_option: Request option including API key

        Returns:
            GetSiteResponse with WebApp settings
        """
        return await ATransport.aexecute(self.config, request, unmarshal_as=GetSiteResponse, option=request_option)
