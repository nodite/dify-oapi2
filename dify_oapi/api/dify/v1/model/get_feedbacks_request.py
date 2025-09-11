from dify_oapi.core.enum import HttpMethod
from dify_oapi.core.model.base_request import BaseRequest


class GetFeedbacksRequest(BaseRequest):
    def __init__(self) -> None:
        super().__init__()

    @staticmethod
    def builder() -> "GetFeedbacksRequestBuilder":
        return GetFeedbacksRequestBuilder()


class GetFeedbacksRequestBuilder:
    def __init__(self) -> None:
        get_feedbacks_request = GetFeedbacksRequest()
        get_feedbacks_request.http_method = HttpMethod.GET
        get_feedbacks_request.uri = "/v1/app/feedbacks"
        self._get_feedbacks_request = get_feedbacks_request

    def page(self, page: int | None) -> "GetFeedbacksRequestBuilder":
        if page is not None:
            self._get_feedbacks_request.add_query("page", str(page))
        return self

    def limit(self, limit: int | None) -> "GetFeedbacksRequestBuilder":
        if limit is not None:
            self._get_feedbacks_request.add_query("limit", str(limit))
        return self

    def build(self) -> GetFeedbacksRequest:
        return self._get_feedbacks_request
