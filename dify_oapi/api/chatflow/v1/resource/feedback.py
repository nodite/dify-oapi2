from dify_oapi.core.http.transport import ATransport, Transport
from dify_oapi.core.model.config import Config
from dify_oapi.core.model.request_option import RequestOption

from ..model.get_app_feedbacks_request import GetAppFeedbacksRequest
from ..model.get_app_feedbacks_response import GetAppFeedbacksResponse
from ..model.message_feedback_request import MessageFeedbackRequest
from ..model.message_feedback_response import MessageFeedbackResponse


class Feedback:
    def __init__(self, config: Config) -> None:
        self.config = config

    def message(self, request: MessageFeedbackRequest, request_option: RequestOption) -> MessageFeedbackResponse:
        return Transport.execute(self.config, request, unmarshal_as=MessageFeedbackResponse, option=request_option)

    async def amessage(self, request: MessageFeedbackRequest, request_option: RequestOption) -> MessageFeedbackResponse:
        return await ATransport.aexecute(
            self.config, request, unmarshal_as=MessageFeedbackResponse, option=request_option
        )

    def list(self, request: GetAppFeedbacksRequest, request_option: RequestOption) -> GetAppFeedbacksResponse:
        return Transport.execute(self.config, request, unmarshal_as=GetAppFeedbacksResponse, option=request_option)

    async def alist(self, request: GetAppFeedbacksRequest, request_option: RequestOption) -> GetAppFeedbacksResponse:
        return await ATransport.aexecute(
            self.config, request, unmarshal_as=GetAppFeedbacksResponse, option=request_option
        )
