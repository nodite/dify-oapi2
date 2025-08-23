from __future__ import annotations

from dify_oapi.core.http.transport import ATransport, Transport
from dify_oapi.core.model.config import Config
from dify_oapi.core.model.request_option import RequestOption

from ..model.feedback.get_feedbacks_request import GetFeedbacksRequest
from ..model.feedback.get_feedbacks_response import GetFeedbacksResponse
from ..model.feedback.message_feedback_request import MessageFeedbackRequest
from ..model.feedback.message_feedback_response import MessageFeedbackResponse


class Feedback:
    def __init__(self, config: Config) -> None:
        self.config: Config = config

    def message_feedback(
        self, request: MessageFeedbackRequest, request_option: RequestOption
    ) -> MessageFeedbackResponse:
        return Transport.execute(self.config, request, unmarshal_as=MessageFeedbackResponse, option=request_option)

    async def amessage_feedback(
        self, request: MessageFeedbackRequest, request_option: RequestOption
    ) -> MessageFeedbackResponse:
        return await ATransport.aexecute(
            self.config, request, unmarshal_as=MessageFeedbackResponse, option=request_option
        )

    def get_feedbacks(self, request: GetFeedbacksRequest, request_option: RequestOption) -> GetFeedbacksResponse:
        return Transport.execute(self.config, request, unmarshal_as=GetFeedbacksResponse, option=request_option)

    async def aget_feedbacks(self, request: GetFeedbacksRequest, request_option: RequestOption) -> GetFeedbacksResponse:
        return await ATransport.aexecute(self.config, request, unmarshal_as=GetFeedbacksResponse, option=request_option)
