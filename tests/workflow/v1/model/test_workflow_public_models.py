from dify_oapi.api.workflow.v1.model.workflow.execution_metadata import ExecutionMetadata
from dify_oapi.api.workflow.v1.model.workflow.node_info import NodeInfo
from dify_oapi.api.workflow.v1.model.workflow.streaming_event import StreamingEvent
from dify_oapi.api.workflow.v1.model.workflow.workflow_file_info import WorkflowFileInfo
from dify_oapi.api.workflow.v1.model.workflow.workflow_inputs import WorkflowInputs
from dify_oapi.api.workflow.v1.model.workflow.workflow_run_data import WorkflowRunData
from dify_oapi.api.workflow.v1.model.workflow.workflow_run_info import WorkflowRunInfo


class TestExecutionMetadata:
    def test_builder_pattern(self) -> None:
        """Test ExecutionMetadata builder pattern functionality."""
        metadata = ExecutionMetadata.builder().total_tokens(100).total_price(0.05).currency("USD").build()
        assert metadata.total_tokens == 100
        assert metadata.total_price == 0.05
        assert metadata.currency == "USD"

    def test_field_validation(self) -> None:
        """Test ExecutionMetadata field validation."""
        metadata = ExecutionMetadata(total_tokens=200, total_price=0.10, currency="EUR")
        assert metadata.total_tokens == 200
        assert metadata.total_price == 0.10
        assert metadata.currency == "EUR"

    def test_serialization(self) -> None:
        """Test ExecutionMetadata serialization."""
        metadata = ExecutionMetadata(total_tokens=100, currency="USD")
        serialized = metadata.model_dump(exclude_none=True)
        assert serialized["total_tokens"] == 100
        assert serialized["currency"] == "USD"

    def test_direct_instantiation(self) -> None:
        """Test ExecutionMetadata direct instantiation alongside builder."""
        direct = ExecutionMetadata(total_tokens=50, currency="GBP")
        builder = ExecutionMetadata.builder().total_tokens(50).currency("GBP").build()
        assert direct.total_tokens == builder.total_tokens
        assert direct.currency == builder.currency


class TestNodeInfo:
    def test_builder_pattern(self) -> None:
        """Test NodeInfo builder pattern functionality."""
        metadata = ExecutionMetadata.builder().total_tokens(50).build()
        node = (
            NodeInfo.builder()
            .id("node-456")
            .node_type("code")
            .title("Code Node")
            .index(1)
            .status("running")
            .execution_metadata(metadata)
            .build()
        )
        assert node.id == "node-456"
        assert node.node_type == "code"
        assert node.title == "Code Node"
        assert node.index == 1
        assert node.status == "running"
        assert node.execution_metadata is not None

    def test_field_validation(self) -> None:
        """Test NodeInfo field validation."""
        node = NodeInfo(id="node-123", node_id="llm-node", node_type="llm", title="LLM Node", status="succeeded")
        assert node.id == "node-123"
        assert node.node_id == "llm-node"
        assert node.node_type == "llm"
        assert node.title == "LLM Node"
        assert node.status == "succeeded"

    def test_serialization(self) -> None:
        """Test NodeInfo serialization."""
        node = NodeInfo(id="node-123", node_type="llm", status="succeeded")
        serialized = node.model_dump(exclude_none=True)
        assert serialized["id"] == "node-123"
        assert serialized["node_type"] == "llm"
        assert serialized["status"] == "succeeded"

    def test_direct_instantiation(self) -> None:
        """Test NodeInfo direct instantiation alongside builder."""
        direct = NodeInfo(id="node-1", node_type="start", status="succeeded")
        builder = NodeInfo.builder().id("node-1").node_type("start").status("succeeded").build()
        assert direct.id == builder.id
        assert direct.node_type == builder.node_type
        assert direct.status == builder.status


class TestWorkflowInputs:
    def test_builder_pattern(self) -> None:
        """Test WorkflowInputs builder pattern functionality."""
        inputs = WorkflowInputs.builder().add_input("query", "Hello world").add_input("max_tokens", 100).build()
        assert inputs.inputs is not None
        assert inputs.get_input("query") == "Hello world"
        assert inputs.get_input("max_tokens") == 100

    def test_field_validation(self) -> None:
        """Test WorkflowInputs field validation."""
        inputs = WorkflowInputs(inputs={"query": "test", "temperature": 0.7})
        assert inputs.inputs is not None
        assert inputs.inputs["query"] == "test"
        assert inputs.inputs["temperature"] == 0.7

    def test_serialization(self) -> None:
        """Test WorkflowInputs serialization."""
        inputs = WorkflowInputs.builder().add_input("query", "test").build()
        serialized = inputs.model_dump(exclude_none=True)
        assert "inputs" in serialized
        assert serialized["inputs"]["query"] == "test"

    def test_direct_instantiation(self) -> None:
        """Test WorkflowInputs direct instantiation alongside builder."""
        direct = WorkflowInputs(inputs={"key": "value"})
        builder = WorkflowInputs.builder().add_input("key", "value").build()
        assert direct.get_input("key") == builder.get_input("key")


class TestWorkflowRunData:
    def test_builder_pattern(self) -> None:
        """Test WorkflowRunData builder pattern functionality."""
        data = (
            WorkflowRunData.builder()
            .id("run-789")
            .status("running")
            .total_tokens(200)
            .outputs({"result": "success"})
            .build()
        )
        assert data.id == "run-789"
        assert data.status == "running"
        assert data.total_tokens == 200
        assert data.outputs is not None
        assert data.outputs["result"] == "success"

    def test_field_validation(self) -> None:
        """Test WorkflowRunData field validation."""
        data = WorkflowRunData(
            id="run-123", workflow_id="workflow-456", status="succeeded", total_tokens=150, elapsed_time=2.5
        )
        assert data.id == "run-123"
        assert data.workflow_id == "workflow-456"
        assert data.status == "succeeded"
        assert data.total_tokens == 150
        assert data.elapsed_time == 2.5

    def test_serialization(self) -> None:
        """Test WorkflowRunData serialization."""
        data = WorkflowRunData(id="run-123", status="succeeded", total_tokens=100)
        serialized = data.model_dump(exclude_none=True)
        assert serialized["id"] == "run-123"
        assert serialized["status"] == "succeeded"
        assert serialized["total_tokens"] == 100

    def test_direct_instantiation(self) -> None:
        """Test WorkflowRunData direct instantiation alongside builder."""
        direct = WorkflowRunData(id="run-1", status="failed")
        builder = WorkflowRunData.builder().id("run-1").status("failed").build()
        assert direct.id == builder.id
        assert direct.status == builder.status


class TestWorkflowRunInfo:
    def test_builder_pattern(self) -> None:
        """Test WorkflowRunInfo builder pattern functionality."""
        data = WorkflowRunData.builder().id("run-789").status("failed").build()
        info = WorkflowRunInfo.builder().workflow_run_id("run-789").task_id("task-123").data(data).build()
        assert info.workflow_run_id == "run-789"
        assert info.task_id == "task-123"
        assert info.data is not None
        assert info.data.id == "run-789"
        assert info.data.status == "failed"

    def test_field_validation(self) -> None:
        """Test WorkflowRunInfo field validation."""
        data = WorkflowRunData(id="run-123", status="succeeded")
        info = WorkflowRunInfo(workflow_run_id="run-123", task_id="task-456", data=data)
        assert info.workflow_run_id == "run-123"
        assert info.task_id == "task-456"
        assert info.data is not None
        assert info.data.id == "run-123"

    def test_serialization(self) -> None:
        """Test WorkflowRunInfo serialization."""
        data = WorkflowRunData(id="run-123", status="succeeded")
        info = WorkflowRunInfo(workflow_run_id="run-123", data=data)
        serialized = info.model_dump(exclude_none=True)
        assert serialized["workflow_run_id"] == "run-123"
        assert "data" in serialized

    def test_direct_instantiation(self) -> None:
        """Test WorkflowRunInfo direct instantiation alongside builder."""
        data = WorkflowRunData(id="run-1", status="succeeded")
        direct = WorkflowRunInfo(workflow_run_id="run-1", data=data)
        builder = WorkflowRunInfo.builder().workflow_run_id("run-1").data(data).build()
        assert direct.workflow_run_id == builder.workflow_run_id
        assert direct.data is not None
        assert builder.data is not None
        assert direct.data.id == builder.data.id


class TestStreamingEvent:
    def test_builder_pattern(self) -> None:
        """Test StreamingEvent builder pattern functionality."""
        event = (
            StreamingEvent.builder()
            .event("text_chunk")
            .task_id("task-789")
            .data({"text": "Hello", "from_variable_selector": ["node1", "output"]})
            .build()
        )
        assert event.event == "text_chunk"
        assert event.task_id == "task-789"
        assert event.data is not None
        assert event.data["text"] == "Hello"

    def test_field_validation(self) -> None:
        """Test StreamingEvent field validation."""
        event = StreamingEvent(
            event="workflow_started", task_id="task-123", workflow_run_id="run-456", data={"message": "started"}
        )
        assert event.event == "workflow_started"
        assert event.task_id == "task-123"
        assert event.workflow_run_id == "run-456"
        assert event.data is not None
        assert event.data["message"] == "started"

    def test_serialization(self) -> None:
        """Test StreamingEvent serialization."""
        event = StreamingEvent(event="node_started", task_id="task-123")
        serialized = event.model_dump(exclude_none=True)
        assert serialized["event"] == "node_started"
        assert serialized["task_id"] == "task-123"

    def test_direct_instantiation(self) -> None:
        """Test StreamingEvent direct instantiation alongside builder."""
        direct = StreamingEvent(event="ping", task_id="task-1")
        builder = StreamingEvent.builder().event("ping").task_id("task-1").build()
        assert direct.event == builder.event
        assert direct.task_id == builder.task_id


class TestWorkflowFileInfo:
    def test_builder_pattern(self) -> None:
        """Test WorkflowFileInfo builder pattern functionality."""
        file_info = (
            WorkflowFileInfo.builder().type("document").transfer_method("local_file").upload_file_id("file-123").build()
        )
        assert file_info.type == "document"
        assert file_info.transfer_method == "local_file"
        assert file_info.upload_file_id == "file-123"

    def test_field_validation(self) -> None:
        """Test WorkflowFileInfo field validation."""
        file_info = WorkflowFileInfo(type="image", transfer_method="remote_url", url="https://example.com/image.jpg")
        assert file_info.type == "image"
        assert file_info.transfer_method == "remote_url"
        assert file_info.url == "https://example.com/image.jpg"
        assert file_info.upload_file_id is None

    def test_serialization(self) -> None:
        """Test WorkflowFileInfo serialization."""
        file_info = WorkflowFileInfo(type="document", transfer_method="local_file", upload_file_id="file-123")
        serialized = file_info.model_dump(exclude_none=True)
        assert serialized["type"] == "document"
        assert serialized["transfer_method"] == "local_file"
        assert serialized["upload_file_id"] == "file-123"

    def test_direct_instantiation(self) -> None:
        """Test WorkflowFileInfo direct instantiation alongside builder."""
        direct = WorkflowFileInfo(type="audio", transfer_method="local_file")
        builder = WorkflowFileInfo.builder().type("audio").transfer_method("local_file").build()
        assert direct.type == builder.type
        assert direct.transfer_method == builder.transfer_method
