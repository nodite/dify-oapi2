from dify_oapi.core.enum import HttpMethod
from dify_oapi.core.model.base_request import BaseRequest

from .submit_feedback_request_body import SubmitFeedbackRequestBody


class SubmitFeedbackRequest(BaseRequest):
    def __init__(self) -> None:
        super().__init__()
        self.request_body: SubmitFeedbackRequestBody | None = None

    @staticmethod
    def builder() -> "SubmitFeedbackRequestBuilder":
        return SubmitFeedbackRequestBuilder()


class SubmitFeedbackRequestBuilder:
    def __init__(self) -> None:
        submit_feedback_request = SubmitFeedbackRequest()
        submit_feedback_request.http_method = HttpMethod.POST
        submit_feedback_request.uri = "/v1/messages/:message_id/feedbacks"
        self._submit_feedback_request = submit_feedback_request

    def message_id(self, message_id: str) -> "SubmitFeedbackRequestBuilder":
        self._submit_feedback_request.paths["message_id"] = message_id
        return self

    def request_body(self, request_body: SubmitFeedbackRequestBody) -> "SubmitFeedbackRequestBuilder":
        self._submit_feedback_request.request_body = request_body
        self._submit_feedback_request.body = request_body.model_dump(exclude_none=True, mode="json")
        return self

    def build(self) -> SubmitFeedbackRequest:
        return self._submit_feedback_request
