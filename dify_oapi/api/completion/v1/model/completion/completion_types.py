from __future__ import annotations

from typing import Literal

# Response mode types
ResponseMode = Literal["streaming", "blocking"]

# File types
FileType = Literal["image"]

# Transfer method types
TransferMethod = Literal["remote_url", "local_file"]

# Feedback rating types
FeedbackRating = Literal["like", "dislike", "null"]

# Annotation action types
AnnotationAction = Literal["enable", "disable"]

# Icon types
IconType = Literal["emoji", "image"]

# App mode types
AppMode = Literal["completion"]

# Job status types
JobStatus = Literal["waiting", "running", "completed", "failed"]
