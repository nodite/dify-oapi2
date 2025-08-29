from __future__ import annotations

from typing import Literal

# Indexing technique types
IndexingTechnique = Literal["high_quality", "economy"]

# Document form types
DocumentForm = Literal["text_model", "hierarchical_model", "qa_model"]

# Document language types
DocumentLanguage = Literal["English", "Chinese", "Japanese", "Korean"]

# Processing rule mode types
ProcessingRuleMode = Literal["automatic", "custom"]

# Segmentation separator types
Separator = Literal["\\n\\n", "\\n", ".", "!", "?", ";"]

# Pre-processing rule types
PreProcessingRuleType = Literal["remove_extra_spaces", "remove_urls_emails"]

# Data source types
DataSourceType = Literal["upload_file", "notion_import", "website_crawl"]

# Document indexing status types
IndexingStatus = Literal["waiting", "parsing", "cleaning", "splitting", "indexing", "completed", "error", "paused"]

# Document status action types
StatusAction = Literal["enable", "disable", "archive"]

# Upload file status types
UploadFileStatus = Literal["success", "processing", "error"]

# Document enabled status
DocumentEnabled = Literal[True, False]
