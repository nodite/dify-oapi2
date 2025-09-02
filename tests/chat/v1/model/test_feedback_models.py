from dify_oapi.api.chat.v1.model.feedback_info import FeedbackInfo
from dify_oapi.api.chat.v1.model.get_feedbacks_request import GetFeedbacksRequest
from dify_oapi.api.chat.v1.model.get_feedbacks_response import GetFeedbacksResponse
from dify_oapi.api.chat.v1.model.submit_feedback_request import SubmitFeedbackRequest
from dify_oapi.api.chat.v1.model.submit_feedback_request_body import SubmitFeedbackRequestBody
from dify_oapi.api.chat.v1.model.submit_feedback_response import SubmitFeedbackResponse
from dify_oapi.core.enum import HttpMethod
from dify_oapi.core.model.base_response import BaseResponse


class TestSubmitFeedbackModels:
    def test_submit_feedback_request_builder(self):
        """Test SubmitFeedbackRequest builder pattern"""
        request_body = (
            SubmitFeedbackRequestBody.builder().rating("like").user("user-123").content("Great response!").build()
        )
        request = SubmitFeedbackRequest.builder().message_id("msg-123").request_body(request_body).build()

        assert request.http_method == HttpMethod.POST
        assert request.uri == "/v1/messages/:message_id/feedbacks"
        assert request.paths["message_id"] == "msg-123"
        assert request.request_body.rating == "like"
        assert request.request_body.user == "user-123"
        assert request.request_body.content == "Great response!"

    def test_submit_feedback_request_body_validation(self):
        """Test SubmitFeedbackRequestBody field validation"""
        # Test valid rating
        body = SubmitFeedbackRequestBody.builder().rating("like").user("user-123").build()
        assert body.rating == "like"
        assert body.user == "user-123"

        # Test null rating
        body = SubmitFeedbackRequestBody.builder().rating(None).user("user-123").build()
        assert body.rating is None

        # Test dislike rating
        body = SubmitFeedbackRequestBody.builder().rating("dislike").user("user-123").build()
        assert body.rating == "dislike"

    def test_submit_feedback_response_inheritance(self):
        """Test SubmitFeedbackResponse inherits from BaseResponse"""
        response = SubmitFeedbackResponse()
        assert isinstance(response, BaseResponse)
        assert hasattr(response, "success")
        assert hasattr(response, "code")
        assert hasattr(response, "msg")
        assert response.result == "success"


class TestGetFeedbacksModels:
    def test_get_feedbacks_request_builder(self):
        """Test GetFeedbacksRequest builder pattern"""
        request = GetFeedbacksRequest.builder().page(1).limit(20).build()

        assert request.http_method == HttpMethod.GET
        assert request.uri == "/v1/app/feedbacks"
        assert ("page", "1") in request.queries
        assert ("limit", "20") in request.queries

    def test_get_feedbacks_request_optional_params(self):
        """Test GetFeedbacksRequest with optional parameters"""
        request = GetFeedbacksRequest.builder().build()

        assert request.http_method == HttpMethod.GET
        assert request.uri == "/v1/app/feedbacks"
        # Optional parameters should not be in queries if not set
        query_keys = [key for key, _ in request.queries]
        assert "page" not in query_keys
        assert "limit" not in query_keys

    def test_get_feedbacks_response_inheritance(self):
        """Test GetFeedbacksResponse inherits from BaseResponse"""
        response = GetFeedbacksResponse()
        assert isinstance(response, BaseResponse)
        assert hasattr(response, "success")
        assert hasattr(response, "code")
        assert hasattr(response, "msg")
        assert hasattr(response, "data")
        assert response.data == []

    def test_get_feedbacks_response_with_data(self):
        """Test GetFeedbacksResponse with feedback data"""
        feedback = FeedbackInfo.builder().id("feedback-123").rating("like").content("Good response").build()
        response = GetFeedbacksResponse(data=[feedback])

        assert len(response.data) == 1
        assert response.data[0].id == "feedback-123"
        assert response.data[0].rating == "like"
        assert response.data[0].content == "Good response"
