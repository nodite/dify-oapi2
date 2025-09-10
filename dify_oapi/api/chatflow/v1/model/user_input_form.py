from pydantic import BaseModel


class TextInputControl(BaseModel):
    label: str
    variable: str
    required: bool
    default: str | None = None

    @staticmethod
    def builder() -> "TextInputControlBuilder":
        return TextInputControlBuilder()


class TextInputControlBuilder:
    def __init__(self):
        self._text_input_control = TextInputControl(label="", variable="", required=False)

    def build(self) -> TextInputControl:
        return self._text_input_control

    def label(self, label: str) -> "TextInputControlBuilder":
        self._text_input_control.label = label
        return self

    def variable(self, variable: str) -> "TextInputControlBuilder":
        self._text_input_control.variable = variable
        return self

    def required(self, required: bool) -> "TextInputControlBuilder":
        self._text_input_control.required = required
        return self

    def default(self, default: str) -> "TextInputControlBuilder":
        self._text_input_control.default = default
        return self


class ParagraphControl(BaseModel):
    label: str
    variable: str
    required: bool
    default: str | None = None

    @staticmethod
    def builder() -> "ParagraphControlBuilder":
        return ParagraphControlBuilder()


class ParagraphControlBuilder:
    def __init__(self):
        self._paragraph_control = ParagraphControl(label="", variable="", required=False)

    def build(self) -> ParagraphControl:
        return self._paragraph_control

    def label(self, label: str) -> "ParagraphControlBuilder":
        self._paragraph_control.label = label
        return self

    def variable(self, variable: str) -> "ParagraphControlBuilder":
        self._paragraph_control.variable = variable
        return self

    def required(self, required: bool) -> "ParagraphControlBuilder":
        self._paragraph_control.required = required
        return self

    def default(self, default: str) -> "ParagraphControlBuilder":
        self._paragraph_control.default = default
        return self


class SelectControl(BaseModel):
    label: str
    variable: str
    required: bool
    default: str | None = None
    options: list[str]

    @staticmethod
    def builder() -> "SelectControlBuilder":
        return SelectControlBuilder()


class SelectControlBuilder:
    def __init__(self):
        self._select_control = SelectControl(label="", variable="", required=False, options=[])

    def build(self) -> SelectControl:
        return self._select_control

    def label(self, label: str) -> "SelectControlBuilder":
        self._select_control.label = label
        return self

    def variable(self, variable: str) -> "SelectControlBuilder":
        self._select_control.variable = variable
        return self

    def required(self, required: bool) -> "SelectControlBuilder":
        self._select_control.required = required
        return self

    def default(self, default: str) -> "SelectControlBuilder":
        self._select_control.default = default
        return self

    def options(self, options: list[str]) -> "SelectControlBuilder":
        self._select_control.options = options
        return self


class UserInputFormItem(BaseModel):
    text_input: TextInputControl | None = None
    paragraph: ParagraphControl | None = None
    select: SelectControl | None = None

    @staticmethod
    def builder() -> "UserInputFormItemBuilder":
        return UserInputFormItemBuilder()


class UserInputFormItemBuilder:
    def __init__(self):
        self._user_input_form_item = UserInputFormItem()

    def build(self) -> UserInputFormItem:
        return self._user_input_form_item

    def text_input(self, text_input: TextInputControl) -> "UserInputFormItemBuilder":
        self._user_input_form_item.text_input = text_input
        return self

    def paragraph(self, paragraph: ParagraphControl) -> "UserInputFormItemBuilder":
        self._user_input_form_item.paragraph = paragraph
        return self

    def select(self, select: SelectControl) -> "UserInputFormItemBuilder":
        self._user_input_form_item.select = select
        return self
