from __future__ import annotations

from pydantic import BaseModel


class AppInfo(BaseModel):
    name: str | None = None
    description: str | None = None
    tags: list[str] | None = None
    mode: str | None = None
    author_name: str | None = None

    @staticmethod
    def builder() -> AppInfoBuilder:
        return AppInfoBuilder()


class AppInfoBuilder:
    def __init__(self):
        self._app_info = AppInfo()

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

    def mode(self, mode: str) -> AppInfoBuilder:
        self._app_info.mode = mode
        return self

    def author_name(self, author_name: str) -> AppInfoBuilder:
        self._app_info.author_name = author_name
        return self
