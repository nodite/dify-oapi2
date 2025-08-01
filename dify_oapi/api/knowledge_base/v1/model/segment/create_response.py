from dify_oapi.core.model.base_response import BaseResponse

from .segment_info import SegmentInfo


class CreateResponse(BaseResponse):
    data: list[SegmentInfo] | None = None
    doc_form: str | None = None
