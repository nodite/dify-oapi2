from dify_oapi.core.model.base_response import BaseResponse

from .segment_info import SegmentInfo


class ListResponse(BaseResponse):
    data: list[SegmentInfo] | None = None
    doc_form: str | None = None
    has_more: bool | None = None
    limit: int | None = None
    total: int | None = None
    page: int | None = None
