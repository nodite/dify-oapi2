from dify_oapi.core.model.base_response import BaseResponse

from .query_info import QueryInfo
from .retrieval_record import RetrievalRecord


class RetrieveFromDatasetResponse(BaseResponse):
    query: QueryInfo | None = None
    records: list[RetrievalRecord] | None = None
