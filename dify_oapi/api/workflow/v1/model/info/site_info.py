from __future__ import annotations

from pydantic import BaseModel

from ..workflow.workflow_types import IconType


class SiteInfo(BaseModel):
    title: str | None = None
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

    @staticmethod
    def builder() -> SiteInfoBuilder:
        return SiteInfoBuilder()


class SiteInfoBuilder:
    def __init__(self):
        self._site_info = SiteInfo()

    def build(self) -> SiteInfo:
        return self._site_info

    def title(self, title: str) -> SiteInfoBuilder:
        self._site_info.title = title
        return self

    def icon_type(self, icon_type: IconType) -> SiteInfoBuilder:
        self._site_info.icon_type = icon_type
        return self

    def icon(self, icon: str) -> SiteInfoBuilder:
        self._site_info.icon = icon
        return self

    def icon_background(self, icon_background: str) -> SiteInfoBuilder:
        self._site_info.icon_background = icon_background
        return self

    def icon_url(self, icon_url: str) -> SiteInfoBuilder:
        self._site_info.icon_url = icon_url
        return self

    def description(self, description: str) -> SiteInfoBuilder:
        self._site_info.description = description
        return self

    def copyright(self, copyright: str) -> SiteInfoBuilder:
        self._site_info.copyright = copyright
        return self

    def privacy_policy(self, privacy_policy: str) -> SiteInfoBuilder:
        self._site_info.privacy_policy = privacy_policy
        return self

    def custom_disclaimer(self, custom_disclaimer: str) -> SiteInfoBuilder:
        self._site_info.custom_disclaimer = custom_disclaimer
        return self

    def default_language(self, default_language: str) -> SiteInfoBuilder:
        self._site_info.default_language = default_language
        return self

    def show_workflow_steps(self, show_workflow_steps: bool) -> SiteInfoBuilder:
        self._site_info.show_workflow_steps = show_workflow_steps
        return self
