"""Knowledge Base API type definitions using Literal types for type safety."""

from typing import Literal

# Indexing technique types
IndexingTechnique = Literal["high_quality", "economy"]

# Permission types
Permission = Literal["only_me", "all_team_members"]

# Search method types
SearchMethod = Literal["semantic_search", "full_text_search", "hybrid_search"]

# Document status types
DocumentStatus = Literal["indexing", "completed", "error", "paused"]

# Processing mode types
ProcessingMode = Literal["automatic", "custom"]

# File types
FileType = Literal["document", "image", "audio", "video", "custom"]

# Transfer method types
TransferMethod = Literal["remote_url", "local_file"]

# Tag types
TagType = Literal["knowledge_type", "custom"]

# Segment status types
SegmentStatus = Literal["waiting", "indexing", "completed", "error", "paused"]

# Model types
ModelType = Literal["text-embedding"]

# Provider types
ProviderType = Literal["system", "custom"]

# Data source types
DataSourceType = Literal["upload_file", "notion_import", "website_crawl"]
