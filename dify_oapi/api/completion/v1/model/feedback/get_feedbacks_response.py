from __future__ import annotations

from dify_oapi.core.model.base_response import BaseResponse

from .feedback_info import FeedbackInfo


class GetFeedbacksResponse(BaseResponse):
    data: list[FeedbackInfo] | None = None
