from dify_oapi.core.model.base_response import BaseResponse

from .chatflow_types import JobStatus


class AnnotationReplyStatusResponse(BaseResponse):
    """Response for annotation reply status."""

    job_id: str | None = None
    job_status: JobStatus | None = None
    error_msg: str | None = None
