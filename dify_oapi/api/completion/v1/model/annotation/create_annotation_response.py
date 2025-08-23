from __future__ import annotations

from dify_oapi.core.model.base_response import BaseResponse

from .annotation_info import AnnotationInfo


class CreateAnnotationResponse(AnnotationInfo, BaseResponse):
    pass
