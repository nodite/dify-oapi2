from __future__ import annotations

from dify_oapi.api.completion.v1.model.completion.completion_inputs import CompletionInputs
from dify_oapi.api.completion.v1.model.completion.send_message_request import SendMessageRequest
from dify_oapi.api.completion.v1.model.completion.send_message_request_body import SendMessageRequestBody
from dify_oapi.api.completion.v1.model.completion.send_message_response import SendMessageResponse
from dify_oapi.api.completion.v1.model.completion.stop_response_request import StopResponseRequest
from dify_oapi.api.completion.v1.model.completion.stop_response_request_body import StopResponseRequestBody
from dify_oapi.api.completion.v1.model.completion.stop_response_response import StopResponseResponse
from dify_oapi.core.enum import HttpMethod
from dify_oapi.core.model.base_response import BaseResponse


class TestSendMessageModels:
    """Test SendMessage API models."""

    def test_request_builder(self) -> None:
        """Test SendMessageRequest builder pattern."""
        inputs = CompletionInputs.builder().query("test query").build()
        request_body = SendMessageRequestBody.builder().inputs(inputs).user("test-user").build()

        request = SendMessageRequest.builder().request_body(request_body).build()

        assert request.http_method == HttpMethod.POST
        assert request.uri == "/v1/completion-messages"
        assert request.request_body == request_body
        assert request.body is not None

    def test_request_validation(self) -> None:
        """Test SendMessageRequest validation."""
        request = SendMessageRequest.builder().build()

        assert request.http_method == HttpMethod.POST
        assert request.uri == "/v1/completion-messages"

    def test_request_body_builder(self) -> None:
        """Test SendMessageRequestBody builder pattern."""
        inputs = CompletionInputs.builder().query("What is AI?").build()

        request_body = (
            SendMessageRequestBody.builder().inputs(inputs).response_mode("blocking").user("user-123").build()
        )

        assert request_body.inputs == inputs
        assert request_body.inputs.query == "What is AI?"
        assert request_body.response_mode == "blocking"
        assert request_body.user == "user-123"

    def test_request_body_validation(self) -> None:
        """Test SendMessageRequestBody validation."""
        request_body = SendMessageRequestBody.builder().build()

        assert request_body.inputs is None
        assert request_body.response_mode is None
        assert request_body.user is None

    def test_response_inheritance(self) -> None:
        """Test SendMessageResponse inherits from BaseResponse."""
        response = SendMessageResponse()

        assert isinstance(response, BaseResponse)
        assert hasattr(response, "success")
        assert hasattr(response, "code")
        assert hasattr(response, "msg")
        assert hasattr(response, "raw")

    def test_response_data_access(self) -> None:
        """Test SendMessageResponse data access."""
        response = SendMessageResponse(
            message_id="test-message-id", mode="completion", answer="Test answer", created_at=1705395332
        )

        assert response.message_id == "test-message-id"
        assert response.mode == "completion"
        assert response.answer == "Test answer"
        assert response.created_at == 1705395332


class TestStopResponseModels:
    """Test StopResponse API models."""

    def test_request_builder(self) -> None:
        """Test StopResponseRequest builder pattern."""
        request_body = StopResponseRequestBody.builder().user("test-user").build()

        request = StopResponseRequest.builder().task_id("task-123").request_body(request_body).build()

        assert request.http_method == HttpMethod.POST
        assert request.uri == "/v1/completion-messages/:task_id/stop"
        assert request.task_id == "task-123"
        assert request.paths["task_id"] == "task-123"
        assert request.request_body == request_body

    def test_request_validation(self) -> None:
        """Test StopResponseRequest validation."""
        request = StopResponseRequest.builder().task_id("task-456").build()

        assert request.task_id == "task-456"
        assert "task_id" in request.paths
        assert request.paths["task_id"] == "task-456"

    def test_request_body_builder(self) -> None:
        """Test StopResponseRequestBody builder pattern."""
        request_body = StopResponseRequestBody.builder().user("user-123").build()

        assert request_body.user == "user-123"

    def test_request_body_validation(self) -> None:
        """Test StopResponseRequestBody validation."""
        request_body = StopResponseRequestBody.builder().build()

        assert request_body.user is None

    def test_response_inheritance(self) -> None:
        """Test StopResponseResponse inherits from BaseResponse."""
        response = StopResponseResponse()

        assert isinstance(response, BaseResponse)
        assert hasattr(response, "success")
        assert hasattr(response, "code")
        assert hasattr(response, "msg")
        assert hasattr(response, "raw")

    def test_response_data_access(self) -> None:
        """Test StopResponseResponse data access."""
        response = StopResponseResponse(result="success")

        assert response.result == "success"
