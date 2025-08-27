from dify_oapi.api.workflow.v1.model.log.end_user_info import EndUserInfo
from dify_oapi.api.workflow.v1.model.log.log_info import LogInfo
from dify_oapi.api.workflow.v1.model.log.workflow_run_log_info import WorkflowRunLogInfo


class TestEndUserInfo:
    def test_builder_pattern(self) -> None:
        """Test EndUserInfo builder pattern functionality."""
        end_user = (
            EndUserInfo.builder().id("user-123").type("end_user").is_anonymous(False).session_id("session-456").build()
        )
        assert end_user.id == "user-123"
        assert end_user.type == "end_user"
        assert end_user.is_anonymous is False
        assert end_user.session_id == "session-456"

    def test_field_validation(self) -> None:
        """Test EndUserInfo field validation."""
        end_user = EndUserInfo(id="user-789", type="anonymous", is_anonymous=True, session_id="session-123")
        assert end_user.id == "user-789"
        assert end_user.type == "anonymous"
        assert end_user.is_anonymous is True
        assert end_user.session_id == "session-123"

    def test_serialization(self) -> None:
        """Test EndUserInfo serialization."""
        end_user = EndUserInfo(id="user-123", type="end_user", is_anonymous=False)
        serialized = end_user.model_dump(exclude_none=True)
        assert serialized["id"] == "user-123"
        assert serialized["type"] == "end_user"
        assert serialized["is_anonymous"] is False

    def test_direct_instantiation(self) -> None:
        """Test EndUserInfo direct instantiation alongside builder."""
        direct = EndUserInfo(id="user-1", type="registered")
        builder = EndUserInfo.builder().id("user-1").type("registered").build()
        assert direct.id == builder.id
        assert direct.type == builder.type


class TestLogInfo:
    def test_builder_pattern(self) -> None:
        """Test LogInfo builder pattern functionality."""
        workflow_run = WorkflowRunLogInfo.builder().id("run-123").status("succeeded").build()
        end_user = EndUserInfo.builder().id("user-456").session_id("session-789").build()
        log_info = (
            LogInfo.builder()
            .id("log-123")
            .workflow_run(workflow_run)
            .created_from("service-api")
            .created_by_role("end_user")
            .created_by_account("user@example.com")
            .created_by_end_user(end_user)
            .created_at(1234567890)
            .build()
        )
        assert log_info.id == "log-123"
        assert log_info.workflow_run is not None
        assert log_info.workflow_run.id == "run-123"
        assert log_info.created_from == "service-api"
        assert log_info.created_by_role == "end_user"

    def test_field_validation(self) -> None:
        """Test LogInfo field validation."""
        log_info = LogInfo(id="log-456", created_from="web-app", created_by_role="account")
        assert log_info.id == "log-456"
        assert log_info.created_from == "web-app"
        assert log_info.created_by_role == "account"

    def test_serialization(self) -> None:
        """Test LogInfo serialization."""
        log_info = LogInfo(id="log-123", created_from="service-api", created_at=1234567890)
        serialized = log_info.model_dump(exclude_none=True)
        assert serialized["id"] == "log-123"
        assert serialized["created_from"] == "service-api"
        assert serialized["created_at"] == 1234567890

    def test_direct_instantiation(self) -> None:
        """Test LogInfo direct instantiation alongside builder."""
        direct = LogInfo(id="log-1", created_from="service-api")
        builder = LogInfo.builder().id("log-1").created_from("service-api").build()
        assert direct.id == builder.id
        assert direct.created_from == builder.created_from


class TestWorkflowRunLogInfo:
    def test_builder_pattern(self) -> None:
        """Test WorkflowRunLogInfo builder pattern functionality."""
        log_info = (
            WorkflowRunLogInfo.builder()
            .id("run-123")
            .version("1.0")
            .status("succeeded")
            .elapsed_time(2.5)
            .total_tokens(150)
            .total_steps(5)
            .created_at(1234567890)
            .finished_at(1234567892)
            .build()
        )
        assert log_info.id == "run-123"
        assert log_info.version == "1.0"
        assert log_info.status == "succeeded"
        assert log_info.elapsed_time == 2.5
        assert log_info.total_tokens == 150
        assert log_info.total_steps == 5
        assert log_info.created_at == 1234567890
        assert log_info.finished_at == 1234567892

    def test_field_validation(self) -> None:
        """Test WorkflowRunLogInfo field validation."""
        log_info = WorkflowRunLogInfo(id="run-456", status="failed", error="Workflow execution failed")
        assert log_info.id == "run-456"
        assert log_info.status == "failed"
        assert log_info.error == "Workflow execution failed"

    def test_serialization(self) -> None:
        """Test WorkflowRunLogInfo serialization."""
        log_info = WorkflowRunLogInfo(id="run-123", status="succeeded", total_tokens=150)
        serialized = log_info.model_dump(exclude_none=True)
        assert serialized["id"] == "run-123"
        assert serialized["status"] == "succeeded"
        assert serialized["total_tokens"] == 150

    def test_direct_instantiation(self) -> None:
        """Test WorkflowRunLogInfo direct instantiation alongside builder."""
        direct = WorkflowRunLogInfo(id="run-1", status="succeeded")
        builder = WorkflowRunLogInfo.builder().id("run-1").status("succeeded").build()
        assert direct.id == builder.id
        assert direct.status == builder.status
