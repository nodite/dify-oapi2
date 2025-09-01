"""Application parameters model for Chat API."""

from __future__ import annotations

from typing import Any

from pydantic import BaseModel, Field

from .chat_types import FormInputType


class UserInputFormItem(BaseModel):
    """User input form item model."""

    label: str | None = Field(None, description="Form item label")
    variable: str | None = Field(None, description="Variable name")
    required: bool | None = Field(None, description="Whether required")
    default: str | None = Field(None, description="Default value")
    options: list[str] | None = Field(None, description="Options for select type")
    type: FormInputType | None = Field(None, description="Form input type")

    @classmethod
    def builder(cls) -> UserInputFormItemBuilder:
        """Create a UserInputFormItem builder."""
        return UserInputFormItemBuilder()


class UserInputFormItemBuilder:
    """Builder for UserInputFormItem."""

    def __init__(self) -> None:
        self._form_item = UserInputFormItem()

    def label(self, label: str) -> UserInputFormItemBuilder:
        """Set form item label."""
        self._form_item.label = label
        return self

    def variable(self, variable: str) -> UserInputFormItemBuilder:
        """Set variable name."""
        self._form_item.variable = variable
        return self

    def required(self, required: bool) -> UserInputFormItemBuilder:
        """Set whether required."""
        self._form_item.required = required
        return self

    def default(self, default: str) -> UserInputFormItemBuilder:
        """Set default value."""
        self._form_item.default = default
        return self

    def options(self, options: list[str]) -> UserInputFormItemBuilder:
        """Set options for select type."""
        self._form_item.options = options
        return self

    def type(self, type: FormInputType) -> UserInputFormItemBuilder:
        """Set form input type."""
        self._form_item.type = type
        return self

    def build(self) -> UserInputFormItem:
        """Build the UserInputFormItem instance."""
        return self._form_item


class FileUploadConfig(BaseModel):
    """File upload configuration model."""

    enabled: bool | None = Field(None, description="Whether file upload is enabled")
    number_limits: int | None = Field(None, description="Number limits")
    detail: str | None = Field(None, description="Detail configuration")
    transfer_methods: list[str] | None = Field(None, description="Transfer methods")

    @classmethod
    def builder(cls) -> FileUploadConfigBuilder:
        """Create a FileUploadConfig builder."""
        return FileUploadConfigBuilder()


class FileUploadConfigBuilder:
    """Builder for FileUploadConfig."""

    def __init__(self) -> None:
        self._config = FileUploadConfig()

    def enabled(self, enabled: bool) -> FileUploadConfigBuilder:
        """Set whether enabled."""
        self._config.enabled = enabled
        return self

    def number_limits(self, number_limits: int) -> FileUploadConfigBuilder:
        """Set number limits."""
        self._config.number_limits = number_limits
        return self

    def detail(self, detail: str) -> FileUploadConfigBuilder:
        """Set detail configuration."""
        self._config.detail = detail
        return self

    def transfer_methods(self, transfer_methods: list[str]) -> FileUploadConfigBuilder:
        """Set transfer methods."""
        self._config.transfer_methods = transfer_methods
        return self

    def build(self) -> FileUploadConfig:
        """Build the FileUploadConfig instance."""
        return self._config


class AppParameters(BaseModel):
    """Application parameters model."""

    opening_statement: str | None = Field(None, description="Opening statement")
    suggested_questions: list[str] | None = Field(None, description="Suggested questions")
    suggested_questions_after_answer: dict[str, bool] | None = Field(
        None, description="Suggested questions after answer"
    )
    speech_to_text: dict[str, bool] | None = Field(None, description="Speech to text configuration")
    text_to_speech: dict[str, Any] | None = Field(None, description="Text to speech configuration")
    retriever_resource: dict[str, bool] | None = Field(None, description="Retriever resource configuration")
    annotation_reply: dict[str, bool] | None = Field(None, description="Annotation reply configuration")
    user_input_form: list[UserInputFormItem] | None = Field(None, description="User input form")
    file_upload: dict[str, FileUploadConfig] | None = Field(None, description="File upload configuration")
    system_parameters: dict[str, int] | None = Field(None, description="System parameters")

    @classmethod
    def builder(cls) -> AppParametersBuilder:
        """Create an AppParameters builder."""
        return AppParametersBuilder()


class AppParametersBuilder:
    """Builder for AppParameters."""

    def __init__(self) -> None:
        self._app_parameters = AppParameters()

    def opening_statement(self, opening_statement: str) -> AppParametersBuilder:
        """Set opening statement."""
        self._app_parameters.opening_statement = opening_statement
        return self

    def suggested_questions(self, suggested_questions: list[str]) -> AppParametersBuilder:
        """Set suggested questions."""
        self._app_parameters.suggested_questions = suggested_questions
        return self

    def suggested_questions_after_answer(self, config: dict[str, bool]) -> AppParametersBuilder:
        """Set suggested questions after answer configuration."""
        self._app_parameters.suggested_questions_after_answer = config
        return self

    def speech_to_text(self, config: dict[str, bool]) -> AppParametersBuilder:
        """Set speech to text configuration."""
        self._app_parameters.speech_to_text = config
        return self

    def text_to_speech(self, config: dict[str, Any]) -> AppParametersBuilder:
        """Set text to speech configuration."""
        self._app_parameters.text_to_speech = config
        return self

    def retriever_resource(self, config: dict[str, bool]) -> AppParametersBuilder:
        """Set retriever resource configuration."""
        self._app_parameters.retriever_resource = config
        return self

    def annotation_reply(self, config: dict[str, bool]) -> AppParametersBuilder:
        """Set annotation reply configuration."""
        self._app_parameters.annotation_reply = config
        return self

    def user_input_form(self, user_input_form: list[UserInputFormItem]) -> AppParametersBuilder:
        """Set user input form."""
        self._app_parameters.user_input_form = user_input_form
        return self

    def file_upload(self, file_upload: dict[str, FileUploadConfig]) -> AppParametersBuilder:
        """Set file upload configuration."""
        self._app_parameters.file_upload = file_upload
        return self

    def system_parameters(self, system_parameters: dict[str, int]) -> AppParametersBuilder:
        """Set system parameters."""
        self._app_parameters.system_parameters = system_parameters
        return self

    def build(self) -> AppParameters:
        """Build the AppParameters instance."""
        return self._app_parameters
