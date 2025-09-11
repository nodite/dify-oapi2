from dify_oapi.core.http.transport import ATransport, Transport
from dify_oapi.core.model.config import Config
from dify_oapi.core.model.request_option import RequestOption

from ..model.get_feedbacks_request import GetFeedbacksRequest
from ..model.get_feedbacks_response import GetFeedbacksResponse
from ..model.submit_feedback_request import SubmitFeedbackRequest
from ..model.submit_feedback_response import SubmitFeedbackResponse


class Feedback:
    def __init__(self, config: Config) -> None:
        self.config = config

    def submit(self, request: SubmitFeedbackRequest, request_option: RequestOption) -> SubmitFeedbackResponse:
        return Transport.execute(self.config, request, unmarshal_as=SubmitFeedbackResponse, option=request_option)

    async def asubmit(self, request: SubmitFeedbackRequest, request_option: RequestOption) -> SubmitFeedbackResponse:
        return await ATransport.aexecute(
            self.config, request, unmarshal_as=SubmitFeedbackResponse, option=request_option
        )

    def list(self, request: GetFeedbacksRequest, request_option: RequestOption) -> GetFeedbacksResponse:
        return Transport.execute(self.config, request, unmarshal_as=GetFeedbacksResponse, option=request_option)

    async def alist(self, request: GetFeedbacksRequest, request_option: RequestOption) -> GetFeedbacksResponse:
        return await ATransport.aexecute(self.config, request, unmarshal_as=GetFeedbacksResponse, option=request_option)
