from __future__ import annotations

from typing import Any

from pydantic import BaseModel

from .execution_metadata import ExecutionMetadata
from .workflow_types import NodeType, WorkflowStatus


class NodeInfo(BaseModel):
    id: str | None = None
    node_id: str | None = None
    node_type: NodeType | None = None
    title: str | None = None
    index: int | None = None
    predecessor_node_id: str | None = None
    inputs: dict[str, Any] | None = None
    outputs: dict[str, Any] | None = None
    status: WorkflowStatus | None = None
    error: str | None = None
    elapsed_time: float | None = None
    execution_metadata: ExecutionMetadata | None = None
    created_at: int | None = None

    @staticmethod
    def builder() -> NodeInfoBuilder:
        return NodeInfoBuilder()


class NodeInfoBuilder:
    def __init__(self):
        self._node_info = NodeInfo()

    def build(self) -> NodeInfo:
        return self._node_info

    def id(self, id: str) -> NodeInfoBuilder:
        self._node_info.id = id
        return self

    def node_id(self, node_id: str) -> NodeInfoBuilder:
        self._node_info.node_id = node_id
        return self

    def node_type(self, node_type: NodeType) -> NodeInfoBuilder:
        self._node_info.node_type = node_type
        return self

    def title(self, title: str) -> NodeInfoBuilder:
        self._node_info.title = title
        return self

    def index(self, index: int) -> NodeInfoBuilder:
        self._node_info.index = index
        return self

    def predecessor_node_id(self, predecessor_node_id: str) -> NodeInfoBuilder:
        self._node_info.predecessor_node_id = predecessor_node_id
        return self

    def inputs(self, inputs: dict[str, Any]) -> NodeInfoBuilder:
        self._node_info.inputs = inputs
        return self

    def outputs(self, outputs: dict[str, Any]) -> NodeInfoBuilder:
        self._node_info.outputs = outputs
        return self

    def status(self, status: WorkflowStatus) -> NodeInfoBuilder:
        self._node_info.status = status
        return self

    def error(self, error: str) -> NodeInfoBuilder:
        self._node_info.error = error
        return self

    def elapsed_time(self, elapsed_time: float) -> NodeInfoBuilder:
        self._node_info.elapsed_time = elapsed_time
        return self

    def execution_metadata(self, execution_metadata: ExecutionMetadata) -> NodeInfoBuilder:
        self._node_info.execution_metadata = execution_metadata
        return self

    def created_at(self, created_at: int) -> NodeInfoBuilder:
        self._node_info.created_at = created_at
        return self
