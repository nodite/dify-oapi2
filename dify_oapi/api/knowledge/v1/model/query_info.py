"""Query information model for Knowledge Base API."""

from typing import Optional

from pydantic import BaseModel


class QueryInfo(BaseModel):
    """Query information model with builder pattern."""

    content: Optional[str] = None

    @staticmethod
    def builder() -> "QueryInfoBuilder":
        return QueryInfoBuilder()


class QueryInfoBuilder:
    """Builder for QueryInfo."""

    def __init__(self):
        self._query_info = QueryInfo()

    def build(self) -> QueryInfo:
        return self._query_info

    def content(self, content: str) -> "QueryInfoBuilder":
        self._query_info.content = content
        return self
