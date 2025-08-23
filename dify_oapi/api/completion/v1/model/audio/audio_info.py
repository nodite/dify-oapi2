from __future__ import annotations

from pydantic import BaseModel


class AudioInfo(BaseModel):
    content_type: str | None = None
    data: bytes | None = None

    @staticmethod
    def builder() -> AudioInfoBuilder:
        return AudioInfoBuilder()


class AudioInfoBuilder:
    def __init__(self):
        self._audio_info = AudioInfo()

    def build(self) -> AudioInfo:
        return self._audio_info

    def content_type(self, content_type: str) -> AudioInfoBuilder:
        self._audio_info.content_type = content_type
        return self

    def data(self, data: bytes) -> AudioInfoBuilder:
        self._audio_info.data = data
        return self
