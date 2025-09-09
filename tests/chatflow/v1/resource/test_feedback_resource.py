from unittest.mock import patch

import pytest

from dify_oapi.api.chatflow.v1.model.feedback_info import FeedbackInfo
from dify_oapi.api.chatflow.v1.model.get_app_feedbacks_request import GetAppFeedbacksRequest
from dify_oapi.api.chatflow.v1.model.get_app_feedbacks_response import GetAppFeedbacksResponse
from dify_oapi.api.chatflow.v1.model.message_feedback_request import MessageFeedbackRequest
from dify_oapi.api.chatflow.v1.model.message_feedback_request_body import MessageFeedbackRequestBody
from dify_oapi.api.chatflow.v1.model.message_feedback_response import MessageFeedbackResponse
from dify_oapi.api.chatflow.v1.resource.feedback import Feedback
from dify_oapi.core.model.config import Config
from dify_oapi.core.model.request_option import RequestOption


class TestFeedbackResource:
    """Test class for Feedback resource."""

    @pytest.fixture
    def config(self):
        """Create test config."""
        config = Config()
        config.domain = "https://api.dify.ai"
        return config

    @pytest.fixture
    def request_option(self):
        """Create test request option."""
        return RequestOption.builder().api_key("test_api_key").build()

    @pytest.fixture
    def feedback_resource(self, config):
        """Create Feedback resource instance."""
        return Feedback(config)

    @pytest.fixture
    def message_feedback_request(self):
        """Create test message feedback request."""
        request_body = (
            MessageFeedbackRequestBody.builder().rating("like").user("test_user").content("Great response!").build()
        )
        return MessageFeedbackRequest.builder().message_id("msg_123").request_body(request_body).build()

    @pytest.fixture
    def get_app_feedbacks_request(self):
        """Create test get app feedbacks request."""
        return GetAppFeedbacksRequest.builder().page(1).limit(20).build()

    @pytest.fixture
    def message_feedback_response(self):
        """Create mock message feedback response."""
        return MessageFeedbackResponse(
            result="success",
            success=True,
            code="200",
            msg="Feedback submitted successfully",
        )

    @pytest.fixture
    def get_app_feedbacks_response(self):
        """Create mock get app feedbacks response."""
        feedback_items = [
            FeedbackInfo(
                id="feedback_1",
                app_id="app_123",
                conversation_id="conv_123",
                message_id="msg_123",
                rating="like",
                content="Great response!",
                from_source="api",
                from_end_user_id="user_123",
                from_account_id="account_123",
                created_at="2024-01-01T00:00:00Z",
                updated_at="2024-01-01T00:00:00Z",
            ),
            FeedbackInfo(
                id="feedback_2",
                app_id="app_123",
                conversation_id="conv_124",
                message_id="msg_124",
                rating="dislike",
                content="Could be better",
                from_source="api",
                from_end_user_id="user_124",
                from_account_id="account_123",
                created_at="2024-01-01T01:00:00Z",
                updated_at="2024-01-01T01:00:00Z",
            ),
        ]
        return GetAppFeedbacksResponse(
            data=feedback_items,
            success=True,
            code="200",
            msg="Feedbacks retrieved successfully",
        )

    def test_feedback_resource_initialization(self, config):
        """Test Feedback resource initialization."""
        feedback_resource = Feedback(config)
        assert feedback_resource.config == config

    @patch("dify_oapi.core.http.transport.Transport.execute")
    def test_message_feedback_sync(
        self, mock_execute, feedback_resource, message_feedback_request, request_option, message_feedback_response
    ):
        """Test sync message feedback."""
        # Setup mock
        mock_execute.return_value = message_feedback_response

        # Execute message feedback
        response = feedback_resource.message(message_feedback_request, request_option)

        # Verify mock was called correctly
        mock_execute.assert_called_once_with(
            feedback_resource.config,
            message_feedback_request,
            unmarshal_as=MessageFeedbackResponse,
            option=request_option,
        )

        # Verify response
        assert response == message_feedback_response
        assert response.success is True
        assert response.result == "success"

    @patch("dify_oapi.core.http.transport.ATransport.aexecute")
    @pytest.mark.asyncio
    async def test_message_feedback_async(
        self, mock_aexecute, feedback_resource, message_feedback_request, request_option, message_feedback_response
    ):
        """Test async message feedback."""
        # Setup mock
        mock_aexecute.return_value = message_feedback_response

        # Execute async message feedback
        response = await feedback_resource.amessage(message_feedback_request, request_option)

        # Verify mock was called correctly
        mock_aexecute.assert_called_once_with(
            feedback_resource.config,
            message_feedback_request,
            unmarshal_as=MessageFeedbackResponse,
            option=request_option,
        )

        # Verify response
        assert response == message_feedback_response
        assert response.success is True
        assert response.result == "success"

    @patch("dify_oapi.core.http.transport.Transport.execute")
    def test_get_app_feedbacks_sync(
        self, mock_execute, feedback_resource, get_app_feedbacks_request, request_option, get_app_feedbacks_response
    ):
        """Test sync get app feedbacks."""
        # Setup mock
        mock_execute.return_value = get_app_feedbacks_response

        # Execute get app feedbacks
        response = feedback_resource.list(get_app_feedbacks_request, request_option)

        # Verify mock was called correctly
        mock_execute.assert_called_once_with(
            feedback_resource.config,
            get_app_feedbacks_request,
            unmarshal_as=GetAppFeedbacksResponse,
            option=request_option,
        )

        # Verify response
        assert response == get_app_feedbacks_response
        assert response.success is True
        assert len(response.data) == 2
        assert response.data[0].rating == "like"
        assert response.data[1].rating == "dislike"

    @patch("dify_oapi.core.http.transport.ATransport.aexecute")
    @pytest.mark.asyncio
    async def test_get_app_feedbacks_async(
        self, mock_aexecute, feedback_resource, get_app_feedbacks_request, request_option, get_app_feedbacks_response
    ):
        """Test async get app feedbacks."""
        # Setup mock
        mock_aexecute.return_value = get_app_feedbacks_response

        # Execute async get app feedbacks
        response = await feedback_resource.alist(get_app_feedbacks_request, request_option)

        # Verify mock was called correctly
        mock_aexecute.assert_called_once_with(
            feedback_resource.config,
            get_app_feedbacks_request,
            unmarshal_as=GetAppFeedbacksResponse,
            option=request_option,
        )

        # Verify response
        assert response == get_app_feedbacks_response
        assert response.success is True
        assert len(response.data) == 2

    @patch("dify_oapi.core.http.transport.Transport.execute")
    def test_message_feedback_different_ratings(self, mock_execute, feedback_resource, request_option):
        """Test message feedback with different rating types."""
        ratings = ["like", "dislike", None]

        for rating in ratings:
            # Create request with specific rating
            request_body = (
                MessageFeedbackRequestBody.builder()
                .rating(rating)
                .user("test_user")
                .content(f"Feedback with {rating} rating")
                .build()
            )
            request = MessageFeedbackRequest.builder().message_id("msg_123").request_body(request_body).build()

            # Create mock response
            mock_response = MessageFeedbackResponse(
                result="success",
                success=True,
                code="200",
                msg=f"Feedback with {rating} submitted",
            )
            mock_execute.return_value = mock_response

            # Execute feedback
            response = feedback_resource.message(request, request_option)

            # Verify response
            assert response.success is True
            assert response.result == "success"

    @patch("dify_oapi.core.http.transport.Transport.execute")
    def test_message_feedback_without_content(self, mock_execute, feedback_resource, request_option):
        """Test message feedback without content."""
        # Create request without content
        request_body = MessageFeedbackRequestBody.builder().rating("like").user("test_user").build()
        request = MessageFeedbackRequest.builder().message_id("msg_123").request_body(request_body).build()

        mock_response = MessageFeedbackResponse(
            result="success",
            success=True,
            code="200",
            msg="Feedback submitted successfully",
        )
        mock_execute.return_value = mock_response

        # Execute feedback
        response = feedback_resource.message(request, request_option)

        # Verify response
        assert response.success is True
        assert response.result == "success"

    @patch("dify_oapi.core.http.transport.Transport.execute")
    def test_get_app_feedbacks_pagination(self, mock_execute, feedback_resource, request_option):
        """Test get app feedbacks with different pagination parameters."""
        pagination_params = [
            (1, 10),
            (2, 20),
            (1, 50),
            (None, None),  # No pagination
        ]

        for page, limit in pagination_params:
            # Create request with pagination
            builder = GetAppFeedbacksRequest.builder()
            if page is not None:
                builder.page(page)
            if limit is not None:
                builder.limit(limit)
            request = builder.build()

            # Create mock response
            mock_response = GetAppFeedbacksResponse(
                data=[],
                success=True,
                code="200",
                msg=f"Page {page}, Limit {limit}",
            )
            mock_execute.return_value = mock_response

            # Execute request
            response = feedback_resource.list(request, request_option)

            # Verify response
            assert response.success is True
            assert response.data == []

    @patch("dify_oapi.core.http.transport.Transport.execute")
    def test_message_feedback_error_handling(
        self, mock_execute, feedback_resource, message_feedback_request, request_option
    ):
        """Test message feedback error handling."""
        # Create error response
        error_response = MessageFeedbackResponse(
            success=False,
            code="400",
            msg="Invalid message ID",
        )
        mock_execute.return_value = error_response

        # Execute feedback
        response = feedback_resource.message(message_feedback_request, request_option)

        # Verify error response
        assert response.success is False
        assert response.code == "400"
        assert response.msg == "Invalid message ID"

    @patch("dify_oapi.core.http.transport.Transport.execute")
    def test_get_app_feedbacks_error_handling(
        self, mock_execute, feedback_resource, get_app_feedbacks_request, request_option
    ):
        """Test get app feedbacks error handling."""
        # Create error response
        error_response = GetAppFeedbacksResponse(
            success=False,
            code="403",
            msg="Insufficient permissions",
        )
        mock_execute.return_value = error_response

        # Execute request
        response = feedback_resource.list(get_app_feedbacks_request, request_option)

        # Verify error response
        assert response.success is False
        assert response.code == "403"
        assert response.msg == "Insufficient permissions"

    @patch("dify_oapi.core.http.transport.ATransport.aexecute")
    @pytest.mark.asyncio
    async def test_message_feedback_async_error_handling(
        self, mock_aexecute, feedback_resource, message_feedback_request, request_option
    ):
        """Test async message feedback error handling."""
        # Create error response
        error_response = MessageFeedbackResponse(
            success=False,
            code="404",
            msg="Message not found",
        )
        mock_aexecute.return_value = error_response

        # Execute async feedback
        response = await feedback_resource.amessage(message_feedback_request, request_option)

        # Verify error response
        assert response.success is False
        assert response.code == "404"
        assert response.msg == "Message not found"

    @patch("dify_oapi.core.http.transport.ATransport.aexecute")
    @pytest.mark.asyncio
    async def test_get_app_feedbacks_async_error_handling(
        self, mock_aexecute, feedback_resource, get_app_feedbacks_request, request_option
    ):
        """Test async get app feedbacks error handling."""
        # Create error response
        error_response = GetAppFeedbacksResponse(
            success=False,
            code="500",
            msg="Internal server error",
        )
        mock_aexecute.return_value = error_response

        # Execute async request
        response = await feedback_resource.alist(get_app_feedbacks_request, request_option)

        # Verify error response
        assert response.success is False
        assert response.code == "500"
        assert response.msg == "Internal server error"

    def test_feedback_method_signatures(self, feedback_resource):
        """Test feedback method signatures."""
        # Verify sync methods exist
        assert hasattr(feedback_resource, "message")
        assert callable(feedback_resource.message)
        assert hasattr(feedback_resource, "list")
        assert callable(feedback_resource.list)

        # Verify async methods exist
        assert hasattr(feedback_resource, "amessage")
        assert callable(feedback_resource.amessage)
        assert hasattr(feedback_resource, "alist")
        assert callable(feedback_resource.alist)

    @patch("dify_oapi.core.http.transport.Transport.execute")
    def test_message_feedback_long_content(self, mock_execute, feedback_resource, request_option):
        """Test message feedback with long content."""
        # Create request with long content
        long_content = "This is a very long feedback content. " * 100  # ~3700 characters
        request_body = (
            MessageFeedbackRequestBody.builder().rating("like").user("test_user").content(long_content).build()
        )
        request = MessageFeedbackRequest.builder().message_id("msg_123").request_body(request_body).build()

        mock_response = MessageFeedbackResponse(
            result="success",
            success=True,
            code="200",
            msg="Long feedback submitted successfully",
        )
        mock_execute.return_value = mock_response

        # Execute feedback
        response = feedback_resource.message(request, request_option)

        # Verify response
        assert response.success is True
        assert response.result == "success"

    @patch("dify_oapi.core.http.transport.Transport.execute")
    def test_get_app_feedbacks_empty_response(
        self, mock_execute, feedback_resource, get_app_feedbacks_request, request_option
    ):
        """Test get app feedbacks with empty response."""
        # Create empty response
        empty_response = GetAppFeedbacksResponse(
            data=[],
            success=True,
            code="200",
            msg="No feedbacks found",
        )
        mock_execute.return_value = empty_response

        # Execute request
        response = feedback_resource.list(get_app_feedbacks_request, request_option)

        # Verify empty response
        assert response.success is True
        assert response.data == []
        assert len(response.data) == 0

    @patch("dify_oapi.core.http.transport.Transport.execute")
    def test_message_feedback_special_characters(self, mock_execute, feedback_resource, request_option):
        """Test message feedback with special characters in content."""
        # Create request with special characters
        special_content = "Great! 👍 This response is 很好 and très bien! 🎉"
        request_body = (
            MessageFeedbackRequestBody.builder().rating("like").user("test_user").content(special_content).build()
        )
        request = MessageFeedbackRequest.builder().message_id("msg_123").request_body(request_body).build()

        mock_response = MessageFeedbackResponse(
            result="success",
            success=True,
            code="200",
            msg="Special character feedback submitted",
        )
        mock_execute.return_value = mock_response

        # Execute feedback
        response = feedback_resource.message(request, request_option)

        # Verify response
        assert response.success is True
        assert response.result == "success"

    @patch("dify_oapi.core.http.transport.Transport.execute")
    def test_get_app_feedbacks_large_dataset(self, mock_execute, feedback_resource, request_option):
        """Test get app feedbacks with large dataset."""
        # Create request for large dataset
        request = (
            GetAppFeedbacksRequest.builder()
            .page(1)
            .limit(100)  # Large limit
            .build()
        )

        # Create large feedback list
        large_feedback_list = []
        for i in range(100):
            feedback = FeedbackInfo(
                id=f"feedback_{i}",
                app_id="app_123",
                conversation_id=f"conv_{i}",
                message_id=f"msg_{i}",
                rating="like" if i % 2 == 0 else "dislike",
                content=f"Feedback content {i}",
                from_source="api",
                from_end_user_id=f"user_{i}",
                from_account_id="account_123",
                created_at=f"2024-01-01T{i:02d}:00:00Z",
                updated_at=f"2024-01-01T{i:02d}:00:00Z",
            )
            large_feedback_list.append(feedback)

        large_response = GetAppFeedbacksResponse(
            data=large_feedback_list,
            success=True,
            code="200",
            msg="Large dataset retrieved",
        )
        mock_execute.return_value = large_response

        # Execute request
        response = feedback_resource.list(request, request_option)

        # Verify large response
        assert response.success is True
        assert len(response.data) == 100
        assert response.data[0].id == "feedback_0"
        assert response.data[99].id == "feedback_99"
