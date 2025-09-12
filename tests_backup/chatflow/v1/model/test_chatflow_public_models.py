from dify_oapi.api.chatflow.v1.model.annotation_info import AnnotationInfo
from dify_oapi.api.chatflow.v1.model.app_info import AppInfo
from dify_oapi.api.chatflow.v1.model.chat_file import ChatFile
from dify_oapi.api.chatflow.v1.model.chat_message import ChatMessage, MessageFeedback, MessageFile
from dify_oapi.api.chatflow.v1.model.conversation_info import ConversationInfo
from dify_oapi.api.chatflow.v1.model.feedback_info import FeedbackInfo
from dify_oapi.api.chatflow.v1.model.file_info import FileInfo
from dify_oapi.api.chatflow.v1.model.retriever_resource import RetrieverResource
from dify_oapi.api.chatflow.v1.model.usage_info import UsageInfo


class TestChatMessage:
    def test_builder_pattern(self):
        """Test ChatMessage builder pattern functionality."""
        message = (
            ChatMessage.builder()
            .id("msg_123")
            .conversation_id("conv_456")
            .query("Hello")
            .answer("Hi there!")
            .created_at(1234567890)
            .build()
        )

        assert message.id == "msg_123"
        assert message.conversation_id == "conv_456"
        assert message.query == "Hello"
        assert message.answer == "Hi there!"
        assert message.created_at == 1234567890

    def test_field_validation(self):
        """Test ChatMessage field validation."""
        message = ChatMessage()

        # Test optional fields
        assert message.id is None
        assert message.conversation_id is None
        assert message.inputs is None
        assert message.query is None
        assert message.answer is None
        assert message.message_files is None
        assert message.feedback is None
        assert message.retriever_resources is None
        assert message.created_at is None

    def test_with_inputs(self):
        """Test ChatMessage with inputs."""
        inputs = {"user_name": "Alice", "context": "test"}
        message = ChatMessage.builder().inputs(inputs).build()

        assert message.inputs == inputs

    def test_with_message_files(self):
        """Test ChatMessage with message files."""
        message_file = MessageFile(id="file_123", type="image", url="https://example.com/image.jpg")
        message = ChatMessage.builder().message_files([message_file]).build()

        assert len(message.message_files) == 1
        assert message.message_files[0].id == "file_123"

    def test_with_feedback(self):
        """Test ChatMessage with feedback."""
        feedback = MessageFeedback(rating="like")
        message = ChatMessage.builder().feedback(feedback).build()

        assert message.feedback.rating == "like"


class TestChatFile:
    def test_builder_pattern(self):
        """Test ChatFile builder pattern functionality."""
        file = (
            ChatFile.builder().type("image").transfer_method("remote_url").url("https://example.com/image.jpg").build()
        )

        assert file.type == "image"
        assert file.transfer_method == "remote_url"
        assert file.url == "https://example.com/image.jpg"

    def test_field_validation(self):
        """Test ChatFile field validation."""
        file = ChatFile()

        # Test optional fields
        assert file.type is None
        assert file.transfer_method is None
        assert file.url is None
        assert file.upload_file_id is None

    def test_local_file_upload(self):
        """Test ChatFile with local file upload."""
        file = ChatFile.builder().type("document").transfer_method("local_file").upload_file_id("upload_123").build()

        assert file.type == "document"
        assert file.transfer_method == "local_file"
        assert file.upload_file_id == "upload_123"


class TestFileInfo:
    def test_builder_pattern(self):
        """Test FileInfo builder pattern functionality."""
        file_info = (
            FileInfo.builder()
            .id("file_123")
            .name("document.pdf")
            .size(1024)
            .extension("pdf")
            .mime_type("application/pdf")
            .created_by("user_456")
            .created_at(1234567890)
            .build()
        )

        assert file_info.id == "file_123"
        assert file_info.name == "document.pdf"
        assert file_info.size == 1024
        assert file_info.extension == "pdf"
        assert file_info.mime_type == "application/pdf"
        assert file_info.created_by == "user_456"
        assert file_info.created_at == 1234567890

    def test_field_validation(self):
        """Test FileInfo field validation."""
        file_info = FileInfo()

        # Test optional fields
        assert file_info.id is None
        assert file_info.name is None
        assert file_info.size is None
        assert file_info.extension is None
        assert file_info.mime_type is None
        assert file_info.created_by is None
        assert file_info.created_at is None


class TestConversationInfo:
    def test_builder_pattern(self):
        """Test ConversationInfo builder pattern functionality."""
        conversation = (
            ConversationInfo.builder()
            .id("conv_123")
            .name("Test Conversation")
            .status("normal")
            .introduction("Welcome to the conversation")
            .created_at(1234567890)
            .updated_at(1234567900)
            .build()
        )

        assert conversation.id == "conv_123"
        assert conversation.name == "Test Conversation"
        assert conversation.status == "normal"
        assert conversation.introduction == "Welcome to the conversation"
        assert conversation.created_at == 1234567890
        assert conversation.updated_at == 1234567900

    def test_field_validation(self):
        """Test ConversationInfo field validation."""
        conversation = ConversationInfo()

        # Test optional fields
        assert conversation.id is None
        assert conversation.name is None
        assert conversation.inputs is None
        assert conversation.status is None
        assert conversation.introduction is None
        assert conversation.created_at is None
        assert conversation.updated_at is None

    def test_with_inputs(self):
        """Test ConversationInfo with inputs."""
        inputs = {"user_name": "Alice", "context": "test"}
        conversation = ConversationInfo.builder().inputs(inputs).build()

        assert conversation.inputs == inputs


class TestFeedbackInfo:
    def test_builder_pattern(self):
        """Test FeedbackInfo builder pattern functionality."""
        feedback = (
            FeedbackInfo.builder()
            .id("feedback_123")
            .app_id("app_456")
            .conversation_id("conv_789")
            .message_id("msg_012")
            .rating("like")
            .content("Great response!")
            .from_source("api")
            .from_end_user_id("user_345")
            .created_at("2023-01-01T00:00:00Z")
            .updated_at("2023-01-01T00:01:00Z")
            .build()
        )

        assert feedback.id == "feedback_123"
        assert feedback.app_id == "app_456"
        assert feedback.conversation_id == "conv_789"
        assert feedback.message_id == "msg_012"
        assert feedback.rating == "like"
        assert feedback.content == "Great response!"
        assert feedback.from_source == "api"
        assert feedback.from_end_user_id == "user_345"
        assert feedback.created_at == "2023-01-01T00:00:00Z"
        assert feedback.updated_at == "2023-01-01T00:01:00Z"

    def test_field_validation(self):
        """Test FeedbackInfo field validation."""
        feedback = FeedbackInfo()

        # Test optional fields
        assert feedback.id is None
        assert feedback.app_id is None
        assert feedback.conversation_id is None
        assert feedback.message_id is None
        assert feedback.rating is None
        assert feedback.content is None
        assert feedback.from_source is None
        assert feedback.from_end_user_id is None
        assert feedback.from_account_id is None
        assert feedback.created_at is None
        assert feedback.updated_at is None


class TestAppInfo:
    def test_builder_pattern(self):
        """Test AppInfo builder pattern functionality."""
        app = AppInfo.builder().name("Test App").description("A test application").tags(["test", "demo"]).build()

        assert app.name == "Test App"
        assert app.description == "A test application"
        assert app.tags == ["test", "demo"]

    def test_field_validation(self):
        """Test AppInfo field validation."""
        app = AppInfo()

        # Test optional fields
        assert app.name is None
        assert app.description is None
        assert app.tags is None


class TestAnnotationInfo:
    def test_builder_pattern(self):
        """Test AnnotationInfo builder pattern functionality."""
        annotation = (
            AnnotationInfo.builder()
            .id("annotation_123")
            .question("What is AI?")
            .answer("AI is artificial intelligence")
            .hit_count(5)
            .created_at(1234567890)
            .build()
        )

        assert annotation.id == "annotation_123"
        assert annotation.question == "What is AI?"
        assert annotation.answer == "AI is artificial intelligence"
        assert annotation.hit_count == 5
        assert annotation.created_at == 1234567890

    def test_field_validation(self):
        """Test AnnotationInfo field validation."""
        annotation = AnnotationInfo()

        # Test optional fields
        assert annotation.id is None
        assert annotation.question is None
        assert annotation.answer is None
        assert annotation.hit_count is None
        assert annotation.created_at is None


class TestUsageInfo:
    def test_builder_pattern(self):
        """Test UsageInfo builder pattern functionality."""
        usage = (
            UsageInfo.builder()
            .prompt_tokens(100)
            .completion_tokens(50)
            .total_tokens(150)
            .total_price("0.001")
            .currency("USD")
            .latency(1.5)
            .build()
        )

        assert usage.prompt_tokens == 100
        assert usage.completion_tokens == 50
        assert usage.total_tokens == 150
        assert usage.total_price == "0.001"
        assert usage.currency == "USD"
        assert usage.latency == 1.5

    def test_field_validation(self):
        """Test UsageInfo field validation."""
        usage = UsageInfo()

        # Test optional fields
        assert usage.prompt_tokens is None
        assert usage.prompt_unit_price is None
        assert usage.prompt_price_unit is None
        assert usage.prompt_price is None
        assert usage.completion_tokens is None
        assert usage.completion_unit_price is None
        assert usage.completion_price_unit is None
        assert usage.completion_price is None
        assert usage.total_tokens is None
        assert usage.total_price is None
        assert usage.currency is None
        assert usage.latency is None

    def test_complete_usage_info(self):
        """Test UsageInfo with all fields."""
        usage = (
            UsageInfo.builder()
            .prompt_tokens(100)
            .prompt_unit_price("0.00001")
            .prompt_price_unit("token")
            .prompt_price("0.001")
            .completion_tokens(50)
            .completion_unit_price("0.00002")
            .completion_price_unit("token")
            .completion_price("0.001")
            .total_tokens(150)
            .total_price("0.002")
            .currency("USD")
            .latency(1.5)
            .build()
        )

        assert usage.prompt_tokens == 100
        assert usage.prompt_unit_price == "0.00001"
        assert usage.prompt_price_unit == "token"
        assert usage.prompt_price == "0.001"
        assert usage.completion_tokens == 50
        assert usage.completion_unit_price == "0.00002"
        assert usage.completion_price_unit == "token"
        assert usage.completion_price == "0.001"
        assert usage.total_tokens == 150
        assert usage.total_price == "0.002"
        assert usage.currency == "USD"
        assert usage.latency == 1.5


class TestRetrieverResource:
    def test_builder_pattern(self):
        """Test RetrieverResource builder pattern functionality."""
        resource = (
            RetrieverResource.builder()
            .position(1)
            .dataset_id("dataset_123")
            .dataset_name("Test Dataset")
            .document_id("doc_456")
            .document_name("Test Document")
            .segment_id("seg_789")
            .score(0.95)
            .content("This is the retrieved content")
            .build()
        )

        assert resource.position == 1
        assert resource.dataset_id == "dataset_123"
        assert resource.dataset_name == "Test Dataset"
        assert resource.document_id == "doc_456"
        assert resource.document_name == "Test Document"
        assert resource.segment_id == "seg_789"
        assert resource.score == 0.95
        assert resource.content == "This is the retrieved content"

    def test_field_validation(self):
        """Test RetrieverResource field validation."""
        resource = RetrieverResource()

        # Test optional fields
        assert resource.position is None
        assert resource.dataset_id is None
        assert resource.dataset_name is None
        assert resource.document_id is None
        assert resource.document_name is None
        assert resource.segment_id is None
        assert resource.score is None
        assert resource.content is None
