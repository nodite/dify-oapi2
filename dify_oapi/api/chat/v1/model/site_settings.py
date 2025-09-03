from __future__ import annotations

from pydantic import BaseModel

from .chat_types import IconType


class SiteSettings(BaseModel):
    """Site settings configuration."""

    title: str | None = None
    chat_color_theme: str | None = None
    chat_color_theme_inverted: bool | None = None
    icon_type: IconType | None = None
    icon: str | None = None
    icon_background: str | None = None
    icon_url: str | None = None
    description: str | None = None
    copyright: str | None = None
    privacy_policy: str | None = None
    custom_disclaimer: str | None = None
    default_language: str | None = None
    show_workflow_steps: bool | None = None
    use_icon_as_answer_icon: bool | None = None

    @staticmethod
    def builder() -> SiteSettingsBuilder:
        return SiteSettingsBuilder()


class SiteSettingsBuilder:
    def __init__(self):
        self._site_settings = SiteSettings()

    def build(self) -> SiteSettings:
        return self._site_settings

    def title(self, title: str) -> SiteSettingsBuilder:
        self._site_settings.title = title
        return self

    def chat_color_theme(self, chat_color_theme: str) -> SiteSettingsBuilder:
        self._site_settings.chat_color_theme = chat_color_theme
        return self

    def chat_color_theme_inverted(self, chat_color_theme_inverted: bool) -> SiteSettingsBuilder:
        self._site_settings.chat_color_theme_inverted = chat_color_theme_inverted
        return self

    def icon_type(self, icon_type: IconType) -> SiteSettingsBuilder:
        self._site_settings.icon_type = icon_type
        return self

    def icon(self, icon: str) -> SiteSettingsBuilder:
        self._site_settings.icon = icon
        return self

    def icon_background(self, icon_background: str) -> SiteSettingsBuilder:
        self._site_settings.icon_background = icon_background
        return self

    def icon_url(self, icon_url: str) -> SiteSettingsBuilder:
        self._site_settings.icon_url = icon_url
        return self

    def description(self, description: str) -> SiteSettingsBuilder:
        self._site_settings.description = description
        return self

    def copyright(self, copyright: str) -> SiteSettingsBuilder:
        self._site_settings.copyright = copyright
        return self

    def privacy_policy(self, privacy_policy: str) -> SiteSettingsBuilder:
        self._site_settings.privacy_policy = privacy_policy
        return self

    def custom_disclaimer(self, custom_disclaimer: str) -> SiteSettingsBuilder:
        self._site_settings.custom_disclaimer = custom_disclaimer
        return self

    def default_language(self, default_language: str) -> SiteSettingsBuilder:
        self._site_settings.default_language = default_language
        return self

    def show_workflow_steps(self, show_workflow_steps: bool) -> SiteSettingsBuilder:
        self._site_settings.show_workflow_steps = show_workflow_steps
        return self

    def use_icon_as_answer_icon(self, use_icon_as_answer_icon: bool) -> SiteSettingsBuilder:
        self._site_settings.use_icon_as_answer_icon = use_icon_as_answer_icon
        return self
