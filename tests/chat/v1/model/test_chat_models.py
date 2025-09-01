"""Tests for Chat Messages API models."""

import pytest
from pydantic import ValidationError

from dify_oapi.api.chat.v1.model.chat_file import ChatFile
from dify_oapi.api.chat.v1.model.chat_request import ChatRequest
from dify_oapi.api.chat.v1.model.chat_request_body import ChatRequestBody
from dify_oapi.api.chat.v1.model.chat_response import ChatResponse
from dify_oapi.api.chat.v1.model.get_suggested_questions_request import GetSuggestedQuestionsRequest
from dify_oapi.api.chat.v1.model.get_suggested_questions_response import GetSuggestedQuestionsResponse
from dify_oapi.api.chat.v1.model.stop_chat_request import StopChatRequest
from dify_oapi.api.chat.v1.model.stop_chat_request_body import StopChatRequestBody
from dify_oapi.api.chat.v1.model.stop_chat_response import StopChatResponse
from dify_oapi.core.enum import HttpMethod
from dify_oapi.core.model.base_response import BaseResponse


class TestSendChatMessageModels:
    """Test Send Chat Message API models."""

    def test_chat_request_builder(self):
        """Test ChatRequest builder pattern."""
        request_body = ChatRequestBody.builder().query("Hello").user("user-123").build()
        request = ChatRequest.builder().request_body(request_body).build()

        assert request.http_method == HttpMethod.POST
        assert request.uri == "/v1/chat-messages"
        assert request.request_body.query == "Hello"
        assert request.request_body.user == "user-123"

    def test_chat_request_body_builder(self):
        """Test ChatRequestBody builder pattern."""
        body = (
            ChatRequestBody.builder()
            .query("Hello")
            .inputs({"key": "value"})
            .response_mode("blocking")
            .user("user-123")
            .conversation_id("conv-123")
            .auto_generate_name(True)
            .build()
        )

        assert body.query == "Hello"
        assert body.inputs == {"key": "value"}
        assert body.response_mode == "blocking"
        assert body.user == "user-123"
        assert body.conversation_id == "conv-123"
        assert body.auto_generate_name is True

    def test_chat_request_body_validation(self):
        """Test ChatRequestBody field validation."""
        # Test valid response_mode
        body = ChatRequestBody.builder().response_mode("streaming").build()
        assert body.response_mode == "streaming"

        body = ChatRequestBody.builder().response_mode("blocking").build()
        assert body.response_mode == "blocking"

        # Test invalid response_mode should be caught by Literal type
        with pytest.raises(ValidationError):
            ChatRequestBody(response_mode="invalid")

    def test_chat_request_body_with_files(self):
        """Test ChatRequestBody with files."""
        chat_file = (
            ChatFile.builder().type("image").transfer_method("remote_url").url("https://example.com/image.jpg").build()
        )
        body = ChatRequestBody.builder().files([chat_file]).build()

        assert len(body.files) == 1
        assert body.files[0].type == "image"
        assert body.files[0].transfer_method == "remote_url"
        assert str(body.files[0].url) == "https://example.com/image.jpg"

    def test_chat_request_body_defaults(self):
        """Test ChatRequestBody default values."""
        body = ChatRequestBody.builder().build()

        assert body.response_mode == "streaming"  # Default value
        assert body.query is None
        assert body.inputs is None
        assert body.user is None
        assert body.conversation_id is None
        assert body.files is None
        assert body.auto_generate_name is None

    def test_chat_response_inheritance(self):
        """Test ChatResponse inherits from BaseResponse."""
        response = ChatResponse()
        assert isinstance(response, BaseResponse)
        assert hasattr(response, "success")
        assert hasattr(response, "code")
        assert hasattr(response, "msg")
        assert hasattr(response, "raw")

    def test_chat_response_fields(self):
        """Test ChatResponse fields."""
        response = ChatResponse(
            event="message",
            task_id="task-123",
            id="id-123",
            message_id="msg-123",
            conversation_id="conv-123",
            mode="chat",
            answer="Hello there!",
            created_at=1679586595,
        )

        assert response.event == "message"
        assert response.task_id == "task-123"
        assert response.id == "id-123"
        assert response.message_id == "msg-123"
        assert response.conversation_id == "conv-123"
        assert response.mode == "chat"
        assert response.answer == "Hello there!"
        assert response.created_at == 1679586595

    def test_chat_request_integration(self):
        """Test complete ChatRequest integration."""
        # Create request body with all fields
        request_body = (
            ChatRequestBody.builder()
            .query("What can you help me with?")
            .inputs({})
            .response_mode("blocking")
            .user("user-123")
            .auto_generate_name(True)
            .build()
        )

        # Create request
        request = ChatRequest.builder().request_body(request_body).build()

        # Verify request structure
        assert request.http_method == HttpMethod.POST
        assert request.uri == "/v1/chat-messages"
        assert request.request_body is not None
        assert request.body is not None
        assert isinstance(request.body, dict)

        # Verify body content
        assert request.body["query"] == "What can you help me with?"
        assert request.body["response_mode"] == "blocking"
        assert request.body["user"] == "user-123"
        assert request.body["auto_generate_name"] is True


class TestStopChatGenerationModels:
    """Test Stop Chat Generation API models."""

    def test_stop_chat_request_builder(self):
        """Test StopChatRequest builder pattern."""
        request_body = StopChatRequestBody.builder().user("user-123").build()
        request = StopChatRequest.builder().task_id("task-123").request_body(request_body).build()

        assert request.http_method == HttpMethod.POST
        assert request.uri == "/v1/chat-messages/:task_id/stop"
        assert request.paths["task_id"] == "task-123"
        assert request.request_body.user == "user-123"

    def test_stop_chat_request_body_builder(self):
        """Test StopChatRequestBody builder pattern."""
        body = StopChatRequestBody.builder().user("user-123").build()

        assert body.user == "user-123"

    def test_stop_chat_request_body_defaults(self):
        """Test StopChatRequestBody default values."""
        body = StopChatRequestBody.builder().build()

        assert body.user is None

    def test_stop_chat_response_inheritance(self):
        """Test StopChatResponse inherits from BaseResponse."""
        response = StopChatResponse()
        assert isinstance(response, BaseResponse)
        assert hasattr(response, "success")
        assert hasattr(response, "code")
        assert hasattr(response, "msg")
        assert hasattr(response, "raw")

    def test_stop_chat_response_fields(self):
        """Test StopChatResponse fields."""
        response = StopChatResponse(result="success")

        assert response.result == "success"

    def test_stop_chat_request_integration(self):
        """Test complete StopChatRequest integration."""
        # Create request body
        request_body = StopChatRequestBody.builder().user("user-123").build()

        # Create request
        request = StopChatRequest.builder().task_id("task-456").request_body(request_body).build()

        # Verify request structure
        assert request.http_method == HttpMethod.POST
        assert request.uri == "/v1/chat-messages/:task_id/stop"
        assert request.paths["task_id"] == "task-456"
        assert request.request_body is not None
        assert request.body is not None
        assert isinstance(request.body, dict)

        # Verify body content
        assert request.body["user"] == "user-123"


class TestGetSuggestedQuestionsModels:
    """Test Get Suggested Questions API models."""

    def test_suggested_questions_request_builder(self):
        """Test GetSuggestedQuestionsRequest builder pattern."""
        request = GetSuggestedQuestionsRequest.builder().message_id("msg-123").user("user-123").build()

        assert request.http_method == HttpMethod.GET
        assert request.uri == "/v1/messages/:message_id/suggested"
        assert request.paths["message_id"] == "msg-123"
        assert request.user == "user-123"

    def test_suggested_questions_request_query_params(self):
        """Test GetSuggestedQuestionsRequest query parameters."""
        request = GetSuggestedQuestionsRequest.builder().message_id("msg-123").user("user-456").build()

        # Check that user is added as query parameter
        assert len(request.queries) > 0
        user_query = next((q for q in request.queries if q[0] == "user"), None)
        assert user_query is not None
        assert user_query[1] == "user-456"

    def test_suggested_questions_response_inheritance(self):
        """Test GetSuggestedQuestionsResponse inherits from BaseResponse."""
        response = GetSuggestedQuestionsResponse()
        assert isinstance(response, BaseResponse)
        assert hasattr(response, "success")
        assert hasattr(response, "code")
        assert hasattr(response, "msg")
        assert hasattr(response, "raw")

    def test_suggested_questions_response_fields(self):
        """Test GetSuggestedQuestionsResponse fields."""
        response = GetSuggestedQuestionsResponse(
            result="success", data=["What is AI?", "How does it work?", "Tell me more"]
        )

        assert response.result == "success"
        assert len(response.data) == 3
        assert response.data[0] == "What is AI?"
        assert response.data[1] == "How does it work?"
        assert response.data[2] == "Tell me more"

    def test_suggested_questions_request_integration(self):
        """Test complete GetSuggestedQuestionsRequest integration."""
        # Create request
        request = GetSuggestedQuestionsRequest.builder().message_id("msg-789").user("user-789").build()

        # Verify request structure
        assert request.http_method == HttpMethod.GET
        assert request.uri == "/v1/messages/:message_id/suggested"
        assert request.paths["message_id"] == "msg-789"
        assert request.user == "user-789"
        # Check query parameters
        user_query = next((q for q in request.queries if q[0] == "user"), None)
        assert user_query is not None
        assert user_query[1] == "user-789"

    def test_suggested_questions_request_defaults(self):
        """Test GetSuggestedQuestionsRequest default values."""
        request = GetSuggestedQuestionsRequest()

        assert request.message_id is None
        assert request.user is None


class TestChatFileModel:
    """Test ChatFile model used in chat requests."""

    def test_chat_file_remote_url(self):
        """Test ChatFile with remote URL."""
        chat_file = (
            ChatFile.builder().type("image").transfer_method("remote_url").url("https://example.com/image.jpg").build()
        )

        assert chat_file.type == "image"
        assert chat_file.transfer_method == "remote_url"
        assert str(chat_file.url) == "https://example.com/image.jpg"
        assert chat_file.upload_file_id is None

    def test_chat_file_local_file(self):
        """Test ChatFile with local file."""
        chat_file = ChatFile.builder().type("image").transfer_method("local_file").upload_file_id("file-123").build()

        assert chat_file.type == "image"
        assert chat_file.transfer_method == "local_file"
        assert chat_file.upload_file_id == "file-123"
        assert chat_file.url is None

    def test_chat_file_validation(self):
        """Test ChatFile field validation."""
        # Test valid file type
        chat_file = ChatFile.builder().type("image").build()
        assert chat_file.type == "image"

        # Test invalid file type should be caught by Literal type
        with pytest.raises(ValidationError):
            ChatFile(type="invalid")

        # Test valid transfer methods with required fields
        chat_file = ChatFile.builder().transfer_method("remote_url").url("https://example.com/test.jpg").build()
        assert chat_file.transfer_method == "remote_url"

        chat_file = ChatFile.builder().transfer_method("local_file").upload_file_id("file-123").build()
        assert chat_file.transfer_method == "local_file"

        # Test invalid transfer method should be caught by Literal type
        with pytest.raises(ValidationError):
            ChatFile(transfer_method="invalid")


class TestChatModelsIntegration:
    """Test integration between different chat models."""

    def test_complete_chat_flow_models(self):
        """Test complete chat flow with all models."""
        # 1. Create chat file
        chat_file = (
            ChatFile.builder().type("image").transfer_method("remote_url").url("https://example.com/test.jpg").build()
        )

        # 2. Create chat request body with file
        request_body = (
            ChatRequestBody.builder()
            .query("What's in this image?")
            .inputs({"context": "image analysis"})
            .response_mode("streaming")
            .user("user-123")
            .files([chat_file])
            .auto_generate_name(True)
            .build()
        )

        # 3. Create chat request
        chat_request = ChatRequest.builder().request_body(request_body).build()

        # 4. Verify complete structure
        assert chat_request.http_method == HttpMethod.POST
        assert chat_request.uri == "/v1/chat-messages"
        assert chat_request.request_body.query == "What's in this image?"
        assert len(chat_request.request_body.files) == 1
        assert chat_request.request_body.files[0].type == "image"

        # 5. Create stop request for the same user
        stop_body = StopChatRequestBody.builder().user("user-123").build()
        stop_request = StopChatRequest.builder().task_id("task-456").request_body(stop_body).build()

        assert stop_request.paths["task_id"] == "task-456"
        assert stop_request.request_body.user == "user-123"

        # 6. Create suggested questions request
        suggested_request = GetSuggestedQuestionsRequest.builder().message_id("msg-789").user("user-123").build()

        assert suggested_request.paths["message_id"] == "msg-789"
        # Check query parameters
        user_query = next((q for q in suggested_request.queries if q[0] == "user"), None)
        assert user_query is not None
        assert user_query[1] == "user-123"

    def test_response_models_structure(self):
        """Test response models structure and inheritance."""
        # Test ChatResponse
        chat_response = ChatResponse(
            event="message",
            task_id="task-123",
            message_id="msg-123",
            conversation_id="conv-123",
            answer="Response text",
        )
        assert isinstance(chat_response, BaseResponse)
        assert chat_response.answer == "Response text"

        # Test StopChatResponse
        stop_response = StopChatResponse(result="success")
        assert isinstance(stop_response, BaseResponse)
        assert stop_response.result == "success"

        # Test GetSuggestedQuestionsResponse
        suggested_response = GetSuggestedQuestionsResponse(result="success", data=["Question 1", "Question 2"])
        assert isinstance(suggested_response, BaseResponse)
        assert len(suggested_response.data) == 2
