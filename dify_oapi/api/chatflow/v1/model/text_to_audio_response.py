from dify_oapi.core.model.base_response import BaseResponse


class TextToAudioResponse(BaseResponse):
    # Binary audio data response - handled by Transport layer
    # Response content type: audio/wav or audio/mp3
    pass

    @staticmethod
    def builder() -> "TextToAudioResponseBuilder":
        return TextToAudioResponseBuilder()


class TextToAudioResponseBuilder:
    def __init__(self):
        self._text_to_audio_response = TextToAudioResponse()

    def build(self) -> TextToAudioResponse:
        return self._text_to_audio_response
