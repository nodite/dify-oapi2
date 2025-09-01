"""External retrieval model for Knowledge Base API."""

from typing import Optional

from pydantic import BaseModel


class ExternalRetrievalModel(BaseModel):
    """External retrieval model configuration."""

    top_k: Optional[int] = None
    score_threshold: Optional[float] = None
    score_threshold_enabled: Optional[bool] = None
