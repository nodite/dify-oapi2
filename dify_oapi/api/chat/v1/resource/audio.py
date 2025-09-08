from dify_oapi.core.http.transport import ATransport, Transport
from dify_oapi.core.model.config import Config
from dify_oapi.core.model.request_option import RequestOption

from ..model.audio_to_text_request import AudioToTextRequest
from ..model.audio_to_text_response import AudioToTextResponse
from ..model.text_to_audio_request import TextToAudioRequest


class Audio:
    def __init__(self, config: Config) -> None:
        self.config: Config = config

    def to_text(self, request: AudioToTextRequest, option: RequestOption | None = None) -> AudioToTextResponse:
        return Transport.execute(self.config, request, unmarshal_as=AudioToTextResponse, option=option)

    async def ato_text(self, request: AudioToTextRequest, option: RequestOption | None = None) -> AudioToTextResponse:
        return await ATransport.aexecute(self.config, request, unmarshal_as=AudioToTextResponse, option=option)

    def to_audio(self, request: TextToAudioRequest, option: RequestOption | None = None) -> bytes:
        response = Transport.execute(self.config, request, option=option)
        if hasattr(response, "content") and response.content is not None:
            return bytes(response.content)
        return b""

    async def ato_audio(self, request: TextToAudioRequest, option: RequestOption | None = None) -> bytes:
        response = await ATransport.aexecute(self.config, request, option=option)
        if hasattr(response, "content") and response.content is not None:
            return bytes(response.content)
        return b""
