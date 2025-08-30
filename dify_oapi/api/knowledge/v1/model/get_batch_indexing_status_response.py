"""Get batch indexing status response model."""

from typing import Optional

from dify_oapi.core.model.base_response import BaseResponse


class GetBatchIndexingStatusResponse(BaseResponse):
    """Response model for get batch indexing status API."""

    id: Optional[str] = None
    indexing_status: Optional[str] = None
    processing_started_at: Optional[float] = None
    parsing_completed_at: Optional[float] = None
    cleaning_completed_at: Optional[float] = None
    splitting_completed_at: Optional[float] = None
    completed_at: Optional[float] = None
    paused_at: Optional[float] = None
    error: Optional[str] = None
    stopped_at: Optional[float] = None
    completed_segments: Optional[int] = None
    total_segments: Optional[int] = None
