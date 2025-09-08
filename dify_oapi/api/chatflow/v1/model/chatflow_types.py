"""Strict type definitions for all Chatflow API enums and constants.

This module defines all Literal types used throughout the Chatflow API
to ensure type safety and prevent invalid values.
"""

from typing import Literal

# Response mode types for chat messages
ResponseMode = Literal["streaming", "blocking"]
"""Response mode for chat messages. 
- streaming: Real-time streaming response
- blocking: Complete response after processing (Cloudflare timeout is 100s)
"""

# File types for file attachments
FileType = Literal["document", "image", "audio", "video", "custom"]
"""File type for attachments.
- document: TXT, MD, PDF, HTML, XLSX, DOCX, CSV, EML, MSG, PPTX, XML, EPUB
- image: JPG, PNG, GIF, WEBP, SVG
- audio: MP3, M4A, WAV, WEBM, AMR
- video: MP4, MOV, MPEG, MPGA
- custom: Custom file type
"""

# Transfer method types for file handling
TransferMethod = Literal["remote_url", "local_file"]
"""Transfer method for file handling.
- remote_url: File URL for remote files
- local_file: File upload for local files
"""

# Stream event types for real-time responses
StreamEvent = Literal[
    "message",
    "message_file",
    "message_end",
    "tts_message",
    "tts_message_end",
    "message_replace",
    "workflow_started",
    "node_started",
    "node_finished",
    "workflow_finished",
    "error",
    "ping",
]
"""Stream event types for real-time chat responses.
- message: Chat message content chunk
- message_file: File attachment information
- message_end: End of message with metadata
- tts_message: Text-to-speech audio chunk (Base64 encoded)
- tts_message_end: End of TTS conversion
- message_replace: Replace previous message content
- workflow_started: Workflow execution started
- node_started: Workflow node execution started
- node_finished: Workflow node execution finished
- workflow_finished: Workflow execution completed
- error: Error occurred during processing
- ping: Keep-alive ping
"""

# Message file belongs to types
MessageFileBelongsTo = Literal["user", "assistant"]
"""Message file ownership.
- user: File belongs to user
- assistant: File belongs to assistant
"""

# Feedback rating types
FeedbackRating = Literal["like", "dislike"]
"""Feedback rating types.
- like: Positive feedback
- dislike: Negative feedback
"""

# Sort by types for conversation listing
SortBy = Literal["created_at", "-created_at", "updated_at", "-updated_at"]
"""Sort by options for conversation listing.
- created_at: Sort by creation time (ascending)
- -created_at: Sort by creation time (descending)
- updated_at: Sort by update time (ascending)
- -updated_at: Sort by update time (descending)
"""

# Conversation status types
ConversationStatus = Literal["normal", "archived"]
"""Conversation status types.
- normal: Active conversation
- archived: Archived conversation
"""

# Variable value types
VariableValueType = Literal["string", "number", "select"]
"""Variable value types for conversation variables.
- string: String value
- number: Numeric value
- select: Selection value
"""

# Form input types for user input forms
FormInputType = Literal["text-input", "paragraph", "select"]
"""Form input types for user input forms.
- text-input: Single line text input
- paragraph: Multi-line text input
- select: Selection dropdown
"""

# Job status types for annotation operations
JobStatus = Literal["waiting", "running", "completed", "failed"]
"""Job status types for annotation operations.
- waiting: Job is waiting to start
- running: Job is currently running
- completed: Job completed successfully
- failed: Job failed with error
"""

# Audio format types for TTS operations
AudioFormat = Literal["mp3", "mp4", "mpeg", "mpga", "m4a", "wav", "webm"]
"""Audio format types for TTS operations.
- mp3: MP3 audio format
- mp4: MP4 audio format
- mpeg: MPEG audio format
- mpga: MPGA audio format
- m4a: M4A audio format
- wav: WAV audio format
- webm: WebM audio format
"""

# Language codes for internationalization
LanguageCode = Literal["en", "zh", "ja", "ko", "es", "fr", "de", "it", "pt", "ru"]
"""Language codes for internationalization.
- en: English
- zh: Chinese
- ja: Japanese
- ko: Korean
- es: Spanish
- fr: French
- de: German
- it: Italian
- pt: Portuguese
- ru: Russian
"""

# Chat color theme types
ChatColorTheme = Literal["blue", "green", "purple", "orange", "red"]
"""Chat color theme types for UI customization.
- blue: Blue theme
- green: Green theme
- purple: Purple theme
- orange: Orange theme
- red: Red theme
"""

# Default language types for application settings
DefaultLanguage = Literal[
    "en-US", "zh-Hans", "zh-Hant", "ja-JP", "ko-KR", "es-ES", "fr-FR", "de-DE", "it-IT", "pt-BR", "ru-RU"
]
"""Default language types for application settings.
- en-US: English (United States)
- zh-Hans: Chinese (Simplified)
- zh-Hant: Chinese (Traditional)
- ja-JP: Japanese (Japan)
- ko-KR: Korean (Korea)
- es-ES: Spanish (Spain)
- fr-FR: French (France)
- de-DE: German (Germany)
- it-IT: Italian (Italy)
- pt-BR: Portuguese (Brazil)
- ru-RU: Russian (Russia)
"""

# Icon types for application settings
IconType = Literal["emoji", "image"]
"""Icon types for application settings.
- emoji: Emoji icon
- image: Image icon
"""

# AutoPlay types for TTS settings
AutoPlay = Literal["enabled", "disabled"]
"""AutoPlay types for TTS settings.
- enabled: Auto-play enabled
- disabled: Auto-play disabled
"""

# Annotation action types
AnnotationAction = Literal["enable", "disable"]
"""Annotation action types for reply settings.
- enable: Enable annotation reply
- disable: Disable annotation reply
"""

# Node status types for workflow operations
NodeStatus = Literal["running", "succeeded", "failed", "stopped"]
"""Node status types for workflow operations.
- running: Node is currently running
- succeeded: Node completed successfully
- failed: Node failed with error
- stopped: Node was stopped
"""

# Workflow status types
WorkflowStatus = Literal["running", "succeeded", "failed", "stopped"]
"""Workflow status types.
- running: Workflow is currently running
- succeeded: Workflow completed successfully
- failed: Workflow failed with error
- stopped: Workflow was stopped
"""
