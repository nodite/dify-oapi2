from dify_oapi.core.model.base_response import BaseResponse


class MessageFeedbackResponse(BaseResponse):
    result: str | None = None

    @staticmethod
    def builder() -> "MessageFeedbackResponseBuilder":
        return MessageFeedbackResponseBuilder()


class MessageFeedbackResponseBuilder:
    def __init__(self):
        self._message_feedback_response = MessageFeedbackResponse()

    def build(self) -> MessageFeedbackResponse:
        return self._message_feedback_response

    def result(self, result: str) -> "MessageFeedbackResponseBuilder":
        self._message_feedback_response.result = result
        return self
