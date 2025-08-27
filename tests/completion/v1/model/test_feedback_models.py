from __future__ import annotations

from dify_oapi.api.completion.v1.model.feedback.get_feedbacks_request import GetFeedbacksRequest
from dify_oapi.api.completion.v1.model.feedback.get_feedbacks_response import GetFeedbacksResponse
from dify_oapi.api.completion.v1.model.feedback.message_feedback_request import MessageFeedbackRequest
from dify_oapi.api.completion.v1.model.feedback.message_feedback_request_body import MessageFeedbackRequestBody
from dify_oapi.api.completion.v1.model.feedback.message_feedback_response import MessageFeedbackResponse
from dify_oapi.core.enum import HttpMethod
from dify_oapi.core.model.base_response import BaseResponse


class TestMessageFeedbackModels:
    """Test MessageFeedback API models."""

    def test_request_builder(self) -> None:
        """Test MessageFeedbackRequest builder pattern."""
        request_body = MessageFeedbackRequestBody.builder().rating("like").user("test-user").build()

        request = MessageFeedbackRequest.builder().message_id("message-123").request_body(request_body).build()

        assert request.http_method == HttpMethod.POST
        assert request.uri == "/v1/messages/:message_id/feedbacks"
        assert request.message_id == "message-123"
        assert request.paths["message_id"] == "message-123"
        assert request.request_body == request_body

    def test_request_validation(self) -> None:
        """Test MessageFeedbackRequest validation."""
        request = MessageFeedbackRequest.builder().message_id("message-456").build()

        assert request.message_id == "message-456"
        assert "message_id" in request.paths
        assert request.paths["message_id"] == "message-456"

    def test_request_body_builder(self) -> None:
        """Test MessageFeedbackRequestBody builder pattern."""
        request_body = (
            MessageFeedbackRequestBody.builder().rating("like").user("user-123").content("Excellent response!").build()
        )

        assert request_body.rating == "like"
        assert request_body.user == "user-123"
        assert request_body.content == "Excellent response!"

    def test_request_body_validation(self) -> None:
        """Test MessageFeedbackRequestBody validation."""
        request_body = MessageFeedbackRequestBody.builder().build()

        assert request_body.rating is None
        assert request_body.user is None
        assert request_body.content is None

    def test_response_inheritance(self) -> None:
        """Test MessageFeedbackResponse inherits from BaseResponse."""
        response = MessageFeedbackResponse()

        assert isinstance(response, BaseResponse)
        assert hasattr(response, "success")
        assert hasattr(response, "code")
        assert hasattr(response, "msg")
        assert hasattr(response, "raw")

    def test_response_data_access(self) -> None:
        """Test MessageFeedbackResponse data access."""
        response = MessageFeedbackResponse(result="success")

        assert response.result == "success"


class TestGetFeedbacksModels:
    """Test GetFeedbacks API models."""

    def test_request_builder(self) -> None:
        """Test GetFeedbacksRequest builder pattern."""
        request = GetFeedbacksRequest.builder().page("1").limit("20").build()

        assert request.http_method == HttpMethod.GET
        assert request.uri == "/v1/app/feedbacks"
        assert ("page", "1") in request.queries
        assert ("limit", "20") in request.queries
        assert len(request.queries) == 2

    def test_request_validation(self) -> None:
        """Test GetFeedbacksRequest validation."""
        # Test with no parameters
        request_empty = GetFeedbacksRequest.builder().build()
        assert len(request_empty.queries) == 0

        # Test with only page
        request_page = GetFeedbacksRequest.builder().page("2").build()
        assert ("page", "2") in request_page.queries
        assert len(request_page.queries) == 1

    def test_response_inheritance(self) -> None:
        """Test GetFeedbacksResponse inherits from BaseResponse."""
        response = GetFeedbacksResponse()

        assert isinstance(response, BaseResponse)
        assert hasattr(response, "success")
        assert hasattr(response, "code")
        assert hasattr(response, "msg")
        assert hasattr(response, "raw")

    def test_response_data_access(self) -> None:
        """Test GetFeedbacksResponse data access."""
        response = GetFeedbacksResponse(data=[])

        assert response.data == []
        assert len(response.data) == 0
