from dify_oapi.core.http.transport import ATransport, Transport
from dify_oapi.core.model.config import Config
from dify_oapi.core.model.request_option import RequestOption

from ..model.audio_to_text_request import AudioToTextRequest
from ..model.audio_to_text_response import AudioToTextResponse
from ..model.text_to_audio_request import TextToAudioRequest
from ..model.text_to_audio_response import TextToAudioResponse


class TTS:
    def __init__(self, config: Config) -> None:
        self.config = config

    def speech_to_text(self, request: AudioToTextRequest, request_option: RequestOption) -> AudioToTextResponse:
        return Transport.execute(self.config, request, unmarshal_as=AudioToTextResponse, option=request_option)

    async def aspeech_to_text(self, request: AudioToTextRequest, request_option: RequestOption) -> AudioToTextResponse:
        return await ATransport.aexecute(self.config, request, unmarshal_as=AudioToTextResponse, option=request_option)

    def text_to_audio(self, request: TextToAudioRequest, request_option: RequestOption) -> TextToAudioResponse:
        return Transport.execute(self.config, request, unmarshal_as=TextToAudioResponse, option=request_option)

    async def atext_to_audio(self, request: TextToAudioRequest, request_option: RequestOption) -> TextToAudioResponse:
        return await ATransport.aexecute(self.config, request, unmarshal_as=TextToAudioResponse, option=request_option)
