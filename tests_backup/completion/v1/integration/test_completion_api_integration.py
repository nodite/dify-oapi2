from __future__ import annotations

from dify_oapi.api.completion.v1.model.completion.send_message_request import SendMessageRequest
from dify_oapi.api.completion.v1.model.completion.send_message_request_body import SendMessageRequestBody
from dify_oapi.api.completion.v1.model.completion.stop_response_request import StopResponseRequest
from dify_oapi.api.completion.v1.model.completion.stop_response_request_body import StopResponseRequestBody
from dify_oapi.api.completion.v1.model.feedback.message_feedback_request import MessageFeedbackRequest
from dify_oapi.api.completion.v1.model.feedback.message_feedback_request_body import MessageFeedbackRequestBody
from dify_oapi.api.completion.v1.model.file.upload_file_request import UploadFileRequest
from dify_oapi.api.completion.v1.model.file.upload_file_request_body import UploadFileRequestBody
from dify_oapi.api.completion.v1.model.info.get_info_request import GetInfoRequest
from dify_oapi.api.completion.v1.version import V1
from dify_oapi.core.model.config import Config
from dify_oapi.core.model.request_option import RequestOption


class TestCompletionAPIIntegration:
    """Integration tests for Completion API components."""

    def test_request_building(self) -> None:
        """Test that all request models can be built correctly."""
        # Test SendMessage request building
        send_body = SendMessageRequestBody.builder().user("test-user").build()
        send_request = SendMessageRequest.builder().request_body(send_body).build()

        assert send_request.request_body is not None
        assert send_request.request_body.user == "test-user"

        # Test StopResponse request building
        stop_body = StopResponseRequestBody.builder().user("test-user").build()
        stop_request = StopResponseRequest.builder().task_id("task-123").request_body(stop_body).build()

        assert stop_request.task_id == "task-123"
        assert stop_request.request_body is not None
        assert stop_request.request_body.user == "test-user"

        # Test UploadFile request building
        upload_body = UploadFileRequestBody.builder().user("test-user").build()
        upload_request = UploadFileRequest.builder().request_body(upload_body).build()

        assert upload_request.request_body is not None
        assert upload_request.request_body.user == "test-user"

        # Test MessageFeedback request building
        feedback_body = MessageFeedbackRequestBody.builder().rating("like").user("test-user").build()
        feedback_request = MessageFeedbackRequest.builder().message_id("msg-123").request_body(feedback_body).build()

        assert feedback_request.message_id == "msg-123"
        assert feedback_request.request_body is not None
        assert feedback_request.request_body.rating == "like"

        # Test GetInfo request building
        info_request = GetInfoRequest.builder().build()

        assert info_request.http_method is not None
        assert info_request.http_method.value == 1  # HttpMethod.GET

    def test_v1_resource_integration(self) -> None:
        """Test V1 resource integration with config."""
        config = Config()
        config.domain = "https://api.dify.ai"
        v1 = V1(config)

        # Verify all resources are accessible
        assert v1.completion is not None
        assert v1.file is not None
        assert v1.feedback is not None
        assert v1.audio is not None
        assert v1.info is not None
        assert v1.annotation is not None

    def test_request_option_integration(self) -> None:
        """Test RequestOption integration with requests."""
        request_option = RequestOption.builder().api_key("test-key").build()

        # Test with SendMessage request
        send_body = SendMessageRequestBody.builder().user("user").build()
        send_request = SendMessageRequest.builder().request_body(send_body).build()

        # Verify request option can be used with request
        assert request_option.api_key == "test-key"
        assert send_request.request_body is not None

    def test_builder_pattern_consistency(self) -> None:
        """Test that builder patterns are consistent across all models."""
        # Test that all request bodies can be built
        send_body = SendMessageRequestBody.builder().build()
        stop_body = StopResponseRequestBody.builder().build()
        upload_body = UploadFileRequestBody.builder().build()
        feedback_body = MessageFeedbackRequestBody.builder().build()

        # Test that all requests can be built
        send_request = SendMessageRequest.builder().build()
        stop_request = StopResponseRequest.builder().build()
        upload_request = UploadFileRequest.builder().build()
        feedback_request = MessageFeedbackRequest.builder().build()
        info_request = GetInfoRequest.builder().build()

        # Verify all builders return valid objects
        assert send_body is not None
        assert stop_body is not None
        assert upload_body is not None
        assert feedback_body is not None
        assert send_request is not None
        assert stop_request is not None
        assert upload_request is not None
        assert feedback_request is not None
        assert info_request is not None
