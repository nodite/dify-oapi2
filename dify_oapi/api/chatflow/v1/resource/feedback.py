from __future__ import annotations

from dify_oapi.core.http.transport import ATransport, Transport
from dify_oapi.core.model.config import Config
from dify_oapi.core.model.request_option import RequestOption

from ..model.get_app_feedbacks_request import GetAppFeedbacksRequest
from ..model.get_app_feedbacks_response import GetAppFeedbacksResponse
from ..model.message_feedback_request import MessageFeedbackRequest
from ..model.message_feedback_response import MessageFeedbackResponse


class Feedback:
    """Feedback resource for chatflow API operations."""

    def __init__(self, config: Config):
        self.config = config

    def message(self, request: MessageFeedbackRequest, request_option: RequestOption) -> MessageFeedbackResponse:
        """Provide feedback for a message.

        Args:
            request: Message feedback request
            request_option: Request options including API key

        Returns:
            Message feedback response
        """
        return Transport.execute(self.config, request, unmarshal_as=MessageFeedbackResponse, option=request_option)

    async def amessage(self, request: MessageFeedbackRequest, request_option: RequestOption) -> MessageFeedbackResponse:
        """Provide feedback for a message (async).

        Args:
            request: Message feedback request
            request_option: Request options including API key

        Returns:
            Message feedback response
        """
        return await ATransport.aexecute(
            self.config, request, unmarshal_as=MessageFeedbackResponse, option=request_option
        )

    def list(self, request: GetAppFeedbacksRequest, request_option: RequestOption) -> GetAppFeedbacksResponse:
        """Get application feedbacks.

        Args:
            request: Get app feedbacks request
            request_option: Request options including API key

        Returns:
            Get app feedbacks response with feedback list
        """
        return Transport.execute(self.config, request, unmarshal_as=GetAppFeedbacksResponse, option=request_option)

    async def alist(self, request: GetAppFeedbacksRequest, request_option: RequestOption) -> GetAppFeedbacksResponse:
        """Get application feedbacks (async).

        Args:
            request: Get app feedbacks request
            request_option: Request options including API key

        Returns:
            Get app feedbacks response with feedback list
        """
        return await ATransport.aexecute(
            self.config, request, unmarshal_as=GetAppFeedbacksResponse, option=request_option
        )
