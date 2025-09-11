from pydantic import BaseModel

from dify_oapi.core.model.base_response import BaseResponse


class FeedbackInfo(BaseModel):
    """Feedback information."""

    id: str | None = None
    username: str | None = None
    phone: str | None = None
    avatar: str | None = None
    display_name: str | None = None
    timestamp: int | None = None
    rating: str | None = None
    content: str | None = None


class GetFeedbacksResponse(BaseResponse):
    """Response for get feedbacks API."""

    data: list[FeedbackInfo] | None = None
    has_more: bool | None = None
    limit: int | None = None
    page: int | None = None
    total: int | None = None
