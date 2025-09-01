"""Application information model for Chat API."""

from __future__ import annotations

from pydantic import BaseModel, Field


class AppInfo(BaseModel):
    """Application information model."""

    name: str | None = Field(None, description="Application name")
    description: str | None = Field(None, description="Application description")
    tags: list[str] | None = Field(None, description="Application tags")

    @classmethod
    def builder(cls) -> AppInfoBuilder:
        """Create an AppInfo builder."""
        return AppInfoBuilder()


class AppInfoBuilder:
    """Builder for AppInfo."""

    def __init__(self) -> None:
        self._app_info = AppInfo()

    def name(self, name: str) -> AppInfoBuilder:
        """Set application name."""
        self._app_info.name = name
        return self

    def description(self, description: str) -> AppInfoBuilder:
        """Set application description."""
        self._app_info.description = description
        return self

    def tags(self, tags: list[str]) -> AppInfoBuilder:
        """Set application tags."""
        self._app_info.tags = tags
        return self

    def build(self) -> AppInfo:
        """Build the AppInfo instance."""
        return self._app_info
