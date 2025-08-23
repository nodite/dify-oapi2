from __future__ import annotations

from pydantic import BaseModel

from .file_upload_config import FileUploadConfig
from .system_parameters import SystemParameters
from .user_input_form import UserInputForm


class ParametersInfo(BaseModel):
    opening_statement: str | None = None
    suggested_questions: list[str] | None = None
    suggested_questions_after_answer: dict | None = None
    speech_to_text: dict | None = None
    retriever_resource: dict | None = None
    annotation_reply: dict | None = None
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

    def opening_statement(self, opening_statement: str) -> ParametersInfoBuilder:
        self._parameters_info.opening_statement = opening_statement
        return self

    def suggested_questions(self, suggested_questions: list[str]) -> ParametersInfoBuilder:
        self._parameters_info.suggested_questions = suggested_questions
        return self

    def suggested_questions_after_answer(self, suggested_questions_after_answer: dict) -> ParametersInfoBuilder:
        self._parameters_info.suggested_questions_after_answer = suggested_questions_after_answer
        return self

    def speech_to_text(self, speech_to_text: dict) -> ParametersInfoBuilder:
        self._parameters_info.speech_to_text = speech_to_text
        return self

    def retriever_resource(self, retriever_resource: dict) -> ParametersInfoBuilder:
        self._parameters_info.retriever_resource = retriever_resource
        return self

    def annotation_reply(self, annotation_reply: dict) -> ParametersInfoBuilder:
        self._parameters_info.annotation_reply = annotation_reply
        return self

    def user_input_form(self, user_input_form: list[UserInputForm]) -> ParametersInfoBuilder:
        self._parameters_info.user_input_form = user_input_form
        return self

    def file_upload(self, file_upload: FileUploadConfig) -> ParametersInfoBuilder:
        self._parameters_info.file_upload = file_upload
        return self

    def system_parameters(self, system_parameters: SystemParameters) -> ParametersInfoBuilder:
        self._parameters_info.system_parameters = system_parameters
        return self
