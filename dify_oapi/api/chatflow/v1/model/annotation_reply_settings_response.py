from dify_oapi.core.model.base_response import BaseResponse

from .chatflow_types import JobStatus


class AnnotationReplySettingsResponse(BaseResponse):
    """Response for annotation reply settings."""

    job_id: str | None = None
    job_status: JobStatus | None = None
