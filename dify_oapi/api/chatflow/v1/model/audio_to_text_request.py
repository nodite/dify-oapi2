from io import BytesIO

from dify_oapi.core.enum import HttpMethod
from dify_oapi.core.model.base_request import BaseRequest


class AudioToTextRequest(BaseRequest):
    def __init__(self):
        super().__init__()
        self.file: BytesIO | None = None
        self.user: str | None = None

    @staticmethod
    def builder() -> "AudioToTextRequestBuilder":
        return AudioToTextRequestBuilder()


class AudioToTextRequestBuilder:
    def __init__(self):
        audio_to_text_request = AudioToTextRequest()
        audio_to_text_request.http_method = HttpMethod.POST
        audio_to_text_request.uri = "/v1/audio-to-text"
        self._audio_to_text_request = audio_to_text_request

    def build(self) -> AudioToTextRequest:
        return self._audio_to_text_request

    def file(self, file: BytesIO, file_name: str | None = None) -> "AudioToTextRequestBuilder":
        self._audio_to_text_request.file = file
        file_name = file_name or "audio"
        self._audio_to_text_request.files = {"file": (file_name, file)}
        return self

    def user(self, user: str) -> "AudioToTextRequestBuilder":
        self._audio_to_text_request.user = user
        self._audio_to_text_request.body = {"user": user}
        return self
