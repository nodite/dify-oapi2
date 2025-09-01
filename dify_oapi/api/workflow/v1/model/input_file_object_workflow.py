"""Input file object for workflow multimodal support.

This module defines the InputFileObjectWorkflow model for handling file inputs
in workflow execution with proper validation rules.
"""

from typing import Optional

from pydantic import BaseModel, model_validator

from .workflow_types import FileType, TransferMethod


class InputFileObjectWorkflow(BaseModel):
    """File input object for workflow execution.

    Supports both remote URL and local file upload methods with validation rules:
    - When transfer_method is "remote_url": url is required, upload_file_id must be None
    - When transfer_method is "local_file": upload_file_id is required, url must be None
    """

    type: FileType
    transfer_method: TransferMethod
    url: Optional[str] = None
    upload_file_id: Optional[str] = None

    @model_validator(mode="after")
    def validate_transfer_method_fields(self):
        """Validate that the correct fields are provided based on transfer_method."""
        if self.transfer_method == "remote_url":
            if not self.url:
                raise ValueError("url is required when transfer_method is 'remote_url'")
            if self.upload_file_id is not None:
                raise ValueError("upload_file_id must be None when transfer_method is 'remote_url'")
        elif self.transfer_method == "local_file":
            if not self.upload_file_id:
                raise ValueError("upload_file_id is required when transfer_method is 'local_file'")
            if self.url is not None:
                raise ValueError("url must be None when transfer_method is 'local_file'")
        return self

    @staticmethod
    def builder() -> "InputFileObjectWorkflowBuilder":
        """Create a new InputFileObjectWorkflow builder."""
        return InputFileObjectWorkflowBuilder()


class InputFileObjectWorkflowBuilder:
    """Builder for InputFileObjectWorkflow."""

    def __init__(self):
        self._input_file_object_workflow = InputFileObjectWorkflow(type="document", transfer_method="local_file")

    def build(self) -> InputFileObjectWorkflow:
        """Build the InputFileObjectWorkflow instance."""
        return self._input_file_object_workflow

    def type(self, file_type: FileType) -> "InputFileObjectWorkflowBuilder":
        """Set the file type."""
        self._input_file_object_workflow.type = file_type
        return self

    def transfer_method(self, transfer_method: TransferMethod) -> "InputFileObjectWorkflowBuilder":
        """Set the transfer method."""
        self._input_file_object_workflow.transfer_method = transfer_method
        return self

    def url(self, url: str) -> "InputFileObjectWorkflowBuilder":
        """Set the remote URL (for remote_url transfer method)."""
        self._input_file_object_workflow.url = url
        return self

    def upload_file_id(self, upload_file_id: str) -> "InputFileObjectWorkflowBuilder":
        """Set the upload file ID (for local_file transfer method)."""
        self._input_file_object_workflow.upload_file_id = upload_file_id
        return self
