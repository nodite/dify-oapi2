from __future__ import annotations

from dify_oapi.core.model.base_response import BaseResponse

from .audio_info import AudioInfo


class TextToAudioResponse(AudioInfo, BaseResponse):
    pass
