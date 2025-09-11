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
ProcessingMode = Literal["automatic", "custom", "hierarchical"]

# File types
FileType = Literal["document", "image", "audio", "video", "custom"]

# Transfer method types
TransferMethod = Literal["remote_url", "local_file"]

# Tag types
TagType = Literal["knowledge", "custom"]

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

# Dataset types
DatasetType = Literal["knowledge_base", "external_api"]

# Indexing status types
IndexingStatus = Literal["waiting", "parsing", "cleaning", "splitting", "indexing", "completed", "error", "paused"]

# Reranking model configuration types
RerankingProviderName = str  # Dynamic provider names
RerankingModelName = str  # Dynamic model names

# Preprocessing rule types
PreprocessingRuleId = Literal["remove_extra_spaces", "remove_urls_emails"]

# Parent mode types for hierarchical processing
ParentMode = Literal["full-doc", "paragraph"]

# Model status types
ModelStatus = Literal["active", "inactive", "deprecated"]

# Model fetch source types
ModelFetchFrom = Literal["predefined-model", "customizable-model"]

# Model feature types
ModelFeature = Literal["embedding", "reranking"]

# Tag binding target types
TagBindingTarget = Literal["dataset", "document"]

# External knowledge provider types
ExternalKnowledgeProvider = Literal["external_api", "notion", "web_crawler"]

# Document creation source types
DocumentCreatedFrom = Literal["api", "web", "upload"]

# Document display status types
DocumentDisplayStatus = Literal["available", "indexing", "error", "paused", "archived", "queuing"]

# Batch processing status types
BatchProcessingStatus = Literal["processing", "completed", "failed", "cancelled"]

# File extension types (common ones)
FileExtension = Literal["pdf", "doc", "docx", "txt", "md", "html", "csv", "xlsx", "ppt", "pptx"]

# MIME type categories
MimeTypeCategory = Literal["application", "text", "image", "audio", "video"]

# Chunk processing status
ChunkStatus = Literal["waiting", "processing", "completed", "error"]

# Query content type
QueryContentType = Literal["text", "structured"]

# Retrieval record score type
RetrievalScoreType = Literal["cosine", "dot_product", "euclidean"]
