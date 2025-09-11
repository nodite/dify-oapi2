from typing import Union

from pydantic import BaseModel


class ToolIconDetail(BaseModel):
    background: str | None = None
    content: str | None = None

    @staticmethod
    def builder() -> "ToolIconDetailBuilder":
        return ToolIconDetailBuilder()


class ToolIconDetailBuilder:
    def __init__(self):
        self._tool_icon_detail = ToolIconDetail()

    def build(self) -> ToolIconDetail:
        return self._tool_icon_detail

    def background(self, background: str) -> "ToolIconDetailBuilder":
        self._tool_icon_detail.background = background
        return self

    def content(self, content: str) -> "ToolIconDetailBuilder":
        self._tool_icon_detail.content = content
        return self


class AppMeta(BaseModel):
    tool_icons: dict[str, Union[str, ToolIconDetail]] | None = None

    @staticmethod
    def builder() -> "AppMetaBuilder":
        return AppMetaBuilder()


class AppMetaBuilder:
    def __init__(self):
        self._app_meta = AppMeta()

    def build(self) -> AppMeta:
        return self._app_meta

    def tool_icons(self, tool_icons: dict[str, Union[str, ToolIconDetail]]) -> "AppMetaBuilder":
        self._app_meta.tool_icons = tool_icons
        return self
