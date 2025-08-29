"""Pagination information model for Knowledge Base API."""

from typing import Optional

from pydantic import BaseModel


class PaginationInfo(BaseModel):
    """Pagination information model with builder pattern."""

    page: Optional[int] = None
    limit: Optional[int] = None
    total: Optional[int] = None
    has_more: Optional[bool] = None

    @staticmethod
    def builder() -> "PaginationInfoBuilder":
        return PaginationInfoBuilder()


class PaginationInfoBuilder:
    """Builder for PaginationInfo."""

    def __init__(self):
        self._pagination_info = PaginationInfo()

    def build(self) -> PaginationInfo:
        return self._pagination_info

    def page(self, page: int) -> "PaginationInfoBuilder":
        self._pagination_info.page = page
        return self

    def limit(self, limit: int) -> "PaginationInfoBuilder":
        self._pagination_info.limit = limit
        return self

    def total(self, total: int) -> "PaginationInfoBuilder":
        self._pagination_info.total = total
        return self

    def has_more(self, has_more: bool) -> "PaginationInfoBuilder":
        self._pagination_info.has_more = has_more
        return self
