from __future__ import annotations

from pydantic import BaseModel


class UserInputForm(BaseModel):
    label: str | None = None
    variable: str | None = None
    required: bool | None = None
    default: str | None = None
    options: list[str] | None = None

    @staticmethod
    def builder() -> UserInputFormBuilder:
        return UserInputFormBuilder()


class UserInputFormBuilder:
    def __init__(self):
        self._user_input_form = UserInputForm()

    def build(self) -> UserInputForm:
        return self._user_input_form

    def label(self, label: str) -> UserInputFormBuilder:
        self._user_input_form.label = label
        return self

    def variable(self, variable: str) -> UserInputFormBuilder:
        self._user_input_form.variable = variable
        return self

    def required(self, required: bool) -> UserInputFormBuilder:
        self._user_input_form.required = required
        return self

    def default(self, default: str) -> UserInputFormBuilder:
        self._user_input_form.default = default
        return self

    def options(self, options: list[str]) -> UserInputFormBuilder:
        self._user_input_form.options = options
        return self
