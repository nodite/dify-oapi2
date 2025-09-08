"""Chat API type definitions for strict type safety."""

from typing import Literal

# Response mode types
ResponseMode = Literal["streaming", "blocking"]

# File types
FileType = Literal["image"]

# Transfer method types
TransferMethod = Literal["remote_url", "local_file"]

# Rating types
Rating = Literal["like", "dislike"]

# Sort types
SortBy = Literal["created_at", "-created_at", "updated_at", "-updated_at"]

# Icon types
IconType = Literal["emoji", "image"]

# Auto play types
AutoPlay = Literal["enabled", "disabled"]

# Annotation action types
AnnotationAction = Literal["enable", "disable"]

# Job status types
JobStatus = Literal["waiting", "running", "completed", "failed"]

# Message belongs to types
MessageBelongsTo = Literal["user", "assistant"]

# Conversation status types
ConversationStatus = Literal["normal", "archived"]

# Variable value types
VariableValueType = Literal["string", "number", "select"]

# Form input types
FormInputType = Literal["text-input", "paragraph", "select"]

# Streaming event types
StreamingEventType = Literal[
    "message",
    "agent_message",
    "tts_message",
    "tts_message_end",
    "agent_thought",
    "message_file",
    "message_end",
    "message_replace",
    "error",
    "ping",
]

# Audio file formats
AudioFormat = Literal["mp3", "mp4", "mpeg", "mpga", "m4a", "wav", "webm"]

# Image file formats
ImageFormat = Literal["png", "jpg", "jpeg", "webp", "gif"]

# HTTP status codes
HttpStatusCode = Literal[200, 204, 400, 401, 403, 404, 413, 415, 429, 500, 503]
