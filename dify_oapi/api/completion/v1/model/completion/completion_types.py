from __future__ import annotations

from typing import Literal

# Response mode types
ResponseMode = Literal["streaming", "blocking"]

# File types
FileType = Literal["image"]

# Transfer method types
TransferMethod = Literal["remote_url", "local_file"]

# Feedback rating types
FeedbackRating = Literal["like", "dislike"]

# Annotation action types
AnnotationAction = Literal["enable", "disable"]

# Icon types
IconType = Literal["emoji", "image"]

# App mode types
AppMode = Literal["completion"]

# Job status types
JobStatus = Literal["waiting", "running", "completed", "failed"]

# Event types for streaming
EventType = Literal["message", "message_end", "tts_message", "tts_message_end", "message_replace", "error", "ping"]

# User input form types
UserInputFormType = Literal["text-input", "paragraph", "select"]

# Audio format types
AudioFormat = Literal["mp3", "wav"]

# Image format types
ImageFormat = Literal["png", "jpg", "jpeg", "webp", "gif"]

# Currency types (common currencies)
CurrencyType = Literal["USD", "EUR", "CNY", "JPY", "GBP"]

# Language codes (common language codes)
LanguageCode = Literal["en-US", "zh-CN", "ja-JP", "ko-KR", "fr-FR", "de-DE", "es-ES", "pt-BR", "ru-RU"]
