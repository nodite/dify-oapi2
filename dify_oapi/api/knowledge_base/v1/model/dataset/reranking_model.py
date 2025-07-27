from __future__ import annotations

from typing import Optional

from pydantic import BaseModel


class RerankingModel(BaseModel):
    reranking_provider_name: Optional[str] = None
    reranking_model_name: Optional[str] = None

