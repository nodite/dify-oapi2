from collections.abc import AsyncGenerator, Generator
from typing import Literal, overload

from dify_oapi.core.http.transport import ATransport, Transport
from dify_oapi.core.model.config import Config
from dify_oapi.core.model.request_option import RequestOption

from ..model.workflow.get_workflow_run_detail_request import GetWorkflowRunDetailRequest
from ..model.workflow.get_workflow_run_detail_response import GetWorkflowRunDetailResponse
from ..model.workflow.run_specific_workflow_request import RunSpecificWorkflowRequest
from ..model.workflow.run_specific_workflow_response import RunSpecificWorkflowResponse
from ..model.workflow.run_workflow_request import RunWorkflowRequest
from ..model.workflow.run_workflow_response import RunWorkflowResponse
from ..model.workflow.stop_workflow_request import StopWorkflowRequest
from ..model.workflow.stop_workflow_response import StopWorkflowResponse


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

    @overload
    def run_specific_workflow(
        self,
        request: RunSpecificWorkflowRequest,
        request_option: RequestOption,
        stream: Literal[True],
    ) -> Generator[bytes, None, None]: ...

    @overload
    def run_specific_workflow(
        self,
        request: RunSpecificWorkflowRequest,
        request_option: RequestOption,
        stream: Literal[False] = False,
    ) -> RunSpecificWorkflowResponse: ...

    def run_specific_workflow(
        self,
        request: RunSpecificWorkflowRequest,
        request_option: RequestOption,
        stream: bool = False,
    ) -> RunSpecificWorkflowResponse | Generator[bytes, None, None]:
        """Execute specific version workflow.

        Args:
            request: The run specific workflow request
            request_option: Request options including API key
            stream: Whether to use streaming mode

        Returns:
            RunSpecificWorkflowResponse for blocking mode or Generator[bytes, None, None] for streaming mode
        """
        if stream:
            return Transport.execute(self.config, request, stream=True, option=request_option)
        return Transport.execute(self.config, request, unmarshal_as=RunSpecificWorkflowResponse, option=request_option)

    @overload
    async def arun_specific_workflow(
        self,
        request: RunSpecificWorkflowRequest,
        request_option: RequestOption,
        stream: Literal[True],
    ) -> AsyncGenerator[bytes, None]: ...

    @overload
    async def arun_specific_workflow(
        self,
        request: RunSpecificWorkflowRequest,
        request_option: RequestOption,
        stream: Literal[False] = False,
    ) -> RunSpecificWorkflowResponse: ...

    async def arun_specific_workflow(
        self,
        request: RunSpecificWorkflowRequest,
        request_option: RequestOption,
        stream: bool = False,
    ) -> RunSpecificWorkflowResponse | AsyncGenerator[bytes, None]:
        """Execute specific version workflow asynchronously.

        Args:
            request: The run specific workflow request
            request_option: Request options including API key
            stream: Whether to use streaming mode

        Returns:
            RunSpecificWorkflowResponse for blocking mode or AsyncGenerator[bytes, None] for streaming mode
        """
        if stream:
            return await ATransport.aexecute(self.config, request, stream=True, option=request_option)
        return await ATransport.aexecute(
            self.config, request, unmarshal_as=RunSpecificWorkflowResponse, option=request_option
        )

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
