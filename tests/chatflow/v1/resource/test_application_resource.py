from unittest.mock import patch

import pytest

from dify_oapi.api.chatflow.v1.model.app_parameters import (
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
from dify_oapi.api.chatflow.v1.model.tool_icon import ToolIconDetail
from dify_oapi.api.chatflow.v1.model.user_input_form import (
    ParagraphControl,
    SelectControl,
    TextInputControl,
    UserInputFormItem,
)
from dify_oapi.api.chatflow.v1.resource.application import Application
from dify_oapi.core.model.config import Config
from dify_oapi.core.model.request_option import RequestOption


class TestApplicationResource:
    """Test class for Application resource."""

    @pytest.fixture
    def config(self):
        """Create test config."""
        config = Config()
        config.domain = "https://api.dify.ai"
        return config

    @pytest.fixture
    def request_option(self):
        """Create test request option."""
        return RequestOption.builder().api_key("test_api_key").build()

    @pytest.fixture
    def application_resource(self, config):
        """Create Application resource instance."""
        return Application(config)

    @pytest.fixture
    def get_info_request(self):
        """Create test get info request."""
        return GetInfoRequest.builder().build()

    @pytest.fixture
    def get_parameters_request(self):
        """Create test get parameters request."""
        return GetParametersRequest.builder().build()

    @pytest.fixture
    def get_meta_request(self):
        """Create test get meta request."""
        return GetMetaRequest.builder().build()

    @pytest.fixture
    def get_site_request(self):
        """Create test get site request."""
        return GetSiteRequest.builder().build()

    @pytest.fixture
    def get_info_response(self):
        """Create mock get info response."""
        return GetInfoResponse(
            name="Test Application",
            description="A test application for chatflow",
            tags=["test", "chatflow", "ai"],
        )

    @pytest.fixture
    def get_parameters_response(self):
        """Create mock get parameters response."""
        # Create complex nested objects
        suggested_questions_after_answer = SuggestedQuestionsAfterAnswer.builder().enabled(True).build()
        speech_to_text = SpeechToText.builder().enabled(True).build()
        text_to_speech = TextToSpeech.builder().enabled(True).voice("alloy").language("en").auto_play("enabled").build()

        # Create user input form
        text_input = TextInputControl.builder().label("Name").variable("name").required(True).default("John").build()
        form_item = UserInputFormItem.builder().text_input(text_input).build()

        # Create file upload
        image_upload = (
            ImageUpload.builder()
            .enabled(True)
            .number_limits(5)
            .detail("high")
            .transfer_methods(["local_file", "remote_url"])
            .build()
        )
        file_upload = FileUpload.builder().image(image_upload).build()

        # Create system parameters
        system_params = (
            SystemParameters.builder()
            .file_size_limit(10485760)
            .image_file_size_limit(5242880)
            .audio_file_size_limit(15728640)
            .video_file_size_limit(52428800)
            .build()
        )

        return GetParametersResponse(
            opening_statement="Welcome to our AI assistant!",
            suggested_questions=["What can you do?", "How does this work?", "Tell me about your features"],
            suggested_questions_after_answer=suggested_questions_after_answer,
            speech_to_text=speech_to_text,
            text_to_speech=text_to_speech,
            user_input_form=[form_item],
            file_upload=file_upload,
            system_parameters=system_params,
        )

    @pytest.fixture
    def get_meta_response(self):
        """Create mock get meta response."""
        tool_icon_detail = ToolIconDetail.builder().background("#FF5733").content("🤖").build()
        return GetMetaResponse(
            tool_icons={
                "calculator": "https://example.com/calculator-icon.png",
                "weather": tool_icon_detail,
                "search": "https://example.com/search-icon.png",
            },
        )

    @pytest.fixture
    def get_site_response(self):
        """Create mock get site response."""
        return GetSiteResponse(
            title="Test AI Assistant",
            chat_color_theme="blue",
            chat_color_theme_inverted=False,
            icon_type="emoji",
            icon="🤖",
            icon_background="#FFFFFF",
            icon_url=None,
            description="An intelligent AI assistant for testing",
            copyright="© 2024 Test Company",
            privacy_policy="https://example.com/privacy",
            custom_disclaimer="This is a test application",
            default_language="en-US",
            show_workflow_steps=True,
            use_icon_as_answer_icon=False,
        )

    def test_application_resource_initialization(self, config):
        """Test Application resource initialization."""
        application_resource = Application(config)
        assert application_resource.config == config

    @patch("dify_oapi.core.http.transport.Transport.execute")
    def test_info_sync(self, mock_execute, application_resource, get_info_request, request_option, get_info_response):
        """Test sync info method."""
        # Setup mock
        mock_execute.return_value = get_info_response

        # Execute info
        response = application_resource.info(get_info_request, request_option)

        # Verify mock was called correctly
        mock_execute.assert_called_once_with(
            application_resource.config,
            get_info_request,
            unmarshal_as=GetInfoResponse,
            option=request_option,
        )

        # Verify response
        assert response == get_info_response
        assert response.success is True
        assert response.name == "Test Application"
        assert response.description == "A test application for chatflow"
        assert len(response.tags) == 3

    @patch("dify_oapi.core.http.transport.ATransport.aexecute")
    @pytest.mark.asyncio
    async def test_info_async(
        self, mock_aexecute, application_resource, get_info_request, request_option, get_info_response
    ):
        """Test async info method."""
        # Setup mock
        mock_aexecute.return_value = get_info_response

        # Execute async info
        response = await application_resource.ainfo(get_info_request, request_option)

        # Verify mock was called correctly
        mock_aexecute.assert_called_once_with(
            application_resource.config,
            get_info_request,
            unmarshal_as=GetInfoResponse,
            option=request_option,
        )

        # Verify response
        assert response == get_info_response
        assert response.success is True
        assert response.name == "Test Application"

    @patch("dify_oapi.core.http.transport.Transport.execute")
    def test_parameters_sync(
        self, mock_execute, application_resource, get_parameters_request, request_option, get_parameters_response
    ):
        """Test sync parameters method."""
        # Setup mock
        mock_execute.return_value = get_parameters_response

        # Execute parameters
        response = application_resource.parameters(get_parameters_request, request_option)

        # Verify mock was called correctly
        mock_execute.assert_called_once_with(
            application_resource.config,
            get_parameters_request,
            unmarshal_as=GetParametersResponse,
            option=request_option,
        )

        # Verify response
        assert response == get_parameters_response
        assert response.success is True
        assert response.opening_statement == "Welcome to our AI assistant!"
        assert len(response.suggested_questions) == 3
        assert response.suggested_questions_after_answer.enabled is True
        assert response.speech_to_text.enabled is True
        assert response.text_to_speech.enabled is True
        assert response.text_to_speech.voice == "alloy"
        assert response.text_to_speech.auto_play == "enabled"
        assert len(response.user_input_form) == 1
        assert response.file_upload.image.enabled is True
        assert response.system_parameters.file_size_limit == 10485760

    @patch("dify_oapi.core.http.transport.ATransport.aexecute")
    @pytest.mark.asyncio
    async def test_parameters_async(
        self, mock_aexecute, application_resource, get_parameters_request, request_option, get_parameters_response
    ):
        """Test async parameters method."""
        # Setup mock
        mock_aexecute.return_value = get_parameters_response

        # Execute async parameters
        response = await application_resource.aparameters(get_parameters_request, request_option)

        # Verify mock was called correctly
        mock_aexecute.assert_called_once_with(
            application_resource.config,
            get_parameters_request,
            unmarshal_as=GetParametersResponse,
            option=request_option,
        )

        # Verify response
        assert response == get_parameters_response
        assert response.success is True
        assert response.opening_statement == "Welcome to our AI assistant!"

    @patch("dify_oapi.core.http.transport.Transport.execute")
    def test_meta_sync(self, mock_execute, application_resource, get_meta_request, request_option, get_meta_response):
        """Test sync meta method."""
        # Setup mock
        mock_execute.return_value = get_meta_response

        # Execute meta
        response = application_resource.meta(get_meta_request, request_option)

        # Verify mock was called correctly
        mock_execute.assert_called_once_with(
            application_resource.config,
            get_meta_request,
            unmarshal_as=GetMetaResponse,
            option=request_option,
        )

        # Verify response
        assert response == get_meta_response
        assert response.success is True
        assert len(response.tool_icons) == 3
        assert response.tool_icons["calculator"] == "https://example.com/calculator-icon.png"
        assert response.tool_icons["weather"].background == "#FF5733"
        assert response.tool_icons["weather"].content == "🤖"

    @patch("dify_oapi.core.http.transport.ATransport.aexecute")
    @pytest.mark.asyncio
    async def test_meta_async(
        self, mock_aexecute, application_resource, get_meta_request, request_option, get_meta_response
    ):
        """Test async meta method."""
        # Setup mock
        mock_aexecute.return_value = get_meta_response

        # Execute async meta
        response = await application_resource.ameta(get_meta_request, request_option)

        # Verify mock was called correctly
        mock_aexecute.assert_called_once_with(
            application_resource.config,
            get_meta_request,
            unmarshal_as=GetMetaResponse,
            option=request_option,
        )

        # Verify response
        assert response == get_meta_response
        assert response.success is True
        assert len(response.tool_icons) == 3

    @patch("dify_oapi.core.http.transport.Transport.execute")
    def test_site_sync(self, mock_execute, application_resource, get_site_request, request_option, get_site_response):
        """Test sync site method."""
        # Setup mock
        mock_execute.return_value = get_site_response

        # Execute site
        response = application_resource.site(get_site_request, request_option)

        # Verify mock was called correctly
        mock_execute.assert_called_once_with(
            application_resource.config,
            get_site_request,
            unmarshal_as=GetSiteResponse,
            option=request_option,
        )

        # Verify response
        assert response == get_site_response
        assert response.success is True
        assert response.title == "Test AI Assistant"
        assert response.chat_color_theme == "blue"
        assert response.icon_type == "emoji"
        assert response.icon == "🤖"
        assert response.default_language == "en-US"
        assert response.show_workflow_steps is True

    @patch("dify_oapi.core.http.transport.ATransport.aexecute")
    @pytest.mark.asyncio
    async def test_site_async(
        self, mock_aexecute, application_resource, get_site_request, request_option, get_site_response
    ):
        """Test async site method."""
        # Setup mock
        mock_aexecute.return_value = get_site_response

        # Execute async site
        response = await application_resource.asite(get_site_request, request_option)

        # Verify mock was called correctly
        mock_aexecute.assert_called_once_with(
            application_resource.config,
            get_site_request,
            unmarshal_as=GetSiteResponse,
            option=request_option,
        )

        # Verify response
        assert response == get_site_response
        assert response.success is True
        assert response.title == "Test AI Assistant"

    @patch("dify_oapi.core.http.transport.Transport.execute")
    def test_info_error_handling(self, mock_execute, application_resource, get_info_request, request_option):
        """Test info error handling."""
        # Create error response
        error_response = GetInfoResponse(
            success=False,
            code="404",
            msg="Application not found",
        )
        mock_execute.return_value = error_response

        # Execute info
        response = application_resource.info(get_info_request, request_option)

        # Verify error response
        assert response.success is False
        assert response.code == "404"
        assert response.msg == "Application not found"

    @patch("dify_oapi.core.http.transport.Transport.execute")
    def test_parameters_error_handling(
        self, mock_execute, application_resource, get_parameters_request, request_option
    ):
        """Test parameters error handling."""
        # Create error response
        error_response = GetParametersResponse(
            success=False,
            code="403",
            msg="Insufficient permissions",
        )
        mock_execute.return_value = error_response

        # Execute parameters
        response = application_resource.parameters(get_parameters_request, request_option)

        # Verify error response
        assert response.success is False
        assert response.code == "403"
        assert response.msg == "Insufficient permissions"

    @patch("dify_oapi.core.http.transport.Transport.execute")
    def test_meta_error_handling(self, mock_execute, application_resource, get_meta_request, request_option):
        """Test meta error handling."""
        # Create error response
        error_response = GetMetaResponse(
            success=False,
            code="500",
            msg="Internal server error",
        )
        mock_execute.return_value = error_response

        # Execute meta
        response = application_resource.meta(get_meta_request, request_option)

        # Verify error response
        assert response.success is False
        assert response.code == "500"
        assert response.msg == "Internal server error"

    @patch("dify_oapi.core.http.transport.Transport.execute")
    def test_site_error_handling(self, mock_execute, application_resource, get_site_request, request_option):
        """Test site error handling."""
        # Create error response
        error_response = GetSiteResponse(
            success=False,
            code="401",
            msg="Unauthorized access",
        )
        mock_execute.return_value = error_response

        # Execute site
        response = application_resource.site(get_site_request, request_option)

        # Verify error response
        assert response.success is False
        assert response.code == "401"
        assert response.msg == "Unauthorized access"

    @patch("dify_oapi.core.http.transport.ATransport.aexecute")
    @pytest.mark.asyncio
    async def test_info_async_error_handling(
        self, mock_aexecute, application_resource, get_info_request, request_option
    ):
        """Test async info error handling."""
        # Create error response
        error_response = GetInfoResponse(
            success=False,
            code="503",
            msg="Service unavailable",
        )
        mock_aexecute.return_value = error_response

        # Execute async info
        response = await application_resource.ainfo(get_info_request, request_option)

        # Verify error response
        assert response.success is False
        assert response.code == "503"
        assert response.msg == "Service unavailable"

    @patch("dify_oapi.core.http.transport.ATransport.aexecute")
    @pytest.mark.asyncio
    async def test_parameters_async_error_handling(
        self, mock_aexecute, application_resource, get_parameters_request, request_option
    ):
        """Test async parameters error handling."""
        # Create error response
        error_response = GetParametersResponse(
            success=False,
            code="429",
            msg="Rate limit exceeded",
        )
        mock_aexecute.return_value = error_response

        # Execute async parameters
        response = await application_resource.aparameters(get_parameters_request, request_option)

        # Verify error response
        assert response.success is False
        assert response.code == "429"
        assert response.msg == "Rate limit exceeded"

    @patch("dify_oapi.core.http.transport.ATransport.aexecute")
    @pytest.mark.asyncio
    async def test_meta_async_error_handling(
        self, mock_aexecute, application_resource, get_meta_request, request_option
    ):
        """Test async meta error handling."""
        # Create error response
        error_response = GetMetaResponse(
            success=False,
            code="400",
            msg="Bad request",
        )
        mock_aexecute.return_value = error_response

        # Execute async meta
        response = await application_resource.ameta(get_meta_request, request_option)

        # Verify error response
        assert response.success is False
        assert response.code == "400"
        assert response.msg == "Bad request"

    @patch("dify_oapi.core.http.transport.ATransport.aexecute")
    @pytest.mark.asyncio
    async def test_site_async_error_handling(
        self, mock_aexecute, application_resource, get_site_request, request_option
    ):
        """Test async site error handling."""
        # Create error response
        error_response = GetSiteResponse(
            success=False,
            code="502",
            msg="Bad gateway",
        )
        mock_aexecute.return_value = error_response

        # Execute async site
        response = await application_resource.asite(get_site_request, request_option)

        # Verify error response
        assert response.success is False
        assert response.code == "502"
        assert response.msg == "Bad gateway"

    def test_application_method_signatures(self, application_resource):
        """Test application method signatures."""
        # Verify sync methods exist
        assert hasattr(application_resource, "info")
        assert callable(application_resource.info)
        assert hasattr(application_resource, "parameters")
        assert callable(application_resource.parameters)
        assert hasattr(application_resource, "meta")
        assert callable(application_resource.meta)
        assert hasattr(application_resource, "site")
        assert callable(application_resource.site)

        # Verify async methods exist
        assert hasattr(application_resource, "ainfo")
        assert callable(application_resource.ainfo)
        assert hasattr(application_resource, "aparameters")
        assert callable(application_resource.aparameters)
        assert hasattr(application_resource, "ameta")
        assert callable(application_resource.ameta)
        assert hasattr(application_resource, "asite")
        assert callable(application_resource.asite)

    @patch("dify_oapi.core.http.transport.Transport.execute")
    def test_parameters_complex_nested_objects(
        self, mock_execute, application_resource, get_parameters_request, request_option
    ):
        """Test parameters with complex nested objects."""
        # Create complex nested response
        paragraph_control = (
            ParagraphControl.builder().label("Description").variable("desc").required(False).default("").build()
        )
        select_control = (
            SelectControl.builder()
            .label("Category")
            .variable("category")
            .required(True)
            .options(["Technology", "Science", "Art"])
            .build()
        )

        form_items = [
            UserInputFormItem.builder()
            .text_input(TextInputControl.builder().label("Name").variable("name").required(True).build())
            .build(),
            UserInputFormItem.builder().paragraph(paragraph_control).build(),
            UserInputFormItem.builder().select(select_control).build(),
        ]

        complex_response = GetParametersResponse(
            opening_statement="Welcome to our advanced AI assistant!",
            suggested_questions=["What's new?", "How can I help?", "Tell me more"],
            user_input_form=form_items,
        )
        mock_execute.return_value = complex_response

        # Execute parameters
        response = application_resource.parameters(get_parameters_request, request_option)

        # Verify complex response
        assert response.success is True
        assert len(response.user_input_form) == 3
        assert response.user_input_form[0].text_input.label == "Name"
        assert response.user_input_form[1].paragraph.label == "Description"
        assert response.user_input_form[2].select.label == "Category"
        assert len(response.user_input_form[2].select.options) == 3

    @patch("dify_oapi.core.http.transport.Transport.execute")
    def test_meta_empty_tool_icons(self, mock_execute, application_resource, get_meta_request, request_option):
        """Test meta with empty tool icons."""
        # Create response with empty tool icons
        empty_meta_response = GetMetaResponse(
            tool_icons={},
        )
        mock_execute.return_value = empty_meta_response

        # Execute meta
        response = application_resource.meta(get_meta_request, request_option)

        # Verify empty response
        assert response.success is True
        assert len(response.tool_icons) == 0
        assert response.tool_icons == {}

    @patch("dify_oapi.core.http.transport.Transport.execute")
    def test_site_different_themes(self, mock_execute, application_resource, get_site_request, request_option):
        """Test site with different color themes."""
        themes = ["blue", "green", "purple", "orange", "red"]

        for theme in themes:
            # Create response with specific theme
            theme_response = GetSiteResponse(
                title=f"App with {theme} theme",
                chat_color_theme=theme,
                chat_color_theme_inverted=theme == "purple",  # Invert for purple theme
                icon_type="emoji",
                icon="🎨",
            )
            mock_execute.return_value = theme_response

            # Execute site
            response = application_resource.site(get_site_request, request_option)

            # Verify theme response
            assert response.success is True
            assert response.chat_color_theme == theme
            assert response.title == f"App with {theme} theme"
            assert response.chat_color_theme_inverted == (theme == "purple")

    @patch("dify_oapi.core.http.transport.Transport.execute")
    def test_site_different_icon_types(self, mock_execute, application_resource, get_site_request, request_option):
        """Test site with different icon types."""
        icon_configs = [
            ("emoji", "🤖", None),
            ("image", None, "https://example.com/icon.png"),
        ]

        for icon_type, icon, icon_url in icon_configs:
            # Create response with specific icon configuration
            icon_response = GetSiteResponse(
                title="Test App",
                icon_type=icon_type,
                icon=icon,
                icon_url=icon_url,
            )
            mock_execute.return_value = icon_response

            # Execute site
            response = application_resource.site(get_site_request, request_option)

            # Verify icon response
            assert response.success is True
            assert response.icon_type == icon_type
            assert response.icon == icon
            assert response.icon_url == icon_url

    @patch("dify_oapi.core.http.transport.Transport.execute")
    def test_parameters_file_upload_configurations(
        self, mock_execute, application_resource, get_parameters_request, request_option
    ):
        """Test parameters with different file upload configurations."""
        # Create different file upload configurations
        configs = [
            # Image only
            FileUpload.builder()
            .image(
                ImageUpload.builder()
                .enabled(True)
                .number_limits(3)
                .detail("low")
                .transfer_methods(["local_file"])
                .build()
            )
            .build(),
            # Image with high detail
            FileUpload.builder()
            .image(
                ImageUpload.builder()
                .enabled(True)
                .number_limits(10)
                .detail("high")
                .transfer_methods(["local_file", "remote_url"])
                .build()
            )
            .build(),
            # Disabled image upload
            FileUpload.builder().image(ImageUpload.builder().enabled(False).build()).build(),
        ]

        for i, file_upload_config in enumerate(configs):
            # Create response with specific file upload configuration
            config_response = GetParametersResponse(
                opening_statement=f"Config {i}",
                file_upload=file_upload_config,
            )
            mock_execute.return_value = config_response

            # Execute parameters
            response = application_resource.parameters(get_parameters_request, request_option)

            # Verify file upload configuration
            assert response.success is True
            assert response.file_upload is not None
            if i < 2:  # First two configs have enabled image upload
                assert response.file_upload.image.enabled is True
            else:  # Last config has disabled image upload
                assert response.file_upload.image.enabled is False

    @patch("dify_oapi.core.http.transport.Transport.execute")
    def test_parameters_system_parameters_variations(
        self, mock_execute, application_resource, get_parameters_request, request_option
    ):
        """Test parameters with different system parameter configurations."""
        # Create different system parameter configurations
        system_configs = [
            # Small limits
            SystemParameters.builder()
            .file_size_limit(1048576)  # 1MB
            .image_file_size_limit(524288)  # 512KB
            .audio_file_size_limit(2097152)  # 2MB
            .video_file_size_limit(5242880)  # 5MB
            .build(),
            # Large limits
            SystemParameters.builder()
            .file_size_limit(104857600)  # 100MB
            .image_file_size_limit(52428800)  # 50MB
            .audio_file_size_limit(157286400)  # 150MB
            .video_file_size_limit(524288000)  # 500MB
            .build(),
        ]

        for i, system_config in enumerate(system_configs):
            # Create response with specific system configuration
            config_response = GetParametersResponse(
                opening_statement=f"System config {i}",
                system_parameters=system_config,
            )
            mock_execute.return_value = config_response

            # Execute parameters
            response = application_resource.parameters(get_parameters_request, request_option)

            # Verify system configuration
            assert response.success is True
            assert response.system_parameters is not None
            if i == 0:  # Small limits
                assert response.system_parameters.file_size_limit == 1048576
                assert response.system_parameters.image_file_size_limit == 524288
            else:  # Large limits
                assert response.system_parameters.file_size_limit == 104857600
                assert response.system_parameters.image_file_size_limit == 52428800

    @patch("dify_oapi.core.http.transport.Transport.execute")
    def test_info_with_different_tag_configurations(
        self, mock_execute, application_resource, get_info_request, request_option
    ):
        """Test info with different tag configurations."""
        tag_configs = [
            [],  # No tags
            ["ai"],  # Single tag
            ["ai", "chatbot", "assistant"],  # Multiple tags
            ["ai", "chatbot", "assistant", "nlp", "machine-learning", "deep-learning"],  # Many tags
        ]

        for tags in tag_configs:
            # Create response with specific tags
            tag_response = GetInfoResponse(
                name="Test App",
                description="Test description",
                tags=tags,
            )
            mock_execute.return_value = tag_response

            # Execute info
            response = application_resource.info(get_info_request, request_option)

            # Verify tags
            assert response.success is True
            assert len(response.tags) == len(tags)
            assert response.tags == tags

    @patch("dify_oapi.core.http.transport.Transport.execute")
    def test_meta_mixed_tool_icon_types(self, mock_execute, application_resource, get_meta_request, request_option):
        """Test meta with mixed tool icon types."""
        # Create mixed tool icons (URLs and detailed objects)
        mixed_icons = {
            "calculator": "https://example.com/calc.png",
            "weather": ToolIconDetail.builder().background("#87CEEB").content("☀️").build(),
            "search": "https://example.com/search.png",
            "translate": ToolIconDetail.builder().background("#FFB6C1").content("🌐").build(),
            "calendar": "https://example.com/calendar.png",
        }

        mixed_response = GetMetaResponse(
            tool_icons=mixed_icons,
        )
        mock_execute.return_value = mixed_response

        # Execute meta
        response = application_resource.meta(get_meta_request, request_option)

        # Verify mixed icons
        assert response.success is True
        assert len(response.tool_icons) == 5
        assert isinstance(response.tool_icons["calculator"], str)
        assert isinstance(response.tool_icons["weather"], ToolIconDetail)
        assert response.tool_icons["weather"].background == "#87CEEB"
        assert response.tool_icons["weather"].content == "☀️"
        assert isinstance(response.tool_icons["translate"], ToolIconDetail)
        assert response.tool_icons["translate"].background == "#FFB6C1"
