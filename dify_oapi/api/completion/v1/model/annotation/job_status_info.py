from __future__ import annotations

from pydantic import BaseModel

from ..completion.completion_types import JobStatus


class JobStatusInfo(BaseModel):
    job_id: str | None = None
    job_status: JobStatus | None = None
    error_msg: str | None = None

    @staticmethod
    def builder() -> JobStatusInfoBuilder:
        return JobStatusInfoBuilder()


class JobStatusInfoBuilder:
    def __init__(self):
        self._job_status_info = JobStatusInfo()

    def build(self) -> JobStatusInfo:
        return self._job_status_info

    def job_id(self, job_id: str) -> JobStatusInfoBuilder:
        self._job_status_info.job_id = job_id
        return self

    def job_status(self, job_status: JobStatus) -> JobStatusInfoBuilder:
        self._job_status_info.job_status = job_status
        return self

    def error_msg(self, error_msg: str) -> JobStatusInfoBuilder:
        self._job_status_info.error_msg = error_msg
        return self
