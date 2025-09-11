from dify_oapi.core.model.base_response import BaseResponse

from .feedback_info import FeedbackInfo


class GetAppFeedbacksResponse(BaseResponse):
    data: list[FeedbackInfo] | None = None

    @staticmethod
    def builder() -> "GetAppFeedbacksResponseBuilder":
        return GetAppFeedbacksResponseBuilder()


class GetAppFeedbacksResponseBuilder:
    def __init__(self):
        self._get_app_feedbacks_response = GetAppFeedbacksResponse()

    def build(self) -> GetAppFeedbacksResponse:
        return self._get_app_feedbacks_response

    def data(self, data: list[FeedbackInfo]) -> "GetAppFeedbacksResponseBuilder":
        self._get_app_feedbacks_response.data = data
        return self
