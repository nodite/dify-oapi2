from __future__ import annotations

from pydantic import BaseModel

from dify_oapi.api.completion.v1.model.completion.completion_message_info import CompletionMessageInfo
from dify_oapi.api.completion.v1.model.completion.metadata import Metadata
from dify_oapi.api.completion.v1.model.completion.retriever_resource import RetrieverResource
from dify_oapi.api.completion.v1.model.completion.usage import Usage


class TestCompletionMessageInfo:
    """Test CompletionMessageInfo public model."""

    def test_builder_pattern(self) -> None:
        """Test CompletionMessageInfo builder pattern."""
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

    def test_field_validation(self) -> None:
        """Test CompletionMessageInfo field validation."""
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

    def test_serialization(self) -> None:
        """Test CompletionMessageInfo serialization."""
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

    def test_direct_instantiation(self) -> None:
        """Test CompletionMessageInfo direct instantiation alongside builder."""
        # Direct instantiation
        direct = CompletionMessageInfo(message_id="test-id", mode="completion")

        # Builder instantiation
        builder = CompletionMessageInfo.builder().message_id("test-id").mode("completion").build()

        assert direct.message_id == builder.message_id
        assert direct.mode == builder.mode
        assert isinstance(direct, BaseModel)
        assert isinstance(builder, BaseModel)


class TestUsage:
    """Test Usage public model."""

    def test_builder_pattern(self) -> None:
        """Test Usage builder pattern."""
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

    def test_field_validation(self) -> None:
        """Test Usage field validation."""
        usage = Usage(total_tokens=100)

        assert usage.total_tokens == 100
        assert usage.prompt_tokens is None
        assert usage.completion_tokens is None

    def test_serialization(self) -> None:
        """Test Usage serialization."""
        usage = Usage.builder().total_tokens(100).build()

        data = usage.model_dump()

        assert data["total_tokens"] == 100
        assert data["prompt_tokens"] is None

    def test_direct_instantiation(self) -> None:
        """Test Usage direct instantiation alongside builder."""
        # Direct instantiation
        direct = Usage(total_tokens=100, currency="USD")

        # Builder instantiation
        builder = Usage.builder().total_tokens(100).currency("USD").build()

        assert direct.total_tokens == builder.total_tokens
        assert direct.currency == builder.currency
        assert isinstance(direct, BaseModel)
        assert isinstance(builder, BaseModel)


class TestRetrieverResource:
    """Test RetrieverResource public model."""

    def test_builder_pattern(self) -> None:
        """Test RetrieverResource builder pattern."""
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

    def test_field_validation(self) -> None:
        """Test RetrieverResource field validation."""
        retriever_resource = RetrieverResource(position=1, content="test content")

        assert retriever_resource.position == 1
        assert retriever_resource.content == "test content"
        assert retriever_resource.dataset_id is None

    def test_serialization(self) -> None:
        """Test RetrieverResource serialization."""
        retriever_resource = RetrieverResource.builder().position(1).content("test content").build()

        data = retriever_resource.model_dump()

        assert data["position"] == 1
        assert data["content"] == "test content"
        assert data["dataset_id"] is None

    def test_direct_instantiation(self) -> None:
        """Test RetrieverResource direct instantiation alongside builder."""
        # Direct instantiation
        direct = RetrieverResource(position=1, content="test")

        # Builder instantiation
        builder = RetrieverResource.builder().position(1).content("test").build()

        assert direct.position == builder.position
        assert direct.content == builder.content
        assert isinstance(direct, BaseModel)
        assert isinstance(builder, BaseModel)


class TestMetadata:
    """Test Metadata public model."""

    def test_builder_pattern(self) -> None:
        """Test Metadata builder pattern."""
        usage = Usage.builder().total_tokens(100).build()
        retriever_resources = [
            RetrieverResource.builder().position(1).content("content 1").build(),
            RetrieverResource.builder().position(2).content("content 2").build(),
        ]

        metadata = Metadata.builder().usage(usage).retriever_resources(retriever_resources).build()

        assert metadata.usage == usage
        assert metadata.retriever_resources == retriever_resources
        assert len(metadata.retriever_resources) == 2

    def test_field_validation(self) -> None:
        """Test Metadata field validation."""
        usage = Usage.builder().total_tokens(100).build()

        metadata = Metadata(usage=usage)

        assert metadata.usage == usage
        assert metadata.retriever_resources is None

    def test_serialization(self) -> None:
        """Test Metadata serialization."""
        usage = Usage.builder().total_tokens(100).build()

        metadata = Metadata.builder().usage(usage).build()

        data = metadata.model_dump()

        assert data["usage"] is not None
        assert data["retriever_resources"] is None

    def test_direct_instantiation(self) -> None:
        """Test Metadata direct instantiation alongside builder."""
        usage = Usage.builder().total_tokens(100).build()

        # Direct instantiation
        direct = Metadata(usage=usage)

        # Builder instantiation
        builder = Metadata.builder().usage(usage).build()

        assert direct.usage == builder.usage
        assert isinstance(direct, BaseModel)
        assert isinstance(builder, BaseModel)
