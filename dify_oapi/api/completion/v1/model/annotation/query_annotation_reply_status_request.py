from __future__ import annotations

from dify_oapi.core.enum import HttpMethod
from dify_oapi.core.model.base_request import BaseRequest

from ..completion.completion_types import AnnotationAction


class QueryAnnotationReplyStatusRequest(BaseRequest):
    def __init__(self):
        super().__init__()
        self.action: AnnotationAction | None = None
        self.job_id: str | None = None

    @staticmethod
    def builder() -> QueryAnnotationReplyStatusRequestBuilder:
        return QueryAnnotationReplyStatusRequestBuilder()


class QueryAnnotationReplyStatusRequestBuilder:
    def __init__(self):
        query_annotation_reply_status_request = QueryAnnotationReplyStatusRequest()
        query_annotation_reply_status_request.http_method = HttpMethod.GET
        query_annotation_reply_status_request.uri = "/v1/apps/annotation-reply/:action/status/:job_id"
        self._query_annotation_reply_status_request = query_annotation_reply_status_request

    def build(self) -> QueryAnnotationReplyStatusRequest:
        return self._query_annotation_reply_status_request

    def action(self, action: AnnotationAction) -> QueryAnnotationReplyStatusRequestBuilder:
        self._query_annotation_reply_status_request.action = action
        self._query_annotation_reply_status_request.paths["action"] = action
        return self

    def job_id(self, job_id: str) -> QueryAnnotationReplyStatusRequestBuilder:
        self._query_annotation_reply_status_request.job_id = job_id
        self._query_annotation_reply_status_request.paths["job_id"] = job_id
        return self
