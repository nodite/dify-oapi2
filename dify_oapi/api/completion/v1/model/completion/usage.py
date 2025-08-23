from __future__ import annotations

from pydantic import BaseModel


class Usage(BaseModel):
    prompt_tokens: int | None = None
    prompt_unit_price: str | None = None
    prompt_price_unit: str | None = None
    prompt_price: str | None = None
    completion_tokens: int | None = None
    completion_unit_price: str | None = None
    completion_price_unit: str | None = None
    completion_price: str | None = None
    total_tokens: int | None = None
    total_price: str | None = None
    currency: str | None = None
    latency: float | None = None

    @staticmethod
    def builder() -> UsageBuilder:
        return UsageBuilder()


class UsageBuilder:
    def __init__(self):
        self._usage = Usage()

    def build(self) -> Usage:
        return self._usage

    def prompt_tokens(self, prompt_tokens: int) -> UsageBuilder:
        self._usage.prompt_tokens = prompt_tokens
        return self

    def prompt_unit_price(self, prompt_unit_price: str) -> UsageBuilder:
        self._usage.prompt_unit_price = prompt_unit_price
        return self

    def prompt_price_unit(self, prompt_price_unit: str) -> UsageBuilder:
        self._usage.prompt_price_unit = prompt_price_unit
        return self

    def prompt_price(self, prompt_price: str) -> UsageBuilder:
        self._usage.prompt_price = prompt_price
        return self

    def completion_tokens(self, completion_tokens: int) -> UsageBuilder:
        self._usage.completion_tokens = completion_tokens
        return self

    def completion_unit_price(self, completion_unit_price: str) -> UsageBuilder:
        self._usage.completion_unit_price = completion_unit_price
        return self

    def completion_price_unit(self, completion_price_unit: str) -> UsageBuilder:
        self._usage.completion_price_unit = completion_price_unit
        return self

    def completion_price(self, completion_price: str) -> UsageBuilder:
        self._usage.completion_price = completion_price
        return self

    def total_tokens(self, total_tokens: int) -> UsageBuilder:
        self._usage.total_tokens = total_tokens
        return self

    def total_price(self, total_price: str) -> UsageBuilder:
        self._usage.total_price = total_price
        return self

    def currency(self, currency: str) -> UsageBuilder:
        self._usage.currency = currency
        return self

    def latency(self, latency: float) -> UsageBuilder:
        self._usage.latency = latency
        return self
