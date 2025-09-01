"""Tool icon model for Chat API."""

from __future__ import annotations

from pydantic import BaseModel, Field


class ToolIconDetail(BaseModel):
    """Tool icon detail model."""

    background: str | None = Field(None, description="Background color")
    content: str | None = Field(None, description="Icon content")

    @classmethod
    def builder(cls) -> ToolIconDetailBuilder:
        """Create a ToolIconDetail builder."""
        return ToolIconDetailBuilder()


class ToolIconDetailBuilder:
    """Builder for ToolIconDetail."""

    def __init__(self) -> None:
        self._tool_icon_detail = ToolIconDetail()

    def background(self, background: str) -> ToolIconDetailBuilder:
        """Set background color."""
        self._tool_icon_detail.background = background
        return self

    def content(self, content: str) -> ToolIconDetailBuilder:
        """Set icon content."""
        self._tool_icon_detail.content = content
        return self

    def build(self) -> ToolIconDetail:
        """Build the ToolIconDetail instance."""
        return self._tool_icon_detail


class ToolIcon(BaseModel):
    """Tool icon model."""

    icon: str | ToolIconDetail | None = Field(None, description="Tool icon")

    @classmethod
    def builder(cls) -> ToolIconBuilder:
        """Create a ToolIcon builder."""
        return ToolIconBuilder()


class ToolIconBuilder:
    """Builder for ToolIcon."""

    def __init__(self) -> None:
        self._tool_icon = ToolIcon()

    def icon(self, icon: str | ToolIconDetail) -> ToolIconBuilder:
        """Set tool icon."""
        self._tool_icon.icon = icon
        return self

    def build(self) -> ToolIcon:
        """Build the ToolIcon instance."""
        return self._tool_icon
