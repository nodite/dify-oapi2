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
