from pydantic import BaseModel


class TextToAudioRequestBody(BaseModel):
    message_id: str | None = None
    text: str | None = None
    user: str | None = None
    streaming: bool | None = None

    @staticmethod
    def builder() -> "TextToAudioRequestBodyBuilder":
        return TextToAudioRequestBodyBuilder()


class TextToAudioRequestBodyBuilder:
    def __init__(self):
        self._text_to_audio_request_body = TextToAudioRequestBody()

    def build(self) -> TextToAudioRequestBody:
        return self._text_to_audio_request_body

    def message_id(self, message_id: str) -> "TextToAudioRequestBodyBuilder":
        self._text_to_audio_request_body.message_id = message_id
        return self

    def text(self, text: str) -> "TextToAudioRequestBodyBuilder":
        self._text_to_audio_request_body.text = text
        return self

    def user(self, user: str) -> "TextToAudioRequestBodyBuilder":
        self._text_to_audio_request_body.user = user
        return self

    def streaming(self, streaming: bool) -> "TextToAudioRequestBodyBuilder":
        self._text_to_audio_request_body.streaming = streaming
        return self
