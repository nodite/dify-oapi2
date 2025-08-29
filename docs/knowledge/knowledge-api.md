# Knowledge Base APIs

This document covers all knowledge base APIs based on the official Dify OpenAPI specification. Knowledge base APIs provide comprehensive dataset management, document processing, and content retrieval capabilities for AI applications.

## Base URL

```
https://api.dify.ai/v1
```

## Authentication

Service API uses `API-Key` for authentication. **It is strongly recommended that developers store the `API-Key` in the backend rather than sharing or storing it on the client side to prevent `API-Key` leakage and financial loss.**

All API requests should include your `API-Key` in the **`Authorization`** HTTP Header:

```
Authorization: Bearer {API_KEY}
```

## API Overview

The Knowledge Base API provides 39 endpoints organized into 5 main categories:

### Dataset Management (8 APIs)
- Create Dataset - Create a new knowledge base
- List Datasets - Retrieve all datasets
- Get Dataset - Retrieve dataset details
- Update Dataset - Modify dataset configuration
- Delete Dataset - Remove a dataset
- Dataset Tags - Manage dataset tags
- Bind/Unbind Tags - Associate tags with datasets
- Retrieve from Dataset - Search and retrieve content

### Document Management (12 APIs)
- Create Document by File - Upload and process files
- Create Document by Text - Add text content directly
- List Documents - Retrieve all documents in a dataset
- Get Document - Retrieve document details
- Update Document by File - Replace document with new file
- Update Document by Text - Update document content
- Delete Document - Remove a document
- Upload File for Document - File upload endpoint
- Document Status Management - Enable/disable documents
- Batch Indexing Status - Check processing status

### Segment Management (8 APIs)
- List Segments - Retrieve document segments
- Create Segment - Add new content segments
- Get Segment - Retrieve segment details
- Update Segment - Modify segment content
- Delete Segment - Remove a segment
- List Child Chunks - Retrieve sub-segments
- Create Child Chunk - Add sub-segments
- Update/Delete Child Chunks - Manage sub-segments

### Metadata & Tags (10 APIs)
- List All Tags - Retrieve available tags
- Create Tag - Add new tags
- Update Tag - Modify tag information
- Delete Tag - Remove tags
- Bind Tags to Dataset - Associate tags
- Unbind Tags from Dataset - Remove tag associations
- Dataset-specific Tags - Manage dataset tags

### Models (1 API)
- Get Text Embedding Models - Retrieve available embedding models

## APIs

### Dataset Management

#### 1. Create Dataset

**POST** `/datasets`

Creates a new knowledge base (dataset) for storing and managing documents.

##### Request Body
- `name` (string, required): Dataset name
- `description` (string, optional): Dataset description
- `indexing_technique` (string, required): Indexing method
  - `high_quality`: High quality indexing (recommended)
  - `economy`: Economy indexing for cost efficiency
- `permission` (string, required): Access permission
  - `only_me`: Private access
  - `all_team_members`: Team access
- `provider` (string, optional): Embedding model provider
- `model` (string, optional): Embedding model name
- `embedding_model_parameters` (object, optional): Model configuration
- `retrieval_model` (object, optional): Retrieval configuration
  - `search_method` (string): Search method (`semantic_search`, `full_text_search`, `hybrid_search`)
  - `reranking_enable` (boolean): Enable reranking
  - `reranking_model` (object): Reranking model configuration
  - `top_k` (integer): Number of results to return
  - `score_threshold_enabled` (boolean): Enable score threshold
  - `score_threshold` (number): Minimum relevance score

##### Example Request
```json
{
  "name": "Product Documentation",
  "description": "Knowledge base for product documentation and FAQs",
  "indexing_technique": "high_quality",
  "permission": "all_team_members",
  "provider": "openai",
  "model": "text-embedding-ada-002",
  "retrieval_model": {
    "search_method": "hybrid_search",
    "reranking_enable": true,
    "top_k": 10,
    "score_threshold_enabled": true,
    "score_threshold": 0.7
  }
}
```

##### Response
- `id` (string): Dataset ID (UUID)
- `name` (string): Dataset name
- `description` (string): Dataset description
- `permission` (string): Access permission
- `data_source_type` (string): Data source type
- `indexing_technique` (string): Indexing technique used
- `app_count` (integer): Number of associated applications
- `document_count` (integer): Number of documents
- `word_count` (integer): Total word count
- `created_by` (string): Creator ID
- `created_at` (timestamp): Creation time
- `updated_at` (timestamp): Last update time

#### 2. List Datasets

**GET** `/datasets`

Retrieves all datasets accessible to the current user.

##### Query Parameters
- `page` (integer, optional): Page number, default 1
- `limit` (integer, optional): Items per page, default 20

##### Response
- `data` (array): List of datasets
- `has_more` (boolean): Whether more data exists
- `limit` (integer): Items per page
- `total` (integer): Total count
- `page` (integer): Current page

#### 3. Get Dataset

**GET** `/datasets/{dataset_id}`

Retrieves detailed information about a specific dataset.

##### Path Parameters
- `dataset_id` (string, required): Dataset ID (UUID)

##### Response
Same structure as Create Dataset response with additional statistics.

#### 4. Update Dataset

**PATCH** `/datasets/{dataset_id}`

Updates dataset configuration and settings.

##### Path Parameters
- `dataset_id` (string, required): Dataset ID (UUID)

##### Request Body
Same fields as Create Dataset (all optional for updates).

#### 5. Delete Dataset

**DELETE** `/datasets/{dataset_id}`

Permanently removes a dataset and all its contents.

##### Path Parameters
- `dataset_id` (string, required): Dataset ID (UUID)

##### Response
- `result` (string): "success"

#### 6. Retrieve from Dataset

**POST** `/datasets/{dataset_id}/retrieve`

Searches and retrieves relevant content from the dataset.

##### Path Parameters
- `dataset_id` (string, required): Dataset ID (UUID)

##### Request Body
- `query` (string, required): Search query
- `retrieval_model` (object, optional): Override retrieval settings
- `top_k` (integer, optional): Number of results
- `score_threshold` (number, optional): Minimum relevance score

##### Response
- `query` (string): Original query
- `records` (array): Retrieved segments
  - `segment` (object): Segment information
    - `id` (string): Segment ID
    - `content` (string): Segment content
    - `score` (number): Relevance score
    - `document_id` (string): Source document ID
    - `document_name` (string): Source document name

### Document Management

#### 7. Create Document by File

**POST** `/datasets/{dataset_id}/document/create-by-file`

Uploads and processes a file to create a new document in the dataset.

##### Path Parameters
- `dataset_id` (string, required): Dataset ID (UUID)

##### Request Body (multipart/form-data)
- `data` (string, required): JSON string containing document metadata
  - `name` (string): Document name
  - `indexing_technique` (string): Indexing method
  - `process_rule` (object): Processing rules
    - `mode` (string): Processing mode (`automatic`, `custom`)
    - `rules` (object): Custom processing rules
- `file` (binary, required): File to upload

##### Response
- `document` (object): Created document information
- `batch` (string): Processing batch ID

#### 8. Create Document by Text

**POST** `/datasets/{dataset_id}/document/create-by-text`

Creates a document directly from text content.

##### Path Parameters
- `dataset_id` (string, required): Dataset ID (UUID)

##### Request Body
- `name` (string, required): Document name
- `text` (string, required): Document content
- `indexing_technique` (string, required): Indexing method
- `process_rule` (object, optional): Processing configuration

#### 9. List Documents

**GET** `/datasets/{dataset_id}/documents`

Retrieves all documents in a dataset with pagination.

##### Path Parameters
- `dataset_id` (string, required): Dataset ID (UUID)

##### Query Parameters
- `keyword` (string, optional): Search keyword
- `page` (integer, optional): Page number
- `limit` (integer, optional): Items per page

##### Response
- `data` (array): List of documents
- `has_more` (boolean): More data available
- `limit` (integer): Items per page
- `total` (integer): Total documents
- `page` (integer): Current page

#### 10. Get Document

**GET** `/datasets/{dataset_id}/documents/{document_id}`

Retrieves detailed information about a specific document.

##### Path Parameters
- `dataset_id` (string, required): Dataset ID (UUID)
- `document_id` (string, required): Document ID (UUID)

#### 11. Update Document by File

**POST** `/datasets/{dataset_id}/documents/{document_id}/update-by-file`

Replaces document content with a new file.

##### Path Parameters
- `dataset_id` (string, required): Dataset ID (UUID)
- `document_id` (string, required): Document ID (UUID)

##### Request Body (multipart/form-data)
Same as Create Document by File.

#### 12. Update Document by Text

**POST** `/datasets/{dataset_id}/documents/{document_id}/update-by-text`

Updates document content with new text.

##### Path Parameters
- `dataset_id` (string, required): Dataset ID (UUID)
- `document_id` (string, required): Document ID (UUID)

##### Request Body
Same as Create Document by Text.

#### 13. Delete Document

**DELETE** `/datasets/{dataset_id}/documents/{document_id}`

Permanently removes a document from the dataset.

##### Path Parameters
- `dataset_id` (string, required): Dataset ID (UUID)
- `document_id` (string, required): Document ID (UUID)

#### 14. Document Status Management

**PATCH** `/datasets/{dataset_id}/documents/status/{action}`

Enables or disables documents in batch.

##### Path Parameters
- `dataset_id` (string, required): Dataset ID (UUID)
- `action` (string, required): Action to perform (`enable`, `disable`)

##### Request Body
- `document_ids` (array[string], required): List of document IDs

#### 15. Get Batch Indexing Status

**GET** `/datasets/{dataset_id}/documents/{batch}/indexing-status`

Checks the processing status of a document batch.

##### Path Parameters
- `dataset_id` (string, required): Dataset ID (UUID)
- `batch` (string, required): Batch ID from document creation

##### Response
- `id` (string): Batch ID
- `indexing_status` (string): Processing status
  - `waiting`: Waiting to process
  - `parsing`: Parsing document
  - `cleaning`: Cleaning content
  - `splitting`: Splitting into segments
  - `indexing`: Creating embeddings
  - `completed`: Processing complete
  - `error`: Processing failed
- `processing_started_at` (timestamp): Processing start time
- `parsing_completed_at` (timestamp): Parsing completion time
- `cleaning_completed_at` (timestamp): Cleaning completion time
- `splitting_completed_at` (timestamp): Splitting completion time
- `completed_at` (timestamp): Overall completion time
- `error` (string): Error message if failed
- `stopped_at` (timestamp): Stop time if interrupted

### Segment Management

#### 16. List Segments

**GET** `/datasets/{dataset_id}/documents/{document_id}/segments`

Retrieves all segments (chunks) of a document.

##### Path Parameters
- `dataset_id` (string, required): Dataset ID (UUID)
- `document_id` (string, required): Document ID (UUID)

##### Query Parameters
- `keyword` (string, optional): Search keyword
- `status` (string, optional): Filter by status (`enabled`, `disabled`)

##### Response
- `data` (array): List of segments
  - `id` (string): Segment ID
  - `position` (integer): Position in document
  - `document_id` (string): Parent document ID
  - `content` (string): Segment content
  - `word_count` (integer): Word count
  - `tokens` (integer): Token count
  - `keywords` (array[string]): Extracted keywords
  - `index_node_id` (string): Vector index ID
  - `index_node_hash` (string): Content hash
  - `hit_count` (integer): Retrieval hit count
  - `enabled` (boolean): Whether enabled
  - `disabled_at` (timestamp): Disable time
  - `disabled_by` (string): Disabled by user
  - `status` (string): Processing status
  - `created_by` (string): Creator ID
  - `created_at` (timestamp): Creation time
  - `indexing_at` (timestamp): Indexing time
  - `completed_at` (timestamp): Completion time
  - `error` (string): Error message
  - `stopped_at` (timestamp): Stop time

#### 17. Create Segment

**POST** `/datasets/{dataset_id}/documents/{document_id}/segments`

Adds a new segment to a document.

##### Path Parameters
- `dataset_id` (string, required): Dataset ID (UUID)
- `document_id` (string, required): Document ID (UUID)

##### Request Body
- `segments` (array, required): List of segments to create
  - `content` (string, required): Segment content
  - `answer` (string, optional): Associated answer for Q&A
  - `keywords` (array[string], optional): Keywords

#### 18. Get Segment

**GET** `/datasets/{dataset_id}/documents/{document_id}/segments/{segment_id}`

Retrieves detailed information about a specific segment.

##### Path Parameters
- `dataset_id` (string, required): Dataset ID (UUID)
- `document_id` (string, required): Document ID (UUID)
- `segment_id` (string, required): Segment ID (UUID)

#### 19. Update Segment

**POST** `/datasets/{dataset_id}/documents/{document_id}/segments/{segment_id}`

Updates the content and metadata of a segment.

##### Path Parameters
- `dataset_id` (string, required): Dataset ID (UUID)
- `document_id` (string, required): Document ID (UUID)
- `segment_id` (string, required): Segment ID (UUID)

##### Request Body
- `segment` (object, required): Updated segment data
  - `content` (string): New content
  - `answer` (string): Associated answer
  - `keywords` (array[string]): Keywords

#### 20. Delete Segment

**DELETE** `/datasets/{dataset_id}/documents/{document_id}/segments/{segment_id}`

Permanently removes a segment from the document.

##### Path Parameters
- `dataset_id` (string, required): Dataset ID (UUID)
- `document_id` (string, required): Document ID (UUID)
- `segment_id` (string, required): Segment ID (UUID)

### Child Chunks Management

#### 21. List Child Chunks

**GET** `/datasets/{dataset_id}/documents/{document_id}/segments/{segment_id}/child_chunks`

Retrieves all child chunks (sub-segments) of a segment.

##### Path Parameters
- `dataset_id` (string, required): Dataset ID (UUID)
- `document_id` (string, required): Document ID (UUID)
- `segment_id` (string, required): Segment ID (UUID)

#### 22. Create Child Chunk

**POST** `/datasets/{dataset_id}/documents/{document_id}/segments/{segment_id}/child_chunks`

Creates new child chunks within a segment.

##### Path Parameters
- `dataset_id` (string, required): Dataset ID (UUID)
- `document_id` (string, required): Document ID (UUID)
- `segment_id` (string, required): Segment ID (UUID)

##### Request Body
- `chunks` (array, required): List of child chunks to create
  - `content` (string, required): Chunk content
  - `keywords` (array[string], optional): Keywords

#### 23. Update Child Chunk

**PATCH** `/datasets/{dataset_id}/documents/{document_id}/segments/{segment_id}/child_chunks/{child_chunk_id}`

Updates a specific child chunk.

##### Path Parameters
- `dataset_id` (string, required): Dataset ID (UUID)
- `document_id` (string, required): Document ID (UUID)
- `segment_id` (string, required): Segment ID (UUID)
- `child_chunk_id` (string, required): Child chunk ID (UUID)

#### 24. Delete Child Chunk

**DELETE** `/datasets/{dataset_id}/documents/{document_id}/segments/{segment_id}/child_chunks/{child_chunk_id}`

Removes a child chunk from the segment.

##### Path Parameters
- `dataset_id` (string, required): Dataset ID (UUID)
- `document_id` (string, required): Document ID (UUID)
- `segment_id` (string, required): Segment ID (UUID)
- `child_chunk_id` (string, required): Child chunk ID (UUID)

### Tags and Metadata Management

#### 25. List All Tags

**GET** `/datasets/tags`

Retrieves all available tags in the workspace.

##### Query Parameters
- `type` (string, optional): Filter by tag type (`knowledge_type`, `custom`)

##### Response
- `data` (array): List of tags
  - `id` (string): Tag ID
  - `name` (string): Tag name
  - `type` (string): Tag type
  - `binding_count` (integer): Number of datasets using this tag

#### 26. Create Tag

**POST** `/datasets/tags`

Creates a new tag for organizing datasets.

##### Request Body
- `name` (string, required): Tag name
- `type` (string, required): Tag type (`knowledge_type`, `custom`)

#### 27. Update Tag

**PATCH** `/datasets/tags`

Updates an existing tag.

##### Request Body
- `tag_id` (string, required): Tag ID to update
- `name` (string, required): New tag name

#### 28. Delete Tag

**DELETE** `/datasets/tags`

Removes a tag from the system.

##### Request Body
- `tag_id` (string, required): Tag ID to delete

#### 29. Bind Tags to Dataset

**POST** `/datasets/tags/binding`

Associates tags with a dataset.

##### Request Body
- `dataset_id` (string, required): Dataset ID
- `tag_ids` (array[string], required): List of tag IDs to bind

#### 30. Unbind Tags from Dataset

**POST** `/datasets/tags/unbinding`

Removes tag associations from a dataset.

##### Request Body
- `dataset_id` (string, required): Dataset ID
- `tag_ids` (array[string], required): List of tag IDs to unbind

#### 31. Get Dataset Tags

**POST** `/datasets/{dataset_id}/tags`

Retrieves all tags associated with a specific dataset.

##### Path Parameters
- `dataset_id` (string, required): Dataset ID (UUID)

### File Upload

#### 32. Get Upload File Info

**GET** `/datasets/{dataset_id}/documents/{document_id}/upload-file`

Retrieves information about an uploaded file.

##### Path Parameters
- `dataset_id` (string, required): Dataset ID (UUID)
- `document_id` (string, required): Document ID (UUID)

##### Response
- `id` (string): File ID
- `name` (string): Original filename
- `size` (integer): File size in bytes
- `extension` (string): File extension
- `mime_type` (string): MIME type
- `created_by` (string): Uploader ID
- `created_at` (timestamp): Upload time

### Models

#### 33. Get Text Embedding Models

**GET** `/workspaces/current/models/model-types/text-embedding`

Retrieves available text embedding models for the workspace.

##### Response
- `data` (array): List of available models
  - `model_name` (string): Model identifier
  - `model_type` (string): Model type
  - `provider` (object): Provider information
    - `provider_name` (string): Provider name
    - `provider_type` (string): Provider type
  - `credentials` (object): Model credentials status
  - `load_balancing` (object): Load balancing configuration

## Error Responses

All APIs return standard HTTP status codes with detailed error information:

- **400 Bad Request**: Invalid parameters or request format
- **401 Unauthorized**: Missing or invalid API key
- **403 Forbidden**: Insufficient permissions
- **404 Not Found**: Resource not found
- **413 Payload Too Large**: File size exceeds limits
- **415 Unsupported Media Type**: Invalid file format
- **422 Unprocessable Entity**: Validation errors
- **429 Too Many Requests**: Rate limit exceeded
- **500 Internal Server Error**: Server error

### Error Response Format

```json
{
  "code": "invalid_param",
  "message": "Invalid parameter: name is required",
  "status": 400
}
```

## Usage Examples

### Basic Dataset Creation and Document Upload

```python
# Create dataset
dataset_data = {
    "name": "Product Knowledge Base",
    "indexing_technique": "high_quality",
    "permission": "all_team_members"
}

# Upload document
with open("manual.pdf", "rb") as f:
    files = {"file": f}
    data = {
        "data": json.dumps({
            "name": "Product Manual",
            "indexing_technique": "high_quality"
        })
    }
    response = requests.post(f"/datasets/{dataset_id}/document/create-by-file", 
                           files=files, data=data)
```

### Content Retrieval

```python
# Search for relevant content
search_data = {
    "query": "How to install the product?",
    "top_k": 5,
    "score_threshold": 0.7
}

response = requests.post(f"/datasets/{dataset_id}/retrieve", json=search_data)
results = response.json()["records"]
```

## Best Practices

1. **Indexing Strategy**: Use `high_quality` indexing for better accuracy, `economy` for cost optimization
2. **Document Processing**: Monitor batch indexing status before using documents
3. **Content Retrieval**: Adjust `top_k` and `score_threshold` based on your use case
4. **Tag Management**: Use tags to organize datasets by domain or purpose
5. **Segment Management**: Keep segments focused and coherent for better retrieval
6. **File Formats**: Support varies by deployment - check supported formats
7. **Rate Limits**: Implement proper retry logic for production applications

## Supported File Formats

Common supported formats include:
- **Documents**: PDF, DOC, DOCX, TXT, MD
- **Spreadsheets**: XLS, XLSX, CSV
- **Presentations**: PPT, PPTX
- **Web**: HTML, XML
- **Code**: Various programming language files

*Note: Exact format support may vary by deployment configuration.*