"""Usage information model for Chat API."""

from __future__ import annotations

from pydantic import BaseModel, Field


class UsageInfo(BaseModel):
    """Usage information model."""

    prompt_tokens: int | None = Field(None, description="Prompt tokens")
    prompt_unit_price: str | None = Field(None, description="Prompt unit price")
    prompt_price_unit: str | None = Field(None, description="Prompt price unit")
    prompt_price: str | None = Field(None, description="Prompt price")
    completion_tokens: int | None = Field(None, description="Completion tokens")
    completion_unit_price: str | None = Field(None, description="Completion unit price")
    completion_price_unit: str | None = Field(None, description="Completion price unit")
    completion_price: str | None = Field(None, description="Completion price")
    total_tokens: int | None = Field(None, description="Total tokens")
    total_price: str | None = Field(None, description="Total price")
    currency: str | None = Field(None, description="Currency")
    latency: float | None = Field(None, description="Latency")

    @classmethod
    def builder(cls) -> UsageInfoBuilder:
        """Create a UsageInfo builder."""
        return UsageInfoBuilder()


class UsageInfoBuilder:
    """Builder for UsageInfo."""

    def __init__(self) -> None:
        self._usage_info = UsageInfo()

    def prompt_tokens(self, prompt_tokens: int) -> UsageInfoBuilder:
        """Set prompt tokens."""
        self._usage_info.prompt_tokens = prompt_tokens
        return self

    def prompt_unit_price(self, prompt_unit_price: str) -> UsageInfoBuilder:
        """Set prompt unit price."""
        self._usage_info.prompt_unit_price = prompt_unit_price
        return self

    def prompt_price_unit(self, prompt_price_unit: str) -> UsageInfoBuilder:
        """Set prompt price unit."""
        self._usage_info.prompt_price_unit = prompt_price_unit
        return self

    def prompt_price(self, prompt_price: str) -> UsageInfoBuilder:
        """Set prompt price."""
        self._usage_info.prompt_price = prompt_price
        return self

    def completion_tokens(self, completion_tokens: int) -> UsageInfoBuilder:
        """Set completion tokens."""
        self._usage_info.completion_tokens = completion_tokens
        return self

    def completion_unit_price(self, completion_unit_price: str) -> UsageInfoBuilder:
        """Set completion unit price."""
        self._usage_info.completion_unit_price = completion_unit_price
        return self

    def completion_price_unit(self, completion_price_unit: str) -> UsageInfoBuilder:
        """Set completion price unit."""
        self._usage_info.completion_price_unit = completion_price_unit
        return self

    def completion_price(self, completion_price: str) -> UsageInfoBuilder:
        """Set completion price."""
        self._usage_info.completion_price = completion_price
        return self

    def total_tokens(self, total_tokens: int) -> UsageInfoBuilder:
        """Set total tokens."""
        self._usage_info.total_tokens = total_tokens
        return self

    def total_price(self, total_price: str) -> UsageInfoBuilder:
        """Set total price."""
        self._usage_info.total_price = total_price
        return self

    def currency(self, currency: str) -> UsageInfoBuilder:
        """Set currency."""
        self._usage_info.currency = currency
        return self

    def latency(self, latency: float) -> UsageInfoBuilder:
        """Set latency."""
        self._usage_info.latency = latency
        return self

    def build(self) -> UsageInfo:
        """Build the UsageInfo instance."""
        return self._usage_info
