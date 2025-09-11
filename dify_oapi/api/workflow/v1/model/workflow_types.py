"""Workflow API type definitions.

This module contains all Literal type definitions for the Workflow API,
ensuring strict type safety throughout the workflow module.
"""

from typing import Literal

# Response mode types for workflow execution
ResponseMode = Literal["streaming", "blocking"]

# File types supported in workflow inputs
FileType = Literal["document", "image", "audio", "video", "custom"]

# File transfer methods
TransferMethod = Literal["remote_url", "local_file"]

# Workflow execution status
WorkflowStatus = Literal["running", "succeeded", "failed", "stopped"]

# Node execution status
NodeStatus = Literal["running", "succeeded", "failed", "stopped"]

# Streaming event types
EventType = Literal[
    "workflow_started",
    "node_started",
    "text_chunk",
    "node_finished",
    "workflow_finished",
    "tts_message",
    "tts_message_end",
    "ping",
]

# Workflow node types
NodeType = Literal[
    "start",
    "end",
    "llm",
    "code",
    "template",
    "knowledge_retrieval",
    "question_classifier",
    "if_else",
    "variable_assigner",
    "parameter_extractor",
]

# WebApp icon types
IconType = Literal["emoji", "image"]

# Application mode types
AppMode = Literal["workflow"]

# Log status filter types (includes "running" for filtering)
LogStatus = Literal["succeeded", "failed", "stopped", "running"]

# Creator role types
CreatedByRole = Literal["end_user", "account"]

# Creation source types
CreatedFrom = Literal["service-api", "web-app"]

# User input form control types
UserInputFormType = Literal["text-input", "paragraph", "select"]

# UUID format validation pattern
UUID_PATTERN = r"^[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}$"
