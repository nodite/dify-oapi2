from dify_oapi.api.chatflow.v1.model.audio_to_text_request import AudioToTextRequest
from dify_oapi.api.chatflow.v1.model.audio_to_text_response import AudioToTextResponse
from dify_oapi.api.chatflow.v1.model.text_to_audio_request import TextToAudioRequest
from dify_oapi.api.chatflow.v1.model.text_to_audio_response import TextToAudioResponse
from dify_oapi.core.http.transport.async_transport import ATransport
from dify_oapi.core.http.transport.sync_transport import Transport
from dify_oapi.core.model.config import Config
from dify_oapi.core.model.request_option import RequestOption


class TTS:
    def __init__(self, config: Config):
        self.config = config

    def speech_to_text(self, request: AudioToTextRequest, request_option: RequestOption) -> AudioToTextResponse:
        """Convert audio to text (sync)"""
        return Transport.execute(self.config, request, unmarshal_as=AudioToTextResponse, option=request_option)

    async def aspeech_to_text(self, request: AudioToTextRequest, request_option: RequestOption) -> AudioToTextResponse:
        """Convert audio to text (async)"""
        return await ATransport.aexecute(self.config, request, unmarshal_as=AudioToTextResponse, option=request_option)

    def text_to_audio(self, request: TextToAudioRequest, request_option: RequestOption) -> TextToAudioResponse:
        """Convert text to audio (sync)"""
        return Transport.execute(self.config, request, unmarshal_as=TextToAudioResponse, option=request_option)

    async def atext_to_audio(self, request: TextToAudioRequest, request_option: RequestOption) -> TextToAudioResponse:
        """Convert text to audio (async)"""
        return await ATransport.aexecute(self.config, request, unmarshal_as=TextToAudioResponse, option=request_option)
