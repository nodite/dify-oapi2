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
