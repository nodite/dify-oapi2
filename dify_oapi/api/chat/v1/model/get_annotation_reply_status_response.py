from dify_oapi.core.model.base_response import BaseResponse

from .chat_types import JobStatus


class GetAnnotationReplyStatusResponse(BaseResponse):
    """Response for getting annotation reply settings status."""

    job_id: str | None = None
    job_status: JobStatus | None = None
    error_msg: str | None = None
