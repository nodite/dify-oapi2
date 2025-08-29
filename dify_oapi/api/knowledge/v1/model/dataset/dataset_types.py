from __future__ import annotations

from typing import Literal

# Indexing technique types
IndexingTechnique = Literal["high_quality", "economy"]

# Search method types
SearchMethod = Literal["keyword_search", "semantic_search", "full_text_search", "hybrid_search"]

# Reranking model types
RerankingModelType = Literal["rerank-model"]

# Processing rule mode types
ProcessingRuleMode = Literal["automatic", "custom"]

# Data source types
DataSourceType = Literal["upload_file", "notion_import", "website_crawl"]

# Document status types
DocumentStatus = Literal["indexing", "completed", "error", "paused"]

# Metadata field types
MetadataFieldType = Literal["text", "number", "select"]

# Tag types
TagType = Literal["knowledge", "custom"]

# Built-in metadata actions
BuiltinMetadataAction = Literal["enable", "disable"]

# Filter operator types
FilterOperator = Literal["contains", "not_contains", "is", "is_not", "is_empty", "is_not_empty"]

# Reranking enable types
RerankingEnable = Literal[True, False]
