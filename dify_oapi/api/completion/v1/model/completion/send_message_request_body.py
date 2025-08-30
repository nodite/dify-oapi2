from __future__ import annotations

from typing import Any

from pydantic import BaseModel, field_validator

from .completion_inputs import CompletionInputs
from .completion_types import ResponseMode
from .input_file_object import InputFileObject


class SendMessageRequestBody(BaseModel):
    """Request body for sending completion messages."""

    inputs: dict[str, Any]  # Variable values defined by the App, must include 'query'
    response_mode: ResponseMode | None = "streaming"
    user: str | None = None
    files: list[InputFileObject] | None = None

    @field_validator("inputs")
    @classmethod
    def validate_inputs(cls, v):
        """Validate that inputs contains the required 'query' field."""
        if not isinstance(v, dict):
            raise ValueError("inputs must be a dictionary")
        if "query" not in v:
            raise ValueError('inputs must contain a "query" field')
        if not isinstance(v["query"], str):
            raise ValueError("query field must be a string")
        return v

    @staticmethod
    def builder() -> SendMessageRequestBodyBuilder:
        return SendMessageRequestBodyBuilder()


class SendMessageRequestBodyBuilder:
    def __init__(self):
        self._send_message_request_body = SendMessageRequestBody(inputs={"query": ""})

    def build(self) -> SendMessageRequestBody:
        return self._send_message_request_body

    def inputs(self, inputs: CompletionInputs | dict[str, Any]) -> SendMessageRequestBodyBuilder:
        """Set inputs from CompletionInputs object or dictionary."""
        if isinstance(inputs, CompletionInputs):
            self._send_message_request_body.inputs = inputs.model_dump()
        else:
            self._send_message_request_body.inputs = inputs
        return self

    def query(self, query: str) -> SendMessageRequestBodyBuilder:
        """Set the query field directly."""
        self._send_message_request_body.inputs["query"] = query
        return self

    def add_variable(self, key: str, value: str) -> SendMessageRequestBodyBuilder:
        """Add a custom variable to inputs."""
        self._send_message_request_body.inputs[key] = value
        return self

    def response_mode(self, response_mode: ResponseMode) -> SendMessageRequestBodyBuilder:
        self._send_message_request_body.response_mode = response_mode
        return self

    def user(self, user: str) -> SendMessageRequestBodyBuilder:
        self._send_message_request_body.user = user
        return self

    def files(self, files: list[InputFileObject]) -> SendMessageRequestBodyBuilder:
        self._send_message_request_body.files = files
        return self
