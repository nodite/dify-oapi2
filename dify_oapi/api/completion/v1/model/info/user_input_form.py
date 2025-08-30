from __future__ import annotations

from pydantic import BaseModel, Field


class TextInputControl(BaseModel):
    """Text input control configuration."""

    label: str
    variable: str
    required: bool
    default: str | None = None


class ParagraphControl(BaseModel):
    """Paragraph (multi-line text) control configuration."""

    label: str
    variable: str
    required: bool
    default: str | None = None


class SelectControl(BaseModel):
    """Select (dropdown) control configuration."""

    label: str
    variable: str
    required: bool
    default: str | None = None
    options: list[str]


class UserInputForm(BaseModel):
    """User input form configuration supporting different control types."""

    # Use discriminated union to support different form control types
    text_input: TextInputControl | None = Field(default=None, alias="text-input")
    paragraph: ParagraphControl | None = None
    select: SelectControl | None = None

    @staticmethod
    def builder() -> UserInputFormBuilder:
        return UserInputFormBuilder()

    @staticmethod
    def text_input_builder() -> TextInputFormBuilder:
        return TextInputFormBuilder()

    @staticmethod
    def paragraph_builder() -> ParagraphFormBuilder:
        return ParagraphFormBuilder()

    @staticmethod
    def select_builder() -> SelectFormBuilder:
        return SelectFormBuilder()


class UserInputFormBuilder:
    def __init__(self):
        self._user_input_form = UserInputForm()

    def build(self) -> UserInputForm:
        return self._user_input_form

    def text_input(self, text_input: TextInputControl) -> UserInputFormBuilder:
        self._user_input_form.text_input = text_input
        return self

    def paragraph(self, paragraph: ParagraphControl) -> UserInputFormBuilder:
        self._user_input_form.paragraph = paragraph
        return self

    def select(self, select: SelectControl) -> UserInputFormBuilder:
        self._user_input_form.select = select
        return self


class TextInputFormBuilder:
    def __init__(self):
        self._control = TextInputControl(label="", variable="", required=False)

    def build(self) -> UserInputForm:
        form = UserInputForm()
        form.text_input = self._control
        return form

    def label(self, label: str) -> TextInputFormBuilder:
        self._control.label = label
        return self

    def variable(self, variable: str) -> TextInputFormBuilder:
        self._control.variable = variable
        return self

    def required(self, required: bool) -> TextInputFormBuilder:
        self._control.required = required
        return self

    def default(self, default: str) -> TextInputFormBuilder:
        self._control.default = default
        return self


class ParagraphFormBuilder:
    def __init__(self):
        self._control = ParagraphControl(label="", variable="", required=False)

    def build(self) -> UserInputForm:
        form = UserInputForm()
        form.paragraph = self._control
        return form

    def label(self, label: str) -> ParagraphFormBuilder:
        self._control.label = label
        return self

    def variable(self, variable: str) -> ParagraphFormBuilder:
        self._control.variable = variable
        return self

    def required(self, required: bool) -> ParagraphFormBuilder:
        self._control.required = required
        return self

    def default(self, default: str) -> ParagraphFormBuilder:
        self._control.default = default
        return self


class SelectFormBuilder:
    def __init__(self):
        self._control = SelectControl(label="", variable="", required=False, options=[])

    def build(self) -> UserInputForm:
        form = UserInputForm()
        form.select = self._control
        return form

    def label(self, label: str) -> SelectFormBuilder:
        self._control.label = label
        return self

    def variable(self, variable: str) -> SelectFormBuilder:
        self._control.variable = variable
        return self

    def required(self, required: bool) -> SelectFormBuilder:
        self._control.required = required
        return self

    def default(self, default: str) -> SelectFormBuilder:
        self._control.default = default
        return self

    def options(self, options: list[str]) -> SelectFormBuilder:
        self._control.options = options
        return self
