from dify_oapi.core.model.base_response import BaseResponse

from .retrieval_record import RetrievalRecord


class RetrieveFromDatasetResponse(BaseResponse):
    query: str | None = None
    records: list[RetrievalRecord] | None = None
