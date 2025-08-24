from dify_oapi.api.workflow.v1.model.workflow.execution_metadata import ExecutionMetadata
from dify_oapi.api.workflow.v1.model.workflow.node_info import NodeInfo
from dify_oapi.api.workflow.v1.model.workflow.streaming_event import StreamingEvent
from dify_oapi.api.workflow.v1.model.workflow.workflow_inputs import WorkflowInputs
from dify_oapi.api.workflow.v1.model.workflow.workflow_run_data import WorkflowRunData
from dify_oapi.api.workflow.v1.model.workflow.workflow_run_info import WorkflowRunInfo
from dify_oapi.api.workflow.v1.model.workflow.workflow_types import EventType, NodeType, WorkflowStatus

# ===== SHARED WORKFLOW MODELS TESTS =====


def test_execution_metadata_creation() -> None:
    """Test ExecutionMetadata model creation and validation."""
    metadata = ExecutionMetadata(total_tokens=100, total_price=0.05, currency="USD")
    assert metadata.total_tokens == 100
    assert metadata.total_price == 0.05
    assert metadata.currency == "USD"


def test_execution_metadata_builder_pattern() -> None:
    """Test ExecutionMetadata builder pattern functionality."""
    metadata = ExecutionMetadata.builder().total_tokens(200).total_price(0.10).currency("EUR").build()
    assert metadata.total_tokens == 200
    assert metadata.total_price == 0.10
    assert metadata.currency == "EUR"


def test_node_info_creation() -> None:
    """Test NodeInfo model creation and validation."""
    node = NodeInfo(id="node-123", node_id="llm-node", node_type="llm", title="LLM Node", status="succeeded")
    assert node.id == "node-123"
    assert node.node_id == "llm-node"
    assert node.node_type == "llm"
    assert node.title == "LLM Node"
    assert node.status == "succeeded"


def test_node_info_builder_pattern() -> None:
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
    assert node.execution_metadata.total_tokens == 50


def test_workflow_status_literal_validation() -> None:
    """Test WorkflowStatus literal type validation."""
    # Valid statuses should work
    valid_statuses: list[WorkflowStatus] = ["running", "succeeded", "failed", "stopped"]
    for status in valid_statuses:
        node = NodeInfo(status=status)
        assert node.status == status


def test_node_type_literal_validation() -> None:
    """Test NodeType literal type validation."""
    # Valid node types should work
    valid_types: list[NodeType] = ["start", "end", "llm", "code", "template"]
    for node_type in valid_types:
        node = NodeInfo(node_type=node_type)
        assert node.node_type == node_type


def test_workflow_inputs_creation() -> None:
    """Test WorkflowInputs model creation and validation."""
    inputs = WorkflowInputs(inputs={"query": "test", "temperature": 0.7})
    assert inputs.inputs is not None
    assert inputs.inputs["query"] == "test"
    assert inputs.inputs["temperature"] == 0.7


def test_workflow_inputs_builder_pattern() -> None:
    """Test WorkflowInputs builder pattern functionality."""
    inputs = WorkflowInputs.builder().add_input("query", "Hello world").add_input("max_tokens", 100).build()
    assert inputs.inputs is not None
    assert inputs.get_input("query") == "Hello world"
    assert inputs.get_input("max_tokens") == 100


def test_workflow_inputs_methods() -> None:
    """Test WorkflowInputs helper methods."""
    inputs = WorkflowInputs()
    inputs.add_input("key1", "value1")
    inputs.add_input("key2", 42)

    assert inputs.get_input("key1") == "value1"
    assert inputs.get_input("key2") == 42
    assert inputs.get_input("nonexistent") is None


def test_workflow_run_data_creation() -> None:
    """Test WorkflowRunData model creation and validation."""
    data = WorkflowRunData(
        id="run-123", workflow_id="workflow-456", status="succeeded", total_tokens=150, elapsed_time=2.5
    )
    assert data.id == "run-123"
    assert data.workflow_id == "workflow-456"
    assert data.status == "succeeded"
    assert data.total_tokens == 150
    assert data.elapsed_time == 2.5


def test_workflow_run_data_builder_pattern() -> None:
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


def test_workflow_run_info_creation() -> None:
    """Test WorkflowRunInfo model creation and validation."""
    data = WorkflowRunData(id="run-123", status="succeeded")
    info = WorkflowRunInfo(workflow_run_id="run-123", task_id="task-456", data=data)
    assert info.workflow_run_id == "run-123"
    assert info.task_id == "task-456"
    assert info.data is not None
    assert info.data.id == "run-123"
    assert info.data.status == "succeeded"


def test_workflow_run_info_builder_pattern() -> None:
    """Test WorkflowRunInfo builder pattern functionality."""
    data = WorkflowRunData.builder().id("run-789").status("failed").build()
    info = WorkflowRunInfo.builder().workflow_run_id("run-789").task_id("task-123").data(data).build()
    assert info.workflow_run_id == "run-789"
    assert info.task_id == "task-123"
    assert info.data is not None
    assert info.data.id == "run-789"
    assert info.data.status == "failed"


def test_streaming_event_creation() -> None:
    """Test StreamingEvent model creation and validation."""
    event = StreamingEvent(
        event="workflow_started", task_id="task-123", workflow_run_id="run-456", data={"message": "started"}
    )
    assert event.event == "workflow_started"
    assert event.task_id == "task-123"
    assert event.workflow_run_id == "run-456"
    assert event.data is not None
    assert event.data["message"] == "started"


def test_streaming_event_builder_pattern() -> None:
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


def test_event_type_literal_validation() -> None:
    """Test EventType literal type validation."""
    # Valid event types should work
    valid_events: list[EventType] = [
        "workflow_started",
        "node_started",
        "text_chunk",
        "node_finished",
        "workflow_finished",
        "ping",
    ]
    for event_type in valid_events:
        event = StreamingEvent(event=event_type)
        assert event.event == event_type


def test_model_serialization() -> None:
    """Test model serialization with model_dump()."""
    metadata = ExecutionMetadata(total_tokens=100, currency="USD")
    serialized = metadata.model_dump()
    assert serialized["total_tokens"] == 100
    assert serialized["currency"] == "USD"
    assert serialized["total_price"] is None  # None values included by default

    # Test exclude_none=True
    serialized_no_none = metadata.model_dump(exclude_none=True)
    assert "total_price" not in serialized_no_none  # None values excluded


def test_nested_model_relationships() -> None:
    """Test nested model relationships work correctly."""
    # Create nested structure
    metadata = ExecutionMetadata.builder().total_tokens(50).currency("USD").build()
    node = NodeInfo.builder().id("node-1").execution_metadata(metadata).build()
    data = WorkflowRunData.builder().id("run-1").status("succeeded").build()
    info = WorkflowRunInfo.builder().workflow_run_id("run-1").data(data).build()

    # Verify relationships
    assert info.data is not None
    assert info.data.id == "run-1"
    assert info.data.status == "succeeded"
    assert node.execution_metadata is not None
    assert node.execution_metadata.total_tokens == 50
    assert node.execution_metadata.currency == "USD"
