# Knowledge Base API Implementation Plan

This document provides step-by-step prompts for implementing the complete Knowledge Base API module in dify-oapi2. Each implementation step is followed by a corresponding test step to ensure code quality and functionality.

## Overview

The Knowledge Base API module implements **33 APIs** across **6 specialized resources**:
- **Dataset Resource**: 6 APIs for dataset management (create, list, get, update, delete, retrieve)
- **Document Resource**: 10 APIs for document processing (create_by_file, create_by_text, list, get, update_by_file, update_by_text, delete, update_status, get_batch_status, file_info)
- **Segment Resource**: 5 APIs for content segmentation (list, create, get, update, delete)
- **Child Chunks Resource**: 4 APIs for sub-segment management (list, create, update, delete)
- **Tag Resource**: 7 APIs for metadata and tagging (list, create, update, delete, bind, unbind, get_dataset_tags)
- **Model Resource**: 1 API for embedding models (embedding_models)

## Prerequisites

Before starting, ensure you understand:
- The existing dify-oapi2 project structure and patterns
- Current knowledge implementation structure (if any)
- Pydantic models and builder patterns with type safety
- HTTP request/response handling with multipart/form-data support
- Strict type safety with Literal types (MANDATORY)
- BaseRequest and BaseResponse inheritance patterns (CRITICAL)
- Multi-resource architecture requirements (6 resources)
- File organization strategy: flat models, grouped resources
- Simple method naming convention with ambiguity resolution
- Class naming conflict resolution with domain prefixes
- Response model inheritance rules (ALL must inherit from BaseResponse)
- File upload handling for document APIs
- Nested path parameters (up to 5 levels deep)
- Environment variable validation for examples

## File Organization Strategy

**Models**: Use flat structure in `v1/model/` directory
- All model files are placed directly in the model directory
- No subdirectories or grouping for models
- Enables easy imports and reduces nesting complexity
- Total of 99+ model files for 33 APIs (Request, RequestBody, Response for each)

**Resources**: Use functional grouping in `v1/resource/` directory
- `dataset.py` - Dataset management operations (create, list, get, update, delete, retrieve)
- `document.py` - Document processing operations (create_by_file, create_by_text, list, get, update_by_file, update_by_text, delete, update_status, get_batch_status, file_info)
- `segment.py` - Segment operations (list, create, get, update, delete)
- `chunk.py` - Child chunk operations (list, create, update, delete)
- `tag.py` - Tag and metadata operations (list, create, update, delete, bind, unbind, get_dataset_tags)
- `model.py` - Model information operations (embedding_models)

**Method Naming**: Use simple, concise names
- Avoid redundant prefixes (e.g., `create` instead of `create_dataset` in Dataset resource)
- Use underscores only when necessary for clarity
- Async methods use `a` prefix (e.g., `acreate`, `alist`, `aget`)

**Ambiguity Resolution Rules (MANDATORY)**:
- When multiple operations in the same resource could cause naming ambiguity, use descriptive prefixes
- Update operations use `update_` prefix (e.g., `update_status` for document status updates)
- Get operations use `get_` prefix when needed for clarity (e.g., `get_batch_status` for batch indexing status)
- Maintain method names concise but unambiguous within the resource context
- Examples:
  - `update_status()` vs `get_batch_status()` - clearly different operations
  - `create_by_file()` vs `create_by_text()` - different creation methods
  - `update_by_file()` vs `update_by_text()` - different update methods

**Class Naming Conflict Resolution (MANDATORY)**:
- All classes must use domain-specific prefixes to avoid naming conflicts
- Dataset-related: `Dataset*` (e.g., `DatasetInfo`, `DatasetTag`)
- Document-related: `Document*` (e.g., `DocumentInfo`, `DocumentStatus`)
- Segment-related: `Segment*` (e.g., `SegmentInfo`, `ChildChunkInfo`)
- Tag-related: `Tag*` (e.g., `TagInfo`, `TagBinding`)
- Model-related: `Model*` (e.g., `ModelInfo`, `EmbeddingModel`)
- File-related: `File*` (e.g., `FileInfo`, `FileUpload`)

**Response Model Inheritance Rules (CRITICAL - ZERO TOLERANCE)**:
- ALL Response classes MUST inherit from BaseResponse for error handling
- NEVER inherit from pydantic.BaseModel directly
- Use multiple inheritance when needed: `class CreateDatasetResponse(DatasetInfo, BaseResponse):`

## Implementation Steps

### Step 0: Analyze Current Knowledge Implementation

**Analysis Prompt:**
```
Analyze the existing knowledge implementation to plan the implementation strategy.

Requirements:
1. Examine current structure:
   - Check if dify_oapi/api/knowledge/ exists
   - Document any existing model files and their locations
   - Identify any existing resource implementations
   - Map current API endpoints (if any)
   - Note any existing tests that need consideration
   - Assess existing V1 class structure

2. Plan implementation strategy:
   - Multi-resource architecture (dataset, document, segment, chunk, tag, model)
   - Flat model structure in v1/model/
   - 33 API endpoints across 6 resources
   - Complex nested path parameters for segments and child chunks (up to 5 levels)
   - File upload handling for document APIs with multipart/form-data
   - Strict type safety with Literal types

3. Create implementation checklist:
   - [ ] Foundation types and models (knowledge_types.py + 12 public models)
   - [ ] Dataset resource (6 APIs: create, list, get, update, delete, retrieve)
   - [ ] Document resource (10 APIs: create_by_file, create_by_text, list, get, update_by_file, update_by_text, delete, update_status, get_batch_status, file_info)
   - [ ] Segment resource (5 APIs: list, create, get, update, delete)
   - [ ] Child Chunks resource (4 APIs: list, create, update, delete)
   - [ ] Tag resource (7 APIs: list, create, update, delete, bind, unbind, get_dataset_tags)
   - [ ] Model resource (1 API: embedding_models)
   - [ ] Version integration (V1 class with 6 resources)
   - [ ] Service integration
   - [ ] Client integration
   - [ ] Examples for all 33 APIs (with environment validation)
   - [ ] Comprehensive testing (33 API test classes + public model tests)

4. Risk assessment:
   - Complex nested resource paths (up to 5 levels deep)
   - File upload multipart handling with proper content-type
   - Large number of APIs to implement (33 total)
   - Type safety across all models with Literal types
   - Child chunks management complexity
   - Class naming conflicts requiring domain prefixes
   - Response model inheritance requirements (ALL must inherit from BaseResponse)
```

**Testing Prompt:**
```
Create analysis documentation and migration plan for existing knowledge implementation.

Requirements:
1. Create `docs/knowledge/migration-analysis.md` documenting:
   - Current implementation assessment
   - Migration strategy for existing code
   - Risk mitigation plans
   - Implementation timeline
   - Resource allocation requirements

2. Verify project structure readiness:
   - Ensure dify_oapi/api/knowledge/v1/model/ directory exists
   - Ensure dify_oapi/api/knowledge/v1/resource/ directory exists
   - Check for any conflicting existing implementations
   - Document any required cleanup or migration steps

3. Create implementation tracking:
   - Implementation progress checklist
   - Quality gates for each step
   - Testing requirements for each component
   - Integration validation checkpoints
```

### Step 1: Create Knowledge Types and Base Models

**Implementation Prompt:**
```
Create the foundational types and base models for the Knowledge Base API module in dify-oapi2.

**CRITICAL: Class Naming Conflict Resolution**
All classes must use domain-specific prefixes to avoid naming conflicts:
- Dataset-related: `Dataset*` (e.g., `DatasetInfo`, `DatasetTag`)
- Document-related: `Document*` (e.g., `DocumentInfo`, `DocumentStatus`)
- Segment-related: `Segment*` (e.g., `SegmentInfo`, `ChildChunkInfo`)
- Tag-related: `Tag*` (e.g., `TagInfo`, `TagBinding`)
- Model-related: `Model*` (e.g., `ModelInfo`, `EmbeddingModel`)
- File-related: `File*` (e.g., `FileInfo`, `FileUpload`)

Requirements:
1. Create `dify_oapi/api/knowledge/v1/model/knowledge_types.py` with all Literal types:
   - IndexingTechnique = Literal["high_quality", "economy"]
   - Permission = Literal["only_me", "all_team_members", "partial_members"]
   - SearchMethod = Literal["hybrid_search", "semantic_search", "full_text_search", "keyword_search"]
   - DocumentStatus = Literal["indexing", "completed", "error", "paused"]
   - ProcessingMode = Literal["automatic", "custom"]
   - FileType = Literal["document", "image", "audio", "video", "custom"]
   - TransferMethod = Literal["remote_url", "local_file"]
   - TagType = Literal["knowledge_type", "custom"]
   - SegmentStatus = Literal["waiting", "parsing", "cleaning", "splitting", "indexing", "completed", "error", "paused"]
   - DocumentStatusAction = Literal["enable", "disable", "archive", "un_archive"]
   - DocumentForm = Literal["text_model", "hierarchical_model", "qa_model"]
   - ModelType = Literal["text-embedding"]
   - ProviderType = Literal["vendor", "external"]
   - DataSourceType = Literal["upload_file", "notion_import", "website_crawl"]
   - IndexingStatus = Literal["waiting", "parsing", "cleaning", "splitting", "indexing", "completed", "error", "paused"]

2. Create core public model classes with builder patterns:
   - `dataset_info.py`: DatasetInfo class with all dataset fields (id, name, description, provider, permission, data_source_type, indexing_technique, app_count, document_count, word_count, created_by, created_at, updated_by, updated_at, embedding_model, embedding_model_provider, embedding_available)
   - `document_info.py`: DocumentInfo class with all document fields (id, position, data_source_type, data_source_info, dataset_process_rule_id, name, created_from, created_by, created_at, tokens, indexing_status, error, enabled, disabled_at, disabled_by, archived, display_status, word_count, hit_count, doc_form)
   - `segment_info.py`: SegmentInfo class with all segment fields (id, position, document_id, content, word_count, tokens, keywords, index_node_id, index_node_hash, hit_count, enabled, disabled_at, disabled_by, status, created_by, created_at, indexing_at, completed_at, error, stopped_at)
   - `child_chunk_info.py`: ChildChunkInfo class for sub-segments (id, content, keywords, created_at)
   - `tag_info.py`: TagInfo class for tag metadata (id, name, type, binding_count)
   - `model_info.py`: ModelInfo class for embedding models (provider, label, icon_small, icon_large, status, models)
   - `file_info.py`: FileInfo class for file metadata (id, name, size, extension, mime_type, created_by, created_at)
   - `process_rule.py`: ProcessRule class for document processing configuration
   - `retrieval_model.py`: RetrievalModel class for search configuration (search_method, reranking_enable, reranking_mode, top_k, score_threshold_enabled, score_threshold, weights)
   - `embedding_model_parameters.py`: EmbeddingModelParameters class for model configuration
   - `reranking_model.py`: RerankingModel class for reranking configuration (reranking_provider_name, reranking_model_name)
   - `batch_info.py`: BatchInfo class for processing batches (id, indexing_status, processing_started_at, parsing_completed_at, cleaning_completed_at, splitting_completed_at, completed_at, paused_at, error, stopped_at, completed_segments, total_segments)
   - `pagination_info.py`: PaginationInfo class for paginated responses (has_more, limit, total, page)
   - `query_info.py`: QueryInfo class for search queries (content)
   - `retrieval_record.py`: RetrievalRecord class for search results (segment, score)
   - `segment_document_info.py`: SegmentDocumentInfo class for segment document references (id, data_source_type, name)

3. All public classes must:
   - Inherit from pydantic.BaseModel (NOT BaseResponse)
   - Include comprehensive type hints using the Literal types
   - Implement builder patterns with static builder() method
   - Include proper field validation
   - Use domain-specific prefixes to avoid naming conflicts

4. Follow the existing project structure and patterns from chat/completion modules.
```

**Testing Prompt:**
```
Create comprehensive tests for the Knowledge Base foundation models.

Requirements:
1. Create `tests/knowledge/v1/model/test_knowledge_public_models.py`
2. Test all public model classes:
   - TestDatasetInfo: builder pattern, field validation, type safety
   - TestDocumentInfo: builder pattern, field validation, type safety
   - TestSegmentInfo: builder pattern, field validation, type safety
   - TestChildChunkInfo: builder pattern, field validation, type safety
   - TestTagInfo: builder pattern, field validation, type safety
   - TestModelInfo: builder pattern, field validation, type safety
   - TestFileInfo: builder pattern, field validation, type safety
   - TestProcessRule: builder pattern, field validation, type safety
   - TestRetrievalModel: builder pattern, field validation, type safety
   - TestEmbeddingModelParameters: builder pattern, field validation
   - TestRerankingModel: builder pattern, field validation
   - TestBatchInfo: builder pattern, field validation
   - TestPaginationInfo: builder pattern, field validation
   - TestQueryInfo: builder pattern, field validation
   - TestRetrievalRecord: builder pattern, field validation
   - TestSegmentDocumentInfo: builder pattern, field validation

3. Each test class should verify:
   - Builder pattern functionality
   - Field type validation with Literal types
   - Required vs optional fields
   - Model serialization/deserialization
   - Edge cases and error handling
   - Domain-specific prefix usage

4. Use pytest framework and follow existing test patterns.
```

### Step 2: Implement Dataset Resource APIs (6 APIs)

**Implementation Prompt:**
```
Implement all Dataset Resource API models for the 6 dataset management endpoints.

**CRITICAL REQUIREMENTS:**
- ALL Response classes MUST inherit from BaseResponse (ZERO TOLERANCE)
- Use domain-specific prefixes for all classes (Dataset*)
- Implement strict type safety with Literal types
- Follow established request/response patterns

Requirements:
1. Create Dataset API Request models:
   - `create_dataset_request.py`: POST /v1/datasets
   - `list_datasets_request.py`: GET /v1/datasets (with query params: page, limit)
   - `get_dataset_request.py`: GET /v1/datasets/{dataset_id}
   - `update_dataset_request.py`: PATCH /v1/datasets/{dataset_id}
   - `delete_dataset_request.py`: DELETE /v1/datasets/{dataset_id}
   - `retrieve_from_dataset_request.py`: POST /v1/datasets/{dataset_id}/retrieve

2. Create Dataset API RequestBody models (for POST/PATCH):
   - `create_dataset_request_body.py`: Dataset creation fields
   - `update_dataset_request_body.py`: Dataset update fields (all optional)
   - `retrieve_from_dataset_request_body.py`: Search query and parameters

3. Create Dataset API Response models (ALL inherit from BaseResponse):
   - `create_dataset_response.py`: class CreateDatasetResponse(DatasetInfo, BaseResponse)
   - `list_datasets_response.py`: class ListDatasetsResponse(BaseResponse) with data array
   - `get_dataset_response.py`: class GetDatasetResponse(DatasetInfo, BaseResponse)
   - `update_dataset_response.py`: class UpdateDatasetResponse(DatasetInfo, BaseResponse)
   - `delete_dataset_response.py`: class DeleteDatasetResponse(BaseResponse) with result field
   - `retrieve_from_dataset_response.py`: class RetrieveFromDatasetResponse(BaseResponse) with query and records

4. All Request classes must:
   - Inherit from BaseRequest
   - Include proper HTTP method and URI configuration
   - Implement builder patterns with appropriate methods
   - Handle path parameters using self._request.paths["param_name"] = value
   - Handle query parameters using self._request.add_query("key", value)
   - Handle request bodies using self._request.body = request_body.model_dump()

5. All RequestBody classes must:
   - Inherit from pydantic.BaseModel
   - Use Literal types for all predefined values
   - Implement builder patterns
   - Include comprehensive field validation

6. All Response classes must:
   - Inherit from BaseResponse (MANDATORY)
   - Use multiple inheritance when including data: class XResponse(DataInfo, BaseResponse)
   - Never inherit directly from pydantic.BaseModel
```

**Testing Prompt:**
```
Create comprehensive tests for all Dataset Resource API models.

Requirements:
1. Create `tests/knowledge/v1/model/test_dataset_models.py`
2. Implement test classes for each API operation:
   - TestCreateDatasetModels: Request, RequestBody, Response tests
   - TestListDatasetsModels: Request, Response tests (no RequestBody for GET)
   - TestGetDatasetModels: Request, Response tests
   - TestUpdateDatasetModels: Request, RequestBody, Response tests
   - TestDeleteDatasetModels: Request, Response tests
   - TestRetrieveFromDatasetModels: Request, RequestBody, Response tests

3. Each test class should verify:
   - Request builder pattern and HTTP method/URI configuration
   - Path parameter handling for dataset_id
   - Query parameter handling for list operations
   - RequestBody builder pattern and field validation
   - Response inheritance from BaseResponse (CRITICAL)
   - Type safety with Literal types
   - Model serialization/deserialization
   - Edge cases and error handling

4. Specific test requirements:
   - Verify all Response classes inherit from BaseResponse
   - Test multiple inheritance patterns (DatasetInfo + BaseResponse)
   - Validate Literal type constraints
   - Test builder pattern functionality
   - Verify HTTP method and URI configuration
   - Test path and query parameter handling

5. Use pytest framework and follow existing test patterns.
```

### Step 3: Implement Document Resource APIs (10 APIs)

**Implementation Prompt:**
```
Implement all Document Resource API models for the 10 document processing endpoints.

**CRITICAL REQUIREMENTS:**
- ALL Response classes MUST inherit from BaseResponse (ZERO TOLERANCE)
- Handle multipart/form-data for file upload APIs
- Use domain-specific prefixes for all classes (Document*)
- Implement strict type safety with Literal types
- Support complex nested path parameters

Requirements:
1. Create Document API Request models:
   - `create_document_by_file_request.py`: POST /v1/datasets/{dataset_id}/document/create-by-file (multipart)
   - `create_document_by_text_request.py`: POST /v1/datasets/{dataset_id}/document/create-by-text
   - `list_documents_request.py`: GET /v1/datasets/{dataset_id}/documents (with query params)
   - `get_document_request.py`: GET /v1/datasets/{dataset_id}/documents/{document_id}
   - `update_document_by_file_request.py`: POST /v1/datasets/{dataset_id}/documents/{document_id}/update-by-file (multipart)
   - `update_document_by_text_request.py`: POST /v1/datasets/{dataset_id}/documents/{document_id}/update-by-text
   - `delete_document_request.py`: DELETE /v1/datasets/{dataset_id}/documents/{document_id}
   - `update_document_status_request.py`: PATCH /v1/datasets/{dataset_id}/documents/status/{action}
   - `get_batch_indexing_status_request.py`: GET /v1/datasets/{dataset_id}/documents/{batch}/indexing-status
   - `get_upload_file_info_request.py`: GET /v1/datasets/{dataset_id}/documents/{document_id}/upload-file

2. Create Document API RequestBody models:
   - `create_document_by_file_request_body.py`: File upload metadata
   - `create_document_by_text_request_body.py`: Text document creation
   - `update_document_by_file_request_body.py`: File update metadata
   - `update_document_by_text_request_body.py`: Text document update
   - `update_document_status_request_body.py`: Status update with document_ids array

3. Create Document API Response models (ALL inherit from BaseResponse):
   - `create_document_by_file_response.py`: Document creation with batch info
   - `create_document_by_text_response.py`: Document creation with batch info
   - `list_documents_response.py`: Paginated document list
   - `get_document_response.py`: Single document details
   - `update_document_by_file_response.py`: Updated document with batch info
   - `update_document_by_text_response.py`: Updated document with batch info
   - `delete_document_response.py`: Simple success response
   - `update_document_status_response.py`: Simple success response
   - `get_batch_indexing_status_response.py`: Batch processing status
   - `get_upload_file_info_response.py`: File information

4. Special handling for file upload APIs:
   - File upload requests must support both files and body fields
   - Use multipart/form-data content type
   - Handle file parameter with BytesIO support
   - RequestBody data should be JSON-encoded in form data

5. All models must follow established patterns with proper inheritance and type safety.
```

**Testing Prompt:**
```
Create comprehensive tests for all Document Resource API models.

Requirements:
1. Create `tests/knowledge/v1/model/test_document_models.py`
2. Implement test classes for each API operation:
   - TestCreateDocumentByFileModels: Request (with file handling), RequestBody, Response tests
   - TestCreateDocumentByTextModels: Request, RequestBody, Response tests
   - TestListDocumentsModels: Request (with query params), Response tests
   - TestGetDocumentModels: Request, Response tests
   - TestUpdateDocumentByFileModels: Request (with file handling), RequestBody, Response tests
   - TestUpdateDocumentByTextModels: Request, RequestBody, Response tests
   - TestDeleteDocumentModels: Request, Response tests
   - TestUpdateDocumentStatusModels: Request, RequestBody, Response tests
   - TestGetBatchIndexingStatusModels: Request, Response tests
   - TestGetUploadFileInfoModels: Request, Response tests

3. Each test class should verify:
   - Request builder pattern and HTTP method/URI configuration
   - Path parameter handling (dataset_id, document_id, batch, action)
   - Query parameter handling for list operations
   - File upload handling for multipart requests
   - RequestBody builder pattern and field validation
   - Response inheritance from BaseResponse (CRITICAL)
   - Type safety with Literal types
   - Complex nested path parameter handling

4. Special test requirements for file upload APIs:
   - Test file parameter handling with BytesIO
   - Verify multipart/form-data content type
   - Test JSON encoding of RequestBody data in form
   - Validate file and data field separation

5. Use pytest framework and follow existing test patterns.
```

### Step 4: Implement Segment Resource APIs (5 APIs)

**Implementation Prompt:**
```
Implement all Segment Resource API models for the 5 segment management endpoints.

**CRITICAL REQUIREMENTS:**
- ALL Response classes MUST inherit from BaseResponse (ZERO TOLERANCE)
- Handle complex nested path parameters (dataset_id, document_id, segment_id)
- Use domain-specific prefixes for all classes (Segment*)
- Implement strict type safety with Literal types

Requirements:
1. Create Segment API Request models:
   - `list_segments_request.py`: GET /v1/datasets/{dataset_id}/documents/{document_id}/segments
   - `create_segment_request.py`: POST /v1/datasets/{dataset_id}/documents/{document_id}/segments
   - `get_segment_request.py`: GET /v1/datasets/{dataset_id}/documents/{document_id}/segments/{segment_id}
   - `update_segment_request.py`: POST /v1/datasets/{dataset_id}/documents/{document_id}/segments/{segment_id}
   - `delete_segment_request.py`: DELETE /v1/datasets/{dataset_id}/documents/{document_id}/segments/{segment_id}

2. Create Segment API RequestBody models:
   - `create_segment_request_body.py`: Segments array with content, answer, keywords
   - `update_segment_request_body.py`: Single segment update with content, answer, keywords

3. Create Segment API Response models (ALL inherit from BaseResponse):
   - `list_segments_response.py`: Array of segment data
   - `create_segment_response.py`: Array of created segments
   - `get_segment_response.py`: Single segment details
   - `update_segment_response.py`: Updated segment details
   - `delete_segment_response.py`: Simple success response

4. All Request classes must handle 3-level nested paths:
   - dataset_id parameter
   - document_id parameter
   - segment_id parameter (for specific segment operations)

5. Query parameters for list_segments:
   - keyword (optional): Search keyword
   - status (optional): Filter by indexing status

6. All models must follow established patterns with proper inheritance and type safety.
```

**Testing Prompt:**
```
Create comprehensive tests for all Segment Resource API models.

Requirements:
1. Create `tests/knowledge/v1/model/test_segment_models.py`
2. Implement test classes for each API operation:
   - TestListSegmentsModels: Request (with query params), Response tests
   - TestCreateSegmentModels: Request, RequestBody, Response tests
   - TestGetSegmentModels: Request, Response tests
   - TestUpdateSegmentModels: Request, RequestBody, Response tests
   - TestDeleteSegmentModels: Request, Response tests

3. Each test class should verify:
   - Request builder pattern and HTTP method/URI configuration
   - Complex nested path parameter handling (dataset_id, document_id, segment_id)
   - Query parameter handling for list operations (keyword, status)
   - RequestBody builder pattern and field validation
   - Response inheritance from BaseResponse (CRITICAL)
   - Type safety with Literal types
   - Segments array handling in create operations

4. Special test requirements:
   - Test 3-level nested path parameter handling
   - Verify segments array structure in RequestBody
   - Test segment content, answer, and keywords fields
   - Validate status filtering with Literal types

5. Use pytest framework and follow existing test patterns.
```

### Step 5: Implement Child Chunks Resource APIs (4 APIs)

**Implementation Prompt:**
```
Implement all Child Chunks Resource API models for the 4 child chunk management endpoints.

**CRITICAL REQUIREMENTS:**
- ALL Response classes MUST inherit from BaseResponse (ZERO TOLERANCE)
- Handle complex 4-level nested path parameters (dataset_id, document_id, segment_id, child_chunk_id)
- Use domain-specific prefixes for all classes (ChildChunk* or Chunk*)
- Implement strict type safety with Literal types

Requirements:
1. Create Child Chunks API Request models:
   - `list_child_chunks_request.py`: GET /v1/datasets/{dataset_id}/documents/{document_id}/segments/{segment_id}/child_chunks
   - `create_child_chunk_request.py`: POST /v1/datasets/{dataset_id}/documents/{document_id}/segments/{segment_id}/child_chunks
   - `update_child_chunk_request.py`: PATCH /v1/datasets/{dataset_id}/documents/{document_id}/segments/{segment_id}/child_chunks/{child_chunk_id}
   - `delete_child_chunk_request.py`: DELETE /v1/datasets/{dataset_id}/documents/{document_id}/segments/{segment_id}/child_chunks/{child_chunk_id}

2. Create Child Chunks API RequestBody models:
   - `create_child_chunk_request_body.py`: Chunks array with content and keywords
   - `update_child_chunk_request_body.py`: Single chunk update with content and keywords

3. Create Child Chunks API Response models (ALL inherit from BaseResponse):
   - `list_child_chunks_response.py`: Array of child chunk data
   - `create_child_chunk_response.py`: Array of created child chunks
   - `update_child_chunk_response.py`: Updated child chunk details
   - `delete_child_chunk_response.py`: Simple success response

4. All Request classes must handle 4-level nested paths:
   - dataset_id parameter
   - document_id parameter
   - segment_id parameter
   - child_chunk_id parameter (for specific chunk operations)

5. All models must follow established patterns with proper inheritance and type safety.
```

**Testing Prompt:**
```
Create comprehensive tests for all Child Chunks Resource API models.

Requirements:
1. Create `tests/knowledge/v1/model/test_chunk_models.py`
2. Implement test classes for each API operation:
   - TestListChildChunksModels: Request, Response tests
   - TestCreateChildChunkModels: Request, RequestBody, Response tests
   - TestUpdateChildChunkModels: Request, RequestBody, Response tests
   - TestDeleteChildChunkModels: Request, Response tests

3. Each test class should verify:
   - Request builder pattern and HTTP method/URI configuration
   - Complex 4-level nested path parameter handling
   - RequestBody builder pattern and field validation
   - Response inheritance from BaseResponse (CRITICAL)
   - Type safety with Literal types
   - Chunks array handling in create operations

4. Special test requirements:
   - Test 4-level nested path parameter handling (dataset_id, document_id, segment_id, child_chunk_id)
   - Verify chunks array structure in RequestBody
   - Test chunk content and keywords fields
   - Validate PATCH method for update operations

5. Use pytest framework and follow existing test patterns.
```

### Step 6: Implement Tag Resource APIs (7 APIs)

**Implementation Prompt:**
```
Implement all Tag Resource API models for the 7 tag management endpoints.

**CRITICAL REQUIREMENTS:**
- ALL Response classes MUST inherit from BaseResponse (ZERO TOLERANCE)
- Handle both global tag operations and dataset-specific operations
- Use domain-specific prefixes for all classes (Tag*)
- Implement strict type safety with Literal types

Requirements:
1. Create Tag API Request models:
   - `list_tags_request.py`: GET /v1/datasets/tags (with query param: type)
   - `create_tag_request.py`: POST /v1/datasets/tags
   - `update_tag_request.py`: PATCH /v1/datasets/tags
   - `delete_tag_request.py`: DELETE /v1/datasets/tags
   - `bind_tags_to_dataset_request.py`: POST /v1/datasets/tags/binding
   - `unbind_tags_from_dataset_request.py`: POST /v1/datasets/tags/unbinding
   - `get_dataset_tags_request.py`: POST /v1/datasets/{dataset_id}/tags

2. Create Tag API RequestBody models:
   - `create_tag_request_body.py`: Tag creation with name and type
   - `update_tag_request_body.py`: Tag update with tag_id and name
   - `delete_tag_request_body.py`: Tag deletion with tag_id
   - `bind_tags_to_dataset_request_body.py`: Dataset binding with dataset_id and tag_ids array
   - `unbind_tags_from_dataset_request_body.py`: Dataset unbinding with dataset_id and tag_ids array

3. Create Tag API Response models (ALL inherit from BaseResponse):
   - `list_tags_response.py`: Array of tag data
   - `create_tag_response.py`: Created tag details
   - `update_tag_response.py`: Updated tag details
   - `delete_tag_response.py`: Simple success response
   - `bind_tags_to_dataset_response.py`: Simple success response
   - `unbind_tags_from_dataset_response.py`: Simple success response
   - `get_dataset_tags_response.py`: Array of dataset tags

4. Special handling requirements:
   - list_tags supports type query parameter (knowledge_type, custom)
   - update_tag, delete_tag use RequestBody instead of path parameters
   - bind/unbind operations work with tag_ids arrays
   - get_dataset_tags uses POST method with dataset_id path parameter

5. All models must follow established patterns with proper inheritance and type safety.
```

**Testing Prompt:**
```
Create comprehensive tests for all Tag Resource API models.

Requirements:
1. Create `tests/knowledge/v1/model/test_tag_models.py`
2. Implement test classes for each API operation:
   - TestListTagsModels: Request (with query params), Response tests
   - TestCreateTagModels: Request, RequestBody, Response tests
   - TestUpdateTagModels: Request, RequestBody, Response tests
   - TestDeleteTagModels: Request, RequestBody, Response tests
   - TestBindTagsToDatasetModels: Request, RequestBody, Response tests
   - TestUnbindTagsFromDatasetModels: Request, RequestBody, Response tests
   - TestGetDatasetTagsModels: Request, Response tests

3. Each test class should verify:
   - Request builder pattern and HTTP method/URI configuration
   - Query parameter handling for list operations (type filter)
   - RequestBody handling for operations using body instead of path params
   - Response inheritance from BaseResponse (CRITICAL)
   - Type safety with Literal types (TagType)
   - Array handling for tag_ids in bind/unbind operations

4. Special test requirements:
   - Test type query parameter with TagType Literal values
   - Verify RequestBody usage for update/delete instead of path parameters
   - Test tag_ids array handling in bind/unbind operations
   - Validate POST method for get_dataset_tags operation

5. Use pytest framework and follow existing test patterns.
```

### Step 7: Implement Model Resource APIs (1 API)

**Implementation Prompt:**
```
Implement the Model Resource API models for the single embedding models endpoint.

**CRITICAL REQUIREMENTS:**
- ALL Response classes MUST inherit from BaseResponse (ZERO TOLERANCE)
- Use domain-specific prefixes for all classes (Model*)
- Implement strict type safety with Literal types

Requirements:
1. Create Model API Request model:
   - `get_text_embedding_models_request.py`: GET /v1/workspaces/current/models/model-types/text-embedding

2. Create Model API Response model (inherits from BaseResponse):
   - `get_text_embedding_models_response.py`: Array of embedding model providers and models

3. The response should include:
   - Array of providers with provider info
   - Each provider contains models array
   - Model details include model name, type, features, properties
   - Support for model status and deprecation flags

4. All models must follow established patterns with proper inheritance and type safety.
```

**Testing Prompt:**
```
Create comprehensive tests for the Model Resource API models.

Requirements:
1. Create `tests/knowledge/v1/model/test_model_models.py`
2. Implement test class:
   - TestGetTextEmbeddingModelsModels: Request, Response tests

3. Test class should verify:
   - Request builder pattern and HTTP method/URI configuration
   - Response inheritance from BaseResponse (CRITICAL)
   - Type safety with model-related Literal types
   - Complex nested response structure (providers -> models)

4. Special test requirements:
   - Test complex nested response structure
   - Verify provider and model arrays
   - Test model properties and features handling
   - Validate model status and deprecation flags

5. Use pytest framework and follow existing test patterns.
```

### Step 8: Implement Resource Classes

**Implementation Prompt:**
```
Implement all 6 Knowledge Resource classes with proper method implementations.

**CRITICAL REQUIREMENTS:**
- Each resource class handles its specific domain APIs
- All methods support both sync and async operations
- Use Transport.execute and ATransport.aexecute for HTTP calls
- Follow established resource class patterns from other modules

Requirements:
1. Create `dify_oapi/api/knowledge/v1/resource/dataset.py`:
   - Dataset class with 6 methods: create, list, get, update, delete, retrieve
   - Each method has sync and async versions (acreate, alist, etc.)

2. Create `dify_oapi/api/knowledge/v1/resource/document.py`:
   - Document class with 10 methods: create_by_file, create_by_text, list, get, update_by_file, update_by_text, delete, update_status, get_batch_status, file_info
   - Each method has sync and async versions

3. Create `dify_oapi/api/knowledge/v1/resource/segment.py`:
   - Segment class with 5 methods: list, create, get, update, delete
   - Each method has sync and async versions

4. Create `dify_oapi/api/knowledge/v1/resource/chunk.py`:
   - Chunk class with 4 methods: list, create, update, delete
   - Each method has sync and async versions

5. Create `dify_oapi/api/knowledge/v1/resource/tag.py`:
   - Tag class with 7 methods: list, create, update, delete, bind, unbind, get_dataset_tags
   - Each method has sync and async versions

6. Create `dify_oapi/api/knowledge/v1/resource/model.py`:
   - Model class with 1 method: embedding_models
   - Method has sync and async versions

7. All resource classes must:
   - Accept Config in constructor
   - Use proper request/response type hints
   - Handle RequestOption parameter
   - Use Transport.execute for sync operations
   - Use ATransport.aexecute for async operations
   - Follow established error handling patterns

8. Method signatures should match:
   ```python
   def create(self, request: CreateDatasetRequest, request_option: RequestOption) -> CreateDatasetResponse:
       return Transport.execute(self.config, request, unmarshal_as=CreateDatasetResponse, option=request_option)

   async def acreate(self, request: CreateDatasetRequest, request_option: RequestOption) -> CreateDatasetResponse:
       return await ATransport.aexecute(self.config, request, unmarshal_as=CreateDatasetResponse, option=request_option)
   ```
```

**Testing Prompt:**
```
Create comprehensive tests for all Knowledge Resource classes.

Requirements:
1. Create resource test files:
   - `tests/knowledge/v1/resource/test_dataset_resource.py`
   - `tests/knowledge/v1/resource/test_document_resource.py`
   - `tests/knowledge/v1/resource/test_segment_resource.py`
   - `tests/knowledge/v1/resource/test_chunk_resource.py`
   - `tests/knowledge/v1/resource/test_tag_resource.py`
   - `tests/knowledge/v1/resource/test_model_resource.py`

2. Each test file should test:
   - Resource class initialization with Config
   - All sync method implementations
   - All async method implementations
   - Proper request/response type handling
   - Transport.execute and ATransport.aexecute usage
   - Error handling and exception propagation

3. Test patterns for each method:
   - Mock Transport.execute/ATransport.aexecute
   - Verify correct request object passed
   - Verify correct response type returned
   - Test both sync and async versions
   - Validate RequestOption handling

4. Use pytest framework with proper mocking for Transport classes.
```

### Step 9: Update Version Integration

**Implementation Prompt:**
```
Update the Knowledge V1 class to expose all 6 resource classes.

Requirements:
1. Update `dify_oapi/api/knowledge/v1/v1.py`:
   - Import all 6 resource classes
   - Initialize all resources in constructor
   - Expose as public properties

2. V1 class structure:
   ```python
   from .resource.dataset import Dataset
   from .resource.document import Document
   from .resource.segment import Segment
   from .resource.chunk import Chunk
   from .resource.tag import Tag
   from .resource.model import Model

   class V1:
       def __init__(self, config: Config):
           self.dataset = Dataset(config)
           self.document = Document(config)
           self.segment = Segment(config)
           self.chunk = Chunk(config)
           self.tag = Tag(config)
           self.model = Model(config)
   ```

3. Update `dify_oapi/api/knowledge/knowledge.py`:
   - Ensure proper V1 integration
   - Update any existing method signatures

4. Update `dify_oapi/api/knowledge/__init__.py`:
   - Export all necessary classes
   - Maintain backward compatibility if needed

5. Follow established patterns from other API modules.
```

**Testing Prompt:**
```
Create tests for Knowledge version integration.

Requirements:
1. Create `tests/knowledge/v1/test_version_integration.py`
2. Test V1 class:
   - Proper initialization with Config
   - All 6 resources are accessible
   - Resource instances are correctly typed
   - Config is properly passed to all resources

3. Test Knowledge service integration:
   - Proper V1 integration
   - Backward compatibility (if applicable)
   - Import/export functionality

4. Use pytest framework and follow existing test patterns.
```

### Step 10: Create Examples for All 33 APIs

**Implementation Prompt:**
```
Create comprehensive examples for all 33 Knowledge Base APIs.

**CRITICAL REQUIREMENTS:**
- ALL examples must validate required environment variables and raise ValueError if missing
- ALL resource names must use "[Example]" prefix for safety
- Write MINIMAL code - only what's absolutely necessary to demonstrate each API
- Each file must contain both sync and async examples
- Follow established example patterns from other modules

Requirements:
1. Create example directory structure:
   ```
   examples/knowledge/
   ├── dataset/
   │   ├── create_dataset.py
   │   ├── list_datasets.py
   │   ├── get_dataset.py
   │   ├── update_dataset.py
   │   ├── delete_dataset.py
   │   └── retrieve_from_dataset.py
   ├── document/
   │   ├── create_document_by_file.py
   │   ├── create_document_by_text.py
   │   ├── list_documents.py
   │   ├── get_document.py
   │   ├── update_document_by_file.py
   │   ├── update_document_by_text.py
   │   ├── delete_document.py
   │   ├── update_document_status.py
   │   ├── get_batch_indexing_status.py
   │   └── get_upload_file_info.py
   ├── segment/
   │   ├── list_segments.py
   │   ├── create_segment.py
   │   ├── get_segment.py
   │   ├── update_segment.py
   │   └── delete_segment.py
   ├── chunk/
   │   ├── list_child_chunks.py
   │   ├── create_child_chunk.py
   │   ├── update_child_chunk.py
   │   └── delete_child_chunk.py
   ├── tag/
   │   ├── list_tags.py
   │   ├── create_tag.py
   │   ├── update_tag.py
   │   ├── delete_tag.py
   │   ├── bind_tags_to_dataset.py
   │   ├── unbind_tags_from_dataset.py
   │   └── get_dataset_tags.py
   ├── model/
   │   └── get_text_embedding_models.py
   └── README.md
   ```

2. Each example file must:
   - Validate environment variables at start of each function
   - Use "[Example]" prefix for all created resources
   - Include both sync and async functions
   - Handle basic error cases
   - Use minimal code approach
   - Include proper imports and setup

3. Environment variable validation pattern:
   ```python
   def validate_environment():
       api_key = os.getenv("API_KEY")
       if not api_key:
           raise ValueError("API_KEY environment variable is required")
       return api_key
   ```

4. Resource naming safety pattern:
   - All created resources: "[Example] Dataset Name"
   - All delete operations: verify "[Example]" prefix before deletion

5. Update `examples/knowledge/README.md` with:
   - Complete API coverage (33 APIs)
   - Correct API counts per resource
   - Usage instructions
   - Environment variable requirements
```

**Testing Prompt:**
```
Create validation tests for all Knowledge examples.

Requirements:
1. Create `tests/knowledge/v1/integration/test_examples_validation.py`
2. Test all 33 example files:
   - Verify files exist and are executable
   - Test environment variable validation
   - Verify "[Example]" prefix usage
   - Test both sync and async functions
   - Validate proper imports and setup

3. Test categories:
   - Dataset examples (6 files)
   - Document examples (10 files)
   - Segment examples (5 files)
   - Chunk examples (4 files)
   - Tag examples (7 files)
   - Model examples (1 file)

4. Validation requirements:
   - All functions validate required environment variables
   - All resource creation uses "[Example]" prefix
   - All delete operations check for "[Example]" prefix
   - Both sync and async versions exist and work

5. Use pytest framework and mock environment variables for testing.
```

### Step 11: Integration Testing

**Implementation Prompt:**
```
Create comprehensive integration tests for all Knowledge Base APIs.

Requirements:
1. Create `tests/knowledge/v1/integration/test_knowledge_api_integration.py`
2. Test all 33 APIs with proper mocking:
   - Mock HTTP responses for all endpoints
   - Test request/response serialization
   - Verify proper error handling
   - Test both sync and async operations

3. Integration test structure:
   - TestDatasetIntegration (6 API tests)
   - TestDocumentIntegration (10 API tests)
   - TestSegmentIntegration (5 API tests)
   - TestChunkIntegration (4 API tests)
   - TestTagIntegration (7 API tests)
   - TestModelIntegration (1 API test)

4. Each test should:
   - Mock HTTP client responses
   - Test complete request/response cycle
   - Verify proper model serialization/deserialization
   - Test error scenarios
   - Validate type safety

5. Use pytest framework with httpx mocking for HTTP calls.
```

**Testing Prompt:**
```
Create comprehensive integration validation tests.

Requirements:
1. Create `tests/knowledge/v1/integration/test_comprehensive_integration.py`
2. Test complete Knowledge module integration:
   - Client -> Service -> V1 -> Resources -> Models flow
   - All 33 APIs end-to-end testing
   - Cross-resource dependencies (e.g., dataset -> document -> segment)
   - Error propagation through all layers

3. Test scenarios:
   - Complete workflow: create dataset -> add document -> create segments -> manage chunks
   - Tag management across multiple datasets
   - Model selection and usage
   - Batch operations and status checking

4. Validation requirements:
   - All Response classes inherit from BaseResponse
   - All Request classes inherit from BaseRequest
   - Proper type safety throughout the chain
   - Error handling at all levels

5. Use pytest framework with comprehensive mocking.
```

### Step 12: Final Validation and Documentation

**Implementation Prompt:**
```
Perform final validation and create comprehensive documentation.

Requirements:
1. Validate complete implementation:
   - All 33 APIs implemented and tested
   - All 6 resources properly integrated
   - All models follow established patterns
   - Type safety throughout the module
   - Examples for all APIs

2. Create documentation:
   - Update `docs/knowledge/apis.md` with complete API documentation
   - Create `docs/knowledge/examples.md` with usage examples
   - Update main README.md with Knowledge module information

3. Validation checklist:
   - [ ] 33 API models implemented (Request, RequestBody, Response)
   - [ ] 6 resource classes implemented
   - [ ] V1 integration complete
   - [ ] All Response classes inherit from BaseResponse
   - [ ] All examples include environment validation
   - [ ] All tests pass
   - [ ] Type safety verified
   - [ ] Documentation complete

4. Performance validation:
   - Test with realistic data sizes
   - Verify memory usage patterns
   - Test concurrent operations
   - Validate error handling under load

5. Create migration guide if updating existing implementation.
```

**Testing Prompt:**
```
Create final validation test suite.

Requirements:
1. Create `tests/knowledge/v1/test_final_validation.py`
2. Comprehensive validation tests:
   - All 33 APIs are accessible through client
   - All Response classes inherit from BaseResponse
   - All Request classes inherit from BaseRequest
   - Type safety validation across all models
   - Builder pattern functionality for all models

3. Integration validation:
   - Client integration works properly
   - All resources are accessible through V1
   - Error handling works at all levels
   - Examples run without errors (with mocked environment)

4. Documentation validation:
   - All APIs documented
   - Examples match implementation
   - README information is accurate
   - Migration guide is complete (if applicable)

5. Create test report summarizing:
   - Total APIs implemented: 33
   - Total resources: 6
   - Total model files: 99+
   - Test coverage percentage
   - Performance benchmarks
```

## Summary

This comprehensive implementation plan provides step-by-step prompts for implementing all 33 Knowledge Base APIs across 6 specialized resources. Each step includes both implementation and testing prompts to ensure code quality and functionality.

### Key Implementation Features:
- **Complete API Coverage**: All 33 knowledge APIs implemented
- **Multi-Resource Architecture**: 6 specialized resource classes
- **Strict Type Safety**: Literal types for all predefined values
- **File Upload Support**: Multipart/form-data handling for document APIs
- **Complex Path Parameters**: Support for up to 5-level nested paths
- **Comprehensive Testing**: Tests for all models, resources, and integrations
- **Safety-First Examples**: Environment validation and "[Example]" prefix usage
- **Minimal Code Approach**: Only essential code in all implementations

### Quality Assurance:
- **Zero Tolerance Rules**: All Response classes MUST inherit from BaseResponse
- **Domain Prefixes**: All classes use domain-specific prefixes to avoid conflicts
- **Builder Patterns**: All models implement builder patterns for consistency
- **Environment Validation**: All examples validate required environment variables
- **Comprehensive Testing**: 33 API test classes plus integration and validation tests

This plan ensures a robust, type-safe, and maintainable implementation of the complete Knowledge Base API module for dify-oapi2.

## Critical Implementation Checklist

**Before starting implementation, verify:**
- [ ] All 33 APIs are correctly mapped (6+10+5+4+7+1=33)
- [ ] All Literal types are properly defined in knowledge_types.py
- [ ] All Response classes inherit from BaseResponse (ZERO TOLERANCE)
- [ ] All public classes use domain-specific prefixes (Dataset*, Document*, Segment*, Tag*, Model*, File*)
- [ ] File upload APIs use multipart/form-data handling
- [ ] Complex nested path parameters are handled (up to 5 levels)
- [ ] Environment variable validation in all examples
- [ ] "[Example]" prefix safety in all examples
- [ ] All 6 resources are properly integrated in V1 class
- [ ] Comprehensive test coverage for all 33 APIs

**API Count Verification:**
- Dataset Resource: 6 APIs (create, list, get, update, delete, retrieve)
- Document Resource: 10 APIs (create_by_file, create_by_text, list, get, update_by_file, update_by_text, delete, update_status, get_batch_status, file_info)
- Segment Resource: 5 APIs (list, create, get, update, delete)
- Child Chunks Resource: 4 APIs (list, create, update, delete)
- Tag Resource: 7 APIs (list, create, update, delete, bind, unbind, get_dataset_tags)
- Model Resource: 1 API (embedding_models)
- **Total: 33 APIs**

**File Count Verification:**
- Request files: 33 (one per API)
- RequestBody files: ~20 (for POST/PATCH APIs)
- Response files: 33 (one per API)
- Public model files: ~16 (DatasetInfo, DocumentInfo, etc.)
- **Total model files: ~102**

**Resource Integration Verification:**
- V1 class must expose: dataset, document, segment, chunk, tag, model
- Each resource must implement all its methods with sync/async versions
- All methods must use proper Transport.execute patterns

**Testing Verification:**
- Model tests: 7 files (dataset, document, segment, chunk, tag, model, public models)
- Resource tests: 6 files (one per resource)
- Integration tests: 4 files (api integration, comprehensive, examples validation, version integration)
- **Total test files: 17**

**Examples Verification:**
- Example files: 33 (one per API)
- Directory structure: 6 resource directories + README
- All examples must validate environment variables
- All examples must use "[Example]" prefix for safety
