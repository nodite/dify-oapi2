from __future__ import annotations

from dify_oapi.core.http.transport import ATransport, Transport
from dify_oapi.core.model.config import Config
from dify_oapi.core.model.request_option import RequestOption

from ..model.log.get_workflow_logs_request import GetWorkflowLogsRequest
from ..model.log.get_workflow_logs_response import GetWorkflowLogsResponse


class Log:
    def __init__(self, config: Config) -> None:
        self.config = config

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
