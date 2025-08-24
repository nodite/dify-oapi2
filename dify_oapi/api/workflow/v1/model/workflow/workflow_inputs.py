from __future__ import annotations

from typing import Any

from pydantic import BaseModel


class WorkflowInputs(BaseModel):
    # Dynamic inputs based on workflow configuration
    # Can contain any key-value pairs defined by the workflow
    inputs: dict[str, Any] | None = None

    @staticmethod
    def builder() -> WorkflowInputsBuilder:
        return WorkflowInputsBuilder()

    def add_input(self, key: str, value: Any) -> None:
        if self.inputs is None:
            self.inputs = {}
        self.inputs[key] = value

    def get_input(self, key: str) -> Any:
        if self.inputs is None:
            return None
        return self.inputs.get(key)


class WorkflowInputsBuilder:
    def __init__(self):
        self._workflow_inputs = WorkflowInputs()

    def build(self) -> WorkflowInputs:
        return self._workflow_inputs

    def inputs(self, inputs: dict[str, Any]) -> WorkflowInputsBuilder:
        self._workflow_inputs.inputs = inputs
        return self

    def add_input(self, key: str, value: Any) -> WorkflowInputsBuilder:
        if self._workflow_inputs.inputs is None:
            self._workflow_inputs.inputs = {}
        self._workflow_inputs.inputs[key] = value
        return self
