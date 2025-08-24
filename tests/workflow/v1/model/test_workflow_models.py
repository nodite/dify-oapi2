from dify_oapi.api.workflow.v1.model.workflow.execution_metadata import ExecutionMetadata
from dify_oapi.api.workflow.v1.model.workflow.node_info import NodeInfo
from dify_oapi.api.workflow.v1.model.workflow.run_specific_workflow_request import RunSpecificWorkflowRequest
from dify_oapi.api.workflow.v1.model.workflow.run_specific_workflow_request_body import RunSpecificWorkflowRequestBody
from dify_oapi.api.workflow.v1.model.workflow.run_specific_workflow_response import RunSpecificWorkflowResponse
from dify_oapi.api.workflow.v1.model.workflow.run_workflow_request import RunWorkflowRequest
from dify_oapi.api.workflow.v1.model.workflow.run_workflow_request_body import FileInfo, RunWorkflowRequestBody
from dify_oapi.api.workflow.v1.model.workflow.run_workflow_response import RunWorkflowResponse
from dify_oapi.api.workflow.v1.model.workflow.streaming_event import StreamingEvent
from dify_oapi.api.workflow.v1.model.workflow.workflow_inputs import WorkflowInputs
from dify_oapi.api.workflow.v1.model.workflow.workflow_run_data import WorkflowRunData
from dify_oapi.api.workflow.v1.model.workflow.workflow_run_info import WorkflowRunInfo
from dify_oapi.api.workflow.v1.model.workflow.workflow_types import EventType, NodeType, ResponseMode, WorkflowStatus
from dify_oapi.core.enum import HttpMethod

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


# ===== RUN WORKFLOW API MODELS TESTS =====


def test_run_workflow_request_builder() -> None:
    """Test RunWorkflowRequest builder pattern."""
    request = RunWorkflowRequest.builder().build()
    assert request.http_method == HttpMethod.POST
    assert request.uri == "/v1/workflows/run"
    assert request.request_body is None


def test_run_workflow_request_with_body() -> None:
    """Test RunWorkflowRequest with request body."""
    inputs = WorkflowInputs.builder().add_input("query", "test").build()
    request_body = (
        RunWorkflowRequestBody.builder()
        .inputs(inputs)
        .response_mode("blocking")
        .user("user-123")
        .trace_id("trace-456")
        .build()
    )
    request = RunWorkflowRequest.builder().request_body(request_body).build()

    assert request.request_body is not None
    assert request.request_body.inputs is not None
    assert request.request_body.response_mode == "blocking"
    assert request.request_body.user == "user-123"
    assert request.request_body.trace_id == "trace-456"
    assert request.body is not None


def test_run_workflow_request_body_validation() -> None:
    """Test RunWorkflowRequestBody validation and builder."""
    file_info = FileInfo(type="document", transfer_method="local_file", upload_file_id="file-123")
    inputs = WorkflowInputs.builder().add_input("content", "test content").build()

    request_body = (
        RunWorkflowRequestBody.builder()
        .inputs(inputs)
        .response_mode("streaming")
        .user("user-456")
        .files([file_info])
        .build()
    )

    assert request_body.inputs is not None
    assert request_body.inputs.get_input("content") == "test content"
    assert request_body.response_mode == "streaming"
    assert request_body.user == "user-456"
    assert request_body.files is not None
    assert len(request_body.files) == 1
    assert request_body.files[0].type == "document"
    assert request_body.files[0].upload_file_id == "file-123"


def test_response_mode_literal_validation() -> None:
    """Test ResponseMode literal type validation."""
    # Valid response modes should work
    valid_modes: list[ResponseMode] = ["streaming", "blocking"]
    for mode in valid_modes:
        request_body = RunWorkflowRequestBody(response_mode=mode)
        assert request_body.response_mode == mode


def test_run_workflow_response_model() -> None:
    """Test RunWorkflowResponse model."""
    # Create workflow run data
    data = WorkflowRunData.builder().id("run-123").status("succeeded").build()

    # Create response using multiple inheritance
    response = RunWorkflowResponse(
        workflow_run_id="run-123", task_id="task-456", data=data, success=True, code="200", msg="Success"
    )

    # Test WorkflowRunInfo properties
    assert response.workflow_run_id == "run-123"
    assert response.task_id == "task-456"
    assert response.data is not None
    assert response.data.id == "run-123"
    assert response.data.status == "succeeded"

    # Test BaseResponse properties
    assert response.success is False  # success is False when code is set
    assert response.code == "200"
    assert response.msg == "Success"


def test_file_info_model() -> None:
    """Test FileInfo model creation and validation."""
    file_info = FileInfo(type="image", transfer_method="remote_url", url="https://example.com/image.jpg")

    assert file_info.type == "image"
    assert file_info.transfer_method == "remote_url"
    assert file_info.url == "https://example.com/image.jpg"
    assert file_info.upload_file_id is None


def test_run_workflow_request_body_builder_chaining() -> None:
    """Test RunWorkflowRequestBody builder method chaining."""
    inputs = WorkflowInputs.builder().add_input("query", "test").build()

    # Test method chaining
    builder = RunWorkflowRequestBody.builder()
    result = builder.inputs(inputs).response_mode("blocking").user("user-123").trace_id("trace-456")

    # Verify builder returns self for chaining
    assert result is builder

    # Build and verify final result
    request_body = result.build()
    assert request_body.inputs is not None
    assert request_body.response_mode == "blocking"
    assert request_body.user == "user-123"
    assert request_body.trace_id == "trace-456"


def test_request_body_serialization() -> None:
    """Test request body serialization."""
    inputs = WorkflowInputs.builder().add_input("query", "test").build()
    request_body = RunWorkflowRequestBody.builder().inputs(inputs).response_mode("blocking").user("user-123").build()

    serialized = request_body.model_dump(exclude_none=True, mode="json")
    assert "inputs" in serialized
    assert "response_mode" in serialized
    assert "user" in serialized
    assert serialized["response_mode"] == "blocking"
    assert serialized["user"] == "user-123"
    # trace_id and files should not be present (None values excluded)
    assert "trace_id" not in serialized
    assert "files" not in serialized


# ===== RUN SPECIFIC WORKFLOW API MODELS TESTS =====


def test_run_specific_workflow_request_builder() -> None:
    """Test RunSpecificWorkflowRequest builder pattern."""
    request = RunSpecificWorkflowRequest.builder().workflow_id("workflow-123").build()
    assert request.http_method == HttpMethod.POST
    assert request.uri == "/v1/workflows/:workflow_id/run"
    assert request.workflow_id == "workflow-123"
    assert request.paths["workflow_id"] == "workflow-123"
    assert request.request_body is None


def test_run_specific_workflow_request_with_body() -> None:
    """Test RunSpecificWorkflowRequest with request body."""
    inputs = WorkflowInputs.builder().add_input("query", "test").build()
    request_body = (
        RunSpecificWorkflowRequestBody.builder()
        .inputs(inputs)
        .response_mode("blocking")
        .user("user-123")
        .trace_id("trace-456")
        .build()
    )
    request = RunSpecificWorkflowRequest.builder().workflow_id("workflow-456").request_body(request_body).build()

    assert request.workflow_id == "workflow-456"
    assert request.paths["workflow_id"] == "workflow-456"
    assert request.request_body is not None
    assert request.request_body.inputs is not None
    assert request.request_body.response_mode == "blocking"
    assert request.request_body.user == "user-123"
    assert request.request_body.trace_id == "trace-456"
    assert request.body is not None


def test_run_specific_workflow_request_body_validation() -> None:
    """Test RunSpecificWorkflowRequestBody validation and builder."""
    from dify_oapi.api.workflow.v1.model.file.file_info import FileInfo as FileInfoModel

    file_info = FileInfoModel(type="document", transfer_method="local_file", upload_file_id="file-123")
    inputs = WorkflowInputs.builder().add_input("content", "test content").build()

    request_body = (
        RunSpecificWorkflowRequestBody.builder()
        .inputs(inputs)
        .response_mode("streaming")
        .user("user-456")
        .files([file_info])
        .build()
    )

    assert request_body.inputs is not None
    assert request_body.inputs.get_input("content") == "test content"
    assert request_body.response_mode == "streaming"
    assert request_body.user == "user-456"
    assert request_body.files is not None
    assert len(request_body.files) == 1
    assert request_body.files[0].type == "document"
    assert request_body.files[0].upload_file_id == "file-123"


def test_run_specific_workflow_response_model() -> None:
    """Test RunSpecificWorkflowResponse model."""
    # Create workflow run data
    data = WorkflowRunData.builder().id("run-123").status("succeeded").build()

    # Create response using multiple inheritance
    response = RunSpecificWorkflowResponse(
        workflow_run_id="run-123", task_id="task-456", data=data, success=True, code="200", msg="Success"
    )

    # Test WorkflowRunInfo properties
    assert response.workflow_run_id == "run-123"
    assert response.task_id == "task-456"
    assert response.data is not None
    assert response.data.id == "run-123"
    assert response.data.status == "succeeded"

    # Test BaseResponse properties
    assert response.success is False  # success is False when code is set
    assert response.code == "200"
    assert response.msg == "Success"


def test_run_specific_workflow_request_body_builder_chaining() -> None:
    """Test RunSpecificWorkflowRequestBody builder method chaining."""
    inputs = WorkflowInputs.builder().add_input("query", "test").build()

    # Test method chaining
    builder = RunSpecificWorkflowRequestBody.builder()
    result = builder.inputs(inputs).response_mode("blocking").user("user-123").trace_id("trace-456")

    # Verify builder returns self for chaining
    assert result is builder

    # Build and verify final result
    request_body = result.build()
    assert request_body.inputs is not None
    assert request_body.response_mode == "blocking"
    assert request_body.user == "user-123"
    assert request_body.trace_id == "trace-456"


def test_run_specific_workflow_path_parameter_handling() -> None:
    """Test RunSpecificWorkflowRequest path parameter handling."""
    request = RunSpecificWorkflowRequest.builder().workflow_id("workflow-789").build()

    # Verify path parameter is set correctly
    assert request.workflow_id == "workflow-789"
    assert "workflow_id" in request.paths
    assert request.paths["workflow_id"] == "workflow-789"

    # Verify URI template is correct
    assert request.uri == "/v1/workflows/:workflow_id/run"
