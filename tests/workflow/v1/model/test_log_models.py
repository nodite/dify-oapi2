from dify_oapi.api.workflow.v1.model.log.get_workflow_logs_request import GetWorkflowLogsRequest
from dify_oapi.api.workflow.v1.model.log.get_workflow_logs_response import GetWorkflowLogsResponse
from dify_oapi.core.enum import HttpMethod
from dify_oapi.core.model.base_response import BaseResponse


class TestGetWorkflowLogsModels:
    def test_request_builder(self) -> None:
        """Test GetWorkflowLogsRequest builder pattern."""
        request = (
            GetWorkflowLogsRequest.builder()
            .keyword("test")
            .status("succeeded")
            .page(2)
            .limit(50)
            .created_by_end_user_session_id("session-123")
            .created_by_account("user@example.com")
            .build()
        )
        assert request.http_method == HttpMethod.GET
        assert request.uri == "/v1/workflows/logs"

    def test_request_validation(self) -> None:
        """Test GetWorkflowLogsRequest validation."""
        request = GetWorkflowLogsRequest.builder().build()
        assert request.http_method == HttpMethod.GET
        assert request.uri == "/v1/workflows/logs"

    def test_request_query_parameters(self) -> None:
        """Test GetWorkflowLogsRequest query parameter handling."""
        request = (
            GetWorkflowLogsRequest.builder()
            .keyword("test")
            .status("succeeded")
            .page(2)
            .limit(50)
            .created_by_end_user_session_id("session-123")
            .created_by_account("user@example.com")
            .build()
        )
        query_params = dict(request.queries)
        assert query_params["keyword"] == "test"
        assert query_params["status"] == "succeeded"
        assert query_params["page"] == "2"
        assert query_params["limit"] == "50"
        assert query_params["created_by_end_user_session_id"] == "session-123"
        assert query_params["created_by_account"] == "user@example.com"

    def test_response_inheritance(self) -> None:
        """Test GetWorkflowLogsResponse inherits from BaseResponse."""
        response = GetWorkflowLogsResponse()
        assert isinstance(response, BaseResponse)
        assert hasattr(response, "success")
        assert hasattr(response, "code")
        assert hasattr(response, "msg")
        assert hasattr(response, "raw")

    def test_response_data_access(self) -> None:
        """Test GetWorkflowLogsResponse data access."""
        response = GetWorkflowLogsResponse(page=1, limit=20, total=100, has_more=True, data=[])
        assert response.page == 1
        assert response.limit == 20
        assert response.total == 100
        assert response.has_more is True
        assert response.data is not None
        assert len(response.data) == 0
