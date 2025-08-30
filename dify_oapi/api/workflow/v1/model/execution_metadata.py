from __future__ import annotations

from pydantic import BaseModel


class ExecutionMetadata(BaseModel):
    total_tokens: int | None = None
    total_price: float | None = None
    currency: str | None = None

    @staticmethod
    def builder() -> ExecutionMetadataBuilder:
        return ExecutionMetadataBuilder()


class ExecutionMetadataBuilder:
    def __init__(self):
        self._execution_metadata = ExecutionMetadata()

    def build(self) -> ExecutionMetadata:
        return self._execution_metadata

    def total_tokens(self, total_tokens: int) -> ExecutionMetadataBuilder:
        self._execution_metadata.total_tokens = total_tokens
        return self

    def total_price(self, total_price: float) -> ExecutionMetadataBuilder:
        self._execution_metadata.total_price = total_price
        return self

    def currency(self, currency: str) -> ExecutionMetadataBuilder:
        self._execution_metadata.currency = currency
        return self
