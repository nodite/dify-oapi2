from dify_oapi.api.workflow.v1.model.log.end_user_info import EndUserInfo
from dify_oapi.api.workflow.v1.model.log.get_workflow_logs_request import GetWorkflowLogsRequest
from dify_oapi.api.workflow.v1.model.log.get_workflow_logs_response import GetWorkflowLogsResponse
from dify_oapi.api.workflow.v1.model.log.log_info import LogInfo
from dify_oapi.api.workflow.v1.model.log.workflow_run_log_info import WorkflowRunLogInfo
from dify_oapi.api.workflow.v1.model.workflow.execution_metadata import ExecutionMetadata
from dify_oapi.api.workflow.v1.model.workflow.get_workflow_run_detail_request import GetWorkflowRunDetailRequest
from dify_oapi.api.workflow.v1.model.workflow.get_workflow_run_detail_response import GetWorkflowRunDetailResponse
from dify_oapi.api.workflow.v1.model.workflow.node_info import NodeInfo
from dify_oapi.api.workflow.v1.model.workflow.run_specific_workflow_request import RunSpecificWorkflowRequest
from dify_oapi.api.workflow.v1.model.workflow.run_specific_workflow_request_body import RunSpecificWorkflowRequestBody
from dify_oapi.api.workflow.v1.model.workflow.run_specific_workflow_response import RunSpecificWorkflowResponse
from dify_oapi.api.workflow.v1.model.workflow.run_workflow_request import RunWorkflowRequest
from dify_oapi.api.workflow.v1.model.workflow.run_workflow_request_body import RunWorkflowRequestBody
from dify_oapi.api.workflow.v1.model.workflow.run_workflow_response import RunWorkflowResponse
from dify_oapi.api.workflow.v1.model.workflow.stop_workflow_request import StopWorkflowRequest
from dify_oapi.api.workflow.v1.model.workflow.stop_workflow_request_body import StopWorkflowRequestBody
from dify_oapi.api.workflow.v1.model.workflow.stop_workflow_response import StopWorkflowResponse
from dify_oapi.api.workflow.v1.model.workflow.streaming_event import StreamingEvent
from dify_oapi.api.workflow.v1.model.workflow.workflow_file_info import WorkflowFileInfo
from dify_oapi.api.workflow.v1.model.workflow.workflow_inputs import WorkflowInputs
from dify_oapi.api.workflow.v1.model.workflow.workflow_run_data import WorkflowRunData
from dify_oapi.api.workflow.v1.model.workflow.workflow_run_info import WorkflowRunInfo
from dify_oapi.api.workflow.v1.model.workflow.workflow_types import (
    AppMode,
    CreatedByRole,
    CreatedFrom,
    EventType,
    IconType,
    LogStatus,
    NodeType,
    ResponseMode,
    WorkflowStatus,
)
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
    file_info = WorkflowFileInfo(type="document", transfer_method="local_file", upload_file_id="file-123")
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


def test_workflow_file_info_model() -> None:
    """Test WorkflowFileInfo model creation and validation."""
    file_info = WorkflowFileInfo(type="image", transfer_method="remote_url", url="https://example.com/image.jpg")

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
    file_info = WorkflowFileInfo(type="document", transfer_method="local_file", upload_file_id="file-123")
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


def test_workflow_inputs_with_file_list() -> None:
    """Test WorkflowInputs with file list type variables."""
    # Use WorkflowFileInfo for workflow inputs
    file1 = WorkflowFileInfo(type="document", transfer_method="local_file", upload_file_id="file-123")
    file2 = WorkflowFileInfo(type="image", transfer_method="remote_url", url="https://example.com/image.jpg")
    file_list = [file1, file2]

    # Test with file list type variable
    inputs = WorkflowInputs.builder().add_input("documents", file_list).build()

    assert inputs.inputs is not None
    assert "documents" in inputs.inputs
    retrieved_files = inputs.get_input("documents")
    assert isinstance(retrieved_files, list)
    assert len(retrieved_files) == 2
    # Type assertion for mypy
    assert isinstance(retrieved_files[0], WorkflowFileInfo)
    assert isinstance(retrieved_files[1], WorkflowFileInfo)
    assert retrieved_files[0].type == "document"
    assert retrieved_files[0].upload_file_id == "file-123"
    assert retrieved_files[1].type == "image"
    assert retrieved_files[1].url == "https://example.com/image.jpg"


def test_workflow_inputs_with_various_types() -> None:
    """Test WorkflowInputs with various supported value types."""
    inputs = WorkflowInputs()

    # Test different value types
    inputs.add_input("text_field", "Hello World")
    inputs.add_input("number_field", 42)
    inputs.add_input("float_field", 3.14)
    inputs.add_input("boolean_field", True)
    inputs.add_input("string_array", ["item1", "item2", "item3"])
    inputs.add_input("config", {"setting1": "value1", "setting2": "100"})

    # Verify all types are stored correctly
    assert inputs.get_input("text_field") == "Hello World"
    assert inputs.get_input("number_field") == 42
    assert inputs.get_input("float_field") == 3.14
    assert inputs.get_input("boolean_field") is True

    string_array = inputs.get_input("string_array")
    assert isinstance(string_array, list)
    assert string_array == ["item1", "item2", "item3"]

    config = inputs.get_input("config")
    assert isinstance(config, dict)
    assert config["setting1"] == "value1"
    assert config["setting2"] == "100"


def test_workflow_inputs_builder_with_mixed_types() -> None:
    """Test WorkflowInputs builder with mixed value types."""
    # Use WorkflowFileInfo for workflow inputs
    file_info = WorkflowFileInfo(type="document", transfer_method="local_file", upload_file_id="doc-456")

    inputs = (
        WorkflowInputs.builder()
        .add_input("query", "Analyze this document")
        .add_input("temperature", 0.7)
        .add_input("max_tokens", 1000)
        .add_input("stream", True)
        .add_input("files", [file_info])
        .add_input("tags", ["analysis", "document"])
        .add_input("metadata", {"source": "upload", "priority": "1"})
        .build()
    )

    assert inputs.inputs is not None
    assert len(inputs.inputs) == 7

    # Verify each type
    assert inputs.get_input("query") == "Analyze this document"
    assert inputs.get_input("temperature") == 0.7
    assert inputs.get_input("max_tokens") == 1000
    assert inputs.get_input("stream") is True

    files = inputs.get_input("files")
    assert isinstance(files, list)
    assert len(files) == 1
    # Type assertion for mypy
    assert isinstance(files[0], WorkflowFileInfo)
    assert files[0].type == "document"

    tags = inputs.get_input("tags")
    assert isinstance(tags, list)
    assert tags == ["analysis", "document"]

    metadata = inputs.get_input("metadata")
    assert isinstance(metadata, dict)
    assert metadata["source"] == "upload"
    assert metadata["priority"] == "1"


# ===== GET WORKFLOW RUN DETAIL API MODELS TESTS =====


def test_get_workflow_run_detail_request_builder() -> None:
    """Test GetWorkflowRunDetailRequest builder pattern."""
    request = GetWorkflowRunDetailRequest.builder().workflow_run_id("run-123").build()
    assert request.http_method == HttpMethod.GET
    assert request.uri == "/v1/workflows/run/:workflow_run_id"
    assert request.workflow_run_id == "run-123"
    assert request.paths["workflow_run_id"] == "run-123"


def test_get_workflow_run_detail_request_path_parameter() -> None:
    """Test GetWorkflowRunDetailRequest path parameter handling."""
    request = GetWorkflowRunDetailRequest.builder().workflow_run_id("run-456").build()

    # Verify path parameter is set correctly
    assert request.workflow_run_id == "run-456"
    assert "workflow_run_id" in request.paths
    assert request.paths["workflow_run_id"] == "run-456"

    # Verify URI template is correct
    assert request.uri == "/v1/workflows/run/:workflow_run_id"


def test_get_workflow_run_detail_response_model() -> None:
    """Test GetWorkflowRunDetailResponse model."""
    response = GetWorkflowRunDetailResponse(
        id="run-123",
        workflow_id="workflow-456",
        status="succeeded",
        inputs={"query": "test"},
        outputs={"result": "success"},
        total_steps=5,
        total_tokens=150,
        elapsed_time=2.5,
        success=True,
        code="200",
        msg="Success",
    )

    # Test response fields
    assert response.id == "run-123"
    assert response.workflow_id == "workflow-456"
    assert response.status == "succeeded"
    assert response.inputs is not None
    assert response.inputs["query"] == "test"
    assert response.outputs is not None
    assert response.outputs["result"] == "success"
    assert response.total_steps == 5
    assert response.total_tokens == 150
    assert response.elapsed_time == 2.5

    # Test BaseResponse properties
    assert response.success is False  # success is False when code is set
    assert response.code == "200"
    assert response.msg == "Success"


def test_get_workflow_run_detail_response_with_error() -> None:
    """Test GetWorkflowRunDetailResponse with error status."""
    response = GetWorkflowRunDetailResponse(
        id="run-789",
        workflow_id="workflow-123",
        status="failed",
        error="Workflow execution failed",
        total_steps=3,
        elapsed_time=1.2,
    )

    assert response.id == "run-789"
    assert response.workflow_id == "workflow-123"
    assert response.status == "failed"
    assert response.error == "Workflow execution failed"
    assert response.total_steps == 3
    assert response.elapsed_time == 1.2
    assert response.outputs is None
    assert response.total_tokens is None


def test_get_workflow_run_detail_response_workflow_status_validation() -> None:
    """Test GetWorkflowRunDetailResponse WorkflowStatus literal type validation."""
    # Valid statuses should work
    valid_statuses: list[WorkflowStatus] = ["running", "succeeded", "failed", "stopped"]
    for status in valid_statuses:
        response = GetWorkflowRunDetailResponse(status=status)
        assert response.status == status


def test_get_workflow_run_detail_response_serialization() -> None:
    """Test GetWorkflowRunDetailResponse serialization."""
    response = GetWorkflowRunDetailResponse(
        id="run-123", status="succeeded", inputs={"query": "test"}, outputs={"result": "success"}, total_tokens=100
    )

    serialized = response.model_dump(exclude_none=True)
    assert serialized["id"] == "run-123"
    assert serialized["status"] == "succeeded"
    assert "inputs" in serialized
    assert "outputs" in serialized
    assert serialized["total_tokens"] == 100
    # None values should be excluded
    assert "error" not in serialized
    assert "workflow_id" not in serialized


def test_workflow_inputs_serialization_with_files() -> None:
    """Test WorkflowInputs serialization with file list types."""
    # Use WorkflowFileInfo for workflow inputs
    file_info = WorkflowFileInfo(type="image", transfer_method="remote_url", url="https://example.com/test.jpg")

    inputs = (
        WorkflowInputs.builder().add_input("prompt", "Describe this image").add_input("images", [file_info]).build()
    )

    # Test serialization
    serialized = inputs.model_dump(exclude_none=True)
    assert "inputs" in serialized
    assert serialized["inputs"]["prompt"] == "Describe this image"
    assert "images" in serialized["inputs"]

    # Verify file info is properly serialized
    images_data = serialized["inputs"]["images"]
    assert isinstance(images_data, list)
    assert len(images_data) == 1
    assert images_data[0]["type"] == "image"
    assert images_data[0]["transfer_method"] == "remote_url"
    assert images_data[0]["url"] == "https://example.com/test.jpg"


# ===== STOP WORKFLOW API MODELS TESTS =====


def test_stop_workflow_request_builder() -> None:
    """Test StopWorkflowRequest builder pattern."""
    request = StopWorkflowRequest.builder().task_id("task-123").build()
    assert request.http_method == HttpMethod.POST
    assert request.uri == "/v1/workflows/tasks/:task_id/stop"
    assert request.task_id == "task-123"
    assert request.paths["task_id"] == "task-123"
    assert request.request_body is None


def test_stop_workflow_request_with_body() -> None:
    """Test StopWorkflowRequest with request body."""
    request_body = StopWorkflowRequestBody.builder().user("user-123").build()
    request = StopWorkflowRequest.builder().task_id("task-456").request_body(request_body).build()

    assert request.task_id == "task-456"
    assert request.paths["task_id"] == "task-456"
    assert request.request_body is not None
    assert request.request_body.user == "user-123"
    assert request.body is not None


def test_stop_workflow_request_body_validation() -> None:
    """Test StopWorkflowRequestBody validation and builder."""
    request_body = StopWorkflowRequestBody.builder().user("user-456").build()

    assert request_body.user == "user-456"


def test_stop_workflow_response_model() -> None:
    """Test StopWorkflowResponse model."""
    response = StopWorkflowResponse(result="success", success=True, code="200", msg="Success")

    # Test response fields
    assert response.result == "success"

    # Test BaseResponse properties
    assert response.success is False  # success is False when code is set
    assert response.code == "200"
    assert response.msg == "Success"


def test_stop_workflow_request_body_builder_chaining() -> None:
    """Test StopWorkflowRequestBody builder method chaining."""
    # Test method chaining
    builder = StopWorkflowRequestBody.builder()
    result = builder.user("user-789")

    # Verify builder returns self for chaining
    assert result is builder

    # Build and verify final result
    request_body = result.build()
    assert request_body.user == "user-789"


def test_stop_workflow_request_path_parameter_handling() -> None:
    """Test StopWorkflowRequest path parameter handling."""
    request = StopWorkflowRequest.builder().task_id("task-789").build()

    # Verify path parameter is set correctly
    assert request.task_id == "task-789"
    assert "task_id" in request.paths
    assert request.paths["task_id"] == "task-789"

    # Verify URI template is correct
    assert request.uri == "/v1/workflows/tasks/:task_id/stop"


def test_stop_workflow_request_body_serialization() -> None:
    """Test StopWorkflowRequestBody serialization."""
    request_body = StopWorkflowRequestBody.builder().user("user-123").build()

    serialized = request_body.model_dump(exclude_none=True, mode="json")
    assert "user" in serialized
    assert serialized["user"] == "user-123"


def test_stop_workflow_response_serialization() -> None:
    """Test StopWorkflowResponse serialization."""
    response = StopWorkflowResponse(result="success")

    serialized = response.model_dump(exclude_none=True)
    assert serialized["result"] == "success"
    # None values should be excluded
    assert "code" not in serialized
    assert "msg" not in serialized


# ===== FILE API MODELS TESTS =====


def test_file_info_builder_pattern() -> None:
    """Test FileInfo builder pattern."""
    from dify_oapi.api.workflow.v1.model.file.file_info import FileInfo as FileInfoModel

    file_info = (
        FileInfoModel.builder()
        .id("file-123")
        .name("test_document.pdf")
        .size(1024)
        .extension("pdf")
        .mime_type("application/pdf")
        .created_by("user-456")
        .created_at(1234567890)
        .build()
    )

    assert file_info.id == "file-123"
    assert file_info.name == "test_document.pdf"
    assert file_info.size == 1024
    assert file_info.extension == "pdf"
    assert file_info.mime_type == "application/pdf"
    assert file_info.created_by == "user-456"
    assert file_info.created_at == 1234567890


def test_file_info_creation() -> None:
    """Test FileInfo model creation and validation."""
    from dify_oapi.api.workflow.v1.model.file.file_info import FileInfo as FileInfoModel

    file_info = FileInfoModel(
        id="file-789",
        name="image.jpg",
        size=2048,
        extension="jpg",
        mime_type="image/jpeg",
        created_by="user-123",
        created_at=1234567891,
    )

    assert file_info.id == "file-789"
    assert file_info.name == "image.jpg"
    assert file_info.size == 2048
    assert file_info.extension == "jpg"
    assert file_info.mime_type == "image/jpeg"
    assert file_info.created_by == "user-123"
    assert file_info.created_at == 1234567891


def test_upload_file_request_multipart() -> None:
    """Test UploadFileRequest multipart handling."""
    from io import BytesIO

    from dify_oapi.api.workflow.v1.model.file.upload_file_request import UploadFileRequest
    from dify_oapi.api.workflow.v1.model.file.upload_file_request_body import UploadFileRequestBody

    # Create file content
    file_content = BytesIO(b"test file content")
    request_body = UploadFileRequestBody.builder().user("user-123").build()

    request = UploadFileRequest.builder().file(file_content, "test.txt").request_body(request_body).build()

    assert request.http_method == HttpMethod.POST
    assert request.uri == "/v1/files/upload"
    assert request.file is not None
    assert request.files is not None
    assert "file" in request.files
    assert request.files["file"][0] == "test.txt"
    assert request.files["file"][1] == file_content
    assert request.body is not None
    assert request.body["user"] == "user-123"
    assert request.request_body is not None
    assert request.request_body.user == "user-123"


def test_upload_file_request_body_validation() -> None:
    """Test UploadFileRequestBody validation and builder."""
    from dify_oapi.api.workflow.v1.model.file.upload_file_request_body import UploadFileRequestBody

    request_body = UploadFileRequestBody.builder().user("user-456").build()

    assert request_body.user == "user-456"


def test_upload_file_response_model() -> None:
    """Test UploadFileResponse model."""
    from dify_oapi.api.workflow.v1.model.file.upload_file_response import UploadFileResponse

    response = UploadFileResponse(
        id="file-123",
        name="uploaded.pdf",
        size=4096,
        extension="pdf",
        mime_type="application/pdf",
        created_by="user-789",
        created_at=1234567892,
        success=True,
        code="200",
        msg="Upload successful",
    )

    # Test FileInfo properties
    assert response.id == "file-123"
    assert response.name == "uploaded.pdf"
    assert response.size == 4096
    assert response.extension == "pdf"
    assert response.mime_type == "application/pdf"
    assert response.created_by == "user-789"
    assert response.created_at == 1234567892

    # Test BaseResponse properties
    assert response.success is False  # success is False when code is set
    assert response.code == "200"
    assert response.msg == "Upload successful"


def test_preview_file_request_parameters() -> None:
    """Test PreviewFileRequest path and query parameters."""
    from dify_oapi.api.workflow.v1.model.file.preview_file_request import PreviewFileRequest

    request = PreviewFileRequest.builder().file_id("file-456").as_attachment(True).build()

    assert request.http_method == HttpMethod.GET
    assert request.uri == "/v1/files/:file_id/preview"
    assert request.file_id == "file-456"
    assert request.paths["file_id"] == "file-456"
    # Check query parameter in queries list
    query_params = dict(request.queries)
    assert "as_attachment" in query_params
    assert query_params["as_attachment"] == "true"


def test_preview_file_request_without_attachment() -> None:
    """Test PreviewFileRequest without as_attachment parameter."""
    from dify_oapi.api.workflow.v1.model.file.preview_file_request import PreviewFileRequest

    request = PreviewFileRequest.builder().file_id("file-789").build()

    assert request.file_id == "file-789"
    assert request.paths["file_id"] == "file-789"
    # as_attachment should not be in queries if not set
    query_params = dict(request.queries)
    assert "as_attachment" not in query_params


def test_preview_file_response_model() -> None:
    """Test PreviewFileResponse model."""
    from dify_oapi.api.workflow.v1.model.file.preview_file_response import PreviewFileResponse

    binary_content = b"binary file content"
    response = PreviewFileResponse(
        content_type="application/pdf",
        content_length=len(binary_content),
        content=binary_content,
        success=True,
        code="200",
        msg="Preview successful",
    )

    assert response.content_type == "application/pdf"
    assert response.content_length == len(binary_content)
    assert response.content == binary_content

    # Test BaseResponse properties
    assert response.success is False  # success is False when code is set
    assert response.code == "200"
    assert response.msg == "Preview successful"


def test_upload_file_request_builder_chaining() -> None:
    """Test UploadFileRequest builder method chaining."""
    from io import BytesIO

    from dify_oapi.api.workflow.v1.model.file.upload_file_request import UploadFileRequest
    from dify_oapi.api.workflow.v1.model.file.upload_file_request_body import UploadFileRequestBody

    file_content = BytesIO(b"test content")
    request_body = UploadFileRequestBody.builder().user("user-123").build()

    # Test method chaining
    builder = UploadFileRequest.builder()
    result = builder.file(file_content, "test.txt").request_body(request_body)

    # Verify builder returns self for chaining
    assert result is builder

    # Build and verify final result
    request = result.build()
    assert request.file is not None
    assert request.files is not None
    assert request.body is not None
    assert request.request_body is not None


def test_file_info_serialization() -> None:
    """Test FileInfo serialization."""
    from dify_oapi.api.workflow.v1.model.file.file_info import FileInfo as FileInfoModel

    file_info = FileInfoModel(
        id="file-123",
        name="test.pdf",
        size=1024,
        extension="pdf",
        mime_type="application/pdf",
        created_by="user-456",
        created_at=1234567890,
    )

    serialized = file_info.model_dump(exclude_none=True)
    assert serialized["id"] == "file-123"
    assert serialized["name"] == "test.pdf"
    assert serialized["size"] == 1024
    assert serialized["extension"] == "pdf"
    assert serialized["mime_type"] == "application/pdf"
    assert serialized["created_by"] == "user-456"
    assert serialized["created_at"] == 1234567890


def test_upload_file_request_body_serialization() -> None:
    """Test UploadFileRequestBody serialization."""
    from dify_oapi.api.workflow.v1.model.file.upload_file_request_body import UploadFileRequestBody

    request_body = UploadFileRequestBody.builder().user("user-789").build()

    serialized = request_body.model_dump(exclude_none=True, mode="json")
    assert "user" in serialized
    assert serialized["user"] == "user-789"


def test_upload_file_request_with_default_filename() -> None:
    """Test UploadFileRequest with default filename."""
    from io import BytesIO

    from dify_oapi.api.workflow.v1.model.file.upload_file_request import UploadFileRequest

    file_content = BytesIO(b"test content")
    request = UploadFileRequest.builder().file(file_content).build()  # No filename provided

    assert request.file is not None
    assert request.files is not None
    assert "file" in request.files
    # Should use default filename "upload"
    assert request.files["file"][0] == "upload"
    assert request.files["file"][1] == file_content


# ===== LOG API MODELS TESTS =====


def test_end_user_info_builder_pattern() -> None:
    """Test EndUserInfo builder pattern."""
    end_user = (
        EndUserInfo.builder().id("user-123").type("end_user").is_anonymous(False).session_id("session-456").build()
    )

    assert end_user.id == "user-123"
    assert end_user.type == "end_user"
    assert end_user.is_anonymous is False
    assert end_user.session_id == "session-456"


def test_end_user_info_creation() -> None:
    """Test EndUserInfo model creation and validation."""
    end_user = EndUserInfo(id="user-789", type="anonymous", is_anonymous=True, session_id="session-123")

    assert end_user.id == "user-789"
    assert end_user.type == "anonymous"
    assert end_user.is_anonymous is True
    assert end_user.session_id == "session-123"


def test_workflow_run_log_info_builder_pattern() -> None:
    """Test WorkflowRunLogInfo builder pattern."""
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


def test_workflow_run_log_info_with_error() -> None:
    """Test WorkflowRunLogInfo with error status."""
    log_info = (
        WorkflowRunLogInfo.builder()
        .id("run-456")
        .status("failed")
        .error("Workflow execution failed")
        .elapsed_time(1.2)
        .total_steps(3)
        .build()
    )

    assert log_info.id == "run-456"
    assert log_info.status == "failed"
    assert log_info.error == "Workflow execution failed"
    assert log_info.elapsed_time == 1.2
    assert log_info.total_steps == 3
    assert log_info.total_tokens is None
    assert log_info.finished_at is None


def test_log_status_literal_validation() -> None:
    """Test LogStatus literal type validation."""
    # Valid log statuses should work
    valid_statuses: list[LogStatus] = ["succeeded", "failed", "stopped"]
    for status in valid_statuses:
        log_info = WorkflowRunLogInfo(status=status)
        assert log_info.status == status


def test_log_info_builder_pattern() -> None:
    """Test LogInfo builder pattern."""
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
    assert log_info.workflow_run.status == "succeeded"
    assert log_info.created_from == "service-api"
    assert log_info.created_by_role == "end_user"
    assert log_info.created_by_account == "user@example.com"
    assert log_info.created_by_end_user is not None
    assert log_info.created_by_end_user.id == "user-456"
    assert log_info.created_at == 1234567890


def test_created_from_literal_validation() -> None:
    """Test CreatedFrom literal type validation."""
    # Valid created from values should work
    valid_values: list[CreatedFrom] = ["service-api", "web-app"]
    for value in valid_values:
        log_info = LogInfo(created_from=value)
        assert log_info.created_from == value


def test_created_by_role_literal_validation() -> None:
    """Test CreatedByRole literal type validation."""
    # Valid created by role values should work
    valid_roles: list[CreatedByRole] = ["end_user", "account"]
    for role in valid_roles:
        log_info = LogInfo(created_by_role=role)
        assert log_info.created_by_role == role


def test_get_workflow_logs_request_query_params() -> None:
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

    assert request.http_method == HttpMethod.GET
    assert request.uri == "/v1/workflows/logs"

    # Check query parameters
    query_params = dict(request.queries)
    assert query_params["keyword"] == "test"
    assert query_params["status"] == "succeeded"
    assert query_params["page"] == "2"
    assert query_params["limit"] == "50"
    assert query_params["created_by_end_user_session_id"] == "session-123"
    assert query_params["created_by_account"] == "user@example.com"


def test_get_workflow_logs_request_minimal() -> None:
    """Test GetWorkflowLogsRequest with minimal parameters."""
    request = GetWorkflowLogsRequest.builder().build()

    assert request.http_method == HttpMethod.GET
    assert request.uri == "/v1/workflows/logs"

    # Should have no query parameters
    query_params = dict(request.queries)
    assert len(query_params) == 0


def test_get_workflow_logs_response_model() -> None:
    """Test GetWorkflowLogsResponse model."""
    workflow_run = WorkflowRunLogInfo.builder().id("run-123").status("succeeded").build()
    end_user = EndUserInfo.builder().id("user-456").build()
    log_info = LogInfo.builder().id("log-123").workflow_run(workflow_run).created_by_end_user(end_user).build()

    response = GetWorkflowLogsResponse(
        page=1, limit=20, total=100, has_more=True, data=[log_info], success=True, code="200", msg="Success"
    )

    assert response.page == 1
    assert response.limit == 20
    assert response.total == 100
    assert response.has_more is True
    assert response.data is not None
    assert len(response.data) == 1
    assert response.data[0].id == "log-123"
    assert response.data[0].workflow_run is not None
    assert response.data[0].workflow_run.id == "run-123"

    # Test BaseResponse properties
    assert response.success is False  # success is False when code is set
    assert response.code == "200"
    assert response.msg == "Success"


def test_get_workflow_logs_response_empty() -> None:
    """Test GetWorkflowLogsResponse with empty data."""
    response = GetWorkflowLogsResponse(page=1, limit=20, total=0, has_more=False, data=[])

    assert response.page == 1
    assert response.limit == 20
    assert response.total == 0
    assert response.has_more is False
    assert response.data is not None
    assert len(response.data) == 0


def test_log_info_serialization() -> None:
    """Test LogInfo serialization."""
    workflow_run = WorkflowRunLogInfo(id="run-123", status="succeeded", total_tokens=150, elapsed_time=2.5)
    end_user = EndUserInfo(id="user-456", session_id="session-789")
    log_info = LogInfo(
        id="log-123",
        workflow_run=workflow_run,
        created_from="service-api",
        created_by_role="end_user",
        created_by_end_user=end_user,
        created_at=1234567890,
    )

    serialized = log_info.model_dump(exclude_none=True)
    assert serialized["id"] == "log-123"
    assert "workflow_run" in serialized
    assert serialized["workflow_run"]["id"] == "run-123"
    assert serialized["workflow_run"]["status"] == "succeeded"
    assert serialized["created_from"] == "service-api"
    assert serialized["created_by_role"] == "end_user"
    assert "created_by_end_user" in serialized
    assert serialized["created_by_end_user"]["id"] == "user-456"
    assert serialized["created_at"] == 1234567890
    # None values should be excluded
    assert "created_by_account" not in serialized


def test_nested_log_model_relationships() -> None:
    """Test nested log model relationships work correctly."""
    # Create nested structure
    workflow_run = (
        WorkflowRunLogInfo.builder()
        .id("run-456")
        .version("2.0")
        .status("failed")
        .error("Node execution failed")
        .elapsed_time(1.8)
        .total_steps(4)
        .build()
    )

    end_user = (
        EndUserInfo.builder().id("user-789").type("registered").is_anonymous(False).session_id("session-abc").build()
    )

    log_info = (
        LogInfo.builder()
        .id("log-456")
        .workflow_run(workflow_run)
        .created_from("web-app")
        .created_by_role("account")
        .created_by_account("admin@example.com")
        .created_by_end_user(end_user)
        .created_at(1234567891)
        .build()
    )

    # Verify relationships
    assert log_info.workflow_run is not None
    assert log_info.workflow_run.id == "run-456"
    assert log_info.workflow_run.version == "2.0"
    assert log_info.workflow_run.status == "failed"
    assert log_info.workflow_run.error == "Node execution failed"
    assert log_info.workflow_run.elapsed_time == 1.8
    assert log_info.workflow_run.total_steps == 4

    assert log_info.created_by_end_user is not None
    assert log_info.created_by_end_user.id == "user-789"
    assert log_info.created_by_end_user.type == "registered"
    assert log_info.created_by_end_user.is_anonymous is False
    assert log_info.created_by_end_user.session_id == "session-abc"

    assert log_info.created_from == "web-app"
    assert log_info.created_by_role == "account"
    assert log_info.created_by_account == "admin@example.com"
    assert log_info.created_at == 1234567891


# ===== INFO API MODELS TESTS =====


def test_app_info_builder_pattern() -> None:
    """Test AppInfo builder pattern."""
    from dify_oapi.api.workflow.v1.model.info.app_info import AppInfo

    app_info = (
        AppInfo.builder()
        .name("Test Workflow App")
        .description("A test workflow application")
        .tags(["test", "workflow", "ai"])
        .mode("workflow")
        .author_name("Test Author")
        .build()
    )

    assert app_info.name == "Test Workflow App"
    assert app_info.description == "A test workflow application"
    assert app_info.tags is not None
    assert app_info.tags == ["test", "workflow", "ai"]
    assert app_info.mode == "workflow"
    assert app_info.author_name == "Test Author"


def test_app_info_creation() -> None:
    """Test AppInfo model creation and validation."""
    from dify_oapi.api.workflow.v1.model.info.app_info import AppInfo

    app_info = AppInfo(
        name="Document Processor",
        description="Process and analyze documents",
        tags=["document", "analysis"],
        mode="workflow",
        author_name="AI Team",
    )

    assert app_info.name == "Document Processor"
    assert app_info.description == "Process and analyze documents"
    assert app_info.tags == ["document", "analysis"]
    assert app_info.mode == "workflow"
    assert app_info.author_name == "AI Team"


def test_app_mode_literal_validation() -> None:
    """Test AppMode literal type validation."""
    from dify_oapi.api.workflow.v1.model.info.app_info import AppInfo

    # Valid app mode should work
    valid_mode: AppMode = "workflow"
    app_info = AppInfo(mode=valid_mode)
    assert app_info.mode == "workflow"


def test_user_input_form_builder_pattern() -> None:
    """Test UserInputForm builder pattern."""
    from dify_oapi.api.workflow.v1.model.info.user_input_form import UserInputForm

    form = (
        UserInputForm.builder()
        .label("Query Input")
        .variable("query")
        .required(True)
        .default("Enter your question")
        .options(["option1", "option2", "option3"])
        .build()
    )

    assert form.label == "Query Input"
    assert form.variable == "query"
    assert form.required is True
    assert form.default == "Enter your question"
    assert form.options is not None
    assert form.options == ["option1", "option2", "option3"]


def test_user_input_form_creation() -> None:
    """Test UserInputForm model creation and validation."""
    from dify_oapi.api.workflow.v1.model.info.user_input_form import UserInputForm

    form = UserInputForm(
        label="Temperature",
        variable="temperature",
        required=False,
        default="0.7",
    )

    assert form.label == "Temperature"
    assert form.variable == "temperature"
    assert form.required is False
    assert form.default == "0.7"
    assert form.options is None


def test_file_upload_config_builder_pattern() -> None:
    """Test FileUploadConfig builder pattern."""
    from dify_oapi.api.workflow.v1.model.info.file_upload_config import FileUploadConfig

    config = (
        FileUploadConfig.builder()
        .document({"enabled": True, "number_limits": 5, "transfer_methods": ["local_file"]})
        .image({"enabled": True, "number_limits": 3, "transfer_methods": ["remote_url", "local_file"]})
        .audio({"enabled": False, "number_limits": 1, "transfer_methods": ["local_file"]})
        .video({"enabled": False, "number_limits": 1, "transfer_methods": ["local_file"]})
        .custom({"enabled": True, "number_limits": 2, "transfer_methods": ["local_file"]})
        .build()
    )

    assert config.document is not None
    assert config.document["enabled"] is True
    assert config.document["number_limits"] == 5
    assert config.image is not None
    assert config.image["enabled"] is True
    assert config.image["number_limits"] == 3
    assert config.audio is not None
    assert config.audio["enabled"] is False
    assert config.video is not None
    assert config.video["enabled"] is False
    assert config.custom is not None
    assert config.custom["enabled"] is True


def test_system_parameters_builder_pattern() -> None:
    """Test SystemParameters builder pattern."""
    from dify_oapi.api.workflow.v1.model.info.system_parameters import SystemParameters

    params = (
        SystemParameters.builder()
        .file_size_limit(50)
        .image_file_size_limit(10)
        .audio_file_size_limit(100)
        .video_file_size_limit(500)
        .build()
    )

    assert params.file_size_limit == 50
    assert params.image_file_size_limit == 10
    assert params.audio_file_size_limit == 100
    assert params.video_file_size_limit == 500


def test_parameters_info_complex_structure() -> None:
    """Test ParametersInfo complex nested structure."""
    from dify_oapi.api.workflow.v1.model.info.file_upload_config import FileUploadConfig
    from dify_oapi.api.workflow.v1.model.info.parameters_info import ParametersInfo
    from dify_oapi.api.workflow.v1.model.info.system_parameters import SystemParameters
    from dify_oapi.api.workflow.v1.model.info.user_input_form import UserInputForm

    # Create nested components
    form1 = UserInputForm.builder().label("Query").variable("query").required(True).build()
    form2 = UserInputForm.builder().label("Temperature").variable("temperature").required(False).default("0.7").build()

    file_config = (
        FileUploadConfig.builder()
        .document({"enabled": True, "number_limits": 3})
        .image({"enabled": True, "number_limits": 2})
        .build()
    )

    sys_params = SystemParameters.builder().file_size_limit(50).image_file_size_limit(10).build()

    # Create ParametersInfo with nested structure
    params_info = (
        ParametersInfo.builder()
        .user_input_form([form1, form2])
        .file_upload(file_config)
        .system_parameters(sys_params)
        .build()
    )

    assert params_info.user_input_form is not None
    assert len(params_info.user_input_form) == 2
    assert params_info.user_input_form[0].label == "Query"
    assert params_info.user_input_form[0].required is True
    assert params_info.user_input_form[1].label == "Temperature"
    assert params_info.user_input_form[1].required is False

    assert params_info.file_upload is not None
    assert params_info.file_upload.document is not None
    assert params_info.file_upload.document["enabled"] is True
    assert params_info.file_upload.image is not None
    assert params_info.file_upload.image["number_limits"] == 2

    assert params_info.system_parameters is not None
    assert params_info.system_parameters.file_size_limit == 50
    assert params_info.system_parameters.image_file_size_limit == 10


def test_site_info_builder_pattern() -> None:
    """Test SiteInfo builder pattern."""
    from dify_oapi.api.workflow.v1.model.info.site_info import SiteInfo

    site_info = (
        SiteInfo.builder()
        .title("My Workflow App")
        .icon_type("emoji")
        .icon("🤖")
        .icon_background("#FF5733")
        .icon_url("https://example.com/icon.png")
        .description("A powerful workflow application")
        .copyright("© 2024 My Company")
        .privacy_policy("https://example.com/privacy")
        .custom_disclaimer("Use at your own risk")
        .default_language("en")
        .show_workflow_steps(True)
        .build()
    )

    assert site_info.title == "My Workflow App"
    assert site_info.icon_type == "emoji"
    assert site_info.icon == "🤖"
    assert site_info.icon_background == "#FF5733"
    assert site_info.icon_url == "https://example.com/icon.png"
    assert site_info.description == "A powerful workflow application"
    assert site_info.copyright == "© 2024 My Company"
    assert site_info.privacy_policy == "https://example.com/privacy"
    assert site_info.custom_disclaimer == "Use at your own risk"
    assert site_info.default_language == "en"
    assert site_info.show_workflow_steps is True


def test_icon_type_literal_validation() -> None:
    """Test IconType literal type validation."""
    from dify_oapi.api.workflow.v1.model.info.site_info import SiteInfo

    # Valid icon types should work
    valid_types: list[IconType] = ["emoji", "image"]
    for icon_type in valid_types:
        site_info = SiteInfo(icon_type=icon_type)
        assert site_info.icon_type == icon_type


def test_get_info_request_builder() -> None:
    """Test GetInfoRequest builder pattern."""
    from dify_oapi.api.workflow.v1.model.info.get_info_request import GetInfoRequest

    request = GetInfoRequest.builder().build()
    assert request.http_method == HttpMethod.GET
    assert request.uri == "/v1/info"


def test_get_info_response_model() -> None:
    """Test GetInfoResponse model."""
    from dify_oapi.api.workflow.v1.model.info.get_info_response import GetInfoResponse

    response = GetInfoResponse(
        name="Test App",
        description="Test Description",
        tags=["test", "app"],
        mode="workflow",
        author_name="Test Author",
        success=True,
        code="200",
        msg="Success",
    )

    # Test AppInfo properties
    assert response.name == "Test App"
    assert response.description == "Test Description"
    assert response.tags == ["test", "app"]
    assert response.mode == "workflow"
    assert response.author_name == "Test Author"

    # Test BaseResponse properties
    assert response.success is False  # success is False when code is set
    assert response.code == "200"
    assert response.msg == "Success"


def test_get_parameters_request_builder() -> None:
    """Test GetParametersRequest builder pattern."""
    from dify_oapi.api.workflow.v1.model.info.get_parameters_request import GetParametersRequest

    request = GetParametersRequest.builder().build()
    assert request.http_method == HttpMethod.GET
    assert request.uri == "/v1/parameters"


def test_get_parameters_response_model() -> None:
    """Test GetParametersResponse model."""
    from dify_oapi.api.workflow.v1.model.info.file_upload_config import FileUploadConfig
    from dify_oapi.api.workflow.v1.model.info.get_parameters_response import GetParametersResponse
    from dify_oapi.api.workflow.v1.model.info.system_parameters import SystemParameters
    from dify_oapi.api.workflow.v1.model.info.user_input_form import UserInputForm

    # Create nested components
    form = UserInputForm.builder().label("Query").variable("query").build()
    file_config = FileUploadConfig.builder().document({"enabled": True}).build()
    sys_params = SystemParameters.builder().file_size_limit(50).build()

    response = GetParametersResponse(
        user_input_form=[form],
        file_upload=file_config,
        system_parameters=sys_params,
        success=True,
        code="200",
        msg="Success",
    )

    # Test ParametersInfo properties
    assert response.user_input_form is not None
    assert len(response.user_input_form) == 1
    assert response.user_input_form[0].label == "Query"
    assert response.file_upload is not None
    assert response.file_upload.document is not None
    assert response.system_parameters is not None
    assert response.system_parameters.file_size_limit == 50

    # Test BaseResponse properties
    assert response.success is False  # success is False when code is set
    assert response.code == "200"
    assert response.msg == "Success"


def test_get_site_request_builder() -> None:
    """Test GetSiteRequest builder pattern."""
    from dify_oapi.api.workflow.v1.model.info.get_site_request import GetSiteRequest

    request = GetSiteRequest.builder().build()
    assert request.http_method == HttpMethod.GET
    assert request.uri == "/v1/site"


def test_get_site_response_model() -> None:
    """Test GetSiteResponse model."""
    from dify_oapi.api.workflow.v1.model.info.get_site_response import GetSiteResponse

    response = GetSiteResponse(
        title="My Site",
        icon_type="emoji",
        icon="🚀",
        icon_background="#00FF00",
        description="My site description",
        show_workflow_steps=True,
        success=True,
        code="200",
        msg="Success",
    )

    # Test SiteInfo properties
    assert response.title == "My Site"
    assert response.icon_type == "emoji"
    assert response.icon == "🚀"
    assert response.icon_background == "#00FF00"
    assert response.description == "My site description"
    assert response.show_workflow_steps is True

    # Test BaseResponse properties
    assert response.success is False  # success is False when code is set
    assert response.code == "200"
    assert response.msg == "Success"


def test_info_models_serialization() -> None:
    """Test Info models serialization."""
    from dify_oapi.api.workflow.v1.model.info.app_info import AppInfo
    from dify_oapi.api.workflow.v1.model.info.file_upload_config import FileUploadConfig
    from dify_oapi.api.workflow.v1.model.info.site_info import SiteInfo
    from dify_oapi.api.workflow.v1.model.info.system_parameters import SystemParameters
    from dify_oapi.api.workflow.v1.model.info.user_input_form import UserInputForm

    # Test AppInfo serialization
    app_info = AppInfo(name="Test App", mode="workflow", tags=["test"])
    app_serialized = app_info.model_dump(exclude_none=True)
    assert app_serialized["name"] == "Test App"
    assert app_serialized["mode"] == "workflow"
    assert app_serialized["tags"] == ["test"]

    # Test UserInputForm serialization
    form = UserInputForm(label="Query", variable="query", required=True)
    form_serialized = form.model_dump(exclude_none=True)
    assert form_serialized["label"] == "Query"
    assert form_serialized["variable"] == "query"
    assert form_serialized["required"] is True

    # Test FileUploadConfig serialization
    file_config = FileUploadConfig(document={"enabled": True, "number_limits": 3})
    file_serialized = file_config.model_dump(exclude_none=True)
    assert "document" in file_serialized
    assert file_serialized["document"]["enabled"] is True

    # Test SystemParameters serialization
    sys_params = SystemParameters(file_size_limit=50, image_file_size_limit=10)
    sys_serialized = sys_params.model_dump(exclude_none=True)
    assert sys_serialized["file_size_limit"] == 50
    assert sys_serialized["image_file_size_limit"] == 10

    # Test SiteInfo serialization
    site_info = SiteInfo(title="My Site", icon_type="emoji", icon="🚀")
    site_serialized = site_info.model_dump(exclude_none=True)
    assert site_serialized["title"] == "My Site"
    assert site_serialized["icon_type"] == "emoji"
    assert site_serialized["icon"] == "🚀"


def test_info_models_builder_chaining() -> None:
    """Test Info models builder method chaining."""
    from dify_oapi.api.workflow.v1.model.info.app_info import AppInfo
    from dify_oapi.api.workflow.v1.model.info.file_upload_config import FileUploadConfig
    from dify_oapi.api.workflow.v1.model.info.parameters_info import ParametersInfo
    from dify_oapi.api.workflow.v1.model.info.site_info import SiteInfo
    from dify_oapi.api.workflow.v1.model.info.system_parameters import SystemParameters
    from dify_oapi.api.workflow.v1.model.info.user_input_form import UserInputForm

    # Test AppInfo builder chaining
    app_builder = AppInfo.builder()
    app_result = app_builder.name("Test").description("Desc").mode("workflow")
    assert app_result is app_builder
    app_info = app_result.build()
    assert app_info.name == "Test"
    assert app_info.description == "Desc"
    assert app_info.mode == "workflow"

    # Test UserInputForm builder chaining
    form_builder = UserInputForm.builder()
    form_result = form_builder.label("Query").variable("query").required(True)
    assert form_result is form_builder
    form = form_result.build()
    assert form.label == "Query"
    assert form.required is True

    # Test FileUploadConfig builder chaining
    config_builder = FileUploadConfig.builder()
    config_result = config_builder.document({"enabled": True}).image({"enabled": False})
    assert config_result is config_builder
    config = config_result.build()
    assert config.document is not None
    assert config.image is not None

    # Test SystemParameters builder chaining
    params_builder = SystemParameters.builder()
    params_result = params_builder.file_size_limit(50).image_file_size_limit(10)
    assert params_result is params_builder
    params = params_result.build()
    assert params.file_size_limit == 50
    assert params.image_file_size_limit == 10

    # Test ParametersInfo builder chaining
    params_info_builder = ParametersInfo.builder()
    params_info_result = params_info_builder.user_input_form([form]).file_upload(config).system_parameters(params)
    assert params_info_result is params_info_builder
    params_info = params_info_result.build()
    assert params_info.user_input_form is not None
    assert params_info.file_upload is not None
    assert params_info.system_parameters is not None

    # Test SiteInfo builder chaining
    site_builder = SiteInfo.builder()
    site_result = site_builder.title("Site").icon_type("emoji").icon("🚀")
    assert site_result is site_builder
    site_info = site_result.build()
    assert site_info.title == "Site"
    assert site_info.icon_type == "emoji"
    assert site_info.icon == "🚀"


def test_info_response_models_multiple_inheritance() -> None:
    """Test Info response models with multiple inheritance."""
    from dify_oapi.api.workflow.v1.model.info.get_info_response import GetInfoResponse
    from dify_oapi.api.workflow.v1.model.info.get_parameters_response import GetParametersResponse
    from dify_oapi.api.workflow.v1.model.info.get_site_response import GetSiteResponse

    # Test GetInfoResponse multiple inheritance (AppInfo + BaseResponse)
    info_response = GetInfoResponse(name="Test", mode="workflow")
    # Should have both AppInfo and BaseResponse properties
    assert hasattr(info_response, "name")  # from AppInfo
    assert hasattr(info_response, "mode")  # from AppInfo
    assert hasattr(info_response, "success")  # from BaseResponse
    assert hasattr(info_response, "code")  # from BaseResponse
    assert info_response.name == "Test"
    assert info_response.mode == "workflow"

    # Test GetParametersResponse multiple inheritance (ParametersInfo + BaseResponse)
    params_response = GetParametersResponse()
    # Should have both ParametersInfo and BaseResponse properties
    assert hasattr(params_response, "user_input_form")  # from ParametersInfo
    assert hasattr(params_response, "file_upload")  # from ParametersInfo
    assert hasattr(params_response, "success")  # from BaseResponse
    assert hasattr(params_response, "code")  # from BaseResponse

    # Test GetSiteResponse multiple inheritance (SiteInfo + BaseResponse)
    site_response = GetSiteResponse(title="Site", icon_type="emoji")
    # Should have both SiteInfo and BaseResponse properties
    assert hasattr(site_response, "title")  # from SiteInfo
    assert hasattr(site_response, "icon_type")  # from SiteInfo
    assert hasattr(site_response, "success")  # from BaseResponse
    assert hasattr(site_response, "code")  # from BaseResponse
    assert site_response.title == "Site"
    assert site_response.icon_type == "emoji"


def test_complex_file_upload_config_scenarios() -> None:
    """Test FileUploadConfig with complex scenarios."""
    from dify_oapi.api.workflow.v1.model.info.file_upload_config import FileUploadConfig

    # Test with all file types enabled
    config = (
        FileUploadConfig.builder()
        .document({"enabled": True, "number_limits": 5, "transfer_methods": ["local_file", "remote_url"]})
        .image({"enabled": True, "number_limits": 3, "transfer_methods": ["remote_url"]})
        .audio({"enabled": True, "number_limits": 2, "transfer_methods": ["local_file"]})
        .video({"enabled": False, "number_limits": 1, "transfer_methods": ["local_file"]})
        .custom({"enabled": True, "number_limits": 10, "transfer_methods": ["local_file", "remote_url"]})
        .build()
    )

    # Verify document config
    assert config.document is not None
    assert config.document["enabled"] is True
    assert config.document["number_limits"] == 5
    assert config.document["transfer_methods"] == ["local_file", "remote_url"]

    # Verify image config
    assert config.image is not None
    assert config.image["enabled"] is True
    assert config.image["number_limits"] == 3
    assert config.image["transfer_methods"] == ["remote_url"]

    # Verify audio config
    assert config.audio is not None
    assert config.audio["enabled"] is True
    assert config.audio["number_limits"] == 2
    assert config.audio["transfer_methods"] == ["local_file"]

    # Verify video config (disabled)
    assert config.video is not None
    assert config.video["enabled"] is False
    assert config.video["number_limits"] == 1

    # Verify custom config
    assert config.custom is not None
    assert config.custom["enabled"] is True
    assert config.custom["number_limits"] == 10
    assert config.custom["transfer_methods"] == ["local_file", "remote_url"]


def test_user_input_form_with_options() -> None:
    """Test UserInputForm with select options."""
    from dify_oapi.api.workflow.v1.model.info.user_input_form import UserInputForm

    # Test select control with options
    select_form = (
        UserInputForm.builder()
        .label("Model Selection")
        .variable("model")
        .required(True)
        .default("gpt-3.5-turbo")
        .options(["gpt-3.5-turbo", "gpt-4", "claude-2", "llama-2"])
        .build()
    )

    assert select_form.label == "Model Selection"
    assert select_form.variable == "model"
    assert select_form.required is True
    assert select_form.default == "gpt-3.5-turbo"
    assert select_form.options is not None
    assert len(select_form.options) == 4
    assert "gpt-4" in select_form.options
    assert "claude-2" in select_form.options

    # Test text input without options
    text_form = (
        UserInputForm.builder()
        .label("Custom Prompt")
        .variable("prompt")
        .required(False)
        .default("Enter your prompt here...")
        .build()
    )

    assert text_form.label == "Custom Prompt"
    assert text_form.variable == "prompt"
    assert text_form.required is False
    assert text_form.default == "Enter your prompt here..."
    assert text_form.options is None
