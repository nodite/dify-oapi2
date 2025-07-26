# Dify-OAPI Examples

This directory contains example code for using the Dify-OAPI SDK.

## Chat Examples
- [Blocking Response](./chat/blocking_response.py): Example of using the Chat API with blocking response mode
- [Streaming Response](./chat/streaming_response.py): Example of using the Chat API with streaming response mode
- [Conversation Management](./chat/conversation_management.py): Example of managing conversations and retrieving message history

## Completion Examples
- [Basic Completion](./completion/basic_completion.py): Example of using the Completion API for text generation

## Knowledge Base Examples

### Dataset Management
- [Create Dataset](./knowledge_base/dataset/create.py): Create new datasets with various configurations
- [List Datasets](./knowledge_base/dataset/list.py): List datasets with pagination and search
- [Get Dataset](./knowledge_base/dataset/get.py): Get detailed dataset information
- [Update Dataset](./knowledge_base/dataset/update.py): Update dataset configuration and settings
- [Delete Dataset](./knowledge_base/dataset/delete.py): Delete datasets with confirmation prompts
- [Retrieve from Dataset](./knowledge_base/dataset/retrieve.py): Perform retrieval search with different methods

### Metadata Management
- [Create Metadata](./knowledge_base/metadata/create.py): Create custom metadata fields
- [List Metadata](./knowledge_base/metadata/list.py): List metadata configuration and usage
- [Update Metadata](./knowledge_base/metadata/update.py): Update metadata field names
- [Delete Metadata](./knowledge_base/metadata/delete.py): Delete metadata fields with warnings
- [Toggle Built-in Metadata](./knowledge_base/metadata/toggle_builtin.py): Enable/disable built-in metadata
- [Update Document Metadata](./knowledge_base/metadata/update_document.py): Update document metadata values

### Tag Management
- [Create Tags](./knowledge_base/tag/create.py): Create knowledge type tags
- [List Tags](./knowledge_base/tag/list.py): List all available tags
- [Update Tags](./knowledge_base/tag/update.py): Update tag names
- [Delete Tags](./knowledge_base/tag/delete.py): Delete tags with confirmation
- [Bind Tags](./knowledge_base/tag/bind.py): Bind tags to datasets
- [Unbind Tags](./knowledge_base/tag/unbind.py): Unbind tags from datasets
- [Query Bound Tags](./knowledge_base/tag/query_bound.py): Query tags bound to datasets

### Documentation
- [Knowledge Base README](./knowledge_base/README.md): Comprehensive usage guide with examples and best practices
