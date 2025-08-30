from __future__ import annotations

from pydantic import BaseModel


class SystemParameters(BaseModel):
    file_size_limit: int | None = None
    image_file_size_limit: int | None = None
    audio_file_size_limit: int | None = None
    video_file_size_limit: int | None = None

    @staticmethod
    def builder() -> SystemParametersBuilder:
        return SystemParametersBuilder()


class SystemParametersBuilder:
    def __init__(self):
        self._system_parameters = SystemParameters()

    def build(self) -> SystemParameters:
        return self._system_parameters

    def file_size_limit(self, file_size_limit: int) -> SystemParametersBuilder:
        self._system_parameters.file_size_limit = file_size_limit
        return self

    def image_file_size_limit(self, image_file_size_limit: int) -> SystemParametersBuilder:
        self._system_parameters.image_file_size_limit = image_file_size_limit
        return self

    def audio_file_size_limit(self, audio_file_size_limit: int) -> SystemParametersBuilder:
        self._system_parameters.audio_file_size_limit = audio_file_size_limit
        return self

    def video_file_size_limit(self, video_file_size_limit: int) -> SystemParametersBuilder:
        self._system_parameters.video_file_size_limit = video_file_size_limit
        return self
