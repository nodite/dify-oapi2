"""Tests for Chat API public model classes."""

from pydantic import BaseModel

from dify_oapi.api.chat.v1.model.agent_thought import AgentThought
from dify_oapi.api.chat.v1.model.annotation_info import AnnotationInfo
from dify_oapi.api.chat.v1.model.app_info import AppInfo
from dify_oapi.api.chat.v1.model.app_parameters import AppParameters, FileUploadConfig, UserInputFormItem
from dify_oapi.api.chat.v1.model.conversation_info import ConversationInfo
from dify_oapi.api.chat.v1.model.conversation_variable import ConversationVariable
from dify_oapi.api.chat.v1.model.feedback_info import FeedbackInfo
from dify_oapi.api.chat.v1.model.file_info import FileInfo
from dify_oapi.api.chat.v1.model.message_file import MessageFile
from dify_oapi.api.chat.v1.model.message_info import MessageInfo
from dify_oapi.api.chat.v1.model.pagination_info import PaginationInfo
from dify_oapi.api.chat.v1.model.retriever_resource import RetrieverResource
from dify_oapi.api.chat.v1.model.site_settings import SiteSettings
from dify_oapi.api.chat.v1.model.tool_icon import ToolIcon, ToolIconDetail
from dify_oapi.api.chat.v1.model.usage_info import UsageInfo


class TestMessageInfo:
    """Test MessageInfo public model class."""

    def test_message_info_builder(self):
        """Test MessageInfo builder pattern."""
        message = (
            MessageInfo.builder()
            .id("msg-123")
            .conversation_id("conv-123")
            .query("Hello")
            .answer("Hi there")
            .created_at(1234567890)
            .build()
        )

        assert message.id == "msg-123"
        assert message.conversation_id == "conv-123"
        assert message.query == "Hello"
        assert message.answer == "Hi there"
        assert message.created_at == 1234567890

    def test_message_info_validation(self):
        """Test MessageInfo field validation."""
        message = MessageInfo.builder().id("msg-123").build()
        assert isinstance(message, BaseModel)
        assert message.id == "msg-123"


class TestConversationInfo:
    """Test ConversationInfo public model class."""

    def test_conversation_info_builder(self):
        """Test ConversationInfo builder pattern."""
        conversation = (
            ConversationInfo.builder().id("conv-123").name("Test Chat").status("normal").created_at(1234567890).build()
        )

        assert conversation.id == "conv-123"
        assert conversation.name == "Test Chat"
        assert conversation.status == "normal"
        assert conversation.created_at == 1234567890

    def test_conversation_info_validation(self):
        """Test ConversationInfo field validation."""
        conversation = ConversationInfo.builder().id("conv-123").build()
        assert isinstance(conversation, BaseModel)
        assert conversation.id == "conv-123"


class TestFileInfo:
    """Test FileInfo public model class."""

    def test_file_info_builder(self):
        """Test FileInfo builder pattern."""
        file_info = (
            FileInfo.builder()
            .id("file-123")
            .name("test.jpg")
            .size(1024)
            .extension("jpg")
            .mime_type("image/jpeg")
            .created_at(1234567890)
            .build()
        )

        assert file_info.id == "file-123"
        assert file_info.name == "test.jpg"
        assert file_info.size == 1024
        assert file_info.extension == "jpg"
        assert file_info.mime_type == "image/jpeg"
        assert file_info.created_at == 1234567890

    def test_file_info_validation(self):
        """Test FileInfo field validation."""
        file_info = FileInfo.builder().id("file-123").build()
        assert isinstance(file_info, BaseModel)
        assert file_info.id == "file-123"


class TestFeedbackInfo:
    """Test FeedbackInfo public model class."""

    def test_feedback_info_builder(self):
        """Test FeedbackInfo builder pattern."""
        feedback = (
            FeedbackInfo.builder()
            .id("feedback-123")
            .message_id("msg-123")
            .rating("like")
            .content("Great response!")
            .created_at("2023-01-01T00:00:00Z")
            .build()
        )

        assert feedback.id == "feedback-123"
        assert feedback.message_id == "msg-123"
        assert feedback.rating == "like"
        assert feedback.content == "Great response!"
        assert feedback.created_at == "2023-01-01T00:00:00Z"

    def test_feedback_info_validation(self):
        """Test FeedbackInfo field validation."""
        feedback = FeedbackInfo.builder().id("feedback-123").build()
        assert isinstance(feedback, BaseModel)
        assert feedback.id == "feedback-123"


class TestAppInfo:
    """Test AppInfo public model class."""

    def test_app_info_builder(self):
        """Test AppInfo builder pattern."""
        app_info = AppInfo.builder().name("Test App").description("A test application").tags(["ai", "chat"]).build()

        assert app_info.name == "Test App"
        assert app_info.description == "A test application"
        assert app_info.tags == ["ai", "chat"]

    def test_app_info_validation(self):
        """Test AppInfo field validation."""
        app_info = AppInfo.builder().name("Test App").build()
        assert isinstance(app_info, BaseModel)
        assert app_info.name == "Test App"


class TestAnnotationInfo:
    """Test AnnotationInfo public model class."""

    def test_annotation_info_builder(self):
        """Test AnnotationInfo builder pattern."""
        annotation = (
            AnnotationInfo.builder()
            .id("annotation-123")
            .question("What is AI?")
            .answer("Artificial Intelligence is...")
            .hit_count(5)
            .created_at(1234567890)
            .build()
        )

        assert annotation.id == "annotation-123"
        assert annotation.question == "What is AI?"
        assert annotation.answer == "Artificial Intelligence is..."
        assert annotation.hit_count == 5
        assert annotation.created_at == 1234567890

    def test_annotation_info_validation(self):
        """Test AnnotationInfo field validation."""
        annotation = AnnotationInfo.builder().id("annotation-123").build()
        assert isinstance(annotation, BaseModel)
        assert annotation.id == "annotation-123"


class TestUsageInfo:
    """Test UsageInfo public model class."""

    def test_usage_info_builder(self):
        """Test UsageInfo builder pattern."""
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

    def test_usage_info_validation(self):
        """Test UsageInfo field validation."""
        usage = UsageInfo.builder().total_tokens(150).build()
        assert isinstance(usage, BaseModel)
        assert usage.total_tokens == 150


class TestRetrieverResource:
    """Test RetrieverResource public model class."""

    def test_retriever_resource_builder(self):
        """Test RetrieverResource builder pattern."""
        resource = (
            RetrieverResource.builder()
            .position(1)
            .dataset_id("dataset-123")
            .dataset_name("Test Dataset")
            .document_id("doc-123")
            .document_name("Test Document")
            .segment_id("segment-123")
            .score(0.95)
            .content("Test content")
            .build()
        )

        assert resource.position == 1
        assert resource.dataset_id == "dataset-123"
        assert resource.dataset_name == "Test Dataset"
        assert resource.document_id == "doc-123"
        assert resource.document_name == "Test Document"
        assert resource.segment_id == "segment-123"
        assert resource.score == 0.95
        assert resource.content == "Test content"

    def test_retriever_resource_validation(self):
        """Test RetrieverResource field validation."""
        resource = RetrieverResource.builder().position(1).build()
        assert isinstance(resource, BaseModel)
        assert resource.position == 1


class TestAgentThought:
    """Test AgentThought public model class."""

    def test_agent_thought_builder(self):
        """Test AgentThought builder pattern."""
        thought = (
            AgentThought.builder()
            .id("thought-123")
            .message_id("msg-123")
            .position(1)
            .thought("I need to search for information")
            .tool("search")
            .tool_input('{"query": "test"}')
            .observation("Found relevant information")
            .created_at(1234567890)
            .build()
        )

        assert thought.id == "thought-123"
        assert thought.message_id == "msg-123"
        assert thought.position == 1
        assert thought.thought == "I need to search for information"
        assert thought.tool == "search"
        assert thought.tool_input == '{"query": "test"}'
        assert thought.observation == "Found relevant information"
        assert thought.created_at == 1234567890

    def test_agent_thought_validation(self):
        """Test AgentThought field validation."""
        thought = AgentThought.builder().id("thought-123").build()
        assert isinstance(thought, BaseModel)
        assert thought.id == "thought-123"


class TestMessageFile:
    """Test MessageFile public model class."""

    def test_message_file_builder(self):
        """Test MessageFile builder pattern."""
        message_file = (
            MessageFile.builder()
            .id("file-123")
            .type("image")
            .url("https://example.com/image.jpg")
            .belongs_to("user")
            .build()
        )

        assert message_file.id == "file-123"
        assert message_file.type == "image"
        assert message_file.url == "https://example.com/image.jpg"
        assert message_file.belongs_to == "user"

    def test_message_file_validation(self):
        """Test MessageFile field validation."""
        message_file = MessageFile.builder().id("file-123").build()
        assert isinstance(message_file, BaseModel)
        assert message_file.id == "file-123"


class TestConversationVariable:
    """Test ConversationVariable public model class."""

    def test_conversation_variable_builder(self):
        """Test ConversationVariable builder pattern."""
        variable = (
            ConversationVariable.builder()
            .id("var-123")
            .name("user_name")
            .value_type("string")
            .value("John Doe")
            .description("User's name")
            .created_at(1234567890)
            .build()
        )

        assert variable.id == "var-123"
        assert variable.name == "user_name"
        assert variable.value_type == "string"
        assert variable.value == "John Doe"
        assert variable.description == "User's name"
        assert variable.created_at == 1234567890

    def test_conversation_variable_validation(self):
        """Test ConversationVariable field validation."""
        variable = ConversationVariable.builder().id("var-123").build()
        assert isinstance(variable, BaseModel)
        assert variable.id == "var-123"


class TestAppParameters:
    """Test AppParameters public model class."""

    def test_app_parameters_builder(self):
        """Test AppParameters builder pattern."""
        form_item = UserInputFormItem.builder().label("Name").variable("name").required(True).type("text-input").build()

        file_config = (
            FileUploadConfig.builder()
            .enabled(True)
            .number_limits(5)
            .transfer_methods(["local_file", "remote_url"])
            .build()
        )

        parameters = (
            AppParameters.builder()
            .opening_statement("Welcome!")
            .suggested_questions(["How can I help?", "What can you do?"])
            .user_input_form([form_item])
            .file_upload({"image": file_config})
            .build()
        )

        assert parameters.opening_statement == "Welcome!"
        assert parameters.suggested_questions == ["How can I help?", "What can you do?"]
        assert len(parameters.user_input_form) == 1
        assert parameters.user_input_form[0].label == "Name"
        assert "image" in parameters.file_upload
        assert parameters.file_upload["image"].enabled is True

    def test_app_parameters_validation(self):
        """Test AppParameters field validation."""
        parameters = AppParameters.builder().opening_statement("Welcome!").build()
        assert isinstance(parameters, BaseModel)
        assert parameters.opening_statement == "Welcome!"


class TestSiteSettings:
    """Test SiteSettings public model class."""

    def test_site_settings_builder(self):
        """Test SiteSettings builder pattern."""
        settings = (
            SiteSettings.builder()
            .title("My Chat App")
            .icon_type("emoji")
            .icon("🤖")
            .description("A chat application")
            .default_language("en")
            .show_workflow_steps(True)
            .build()
        )

        assert settings.title == "My Chat App"
        assert settings.icon_type == "emoji"
        assert settings.icon == "🤖"
        assert settings.description == "A chat application"
        assert settings.default_language == "en"
        assert settings.show_workflow_steps is True

    def test_site_settings_validation(self):
        """Test SiteSettings field validation."""
        settings = SiteSettings.builder().title("My Chat App").build()
        assert isinstance(settings, BaseModel)
        assert settings.title == "My Chat App"


class TestToolIcon:
    """Test ToolIcon public model class."""

    def test_tool_icon_builder_with_string(self):
        """Test ToolIcon builder pattern with string icon."""
        tool_icon = ToolIcon.builder().icon("https://example.com/icon.png").build()

        assert tool_icon.icon == "https://example.com/icon.png"

    def test_tool_icon_builder_with_detail(self):
        """Test ToolIcon builder pattern with detail icon."""
        icon_detail = ToolIconDetail.builder().background("#FF0000").content("🔧").build()

        tool_icon = ToolIcon.builder().icon(icon_detail).build()

        assert isinstance(tool_icon.icon, ToolIconDetail)
        assert tool_icon.icon.background == "#FF0000"
        assert tool_icon.icon.content == "🔧"

    def test_tool_icon_validation(self):
        """Test ToolIcon field validation."""
        tool_icon = ToolIcon.builder().icon("test").build()
        assert isinstance(tool_icon, BaseModel)
        assert tool_icon.icon == "test"


class TestPaginationInfo:
    """Test PaginationInfo public model class."""

    def test_pagination_info_builder(self):
        """Test PaginationInfo builder pattern."""
        pagination = PaginationInfo.builder().limit(20).has_more(True).total(100).page(1).build()

        assert pagination.limit == 20
        assert pagination.has_more is True
        assert pagination.total == 100
        assert pagination.page == 1

    def test_pagination_info_validation(self):
        """Test PaginationInfo field validation."""
        pagination = PaginationInfo.builder().limit(20).build()
        assert isinstance(pagination, BaseModel)
        assert pagination.limit == 20


class TestAllPublicModelsImportable:
    """Test all public model classes can be imported correctly."""

    def test_all_models_importable(self):
        """Test all public model classes can be imported correctly."""
        # This test passes if all imports in the module work
        assert MessageInfo is not None
        assert ConversationInfo is not None
        assert FileInfo is not None
        assert FeedbackInfo is not None
        assert AppInfo is not None
        assert AnnotationInfo is not None
        assert UsageInfo is not None
        assert RetrieverResource is not None
        assert AgentThought is not None
        assert MessageFile is not None
        assert ConversationVariable is not None
        assert AppParameters is not None
        assert UserInputFormItem is not None
        assert FileUploadConfig is not None
        assert SiteSettings is not None
        assert ToolIcon is not None
        assert ToolIconDetail is not None
        assert PaginationInfo is not None

    def test_all_models_have_builders(self):
        """Test all public model classes have builder methods."""
        models = [
            MessageInfo,
            ConversationInfo,
            FileInfo,
            FeedbackInfo,
            AppInfo,
            AnnotationInfo,
            UsageInfo,
            RetrieverResource,
            AgentThought,
            MessageFile,
            ConversationVariable,
            AppParameters,
            UserInputFormItem,
            FileUploadConfig,
            SiteSettings,
            ToolIcon,
            ToolIconDetail,
            PaginationInfo,
        ]

        for model in models:
            assert hasattr(model, "builder"), f"{model.__name__} should have builder method"
            builder = model.builder()
            assert hasattr(builder, "build"), f"{model.__name__}Builder should have build method"

    def test_all_models_inherit_from_basemodel(self):
        """Test all public model classes inherit from BaseModel."""
        models = [
            MessageInfo,
            ConversationInfo,
            FileInfo,
            FeedbackInfo,
            AppInfo,
            AnnotationInfo,
            UsageInfo,
            RetrieverResource,
            AgentThought,
            MessageFile,
            ConversationVariable,
            AppParameters,
            UserInputFormItem,
            FileUploadConfig,
            SiteSettings,
            ToolIcon,
            ToolIconDetail,
            PaginationInfo,
        ]

        for model in models:
            assert issubclass(model, BaseModel), f"{model.__name__} should inherit from BaseModel"
