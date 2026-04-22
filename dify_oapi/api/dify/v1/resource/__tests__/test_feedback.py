import httpx
import pytest
import respx

from dify_oapi.api.dify.v1.model.get_feedbacks_request import GetFeedbacksRequest
from dify_oapi.api.dify.v1.model.submit_feedback_request import SubmitFeedbackRequest
from dify_oapi.api.dify.v1.model.submit_feedback_request_body import SubmitFeedbackRequestBody
from dify_oapi.api.dify.v1.resource.feedback import Feedback


class TestFeedback:
    @pytest.fixture(autouse=True)
    def setup(self, config, request_option):
        self.resource = Feedback(config)
        self.option = request_option

    @respx.mock
    def test_submit(self):
        route = respx.post(
            url__regex=r"https://api\.dify\.ai/v1/messages/[^/]+/feedbacks"
        ).mock(return_value=httpx.Response(200, json={"result": "success"}))
        body = SubmitFeedbackRequestBody.builder().rating("like").user("u1").build()
        result = self.resource.submit(
            SubmitFeedbackRequest.builder().message_id("msg-123").request_body(body).build(),
            self.option,
        )
        assert result.result == "success"
        assert route.calls.last.request.headers["Authorization"] == "Bearer test-key"

    @respx.mock
    def test_list(self):
        route = respx.get("https://api.dify.ai/v1/app/feedbacks").mock(
            return_value=httpx.Response(200, json={"data": [], "total": 0, "page": 1, "limit": 20})
        )
        result = self.resource.list(
            GetFeedbacksRequest.builder().page(1).limit(20).build(), self.option
        )
        assert result.data == []
        assert route.calls.last.request.headers["Authorization"] == "Bearer test-key"
