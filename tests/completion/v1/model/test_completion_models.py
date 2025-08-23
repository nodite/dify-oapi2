from __future__ import annotations

from dify_oapi.api.completion.v1.model.completion.completion_message_info import (
    CompletionMessageInfo,
)
from dify_oapi.api.completion.v1.model.completion.metadata import Metadata
from dify_oapi.api.completion.v1.model.completion.retriever_resource import (
    RetrieverResource,
)
from dify_oapi.api.completion.v1.model.completion.usage import Usage

# ===== SHARED COMPLETION MODELS TESTS =====


def test_completion_message_info_creation() -> None:
    """Test valid completion message info creation."""
    completion_message_info = CompletionMessageInfo(
        message_id="test-message-id",
        mode="completion",
        answer="Test answer",
        created_at=1705395332,
    )

    assert completion_message_info.message_id == "test-message-id"
    assert completion_message_info.mode == "completion"
    assert completion_message_info.answer == "Test answer"
    assert completion_message_info.created_at == 1705395332
    assert completion_message_info.metadata is None


def test_completion_message_info_builder_pattern() -> None:
    """Test builder pattern functionality."""
    metadata = Metadata.builder().build()

    completion_message_info = (
        CompletionMessageInfo.builder()
        .message_id("test-message-id")
        .mode("completion")
        .answer("Test answer")
        .metadata(metadata)
        .created_at(1705395332)
        .build()
    )

    assert completion_message_info.message_id == "test-message-id"
    assert completion_message_info.mode == "completion"
    assert completion_message_info.answer == "Test answer"
    assert completion_message_info.metadata == metadata
    assert completion_message_info.created_at == 1705395332


def test_metadata_validation() -> None:
    """Test metadata validation."""
    usage = Usage.builder().total_tokens(100).build()
    retriever_resource = RetrieverResource.builder().position(1).content("test content").build()

    metadata = Metadata(
        usage=usage,
        retriever_resources=[retriever_resource],
    )

    assert metadata.usage == usage
    assert metadata.retriever_resources == [retriever_resource]


def test_usage_builder() -> None:
    """Test usage builder pattern."""
    usage = (
        Usage.builder()
        .prompt_tokens(50)
        .completion_tokens(50)
        .total_tokens(100)
        .total_price("0.001")
        .currency("USD")
        .latency(1.5)
        .build()
    )

    assert usage.prompt_tokens == 50
    assert usage.completion_tokens == 50
    assert usage.total_tokens == 100
    assert usage.total_price == "0.001"
    assert usage.currency == "USD"
    assert usage.latency == 1.5


def test_retriever_resource_builder() -> None:
    """Test retriever resource builder pattern."""
    retriever_resource = (
        RetrieverResource.builder()
        .position(1)
        .dataset_id("dataset-123")
        .dataset_name("Test Dataset")
        .document_id("doc-456")
        .document_name("Test Document")
        .segment_id("seg-789")
        .score(0.95)
        .content("Test content")
        .build()
    )

    assert retriever_resource.position == 1
    assert retriever_resource.dataset_id == "dataset-123"
    assert retriever_resource.dataset_name == "Test Dataset"
    assert retriever_resource.document_id == "doc-456"
    assert retriever_resource.document_name == "Test Document"
    assert retriever_resource.segment_id == "seg-789"
    assert retriever_resource.score == 0.95
    assert retriever_resource.content == "Test content"


def test_metadata_builder_pattern() -> None:
    """Test metadata builder pattern."""
    usage = Usage.builder().total_tokens(100).build()
    retriever_resources = [
        RetrieverResource.builder().position(1).content("content 1").build(),
        RetrieverResource.builder().position(2).content("content 2").build(),
    ]

    metadata = Metadata.builder().usage(usage).retriever_resources(retriever_resources).build()

    assert metadata.usage == usage
    assert metadata.retriever_resources == retriever_resources
    assert len(metadata.retriever_resources) == 2


def test_model_serialization() -> None:
    """Test model serialization with model_dump()."""
    completion_message_info = (
        CompletionMessageInfo.builder()
        .message_id("test-id")
        .mode("completion")
        .answer("test answer")
        .created_at(1705395332)
        .build()
    )

    data = completion_message_info.model_dump()

    assert data["message_id"] == "test-id"
    assert data["mode"] == "completion"
    assert data["answer"] == "test answer"
    assert data["created_at"] == 1705395332
    assert data["metadata"] is None


def test_optional_field_handling() -> None:
    """Test optional field handling."""
    # Test with minimal fields
    completion_message_info = CompletionMessageInfo()

    assert completion_message_info.message_id is None
    assert completion_message_info.mode is None
    assert completion_message_info.answer is None
    assert completion_message_info.metadata is None
    assert completion_message_info.created_at is None

    # Test builder with no fields
    empty_completion = CompletionMessageInfo.builder().build()
    assert empty_completion.message_id is None


def test_nested_model_relationships() -> None:
    """Test nested model relationships."""
    usage = Usage.builder().total_tokens(100).build()
    retriever_resource = RetrieverResource.builder().position(1).build()

    metadata = Metadata.builder().usage(usage).retriever_resources([retriever_resource]).build()

    completion_message_info = CompletionMessageInfo.builder().message_id("test-id").metadata(metadata).build()

    assert completion_message_info.metadata is not None
    assert completion_message_info.metadata.usage == usage
    assert completion_message_info.metadata.retriever_resources == [retriever_resource]


# ===== SEND MESSAGE API MODELS TESTS =====


def test_send_message_request_builder() -> None:
    """Test SendMessageRequest builder pattern."""
    from dify_oapi.api.completion.v1.model.completion.send_message_request import SendMessageRequest
    from dify_oapi.api.completion.v1.model.completion.send_message_request_body import SendMessageRequestBody
    from dify_oapi.core.enum import HttpMethod

    request_body = SendMessageRequestBody.builder().query("test query").user("test-user").build()

    request = SendMessageRequest.builder().request_body(request_body).build()

    assert request.http_method == HttpMethod.POST
    assert request.uri == "/v1/completion-messages"
    assert request.request_body == request_body
    assert request.body is not None


def test_send_message_request_body_validation() -> None:
    """Test SendMessageRequestBody validation and builder."""
    from dify_oapi.api.completion.v1.model.completion.send_message_request_body import FileInfo, SendMessageRequestBody

    file_info = (
        FileInfo.builder().type("image").transfer_method("remote_url").url("https://example.com/image.jpg").build()
    )

    request_body = (
        SendMessageRequestBody.builder()
        .inputs({"key": "value"})
        .query("What is AI?")
        .response_mode("blocking")
        .user("user-123")
        .files([file_info])
        .build()
    )

    assert request_body.inputs == {"key": "value"}
    assert request_body.query == "What is AI?"
    assert request_body.response_mode == "blocking"
    assert request_body.user == "user-123"
    assert request_body.files == [file_info]


def test_send_message_response_model() -> None:
    """Test SendMessageResponse model."""
    from dify_oapi.api.completion.v1.model.completion.send_message_response import SendMessageResponse

    response = SendMessageResponse(
        message_id="test-message-id", mode="completion", answer="Test answer", created_at=1705395332
    )

    assert response.message_id == "test-message-id"
    assert response.mode == "completion"
    assert response.answer == "Test answer"
    assert response.created_at == 1705395332
    # Test BaseResponse inheritance
    assert hasattr(response, "success")
    assert hasattr(response, "code")
    assert hasattr(response, "msg")


def test_file_info_builder_pattern() -> None:
    """Test FileInfo builder pattern."""
    from dify_oapi.api.completion.v1.model.completion.send_message_request_body import FileInfo

    file_info = FileInfo.builder().type("image").transfer_method("local_file").upload_file_id("file-123").build()

    assert file_info.type == "image"
    assert file_info.transfer_method == "local_file"
    assert file_info.upload_file_id == "file-123"
    assert file_info.url is None


# ===== STOP RESPONSE API MODELS TESTS =====


def test_stop_response_request_builder() -> None:
    """Test StopResponseRequest builder pattern."""
    from dify_oapi.api.completion.v1.model.completion.stop_response_request import StopResponseRequest
    from dify_oapi.api.completion.v1.model.completion.stop_response_request_body import StopResponseRequestBody
    from dify_oapi.core.enum import HttpMethod

    request_body = StopResponseRequestBody.builder().user("test-user").build()

    request = StopResponseRequest.builder().task_id("task-123").request_body(request_body).build()

    assert request.http_method == HttpMethod.POST
    assert request.uri == "/v1/completion-messages/:task_id/stop"
    assert request.task_id == "task-123"
    assert request.paths["task_id"] == "task-123"
    assert request.request_body == request_body
    assert request.body is not None


def test_stop_response_request_body_validation() -> None:
    """Test StopResponseRequestBody validation and builder."""
    from dify_oapi.api.completion.v1.model.completion.stop_response_request_body import StopResponseRequestBody

    request_body = StopResponseRequestBody.builder().user("user-123").build()

    assert request_body.user == "user-123"


def test_stop_response_response_model() -> None:
    """Test StopResponseResponse model."""
    from dify_oapi.api.completion.v1.model.completion.stop_response_response import StopResponseResponse

    response = StopResponseResponse(result="success")

    assert response.result == "success"
    # Test BaseResponse inheritance
    assert hasattr(response, "success")
    assert hasattr(response, "code")
    assert hasattr(response, "msg")


def test_stop_response_path_parameter_handling() -> None:
    """Test StopResponseRequest path parameter handling."""
    from dify_oapi.api.completion.v1.model.completion.stop_response_request import StopResponseRequest

    request = StopResponseRequest.builder().task_id("task-456").build()

    assert request.task_id == "task-456"
    assert "task_id" in request.paths
    assert request.paths["task_id"] == "task-456"


# ===== FILE API MODELS TESTS =====


def test_file_api_file_info_builder_pattern() -> None:
    """Test File API FileInfo builder pattern."""
    from dify_oapi.api.completion.v1.model.file.file_info import FileInfo

    file_info = (
        FileInfo.builder()
        .id("file-123")
        .name("test.jpg")
        .size(1024)
        .extension("jpg")
        .mime_type("image/jpeg")
        .created_by("user-123")
        .created_at(1705395332)
        .build()
    )

    assert file_info.id == "file-123"
    assert file_info.name == "test.jpg"
    assert file_info.size == 1024
    assert file_info.extension == "jpg"
    assert file_info.mime_type == "image/jpeg"
    assert file_info.created_by == "user-123"
    assert file_info.created_at == 1705395332


def test_upload_file_request_multipart() -> None:
    """Test UploadFileRequest multipart handling."""
    from io import BytesIO

    from dify_oapi.api.completion.v1.model.file.upload_file_request import UploadFileRequest
    from dify_oapi.api.completion.v1.model.file.upload_file_request_body import UploadFileRequestBody
    from dify_oapi.core.enum import HttpMethod

    # Create test file data
    file_data = BytesIO(b"test file content")
    request_body = UploadFileRequestBody.builder().user("test-user").build()

    request = UploadFileRequest.builder().file(file_data, "test.jpg").request_body(request_body).build()

    assert request.http_method == HttpMethod.POST
    assert request.uri == "/v1/files/upload"
    assert request.file == file_data
    assert request.request_body == request_body
    assert "file" in request.files
    assert request.files["file"][0] == "test.jpg"
    assert request.files["file"][1] == file_data
    assert request.body == {"user": "test-user"}


def test_upload_file_request_body_validation() -> None:
    """Test UploadFileRequestBody validation and builder."""
    from dify_oapi.api.completion.v1.model.file.upload_file_request_body import UploadFileRequestBody

    request_body = UploadFileRequestBody.builder().user("user-123").build()

    assert request_body.user == "user-123"

    # Test empty request body
    empty_request_body = UploadFileRequestBody.builder().build()
    assert empty_request_body.user is None


def test_upload_file_response_model() -> None:
    """Test UploadFileResponse model."""
    from dify_oapi.api.completion.v1.model.file.upload_file_response import UploadFileResponse

    response = UploadFileResponse(
        id="file-123",
        name="test.jpg",
        size=1024,
        extension="jpg",
        mime_type="image/jpeg",
        created_by="user-123",
        created_at=1705395332,
    )

    assert response.id == "file-123"
    assert response.name == "test.jpg"
    assert response.size == 1024
    assert response.extension == "jpg"
    assert response.mime_type == "image/jpeg"
    assert response.created_by == "user-123"
    assert response.created_at == 1705395332
    # Test BaseResponse inheritance
    assert hasattr(response, "success")
    assert hasattr(response, "code")
    assert hasattr(response, "msg")


def test_upload_file_request_default_filename() -> None:
    """Test UploadFileRequest with default filename."""
    from io import BytesIO

    from dify_oapi.api.completion.v1.model.file.upload_file_request import UploadFileRequest

    file_data = BytesIO(b"test content")
    request = UploadFileRequest.builder().file(file_data).build()

    assert request.file == file_data
    assert "file" in request.files
    assert request.files["file"][0] == "upload"  # Default filename
    assert request.files["file"][1] == file_data


def test_file_info_serialization() -> None:
    """Test FileInfo serialization."""
    from dify_oapi.api.completion.v1.model.file.file_info import FileInfo

    file_info = FileInfo.builder().id("file-123").name("test.jpg").size(1024).build()

    data = file_info.model_dump()

    assert data["id"] == "file-123"
    assert data["name"] == "test.jpg"
    assert data["size"] == 1024
    assert data["extension"] is None
    assert data["mime_type"] is None
    assert data["created_by"] is None
    assert data["created_at"] is None


# ===== FEEDBACK API MODELS TESTS =====


def test_feedback_info_builder_pattern() -> None:
    """Test FeedbackInfo builder pattern."""
    from dify_oapi.api.completion.v1.model.feedback.feedback_info import FeedbackInfo

    feedback_info = (
        FeedbackInfo.builder()
        .id("feedback-123")
        .rating("like")
        .content("Great response!")
        .from_source("api")
        .from_end_user_id("user-123")
        .from_account_id("account-123")
        .created_at(1705395332)
        .build()
    )

    assert feedback_info.id == "feedback-123"
    assert feedback_info.rating == "like"
    assert feedback_info.content == "Great response!"
    assert feedback_info.from_source == "api"
    assert feedback_info.from_end_user_id == "user-123"
    assert feedback_info.from_account_id == "account-123"
    assert feedback_info.created_at == 1705395332


def test_message_feedback_request_builder() -> None:
    """Test MessageFeedbackRequest builder pattern."""
    from dify_oapi.api.completion.v1.model.feedback.message_feedback_request import MessageFeedbackRequest
    from dify_oapi.api.completion.v1.model.feedback.message_feedback_request_body import MessageFeedbackRequestBody
    from dify_oapi.core.enum import HttpMethod

    request_body = MessageFeedbackRequestBody.builder().rating("like").user("test-user").content("Good answer").build()

    request = MessageFeedbackRequest.builder().message_id("message-123").request_body(request_body).build()

    assert request.http_method == HttpMethod.POST
    assert request.uri == "/v1/messages/:message_id/feedbacks"
    assert request.message_id == "message-123"
    assert request.paths["message_id"] == "message-123"
    assert request.request_body == request_body
    assert request.body is not None


def test_message_feedback_request_body_validation() -> None:
    """Test MessageFeedbackRequestBody validation and builder."""
    from dify_oapi.api.completion.v1.model.feedback.message_feedback_request_body import MessageFeedbackRequestBody

    request_body = (
        MessageFeedbackRequestBody.builder().rating("like").user("user-123").content("Excellent response!").build()
    )

    assert request_body.rating == "like"
    assert request_body.user == "user-123"
    assert request_body.content == "Excellent response!"


def test_message_feedback_response_model() -> None:
    """Test MessageFeedbackResponse model."""
    from dify_oapi.api.completion.v1.model.feedback.message_feedback_response import MessageFeedbackResponse

    response = MessageFeedbackResponse(result="success")

    assert response.result == "success"
    # Test BaseResponse inheritance
    assert hasattr(response, "success")
    assert hasattr(response, "code")
    assert hasattr(response, "msg")


def test_get_feedbacks_request_builder() -> None:
    """Test GetFeedbacksRequest builder pattern."""
    from dify_oapi.api.completion.v1.model.feedback.get_feedbacks_request import GetFeedbacksRequest
    from dify_oapi.core.enum import HttpMethod

    request = GetFeedbacksRequest.builder().page("1").limit("20").build()

    assert request.http_method == HttpMethod.GET
    assert request.uri == "/v1/app/feedbacks"
    assert ("page", "1") in request.queries
    assert ("limit", "20") in request.queries
    assert len(request.queries) == 2


def test_get_feedbacks_response_model() -> None:
    """Test GetFeedbacksResponse model."""
    from dify_oapi.api.completion.v1.model.feedback.feedback_info import FeedbackInfo
    from dify_oapi.api.completion.v1.model.feedback.get_feedbacks_response import GetFeedbacksResponse

    feedback_info = FeedbackInfo.builder().id("feedback-123").rating("like").build()
    response = GetFeedbacksResponse(data=[feedback_info])

    assert response.data == [feedback_info]
    assert len(response.data) == 1
    assert response.data[0].id == "feedback-123"
    # Test BaseResponse inheritance
    assert hasattr(response, "success")
    assert hasattr(response, "code")
    assert hasattr(response, "msg")


def test_feedback_info_serialization() -> None:
    """Test FeedbackInfo serialization."""
    from dify_oapi.api.completion.v1.model.feedback.feedback_info import FeedbackInfo

    feedback_info = FeedbackInfo.builder().id("feedback-123").rating("like").content("Great!").build()

    data = feedback_info.model_dump()

    assert data["id"] == "feedback-123"
    assert data["rating"] == "like"
    assert data["content"] == "Great!"
    assert data["from_source"] is None
    assert data["from_end_user_id"] is None
    assert data["from_account_id"] is None
    assert data["created_at"] is None


# ===== AUDIO API MODELS TESTS =====


def test_audio_info_builder_pattern() -> None:
    """Test AudioInfo builder pattern."""
    from dify_oapi.api.completion.v1.model.audio.audio_info import AudioInfo

    audio_info = AudioInfo.builder().content_type("audio/wav").data(b"audio data").build()

    assert audio_info.content_type == "audio/wav"
    assert audio_info.data == b"audio data"


def test_text_to_audio_request_builder() -> None:
    """Test TextToAudioRequest builder pattern."""
    from dify_oapi.api.completion.v1.model.audio.text_to_audio_request import TextToAudioRequest
    from dify_oapi.api.completion.v1.model.audio.text_to_audio_request_body import TextToAudioRequestBody
    from dify_oapi.core.enum import HttpMethod

    request_body = TextToAudioRequestBody.builder().text("Hello world").user("test-user").build()

    request = TextToAudioRequest.builder().request_body(request_body).build()

    assert request.http_method == HttpMethod.POST
    assert request.uri == "/v1/text-to-audio"
    assert request.request_body == request_body
    assert request.body is not None


def test_text_to_audio_request_body_validation() -> None:
    """Test TextToAudioRequestBody validation and builder."""
    from dify_oapi.api.completion.v1.model.audio.text_to_audio_request_body import TextToAudioRequestBody

    # Test with text
    request_body = TextToAudioRequestBody.builder().text("Convert this to audio").user("user-123").build()

    assert request_body.text == "Convert this to audio"
    assert request_body.user == "user-123"
    assert request_body.message_id is None

    # Test with message_id
    request_body_msg = TextToAudioRequestBody.builder().message_id("message-456").user("user-123").build()

    assert request_body_msg.message_id == "message-456"
    assert request_body_msg.user == "user-123"
    assert request_body_msg.text is None


def test_text_to_audio_response_model() -> None:
    """Test TextToAudioResponse model."""
    from dify_oapi.api.completion.v1.model.audio.text_to_audio_response import TextToAudioResponse

    response = TextToAudioResponse(content_type="audio/wav", data=b"audio binary data")

    assert response.content_type == "audio/wav"
    assert response.data == b"audio binary data"
    # Test BaseResponse inheritance
    assert hasattr(response, "success")
    assert hasattr(response, "code")
    assert hasattr(response, "msg")


def test_audio_info_serialization() -> None:
    """Test AudioInfo serialization."""
    from dify_oapi.api.completion.v1.model.audio.audio_info import AudioInfo

    audio_info = AudioInfo.builder().content_type("audio/wav").data(b"test audio").build()

    data = audio_info.model_dump()

    assert data["content_type"] == "audio/wav"
    assert data["data"] == b"test audio"
