"""Node finished event data model.

This module defines the data structure for node_finished streaming events.
"""

from typing import Any, Optional

from pydantic import BaseModel

from .execution_metadata import ExecutionMetadata
from .workflow_types import NodeStatus, NodeType


class NodeFinishedData(BaseModel):
    """Data structure for node_finished streaming event."""

    id: str
    node_id: str
    node_type: NodeType
    title: str
    index: int
    predecessor_node_id: Optional[str] = None
    inputs: Optional[dict[str, Any]] = None
    process_data: Optional[dict[str, Any]] = None
    outputs: Optional[dict[str, Any]] = None
    status: NodeStatus
    error: Optional[str] = None
    elapsed_time: Optional[float] = None
    execution_metadata: Optional[ExecutionMetadata] = None
    created_at: int

    @staticmethod
    def builder() -> "NodeFinishedDataBuilder":
        """Create a new NodeFinishedData builder."""
        return NodeFinishedDataBuilder()


class NodeFinishedDataBuilder:
    """Builder for NodeFinishedData."""

    def __init__(self):
        self._node_finished_data = NodeFinishedData(
            id="", node_id="", node_type="start", title="", index=0, status="succeeded", created_at=0
        )

    def build(self) -> NodeFinishedData:
        """Build the NodeFinishedData instance."""
        return self._node_finished_data

    def id(self, id: str) -> "NodeFinishedDataBuilder":
        """Set the node execution ID."""
        self._node_finished_data.id = id
        return self

    def node_id(self, node_id: str) -> "NodeFinishedDataBuilder":
        """Set the node ID."""
        self._node_finished_data.node_id = node_id
        return self

    def node_type(self, node_type: NodeType) -> "NodeFinishedDataBuilder":
        """Set the node type."""
        self._node_finished_data.node_type = node_type
        return self

    def title(self, title: str) -> "NodeFinishedDataBuilder":
        """Set the node title."""
        self._node_finished_data.title = title
        return self

    def index(self, index: int) -> "NodeFinishedDataBuilder":
        """Set the node index."""
        self._node_finished_data.index = index
        return self

    def predecessor_node_id(self, predecessor_node_id: str) -> "NodeFinishedDataBuilder":
        """Set the predecessor node ID."""
        self._node_finished_data.predecessor_node_id = predecessor_node_id
        return self

    def inputs(self, inputs: dict[str, Any]) -> "NodeFinishedDataBuilder":
        """Set the node inputs."""
        self._node_finished_data.inputs = inputs
        return self

    def process_data(self, process_data: dict[str, Any]) -> "NodeFinishedDataBuilder":
        """Set the process data."""
        self._node_finished_data.process_data = process_data
        return self

    def outputs(self, outputs: dict[str, Any]) -> "NodeFinishedDataBuilder":
        """Set the node outputs."""
        self._node_finished_data.outputs = outputs
        return self

    def status(self, status: NodeStatus) -> "NodeFinishedDataBuilder":
        """Set the node status."""
        self._node_finished_data.status = status
        return self

    def error(self, error: str) -> "NodeFinishedDataBuilder":
        """Set the error message."""
        self._node_finished_data.error = error
        return self

    def elapsed_time(self, elapsed_time: float) -> "NodeFinishedDataBuilder":
        """Set the elapsed time."""
        self._node_finished_data.elapsed_time = elapsed_time
        return self

    def execution_metadata(self, execution_metadata: ExecutionMetadata) -> "NodeFinishedDataBuilder":
        """Set the execution metadata."""
        self._node_finished_data.execution_metadata = execution_metadata
        return self

    def created_at(self, created_at: int) -> "NodeFinishedDataBuilder":
        """Set the creation timestamp."""
        self._node_finished_data.created_at = created_at
        return self
