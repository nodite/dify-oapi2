# Knowledge Base APIs Documentation

Complete documentation for all 33 Knowledge Base APIs implemented in dify-oapi2.

## Overview

The Knowledge Base API module provides comprehensive dataset management, document processing, and content retrieval capabilities for AI applications. It implements **33 APIs** across **6 specialized resources**:

- **Dataset Resource**: 6 APIs for dataset management
- **Document Resource**: 10 APIs for document processing  
- **Segment Resource**: 5 APIs for content segmentation
- **Child Chunks Resource**: 4 APIs for sub-segment management
- **Tag Resource**: 7 APIs for metadata and tagging
- **Model Resource**: 1 API for embedding models

## Quick Start

```python
from dify_oapi.client import Client
from dify_oapi.core.model.request_option import RequestOption

# Initialize client
client = Client.builder().domain("https://api.dify.ai").build()
request_option = RequestOption.builder().api_key("your-api-key").build()

# Access knowledge resources
knowledge = client.knowledge.v1
dataset_resource = knowledge.dataset
document_resource = knowledge.document
segment_resource = knowledge.segment
chunk_resource = knowledge.chunk
tag_resource = knowledge.tag
model_resource = knowledge.model
```

## Dataset Resource APIs (6 APIs)

### 1. Create Dataset

Creates a new knowledge base (dataset) for storing and managing documents.

```python
from dify_oapi.api.knowledge.v1.model.create_dataset_request import CreateDatasetRequest
from dify_oapi.api.knowledge.v1.model.create_dataset_request_body import CreateDatasetRequestBody

# Build request
request_body = (
    CreateDatasetRequestBody.builder()
    .name("Product Documentation")
    .description("Knowledge base for product documentation and FAQs")
    .indexing_technique("high_quality")
    .permission("all_team_members")
    .provider("vendor")
    .embedding_model("text-embedding-ada-002")
    .embedding_model_provider("openai")
    .build()
)

request = CreateDatasetRequest.builder().request_body(request_body).build()

# Execute request
response = client.knowledge.v1.dataset.create(request, request_option)
print(f"Created dataset: {response.id}")
```

### 2. List Datasets

Retrieves all datasets accessible to the current user with pagination.

```python
from dify_oapi.api.knowledge.v1.model.list_datasets_request import ListDatasetsRequest

request = (
    ListDatasetsRequest.builder()
    .page(1)
    .limit(20)
    .build()
)

response = client.knowledge.v1.dataset.list(request, request_option)
print(f"Found {len(response.data)} datasets")
```

### 3. Get Dataset

Retrieves detailed information about a specific dataset.

```python
from dify_oapi.api.knowledge.v1.model.get_dataset_request import GetDatasetRequest

request = GetDatasetRequest.builder().dataset_id("dataset-id").build()
response = client.knowledge.v1.dataset.get(request, request_option)
print(f"Dataset: {response.name}")
```

### 4. Update Dataset

Updates dataset configuration and settings.

```python
from dify_oapi.api.knowledge.v1.model.update_dataset_request import UpdateDatasetRequest
from dify_oapi.api.knowledge.v1.model.update_dataset_request_body import UpdateDatasetRequestBody

request_body = (
    UpdateDatasetRequestBody.builder()
    .name("Updated Dataset Name")
    .description("Updated description")
    .build()
)

request = (
    UpdateDatasetRequest.builder()
    .dataset_id("dataset-id")
    .request_body(request_body)
    .build()
)

response = client.knowledge.v1.dataset.update(request, request_option)
```

### 5. Delete Dataset

Permanently removes a dataset and all its contents.

```python
from dify_oapi.api.knowledge.v1.model.delete_dataset_request import DeleteDatasetRequest

request = DeleteDatasetRequest.builder().dataset_id("dataset-id").build()
response = client.knowledge.v1.dataset.delete(request, request_option)
```

### 6. Retrieve from Dataset

Searches and retrieves relevant content from the dataset.

```python
from dify_oapi.api.knowledge.v1.model.retrieve_from_dataset_request import RetrieveFromDatasetRequest
from dify_oapi.api.knowledge.v1.model.retrieve_from_dataset_request_body import RetrieveFromDatasetRequestBody

request_body = (
    RetrieveFromDatasetRequestBody.builder()
    .query("How to install the product?")
    .top_k(5)
    .score_threshold(0.7)
    .build()
)

request = (
    RetrieveFromDatasetRequest.builder()
    .dataset_id("dataset-id")
    .request_body(request_body)
    .build()
)

response = client.knowledge.v1.dataset.retrieve(request, request_option)
print(f"Found {len(response.records)} relevant segments")
```

## Document Resource APIs (10 APIs)

### 7. Create Document by File

Uploads and processes a file to create a new document in the dataset.

```python
from dify_oapi.api.knowledge.v1.model.create_document_by_file_request import CreateDocumentByFileRequest
from dify_oapi.api.knowledge.v1.model.create_document_by_file_request_body import CreateDocumentByFileRequestBody
from io import BytesIO

# Prepare file
file_content = BytesIO(b"PDF file content here")

request_body = (
    CreateDocumentByFileRequestBody.builder()
    .indexing_technique("high_quality")
    .doc_form("text_model")
    .doc_language("English")
    .build()
)

request = (
    CreateDocumentByFileRequest.builder()
    .dataset_id("dataset-id")
    .request_body(request_body)
    .file(file_content, "manual.pdf")
    .build()
)

response = client.knowledge.v1.document.create_by_file(request, request_option)
print(f"Document created: {response.document.id}, Batch: {response.batch}")
```

### 8. Create Document by Text

Creates a document directly from text content.

```python
from dify_oapi.api.knowledge.v1.model.create_document_by_text_request import CreateDocumentByTextRequest
from dify_oapi.api.knowledge.v1.model.create_document_by_text_request_body import CreateDocumentByTextRequestBody

request_body = (
    CreateDocumentByTextRequestBody.builder()
    .name("Product Manual")
    .text("This is the product manual content...")
    .indexing_technique("high_quality")
    .doc_form("text_model")
    .doc_language("English")
    .build()
)

request = (
    CreateDocumentByTextRequest.builder()
    .dataset_id("dataset-id")
    .request_body(request_body)
    .build()
)

response = client.knowledge.v1.document.create_by_text(request, request_option)
```

### 9. List Documents

Retrieves all documents in a dataset with pagination and filtering.

```python
from dify_oapi.api.knowledge.v1.model.list_documents_request import ListDocumentsRequest

request = (
    ListDocumentsRequest.builder()
    .dataset_id("dataset-id")
    .keyword("manual")
    .page(1)
    .limit(20)
    .build()
)

response = client.knowledge.v1.document.list(request, request_option)
print(f"Found {len(response.data)} documents")
```

### 10. Get Document

Retrieves detailed information about a specific document.

```python
from dify_oapi.api.knowledge.v1.model.get_document_request import GetDocumentRequest

request = (
    GetDocumentRequest.builder()
    .dataset_id("dataset-id")
    .document_id("document-id")
    .build()
)

response = client.knowledge.v1.document.get(request, request_option)
```

### 11. Update Document by File

Replaces document content with a new file.

```python
from dify_oapi.api.knowledge.v1.model.update_document_by_file_request import UpdateDocumentByFileRequest
from dify_oapi.api.knowledge.v1.model.update_document_by_file_request_body import UpdateDocumentByFileRequestBody

file_content = BytesIO(b"Updated PDF content")

request_body = (
    UpdateDocumentByFileRequestBody.builder()
    .indexing_technique("economy")
    .build()
)

request = (
    UpdateDocumentByFileRequest.builder()
    .dataset_id("dataset-id")
    .document_id("document-id")
    .request_body(request_body)
    .file(file_content, "updated_manual.pdf")
    .build()
)

response = client.knowledge.v1.document.update_by_file(request, request_option)
```

### 12. Update Document by Text

Updates document content with new text.

```python
from dify_oapi.api.knowledge.v1.model.update_document_by_text_request import UpdateDocumentByTextRequest
from dify_oapi.api.knowledge.v1.model.update_document_by_text_request_body import UpdateDocumentByTextRequestBody

request_body = (
    UpdateDocumentByTextRequestBody.builder()
    .name("Updated Manual")
    .text("Updated manual content...")
    .build()
)

request = (
    UpdateDocumentByTextRequest.builder()
    .dataset_id("dataset-id")
    .document_id("document-id")
    .request_body(request_body)
    .build()
)

response = client.knowledge.v1.document.update_by_text(request, request_option)
```

### 13. Delete Document

Permanently removes a document from the dataset.

```python
from dify_oapi.api.knowledge.v1.model.delete_document_request import DeleteDocumentRequest

request = (
    DeleteDocumentRequest.builder()
    .dataset_id("dataset-id")
    .document_id("document-id")
    .build()
)

response = client.knowledge.v1.document.delete(request, request_option)
```

### 14. Update Document Status

Enables or disables documents in batch.

```python
from dify_oapi.api.knowledge.v1.model.update_document_status_request import UpdateDocumentStatusRequest
from dify_oapi.api.knowledge.v1.model.update_document_status_request_body import UpdateDocumentStatusRequestBody

request_body = (
    UpdateDocumentStatusRequestBody.builder()
    .document_ids(["doc-1", "doc-2", "doc-3"])
    .build()
)

request = (
    UpdateDocumentStatusRequest.builder()
    .dataset_id("dataset-id")
    .action("enable")  # or "disable", "archive", "un_archive"
    .request_body(request_body)
    .build()
)

response = client.knowledge.v1.document.update_status(request, request_option)
```

### 15. Get Batch Indexing Status

Checks the processing status of a document batch.

```python
from dify_oapi.api.knowledge.v1.model.get_batch_indexing_status_request import GetBatchIndexingStatusRequest

request = (
    GetBatchIndexingStatusRequest.builder()
    .dataset_id("dataset-id")
    .batch("batch-id")
    .build()
)

response = client.knowledge.v1.document.get_batch_status(request, request_option)
print(f"Status: {response.indexing_status}")
```

### 16. Get Upload File Info

Retrieves information about an uploaded file.

```python
from dify_oapi.api.knowledge.v1.model.get_upload_file_info_request import GetUploadFileInfoRequest

request = (
    GetUploadFileInfoRequest.builder()
    .dataset_id("dataset-id")
    .document_id("document-id")
    .build()
)

response = client.knowledge.v1.document.file_info(request, request_option)
print(f"File: {response.name}, Size: {response.size}")
```

## Segment Resource APIs (5 APIs)

### 17. List Segments

Retrieves all segments (chunks) of a document.

```python
from dify_oapi.api.knowledge.v1.model.list_segments_request import ListSegmentsRequest

request = (
    ListSegmentsRequest.builder()
    .dataset_id("dataset-id")
    .document_id("document-id")
    .keyword("installation")
    .status("completed")
    .build()
)

response = client.knowledge.v1.segment.list(request, request_option)
```

### 18. Create Segment

Adds new segments to a document.

```python
from dify_oapi.api.knowledge.v1.model.create_segment_request import CreateSegmentRequest
from dify_oapi.api.knowledge.v1.model.create_segment_request_body import CreateSegmentRequestBody
from dify_oapi.api.knowledge.v1.model.segment_info import SegmentInfo

segments = [
    SegmentInfo.builder()
    .content("First segment content")
    .keywords(["keyword1", "keyword2"])
    .build(),
    SegmentInfo.builder()
    .content("Second segment content")
    .build()
]

request_body = CreateSegmentRequestBody.builder().segments(segments).build()

request = (
    CreateSegmentRequest.builder()
    .dataset_id("dataset-id")
    .document_id("document-id")
    .request_body(request_body)
    .build()
)

response = client.knowledge.v1.segment.create(request, request_option)
```

### 19. Get Segment

Retrieves detailed information about a specific segment.

```python
from dify_oapi.api.knowledge.v1.model.get_segment_request import GetSegmentRequest

request = (
    GetSegmentRequest.builder()
    .dataset_id("dataset-id")
    .document_id("document-id")
    .segment_id("segment-id")
    .build()
)

response = client.knowledge.v1.segment.get(request, request_option)
```

### 20. Update Segment

Updates the content and metadata of a segment.

```python
from dify_oapi.api.knowledge.v1.model.update_segment_request import UpdateSegmentRequest
from dify_oapi.api.knowledge.v1.model.update_segment_request_body import UpdateSegmentRequestBody
from dify_oapi.api.knowledge.v1.model.segment_data import SegmentData

segment_data = (
    SegmentData.builder()
    .content("Updated segment content")
    .keywords(["updated", "keywords"])
    .build()
)

request_body = UpdateSegmentRequestBody.builder().segment(segment_data).build()

request = (
    UpdateSegmentRequest.builder()
    .dataset_id("dataset-id")
    .document_id("document-id")
    .segment_id("segment-id")
    .request_body(request_body)
    .build()
)

response = client.knowledge.v1.segment.update(request, request_option)
```

### 21. Delete Segment

Permanently removes a segment from the document.

```python
from dify_oapi.api.knowledge.v1.model.delete_segment_request import DeleteSegmentRequest

request = (
    DeleteSegmentRequest.builder()
    .dataset_id("dataset-id")
    .document_id("document-id")
    .segment_id("segment-id")
    .build()
)

response = client.knowledge.v1.segment.delete(request, request_option)
```

## Child Chunks Resource APIs (4 APIs)

### 22. List Child Chunks

Retrieves all child chunks (sub-segments) of a segment.

```python
from dify_oapi.api.knowledge.v1.model.list_child_chunks_request import ListChildChunksRequest

request = (
    ListChildChunksRequest.builder()
    .dataset_id("dataset-id")
    .document_id("document-id")
    .segment_id("segment-id")
    .build()
)

response = client.knowledge.v1.chunk.list(request, request_option)
```

### 23. Create Child Chunk

Creates new child chunks within a segment.

```python
from dify_oapi.api.knowledge.v1.model.create_child_chunk_request import CreateChildChunkRequest
from dify_oapi.api.knowledge.v1.model.create_child_chunk_request_body import CreateChildChunkRequestBody

chunks = [
    {
        "content": "First child chunk content",
        "keywords": ["chunk1", "content"]
    },
    {
        "content": "Second child chunk content",
        "keywords": ["chunk2"]
    }
]

request_body = CreateChildChunkRequestBody.builder().chunks(chunks).build()

request = (
    CreateChildChunkRequest.builder()
    .dataset_id("dataset-id")
    .document_id("document-id")
    .segment_id("segment-id")
    .request_body(request_body)
    .build()
)

response = client.knowledge.v1.chunk.create(request, request_option)
```

### 24. Update Child Chunk

Updates a specific child chunk.

```python
from dify_oapi.api.knowledge.v1.model.update_child_chunk_request import UpdateChildChunkRequest
from dify_oapi.api.knowledge.v1.model.update_child_chunk_request_body import UpdateChildChunkRequestBody

request_body = (
    UpdateChildChunkRequestBody.builder()
    .content("Updated child chunk content")
    .keywords(["updated", "chunk"])
    .build()
)

request = (
    UpdateChildChunkRequest.builder()
    .dataset_id("dataset-id")
    .document_id("document-id")
    .segment_id("segment-id")
    .child_chunk_id("chunk-id")
    .request_body(request_body)
    .build()
)

response = client.knowledge.v1.chunk.update(request, request_option)
```

### 25. Delete Child Chunk

Removes a child chunk from the segment.

```python
from dify_oapi.api.knowledge.v1.model.delete_child_chunk_request import DeleteChildChunkRequest

request = (
    DeleteChildChunkRequest.builder()
    .dataset_id("dataset-id")
    .document_id("document-id")
    .segment_id("segment-id")
    .child_chunk_id("chunk-id")
    .build()
)

response = client.knowledge.v1.chunk.delete(request, request_option)
```

## Tag Resource APIs (7 APIs)

### 26. List Tags

Retrieves all available tags in the workspace.

```python
from dify_oapi.api.knowledge.v1.model.list_tags_request import ListTagsRequest

request = (
    ListTagsRequest.builder()
    .type("knowledge_type")  # or "custom"
    .build()
)

response = client.knowledge.v1.tag.list(request, request_option)
```

### 27. Create Tag

Creates a new tag for organizing datasets.

```python
from dify_oapi.api.knowledge.v1.model.create_tag_request import CreateTagRequest
from dify_oapi.api.knowledge.v1.model.create_tag_request_body import CreateTagRequestBody

request_body = (
    CreateTagRequestBody.builder()
    .name("Product Documentation")
    .type("knowledge_type")
    .build()
)

request = CreateTagRequest.builder().request_body(request_body).build()
response = client.knowledge.v1.tag.create(request, request_option)
```

### 28. Update Tag

Updates an existing tag.

```python
from dify_oapi.api.knowledge.v1.model.update_tag_request import UpdateTagRequest
from dify_oapi.api.knowledge.v1.model.update_tag_request_body import UpdateTagRequestBody

request_body = (
    UpdateTagRequestBody.builder()
    .tag_id("tag-id")
    .name("Updated Tag Name")
    .build()
)

request = UpdateTagRequest.builder().request_body(request_body).build()
response = client.knowledge.v1.tag.update(request, request_option)
```

### 29. Delete Tag

Removes a tag from the system.

```python
from dify_oapi.api.knowledge.v1.model.delete_tag_request import DeleteTagRequest
from dify_oapi.api.knowledge.v1.model.delete_tag_request_body import DeleteTagRequestBody

request_body = (
    DeleteTagRequestBody.builder()
    .tag_id("tag-id")
    .build()
)

request = DeleteTagRequest.builder().request_body(request_body).build()
response = client.knowledge.v1.tag.delete(request, request_option)
```

### 30. Bind Tags to Dataset

Associates tags with a dataset.

```python
from dify_oapi.api.knowledge.v1.model.bind_tags_to_dataset_request import BindTagsToDatasetRequest
from dify_oapi.api.knowledge.v1.model.bind_tags_to_dataset_request_body import BindTagsToDatasetRequestBody

request_body = (
    BindTagsToDatasetRequestBody.builder()
    .dataset_id("dataset-id")
    .tag_ids(["tag-1", "tag-2", "tag-3"])
    .build()
)

request = BindTagsToDatasetRequest.builder().request_body(request_body).build()
response = client.knowledge.v1.tag.bind(request, request_option)
```

### 31. Unbind Tags from Dataset

Removes tag associations from a dataset.

```python
from dify_oapi.api.knowledge.v1.model.unbind_tags_from_dataset_request import UnbindTagsFromDatasetRequest
from dify_oapi.api.knowledge.v1.model.unbind_tags_from_dataset_request_body import UnbindTagsFromDatasetRequestBody

request_body = (
    UnbindTagsFromDatasetRequestBody.builder()
    .dataset_id("dataset-id")
    .tag_ids(["tag-1", "tag-2"])
    .build()
)

request = UnbindTagsFromDatasetRequest.builder().request_body(request_body).build()
response = client.knowledge.v1.tag.unbind(request, request_option)
```

### 32. Get Dataset Tags

Retrieves all tags associated with a specific dataset.

```python
from dify_oapi.api.knowledge.v1.model.get_dataset_tags_request import GetDatasetTagsRequest

request = GetDatasetTagsRequest.builder().dataset_id("dataset-id").build()
response = client.knowledge.v1.tag.get_dataset_tags(request, request_option)
```

## Model Resource APIs (1 API)

### 33. Get Text Embedding Models

Retrieves available text embedding models for the workspace.

```python
from dify_oapi.api.knowledge.v1.model.get_text_embedding_models_request import GetTextEmbeddingModelsRequest

request = GetTextEmbeddingModelsRequest.builder().build()
response = client.knowledge.v1.model.embedding_models(request, request_option)

print(f"Available providers: {len(response.data)}")
for provider in response.data:
    print(f"Provider: {provider.provider}, Models: {len(provider.models)}")
```

## Async Support

All APIs support asynchronous operations by using the async versions of the methods:

```python
import asyncio

async def async_example():
    # Create dataset asynchronously
    response = await client.knowledge.v1.dataset.acreate(request, request_option)
    
    # List documents asynchronously
    response = await client.knowledge.v1.document.alist(request, request_option)
    
    # Search content asynchronously
    response = await client.knowledge.v1.dataset.aretrieve(request, request_option)

# Run async function
asyncio.run(async_example())
```

## Error Handling

All response models inherit from `BaseResponse` and provide comprehensive error handling:

```python
try:
    response = client.knowledge.v1.dataset.create(request, request_option)
    if response.success:
        print(f"Success: {response.id}")
    else:
        print(f"Error {response.code}: {response.msg}")
except Exception as e:
    print(f"Request failed: {e}")
```

## Type Safety

The Knowledge Base API module uses strict type safety with Literal types:

```python
from dify_oapi.api.knowledge.v1.model.knowledge_types import (
    IndexingTechnique,
    Permission,
    SearchMethod,
    DocumentForm,
    TagType
)

# Type-safe values
indexing: IndexingTechnique = "high_quality"  # or "economy"
permission: Permission = "all_team_members"   # or "only_me", "partial_members"
search: SearchMethod = "hybrid_search"        # or "semantic_search", "full_text_search", "keyword_search"
doc_form: DocumentForm = "text_model"         # or "hierarchical_model", "qa_model"
tag_type: TagType = "knowledge_type"          # or "custom"
```

## Best Practices

1. **Dataset Organization**: Use descriptive names and tags to organize datasets by domain or purpose
2. **Document Processing**: Monitor batch indexing status before using documents in retrieval
3. **Content Retrieval**: Adjust `top_k` and `score_threshold` based on your use case requirements
4. **Segment Management**: Keep segments focused and coherent for better retrieval performance
5. **File Uploads**: Use appropriate file formats and validate file sizes before upload
6. **Error Handling**: Always check response status and implement proper retry logic
7. **Async Operations**: Use async methods for better performance in concurrent scenarios
8. **Type Safety**: Leverage Literal types to prevent runtime errors and improve code quality

## Performance Considerations

- **Batch Operations**: Use batch status checking for large document uploads
- **Pagination**: Implement proper pagination for large result sets
- **Caching**: Cache frequently accessed datasets and documents
- **Concurrent Requests**: Use async methods for concurrent operations
- **Resource Cleanup**: Properly delete unused datasets and documents to manage storage

## API Limits and Quotas

- Check your Dify API plan for specific rate limits and quotas
- Implement exponential backoff for rate limit handling
- Monitor API usage to avoid quota exhaustion
- Use appropriate batch sizes for bulk operations

## Summary

The Knowledge Base API module provides a comprehensive, type-safe interface for managing knowledge bases in Dify applications. With 33 APIs across 6 specialized resources, it supports everything from basic dataset management to advanced content retrieval and organization.

Key features:
- **Complete API Coverage**: All 33 knowledge base APIs implemented
- **Type Safety**: Strict typing with Literal types for all predefined values
- **Async Support**: Full async/await support for all operations
- **Error Handling**: Comprehensive error handling with BaseResponse inheritance
- **Builder Patterns**: Fluent, chainable interfaces for all models
- **File Upload Support**: Complete multipart/form-data handling for document APIs
- **Complex Path Parameters**: Support for up to 5-level nested resource paths
- **Performance Optimized**: Efficient HTTP transport and connection management