from dify_oapi.api.chatflow.v1.model.feedback_info import FeedbackInfo
from dify_oapi.api.chatflow.v1.model.get_app_feedbacks_request import GetAppFeedbacksRequest
from dify_oapi.api.chatflow.v1.model.get_app_feedbacks_response import GetAppFeedbacksResponse
from dify_oapi.api.chatflow.v1.model.message_feedback_request import MessageFeedbackRequest
from dify_oapi.api.chatflow.v1.model.message_feedback_request_body import MessageFeedbackRequestBody
from dify_oapi.api.chatflow.v1.model.message_feedback_response import MessageFeedbackResponse
from dify_oapi.core.enum import HttpMethod
from dify_oapi.core.model.base_response import BaseResponse


class TestMessageFeedbackModels:
    """Test class for Message Feedback API models."""

    def test_request_builder(self):
        """Test MessageFeedbackRequest builder pattern."""
        request = (
            MessageFeedbackRequest.builder()
            .message_id("msg_123")
            .request_body(
                MessageFeedbackRequestBody.builder().rating("like").user("test_user").content("Great response!").build()
            )
            .build()
        )

        assert request.message_id == "msg_123"
        assert request.paths["message_id"] == "msg_123"
        assert request.http_method == HttpMethod.POST
        assert request.uri == "/v1/messages/:message_id/feedbacks"
        assert request.request_body is not None
        assert request.body is not None

    def test_request_validation(self):
        """Test MessageFeedbackRequest validation."""
        request = MessageFeedbackRequest.builder().build()

        # Test that request can be built without required fields
        assert request.message_id is None
        assert request.request_body is None

    def test_request_body_builder(self):
        """Test MessageFeedbackRequestBody builder pattern."""
        request_body = (
            MessageFeedbackRequestBody.builder().rating("dislike").user("test_user").content("Could be better").build()
        )

        assert request_body.rating == "dislike"
        assert request_body.user == "test_user"
        assert request_body.content == "Could be better"

    def test_request_body_validation(self):
        """Test MessageFeedbackRequestBody validation."""
        # Test with valid rating
        request_body = MessageFeedbackRequestBody.builder().rating("like").build()
        assert request_body.rating == "like"

        # Test with null rating
        request_body = MessageFeedbackRequestBody.builder().build()
        assert request_body.rating is None

    def test_request_body_optional_fields(self):
        """Test MessageFeedbackRequestBody optional fields."""
        # Test with only required user field
        request_body = MessageFeedbackRequestBody.builder().user("test_user").build()
        assert request_body.user == "test_user"
        assert request_body.rating is None
        assert request_body.content is None

        # Test with rating and content but no user
        request_body = MessageFeedbackRequestBody.builder().rating("like").content("Good response").build()
        assert request_body.rating == "like"
        assert request_body.content == "Good response"
        assert request_body.user is None

    def test_response_inheritance(self):
        """Test MessageFeedbackResponse inherits from BaseResponse."""
        response = MessageFeedbackResponse.builder().result("success").build()

        assert isinstance(response, BaseResponse)
        assert response.result == "success"
        assert hasattr(response, "success")
        assert hasattr(response, "code")
        assert hasattr(response, "msg")

    def test_response_data_access(self):
        """Test MessageFeedbackResponse data access."""
        response = MessageFeedbackResponse()
        response.result = "success"

        assert response.result == "success"

    def test_response_builder(self):
        """Test MessageFeedbackResponse builder pattern."""
        response = MessageFeedbackResponse.builder().result("success").build()

        assert response.result == "success"


class TestGetAppFeedbacksModels:
    """Test class for Get App Feedbacks API models."""

    def test_request_builder(self):
        """Test GetAppFeedbacksRequest builder pattern."""
        request = GetAppFeedbacksRequest.builder().page(1).limit(20).build()

        assert request.http_method == HttpMethod.GET
        assert request.uri == "/v1/app/feedbacks"
        assert "page" in request.query
        assert "limit" in request.query
        assert request.query["page"] == "1"
        assert request.query["limit"] == "20"

    def test_request_validation(self):
        """Test GetAppFeedbacksRequest validation."""
        request = GetAppFeedbacksRequest.builder().build()

        # Test that request can be built without optional parameters
        assert request.http_method == HttpMethod.GET
        assert request.uri == "/v1/app/feedbacks"

    def test_request_pagination_parameters(self):
        """Test GetAppFeedbacksRequest pagination parameters."""
        request = GetAppFeedbacksRequest.builder().page(2).limit(50).build()

        assert request.query["page"] == "2"
        assert request.query["limit"] == "50"

    def test_request_optional_parameters(self):
        """Test GetAppFeedbacksRequest optional parameters."""
        # Test with only page
        request = GetAppFeedbacksRequest.builder().page(3).build()
        assert request.query["page"] == "3"
        assert "limit" not in request.query

        # Test with only limit
        request = GetAppFeedbacksRequest.builder().limit(10).build()
        assert request.query["limit"] == "10"
        assert "page" not in request.query

    def test_response_inheritance(self):
        """Test GetAppFeedbacksResponse inherits from BaseResponse."""
        feedback_info = FeedbackInfo.builder().id("feedback_123").rating("like").build()
        response = GetAppFeedbacksResponse.builder().data([feedback_info]).build()

        assert isinstance(response, BaseResponse)
        assert response.data is not None
        assert len(response.data) == 1
        assert response.data[0].id == "feedback_123"
        assert hasattr(response, "success")
        assert hasattr(response, "code")
        assert hasattr(response, "msg")

    def test_response_data_access(self):
        """Test GetAppFeedbacksResponse data access."""
        feedback_info = FeedbackInfo.builder().id("feedback_456").rating("dislike").build()
        response = GetAppFeedbacksResponse()
        response.data = [feedback_info]

        assert response.data is not None
        assert len(response.data) == 1
        assert response.data[0].id == "feedback_456"

    def test_response_empty_data(self):
        """Test GetAppFeedbacksResponse with empty data."""
        response = GetAppFeedbacksResponse.builder().data([]).build()

        assert response.data is not None
        assert len(response.data) == 0

    def test_response_builder(self):
        """Test GetAppFeedbacksResponse builder pattern."""
        feedback_list = [
            FeedbackInfo.builder().id("feedback_1").rating("like").build(),
            FeedbackInfo.builder().id("feedback_2").rating("dislike").build(),
        ]
        response = GetAppFeedbacksResponse.builder().data(feedback_list).build()

        assert response.data is not None
        assert len(response.data) == 2
        assert response.data[0].id == "feedback_1"
        assert response.data[1].id == "feedback_2"

    def test_response_with_feedback_details(self):
        """Test GetAppFeedbacksResponse with detailed feedback information."""
        feedback_info = (
            FeedbackInfo.builder()
            .id("feedback_detailed")
            .app_id("app_123")
            .conversation_id("conv_456")
            .message_id("msg_789")
            .rating("like")
            .content("Excellent response quality")
            .from_source("api")
            .from_end_user_id("user_123")
            .created_at(1234567890)
            .updated_at(1234567900)
            .build()
        )

        response = GetAppFeedbacksResponse.builder().data([feedback_info]).build()

        assert response.data is not None
        assert len(response.data) == 1
        feedback = response.data[0]
        assert feedback.id == "feedback_detailed"
        assert feedback.app_id == "app_123"
        assert feedback.conversation_id == "conv_456"
        assert feedback.message_id == "msg_789"
        assert feedback.rating == "like"
        assert feedback.content == "Excellent response quality"
        assert feedback.from_source == "api"
        assert feedback.from_end_user_id == "user_123"
        assert feedback.created_at == 1234567890
        assert feedback.updated_at == 1234567900
