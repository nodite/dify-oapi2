from dify_oapi.core.model.base_response import BaseResponse


class SubmitFeedbackResponse(BaseResponse):
    """Response for submit feedback API."""

    result: str | None = None
