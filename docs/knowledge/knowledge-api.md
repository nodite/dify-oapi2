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

The Knowledge Base API provides 21 endpoints with 33 total methods organized into 6 main categories:

### Dataset Management (6 APIs)
- **POST** `/datasets` - Create Dataset
- **GET** `/datasets` - List Datasets
- **GET** `/datasets/{dataset_id}` - Get Dataset
- **PATCH** `/datasets/{dataset_id}` - Update Dataset
- **DELETE** `/datasets/{dataset_id}` - Delete Dataset
- **POST** `/datasets/{dataset_id}/retrieve` - Retrieve from Dataset

### Document Management (10 APIs)
- **POST** `/datasets/{dataset_id}/document/create-by-file` - Create Document by File
- **POST** `/datasets/{dataset_id}/document/create-by-text` - Create Document by Text
- **GET** `/datasets/{dataset_id}/documents` - List Documents
- **GET** `/datasets/{dataset_id}/documents/{document_id}` - Get Document
- **POST** `/datasets/{dataset_id}/documents/{document_id}/update-by-file` - Update Document by File
- **POST** `/datasets/{dataset_id}/documents/{document_id}/update-by-text` - Update Document by Text
- **DELETE** `/datasets/{dataset_id}/documents/{document_id}` - Delete Document
- **PATCH** `/datasets/{dataset_id}/documents/status/{action}` - Document Status Management
- **GET** `/datasets/{dataset_id}/documents/{batch}/indexing-status` - Get Batch Indexing Status
- **GET** `/datasets/{dataset_id}/documents/{document_id}/upload-file` - Get Upload File Info

### Segment Management (5 APIs)
- **GET** `/datasets/{dataset_id}/documents/{document_id}/segments` - List Segments
- **POST** `/datasets/{dataset_id}/documents/{document_id}/segments` - Create Segment
- **GET** `/datasets/{dataset_id}/documents/{document_id}/segments/{segment_id}` - Get Segment
- **POST** `/datasets/{dataset_id}/documents/{document_id}/segments/{segment_id}` - Update Segment
- **DELETE** `/datasets/{dataset_id}/documents/{document_id}/segments/{segment_id}` - Delete Segment

### Child Chunks Management (4 APIs)
- **GET** `/datasets/{dataset_id}/documents/{document_id}/segments/{segment_id}/child_chunks` - List Child Chunks
- **POST** `/datasets/{dataset_id}/documents/{document_id}/segments/{segment_id}/child_chunks` - Create Child Chunk
- **PATCH** `/datasets/{dataset_id}/documents/{document_id}/segments/{segment_id}/child_chunks/{child_chunk_id}` - Update Child Chunk
- **DELETE** `/datasets/{dataset_id}/documents/{document_id}/segments/{segment_id}/child_chunks/{child_chunk_id}` - Delete Child Chunk

### Tags Management (7 APIs)
- **GET** `/datasets/tags` - List All Tags
- **POST** `/datasets/tags` - Create Tag
- **PATCH** `/datasets/tags` - Update Tag
- **DELETE** `/datasets/tags` - Delete Tag
- **POST** `/datasets/tags/binding` - Bind Tags to Dataset
- **POST** `/datasets/tags/unbinding` - Unbind Tags from Dataset
- **POST** `/datasets/{dataset_id}/tags` - Get Dataset Tags

### Models (1 API)
- **GET** `/workspaces/current/models/model-types/text-embedding` - Get Text Embedding Models

## APIs

### Dataset Management

#### 1. Create Dataset

**POST** `/datasets`

Creates a new knowledge base (dataset) for storing and managing documents.

#### Request Body (application/json)
```json
{
  "name": {
    "type": "string",
    "required": true,
    "description": "Name of the knowledge base."
  },
  "description": {
    "type": "string",
    "description": "Description of the knowledge base (optional)."
  },
  "indexing_technique": {
    "type": "string",
    "description": "The indexing technique to use.",
    "enum": ["high_quality", "economy"]
  },
  "permission": {
    "type": "string",
    "description": "Access permissions for the knowledge base.",
    "enum": ["only_me", "all_team_members", "partial_members"]
  },
  "provider": {
    "type": "string",
    "description": "The provider of the knowledge base.",
    "enum": ["vendor", "external"]
  },
  "external_knowledge_api_id": {
    "type": "string",
    "description": "ID of the external knowledge API (if provider is 'external')."
  },
  "external_knowledge_id": {
    "type": "string",
    "description": "ID of the external knowledge (if provider is 'external')."
  },
  "embedding_model": {
    "type": "string",
    "description": "Name of the embedding model."
  },
  "embedding_model_provider": {
    "type": "string",
    "description": "Provider of the embedding model."
  },
  "retrieval_model": {
    "type": "object",
    "description": "Retrieval model configuration",
    "properties": {
      "search_method": {
        "type": "string",
        "description": "The search method to use for retrieval",
        "enum": ["hybrid_search", "semantic_search", "full_text_search", "keyword_search"]
      },
      "reranking_enable": {
        "type": "boolean",
        "description": "Whether to enable a reranking model to improve search results"
      },
      "reranking_mode": {
        "type": "object",
        "description": "Configuration for the reranking model",
        "properties": {
          "reranking_provider_name": {
            "type": "string",
            "description": "The provider of the rerank model"
          },
          "reranking_model_name": {
            "type": "string",
            "description": "The name of the rerank model"
          }
        }
      },
      "top_k": {
        "type": "integer",
        "description": "The number of top matching results to return"
      },
      "score_threshold_enabled": {
        "type": "boolean",
        "description": "Whether to apply a score threshold to filter results"
      },
      "score_threshold": {
        "type": "number",
        "description": "The minimum score for a result to be included"
      },
      "weights": {
        "type": "number",
        "description": "The weight of semantic search in a hybrid search mode"
      }
    }
  }
}
```

#### Example Request
```json
{
  "name": "Product Documentation",
  "description": "Knowledge base for product documentation and FAQs",
  "indexing_technique": "high_quality",
  "permission": "all_team_members",
  "provider": "vendor",
  "embedding_model": "text-embedding-ada-002",
  "embedding_model_provider": "openai"
}
```

#### Response

**Success (200)**
```json
{
  "id": "string (uuid)",
  "name": "string",
  "description": "string (nullable)",
  "provider": "string",
  "permission": "string",
  "data_source_type": "string (nullable)",
  "indexing_technique": "string (nullable)",
  "app_count": "integer",
  "document_count": "integer",
  "word_count": "integer",
  "created_by": "string (uuid)",
  "created_at": "integer (int64)",
  "updated_by": "string (uuid)",
  "updated_at": "integer (int64)",
  "embedding_model": "string (nullable)",
  "embedding_model_provider": "string (nullable)",
  "embedding_available": "boolean (nullable)"
}
```

**Error Responses**
- **400**: Bad Request - Invalid parameters
- **401**: Unauthorized - Invalid API key
- **403**: Forbidden - Insufficient permissions

#### 2. List Datasets

**GET** `/datasets`

Retrieves all datasets accessible to the current user.

#### Query Parameters
- `page` (integer, optional): Page number, default 1
- `limit` (integer, optional): Items per page, default 20

#### Response

**Success (200)**
```json
{
  "data": [
    {
      "id": "string (uuid)",
      "name": "string",
      "description": "string (nullable)",
      "provider": "string",
      "permission": "string",
      "data_source_type": "string (nullable)",
      "indexing_technique": "string (nullable)",
      "app_count": "integer",
      "document_count": "integer",
      "word_count": "integer",
      "created_by": "string (uuid)",
      "created_at": "integer (int64)",
      "updated_by": "string (uuid)",
      "updated_at": "integer (int64)",
      "embedding_model": "string (nullable)",
      "embedding_model_provider": "string (nullable)",
      "embedding_available": "boolean (nullable)"
    }
  ],
  "has_more": "boolean",
  "limit": "integer",
  "total": "integer",
  "page": "integer"
}
```

#### 3. Get Dataset

**GET** `/datasets/{dataset_id}`

Retrieves detailed information about a specific dataset.

#### Path Parameters
- `dataset_id` (string, required): Dataset ID (UUID)

#### Response

**Success (200)**
Same structure as Create Dataset response.

#### 4. Update Dataset

**PATCH** `/datasets/{dataset_id}`

Updates dataset configuration and settings.

#### Path Parameters
- `dataset_id` (string, required): Dataset ID (UUID)

#### Request Body (application/json)
Same fields as Create Dataset (all optional for updates).

#### Response

**Success (200)**
Same structure as Create Dataset response.

#### 5. Delete Dataset

**DELETE** `/datasets/{dataset_id}`

Permanently removes a dataset and all its contents.

#### Path Parameters
- `dataset_id` (string, required): Dataset ID (UUID)

#### Response

**Success (200)**
```json
{
  "result": "success"
}
```

#### 6. Retrieve from Dataset

**POST** `/datasets/{dataset_id}/retrieve`

Searches and retrieves relevant content from the dataset.

#### Path Parameters
- `dataset_id` (string, required): Dataset ID (UUID)

#### Request Body (application/json)
```json
{
  "query": {
    "type": "string",
    "required": true,
    "description": "Search query"
  },
  "retrieval_model": {
    "type": "object",
    "description": "Override retrieval settings"
  },
  "top_k": {
    "type": "integer",
    "description": "Number of results to return"
  },
  "score_threshold": {
    "type": "number",
    "description": "Minimum relevance score"
  }
}
```

#### Response

**Success (200)**
```json
{
  "query": {
    "content": "string"
  },
  "records": [
    {
      "segment": {
        "id": "string (uuid)",
        "content": "string",
        "document": {
          "id": "string (uuid)",
          "data_source_type": "string",
          "name": "string"
        }
      },
      "score": "number (float)"
    }
  ]
}
```

### Document Management

#### 7. Create Document by File

**POST** `/datasets/{dataset_id}/document/create-by-file`

Uploads and processes a file to create a new document in the dataset.

#### Path Parameters
- `dataset_id` (string, required): Dataset ID (UUID)

#### Request Body (multipart/form-data)
- `data` (string, required): JSON string containing document metadata
  ```json
  {
    "original_document_id": {
      "type": "string",
      "format": "uuid",
      "description": "ID of an existing document to re-upload or modify"
    },
    "indexing_technique": {
      "type": "string",
      "enum": ["high_quality", "economy"]
    },
    "doc_form": {
      "type": "string",
      "enum": ["text_model", "hierarchical_model", "qa_model"]
    },
    "doc_language": {
      "type": "string",
      "example": "English"
    },
    "process_rule": {
      "$ref": "ProcessRule schema"
    },
    "retrieval_model": {
      "$ref": "RetrievalModel schema"
    },
    "embedding_model": {
      "type": "string"
    },
    "embedding_model_provider": {
      "type": "string"
    }
  }
  ```
- `file` (binary, required): File to upload

#### Response

**Success (200)**
```json
{
  "document": {
    "$ref": "Document schema (same as List Documents response)"
  },
  "batch": "string (batch identifier for tracking indexing progress)"
}
```

#### 8. Create Document by Text

**POST** `/datasets/{dataset_id}/document/create-by-text`

Creates a document directly from text content.

#### Path Parameters
- `dataset_id` (string, required): Dataset ID (UUID)

#### Request Body (application/json)
```json
{
  "name": {
    "type": "string",
    "required": true,
    "description": "Document name"
  },
  "text": {
    "type": "string",
    "required": true,
    "description": "Document content"
  },
  "indexing_technique": {
    "type": "string",
    "description": "Indexing technique for the document",
    "enum": ["high_quality", "economy"]
  },
  "doc_form": {
    "type": "string",
    "description": "Format of the indexed content",
    "enum": ["text_model", "hierarchical_model", "qa_model"]
  },
  "doc_language": {
    "type": "string",
    "description": "Language of the document, important for Q&A mode",
    "example": "English"
  },
  "process_rule": {
    "type": "object",
    "description": "Processing configuration",
    "$ref": "ProcessRule schema"
  },
  "retrieval_model": {
    "type": "object",
    "description": "Retrieval model configuration",
    "$ref": "RetrievalModel schema"
  },
  "embedding_model": {
    "type": "string",
    "description": "Name of the embedding model to use"
  },
  "embedding_model_provider": {
    "type": "string",
    "description": "Provider of the embedding model"
  }
}
```

#### Response

**Success (200)**
Same structure as Create Document by File.

#### 9. List Documents

**GET** `/datasets/{dataset_id}/documents`

Retrieves all documents in a dataset with pagination.

#### Path Parameters
- `dataset_id` (string, required): Dataset ID (UUID)

#### Query Parameters
- `keyword` (string, optional): Search keyword
- `page` (integer, optional): Page number, default 1
- `limit` (integer, optional): Items per page, default 20

#### Response

**Success (200)**
```json
{
  "data": [
    {
      "id": "string (uuid)",
      "position": "integer",
      "data_source_type": "string",
      "data_source_info": "object (nullable)",
      "dataset_process_rule_id": "string (uuid, nullable)",
      "name": "string",
      "created_from": "string",
      "created_by": "string (uuid)",
      "created_at": "integer (int64)",
      "tokens": "integer",
      "indexing_status": "string",
      "error": "string (nullable)",
      "enabled": "boolean",
      "disabled_at": "integer (int64, nullable)",
      "disabled_by": "string (uuid, nullable)",
      "archived": "boolean",
      "display_status": "string",
      "word_count": "integer",
      "hit_count": "integer",
      "doc_form": "string"
    }
  ],
  "has_more": "boolean",
  "limit": "integer",
  "total": "integer",
  "page": "integer"
}
```

#### 10. Get Document

**GET** `/datasets/{dataset_id}/documents/{document_id}`

Retrieves detailed information about a specific document.

#### Path Parameters
- `dataset_id` (string, required): Dataset ID (UUID)
- `document_id` (string, required): Document ID (UUID)

#### Response

**Success (200)**
Same structure as individual document in List Documents response.

#### 11. Update Document by File

**POST** `/datasets/{dataset_id}/documents/{document_id}/update-by-file`

Replaces document content with a new file.

#### Path Parameters
- `dataset_id` (string, required): Dataset ID (UUID)
- `document_id` (string, required): Document ID (UUID)

#### Request Body (multipart/form-data)
Same as Create Document by File.

#### Response

**Success (200)**
Same structure as Create Document by File.

#### 12. Update Document by Text

**POST** `/datasets/{dataset_id}/documents/{document_id}/update-by-text`

Updates document content with new text.

#### Path Parameters
- `dataset_id` (string, required): Dataset ID (UUID)
- `document_id` (string, required): Document ID (UUID)

#### Request Body (application/json)
Same as Create Document by Text.

#### Response

**Success (200)**
Same structure as Create Document by Text.

#### 13. Delete Document

**DELETE** `/datasets/{dataset_id}/documents/{document_id}`

Permanently removes a document from the dataset.

#### Path Parameters
- `dataset_id` (string, required): Dataset ID (UUID)
- `document_id` (string, required): Document ID (UUID)

#### Response

**Success (200)**
```json
{
  "result": "success"
}
```

#### 14. Document Status Management

**PATCH** `/datasets/{dataset_id}/documents/status/{action}`

Enables or disables documents in batch.

#### Path Parameters
- `dataset_id` (string, required): Dataset ID (UUID)
- `action` (string, required): Action to perform
  - **Enum values**: `enable`, `disable`, `archive`, `un_archive`

#### Request Body (application/json)
```json
{
  "document_ids": {
    "type": "array",
    "items": {
      "type": "string"
    },
    "required": true,
    "description": "List of document IDs"
  }
}
```

#### Response

**Success (200)**
```json
{
  "result": "success"
}
```

#### 15. Get Batch Indexing Status

**GET** `/datasets/{dataset_id}/documents/{batch}/indexing-status`

Checks the processing status of a document batch.

#### Path Parameters
- `dataset_id` (string, required): Dataset ID (UUID)
- `batch` (string, required): Batch ID from document creation

#### Response

**Success (200)**
```json
{
  "id": "string (uuid)",
  "indexing_status": "string",
  "processing_started_at": "number (float, nullable)",
  "parsing_completed_at": "number (float, nullable)",
  "cleaning_completed_at": "number (float, nullable)",
  "splitting_completed_at": "number (float, nullable)",
  "completed_at": "number (float, nullable)",
  "paused_at": "number (float, nullable)",
  "error": "string (nullable)",
  "stopped_at": "number (float, nullable)",
  "completed_segments": "integer",
  "total_segments": "integer"
}
```

**Indexing Status Enum Values**: `waiting`, `parsing`, `cleaning`, `splitting`, `indexing`, `completed`, `error`, `paused`

#### 16. Get Upload File Info

**GET** `/datasets/{dataset_id}/documents/{document_id}/upload-file`

Retrieves information about an uploaded file.

#### Path Parameters
- `dataset_id` (string, required): Dataset ID (UUID)
- `document_id` (string, required): Document ID (UUID)

#### Response

**Success (200)**
```json
{
  "id": "string (uuid)",
  "name": "string",
  "size": "integer",
  "extension": "string",
  "mime_type": "string",
  "created_by": "string (uuid)",
  "created_at": "integer (int64)"
}
```

### Segment Management

#### 17. List Segments

**GET** `/datasets/{dataset_id}/documents/{document_id}/segments`

Retrieves all segments (chunks) of a document.

#### Path Parameters
- `dataset_id` (string, required): Dataset ID (UUID)
- `document_id` (string, required): Document ID (UUID)

#### Query Parameters
- `keyword` (string, optional): Keyword to filter segments by content
- `status` (string, optional): Filter segments by their indexing status (e.g., "completed")
- `page` (integer, optional): Page number, default 1
- `limit` (integer, optional): Items per page, default 20, max 100

#### Response

**Success (200)**
```json
{
  "data": [
    {
      "id": "string (uuid)",
      "position": "integer",
      "document_id": "string (uuid)",
      "content": "string",
      "answer": "string (nullable)",
      "word_count": "integer",
      "tokens": "integer",
      "keywords": ["string"],
      "index_node_id": "string",
      "index_node_hash": "string",
      "hit_count": "integer",
      "enabled": "boolean",
      "disabled_at": "integer (int64, nullable)",
      "disabled_by": "string (uuid, nullable)",
      "status": "string",
      "created_by": "string (uuid)",
      "created_at": "integer (int64)",
      "indexing_at": "integer (int64)",
      "completed_at": "integer (int64)",
      "error": "string (nullable)",
      "stopped_at": "integer (int64, nullable)"
    }
  ],
  "doc_form": "string",
  "has_more": "boolean",
  "limit": "integer",
  "total": "integer",
  "page": "integer"
}
```

#### 18. Create Segments

**POST** `/datasets/{dataset_id}/documents/{document_id}/segments`

Adds one or more new chunks (segments) to a specific document.

#### Path Parameters
- `dataset_id` (string, required): Dataset ID (UUID)
- `document_id` (string, required): Document ID (UUID)

#### Request Body (application/json)
```json
{
  "segments": [
    {
      "content": {
        "type": "string",
        "required": true,
        "description": "The text content of the chunk (or question in Q&A mode)"
      },
      "answer": {
        "type": "string",
        "description": "The answer content, required if the document is in Q&A mode"
      },
      "keywords": {
        "type": "array",
        "items": {"type": "string"},
        "description": "Keywords associated with the chunk"
      }
    }
  ]
}
```

#### Response

**Success (200)**
```json
{
  "data": [
    {
      "$ref": "Segment schema (same as List Segments response)"
    }
  ],
  "doc_form": "string"
}
```

#### 19. Get Segment Detail

**GET** `/datasets/{dataset_id}/documents/{document_id}/segments/{segment_id}`

Retrieves detailed information about a specific segment.

#### Path Parameters
- `dataset_id` (string, required): Dataset ID (UUID)
- `document_id` (string, required): Document ID (UUID)
- `segment_id` (string, required): Segment ID (UUID)

#### Response

**Success (200)**
```json
{
  "data": {
    "$ref": "Segment schema (same as List Segments response)"
  },
  "doc_form": "string"
}
```

#### 20. Update Segment

**POST** `/datasets/{dataset_id}/documents/{document_id}/segments/{segment_id}`

Updates the content, keywords, or status of a specific segment.

#### Path Parameters
- `dataset_id` (string, required): Dataset ID (UUID)
- `document_id` (string, required): Document ID (UUID)
- `segment_id` (string, required): Segment ID (UUID)

#### Request Body (application/json)
```json
{
  "segment": {
    "content": {
      "type": "string",
      "required": true
    },
    "answer": {
      "type": "string"
    },
    "keywords": {
      "type": "array",
      "items": {"type": "string"}
    },
    "enabled": {
      "type": "boolean"
    },
    "regenerate_child_chunks": {
      "type": "boolean",
      "description": "Whether to regenerate child chunks (hierarchical mode)"
    }
  }
}
```

#### Response

**Success (200)**
Same structure as Get Segment Detail.

#### 21. Delete Segment

**DELETE** `/datasets/{dataset_id}/documents/{document_id}/segments/{segment_id}`

Deletes a specific segment from a document.

#### Path Parameters
- `dataset_id` (string, required): Dataset ID (UUID)
- `document_id` (string, required): Document ID (UUID)
- `segment_id` (string, required): Segment ID (UUID)

#### Response

**Success (204)**
No content - successfully deleted.

### Child Chunk Management

#### 22. Create Child Chunk

**POST** `/datasets/{dataset_id}/documents/{document_id}/segments/{segment_id}/child_chunks`

Creates a new child chunk under a parent segment in hierarchical mode.

#### Path Parameters
- `dataset_id` (string, required): Dataset ID (UUID)
- `document_id` (string, required): Document ID (UUID)
- `segment_id` (string, required): Parent segment ID (UUID)

#### Request Body (application/json)
```json
{
  "content": {
    "type": "string",
    "required": true,
    "description": "The content of the child chunk"
  }
}
```

#### Response

**Success (200)**
```json
{
  "data": {
    "id": "string (uuid)",
    "segment_id": "string (uuid)",
    "content": "string",
    "word_count": "integer",
    "tokens": "integer",
    "index_node_id": "string",
    "index_node_hash": "string",
    "status": "string",
    "created_by": "string (uuid)",
    "created_at": "integer (int64)",
    "indexing_at": "integer (int64)",
    "completed_at": "integer (int64)",
    "error": "string (nullable)",
    "stopped_at": "integer (int64, nullable)"
  }
}
```

#### 23. List Child Chunks

**GET** `/datasets/{dataset_id}/documents/{document_id}/segments/{segment_id}/child_chunks`

Retrieves a list of child chunks for a specific parent segment.

#### Path Parameters
- `dataset_id` (string, required): Dataset ID (UUID)
- `document_id` (string, required): Document ID (UUID)
- `segment_id` (string, required): Parent segment ID (UUID)

#### Query Parameters
- `keyword` (string, optional): Search keyword to filter child chunks
- `page` (integer, optional): Page number, default 1
- `limit` (integer, optional): Items per page, default 20, max 100

#### Response

**Success (200)**
```json
{
  "data": [
    {
      "$ref": "ChildChunk schema (same as Create Child Chunk response)"
    }
  ],
  "total": "integer",
  "total_pages": "integer",
  "page": "integer",
  "limit": "integer"
}
```

#### 24. Update Child Chunk

**PATCH** `/datasets/{dataset_id}/documents/{document_id}/segments/{segment_id}/child_chunks/{child_chunk_id}`

Updates the content of a specific child chunk.

#### Path Parameters
- `dataset_id` (string, required): Dataset ID (UUID)
- `document_id` (string, required): Document ID (UUID)
- `segment_id` (string, required): Parent segment ID (UUID)
- `child_chunk_id` (string, required): Child chunk ID (UUID)

#### Request Body (application/json)
```json
{
  "content": {
    "type": "string",
    "required": true,
    "description": "The updated content for the child chunk"
  }
}
```

#### Response

**Success (200)**
Same structure as Create Child Chunk.

#### 25. Delete Child Chunk

**DELETE** `/datasets/{dataset_id}/documents/{document_id}/segments/{segment_id}/child_chunks/{child_chunk_id}`

Deletes a specific child chunk.

#### Path Parameters
- `dataset_id` (string, required): Dataset ID (UUID)
- `document_id` (string, required): Document ID (UUID)
- `segment_id` (string, required): Parent segment ID (UUID)
- `child_chunk_id` (string, required): Child chunk ID (UUID)

#### Response

**Success (204)**
No content - successfully deleted.

### Tag Management

#### 26. Create Knowledge Base Tag

**POST** `/datasets/tags`

Creates a new tag that can be used to categorize knowledge bases.

#### Request Body (application/json)
```json
{
  "name": {
    "type": "string",
    "required": true,
    "maxLength": 50,
    "description": "The name of the new tag"
  }
}
```

#### Response

**Success (200)**
```json
{
  "id": "string (uuid)",
  "name": "string",
  "type": "string (example: knowledge)",
  "binding_count": "integer"
}
```

#### 27. Get Knowledge Base Tags

**GET** `/datasets/tags`

Retrieves a list of all available knowledge base tags.

#### Response

**Success (200)**
```json
[
  {
    "id": "string (uuid)",
    "name": "string",
    "type": "string",
    "binding_count": "integer"
  }
]
```

#### 28. Update Knowledge Base Tag

**PATCH** `/datasets/tags`

Updates the name of an existing tag.

#### Request Body (application/json)
```json
{
  "tag_id": {
    "type": "string",
    "format": "uuid",
    "required": true,
    "description": "The ID of the tag to modify"
  },
  "name": {
    "type": "string",
    "required": true,
    "maxLength": 50,
    "description": "The new name for the tag"
  }
}
```

#### Response

**Success (200)**
Same structure as Create Knowledge Base Tag.

#### 29. Delete Knowledge Base Tag

**DELETE** `/datasets/tags`

Deletes a tag. The tag must not be bound to any knowledge bases.

#### Request Body (application/json)
```json
{
  "tag_id": {
    "type": "string",
    "format": "uuid",
    "required": true,
    "description": "The ID of the tag to delete"
  }
}
```

#### Response

**Success (200)**
```json
{
  "result": "success"
}
```

#### 30. Bind Tags to Dataset

**POST** `/datasets/tags/binding`

Binds one or more tags to a specific knowledge base.

#### Request Body (application/json)
```json
{
  "target_id": {
    "type": "string",
    "format": "uuid",
    "required": true,
    "description": "The ID of the dataset to bind tags to"
  },
  "tag_ids": {
    "type": "array",
    "items": {"type": "string", "format": "uuid"},
    "required": true,
    "description": "A list of tag IDs to bind"
  }
}
```

#### Response

**Success (200)**
```json
{
  "result": "success"
}
```

#### 31. Unbind Tag from Dataset

**POST** `/datasets/tags/unbinding`

Unbinds a specific tag from a knowledge base.

#### Request Body (application/json)
```json
{
  "target_id": {
    "type": "string",
    "format": "uuid",
    "required": true,
    "description": "The ID of the dataset"
  },
  "tag_id": {
    "type": "string",
    "format": "uuid",
    "required": true,
    "description": "The ID of the tag to unbind"
  }
}
```

#### Response

**Success (200)**
```json
{
  "result": "success"
}
```

#### 32. Query Dataset Tags

**POST** `/datasets/{dataset_id}/tags`

Retrieves all tags that are currently bound to a specific dataset.

#### Path Parameters
- `dataset_id` (string, required): Dataset ID (UUID)

#### Response

**Success (200)**
```json
{
  "data": [
    {
      "id": "string (uuid)",
      "name": "string"
    }
  ],
  "total": "integer"
}
```

### Model Management

#### 33. Get Available Embedding Models

**GET** `/workspaces/current/models/model-types/text-embedding`

Fetches a list of all available text embedding models that can be used for creating and querying knowledge bases.

#### Response

**Success (200)**
```json
{
  "data": [
    {
      "provider": "string",
      "label": {
        "additionalProperties": "string"
      },
      "icon_small": {
        "additionalProperties": "string (uri)"
      },
      "icon_large": {
        "additionalProperties": "string (uri)"
      },
      "status": "string",
      "models": [
        {
          "model": "string",
          "label": {
            "additionalProperties": "string"
          },
          "model_type": "string",
          "features": "array (nullable)",
          "fetch_from": "string",
          "model_properties": {
            "context_size": "integer"
          },
          "deprecated": "boolean",
          "status": "string",
          "load_balancing_enabled": "boolean"
        }
      ]
    }
  ]
}
```

## 📋 Data Schemas

### ProcessRule Schema

```json
{
  "mode": {
    "type": "string",
    "enum": ["automatic", "custom", "hierarchical"],
    "description": "The processing mode"
  },
  "rules": {
    "type": "object",
    "nullable": true,
    "properties": {
      "pre_processing_rules": {
        "type": "array",
        "items": {
          "type": "object",
          "properties": {
            "id": {
              "type": "string",
              "enum": ["remove_extra_spaces", "remove_urls_emails"]
            },
            "enabled": {"type": "boolean"}
          }
        }
      },
      "segmentation": {
        "type": "object",
        "properties": {
          "separator": {"type": "string"},
          "max_tokens": {"type": "integer"}
        }
      },
      "parent_mode": {
        "type": "string",
        "enum": ["full-doc", "paragraph"]
      },
      "subchunk_segmentation": {
        "type": "object",
        "properties": {
          "separator": {"type": "string"},
          "max_tokens": {"type": "integer"},
          "chunk_overlap": {"type": "integer"}
        }
      }
    }
  }
}
```

### RetrievalModel Schema

```json
{
  "search_method": {
    "type": "string",
    "enum": ["hybrid_search", "semantic_search", "full_text_search", "keyword_search"]
  },
  "reranking_enable": {"type": "boolean"},
  "reranking_mode": {
    "type": "object",
    "nullable": true,
    "properties": {
      "reranking_provider_name": {"type": "string"},
      "reranking_model_name": {"type": "string"}
    }
  },
  "top_k": {"type": "integer"},
  "score_threshold_enabled": {"type": "boolean"},
  "score_threshold": {"type": "number", "nullable": true},
  "weights": {"type": "number", "nullable": true}
}
```

## 🔍 Enum Values

### Indexing Technique
- `high_quality`: High-quality indexing with better accuracy
- `economy`: Economy indexing with faster processing

### Document Form
- `text_model`: Standard text processing
- `hierarchical_model`: Hierarchical chunk processing
- `qa_model`: Question-answer format

### Permission Types
- `only_me`: Private access
- `all_team_members`: Team-wide access
- `partial_members`: Selective member access

### Search Methods
- `hybrid_search`: Combines semantic and keyword search
- `semantic_search`: Vector-based semantic search
- `full_text_search`: Traditional full-text search
- `keyword_search`: Keyword-based search

### Document Status Actions
- `enable`: Enable documents
- `disable`: Disable documents
- `archive`: Archive documents
- `un_archive`: Unarchive documents

### Indexing Status Values
- `waiting`: Waiting to be processed
- `parsing`: Parsing document content
- `cleaning`: Cleaning and preprocessing
- `splitting`: Splitting into segments
- `indexing`: Creating embeddings
- `completed`: Processing completed
- `error`: Processing failed
- `paused`: Processing paused `dataset_id` (string, required): Dataset ID (UUID)
- `document_id` (string, required): Document ID (UUID)

#### Query Parameters
- `keyword` (string, optional): Search keyword
- `status` (string, optional): Filter segments by their indexing status (e.g., "completed")

#### Response

**Success (200)**
```json
{
  "data": [
    {
      "id": "string (uuid)",
      "position": "integer",
      "document_id": "string (uuid)",
      "content": "string",
      "word_count": "integer",
      "tokens": "integer",
      "keywords": ["string"],
      "index_node_id": "string",
      "index_node_hash": "string",
      "hit_count": "integer",
      "enabled": "boolean",
      "disabled_at": "integer (int64, nullable)",
      "disabled_by": "string (uuid, nullable)",
      "status": "string",
      "created_by": "string (uuid)",
      "created_at": "integer (int64)",
      "indexing_at": "integer (int64)",
      "completed_at": "integer (int64)",
      "error": "string (nullable)",
      "stopped_at": "integer (int64, nullable)"
    }
  ]
}
```

#### 18. Create Segment

**POST** `/datasets/{dataset_id}/documents/{document_id}/segments`

Adds a new segment to a document.

#### Path Parameters
- `dataset_id` (string, required): Dataset ID (UUID)
- `document_id` (string, required): Document ID (UUID)

#### Request Body (application/json)
```json
{
  "segments": {
    "type": "array",
    "required": true,
    "items": {
      "type": "object",
      "properties": {
        "content": {
          "type": "string",
          "required": true,
          "description": "Segment content"
        },
        "answer": {
          "type": "string",
          "description": "Associated answer for Q&A"
        },
        "keywords": {
          "type": "array",
          "items": {
            "type": "string"
          },
          "description": "Keywords"
        }
      }
    }
  }
}
```

#### Response

**Success (200)**
```json
{
  "data": [
    {
      "id": "string (uuid)",
      "position": "integer",
      "document_id": "string (uuid)",
      "content": "string",
      "status": "string",
      "created_at": "integer (int64)"
    }
  ]
}
```

#### 19. Get Segment

**GET** `/datasets/{dataset_id}/documents/{document_id}/segments/{segment_id}`

Retrieves detailed information about a specific segment.

#### Path Parameters
- `dataset_id` (string, required): Dataset ID (UUID)
- `document_id` (string, required): Document ID (UUID)
- `segment_id` (string, required): Segment ID (UUID)

#### Response

**Success (200)**
Same structure as individual segment in List Segments response.

#### 20. Update Segment

**POST** `/datasets/{dataset_id}/documents/{document_id}/segments/{segment_id}`

Updates the content and metadata of a segment.

#### Path Parameters
- `dataset_id` (string, required): Dataset ID (UUID)
- `document_id` (string, required): Document ID (UUID)
- `segment_id` (string, required): Segment ID (UUID)

#### Request Body (application/json)
```json
{
  "segment": {
    "type": "object",
    "required": true,
    "properties": {
      "content": {
        "type": "string",
        "description": "New content"
      },
      "answer": {
        "type": "string",
        "description": "Associated answer"
      },
      "keywords": {
        "type": "array",
        "items": {
          "type": "string"
        },
        "description": "Keywords"
      }
    }
  }
}
```

#### Response

**Success (200)**
Same structure as Get Segment response.

#### 21. Delete Segment

**DELETE** `/datasets/{dataset_id}/documents/{document_id}/segments/{segment_id}`

Permanently removes a segment from the document.

#### Path Parameters
- `dataset_id` (string, required): Dataset ID (UUID)
- `document_id` (string, required): Document ID (UUID)
- `segment_id` (string, required): Segment ID (UUID)

#### Response

**Success (200)**
```json
{
  "result": "success"
}
```

### Child Chunks Management

#### 22. List Child Chunks

**GET** `/datasets/{dataset_id}/documents/{document_id}/segments/{segment_id}/child_chunks`

Retrieves all child chunks (sub-segments) of a segment.

#### Path Parameters
- `dataset_id` (string, required): Dataset ID (UUID)
- `document_id` (string, required): Document ID (UUID)
- `segment_id` (string, required): Segment ID (UUID)

#### Response

**Success (200)**
```json
{
  "data": [
    {
      "id": "string (uuid)",
      "content": "string",
      "keywords": ["string"],
      "created_at": "integer (int64)"
    }
  ]
}
```

#### 23. Create Child Chunk

**POST** `/datasets/{dataset_id}/documents/{document_id}/segments/{segment_id}/child_chunks`

Creates new child chunks within a segment.

#### Path Parameters
- `dataset_id` (string, required): Dataset ID (UUID)
- `document_id` (string, required): Document ID (UUID)
- `segment_id` (string, required): Segment ID (UUID)

#### Request Body (application/json)
```json
{
  "chunks": {
    "type": "array",
    "required": true,
    "items": {
      "type": "object",
      "properties": {
        "content": {
          "type": "string",
          "required": true,
          "description": "Chunk content"
        },
        "keywords": {
          "type": "array",
          "items": {
            "type": "string"
          },
          "description": "Keywords"
        }
      }
    }
  }
}
```

#### Response

**Success (200)**
Same structure as List Child Chunks response.

#### 24. Update Child Chunk

**PATCH** `/datasets/{dataset_id}/documents/{document_id}/segments/{segment_id}/child_chunks/{child_chunk_id}`

Updates a specific child chunk.

#### Path Parameters
- `dataset_id` (string, required): Dataset ID (UUID)
- `document_id` (string, required): Document ID (UUID)
- `segment_id` (string, required): Segment ID (UUID)
- `child_chunk_id` (string, required): Child chunk ID (UUID)

#### Request Body (application/json)
```json
{
  "content": {
    "type": "string",
    "description": "Updated chunk content"
  },
  "keywords": {
    "type": "array",
    "items": {
      "type": "string"
    },
    "description": "Updated keywords"
  }
}
```

#### Response

**Success (200)**
Same structure as individual child chunk in List Child Chunks response.

#### 25. Delete Child Chunk

**DELETE** `/datasets/{dataset_id}/documents/{document_id}/segments/{segment_id}/child_chunks/{child_chunk_id}`

Removes a child chunk from the segment.

#### Path Parameters
- `dataset_id` (string, required): Dataset ID (UUID)
- `document_id` (string, required): Document ID (UUID)
- `segment_id` (string, required): Segment ID (UUID)
- `child_chunk_id` (string, required): Child chunk ID (UUID)

#### Response

**Success (200)**
```json
{
  "result": "success"
}
```

### Tags Management

#### 26. List All Tags

**GET** `/datasets/tags`

Retrieves all available tags in the workspace.

#### Query Parameters
- `type` (string, optional): Filter by tag type
  - **Enum values**: `knowledge_type`, `custom`

#### Response

**Success (200)**
```json
{
  "data": [
    {
      "id": "string (uuid)",
      "name": "string",
      "type": "string",
      "binding_count": "integer"
    }
  ]
}
```

#### 27. Create Tag

**POST** `/datasets/tags`

Creates a new tag for organizing datasets.

#### Request Body (application/json)
```json
{
  "name": {
    "type": "string",
    "required": true,
    "description": "Tag name"
  },
  "type": {
    "type": "string",
    "required": true,
    "description": "Tag type",
    "enum": ["knowledge_type", "custom"]
  }
}
```

#### Response

**Success (200)**
```json
{
  "id": "string (uuid)",
  "name": "string",
  "type": "string",
  "binding_count": "integer"
}
```

#### 28. Update Tag

**PATCH** `/datasets/tags`

Updates an existing tag.

#### Request Body (application/json)
```json
{
  "tag_id": {
    "type": "string",
    "required": true,
    "description": "Tag ID to update"
  },
  "name": {
    "type": "string",
    "required": true,
    "description": "New tag name"
  }
}
```

#### Response

**Success (200)**
Same structure as Create Tag response.

#### 29. Delete Tag

**DELETE** `/datasets/tags`

Removes a tag from the system.

#### Request Body (application/json)
```json
{
  "tag_id": {
    "type": "string",
    "required": true,
    "description": "Tag ID to delete"
  }
}
```

#### Response

**Success (200)**
```json
{
  "result": "success"
}
```

#### 30. Bind Tags to Dataset

**POST** `/datasets/tags/binding`

Associates tags with a dataset.

#### Request Body (application/json)
```json
{
  "dataset_id": {
    "type": "string",
    "required": true,
    "description": "Dataset ID"
  },
  "tag_ids": {
    "type": "array",
    "items": {
      "type": "string"
    },
    "required": true,
    "description": "List of tag IDs to bind"
  }
}
```

#### Response

**Success (200)**
```json
{
  "result": "success"
}
```

#### 31. Unbind Tags from Dataset

**POST** `/datasets/tags/unbinding`

Removes tag associations from a dataset.

#### Request Body (application/json)
```json
{
  "dataset_id": {
    "type": "string",
    "required": true,
    "description": "Dataset ID"
  },
  "tag_ids": {
    "type": "array",
    "items": {
      "type": "string"
    },
    "required": true,
    "description": "List of tag IDs to unbind"
  }
}
```

#### Response

**Success (200)**
```json
{
  "result": "success"
}
```

#### 32. Get Dataset Tags

**POST** `/datasets/{dataset_id}/tags`

Retrieves all tags associated with a specific dataset.

#### Path Parameters
- `dataset_id` (string, required): Dataset ID (UUID)

#### Response

**Success (200)**
```json
{
  "data": [
    {
      "id": "string (uuid)",
      "name": "string",
      "type": "string"
    }
  ]
}
```

### Models

#### 33. Get Text Embedding Models

**GET** `/workspaces/current/models/model-types/text-embedding`

Retrieves available text embedding models for the workspace.

#### Response

**Success (200)**
```json
{
  "data": [
    {
      "provider": "string",
      "label": {
        "additionalProperties": "string"
      },
      "icon_small": {
        "additionalProperties": "string (uri)"
      },
      "icon_large": {
        "additionalProperties": "string (uri)"
      },
      "status": "string",
      "models": [
        {
          "model": "string",
          "label": {
            "additionalProperties": "string"
          },
          "model_type": "string",
          "features": "array (nullable)",
          "fetch_from": "string",
          "model_properties": {
            "context_size": "integer"
          },
          "deprecated": "boolean",
          "status": "string",
          "load_balancing_enabled": "boolean"
        }
      ]
    }
  ]
}
```

## Error Responses

All APIs return standard HTTP status codes with detailed error information:

- **200 OK**: Request successful
- **204 No Content**: Request successful with no content returned
- **400 Bad Request**: Invalid parameters or request format
  - **Error codes**: `invalid_param`, `dataset_not_initialized`, `dataset_name_duplicate`, `unsupported_file_type`, `no_file_uploaded`, `too_many_files`
- **401 Unauthorized**: Missing or invalid API key
- **403 Forbidden**: Insufficient permissions
- **404 Not Found**: Resource not found
- **409 Conflict**: Resource conflict (e.g., duplicate name)
- **413 Payload Too Large**: File size exceeds limits
- **415 Unsupported Media Type**: Invalid file format
- **422 Unprocessable Entity**: Validation errors
- **429 Too Many Requests**: Rate limit exceeded
- **500 Internal Server Error**: Server error

### Error Response Format

```json
{
  "code": "string",
  "message": "string",
  "status": "integer"
}
```

## Usage Examples

### Basic Dataset Creation and Document Upload

```python
import requests
import json

# Create dataset
dataset_data = {
    "name": "Product Knowledge Base",
    "indexing_technique": "high_quality",
    "permission": "all_team_members"
}

headers = {
    "Authorization": "Bearer YOUR_API_KEY",
    "Content-Type": "application/json"
}

response = requests.post(
    "https://api.dify.ai/v1/datasets",
    json=dataset_data,
    headers=headers
)
dataset = response.json()
dataset_id = dataset["id"]

# Upload document
with open("manual.pdf", "rb") as f:
    files = {"file": f}
    data = {
        "data": json.dumps({
            "name": "Product Manual",
            "indexing_technique": "high_quality"
        })
    }
    headers_upload = {"Authorization": "Bearer YOUR_API_KEY"}
    response = requests.post(
        f"https://api.dify.ai/v1/datasets/{dataset_id}/document/create-by-file",
        files=files,
        data=data,
        headers=headers_upload
    )
```

### Content Retrieval

```python
# Search for relevant content
search_data = {
    "query": "How to install the product?",
    "top_k": 5,
    "score_threshold": 0.7
}

response = requests.post(
    f"https://api.dify.ai/v1/datasets/{dataset_id}/retrieve",
    json=search_data,
    headers=headers
)
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
8. **External Knowledge**: Use `provider: "external"` for external knowledge bases
9. **Permissions**: Set appropriate permissions (`only_me`, `all_team_members`, `partial_members`)

## Supported File Formats

Common supported formats include:
- **Documents**: PDF, DOC, DOCX, TXT, MD
- **Spreadsheets**: XLS, XLSX, CSV
- **Presentations**: PPT, PPTX
- **Web**: HTML, XML
- **Code**: Various programming language files

*Note: Exact format support may vary by deployment configuration.*

## API Summary

Total APIs: **21 endpoints with 33 methods** across 6 categories:
- **Dataset Management**: 6 APIs
- **Document Management**: 10 APIs  
- **Segment Management**: 5 APIs
- **Child Chunks Management**: 4 APIs
- **Tags Management**: 7 APIs
- **Models**: 1 API

All APIs follow RESTful conventions with proper HTTP methods, consistent request/response formats, and comprehensive error handling.