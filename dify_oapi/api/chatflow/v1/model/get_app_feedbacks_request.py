from dify_oapi.core.enum import HttpMethod
from dify_oapi.core.model.base_request import BaseRequest


class GetAppFeedbacksRequest(BaseRequest):
    def __init__(self):
        super().__init__()

    @staticmethod
    def builder() -> "GetAppFeedbacksRequestBuilder":
        return GetAppFeedbacksRequestBuilder()


class GetAppFeedbacksRequestBuilder:
    def __init__(self):
        get_app_feedbacks_request = GetAppFeedbacksRequest()
        get_app_feedbacks_request.http_method = HttpMethod.GET
        get_app_feedbacks_request.uri = "/v1/app/feedbacks"
        self._get_app_feedbacks_request = get_app_feedbacks_request

    def build(self) -> GetAppFeedbacksRequest:
        return self._get_app_feedbacks_request

    def page(self, page: int) -> "GetAppFeedbacksRequestBuilder":
        self._get_app_feedbacks_request.add_query("page", str(page))
        return self

    def limit(self, limit: int) -> "GetAppFeedbacksRequestBuilder":
        self._get_app_feedbacks_request.add_query("limit", str(limit))
        return self
