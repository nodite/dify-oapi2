from dify_oapi.core.model.base_response import BaseResponse

from .chat_types import JobStatus


class ConfigureAnnotationReplyResponse(BaseResponse):
    """Response for configuring annotation reply settings."""

    job_id: str | None = None
    job_status: JobStatus | None = None
