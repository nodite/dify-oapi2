from __future__ import annotations

from dify_oapi.core.enum import HttpMethod
from dify_oapi.core.model.base_request import BaseRequest


class GetWorkflowLogsRequest(BaseRequest):
    def __init__(self):
        super().__init__()

    @staticmethod
    def builder() -> GetWorkflowLogsRequestBuilder:
        return GetWorkflowLogsRequestBuilder()


class GetWorkflowLogsRequestBuilder:
    def __init__(self):
        get_workflow_logs_request = GetWorkflowLogsRequest()
        get_workflow_logs_request.http_method = HttpMethod.GET
        get_workflow_logs_request.uri = "/v1/workflows/logs"
        self._get_workflow_logs_request = get_workflow_logs_request

    def build(self) -> GetWorkflowLogsRequest:
        return self._get_workflow_logs_request

    def keyword(self, keyword: str) -> GetWorkflowLogsRequestBuilder:
        self._get_workflow_logs_request.add_query("keyword", keyword)
        return self

    def status(self, status: str) -> GetWorkflowLogsRequestBuilder:
        self._get_workflow_logs_request.add_query("status", status)
        return self

    def page(self, page: int) -> GetWorkflowLogsRequestBuilder:
        self._get_workflow_logs_request.add_query("page", str(page))
        return self

    def limit(self, limit: int) -> GetWorkflowLogsRequestBuilder:
        self._get_workflow_logs_request.add_query("limit", str(limit))
        return self

    def created_by_end_user_session_id(self, session_id: str) -> GetWorkflowLogsRequestBuilder:
        self._get_workflow_logs_request.add_query("created_by_end_user_session_id", session_id)
        return self

    def created_by_account(self, account: str) -> GetWorkflowLogsRequestBuilder:
        self._get_workflow_logs_request.add_query("created_by_account", account)
        return self
