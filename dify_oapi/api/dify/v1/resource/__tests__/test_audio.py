import io

import httpx
import pytest
import respx

from dify_oapi.api.dify.v1.model.audio_to_text_request import AudioToTextRequest
from dify_oapi.api.dify.v1.model.text_to_audio_request import TextToAudioRequest
from dify_oapi.api.dify.v1.model.text_to_audio_request_body import TextToAudioRequestBody
from dify_oapi.api.dify.v1.resource.audio import Audio


class TestAudio:
    @pytest.fixture(autouse=True)
    def setup(self, config, request_option):
        self.resource = Audio(config)
        self.option = request_option

    @respx.mock
    def test_to_text(self):
        route = respx.post("https://api.dify.ai/v1/audio-to-text").mock(
            return_value=httpx.Response(200, json={"text": "hello world"})
        )
        file_content = io.BytesIO(b"fake audio data")
        request = AudioToTextRequest.builder().file(file_content, "audio.mp3").build()
        result = self.resource.to_text(request, self.option)
        assert result.text == "hello world"
        assert route.calls.last.request.headers["Authorization"] == "Bearer test-key"

    @respx.mock
    def test_from_text(self):
        route = respx.post("https://api.dify.ai/v1/text-to-audio").mock(
            return_value=httpx.Response(200, content=b"fake audio bytes")
        )
        body = TextToAudioRequestBody.builder().text("hello world").user("u1").build()
        request = TextToAudioRequest.builder().request_body(body).build()
        result = self.resource.from_text(request, self.option)
        assert result is not None
        assert route.calls.last.request.headers["Authorization"] == "Bearer test-key"
