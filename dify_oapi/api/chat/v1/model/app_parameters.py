from __future__ import annotations

from typing import Any

from pydantic import BaseModel

from .chat_types import AutoPlay, TransferMethod


class UserInputFormItem(BaseModel):
    """User input form item configuration."""

    # Text input configuration
    text_input: dict[str, Any] | None = None
    # Paragraph input configuration
    paragraph: dict[str, Any] | None = None
    # Select input configuration
    select: dict[str, Any] | None = None

    @staticmethod
    def builder() -> UserInputFormItemBuilder:
        return UserInputFormItemBuilder()


class UserInputFormItemBuilder:
    def __init__(self):
        self._user_input_form_item = UserInputFormItem()

    def build(self) -> UserInputFormItem:
        return self._user_input_form_item

    def text_input(
        self, label: str, variable: str, required: bool, default: str | None = None
    ) -> UserInputFormItemBuilder:
        config = {"label": label, "variable": variable, "required": required}
        if default is not None:
            config["default"] = default
        self._user_input_form_item.text_input = config
        return self

    def paragraph(
        self, label: str, variable: str, required: bool, default: str | None = None
    ) -> UserInputFormItemBuilder:
        config = {"label": label, "variable": variable, "required": required}
        if default is not None:
            config["default"] = default
        self._user_input_form_item.paragraph = config
        return self

    def select(
        self, label: str, variable: str, required: bool, options: list[str], default: str | None = None
    ) -> UserInputFormItemBuilder:
        config = {"label": label, "variable": variable, "required": required, "options": options}
        if default is not None:
            config["default"] = default
        self._user_input_form_item.select = config
        return self


class FileUploadConfig(BaseModel):
    """File upload configuration."""

    enabled: bool
    number_limits: int | None = None
    detail: str | None = None
    transfer_methods: list[TransferMethod] | None = None

    @staticmethod
    def builder() -> FileUploadConfigBuilder:
        return FileUploadConfigBuilder()


class FileUploadConfigBuilder:
    def __init__(self):
        self._file_upload_config = FileUploadConfig(enabled=False)

    def build(self) -> FileUploadConfig:
        return self._file_upload_config

    def enabled(self, enabled: bool) -> FileUploadConfigBuilder:
        self._file_upload_config.enabled = enabled
        return self

    def number_limits(self, number_limits: int) -> FileUploadConfigBuilder:
        self._file_upload_config.number_limits = number_limits
        return self

    def detail(self, detail: str) -> FileUploadConfigBuilder:
        self._file_upload_config.detail = detail
        return self

    def transfer_methods(self, transfer_methods: list[TransferMethod]) -> FileUploadConfigBuilder:
        self._file_upload_config.transfer_methods = transfer_methods
        return self


class SystemParameters(BaseModel):
    """System parameters configuration."""

    file_size_limit: int | None = None
    image_file_size_limit: int | None = None
    audio_file_size_limit: int | None = None
    video_file_size_limit: int | None = None

    @staticmethod
    def builder() -> SystemParametersBuilder:
        return SystemParametersBuilder()


class SystemParametersBuilder:
    def __init__(self):
        self._system_parameters = SystemParameters()

    def build(self) -> SystemParameters:
        return self._system_parameters

    def file_size_limit(self, file_size_limit: int) -> SystemParametersBuilder:
        self._system_parameters.file_size_limit = file_size_limit
        return self

    def image_file_size_limit(self, image_file_size_limit: int) -> SystemParametersBuilder:
        self._system_parameters.image_file_size_limit = image_file_size_limit
        return self

    def audio_file_size_limit(self, audio_file_size_limit: int) -> SystemParametersBuilder:
        self._system_parameters.audio_file_size_limit = audio_file_size_limit
        return self

    def video_file_size_limit(self, video_file_size_limit: int) -> SystemParametersBuilder:
        self._system_parameters.video_file_size_limit = video_file_size_limit
        return self


class AppParameters(BaseModel):
    """Application parameters configuration."""

    opening_statement: str | None = None
    suggested_questions: list[str] | None = None
    suggested_questions_after_answer: dict[str, bool] | None = None
    speech_to_text: dict[str, bool] | None = None
    text_to_speech: dict[str, Any] | None = None
    retriever_resource: dict[str, bool] | None = None
    annotation_reply: dict[str, bool] | None = None
    user_input_form: list[UserInputFormItem] | None = None
    file_upload: dict[str, FileUploadConfig] | None = None
    system_parameters: SystemParameters | None = None

    @staticmethod
    def builder() -> AppParametersBuilder:
        return AppParametersBuilder()


class AppParametersBuilder:
    def __init__(self):
        self._app_parameters = AppParameters()

    def build(self) -> AppParameters:
        return self._app_parameters

    def opening_statement(self, opening_statement: str) -> AppParametersBuilder:
        self._app_parameters.opening_statement = opening_statement
        return self

    def suggested_questions(self, suggested_questions: list[str]) -> AppParametersBuilder:
        self._app_parameters.suggested_questions = suggested_questions
        return self

    def suggested_questions_after_answer(self, enabled: bool) -> AppParametersBuilder:
        self._app_parameters.suggested_questions_after_answer = {"enabled": enabled}
        return self

    def speech_to_text(self, enabled: bool) -> AppParametersBuilder:
        self._app_parameters.speech_to_text = {"enabled": enabled}
        return self

    def text_to_speech(
        self, enabled: bool, voice: str | None = None, language: str | None = None, auto_play: AutoPlay | None = None
    ) -> AppParametersBuilder:
        config: dict[str, Any] = {"enabled": enabled}
        if voice is not None:
            config["voice"] = voice
        if language is not None:
            config["language"] = language
        if auto_play is not None:
            config["autoPlay"] = auto_play
        self._app_parameters.text_to_speech = config
        return self

    def retriever_resource(self, enabled: bool) -> AppParametersBuilder:
        self._app_parameters.retriever_resource = {"enabled": enabled}
        return self

    def annotation_reply(self, enabled: bool) -> AppParametersBuilder:
        self._app_parameters.annotation_reply = {"enabled": enabled}
        return self

    def user_input_form(self, user_input_form: list[UserInputFormItem]) -> AppParametersBuilder:
        self._app_parameters.user_input_form = user_input_form
        return self

    def file_upload(self, image: FileUploadConfig | None = None) -> AppParametersBuilder:
        config: dict[str, FileUploadConfig] = {}
        if image is not None:
            config["image"] = image
        self._app_parameters.file_upload = config
        return self

    def system_parameters(self, system_parameters: SystemParameters) -> AppParametersBuilder:
        self._app_parameters.system_parameters = system_parameters
        return self
