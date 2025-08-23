from __future__ import annotations

from dify_oapi.core.enum import HttpMethod
from dify_oapi.core.model.base_request import BaseRequest


class GetFeedbacksRequest(BaseRequest):
    def __init__(self):
        super().__init__()

    @staticmethod
    def builder() -> GetFeedbacksRequestBuilder:
        return GetFeedbacksRequestBuilder()


class GetFeedbacksRequestBuilder:
    def __init__(self):
        get_feedbacks_request = GetFeedbacksRequest()
        get_feedbacks_request.http_method = HttpMethod.GET
        get_feedbacks_request.uri = "/v1/app/feedbacks"
        self._get_feedbacks_request = get_feedbacks_request

    def build(self) -> GetFeedbacksRequest:
        return self._get_feedbacks_request

    def page(self, page: str) -> GetFeedbacksRequestBuilder:
        self._get_feedbacks_request.add_query("page", page)
        return self

    def limit(self, limit: str) -> GetFeedbacksRequestBuilder:
        self._get_feedbacks_request.add_query("limit", limit)
        return self
