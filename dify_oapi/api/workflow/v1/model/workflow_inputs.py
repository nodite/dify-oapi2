from __future__ import annotations

from typing import Union

from pydantic import BaseModel

from .workflow_file_info import WorkflowFileInfo

# Define specific types for workflow input values
WorkflowInputValue = Union[
    str,  # Text values
    int,  # Integer values
    float,  # Float values
    bool,  # Boolean values
    list[WorkflowFileInfo],  # File list type variables
    list[str],  # String arrays
    dict[str, Union[str, int, float, bool]],  # Object values
]


class WorkflowInputs(BaseModel):
    # Dynamic inputs based on workflow configuration
    # Can contain any key-value pairs defined by the workflow
    inputs: dict[str, WorkflowInputValue] | None = None

    @staticmethod
    def builder() -> WorkflowInputsBuilder:
        return WorkflowInputsBuilder()

    def add_input(self, key: str, value: WorkflowInputValue) -> None:
        if self.inputs is None:
            self.inputs = {}
        self.inputs[key] = value

    def get_input(self, key: str) -> WorkflowInputValue | None:
        if self.inputs is None:
            return None
        return self.inputs.get(key)


class WorkflowInputsBuilder:
    def __init__(self):
        self._workflow_inputs = WorkflowInputs()

    def build(self) -> WorkflowInputs:
        return self._workflow_inputs

    def inputs(self, inputs: dict[str, WorkflowInputValue]) -> WorkflowInputsBuilder:
        self._workflow_inputs.inputs = inputs
        return self

    def add_input(self, key: str, value: WorkflowInputValue) -> WorkflowInputsBuilder:
        if self._workflow_inputs.inputs is None:
            self._workflow_inputs.inputs = {}
        self._workflow_inputs.inputs[key] = value
        return self
