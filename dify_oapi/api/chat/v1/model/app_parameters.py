from __future__ import annotations

from pydantic import BaseModel

from .chat_types import TransferMethod


class TextInputConfig(BaseModel):
    """Text input configuration."""

    label: str
    variable: str
    required: bool
    default: str | None = None


class ParagraphConfig(BaseModel):
    """Paragraph input configuration."""

    label: str
    variable: str
    required: bool
    default: str | None = None


class SelectConfig(BaseModel):
    """Select input configuration."""

    label: str
    variable: str
    required: bool
    options: list[str]
    default: str | None = None


class UserInputFormItem(BaseModel):
    """User input form item configuration."""

    # Text input configuration
    text_input: TextInputConfig | None = None
    # Paragraph input configuration
    paragraph: ParagraphConfig | None = None
    # Select input configuration
    select: SelectConfig | None = None

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
        self._user_input_form_item.text_input = TextInputConfig(
            label=label, variable=variable, required=required, default=default
        )
        return self

    def paragraph(
        self, label: str, variable: str, required: bool, default: str | None = None
    ) -> UserInputFormItemBuilder:
        self._user_input_form_item.paragraph = ParagraphConfig(
            label=label, variable=variable, required=required, default=default
        )
        return self

    def select(
        self, label: str, variable: str, required: bool, options: list[str], default: str | None = None
    ) -> UserInputFormItemBuilder:
        self._user_input_form_item.select = SelectConfig(
            label=label, variable=variable, required=required, options=options, default=default
        )
        return self


class ImageUploadConfig(BaseModel):
    """Image upload configuration."""

    enabled: bool | None = None
    number_limits: int | None = None
    transfer_methods: list[TransferMethod] | None = None

    @staticmethod
    def builder() -> ImageUploadConfigBuilder:
        return ImageUploadConfigBuilder()


class ImageUploadConfigBuilder:
    def __init__(self):
        self._image_upload_config = ImageUploadConfig()

    def build(self) -> ImageUploadConfig:
        return self._image_upload_config

    def enabled(self, enabled: bool) -> ImageUploadConfigBuilder:
        self._image_upload_config.enabled = enabled
        return self

    def number_limits(self, number_limits: int) -> ImageUploadConfigBuilder:
        self._image_upload_config.number_limits = number_limits
        return self

    def transfer_methods(self, transfer_methods: list[TransferMethod]) -> ImageUploadConfigBuilder:
        self._image_upload_config.transfer_methods = transfer_methods
        return self


class FileUploadSystemConfig(BaseModel):
    """File upload system configuration."""

    file_size_limit: int | None = None
    batch_count_limit: int | None = None
    image_file_size_limit: int | None = None
    video_file_size_limit: int | None = None
    audio_file_size_limit: int | None = None
    workflow_file_upload_limit: int | None = None

    @staticmethod
    def builder() -> FileUploadSystemConfigBuilder:
        return FileUploadSystemConfigBuilder()


class FileUploadSystemConfigBuilder:
    def __init__(self):
        self._config = FileUploadSystemConfig()

    def build(self) -> FileUploadSystemConfig:
        return self._config

    def file_size_limit(self, file_size_limit: int) -> FileUploadSystemConfigBuilder:
        self._config.file_size_limit = file_size_limit
        return self

    def batch_count_limit(self, batch_count_limit: int) -> FileUploadSystemConfigBuilder:
        self._config.batch_count_limit = batch_count_limit
        return self

    def image_file_size_limit(self, image_file_size_limit: int) -> FileUploadSystemConfigBuilder:
        self._config.image_file_size_limit = image_file_size_limit
        return self

    def video_file_size_limit(self, video_file_size_limit: int) -> FileUploadSystemConfigBuilder:
        self._config.video_file_size_limit = video_file_size_limit
        return self

    def audio_file_size_limit(self, audio_file_size_limit: int) -> FileUploadSystemConfigBuilder:
        self._config.audio_file_size_limit = audio_file_size_limit
        return self

    def workflow_file_upload_limit(self, workflow_file_upload_limit: int) -> FileUploadSystemConfigBuilder:
        self._config.workflow_file_upload_limit = workflow_file_upload_limit
        return self


class FileUploadConfig(BaseModel):
    """Complete file upload configuration."""

    image: ImageUploadConfig | None = None
    enabled: bool | None = None
    allowed_file_types: list[str] | None = None
    allowed_file_extensions: list[str] | None = None
    allowed_file_upload_methods: list[TransferMethod] | None = None
    number_limits: int | None = None
    file_upload_config: FileUploadSystemConfig | None = None

    @staticmethod
    def builder() -> FileUploadConfigBuilder:
        return FileUploadConfigBuilder()


class FileUploadConfigBuilder:
    def __init__(self):
        self._file_upload_config = FileUploadConfig()

    def build(self) -> FileUploadConfig:
        return self._file_upload_config

    def image(self, image: ImageUploadConfig) -> FileUploadConfigBuilder:
        self._file_upload_config.image = image
        return self

    def enabled(self, enabled: bool) -> FileUploadConfigBuilder:
        self._file_upload_config.enabled = enabled
        return self

    def allowed_file_types(self, allowed_file_types: list[str]) -> FileUploadConfigBuilder:
        self._file_upload_config.allowed_file_types = allowed_file_types
        return self

    def allowed_file_extensions(self, allowed_file_extensions: list[str]) -> FileUploadConfigBuilder:
        self._file_upload_config.allowed_file_extensions = allowed_file_extensions
        return self

    def allowed_file_upload_methods(self, allowed_file_upload_methods: list[TransferMethod]) -> FileUploadConfigBuilder:
        self._file_upload_config.allowed_file_upload_methods = allowed_file_upload_methods
        return self

    def number_limits(self, number_limits: int) -> FileUploadConfigBuilder:
        self._file_upload_config.number_limits = number_limits
        return self

    def file_upload_config(self, file_upload_config: FileUploadSystemConfig) -> FileUploadConfigBuilder:
        self._file_upload_config.file_upload_config = file_upload_config
        return self


class SuggestedQuestionsAfterAnswerConfig(BaseModel):
    """Suggested questions after answer configuration."""

    enabled: bool | None = None

    @staticmethod
    def builder() -> SuggestedQuestionsAfterAnswerConfigBuilder:
        return SuggestedQuestionsAfterAnswerConfigBuilder()


class SuggestedQuestionsAfterAnswerConfigBuilder:
    def __init__(self):
        self._config = SuggestedQuestionsAfterAnswerConfig()

    def build(self) -> SuggestedQuestionsAfterAnswerConfig:
        return self._config

    def enabled(self, enabled: bool) -> SuggestedQuestionsAfterAnswerConfigBuilder:
        self._config.enabled = enabled
        return self


class SpeechToTextConfig(BaseModel):
    """Speech to text configuration."""

    enabled: bool | None = None

    @staticmethod
    def builder() -> SpeechToTextConfigBuilder:
        return SpeechToTextConfigBuilder()


class SpeechToTextConfigBuilder:
    def __init__(self):
        self._config = SpeechToTextConfig()

    def build(self) -> SpeechToTextConfig:
        return self._config

    def enabled(self, enabled: bool) -> SpeechToTextConfigBuilder:
        self._config.enabled = enabled
        return self


class TextToSpeechConfig(BaseModel):
    """Text to speech configuration."""

    enabled: bool | None = None
    voice: str | None = None
    language: str | None = None

    @staticmethod
    def builder() -> TextToSpeechConfigBuilder:
        return TextToSpeechConfigBuilder()


class TextToSpeechConfigBuilder:
    def __init__(self):
        self._config = TextToSpeechConfig()

    def build(self) -> TextToSpeechConfig:
        return self._config

    def enabled(self, enabled: bool) -> TextToSpeechConfigBuilder:
        self._config.enabled = enabled
        return self

    def voice(self, voice: str) -> TextToSpeechConfigBuilder:
        self._config.voice = voice
        return self

    def language(self, language: str) -> TextToSpeechConfigBuilder:
        self._config.language = language
        return self


class RetrieverResourceConfig(BaseModel):
    """Retriever resource configuration."""

    enabled: bool | None = None

    @staticmethod
    def builder() -> RetrieverResourceConfigBuilder:
        return RetrieverResourceConfigBuilder()


class RetrieverResourceConfigBuilder:
    def __init__(self):
        self._config = RetrieverResourceConfig()

    def build(self) -> RetrieverResourceConfig:
        return self._config

    def enabled(self, enabled: bool) -> RetrieverResourceConfigBuilder:
        self._config.enabled = enabled
        return self


class AnnotationReplyConfig(BaseModel):
    """Annotation reply configuration."""

    enabled: bool | None = None

    @staticmethod
    def builder() -> AnnotationReplyConfigBuilder:
        return AnnotationReplyConfigBuilder()


class AnnotationReplyConfigBuilder:
    def __init__(self):
        self._config = AnnotationReplyConfig()

    def build(self) -> AnnotationReplyConfig:
        return self._config

    def enabled(self, enabled: bool) -> AnnotationReplyConfigBuilder:
        self._config.enabled = enabled
        return self


class MoreLikeThisConfig(BaseModel):
    """More like this configuration."""

    enabled: bool | None = None

    @staticmethod
    def builder() -> MoreLikeThisConfigBuilder:
        return MoreLikeThisConfigBuilder()


class MoreLikeThisConfigBuilder:
    def __init__(self):
        self._config = MoreLikeThisConfig()

    def build(self) -> MoreLikeThisConfig:
        return self._config

    def enabled(self, enabled: bool) -> MoreLikeThisConfigBuilder:
        self._config.enabled = enabled
        return self


class SensitiveWordAvoidanceConfig(BaseModel):
    """Sensitive word avoidance configuration."""

    enabled: bool | None = None

    @staticmethod
    def builder() -> SensitiveWordAvoidanceConfigBuilder:
        return SensitiveWordAvoidanceConfigBuilder()


class SensitiveWordAvoidanceConfigBuilder:
    def __init__(self):
        self._config = SensitiveWordAvoidanceConfig()

    def build(self) -> SensitiveWordAvoidanceConfig:
        return self._config

    def enabled(self, enabled: bool) -> SensitiveWordAvoidanceConfigBuilder:
        self._config.enabled = enabled
        return self


class SystemParameters(BaseModel):
    """System parameters configuration."""

    image_file_size_limit: int | None = None
    video_file_size_limit: int | None = None
    audio_file_size_limit: int | None = None
    file_size_limit: int | None = None
    workflow_file_upload_limit: int | None = None

    @staticmethod
    def builder() -> SystemParametersBuilder:
        return SystemParametersBuilder()


class SystemParametersBuilder:
    def __init__(self):
        self._system_parameters = SystemParameters()

    def build(self) -> SystemParameters:
        return self._system_parameters

    def image_file_size_limit(self, image_file_size_limit: int) -> SystemParametersBuilder:
        self._system_parameters.image_file_size_limit = image_file_size_limit
        return self

    def video_file_size_limit(self, video_file_size_limit: int) -> SystemParametersBuilder:
        self._system_parameters.video_file_size_limit = video_file_size_limit
        return self

    def audio_file_size_limit(self, audio_file_size_limit: int) -> SystemParametersBuilder:
        self._system_parameters.audio_file_size_limit = audio_file_size_limit
        return self

    def file_size_limit(self, file_size_limit: int) -> SystemParametersBuilder:
        self._system_parameters.file_size_limit = file_size_limit
        return self

    def workflow_file_upload_limit(self, workflow_file_upload_limit: int) -> SystemParametersBuilder:
        self._system_parameters.workflow_file_upload_limit = workflow_file_upload_limit
        return self


class AppParameters(BaseModel):
    """Application parameters configuration."""

    opening_statement: str | None = None
    suggested_questions: list[str] | None = None
    suggested_questions_after_answer: SuggestedQuestionsAfterAnswerConfig | None = None
    speech_to_text: SpeechToTextConfig | None = None
    text_to_speech: TextToSpeechConfig | None = None
    retriever_resource: RetrieverResourceConfig | None = None
    annotation_reply: AnnotationReplyConfig | None = None
    more_like_this: MoreLikeThisConfig | None = None
    user_input_form: list[UserInputFormItem] | None = None
    sensitive_word_avoidance: SensitiveWordAvoidanceConfig | None = None
    file_upload: FileUploadConfig | None = None
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

    def suggested_questions_after_answer(self, config: SuggestedQuestionsAfterAnswerConfig) -> AppParametersBuilder:
        self._app_parameters.suggested_questions_after_answer = config
        return self

    def speech_to_text(self, config: SpeechToTextConfig) -> AppParametersBuilder:
        self._app_parameters.speech_to_text = config
        return self

    def text_to_speech(self, config: TextToSpeechConfig) -> AppParametersBuilder:
        self._app_parameters.text_to_speech = config
        return self

    def retriever_resource(self, config: RetrieverResourceConfig) -> AppParametersBuilder:
        self._app_parameters.retriever_resource = config
        return self

    def annotation_reply(self, config: AnnotationReplyConfig) -> AppParametersBuilder:
        self._app_parameters.annotation_reply = config
        return self

    def more_like_this(self, config: MoreLikeThisConfig) -> AppParametersBuilder:
        self._app_parameters.more_like_this = config
        return self

    def user_input_form(self, user_input_form: list[UserInputFormItem]) -> AppParametersBuilder:
        self._app_parameters.user_input_form = user_input_form
        return self

    def sensitive_word_avoidance(self, config: SensitiveWordAvoidanceConfig) -> AppParametersBuilder:
        self._app_parameters.sensitive_word_avoidance = config
        return self

    def file_upload(self, config: FileUploadConfig) -> AppParametersBuilder:
        self._app_parameters.file_upload = config
        return self

    def system_parameters(self, system_parameters: SystemParameters) -> AppParametersBuilder:
        self._app_parameters.system_parameters = system_parameters
        return self
