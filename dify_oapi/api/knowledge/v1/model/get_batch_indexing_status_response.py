"""Get batch indexing status response model."""

from dify_oapi.core.model.base_response import BaseResponse

from .batch_info import BatchInfo


class GetBatchIndexingStatusResponse(BatchInfo, BaseResponse):
    """Response model for get batch indexing status API."""

    pass
