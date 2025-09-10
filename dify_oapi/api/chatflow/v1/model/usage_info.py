from pydantic import BaseModel


class UsageInfo(BaseModel):
    """Token usage information model."""

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
    def builder() -> "UsageInfoBuilder":
        return UsageInfoBuilder()


class UsageInfoBuilder:
    def __init__(self):
        self._usage_info = UsageInfo()

    def build(self) -> UsageInfo:
        return self._usage_info

    def prompt_tokens(self, prompt_tokens: int) -> "UsageInfoBuilder":
        self._usage_info.prompt_tokens = prompt_tokens
        return self

    def prompt_unit_price(self, prompt_unit_price: str) -> "UsageInfoBuilder":
        self._usage_info.prompt_unit_price = prompt_unit_price
        return self

    def prompt_price_unit(self, prompt_price_unit: str) -> "UsageInfoBuilder":
        self._usage_info.prompt_price_unit = prompt_price_unit
        return self

    def prompt_price(self, prompt_price: str) -> "UsageInfoBuilder":
        self._usage_info.prompt_price = prompt_price
        return self

    def completion_tokens(self, completion_tokens: int) -> "UsageInfoBuilder":
        self._usage_info.completion_tokens = completion_tokens
        return self

    def completion_unit_price(self, completion_unit_price: str) -> "UsageInfoBuilder":
        self._usage_info.completion_unit_price = completion_unit_price
        return self

    def completion_price_unit(self, completion_price_unit: str) -> "UsageInfoBuilder":
        self._usage_info.completion_price_unit = completion_price_unit
        return self

    def completion_price(self, completion_price: str) -> "UsageInfoBuilder":
        self._usage_info.completion_price = completion_price
        return self

    def total_tokens(self, total_tokens: int) -> "UsageInfoBuilder":
        self._usage_info.total_tokens = total_tokens
        return self

    def total_price(self, total_price: str) -> "UsageInfoBuilder":
        self._usage_info.total_price = total_price
        return self

    def currency(self, currency: str) -> "UsageInfoBuilder":
        self._usage_info.currency = currency
        return self

    def latency(self, latency: float) -> "UsageInfoBuilder":
        self._usage_info.latency = latency
        return self
