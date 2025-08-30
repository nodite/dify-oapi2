"""Knowledge Base API type definitions using Literal types for type safety."""

from typing import Literal

# Indexing technique types
IndexingTechnique = Literal["high_quality", "economy"]

# Permission types
Permission = Literal["only_me", "all_team_members", "partial_members"]

# Search method types
SearchMethod = Literal["hybrid_search", "semantic_search", "full_text_search", "keyword_search"]

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
SegmentStatus = Literal["waiting", "parsing", "cleaning", "splitting", "indexing", "completed", "error", "paused"]

# Document status action types
DocumentStatusAction = Literal["enable", "disable", "archive", "un_archive"]

# Document form types
DocumentForm = Literal["text_model", "hierarchical_model", "qa_model"]

# Model types
ModelType = Literal["text-embedding"]

# Provider types
ProviderType = Literal["vendor", "external"]

# Data source types
DataSourceType = Literal["upload_file", "notion_import", "website_crawl"]

# Indexing status types
IndexingStatus = Literal["waiting", "parsing", "cleaning", "splitting", "indexing", "completed", "error", "paused"]

# Reranking model configuration types
RerankingProviderName = str  # Dynamic provider names
RerankingModelName = str  # Dynamic model names
