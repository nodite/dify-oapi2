from dify_oapi.core.http.transport import ATransport, Transport
from dify_oapi.core.model.config import Config
from dify_oapi.core.model.request_option import RequestOption

from ..model.get_feedbacks_request import GetFeedbacksRequest
from ..model.get_feedbacks_response import GetFeedbacksResponse
from ..model.submit_feedback_request import SubmitFeedbackRequest
from ..model.submit_feedback_response import SubmitFeedbackResponse


class Feedback:
    def __init__(self, config: Config):
        self.config = config

    def submit(self, request: SubmitFeedbackRequest, option: RequestOption | None = None) -> SubmitFeedbackResponse:
        """Submit feedback for a message."""
        return Transport.execute(self.config, request, unmarshal_as=SubmitFeedbackResponse, option=option)

    async def asubmit(
        self, request: SubmitFeedbackRequest, option: RequestOption | None = None
    ) -> SubmitFeedbackResponse:
        """Submit feedback for a message asynchronously."""
        return await ATransport.aexecute(self.config, request, unmarshal_as=SubmitFeedbackResponse, option=option)

    def list(self, request: GetFeedbacksRequest, option: RequestOption | None = None) -> GetFeedbacksResponse:
        """Get application feedbacks."""
        return Transport.execute(self.config, request, unmarshal_as=GetFeedbacksResponse, option=option)

    async def alist(self, request: GetFeedbacksRequest, option: RequestOption | None = None) -> GetFeedbacksResponse:
        """Get application feedbacks asynchronously."""
        return await ATransport.aexecute(self.config, request, unmarshal_as=GetFeedbacksResponse, option=option)
