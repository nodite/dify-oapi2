from pydantic import BaseModel

from .chatflow_types import AutoPlay, TransferMethod
from .user_input_form import UserInputFormItem


class SuggestedQuestionsAfterAnswer(BaseModel):
    enabled: bool

    @staticmethod
    def builder() -> "SuggestedQuestionsAfterAnswerBuilder":
        return SuggestedQuestionsAfterAnswerBuilder()


class SuggestedQuestionsAfterAnswerBuilder:
    def __init__(self):
        self._suggested_questions_after_answer = SuggestedQuestionsAfterAnswer(enabled=False)

    def build(self) -> SuggestedQuestionsAfterAnswer:
        return self._suggested_questions_after_answer

    def enabled(self, enabled: bool) -> "SuggestedQuestionsAfterAnswerBuilder":
        self._suggested_questions_after_answer.enabled = enabled
        return self


class SpeechToText(BaseModel):
    enabled: bool

    @staticmethod
    def builder() -> "SpeechToTextBuilder":
        return SpeechToTextBuilder()


class SpeechToTextBuilder:
    def __init__(self):
        self._speech_to_text = SpeechToText(enabled=False)

    def build(self) -> SpeechToText:
        return self._speech_to_text

    def enabled(self, enabled: bool) -> "SpeechToTextBuilder":
        self._speech_to_text.enabled = enabled
        return self


class TextToSpeech(BaseModel):
    enabled: bool
    voice: str | None = None
    language: str | None = None
    auto_play: AutoPlay | None = None

    @staticmethod
    def builder() -> "TextToSpeechBuilder":
        return TextToSpeechBuilder()


class TextToSpeechBuilder:
    def __init__(self):
        self._text_to_speech = TextToSpeech(enabled=False)

    def build(self) -> TextToSpeech:
        return self._text_to_speech

    def enabled(self, enabled: bool) -> "TextToSpeechBuilder":
        self._text_to_speech.enabled = enabled
        return self

    def voice(self, voice: str) -> "TextToSpeechBuilder":
        self._text_to_speech.voice = voice
        return self

    def language(self, language: str) -> "TextToSpeechBuilder":
        self._text_to_speech.language = language
        return self

    def auto_play(self, auto_play: AutoPlay) -> "TextToSpeechBuilder":
        self._text_to_speech.auto_play = auto_play
        return self


class RetrieverResource(BaseModel):
    enabled: bool

    @staticmethod
    def builder() -> "RetrieverResourceBuilder":
        return RetrieverResourceBuilder()


class RetrieverResourceBuilder:
    def __init__(self):
        self._retriever_resource = RetrieverResource(enabled=False)

    def build(self) -> RetrieverResource:
        return self._retriever_resource

    def enabled(self, enabled: bool) -> "RetrieverResourceBuilder":
        self._retriever_resource.enabled = enabled
        return self


class AnnotationReply(BaseModel):
    enabled: bool

    @staticmethod
    def builder() -> "AnnotationReplyBuilder":
        return AnnotationReplyBuilder()


class AnnotationReplyBuilder:
    def __init__(self):
        self._annotation_reply = AnnotationReply(enabled=False)

    def build(self) -> AnnotationReply:
        return self._annotation_reply

    def enabled(self, enabled: bool) -> "AnnotationReplyBuilder":
        self._annotation_reply.enabled = enabled
        return self


class ImageUpload(BaseModel):
    enabled: bool
    number_limits: int | None = None
    detail: str | None = None
    transfer_methods: list[TransferMethod] | None = None

    @staticmethod
    def builder() -> "ImageUploadBuilder":
        return ImageUploadBuilder()


class ImageUploadBuilder:
    def __init__(self):
        self._image_upload = ImageUpload(enabled=False)

    def build(self) -> ImageUpload:
        return self._image_upload

    def enabled(self, enabled: bool) -> "ImageUploadBuilder":
        self._image_upload.enabled = enabled
        return self

    def number_limits(self, number_limits: int) -> "ImageUploadBuilder":
        self._image_upload.number_limits = number_limits
        return self

    def detail(self, detail: str) -> "ImageUploadBuilder":
        self._image_upload.detail = detail
        return self

    def transfer_methods(self, transfer_methods: list[TransferMethod]) -> "ImageUploadBuilder":
        self._image_upload.transfer_methods = transfer_methods
        return self


class FileUpload(BaseModel):
    image: ImageUpload | None = None

    @staticmethod
    def builder() -> "FileUploadBuilder":
        return FileUploadBuilder()


class FileUploadBuilder:
    def __init__(self):
        self._file_upload = FileUpload()

    def build(self) -> FileUpload:
        return self._file_upload

    def image(self, image: ImageUpload) -> "FileUploadBuilder":
        self._file_upload.image = image
        return self


class SystemParameters(BaseModel):
    file_size_limit: int | None = None
    image_file_size_limit: int | None = None
    audio_file_size_limit: int | None = None
    video_file_size_limit: int | None = None

    @staticmethod
    def builder() -> "SystemParametersBuilder":
        return SystemParametersBuilder()


class SystemParametersBuilder:
    def __init__(self):
        self._system_parameters = SystemParameters()

    def build(self) -> SystemParameters:
        return self._system_parameters

    def file_size_limit(self, file_size_limit: int) -> "SystemParametersBuilder":
        self._system_parameters.file_size_limit = file_size_limit
        return self

    def image_file_size_limit(self, image_file_size_limit: int) -> "SystemParametersBuilder":
        self._system_parameters.image_file_size_limit = image_file_size_limit
        return self

    def audio_file_size_limit(self, audio_file_size_limit: int) -> "SystemParametersBuilder":
        self._system_parameters.audio_file_size_limit = audio_file_size_limit
        return self

    def video_file_size_limit(self, video_file_size_limit: int) -> "SystemParametersBuilder":
        self._system_parameters.video_file_size_limit = video_file_size_limit
        return self


class AppParameters(BaseModel):
    opening_statement: str | None = None
    suggested_questions: list[str] | None = None
    suggested_questions_after_answer: SuggestedQuestionsAfterAnswer | None = None
    speech_to_text: SpeechToText | None = None
    text_to_speech: TextToSpeech | None = None
    retriever_resource: RetrieverResource | None = None
    annotation_reply: AnnotationReply | None = None
    user_input_form: list[UserInputFormItem] | None = None
    file_upload: FileUpload | None = None
    system_parameters: SystemParameters | None = None

    @staticmethod
    def builder() -> "AppParametersBuilder":
        return AppParametersBuilder()


class AppParametersBuilder:
    def __init__(self):
        self._app_parameters = AppParameters()

    def build(self) -> AppParameters:
        return self._app_parameters

    def opening_statement(self, opening_statement: str) -> "AppParametersBuilder":
        self._app_parameters.opening_statement = opening_statement
        return self

    def suggested_questions(self, suggested_questions: list[str]) -> "AppParametersBuilder":
        self._app_parameters.suggested_questions = suggested_questions
        return self

    def suggested_questions_after_answer(
        self, suggested_questions_after_answer: SuggestedQuestionsAfterAnswer
    ) -> "AppParametersBuilder":
        self._app_parameters.suggested_questions_after_answer = suggested_questions_after_answer
        return self

    def speech_to_text(self, speech_to_text: SpeechToText) -> "AppParametersBuilder":
        self._app_parameters.speech_to_text = speech_to_text
        return self

    def text_to_speech(self, text_to_speech: TextToSpeech) -> "AppParametersBuilder":
        self._app_parameters.text_to_speech = text_to_speech
        return self

    def retriever_resource(self, retriever_resource: RetrieverResource) -> "AppParametersBuilder":
        self._app_parameters.retriever_resource = retriever_resource
        return self

    def annotation_reply(self, annotation_reply: AnnotationReply) -> "AppParametersBuilder":
        self._app_parameters.annotation_reply = annotation_reply
        return self

    def user_input_form(self, user_input_form: list[UserInputFormItem]) -> "AppParametersBuilder":
        self._app_parameters.user_input_form = user_input_form
        return self

    def file_upload(self, file_upload: FileUpload) -> "AppParametersBuilder":
        self._app_parameters.file_upload = file_upload
        return self

    def system_parameters(self, system_parameters: SystemParameters) -> "AppParametersBuilder":
        self._app_parameters.system_parameters = system_parameters
        return self
