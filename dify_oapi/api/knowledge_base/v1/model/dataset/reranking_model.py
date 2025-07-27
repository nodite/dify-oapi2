from __future__ import annotations

from pydantic import BaseModel


class RerankingModel(BaseModel):
    reranking_provider_name: str | None = None
    reranking_model_name: str | None = None
