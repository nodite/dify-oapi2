from dify_oapi.core.http.transport import ATransport, Transport
from dify_oapi.core.model.config import Config
from dify_oapi.core.model.request_option import RequestOption

from ..model.audio_to_text_request import AudioToTextRequest
from ..model.audio_to_text_response import AudioToTextResponse
from ..model.text_to_audio_request import TextToAudioRequest
from ..model.text_to_audio_response import TextToAudioResponse


class Audio:
    def __init__(self, config: Config) -> None:
        self.config: Config = config

    def to_text(self, request: AudioToTextRequest, option: RequestOption | None = None) -> AudioToTextResponse:
        """Convert audio to text (speech-to-text)"""
        return Transport.execute(self.config, request, unmarshal_as=AudioToTextResponse, option=option)

    async def ato_text(self, request: AudioToTextRequest, option: RequestOption | None = None) -> AudioToTextResponse:
        """Convert audio to text (speech-to-text) - async version"""
        return await ATransport.aexecute(self.config, request, unmarshal_as=AudioToTextResponse, option=option)

    def from_text(self, request: TextToAudioRequest, option: RequestOption | None = None) -> TextToAudioResponse:
        """Convert text to audio (text-to-speech)"""
        return Transport.execute(self.config, request, unmarshal_as=TextToAudioResponse, option=option)

    async def afrom_text(self, request: TextToAudioRequest, option: RequestOption | None = None) -> TextToAudioResponse:
        """Convert text to audio (text-to-speech) - async version"""
        return await ATransport.aexecute(self.config, request, unmarshal_as=TextToAudioResponse, option=option)
