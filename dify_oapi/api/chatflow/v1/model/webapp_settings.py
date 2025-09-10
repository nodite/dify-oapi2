from pydantic import BaseModel

from .chatflow_types import ChatColorTheme, DefaultLanguage, IconType


class WebAppSettings(BaseModel):
    title: str | None = None
    chat_color_theme: ChatColorTheme | None = None
    chat_color_theme_inverted: bool | None = None
    icon_type: IconType | None = None
    icon: str | None = None
    icon_background: str | None = None
    icon_url: str | None = None
    description: str | None = None
    copyright: str | None = None
    privacy_policy: str | None = None
    custom_disclaimer: str | None = None
    default_language: DefaultLanguage | None = None
    show_workflow_steps: bool | None = None
    use_icon_as_answer_icon: bool | None = None

    @staticmethod
    def builder() -> "WebAppSettingsBuilder":
        return WebAppSettingsBuilder()


class WebAppSettingsBuilder:
    def __init__(self):
        self._webapp_settings = WebAppSettings()

    def build(self) -> WebAppSettings:
        return self._webapp_settings

    def title(self, title: str) -> "WebAppSettingsBuilder":
        self._webapp_settings.title = title
        return self

    def chat_color_theme(self, chat_color_theme: ChatColorTheme) -> "WebAppSettingsBuilder":
        self._webapp_settings.chat_color_theme = chat_color_theme
        return self

    def chat_color_theme_inverted(self, chat_color_theme_inverted: bool) -> "WebAppSettingsBuilder":
        self._webapp_settings.chat_color_theme_inverted = chat_color_theme_inverted
        return self

    def icon_type(self, icon_type: IconType) -> "WebAppSettingsBuilder":
        self._webapp_settings.icon_type = icon_type
        return self

    def icon(self, icon: str) -> "WebAppSettingsBuilder":
        self._webapp_settings.icon = icon
        return self

    def icon_background(self, icon_background: str) -> "WebAppSettingsBuilder":
        self._webapp_settings.icon_background = icon_background
        return self

    def icon_url(self, icon_url: str) -> "WebAppSettingsBuilder":
        self._webapp_settings.icon_url = icon_url
        return self

    def description(self, description: str) -> "WebAppSettingsBuilder":
        self._webapp_settings.description = description
        return self

    def copyright(self, copyright: str) -> "WebAppSettingsBuilder":
        self._webapp_settings.copyright = copyright
        return self

    def privacy_policy(self, privacy_policy: str) -> "WebAppSettingsBuilder":
        self._webapp_settings.privacy_policy = privacy_policy
        return self

    def custom_disclaimer(self, custom_disclaimer: str) -> "WebAppSettingsBuilder":
        self._webapp_settings.custom_disclaimer = custom_disclaimer
        return self

    def default_language(self, default_language: DefaultLanguage) -> "WebAppSettingsBuilder":
        self._webapp_settings.default_language = default_language
        return self

    def show_workflow_steps(self, show_workflow_steps: bool) -> "WebAppSettingsBuilder":
        self._webapp_settings.show_workflow_steps = show_workflow_steps
        return self

    def use_icon_as_answer_icon(self, use_icon_as_answer_icon: bool) -> "WebAppSettingsBuilder":
        self._webapp_settings.use_icon_as_answer_icon = use_icon_as_answer_icon
        return self
