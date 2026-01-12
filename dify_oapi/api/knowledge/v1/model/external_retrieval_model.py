"""External retrieval model for Knowledge Base API."""

from pydantic import BaseModel


class ExternalRetrievalModel(BaseModel):
    """External retrieval model configuration."""

    top_k: int | None = None
    score_threshold: float | None = None
    score_threshold_enabled: bool | None = None
