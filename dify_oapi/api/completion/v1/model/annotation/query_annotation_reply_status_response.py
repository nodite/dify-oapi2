from __future__ import annotations

from dify_oapi.core.model.base_response import BaseResponse

from .job_status_info import JobStatusInfo


class QueryAnnotationReplyStatusResponse(JobStatusInfo, BaseResponse):
    pass
