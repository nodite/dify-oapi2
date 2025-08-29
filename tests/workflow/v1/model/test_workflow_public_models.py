"""Tests for workflow public models."""

from dify_oapi.api.workflow.v1.model.execution_metadata import ExecutionMetadata
from dify_oapi.api.workflow.v1.model.file_info import FileInfo
from dify_oapi.api.workflow.v1.model.node_info import NodeInfo
from dify_oapi.api.workflow.v1.model.workflow_file_info import WorkflowFileInfo
from dify_oapi.api.workflow.v1.model.workflow_inputs import WorkflowInputs
from dify_oapi.api.workflow.v1.model.workflow_run_data import WorkflowRunData
from dify_oapi.api.workflow.v1.model.workflow_run_info import WorkflowRunInfo


class TestWorkflowInputs:
    """Test WorkflowInputs model."""

    def test_builder_pattern(self) -> None:
        """Test builder pattern functionality."""
        inputs = WorkflowInputs.builder().inputs({"query": "test query", "count": 5}).build()

        assert inputs.inputs is not None
        assert inputs.inputs["query"] == "test query"
        assert inputs.inputs["count"] == 5

    def test_add_input_method(self) -> None:
        """Test add_input method."""
        inputs = WorkflowInputs.builder().build()
        inputs.add_input("key1", "value1")
        inputs.add_input("key2", 42)

        assert inputs.get_input("key1") == "value1"
        assert inputs.get_input("key2") == 42
        assert inputs.get_input("nonexistent") is None

    def test_builder_add_input(self) -> None:
        """Test builder add_input method."""
        inputs = WorkflowInputs.builder().add_input("text", "hello").add_input("number", 123).build()

        assert inputs.inputs is not None
        assert inputs.inputs["text"] == "hello"
        assert inputs.inputs["number"] == 123


class TestFileInfo:
    """Test FileInfo model."""

    def test_builder_pattern(self) -> None:
        """Test builder pattern functionality."""
        file_info = (
            FileInfo.builder()
            .id("file-123")
            .name("test.pdf")
            .size(1024)
            .extension("pdf")
            .mime_type("application/pdf")
            .created_by("user-456")
            .created_at(1640995200)
            .build()
        )

        assert file_info.id == "file-123"
        assert file_info.name == "test.pdf"
        assert file_info.size == 1024
        assert file_info.extension == "pdf"
        assert file_info.mime_type == "application/pdf"
        assert file_info.created_by == "user-456"
        assert file_info.created_at == 1640995200

    def test_field_validation(self) -> None:
        """Test field validation."""
        file_info = FileInfo()
        assert file_info.id is None
        assert file_info.name is None
        assert file_info.size is None


class TestNodeInfo:
    """Test NodeInfo model."""

    def test_builder_pattern(self) -> None:
        """Test builder pattern functionality."""
        metadata = ExecutionMetadata.builder().total_tokens(100).build()

        node_info = (
            NodeInfo.builder()
            .id("node-123")
            .node_id("llm-node-1")
            .node_type("llm")
            .title("LLM Node")
            .index(1)
            .status("succeeded")
            .elapsed_time(2.5)
            .execution_metadata(metadata)
            .created_at(1640995200)
            .build()
        )

        assert node_info.id == "node-123"
        assert node_info.node_id == "llm-node-1"
        assert node_info.node_type == "llm"
        assert node_info.title == "LLM Node"
        assert node_info.index == 1
        assert node_info.status == "succeeded"
        assert node_info.elapsed_time == 2.5
        assert node_info.execution_metadata is not None
        assert node_info.created_at == 1640995200

    def test_type_validation(self) -> None:
        """Test Literal type validation."""
        node_info = NodeInfo.builder().node_type("llm").status("succeeded").build()
        assert node_info.node_type == "llm"
        assert node_info.status == "succeeded"


class TestExecutionMetadata:
    """Test ExecutionMetadata model."""

    def test_builder_pattern(self) -> None:
        """Test builder pattern functionality."""
        metadata = ExecutionMetadata.builder().total_tokens(150).total_price(0.003).currency("USD").build()

        assert metadata.total_tokens == 150
        assert metadata.total_price == 0.003
        assert metadata.currency == "USD"

    def test_numeric_field_validation(self) -> None:
        """Test numeric field validation."""
        metadata = ExecutionMetadata.builder().total_tokens(0).total_price(0.0).build()
        assert metadata.total_tokens == 0
        assert metadata.total_price == 0.0


class TestWorkflowFileInfo:
    """Test WorkflowFileInfo model."""

    def test_builder_pattern(self) -> None:
        """Test builder pattern functionality."""
        file_info = (
            WorkflowFileInfo.builder()
            .type("document")
            .transfer_method("local_file")
            .upload_file_id("upload-123")
            .build()
        )

        assert file_info.type == "document"
        assert file_info.transfer_method == "local_file"
        assert file_info.upload_file_id == "upload-123"
        assert file_info.url is None

    def test_remote_url_pattern(self) -> None:
        """Test remote URL pattern."""
        file_info = (
            WorkflowFileInfo.builder()
            .type("image")
            .transfer_method("remote_url")
            .url("https://example.com/image.jpg")
            .build()
        )

        assert file_info.type == "image"
        assert file_info.transfer_method == "remote_url"
        assert file_info.url == "https://example.com/image.jpg"
        assert file_info.upload_file_id is None

    def test_type_validation(self) -> None:
        """Test Literal type validation."""
        file_info = WorkflowFileInfo.builder().type("document").transfer_method("local_file").build()
        assert file_info.type == "document"
        assert file_info.transfer_method == "local_file"


class TestWorkflowRunInfo:
    """Test WorkflowRunInfo model."""

    def test_builder_pattern(self) -> None:
        """Test builder pattern functionality."""
        run_data = WorkflowRunData.builder().id("run-123").status("succeeded").build()

        run_info = (
            WorkflowRunInfo.builder().workflow_run_id("workflow-run-456").task_id("task-789").data(run_data).build()
        )

        assert run_info.workflow_run_id == "workflow-run-456"
        assert run_info.task_id == "task-789"
        assert run_info.data is not None
        assert run_info.data.id == "run-123"

    def test_field_validation(self) -> None:
        """Test field validation."""
        run_info = WorkflowRunInfo()
        assert run_info.workflow_run_id is None
        assert run_info.task_id is None
        assert run_info.data is None


class TestWorkflowRunData:
    """Test WorkflowRunData model."""

    def test_builder_pattern(self) -> None:
        """Test builder pattern functionality."""
        run_data = (
            WorkflowRunData.builder()
            .id("run-123")
            .workflow_id("workflow-456")
            .status("succeeded")
            .outputs({"result": "success"})
            .total_tokens(150)
            .elapsed_time(2.5)
            .created_at(1640995200)
            .finished_at(1640995300)
            .build()
        )

        assert run_data.id == "run-123"
        assert run_data.workflow_id == "workflow-456"
        assert run_data.status == "succeeded"
        assert run_data.outputs == {"result": "success"}
        assert run_data.total_tokens == 150
        assert run_data.elapsed_time == 2.5
        assert run_data.created_at == 1640995200
        assert run_data.finished_at == 1640995300

    def test_field_validation(self) -> None:
        """Test field validation."""
        run_data = WorkflowRunData.builder().status("failed").error("Test error").build()
        assert run_data.status == "failed"
        assert run_data.error == "Test error"
