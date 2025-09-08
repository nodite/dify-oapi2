from __future__ import annotations

from pydantic import BaseModel


class ToolIconDetail(BaseModel):
    """Tool icon detail configuration."""

    background: str
    content: str

    @staticmethod
    def builder() -> ToolIconDetailBuilder:
        return ToolIconDetailBuilder()


class ToolIconDetailBuilder:
    def __init__(self):
        self._tool_icon_detail = ToolIconDetail(background="", content="")

    def build(self) -> ToolIconDetail:
        return self._tool_icon_detail

    def background(self, background: str) -> ToolIconDetailBuilder:
        self._tool_icon_detail.background = background
        return self

    def content(self, content: str) -> ToolIconDetailBuilder:
        self._tool_icon_detail.content = content
        return self


class ToolIcon(BaseModel):
    """Tool icon configuration."""

    tool_icons: dict[str, str | ToolIconDetail] | None = None

    @staticmethod
    def builder() -> ToolIconBuilder:
        return ToolIconBuilder()


class ToolIconBuilder:
    def __init__(self):
        self._tool_icon = ToolIcon()

    def build(self) -> ToolIcon:
        return self._tool_icon

    def tool_icons(self, tool_icons: dict[str, str | ToolIconDetail]) -> ToolIconBuilder:
        self._tool_icon.tool_icons = tool_icons
        return self
