from dify_oapi.core.model.base_response import BaseResponse


class AudioToTextResponse(BaseResponse):
    text: str | None = None

    @staticmethod
    def builder() -> "AudioToTextResponseBuilder":
        return AudioToTextResponseBuilder()


class AudioToTextResponseBuilder:
    def __init__(self):
        self._audio_to_text_response = AudioToTextResponse()

    def build(self) -> AudioToTextResponse:
        return self._audio_to_text_response

    def text(self, text: str) -> "AudioToTextResponseBuilder":
        self._audio_to_text_response.text = text
        return self
