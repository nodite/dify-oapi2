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
    from dify_oapi.api.completion.v1.model.completion.completion_inputs import CompletionInputs
    from dify_oapi.api.completion.v1.model.completion.send_message_request import SendMessageRequest
    from dify_oapi.api.completion.v1.model.completion.send_message_request_body import SendMessageRequestBody
    from dify_oapi.core.enum import HttpMethod

    inputs = CompletionInputs.builder().query("test query").build()
    request_body = SendMessageRequestBody.builder().inputs(inputs).user("test-user").build()

    request = SendMessageRequest.builder().request_body(request_body).build()

    assert request.http_method == HttpMethod.POST
    assert request.uri == "/v1/completion-messages"
    assert request.request_body == request_body
    assert request.body is not None


def test_send_message_request_body_validation() -> None:
    """Test SendMessageRequestBody validation and builder."""
    from dify_oapi.api.completion.v1.model.completion.completion_inputs import CompletionInputs
    from dify_oapi.api.completion.v1.model.completion.send_message_request_body import FileInfo, SendMessageRequestBody

    file_info = (
        FileInfo.builder().type("image").transfer_method("remote_url").url("https://example.com/image.jpg").build()
    )

    inputs = CompletionInputs.builder().query("What is AI?").build()
    request_body = (
        SendMessageRequestBody.builder()
        .inputs(inputs)
        .response_mode("blocking")
        .user("user-123")
        .files([file_info])
        .build()
    )

    assert request_body.inputs == inputs
    assert request_body.inputs.query == "What is AI?"
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


# ===== INFO API MODELS TESTS =====


def test_app_info_builder_pattern() -> None:
    """Test AppInfo builder pattern."""
    from dify_oapi.api.completion.v1.model.info.app_info import AppInfo

    app_info = (
        AppInfo.builder()
        .name("Test App")
        .description("A test application")
        .tags(["ai", "completion"])
        .mode("completion")
        .author_name("Test Author")
        .build()
    )

    assert app_info.name == "Test App"
    assert app_info.description == "A test application"
    assert app_info.tags == ["ai", "completion"]
    assert app_info.mode == "completion"
    assert app_info.author_name == "Test Author"


def test_parameters_info_complex_structure() -> None:
    """Test ParametersInfo complex nested structure."""
    from dify_oapi.api.completion.v1.model.info.file_upload_config import FileUploadConfig
    from dify_oapi.api.completion.v1.model.info.parameters_info import ParametersInfo
    from dify_oapi.api.completion.v1.model.info.system_parameters import SystemParameters
    from dify_oapi.api.completion.v1.model.info.user_input_form import UserInputForm

    user_input_form = UserInputForm.builder().label("Query").variable("query").required(True).build()
    file_upload_config = FileUploadConfig.builder().image({"enabled": True, "number_limits": 3}).build()
    system_parameters = SystemParameters.builder().file_size_limit(10).image_file_size_limit(5).build()

    parameters_info = (
        ParametersInfo.builder()
        .opening_statement("Welcome to the app")
        .suggested_questions(["What can you do?", "How does this work?"])
        .suggested_questions_after_answer({"enabled": True})
        .speech_to_text({"enabled": False})
        .retriever_resource({"enabled": True})
        .annotation_reply({"enabled": False})
        .user_input_form([user_input_form])
        .file_upload(file_upload_config)
        .system_parameters(system_parameters)
        .build()
    )

    assert parameters_info.opening_statement == "Welcome to the app"
    assert parameters_info.suggested_questions == ["What can you do?", "How does this work?"]
    assert parameters_info.suggested_questions_after_answer == {"enabled": True}
    assert parameters_info.speech_to_text == {"enabled": False}
    assert parameters_info.retriever_resource == {"enabled": True}
    assert parameters_info.annotation_reply == {"enabled": False}
    assert parameters_info.user_input_form == [user_input_form]
    assert parameters_info.file_upload == file_upload_config
    assert parameters_info.system_parameters == system_parameters


def test_site_info_builder_pattern() -> None:
    """Test SiteInfo builder pattern."""
    from dify_oapi.api.completion.v1.model.info.site_info import SiteInfo

    site_info = (
        SiteInfo.builder()
        .title("Test WebApp")
        .chat_color_theme("#007bff")
        .chat_color_theme_inverted(False)
        .icon_type("emoji")
        .icon("🤖")
        .icon_background("#ffffff")
        .icon_url("https://example.com/icon.png")
        .description("A test web application")
        .copyright("© 2024 Test Company")
        .privacy_policy("https://example.com/privacy")
        .custom_disclaimer("This is a test app")
        .default_language("en")
        .show_workflow_steps(True)
        .use_icon_as_answer_icon(False)
        .build()
    )

    assert site_info.title == "Test WebApp"
    assert site_info.chat_color_theme == "#007bff"
    assert site_info.chat_color_theme_inverted is False
    assert site_info.icon_type == "emoji"
    assert site_info.icon == "🤖"
    assert site_info.icon_background == "#ffffff"
    assert site_info.icon_url == "https://example.com/icon.png"
    assert site_info.description == "A test web application"
    assert site_info.copyright == "© 2024 Test Company"
    assert site_info.privacy_policy == "https://example.com/privacy"
    assert site_info.custom_disclaimer == "This is a test app"
    assert site_info.default_language == "en"
    assert site_info.show_workflow_steps is True
    assert site_info.use_icon_as_answer_icon is False


def test_user_input_form_builder_pattern() -> None:
    """Test UserInputForm builder pattern."""
    from dify_oapi.api.completion.v1.model.info.user_input_form import UserInputForm

    user_input_form = (
        UserInputForm.builder()
        .label("User Query")
        .variable("query")
        .required(True)
        .default("Enter your question")
        .options(["Option 1", "Option 2", "Option 3"])
        .build()
    )

    assert user_input_form.label == "User Query"
    assert user_input_form.variable == "query"
    assert user_input_form.required is True
    assert user_input_form.default == "Enter your question"
    assert user_input_form.options == ["Option 1", "Option 2", "Option 3"]


def test_file_upload_config_builder_pattern() -> None:
    """Test FileUploadConfig builder pattern."""
    from dify_oapi.api.completion.v1.model.info.file_upload_config import FileUploadConfig

    image_config = {"enabled": True, "number_limits": 5, "transfer_methods": ["remote_url", "local_file"]}

    file_upload_config = FileUploadConfig.builder().image(image_config).build()

    assert file_upload_config.image == image_config
    assert file_upload_config.image["enabled"] is True
    assert file_upload_config.image["number_limits"] == 5


def test_system_parameters_builder_pattern() -> None:
    """Test SystemParameters builder pattern."""
    from dify_oapi.api.completion.v1.model.info.system_parameters import SystemParameters

    system_parameters = (
        SystemParameters.builder()
        .file_size_limit(20)
        .image_file_size_limit(10)
        .audio_file_size_limit(50)
        .video_file_size_limit(100)
        .build()
    )

    assert system_parameters.file_size_limit == 20
    assert system_parameters.image_file_size_limit == 10
    assert system_parameters.audio_file_size_limit == 50
    assert system_parameters.video_file_size_limit == 100


def test_get_info_request_builder() -> None:
    """Test GetInfoRequest builder pattern."""
    from dify_oapi.api.completion.v1.model.info.get_info_request import GetInfoRequest
    from dify_oapi.core.enum import HttpMethod

    request = GetInfoRequest.builder().build()

    assert request.http_method == HttpMethod.GET
    assert request.uri == "/v1/info"
    assert len(request.queries) == 0


def test_get_info_response_model() -> None:
    """Test GetInfoResponse model."""
    from dify_oapi.api.completion.v1.model.info.get_info_response import GetInfoResponse

    response = GetInfoResponse(
        name="Test App",
        description="A test application",
        tags=["ai", "completion"],
        mode="completion",
        author_name="Test Author",
    )

    assert response.name == "Test App"
    assert response.description == "A test application"
    assert response.tags == ["ai", "completion"]
    assert response.mode == "completion"
    assert response.author_name == "Test Author"
    # Test BaseResponse inheritance
    assert hasattr(response, "success")
    assert hasattr(response, "code")
    assert hasattr(response, "msg")


def test_get_parameters_request_builder() -> None:
    """Test GetParametersRequest builder pattern."""
    from dify_oapi.api.completion.v1.model.info.get_parameters_request import GetParametersRequest
    from dify_oapi.core.enum import HttpMethod

    request = GetParametersRequest.builder().build()

    assert request.http_method == HttpMethod.GET
    assert request.uri == "/v1/parameters"
    assert len(request.queries) == 0


def test_get_parameters_response_model() -> None:
    """Test GetParametersResponse model."""
    from dify_oapi.api.completion.v1.model.info.get_parameters_response import GetParametersResponse
    from dify_oapi.api.completion.v1.model.info.user_input_form import UserInputForm

    user_input_form = UserInputForm.builder().label("Query").variable("query").build()

    response = GetParametersResponse(
        opening_statement="Welcome", suggested_questions=["What can you do?"], user_input_form=[user_input_form]
    )

    assert response.opening_statement == "Welcome"
    assert response.suggested_questions == ["What can you do?"]
    assert response.user_input_form == [user_input_form]
    # Test BaseResponse inheritance
    assert hasattr(response, "success")
    assert hasattr(response, "code")
    assert hasattr(response, "msg")


def test_get_site_request_builder() -> None:
    """Test GetSiteRequest builder pattern."""
    from dify_oapi.api.completion.v1.model.info.get_site_request import GetSiteRequest
    from dify_oapi.core.enum import HttpMethod

    request = GetSiteRequest.builder().build()

    assert request.http_method == HttpMethod.GET
    assert request.uri == "/v1/site"
    assert len(request.queries) == 0


def test_get_site_response_model() -> None:
    """Test GetSiteResponse model."""
    from dify_oapi.api.completion.v1.model.info.get_site_response import GetSiteResponse

    response = GetSiteResponse(
        title="Test WebApp",
        chat_color_theme="#007bff",
        icon_type="emoji",
        icon="🤖",
        description="A test web application",
        default_language="en",
    )

    assert response.title == "Test WebApp"
    assert response.chat_color_theme == "#007bff"
    assert response.icon_type == "emoji"
    assert response.icon == "🤖"
    assert response.description == "A test web application"
    assert response.default_language == "en"
    # Test BaseResponse inheritance
    assert hasattr(response, "success")
    assert hasattr(response, "code")
    assert hasattr(response, "msg")


def test_info_models_serialization() -> None:
    """Test info models serialization."""
    from dify_oapi.api.completion.v1.model.info.app_info import AppInfo
    from dify_oapi.api.completion.v1.model.info.site_info import SiteInfo
    from dify_oapi.api.completion.v1.model.info.user_input_form import UserInputForm

    app_info = AppInfo.builder().name("Test App").mode("completion").build()
    data = app_info.model_dump()
    assert data["name"] == "Test App"
    assert data["mode"] == "completion"
    assert data["description"] is None

    site_info = SiteInfo.builder().title("Test Site").icon_type("emoji").build()
    data = site_info.model_dump()
    assert data["title"] == "Test Site"
    assert data["icon_type"] == "emoji"
    assert data["chat_color_theme"] is None

    user_input_form = UserInputForm.builder().label("Query").required(True).build()
    data = user_input_form.model_dump()
    assert data["label"] == "Query"
    assert data["required"] is True
    assert data["variable"] is None


def test_info_models_multiple_inheritance() -> None:
    """Test info response models with multiple inheritance."""
    from dify_oapi.api.completion.v1.model.info.get_info_response import GetInfoResponse
    from dify_oapi.api.completion.v1.model.info.get_parameters_response import GetParametersResponse
    from dify_oapi.api.completion.v1.model.info.get_site_response import GetSiteResponse

    # Test GetInfoResponse inherits from both AppInfo and BaseResponse
    info_response = GetInfoResponse(name="Test App", mode="completion")
    assert info_response.name == "Test App"
    assert info_response.mode == "completion"
    assert hasattr(info_response, "success")  # From BaseResponse
    assert hasattr(info_response, "code")  # From BaseResponse

    # Test GetParametersResponse inherits from both ParametersInfo and BaseResponse
    params_response = GetParametersResponse(opening_statement="Welcome")
    assert params_response.opening_statement == "Welcome"
    assert hasattr(params_response, "success")  # From BaseResponse
    assert hasattr(params_response, "msg")  # From BaseResponse

    # Test GetSiteResponse inherits from both SiteInfo and BaseResponse
    site_response = GetSiteResponse(title="Test Site", icon_type="emoji")
    assert site_response.title == "Test Site"
    assert site_response.icon_type == "emoji"
    assert hasattr(site_response, "success")  # From BaseResponse
    assert hasattr(site_response, "raw")  # From BaseResponse


# ===== ANNOTATION API MODELS TESTS =====


def test_annotation_info_builder_pattern() -> None:
    """Test AnnotationInfo builder pattern."""
    from dify_oapi.api.completion.v1.model.annotation.annotation_info import AnnotationInfo

    annotation_info = (
        AnnotationInfo.builder()
        .id("annotation-123")
        .question("What is AI?")
        .answer("AI is artificial intelligence.")
        .hit_count(5)
        .created_at(1705395332)
        .build()
    )

    assert annotation_info.id == "annotation-123"
    assert annotation_info.question == "What is AI?"
    assert annotation_info.answer == "AI is artificial intelligence."
    assert annotation_info.hit_count == 5
    assert annotation_info.created_at == 1705395332


def test_job_status_info_builder_pattern() -> None:
    """Test JobStatusInfo builder pattern."""
    from dify_oapi.api.completion.v1.model.annotation.job_status_info import JobStatusInfo

    job_status_info = JobStatusInfo.builder().job_id("job-456").job_status("completed").error_msg("").build()

    assert job_status_info.job_id == "job-456"
    assert job_status_info.job_status == "completed"
    assert job_status_info.error_msg == ""


def test_list_annotations_request_builder() -> None:
    """Test ListAnnotationsRequest builder pattern."""
    from dify_oapi.api.completion.v1.model.annotation.list_annotations_request import ListAnnotationsRequest
    from dify_oapi.core.enum import HttpMethod

    request = ListAnnotationsRequest.builder().page("1").limit("20").build()

    assert request.http_method == HttpMethod.GET
    assert request.uri == "/v1/apps/annotations"
    assert ("page", "1") in request.queries
    assert ("limit", "20") in request.queries
    assert len(request.queries) == 2


def test_list_annotations_response_model() -> None:
    """Test ListAnnotationsResponse model."""
    from dify_oapi.api.completion.v1.model.annotation.annotation_info import AnnotationInfo
    from dify_oapi.api.completion.v1.model.annotation.list_annotations_response import ListAnnotationsResponse

    annotation_info = AnnotationInfo.builder().id("annotation-123").question("What is AI?").build()
    response = ListAnnotationsResponse(data=[annotation_info], has_more=False, limit=20, total=1, page=1)

    assert response.data == [annotation_info]
    assert response.has_more is False
    assert response.limit == 20
    assert response.total == 1
    assert response.page == 1
    # Test BaseResponse inheritance
    assert hasattr(response, "success")
    assert hasattr(response, "code")
    assert hasattr(response, "msg")


def test_create_annotation_request_builder() -> None:
    """Test CreateAnnotationRequest builder pattern."""
    from dify_oapi.api.completion.v1.model.annotation.create_annotation_request import CreateAnnotationRequest
    from dify_oapi.api.completion.v1.model.annotation.create_annotation_request_body import CreateAnnotationRequestBody
    from dify_oapi.core.enum import HttpMethod

    request_body = (
        CreateAnnotationRequestBody.builder().question("What is AI?").answer("AI is artificial intelligence.").build()
    )

    request = CreateAnnotationRequest.builder().request_body(request_body).build()

    assert request.http_method == HttpMethod.POST
    assert request.uri == "/v1/apps/annotations"
    assert request.request_body == request_body
    assert request.body is not None


def test_create_annotation_request_body_validation() -> None:
    """Test CreateAnnotationRequestBody validation and builder."""
    from dify_oapi.api.completion.v1.model.annotation.create_annotation_request_body import CreateAnnotationRequestBody

    request_body = (
        CreateAnnotationRequestBody.builder()
        .question("How does machine learning work?")
        .answer("Machine learning uses algorithms to learn from data.")
        .build()
    )

    assert request_body.question == "How does machine learning work?"
    assert request_body.answer == "Machine learning uses algorithms to learn from data."


def test_create_annotation_response_model() -> None:
    """Test CreateAnnotationResponse model."""
    from dify_oapi.api.completion.v1.model.annotation.create_annotation_response import CreateAnnotationResponse

    response = CreateAnnotationResponse(
        id="annotation-123",
        question="What is AI?",
        answer="AI is artificial intelligence.",
        hit_count=0,
        created_at=1705395332,
    )

    assert response.id == "annotation-123"
    assert response.question == "What is AI?"
    assert response.answer == "AI is artificial intelligence."
    assert response.hit_count == 0
    assert response.created_at == 1705395332
    # Test BaseResponse inheritance
    assert hasattr(response, "success")
    assert hasattr(response, "code")
    assert hasattr(response, "msg")


def test_update_annotation_request_path_params() -> None:
    """Test UpdateAnnotationRequest path parameter handling."""
    from dify_oapi.api.completion.v1.model.annotation.update_annotation_request import UpdateAnnotationRequest
    from dify_oapi.api.completion.v1.model.annotation.update_annotation_request_body import UpdateAnnotationRequestBody
    from dify_oapi.core.enum import HttpMethod

    request_body = UpdateAnnotationRequestBody.builder().question("Updated question?").answer("Updated answer.").build()

    request = UpdateAnnotationRequest.builder().annotation_id("annotation-456").request_body(request_body).build()

    assert request.http_method == HttpMethod.PUT
    assert request.uri == "/v1/apps/annotations/:annotation_id"
    assert request.annotation_id == "annotation-456"
    assert request.paths["annotation_id"] == "annotation-456"
    assert request.request_body == request_body
    assert request.body is not None


def test_update_annotation_request_body_validation() -> None:
    """Test UpdateAnnotationRequestBody validation and builder."""
    from dify_oapi.api.completion.v1.model.annotation.update_annotation_request_body import UpdateAnnotationRequestBody

    request_body = (
        UpdateAnnotationRequestBody.builder()
        .question("What is deep learning?")
        .answer("Deep learning is a subset of machine learning.")
        .build()
    )

    assert request_body.question == "What is deep learning?"
    assert request_body.answer == "Deep learning is a subset of machine learning."


def test_update_annotation_response_model() -> None:
    """Test UpdateAnnotationResponse model."""
    from dify_oapi.api.completion.v1.model.annotation.update_annotation_response import UpdateAnnotationResponse

    response = UpdateAnnotationResponse(
        id="annotation-456",
        question="What is deep learning?",
        answer="Deep learning is a subset of machine learning.",
        hit_count=3,
        created_at=1705395332,
    )

    assert response.id == "annotation-456"
    assert response.question == "What is deep learning?"
    assert response.answer == "Deep learning is a subset of machine learning."
    assert response.hit_count == 3
    assert response.created_at == 1705395332
    # Test BaseResponse inheritance
    assert hasattr(response, "success")
    assert hasattr(response, "code")
    assert hasattr(response, "msg")


def test_delete_annotation_request_builder() -> None:
    """Test DeleteAnnotationRequest builder pattern."""
    from dify_oapi.api.completion.v1.model.annotation.delete_annotation_request import DeleteAnnotationRequest
    from dify_oapi.core.enum import HttpMethod

    request = DeleteAnnotationRequest.builder().annotation_id("annotation-789").build()

    assert request.http_method == HttpMethod.DELETE
    assert request.uri == "/v1/apps/annotations/:annotation_id"
    assert request.annotation_id == "annotation-789"
    assert request.paths["annotation_id"] == "annotation-789"


def test_delete_annotation_response_model() -> None:
    """Test DeleteAnnotationResponse model."""
    from dify_oapi.api.completion.v1.model.annotation.delete_annotation_response import DeleteAnnotationResponse

    response = DeleteAnnotationResponse()

    # Test BaseResponse inheritance
    assert hasattr(response, "success")
    assert hasattr(response, "code")
    assert hasattr(response, "msg")
    assert hasattr(response, "raw")


def test_annotation_reply_settings_request_builder() -> None:
    """Test AnnotationReplySettingsRequest builder pattern."""
    from dify_oapi.api.completion.v1.model.annotation.annotation_reply_settings_request import (
        AnnotationReplySettingsRequest,
    )
    from dify_oapi.api.completion.v1.model.annotation.annotation_reply_settings_request_body import (
        AnnotationReplySettingsRequestBody,
    )
    from dify_oapi.core.enum import HttpMethod

    request_body = (
        AnnotationReplySettingsRequestBody.builder()
        .embedding_provider_name("openai")
        .embedding_model_name("text-embedding-ada-002")
        .score_threshold(0.8)
        .build()
    )

    request = AnnotationReplySettingsRequest.builder().action("enable").request_body(request_body).build()

    assert request.http_method == HttpMethod.POST
    assert request.uri == "/v1/apps/annotation-reply/:action"
    assert request.action == "enable"
    assert request.paths["action"] == "enable"
    assert request.request_body == request_body
    assert request.body is not None


def test_annotation_reply_settings_request_body_validation() -> None:
    """Test AnnotationReplySettingsRequestBody validation and builder."""
    from dify_oapi.api.completion.v1.model.annotation.annotation_reply_settings_request_body import (
        AnnotationReplySettingsRequestBody,
    )

    request_body = (
        AnnotationReplySettingsRequestBody.builder()
        .embedding_provider_name("openai")
        .embedding_model_name("text-embedding-ada-002")
        .score_threshold(0.75)
        .build()
    )

    assert request_body.embedding_provider_name == "openai"
    assert request_body.embedding_model_name == "text-embedding-ada-002"
    assert request_body.score_threshold == 0.75


def test_annotation_reply_settings_response_model() -> None:
    """Test AnnotationReplySettingsResponse model."""
    from dify_oapi.api.completion.v1.model.annotation.annotation_reply_settings_response import (
        AnnotationReplySettingsResponse,
    )

    response = AnnotationReplySettingsResponse(job_id="job-123", job_status="waiting", error_msg="")

    assert response.job_id == "job-123"
    assert response.job_status == "waiting"
    assert response.error_msg == ""
    # Test BaseResponse inheritance
    assert hasattr(response, "success")
    assert hasattr(response, "code")
    assert hasattr(response, "msg")


def test_query_annotation_reply_status_request_builder() -> None:
    """Test QueryAnnotationReplyStatusRequest builder pattern."""
    from dify_oapi.api.completion.v1.model.annotation.query_annotation_reply_status_request import (
        QueryAnnotationReplyStatusRequest,
    )
    from dify_oapi.core.enum import HttpMethod

    request = QueryAnnotationReplyStatusRequest.builder().action("enable").job_id("job-456").build()

    assert request.http_method == HttpMethod.GET
    assert request.uri == "/v1/apps/annotation-reply/:action/status/:job_id"
    assert request.action == "enable"
    assert request.job_id == "job-456"
    assert request.paths["action"] == "enable"
    assert request.paths["job_id"] == "job-456"


def test_query_annotation_reply_status_response_model() -> None:
    """Test QueryAnnotationReplyStatusResponse model."""
    from dify_oapi.api.completion.v1.model.annotation.query_annotation_reply_status_response import (
        QueryAnnotationReplyStatusResponse,
    )

    response = QueryAnnotationReplyStatusResponse(job_id="job-456", job_status="completed", error_msg="")

    assert response.job_id == "job-456"
    assert response.job_status == "completed"
    assert response.error_msg == ""
    # Test BaseResponse inheritance
    assert hasattr(response, "success")
    assert hasattr(response, "code")
    assert hasattr(response, "msg")


def test_annotation_models_serialization() -> None:
    """Test annotation models serialization."""
    from dify_oapi.api.completion.v1.model.annotation.annotation_info import AnnotationInfo
    from dify_oapi.api.completion.v1.model.annotation.job_status_info import JobStatusInfo

    annotation_info = (
        AnnotationInfo.builder()
        .id("annotation-123")
        .question("What is AI?")
        .answer("AI is artificial intelligence.")
        .build()
    )
    data = annotation_info.model_dump()
    assert data["id"] == "annotation-123"
    assert data["question"] == "What is AI?"
    assert data["answer"] == "AI is artificial intelligence."
    assert data["hit_count"] is None
    assert data["created_at"] is None

    job_status_info = JobStatusInfo.builder().job_id("job-456").job_status("waiting").build()
    data = job_status_info.model_dump()
    assert data["job_id"] == "job-456"
    assert data["job_status"] == "waiting"
    assert data["error_msg"] is None


def test_annotation_models_multiple_inheritance() -> None:
    """Test annotation response models with multiple inheritance."""
    from dify_oapi.api.completion.v1.model.annotation.annotation_reply_settings_response import (
        AnnotationReplySettingsResponse,
    )
    from dify_oapi.api.completion.v1.model.annotation.create_annotation_response import CreateAnnotationResponse
    from dify_oapi.api.completion.v1.model.annotation.query_annotation_reply_status_response import (
        QueryAnnotationReplyStatusResponse,
    )
    from dify_oapi.api.completion.v1.model.annotation.update_annotation_response import UpdateAnnotationResponse

    # Test CreateAnnotationResponse inherits from both AnnotationInfo and BaseResponse
    create_response = CreateAnnotationResponse(id="annotation-123", question="What is AI?")
    assert create_response.id == "annotation-123"
    assert create_response.question == "What is AI?"
    assert hasattr(create_response, "success")  # From BaseResponse
    assert hasattr(create_response, "code")  # From BaseResponse

    # Test UpdateAnnotationResponse inherits from both AnnotationInfo and BaseResponse
    update_response = UpdateAnnotationResponse(id="annotation-456", answer="Updated answer")
    assert update_response.id == "annotation-456"
    assert update_response.answer == "Updated answer"
    assert hasattr(update_response, "success")  # From BaseResponse
    assert hasattr(update_response, "msg")  # From BaseResponse

    # Test AnnotationReplySettingsResponse inherits from both JobStatusInfo and BaseResponse
    settings_response = AnnotationReplySettingsResponse(job_id="job-123", job_status="waiting")
    assert settings_response.job_id == "job-123"
    assert settings_response.job_status == "waiting"
    assert hasattr(settings_response, "success")  # From BaseResponse
    assert hasattr(settings_response, "raw")  # From BaseResponse

    # Test QueryAnnotationReplyStatusResponse inherits from both JobStatusInfo and BaseResponse
    query_response = QueryAnnotationReplyStatusResponse(job_id="job-789", job_status="completed")
    assert query_response.job_id == "job-789"
    assert query_response.job_status == "completed"
    assert hasattr(query_response, "success")  # From BaseResponse
    assert hasattr(query_response, "code")  # From BaseResponse


def test_annotation_path_parameter_handling() -> None:
    """Test annotation requests with multiple path parameters."""
    from dify_oapi.api.completion.v1.model.annotation.annotation_reply_settings_request import (
        AnnotationReplySettingsRequest,
    )
    from dify_oapi.api.completion.v1.model.annotation.delete_annotation_request import DeleteAnnotationRequest
    from dify_oapi.api.completion.v1.model.annotation.query_annotation_reply_status_request import (
        QueryAnnotationReplyStatusRequest,
    )
    from dify_oapi.api.completion.v1.model.annotation.update_annotation_request import UpdateAnnotationRequest

    # Test single path parameter
    delete_request = DeleteAnnotationRequest.builder().annotation_id("annotation-123").build()
    assert delete_request.annotation_id == "annotation-123"
    assert "annotation_id" in delete_request.paths
    assert delete_request.paths["annotation_id"] == "annotation-123"

    update_request = UpdateAnnotationRequest.builder().annotation_id("annotation-456").build()
    assert update_request.annotation_id == "annotation-456"
    assert "annotation_id" in update_request.paths
    assert update_request.paths["annotation_id"] == "annotation-456"

    # Test single path parameter for action
    settings_request = AnnotationReplySettingsRequest.builder().action("enable").build()
    assert settings_request.action == "enable"
    assert "action" in settings_request.paths
    assert settings_request.paths["action"] == "enable"

    # Test multiple path parameters
    query_request = QueryAnnotationReplyStatusRequest.builder().action("disable").job_id("job-789").build()
    assert query_request.action == "disable"
    assert query_request.job_id == "job-789"
    assert "action" in query_request.paths
    assert "job_id" in query_request.paths
    assert query_request.paths["action"] == "disable"
    assert query_request.paths["job_id"] == "job-789"


def test_annotation_query_parameter_handling() -> None:
    """Test annotation requests with query parameters."""
    from dify_oapi.api.completion.v1.model.annotation.list_annotations_request import ListAnnotationsRequest

    # Test with both page and limit
    request = ListAnnotationsRequest.builder().page("2").limit("50").build()
    assert ("page", "2") in request.queries
    assert ("limit", "50") in request.queries
    assert len(request.queries) == 2

    # Test with only page
    request_page_only = ListAnnotationsRequest.builder().page("1").build()
    assert ("page", "1") in request_page_only.queries
    assert len(request_page_only.queries) == 1

    # Test with only limit
    request_limit_only = ListAnnotationsRequest.builder().limit("10").build()
    assert ("limit", "10") in request_limit_only.queries
    assert len(request_limit_only.queries) == 1

    # Test with no parameters
    request_empty = ListAnnotationsRequest.builder().build()
    assert len(request_empty.queries) == 0


def test_annotation_optional_field_handling() -> None:
    """Test annotation models with optional fields."""
    from dify_oapi.api.completion.v1.model.annotation.annotation_info import AnnotationInfo
    from dify_oapi.api.completion.v1.model.annotation.job_status_info import JobStatusInfo

    # Test AnnotationInfo with minimal fields
    annotation_minimal = AnnotationInfo()
    assert annotation_minimal.id is None
    assert annotation_minimal.question is None
    assert annotation_minimal.answer is None
    assert annotation_minimal.hit_count is None
    assert annotation_minimal.created_at is None

    # Test AnnotationInfo builder with no fields
    annotation_empty = AnnotationInfo.builder().build()
    assert annotation_empty.id is None
    assert annotation_empty.question is None

    # Test JobStatusInfo with minimal fields
    job_status_minimal = JobStatusInfo()
    assert job_status_minimal.job_id is None
    assert job_status_minimal.job_status is None
    assert job_status_minimal.error_msg is None

    # Test JobStatusInfo builder with no fields
    job_status_empty = JobStatusInfo.builder().build()
    assert job_status_empty.job_id is None
    assert job_status_empty.job_status is None
