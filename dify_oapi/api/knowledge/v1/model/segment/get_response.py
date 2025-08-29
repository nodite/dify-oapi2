from dify_oapi.core.model.base_response import BaseResponse

from .segment_info import SegmentInfo


class GetResponse(BaseResponse):
    data: SegmentInfo | None = None
    doc_form: str | None = None
