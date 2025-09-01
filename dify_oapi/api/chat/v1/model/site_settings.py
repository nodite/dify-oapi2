"""Site settings model for Chat API."""

from __future__ import annotations

from pydantic import BaseModel, Field

from .chat_types import IconType


class SiteSettings(BaseModel):
    """Site settings model."""

    title: str | None = Field(None, description="Site title")
    chat_color_theme: str | None = Field(None, description="Chat color theme")
    chat_color_theme_inverted: bool | None = Field(None, description="Chat color theme inverted")
    icon_type: IconType | None = Field(None, description="Icon type")
    icon: str | None = Field(None, description="Icon")
    icon_background: str | None = Field(None, description="Icon background")
    icon_url: str | None = Field(None, description="Icon URL")
    description: str | None = Field(None, description="Site description")
    copyright: str | None = Field(None, description="Copyright")
    privacy_policy: str | None = Field(None, description="Privacy policy")
    custom_disclaimer: str | None = Field(None, description="Custom disclaimer")
    default_language: str | None = Field(None, description="Default language")
    show_workflow_steps: bool | None = Field(None, description="Show workflow steps")
    use_icon_as_answer_icon: bool | None = Field(None, description="Use icon as answer icon")

    @classmethod
    def builder(cls) -> SiteSettingsBuilder:
        """Create a SiteSettings builder."""
        return SiteSettingsBuilder()


class SiteSettingsBuilder:
    """Builder for SiteSettings."""

    def __init__(self) -> None:
        self._site_settings = SiteSettings()

    def title(self, title: str) -> SiteSettingsBuilder:
        """Set site title."""
        self._site_settings.title = title
        return self

    def chat_color_theme(self, chat_color_theme: str) -> SiteSettingsBuilder:
        """Set chat color theme."""
        self._site_settings.chat_color_theme = chat_color_theme
        return self

    def chat_color_theme_inverted(self, chat_color_theme_inverted: bool) -> SiteSettingsBuilder:
        """Set chat color theme inverted."""
        self._site_settings.chat_color_theme_inverted = chat_color_theme_inverted
        return self

    def icon_type(self, icon_type: IconType) -> SiteSettingsBuilder:
        """Set icon type."""
        self._site_settings.icon_type = icon_type
        return self

    def icon(self, icon: str) -> SiteSettingsBuilder:
        """Set icon."""
        self._site_settings.icon = icon
        return self

    def icon_background(self, icon_background: str) -> SiteSettingsBuilder:
        """Set icon background."""
        self._site_settings.icon_background = icon_background
        return self

    def icon_url(self, icon_url: str) -> SiteSettingsBuilder:
        """Set icon URL."""
        self._site_settings.icon_url = icon_url
        return self

    def description(self, description: str) -> SiteSettingsBuilder:
        """Set site description."""
        self._site_settings.description = description
        return self

    def copyright(self, copyright: str) -> SiteSettingsBuilder:
        """Set copyright."""
        self._site_settings.copyright = copyright
        return self

    def privacy_policy(self, privacy_policy: str) -> SiteSettingsBuilder:
        """Set privacy policy."""
        self._site_settings.privacy_policy = privacy_policy
        return self

    def custom_disclaimer(self, custom_disclaimer: str) -> SiteSettingsBuilder:
        """Set custom disclaimer."""
        self._site_settings.custom_disclaimer = custom_disclaimer
        return self

    def default_language(self, default_language: str) -> SiteSettingsBuilder:
        """Set default language."""
        self._site_settings.default_language = default_language
        return self

    def show_workflow_steps(self, show_workflow_steps: bool) -> SiteSettingsBuilder:
        """Set show workflow steps."""
        self._site_settings.show_workflow_steps = show_workflow_steps
        return self

    def use_icon_as_answer_icon(self, use_icon_as_answer_icon: bool) -> SiteSettingsBuilder:
        """Set use icon as answer icon."""
        self._site_settings.use_icon_as_answer_icon = use_icon_as_answer_icon
        return self

    def build(self) -> SiteSettings:
        """Build the SiteSettings instance."""
        return self._site_settings
