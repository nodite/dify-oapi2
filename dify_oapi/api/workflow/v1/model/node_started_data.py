"""Node started event data model.

This module defines the data structure for node_started streaming events.
"""

from typing import Any, Optional

from pydantic import BaseModel

from .workflow_types import NodeType


class NodeStartedData(BaseModel):
    """Data structure for node_started streaming event."""

    id: str
    node_id: str
    node_type: NodeType
    title: str
    index: int
    predecessor_node_id: Optional[str] = None
    inputs: dict[str, Any]
    created_at: int

    @staticmethod
    def builder() -> "NodeStartedDataBuilder":
        """Create a new NodeStartedData builder."""
        return NodeStartedDataBuilder()


class NodeStartedDataBuilder:
    """Builder for NodeStartedData."""

    def __init__(self):
        self._node_started_data = NodeStartedData(
            id="", node_id="", node_type="start", title="", index=0, inputs={}, created_at=0
        )

    def build(self) -> NodeStartedData:
        """Build the NodeStartedData instance."""
        return self._node_started_data

    def id(self, id: str) -> "NodeStartedDataBuilder":
        """Set the node execution ID."""
        self._node_started_data.id = id
        return self

    def node_id(self, node_id: str) -> "NodeStartedDataBuilder":
        """Set the node ID."""
        self._node_started_data.node_id = node_id
        return self

    def node_type(self, node_type: NodeType) -> "NodeStartedDataBuilder":
        """Set the node type."""
        self._node_started_data.node_type = node_type
        return self

    def title(self, title: str) -> "NodeStartedDataBuilder":
        """Set the node title."""
        self._node_started_data.title = title
        return self

    def index(self, index: int) -> "NodeStartedDataBuilder":
        """Set the node index."""
        self._node_started_data.index = index
        return self

    def predecessor_node_id(self, predecessor_node_id: str) -> "NodeStartedDataBuilder":
        """Set the predecessor node ID."""
        self._node_started_data.predecessor_node_id = predecessor_node_id
        return self

    def inputs(self, inputs: dict[str, Any]) -> "NodeStartedDataBuilder":
        """Set the node inputs."""
        self._node_started_data.inputs = inputs
        return self

    def created_at(self, created_at: int) -> "NodeStartedDataBuilder":
        """Set the creation timestamp."""
        self._node_started_data.created_at = created_at
        return self
