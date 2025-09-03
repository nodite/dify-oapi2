"""Tests for Application Information API models."""

from dify_oapi.api.chat.v1.model.app_info import AppInfo
from dify_oapi.api.chat.v1.model.app_parameters import (
    AppParameters,
    FileUploadConfig,
    SystemParameters,
    UserInputFormItem,
)
from dify_oapi.api.chat.v1.model.get_app_info_request import GetAppInfoRequest
from dify_oapi.api.chat.v1.model.get_app_info_response import GetAppInfoResponse
from dify_oapi.api.chat.v1.model.get_app_meta_request import GetAppMetaRequest
from dify_oapi.api.chat.v1.model.get_app_meta_response import GetAppMetaResponse
from dify_oapi.api.chat.v1.model.get_app_parameters_request import GetAppParametersRequest
from dify_oapi.api.chat.v1.model.get_app_parameters_response import GetAppParametersResponse
from dify_oapi.api.chat.v1.model.get_site_settings_request import GetSiteSettingsRequest
from dify_oapi.api.chat.v1.model.get_site_settings_response import GetSiteSettingsResponse
from dify_oapi.api.chat.v1.model.site_settings import SiteSettings
from dify_oapi.api.chat.v1.model.tool_icon import ToolIcon, ToolIconDetail
from dify_oapi.core.enum import HttpMethod
from dify_oapi.core.model.base_response import BaseResponse


class TestGetAppInfoModels:
    """Test Get Application Info API models."""

    def test_get_app_info_request_builder(self):
        """Test GetAppInfoRequest builder pattern."""
        request = GetAppInfoRequest.builder().build()

        assert request.http_method == HttpMethod.GET
        assert request.uri == "/v1/info"

    def test_get_app_info_response_inheritance(self):
        """Test GetAppInfoResponse inherits from BaseResponse."""
        response = GetAppInfoResponse()
        assert isinstance(response, BaseResponse)
        assert isinstance(response, AppInfo)
        assert hasattr(response, "success")
        assert hasattr(response, "code")
        assert hasattr(response, "msg")

    def test_app_info_builder(self):
        """Test AppInfo builder pattern."""
        app_info = AppInfo.builder().name("Test App").description("Test Description").tags(["ai", "chat"]).build()

        assert app_info.name == "Test App"
        assert app_info.description == "Test Description"
        assert app_info.tags == ["ai", "chat"]

    def test_app_info_validation(self):
        """Test AppInfo field validation."""
        app_info = AppInfo.builder().name("Test App").description("Test Description").tags([]).build()
        assert isinstance(app_info, AppInfo)
        assert app_info.name == "Test App"
        assert app_info.description == "Test Description"
        assert app_info.tags == []


class TestGetAppParametersModels:
    """Test Get Application Parameters API models."""

    def test_get_app_parameters_request_builder(self):
        """Test GetAppParametersRequest builder pattern."""
        request = GetAppParametersRequest.builder().user("user-123").build()

        assert request.http_method == HttpMethod.GET
        assert request.uri == "/v1/parameters"
        # Query parameter should be added
        assert "user" in request.query

    def test_get_app_parameters_response_inheritance(self):
        """Test GetAppParametersResponse inherits from BaseResponse."""
        response = GetAppParametersResponse()
        assert isinstance(response, BaseResponse)
        assert isinstance(response, AppParameters)
        assert hasattr(response, "success")
        assert hasattr(response, "code")
        assert hasattr(response, "msg")

    def test_app_parameters_builder(self):
        """Test AppParameters builder pattern."""
        # Create user input form item
        form_item = UserInputFormItem.builder().text_input("Name", "name", True, "Default Name").build()

        # Create file upload config
        file_config = (
            FileUploadConfig.builder()
            .enabled(True)
            .number_limits(5)
            .detail("high")
            .transfer_methods(["local_file", "remote_url"])
            .build()
        )

        # Create system parameters
        system_params = (
            SystemParameters.builder()
            .file_size_limit(10485760)
            .image_file_size_limit(5242880)
            .audio_file_size_limit(15728640)
            .video_file_size_limit(52428800)
            .build()
        )

        # Create app parameters
        app_params = (
            AppParameters.builder()
            .opening_statement("Welcome to the app!")
            .suggested_questions(["How can I help?", "What can you do?"])
            .suggested_questions_after_answer(True)
            .speech_to_text(True)
            .text_to_speech(True, "alloy", "en", "enabled")
            .retriever_resource(True)
            .annotation_reply(False)
            .user_input_form([form_item])
            .file_upload(file_config)
            .system_parameters(system_params)
            .build()
        )

        assert app_params.opening_statement == "Welcome to the app!"
        assert app_params.suggested_questions == ["How can I help?", "What can you do?"]
        assert app_params.suggested_questions_after_answer == {"enabled": True}
        assert app_params.speech_to_text == {"enabled": True}
        assert app_params.text_to_speech == {
            "enabled": True,
            "voice": "alloy",
            "language": "en",
            "autoPlay": "enabled",
        }
        assert app_params.retriever_resource == {"enabled": True}
        assert app_params.annotation_reply == {"enabled": False}
        assert len(app_params.user_input_form) == 1
        assert app_params.file_upload["image"] == file_config
        assert app_params.system_parameters == system_params

    def test_user_input_form_item_builder(self):
        """Test UserInputFormItem builder pattern."""
        # Test text input
        text_item = UserInputFormItem.builder().text_input("Name", "name", True, "Default").build()
        assert text_item.text_input == {
            "label": "Name",
            "variable": "name",
            "required": True,
            "default": "Default",
        }

        # Test paragraph input
        paragraph_item = UserInputFormItem.builder().paragraph("Description", "desc", False).build()
        assert paragraph_item.paragraph == {
            "label": "Description",
            "variable": "desc",
            "required": False,
        }

        # Test select input
        select_item = (
            UserInputFormItem.builder().select("Type", "type", True, ["option1", "option2"], "option1").build()
        )
        assert select_item.select == {
            "label": "Type",
            "variable": "type",
            "required": True,
            "options": ["option1", "option2"],
            "default": "option1",
        }

    def test_file_upload_config_builder(self):
        """Test FileUploadConfig builder pattern."""
        config = (
            FileUploadConfig.builder()
            .enabled(True)
            .number_limits(3)
            .detail("low")
            .transfer_methods(["local_file"])
            .build()
        )

        assert config.enabled is True
        assert config.number_limits == 3
        assert config.detail == "low"
        assert config.transfer_methods == ["local_file"]

    def test_system_parameters_builder(self):
        """Test SystemParameters builder pattern."""
        params = (
            SystemParameters.builder()
            .file_size_limit(1024)
            .image_file_size_limit(512)
            .audio_file_size_limit(2048)
            .video_file_size_limit(4096)
            .build()
        )

        assert params.file_size_limit == 1024
        assert params.image_file_size_limit == 512
        assert params.audio_file_size_limit == 2048
        assert params.video_file_size_limit == 4096

    def test_auto_play_type_validation(self):
        """Test AutoPlay type validation."""
        # Valid values
        app_params = AppParameters.builder().text_to_speech(True, auto_play="enabled").build()
        assert app_params.text_to_speech["autoPlay"] == "enabled"

        app_params = AppParameters.builder().text_to_speech(True, auto_play="disabled").build()
        assert app_params.text_to_speech["autoPlay"] == "disabled"

    def test_transfer_method_type_validation(self):
        """Test TransferMethod type validation."""
        # Valid values
        config = FileUploadConfig.builder().transfer_methods(["local_file", "remote_url"]).build()
        assert config.transfer_methods == ["local_file", "remote_url"]


class TestGetAppMetaModels:
    """Test Get Application Meta API models."""

    def test_get_app_meta_request_builder(self):
        """Test GetAppMetaRequest builder pattern."""
        request = GetAppMetaRequest.builder().build()

        assert request.http_method == HttpMethod.GET
        assert request.uri == "/v1/meta"

    def test_get_app_meta_response_inheritance(self):
        """Test GetAppMetaResponse inherits from BaseResponse."""
        response = GetAppMetaResponse()
        assert isinstance(response, BaseResponse)
        assert isinstance(response, ToolIcon)
        assert hasattr(response, "success")
        assert hasattr(response, "code")
        assert hasattr(response, "msg")

    def test_tool_icon_builder(self):
        """Test ToolIcon builder pattern."""
        # Create tool icon detail
        icon_detail = ToolIconDetail.builder().background("#FF0000").content("🔧").build()

        # Create tool icon
        tool_icon = (
            ToolIcon.builder()
            .tool_icons(
                {
                    "calculator": "https://example.com/calculator.png",
                    "weather": icon_detail,
                }
            )
            .build()
        )

        assert tool_icon.tool_icons["calculator"] == "https://example.com/calculator.png"
        assert tool_icon.tool_icons["weather"] == icon_detail

    def test_tool_icon_detail_builder(self):
        """Test ToolIconDetail builder pattern."""
        detail = ToolIconDetail.builder().background("#00FF00").content("⚡").build()

        assert detail.background == "#00FF00"
        assert detail.content == "⚡"


class TestGetSiteSettingsModels:
    """Test Get Site Settings API models."""

    def test_get_site_settings_request_builder(self):
        """Test GetSiteSettingsRequest builder pattern."""
        request = GetSiteSettingsRequest.builder().build()

        assert request.http_method == HttpMethod.GET
        assert request.uri == "/v1/site"

    def test_get_site_settings_response_inheritance(self):
        """Test GetSiteSettingsResponse inherits from BaseResponse."""
        response = GetSiteSettingsResponse()
        assert isinstance(response, BaseResponse)
        assert isinstance(response, SiteSettings)
        assert hasattr(response, "success")
        assert hasattr(response, "code")
        assert hasattr(response, "msg")

    def test_site_settings_builder(self):
        """Test SiteSettings builder pattern."""
        settings = (
            SiteSettings.builder()
            .title("My Chat App")
            .chat_color_theme("#007bff")
            .chat_color_theme_inverted(False)
            .icon_type("emoji")
            .icon("🤖")
            .icon_background("#ffffff")
            .icon_url("https://example.com/icon.png")
            .description("A powerful chat application")
            .copyright("© 2024 My Company")
            .privacy_policy("https://example.com/privacy")
            .custom_disclaimer("Use at your own risk")
            .default_language("en")
            .show_workflow_steps(True)
            .use_icon_as_answer_icon(False)
            .build()
        )

        assert settings.title == "My Chat App"
        assert settings.chat_color_theme == "#007bff"
        assert settings.chat_color_theme_inverted is False
        assert settings.icon_type == "emoji"
        assert settings.icon == "🤖"
        assert settings.icon_background == "#ffffff"
        assert settings.icon_url == "https://example.com/icon.png"
        assert settings.description == "A powerful chat application"
        assert settings.copyright == "© 2024 My Company"
        assert settings.privacy_policy == "https://example.com/privacy"
        assert settings.custom_disclaimer == "Use at your own risk"
        assert settings.default_language == "en"
        assert settings.show_workflow_steps is True
        assert settings.use_icon_as_answer_icon is False

    def test_icon_type_validation(self):
        """Test IconType type validation."""
        # Valid values
        settings = SiteSettings.builder().icon_type("emoji").build()
        assert settings.icon_type == "emoji"

        settings = SiteSettings.builder().icon_type("image").build()
        assert settings.icon_type == "image"

    def test_site_settings_optional_fields(self):
        """Test SiteSettings optional fields."""
        settings = SiteSettings.builder().build()

        # All fields should be optional
        assert settings.title is None
        assert settings.chat_color_theme is None
        assert settings.chat_color_theme_inverted is None
        assert settings.icon_type is None
        assert settings.icon is None
        assert settings.icon_background is None
        assert settings.icon_url is None
        assert settings.description is None
        assert settings.copyright is None
        assert settings.privacy_policy is None
        assert settings.custom_disclaimer is None
        assert settings.default_language is None
        assert settings.show_workflow_steps is None
        assert settings.use_icon_as_answer_icon is None
