"""Tests for Application API models."""

from dify_oapi.api.chatflow.v1.model.app_parameters import (
    AppParameters,
    FileUpload,
    ImageUpload,
    SpeechToText,
    SuggestedQuestionsAfterAnswer,
    SystemParameters,
    TextToSpeech,
)
from dify_oapi.api.chatflow.v1.model.get_info_request import GetInfoRequest
from dify_oapi.api.chatflow.v1.model.get_info_response import GetInfoResponse
from dify_oapi.api.chatflow.v1.model.get_meta_request import GetMetaRequest
from dify_oapi.api.chatflow.v1.model.get_meta_response import GetMetaResponse
from dify_oapi.api.chatflow.v1.model.get_parameters_request import GetParametersRequest
from dify_oapi.api.chatflow.v1.model.get_parameters_response import GetParametersResponse
from dify_oapi.api.chatflow.v1.model.get_site_request import GetSiteRequest
from dify_oapi.api.chatflow.v1.model.get_site_response import GetSiteResponse
from dify_oapi.api.chatflow.v1.model.tool_icon import AppMeta, ToolIconDetail
from dify_oapi.api.chatflow.v1.model.user_input_form import (
    ParagraphControl,
    SelectControl,
    TextInputControl,
    UserInputFormItem,
)
from dify_oapi.api.chatflow.v1.model.webapp_settings import WebAppSettings
from dify_oapi.core.enum import HttpMethod
from dify_oapi.core.model.base_response import BaseResponse


class TestGetInfoModels:
    """Test GetInfo API models."""

    def test_request_builder(self):
        """Test GetInfoRequest builder pattern."""
        request = GetInfoRequest.builder().build()

        assert request.http_method == HttpMethod.GET
        assert request.uri == "/v1/info"

    def test_request_validation(self):
        """Test GetInfoRequest validation."""
        request = GetInfoRequest.builder().build()

        # Verify request structure
        assert hasattr(request, "http_method")
        assert hasattr(request, "uri")

    def test_response_inheritance(self):
        """Test GetInfoResponse inherits from BaseResponse."""
        response = GetInfoResponse()

        assert isinstance(response, BaseResponse)
        assert hasattr(response, "success")
        assert hasattr(response, "code")
        assert hasattr(response, "msg")

    def test_response_data_access(self):
        """Test GetInfoResponse data access."""
        response = GetInfoResponse(name="Test App", description="Test Description", tags=["test", "app"])

        assert response.name == "Test App"
        assert response.description == "Test Description"
        assert response.tags == ["test", "app"]


class TestGetParametersModels:
    """Test GetParameters API models."""

    def test_request_builder(self):
        """Test GetParametersRequest builder pattern."""
        request = GetParametersRequest.builder().build()

        assert request.http_method == HttpMethod.GET
        assert request.uri == "/v1/parameters"

    def test_request_validation(self):
        """Test GetParametersRequest validation."""
        request = GetParametersRequest.builder().build()

        # Verify request structure
        assert hasattr(request, "http_method")
        assert hasattr(request, "uri")

    def test_response_inheritance(self):
        """Test GetParametersResponse inherits from BaseResponse."""
        response = GetParametersResponse()

        assert isinstance(response, BaseResponse)
        assert hasattr(response, "success")
        assert hasattr(response, "code")
        assert hasattr(response, "msg")

    def test_response_complex_structure(self):
        """Test GetParametersResponse complex nested structure."""
        # Test nested objects
        suggested_questions_after_answer = SuggestedQuestionsAfterAnswer.builder().enabled(True).build()
        speech_to_text = SpeechToText.builder().enabled(True).build()
        text_to_speech = TextToSpeech.builder().enabled(True).voice("alloy").language("en").auto_play("enabled").build()

        # Test user input form
        text_input = TextInputControl.builder().label("Name").variable("name").required(True).default("John").build()
        form_item = UserInputFormItem.builder().text_input(text_input).build()

        # Test file upload
        image_upload = (
            ImageUpload.builder()
            .enabled(True)
            .number_limits(5)
            .detail("high")
            .transfer_methods(["local_file", "remote_url"])
            .build()
        )
        file_upload = FileUpload.builder().image(image_upload).build()

        # Test system parameters
        system_params = (
            SystemParameters.builder()
            .file_size_limit(10485760)
            .image_file_size_limit(5242880)
            .audio_file_size_limit(15728640)
            .video_file_size_limit(52428800)
            .build()
        )

        response = GetParametersResponse(
            opening_statement="Welcome!",
            suggested_questions=["What can you do?", "How does this work?"],
            suggested_questions_after_answer=suggested_questions_after_answer,
            speech_to_text=speech_to_text,
            text_to_speech=text_to_speech,
            user_input_form=[form_item],
            file_upload=file_upload,
            system_parameters=system_params,
        )

        assert response.opening_statement == "Welcome!"
        assert len(response.suggested_questions) == 2
        assert response.suggested_questions_after_answer.enabled is True
        assert response.speech_to_text.enabled is True
        assert response.text_to_speech.enabled is True
        assert response.text_to_speech.voice == "alloy"
        assert response.text_to_speech.auto_play == "enabled"
        assert len(response.user_input_form) == 1
        assert response.user_input_form[0].text_input.label == "Name"
        assert response.file_upload.image.enabled is True
        assert response.system_parameters.file_size_limit == 10485760

    def test_app_parameters_builder(self):
        """Test AppParameters builder pattern."""
        params = (
            AppParameters.builder()
            .opening_statement("Hello!")
            .suggested_questions(["Question 1", "Question 2"])
            .build()
        )

        assert params.opening_statement == "Hello!"
        assert len(params.suggested_questions) == 2

    def test_user_input_form_builders(self):
        """Test user input form builders."""
        # Test TextInputControl
        text_input = (
            TextInputControl.builder().label("Username").variable("username").required(True).default("user").build()
        )
        assert text_input.label == "Username"
        assert text_input.required is True

        # Test ParagraphControl
        paragraph = ParagraphControl.builder().label("Description").variable("desc").required(False).build()
        assert paragraph.label == "Description"
        assert paragraph.required is False

        # Test SelectControl
        select = (
            SelectControl.builder()
            .label("Category")
            .variable("category")
            .required(True)
            .options(["A", "B", "C"])
            .build()
        )
        assert select.label == "Category"
        assert len(select.options) == 3


class TestGetMetaModels:
    """Test GetMeta API models."""

    def test_request_builder(self):
        """Test GetMetaRequest builder pattern."""
        request = GetMetaRequest.builder().build()

        assert request.http_method == HttpMethod.GET
        assert request.uri == "/v1/meta"

    def test_request_validation(self):
        """Test GetMetaRequest validation."""
        request = GetMetaRequest.builder().build()

        # Verify request structure
        assert hasattr(request, "http_method")
        assert hasattr(request, "uri")

    def test_response_inheritance(self):
        """Test GetMetaResponse inherits from BaseResponse."""
        response = GetMetaResponse()

        assert isinstance(response, BaseResponse)
        assert hasattr(response, "success")
        assert hasattr(response, "code")
        assert hasattr(response, "msg")

    def test_response_tool_icons(self):
        """Test GetMetaResponse tool icons structure."""
        tool_icon_detail = ToolIconDetail.builder().background("#FF0000").content("icon-content").build()

        response = GetMetaResponse(
            tool_icons={
                "tool1": "https://example.com/icon.png",
                "tool2": tool_icon_detail,
            }
        )

        assert len(response.tool_icons) == 2
        assert response.tool_icons["tool1"] == "https://example.com/icon.png"
        assert response.tool_icons["tool2"].background == "#FF0000"

    def test_app_meta_builder(self):
        """Test AppMeta builder pattern."""
        tool_icon = ToolIconDetail.builder().background("#000").content("test").build()
        meta = AppMeta.builder().tool_icons({"test": tool_icon}).build()

        assert len(meta.tool_icons) == 1
        assert meta.tool_icons["test"].background == "#000"


class TestGetSiteModels:
    """Test GetSite API models."""

    def test_request_builder(self):
        """Test GetSiteRequest builder pattern."""
        request = GetSiteRequest.builder().build()

        assert request.http_method == HttpMethod.GET
        assert request.uri == "/v1/site"

    def test_request_validation(self):
        """Test GetSiteRequest validation."""
        request = GetSiteRequest.builder().build()

        # Verify request structure
        assert hasattr(request, "http_method")
        assert hasattr(request, "uri")

    def test_response_inheritance(self):
        """Test GetSiteResponse inherits from BaseResponse."""
        response = GetSiteResponse()

        assert isinstance(response, BaseResponse)
        assert hasattr(response, "success")
        assert hasattr(response, "code")
        assert hasattr(response, "msg")

    def test_response_webapp_settings(self):
        """Test GetSiteResponse webapp settings structure."""
        response = GetSiteResponse(
            title="My App",
            chat_color_theme="blue",
            chat_color_theme_inverted=False,
            icon_type="emoji",
            icon="🤖",
            icon_background="#FFFFFF",
            icon_url="https://example.com/icon.png",
            description="My awesome app",
            copyright="© 2024 My Company",
            privacy_policy="Privacy policy text",
            custom_disclaimer="Custom disclaimer",
            default_language="en-US",
            show_workflow_steps=True,
            use_icon_as_answer_icon=False,
        )

        assert response.title == "My App"
        assert response.chat_color_theme == "blue"
        assert response.chat_color_theme_inverted is False
        assert response.icon_type == "emoji"
        assert response.icon == "🤖"
        assert response.default_language == "en-US"
        assert response.show_workflow_steps is True

    def test_webapp_settings_builder(self):
        """Test WebAppSettings builder pattern."""
        settings = (
            WebAppSettings.builder()
            .title("Test App")
            .chat_color_theme("green")
            .icon_type("image")
            .default_language("zh-Hans")
            .show_workflow_steps(False)
            .build()
        )

        assert settings.title == "Test App"
        assert settings.chat_color_theme == "green"
        assert settings.icon_type == "image"
        assert settings.default_language == "zh-Hans"
        assert settings.show_workflow_steps is False

    def test_literal_type_validation(self):
        """Test Literal type validation in webapp settings."""
        # Test valid values
        settings = WebAppSettings(
            chat_color_theme="purple",
            icon_type="emoji",
            default_language="ja-JP",
        )

        assert settings.chat_color_theme == "purple"
        assert settings.icon_type == "emoji"
        assert settings.default_language == "ja-JP"
