from typing import Literal

# Response mode types
ResponseMode = Literal["streaming", "blocking"]

# File types
FileType = Literal["document", "image", "audio", "video", "custom"]

# Transfer method types
TransferMethod = Literal["remote_url", "local_file"]

# Workflow status types
WorkflowStatus = Literal["running", "succeeded", "failed", "stopped"]

# Event types
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

# Node types
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

# Icon types
IconType = Literal["emoji", "image"]

# App mode types
AppMode = Literal["workflow"]

# Log status types
LogStatus = Literal["succeeded", "failed", "stopped"]

# Created by role types
CreatedByRole = Literal["end_user", "account"]

# Created from types
CreatedFrom = Literal["service-api", "web-app"]
