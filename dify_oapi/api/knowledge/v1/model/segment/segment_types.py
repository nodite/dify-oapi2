from __future__ import annotations

from typing import Literal

# Segment status types
SegmentStatus = Literal["waiting", "indexing", "completed", "error", "paused"]

# Segment enabled status types
SegmentEnabledStatus = Literal["enabled", "disabled"]

# Child chunk status types
ChildChunkStatus = Literal["waiting", "indexing", "completed", "error"]

# Segment search status types
SearchStatus = Literal["all", "enabled", "disabled"]

# Sort order types
SortOrder = Literal["created_at", "position", "word_count", "hit_count"]

# Sort direction types
SortDirection = Literal["asc", "desc"]

# Segment enabled boolean
SegmentEnabled = Literal[True, False]
