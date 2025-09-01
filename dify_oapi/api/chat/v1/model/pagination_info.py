"""Pagination information model for Chat API."""

from __future__ import annotations

from pydantic import BaseModel, Field


class PaginationInfo(BaseModel):
    """Pagination information model."""

    limit: int | None = Field(None, description="Items per page")
    has_more: bool | None = Field(None, description="Whether has more items")
    total: int | None = Field(None, description="Total items count")
    page: int | None = Field(None, description="Current page number")

    @classmethod
    def builder(cls) -> PaginationInfoBuilder:
        """Create a PaginationInfo builder."""
        return PaginationInfoBuilder()


class PaginationInfoBuilder:
    """Builder for PaginationInfo."""

    def __init__(self) -> None:
        self._pagination_info = PaginationInfo()

    def limit(self, limit: int) -> PaginationInfoBuilder:
        """Set items per page."""
        self._pagination_info.limit = limit
        return self

    def has_more(self, has_more: bool) -> PaginationInfoBuilder:
        """Set whether has more items."""
        self._pagination_info.has_more = has_more
        return self

    def total(self, total: int) -> PaginationInfoBuilder:
        """Set total items count."""
        self._pagination_info.total = total
        return self

    def page(self, page: int) -> PaginationInfoBuilder:
        """Set current page number."""
        self._pagination_info.page = page
        return self

    def build(self) -> PaginationInfo:
        """Build the PaginationInfo instance."""
        return self._pagination_info
