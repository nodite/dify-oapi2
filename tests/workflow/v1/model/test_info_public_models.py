from dify_oapi.api.workflow.v1.model.info.app_info import AppInfo
from dify_oapi.api.workflow.v1.model.info.file_upload_config import FileUploadConfig
from dify_oapi.api.workflow.v1.model.info.parameters_info import ParametersInfo
from dify_oapi.api.workflow.v1.model.info.site_info import SiteInfo
from dify_oapi.api.workflow.v1.model.info.system_parameters import SystemParameters
from dify_oapi.api.workflow.v1.model.info.user_input_form import UserInputForm


class TestAppInfo:
    def test_builder_pattern(self) -> None:
        """Test AppInfo builder pattern functionality."""
        app_info = (
            AppInfo.builder()
            .name("Test Workflow App")
            .description("A test workflow application")
            .tags(["test", "workflow", "ai"])
            .mode("workflow")
            .author_name("Test Author")
            .build()
        )
        assert app_info.name == "Test Workflow App"
        assert app_info.description == "A test workflow application"
        assert app_info.tags == ["test", "workflow", "ai"]
        assert app_info.mode == "workflow"
        assert app_info.author_name == "Test Author"

    def test_field_validation(self) -> None:
        """Test AppInfo field validation."""
        app_info = AppInfo(name="Document Processor", mode="workflow", author_name="AI Team")
        assert app_info.name == "Document Processor"
        assert app_info.mode == "workflow"
        assert app_info.author_name == "AI Team"

    def test_serialization(self) -> None:
        """Test AppInfo serialization."""
        app_info = AppInfo(name="Test App", mode="workflow", tags=["test"])
        serialized = app_info.model_dump(exclude_none=True)
        assert serialized["name"] == "Test App"
        assert serialized["mode"] == "workflow"
        assert serialized["tags"] == ["test"]

    def test_direct_instantiation(self) -> None:
        """Test AppInfo direct instantiation alongside builder."""
        direct = AppInfo(name="App1", mode="workflow")
        builder = AppInfo.builder().name("App1").mode("workflow").build()
        assert direct.name == builder.name
        assert direct.mode == builder.mode


class TestUserInputForm:
    def test_builder_pattern(self) -> None:
        """Test UserInputForm builder pattern functionality."""
        form = (
            UserInputForm.builder()
            .label("Query Input")
            .variable("query")
            .required(True)
            .default("Enter your question")
            .options(["option1", "option2", "option3"])
            .build()
        )
        assert form.label == "Query Input"
        assert form.variable == "query"
        assert form.required is True
        assert form.default == "Enter your question"
        assert form.options == ["option1", "option2", "option3"]

    def test_field_validation(self) -> None:
        """Test UserInputForm field validation."""
        form = UserInputForm(label="Temperature", variable="temperature", required=False, default="0.7")
        assert form.label == "Temperature"
        assert form.variable == "temperature"
        assert form.required is False
        assert form.default == "0.7"

    def test_serialization(self) -> None:
        """Test UserInputForm serialization."""
        form = UserInputForm(label="Query", variable="query", required=True)
        serialized = form.model_dump(exclude_none=True)
        assert serialized["label"] == "Query"
        assert serialized["variable"] == "query"
        assert serialized["required"] is True

    def test_direct_instantiation(self) -> None:
        """Test UserInputForm direct instantiation alongside builder."""
        direct = UserInputForm(label="Input", variable="input")
        builder = UserInputForm.builder().label("Input").variable("input").build()
        assert direct.label == builder.label
        assert direct.variable == builder.variable


class TestFileUploadConfig:
    def test_builder_pattern(self) -> None:
        """Test FileUploadConfig builder pattern functionality."""
        config = (
            FileUploadConfig.builder()
            .document({"enabled": True, "number_limits": 5, "transfer_methods": ["local_file"]})
            .image({"enabled": True, "number_limits": 3, "transfer_methods": ["remote_url", "local_file"]})
            .build()
        )
        assert config.document is not None
        assert config.document["enabled"] is True
        assert config.document["number_limits"] == 5
        assert config.image is not None
        assert config.image["enabled"] is True
        assert config.image["number_limits"] == 3

    def test_field_validation(self) -> None:
        """Test FileUploadConfig field validation."""
        config = FileUploadConfig(document={"enabled": True, "number_limits": 3})
        assert config.document is not None
        assert config.document["enabled"] is True
        assert config.document["number_limits"] == 3

    def test_serialization(self) -> None:
        """Test FileUploadConfig serialization."""
        config = FileUploadConfig(document={"enabled": True, "number_limits": 3})
        serialized = config.model_dump(exclude_none=True)
        assert "document" in serialized
        assert serialized["document"]["enabled"] is True

    def test_direct_instantiation(self) -> None:
        """Test FileUploadConfig direct instantiation alongside builder."""
        direct = FileUploadConfig(document={"enabled": False})
        builder = FileUploadConfig.builder().document({"enabled": False}).build()
        assert direct.document == builder.document


class TestSystemParameters:
    def test_builder_pattern(self) -> None:
        """Test SystemParameters builder pattern functionality."""
        params = (
            SystemParameters.builder()
            .file_size_limit(50)
            .image_file_size_limit(10)
            .audio_file_size_limit(100)
            .video_file_size_limit(500)
            .build()
        )
        assert params.file_size_limit == 50
        assert params.image_file_size_limit == 10
        assert params.audio_file_size_limit == 100
        assert params.video_file_size_limit == 500

    def test_field_validation(self) -> None:
        """Test SystemParameters field validation."""
        params = SystemParameters(file_size_limit=50, image_file_size_limit=10)
        assert params.file_size_limit == 50
        assert params.image_file_size_limit == 10

    def test_serialization(self) -> None:
        """Test SystemParameters serialization."""
        params = SystemParameters(file_size_limit=50, image_file_size_limit=10)
        serialized = params.model_dump(exclude_none=True)
        assert serialized["file_size_limit"] == 50
        assert serialized["image_file_size_limit"] == 10

    def test_direct_instantiation(self) -> None:
        """Test SystemParameters direct instantiation alongside builder."""
        direct = SystemParameters(file_size_limit=25)
        builder = SystemParameters.builder().file_size_limit(25).build()
        assert direct.file_size_limit == builder.file_size_limit


class TestSiteInfo:
    def test_builder_pattern(self) -> None:
        """Test SiteInfo builder pattern functionality."""
        site_info = (
            SiteInfo.builder()
            .title("My Workflow App")
            .icon_type("emoji")
            .icon("🤖")
            .icon_background("#FF5733")
            .description("A powerful workflow application")
            .show_workflow_steps(True)
            .build()
        )
        assert site_info.title == "My Workflow App"
        assert site_info.icon_type == "emoji"
        assert site_info.icon == "🤖"
        assert site_info.icon_background == "#FF5733"
        assert site_info.description == "A powerful workflow application"
        assert site_info.show_workflow_steps is True

    def test_field_validation(self) -> None:
        """Test SiteInfo field validation."""
        site_info = SiteInfo(title="My Site", icon_type="emoji", icon="🚀")
        assert site_info.title == "My Site"
        assert site_info.icon_type == "emoji"
        assert site_info.icon == "🚀"

    def test_serialization(self) -> None:
        """Test SiteInfo serialization."""
        site_info = SiteInfo(title="My Site", icon_type="emoji", icon="🚀")
        serialized = site_info.model_dump(exclude_none=True)
        assert serialized["title"] == "My Site"
        assert serialized["icon_type"] == "emoji"
        assert serialized["icon"] == "🚀"

    def test_direct_instantiation(self) -> None:
        """Test SiteInfo direct instantiation alongside builder."""
        direct = SiteInfo(title="Site", icon_type="image")
        builder = SiteInfo.builder().title("Site").icon_type("image").build()
        assert direct.title == builder.title
        assert direct.icon_type == builder.icon_type


class TestParametersInfo:
    def test_builder_pattern(self) -> None:
        """Test ParametersInfo builder pattern functionality."""
        form = UserInputForm.builder().label("Query").variable("query").build()
        file_config = FileUploadConfig.builder().document({"enabled": True}).build()
        sys_params = SystemParameters.builder().file_size_limit(50).build()
        params_info = (
            ParametersInfo.builder()
            .user_input_form([form])
            .file_upload(file_config)
            .system_parameters(sys_params)
            .build()
        )
        assert params_info.user_input_form is not None
        assert len(params_info.user_input_form) == 1
        assert params_info.file_upload is not None
        assert params_info.system_parameters is not None

    def test_field_validation(self) -> None:
        """Test ParametersInfo field validation."""
        params_info = ParametersInfo(user_input_form=[])
        assert params_info.user_input_form is not None
        assert len(params_info.user_input_form) == 0

    def test_serialization(self) -> None:
        """Test ParametersInfo serialization."""
        params_info = ParametersInfo(user_input_form=[])
        serialized = params_info.model_dump(exclude_none=True)
        assert "user_input_form" in serialized
        assert serialized["user_input_form"] == []

    def test_direct_instantiation(self) -> None:
        """Test ParametersInfo direct instantiation alongside builder."""
        direct = ParametersInfo(user_input_form=[])
        builder = ParametersInfo.builder().user_input_form([]).build()
        assert direct.user_input_form is not None
        assert builder.user_input_form is not None
        assert len(direct.user_input_form) == len(builder.user_input_form)
