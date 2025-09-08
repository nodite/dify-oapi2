"""Pagination information model for Chat API."""

from __future__ import annotations

from pydantic import BaseModel


class PaginationInfo(BaseModel):
    """Pagination information model."""

    limit: int | None = None
    has_more: bool | None = None
    total: int | None = None
    page: int | None = None

    @staticmethod
    def builder() -> PaginationInfoBuilder:
        return PaginationInfoBuilder()


class PaginationInfoBuilder:
    """Builder for PaginationInfo."""

    def __init__(self):
        self._pagination_info = PaginationInfo()

    def build(self) -> PaginationInfo:
        return self._pagination_info

    def limit(self, limit: int) -> PaginationInfoBuilder:
        self._pagination_info.limit = limit
        return self

    def has_more(self, has_more: bool) -> PaginationInfoBuilder:
        self._pagination_info.has_more = has_more
        return self

    def total(self, total: int) -> PaginationInfoBuilder:
        self._pagination_info.total = total
        return self

    def page(self, page: int) -> PaginationInfoBuilder:
        self._pagination_info.page = page
        return self
