from __future__ import annotations

from pydantic import BaseModel

from .file_upload_config import FileUploadConfig
from .system_parameters import SystemParameters
from .user_input_form import UserInputForm


class ParametersInfo(BaseModel):
    user_input_form: list[UserInputForm] | None = None
    file_upload: FileUploadConfig | None = None
    system_parameters: SystemParameters | None = None

    @staticmethod
    def builder() -> ParametersInfoBuilder:
        return ParametersInfoBuilder()


class ParametersInfoBuilder:
    def __init__(self):
        self._parameters_info = ParametersInfo()

    def build(self) -> ParametersInfo:
        return self._parameters_info

    def user_input_form(self, user_input_form: list[UserInputForm]) -> ParametersInfoBuilder:
        self._parameters_info.user_input_form = user_input_form
        return self

    def file_upload(self, file_upload: FileUploadConfig) -> ParametersInfoBuilder:
        self._parameters_info.file_upload = file_upload
        return self

    def system_parameters(self, system_parameters: SystemParameters) -> ParametersInfoBuilder:
        self._parameters_info.system_parameters = system_parameters
        return self
