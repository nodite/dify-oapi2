from __future__ import annotations

from pydantic import BaseModel


class AppInfo(BaseModel):
    """Application basic information model."""

    name: str
    description: str
    tags: list[str]

    @staticmethod
    def builder() -> AppInfoBuilder:
        return AppInfoBuilder()


class AppInfoBuilder:
    def __init__(self):
        self._app_info = AppInfo(name="", description="", tags=[])

    def build(self) -> AppInfo:
        return self._app_info

    def name(self, name: str) -> AppInfoBuilder:
        self._app_info.name = name
        return self

    def description(self, description: str) -> AppInfoBuilder:
        self._app_info.description = description
        return self

    def tags(self, tags: list[str]) -> AppInfoBuilder:
        self._app_info.tags = tags
        return self
