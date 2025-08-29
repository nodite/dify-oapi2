# Knowledge Base API Implementation Plan

This document provides step-by-step prompts for implementing the complete Knowledge Base API module in dify-oapi2. Each implementation step is followed by a corresponding test step to ensure code quality and functionality.

## Overview

The Knowledge Base API module implements 33 APIs across 5 specialized resources:
- **Dataset Resource**: 6 APIs for dataset management
- **Document Resource**: 10 APIs for document processing
- **Segment Resource**: 8 APIs for content segmentation
- **Tag Resource**: 7 APIs for metadata and tagging
- **Model Resource**: 1 API for embedding models

## Prerequisites

Before starting, ensure you understand:
- The existing dify-oapi2 project structure
- Current knowledge implementation structure (if any)
- Pydantic models and builder patterns
- HTTP request/response handling
- Type safety with Literal types
- BaseRequest and BaseResponse inheritance patterns
- Multi-resource architecture requirements
- File organization strategy: flat models, grouped resources
- Simple method naming convention

## File Organization Strategy

**Models**: Use flat structure in `v1/model/` directory
- All model files are placed directly in the model directory
- No subdirectories or grouping for models
- Enables easy imports and reduces nesting complexity

**Resources**: Use functional grouping in `v1/resource/` directory
- `dataset.py` - Dataset management operations (create, list, get, update, delete, retrieve, tags)
- `document.py` - Document processing operations (create_by_file, create_by_text, list, get, update_by_file, update_by_text, delete, status, batch_status, file_info)
- `segment.py` - Segment and chunk operations (list, create, get, update, delete, list_chunks, create_chunk, update_chunk, delete_chunk)
- `tag.py` - Tag and metadata operations (list, create, update, delete, bind, unbind)
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

2. Plan implementation strategy:
   - Multi-resource architecture (dataset, document, segment, tag, model)
   - Flat model structure in v1/model/
   - 33 API endpoints across 5 resources
   - Complex nested path parameters for segments and child chunks
   - File upload handling for document APIs

3. Create implementation checklist:
   - [ ] Foundation types and models
   - [ ] Dataset resource (8 APIs)
   - [ ] Document resource (12 APIs) 
   - [ ] Segment resource (8 APIs)
   - [ ] Tag resource (6 APIs)
   - [ ] Model resource (1 API)
   - [ ] Version integration
   - [ ] Service integration
   - [ ] Client integration
   - [ ] Examples for all 39 APIs
   - [ ] Comprehensive testing

4. Risk assessment:
   - Complex nested resource paths
   - File upload multipart handling
   - Large number of APIs to implement
   - Type safety across all models
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
   - Permission = Literal["only_me", "all_team_members"]
   - SearchMethod = Literal["semantic_search", "full_text_search", "hybrid_search"]
   - DocumentStatus = Literal["indexing", "completed", "error", "paused"]
   - ProcessingMode = Literal["automatic", "custom"]
   - FileType = Literal["document", "image", "audio", "video", "custom"]
   - TransferMethod = Literal["remote_url", "local_file"]
   - TagType = Literal["knowledge_type", "custom"]
   - SegmentStatus = Literal["waiting", "indexing", "completed", "error", "paused"]
   - ModelType = Literal["text-embedding"]
   - ProviderType = Literal["system", "custom"]
   - DataSourceType = Literal["upload_file", "notion_import", "website_crawl"]

2. Create core public model classes with builder patterns:
   - `dataset_info.py`: DatasetInfo class with all dataset fields
   - `document_info.py`: DocumentInfo class with all document fields
   - `segment_info.py`: SegmentInfo class with all segment fields
   - `child_chunk_info.py`: ChildChunkInfo class for sub-segments
   - `tag_info.py`: TagInfo class for tag metadata
   - `model_info.py`: ModelInfo class for embedding models
   - `file_info.py`: FileInfo class for file metadata
   - `process_rule.py`: ProcessRule class for document processing
   - `retrieval_model.py`: RetrievalModel class for search configuration
   - `embedding_model_parameters.py`: EmbeddingModelParameters class
   - `reranking_model.py`: RerankingModel class
   - `batch_info.py`: BatchInfo class for processing batches
   - `pagination_info.py`: PaginationInfo class for paginated responses

3. All public classes must:
   - Inherit from pydantic.BaseModel
   - Include comprehensive type hints using the Literal types
   - Implement builder patterns with static builder() method
   - Include proper field validation

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

3. Each test class should verify:
   - Builder pattern functionality
   - Field type validation with Literal types
   - Required vs optional fields
   - Model serialization/deserialization
   - Edge cases and error handling

4. Use pytest framework and follow existing test patterns.
```

### Step 2A: Implement Create Dataset API Models

**Implementation Prompt:**
```
Implement the Create Dataset API request, request body, and response models.

Requirements:
1. Create `create_dataset_request.py`:
   - Inherit from BaseRequest
   - POST method to /v1/datasets
   - Include request_body attribute
   - Builder pattern with request_body() method

2. Create `create_dataset_request_body.py`:
   - Inherit from pydantic.BaseModel
   - Fields: name (str, required), description (str), indexing_technique (IndexingTechnique, required), permission (Permission, required), provider (str), model (str), embedding_model_parameters (EmbeddingModelParameters), retrieval_model (RetrievalModel)
   - Builder pattern with all field methods

3. Create `create_dataset_response.py`:
   - Inherit from DatasetInfo and BaseResponse (MANDATORY)
   - Multiple inheritance pattern for data + error handling
   - No builder pattern for response classes

4. All models must use proper type hints and Literal types from knowledge_types.py
```

**Testing Prompt:**
```
Create tests for Create Dataset API models.

Requirements:
1. Add TestCreateDatasetModels class to `test_dataset_models.py`
2. Test methods:
   - test_request_builder: Verify builder pattern and URI/method setup
   - test_request_validation: Validate request structure
   - test_request_body_builder: Test all builder methods
   - test_request_body_validation: Validate field types and constraints
   - test_response_inheritance: Verify BaseResponse inheritance
   - test_response_data_access: Test response data access patterns

3. Verify proper type safety with Literal types
4. Test required vs optional field validation
```

### Step 2B: Implement List Datasets API Models

**Implementation Prompt:**
```
Implement the List Datasets API models.

Requirements:
1. Create `list_datasets_request.py`:
   - Inherit from BaseRequest
   - GET method to /v1/datasets
   - Query parameters: page, limit
   - Builder with page() and limit() methods using add_query()

2. Create `list_datasets_response.py`:
   - Inherit from BaseResponse (MANDATORY)
   - Fields: data (List[DatasetInfo]), has_more (bool), limit (int), total (int), page (int)
   - Include pagination information

3. Follow established patterns for GET requests with query parameters
```

**Testing Prompt:**
```
Create tests for List Datasets API models.

Requirements:
1. Add TestListDatasetsModels class to `test_dataset_models.py`
2. Test methods:
   - test_request_builder: Verify builder pattern setup
   - test_request_query_parameters: Test query parameter handling
   - test_response_inheritance: Verify BaseResponse inheritance
   - test_response_pagination: Test pagination fields

3. Test query parameter assignment and URI construction
4. Verify proper handling of optional query parameters
```

### Step 2C: Implement Get Dataset API Models

**Implementation Prompt:**
```
Implement the Get Dataset API models.

Requirements:
1. Create `get_dataset_request.py`:
   - Inherit from BaseRequest
   - GET method to /v1/datasets/:dataset_id
   - Path parameter: dataset_id
   - Builder with dataset_id() method using paths["dataset_id"]

2. Create `get_dataset_response.py`:
   - Inherit from DatasetInfo and BaseResponse (MANDATORY)
   - Multiple inheritance pattern for data + error handling

3. Follow established patterns for GET requests with path parameters
```

**Testing Prompt:**
```
Create tests for Get Dataset API models.

Requirements:
1. Add TestGetDatasetModels class to `test_dataset_models.py`
2. Test methods:
   - test_request_builder: Verify builder pattern setup
   - test_request_path_parameters: Test path parameter handling
   - test_response_inheritance: Verify BaseResponse inheritance

3. Test path parameter assignment and URI construction
4. Verify proper UUID validation for dataset_id
```

### Step 2D: Implement Update Dataset API Models

**Implementation Prompt:**
```
Implement the Update Dataset API models.

Requirements:
1. Create `update_dataset_request.py`:
   - Inherit from BaseRequest
   - PATCH method to /v1/datasets/:dataset_id
   - Path parameter: dataset_id
   - Include request_body attribute

2. Create `update_dataset_request_body.py`:
   - Inherit from pydantic.BaseModel
   - Same fields as CreateDatasetRequestBody (all optional for updates)
   - Builder pattern with all field methods

3. Create `update_dataset_response.py`:
   - Inherit from DatasetInfo and BaseResponse (MANDATORY)

4. Follow established patterns for PATCH requests
```

**Testing Prompt:**
```
Create tests for Update Dataset API models.

Requirements:
1. Add TestUpdateDatasetModels class to `test_dataset_models.py`
2. Test methods:
   - test_request_builder: Verify builder pattern and path parameter handling
   - test_request_body_builder: Test request body builder
   - test_response_inheritance: Verify BaseResponse inheritance

3. Validate path parameter and request body integration
4. Test optional field handling in updates
```

### Step 2E: Implement Delete Dataset API Models

**Implementation Prompt:**
```
Implement the Delete Dataset API models.

Requirements:
1. Create `delete_dataset_request.py`:
   - Inherit from BaseRequest
   - DELETE method to /v1/datasets/:dataset_id
   - Path parameter: dataset_id
   - No request body needed

2. Create `delete_dataset_response.py`:
   - Inherit from BaseResponse (MANDATORY)
   - Field: result (str) - "success"

3. Follow established patterns for DELETE requests
```

**Testing Prompt:**
```
Create tests for Delete Dataset API models.

Requirements:
1. Add TestDeleteDatasetModels class to `test_dataset_models.py`
2. Test methods:
   - test_request_builder: Verify builder pattern setup
   - test_response_inheritance: Verify BaseResponse inheritance
   - test_response_success_result: Test "success" result

3. Test path parameter handling
4. Verify proper DELETE method configuration
```

### Step 2F: Implement Retrieve from Dataset API Models

**Implementation Prompt:**
```
Implement the Retrieve from Dataset API models.

Requirements:
1. Create `retrieve_from_dataset_request.py`:
   - Inherit from BaseRequest
   - POST method to /v1/datasets/:dataset_id/retrieve
   - Path parameter: dataset_id
   - Include request_body attribute

2. Create `retrieve_from_dataset_request_body.py`:
   - Inherit from pydantic.BaseModel
   - Fields: query (str, required), retrieval_model (RetrievalModel), top_k (int), score_threshold (float)
   - Builder pattern with all field methods

3. Create `retrieve_from_dataset_response.py`:
   - Inherit from BaseResponse (MANDATORY)
   - Fields: query (str), records (List[RetrievalRecord])

4. Create `retrieval_record.py`:
   - Public model for search results
   - Fields: segment (SegmentInfo), score (float)
   - Builder pattern required
```

**Testing Prompt:**
```
Create tests for Retrieve from Dataset API models.

Requirements:
1. Add TestRetrieveFromDatasetModels class to `test_dataset_models.py`
2. Test methods:
   - test_request_builder: Verify builder pattern and path parameter handling
   - test_request_body_builder: Test search query and parameters
   - test_response_inheritance: Verify BaseResponse inheritance
   - test_response_search_results: Test search result structure

3. Add TestRetrievalRecord class to `test_knowledge_public_models.py`
4. Test search parameter validation and result formatting
```

### Step 2G: Implement Get Dataset Tags API Models

**Implementation Prompt:**
```
Implement the Get Dataset Tags API models.

Requirements:
1. Create `get_dataset_tags_request.py`:
   - Inherit from BaseRequest
   - POST method to /v1/datasets/:dataset_id/tags
   - Path parameter: dataset_id
   - No request body needed (simple POST)

2. Create `get_dataset_tags_response.py`:
   - Inherit from BaseResponse (MANDATORY)
   - Fields: data (List[TagInfo])

3. Follow established patterns for POST requests without body
```

**Testing Prompt:**
```
Create tests for Get Dataset Tags API models.

Requirements:
1. Add TestGetDatasetTagsModels class to `test_dataset_models.py`
2. Test methods:
   - test_request_builder: Verify builder pattern setup
   - test_response_inheritance: Verify BaseResponse inheritance
   - test_response_tags_list: Test tags array structure

3. Test path parameter handling
4. Verify proper POST method without body
```

### Step 2H: Implement Complete Dataset API Models Integration

**Implementation Prompt:**
```
Complete the Dataset API models implementation and integration.

Requirements:
1. Ensure all 6 dataset API models are properly integrated
2. Keep __init__.py files minimal and clean
3. Verify all imports work correctly
4. Test cross-model dependencies (DatasetInfo, TagInfo, etc.)
5. Validate URI patterns and HTTP methods

6. Create comprehensive dataset model integration:
   - All request classes properly inherit from BaseRequest
   - All response classes properly inherit from BaseResponse
   - All request body classes have builder patterns
   - All public classes have builder patterns
   - Proper type safety with Literal types throughout
```

**Testing Prompt:**
```
Create comprehensive integration tests for all Dataset API models.

Requirements:
1. Complete `tests/knowledge/v1/model/test_dataset_models.py`
2. Ensure all 7 test classes are implemented (TestCreateDatasetModels through TestGetDatasetTagsModels)
3. Test model integration:
   - Cross-model dependencies work correctly
   - Import statements are correct
   - Type safety is maintained
   - Builder patterns work consistently

4. Run all dataset model tests and ensure 100% pass rate
5. Verify test coverage for all dataset models
```

### Step 2: Implement Dataset API Models (8 APIs)

**Implementation Prompt:**
```
Implement all Dataset API request and response models for the Knowledge Base module.

Requirements:
1. Create request models for all 8 dataset APIs with detailed specifications:
   - `create_dataset_request.py` + `create_dataset_request_body.py`
     * POST /v1/datasets
     * Fields: name (required), description, indexing_technique (required), permission (required), provider, model, embedding_model_parameters, retrieval_model
   - `list_datasets_request.py` (GET with query params)
     * GET /v1/datasets
     * Query params: page (default 1), limit (default 20)
   - `get_dataset_request.py` (GET with path params)
     * GET /v1/datasets/:dataset_id
     * Path param: dataset_id (UUID)
   - `update_dataset_request.py` + `update_dataset_request_body.py`
     * PATCH /v1/datasets/:dataset_id
     * Same fields as create (all optional for updates)
   - `delete_dataset_request.py` (DELETE with path params)
     * DELETE /v1/datasets/:dataset_id
     * Path param: dataset_id (UUID)
   - `retrieve_from_dataset_request.py` + `retrieve_from_dataset_request_body.py`
     * POST /v1/datasets/:dataset_id/retrieve
     * Fields: query (required), retrieval_model, top_k, score_threshold
   - `get_dataset_tags_request.py` (POST with path params)
     * POST /v1/datasets/:dataset_id/tags
     * Path param: dataset_id (UUID)

2. Create response models for all dataset APIs:
   - `create_dataset_response.py`: Inherit from DatasetInfo + BaseResponse
   - `list_datasets_response.py`: Include data array + pagination
   - `get_dataset_response.py`: Inherit from DatasetInfo + BaseResponse
   - `update_dataset_response.py`: Inherit from DatasetInfo + BaseResponse
   - `delete_dataset_response.py`: Simple result response
   - `retrieve_from_dataset_response.py`: Include query + records array
   - `get_dataset_tags_response.py`: Include tags array

3. All models must:
   - Follow exact naming conventions (file name = class name)
   - Request classes inherit from BaseRequest
   - Response classes inherit from BaseResponse
   - Use proper HTTP methods and URIs
   - Include comprehensive builder patterns
   - Use strict typing with Literal types
   - Handle path/query parameters correctly

4. Follow the URI patterns:
   - POST /v1/datasets → CreateDatasetRequest
   - GET /v1/datasets → ListDatasetsRequest
   - GET /v1/datasets/:dataset_id → GetDatasetRequest
   - PATCH /v1/datasets/:dataset_id → UpdateDatasetRequest
   - DELETE /v1/datasets/:dataset_id → DeleteDatasetRequest
   - POST /v1/datasets/:dataset_id/retrieve → RetrieveFromDatasetRequest
   - POST /v1/datasets/:dataset_id/tags → GetDatasetTagsRequest
```

**Testing Prompt:**
```
Create comprehensive tests for all Dataset API models.

Requirements:
1. Create `tests/knowledge/v1/model/test_dataset_models.py`
2. Implement test classes for each API:
   - TestCreateDatasetModels: request, request_body, response tests
   - TestListDatasetsModels: request, response tests
   - TestGetDatasetModels: request, response tests
   - TestUpdateDatasetModels: request, request_body, response tests
   - TestDeleteDatasetModels: request, response tests
   - TestRetrieveFromDatasetModels: request, request_body, response tests
   - TestGetDatasetTagsModels: request, response tests

3. Each test class should verify:
   - Request builder functionality and validation
   - RequestBody builder functionality (where applicable)
   - Response inheritance from BaseResponse
   - Path parameter handling
   - Query parameter handling
   - HTTP method and URI configuration
   - Type safety with Literal types
   - Error handling and edge cases

4. Test both positive and negative scenarios.
5. Ensure all response classes properly inherit from BaseResponse.
```

### Step 3: Implement Dataset Resource Class

**Implementation Prompt:**
```
Implement the Dataset resource class with all 8 dataset management APIs.

Requirements:
1. Create `dify_oapi/api/knowledge/v1/resource/dataset.py`
2. Implement Dataset class with methods:
   - create(request: CreateDatasetRequest, request_option: RequestOption) -> CreateDatasetResponse
   - acreate(request: CreateDatasetRequest, request_option: RequestOption) -> CreateDatasetResponse
   - list(request: ListDatasetsRequest, request_option: RequestOption) -> ListDatasetsResponse
   - alist(request: ListDatasetsRequest, request_option: RequestOption) -> ListDatasetsResponse
   - get(request: GetDatasetRequest, request_option: RequestOption) -> GetDatasetResponse
   - aget(request: GetDatasetRequest, request_option: RequestOption) -> GetDatasetResponse
   - update(request: UpdateDatasetRequest, request_option: RequestOption) -> UpdateDatasetResponse
   - aupdate(request: UpdateDatasetRequest, request_option: RequestOption) -> UpdateDatasetResponse
   - delete(request: DeleteDatasetRequest, request_option: RequestOption) -> DeleteDatasetResponse
   - adelete(request: DeleteDatasetRequest, request_option: RequestOption) -> DeleteDatasetResponse
   - retrieve(request: RetrieveFromDatasetRequest, request_option: RequestOption) -> RetrieveFromDatasetResponse
   - aretrieve(request: RetrieveFromDatasetRequest, request_option: RequestOption) -> RetrieveFromDatasetResponse
   - tags(request: GetDatasetTagsRequest, request_option: RequestOption) -> GetDatasetTagsResponse
   - atags(request: GetDatasetTagsRequest, request_option: RequestOption) -> GetDatasetTagsResponse

3. Use Transport.execute() for sync and ATransport.aexecute() for async
4. Follow existing resource patterns from chat/completion modules
5. Include proper error handling and type hints
6. Each method should accept proper request and request_option parameters
```

**Implementation Prompt:**
```
Implement the Dataset resource class with all 8 dataset management APIs.

Requirements:
1. Create `dify_oapi/api/knowledge/v1/resource/dataset.py`
2. Implement Dataset class with methods:
   - create(request, request_option) -> CreateDatasetResponse
   - acreate(request, request_option) -> CreateDatasetResponse
   - list(request, request_option) -> ListDatasetsResponse
   - alist(request, request_option) -> ListDatasetsResponse
   - get(request, request_option) -> GetDatasetResponse
   - aget(request, request_option) -> GetDatasetResponse
   - update(request, request_option) -> UpdateDatasetResponse
   - aupdate(request, request_option) -> UpdateDatasetResponse
   - delete(request, request_option) -> DeleteDatasetResponse
   - adelete(request, request_option) -> DeleteDatasetResponse
   - retrieve(request, request_option) -> RetrieveFromDatasetResponse
   - aretrieve(request, request_option) -> RetrieveFromDatasetResponse
   - tags(request, request_option) -> GetDatasetTagsResponse
   - atags(request, request_option) -> GetDatasetTagsResponse

3. Use Transport.execute() for sync and ATransport.aexecute() for async
4. Follow existing resource patterns from chat/completion modules
5. Include proper error handling and type hints
6. Each method should accept proper request and request_option parameters
```

**Testing Prompt:**
```
Create comprehensive tests for the Dataset resource class.

Requirements:
1. Create `tests/knowledge/v1/resource/test_dataset_resource.py`
2. Test all dataset resource methods:
   - Test sync and async versions of each method
   - Mock Transport.execute() and ATransport.aexecute()
   - Verify correct request/response handling
   - Test error scenarios and exception handling
   - Validate proper parameter passing

3. Use pytest-asyncio for async tests
4. Mock external dependencies appropriately
5. Test both successful responses and error conditions
6. Ensure proper type checking and validation
```

### Step 4A: Implement Create Document by File API Models

**Implementation Prompt:**
```
Implement the Create Document by File API models with multipart/form-data support.

Requirements:
1. Create `create_document_by_file_request.py`:
   - Inherit from BaseRequest
   - POST method to /v1/datasets/:dataset_id/document/create-by-file
   - Path parameter: dataset_id
   - Special handling for multipart/form-data
   - Fields: file (BytesIO), request_body
   - Builder methods: dataset_id(), file(), and request_body()
   - Set files and body attributes for multipart handling

2. Create `create_document_by_file_request_body.py`:
   - Inherit from pydantic.BaseModel
   - Fields: name (str), indexing_technique (IndexingTechnique), process_rule (ProcessRule)
   - Builder pattern with all field methods

3. Create `create_document_by_file_response.py`:
   - Inherit from BaseResponse (MANDATORY)
   - Fields: document (DocumentInfo), batch (str)

4. Follow multipart/form-data pattern from design document
```

**Testing Prompt:**
```
Create tests for Create Document by File API models.

Requirements:
1. Add TestCreateDocumentByFileModels class to `test_document_models.py`
2. Test methods:
   - test_request_builder: Verify multipart handling
   - test_request_file_handling: Test file upload mechanics
   - test_request_body_builder: Test request body builder
   - test_response_inheritance: Verify BaseResponse inheritance

3. Mock BytesIO objects for file testing
4. Validate multipart/form-data structure
5. Test file name handling and metadata extraction
```

### Step 4B: Implement Create Document by Text API Models

**Implementation Prompt:**
```
Implement the Create Document by Text API models.

Requirements:
1. Create `create_document_by_text_request.py`:
   - Inherit from BaseRequest
   - POST method to /v1/datasets/:dataset_id/document/create-by-text
   - Path parameter: dataset_id
   - Include request_body attribute

2. Create `create_document_by_text_request_body.py`:
   - Inherit from pydantic.BaseModel
   - Fields: name (str, required), text (str, required), indexing_technique (IndexingTechnique, required), process_rule (ProcessRule)
   - Builder pattern with all field methods

3. Create `create_document_by_text_response.py`:
   - Inherit from BaseResponse (MANDATORY)
   - Fields: document (DocumentInfo), batch (str)

4. Follow established patterns for POST requests with request body
```

**Testing Prompt:**
```
Create tests for Create Document by Text API models.

Requirements:
1. Add TestCreateDocumentByTextModels class to `test_document_models.py`
2. Test methods:
   - test_request_builder: Verify builder pattern setup
   - test_request_body_builder: Test text content handling
   - test_response_inheritance: Verify BaseResponse inheritance

3. Test text content validation and processing rules
4. Verify proper path parameter and request body integration
```

### Step 4C: Implement List Documents API Models

**Implementation Prompt:**
```
Implement the List Documents API models.

Requirements:
1. Create `list_documents_request.py`:
   - Inherit from BaseRequest
   - GET method to /v1/datasets/:dataset_id/documents
   - Path parameter: dataset_id
   - Query parameters: keyword, page, limit
   - Builder with all parameter methods

2. Create `list_documents_response.py`:
   - Inherit from BaseResponse (MANDATORY)
   - Fields: data (List[DocumentInfo]), has_more (bool), limit (int), total (int), page (int)

3. Follow established patterns for GET requests with pagination
```

**Testing Prompt:**
```
Create tests for List Documents API models.

Requirements:
1. Add TestListDocumentsModels class to `test_document_models.py`
2. Test methods:
   - test_request_builder: Verify builder pattern and parameters
   - test_request_query_parameters: Test query parameter handling
   - test_response_inheritance: Verify BaseResponse inheritance
   - test_response_pagination: Test pagination structure

3. Test keyword search parameter handling
4. Verify proper nested resource path construction
```

### Step 4D: Implement Get Document API Models

**Implementation Prompt:**
```
Implement the Get Document API models.

Requirements:
1. Create `get_document_request.py`:
   - Inherit from BaseRequest
   - GET method to /v1/datasets/:dataset_id/documents/:document_id
   - Path parameters: dataset_id, document_id
   - Builder with dataset_id() and document_id() methods

2. Create `get_document_response.py`:
   - Inherit from DocumentInfo and BaseResponse (MANDATORY)
   - Multiple inheritance pattern for data + error handling

3. Follow established patterns for GET requests with multiple path parameters
```

**Testing Prompt:**
```
Create tests for Get Document API models.

Requirements:
1. Add TestGetDocumentModels class to `test_document_models.py`
2. Test methods:
   - test_request_builder: Verify builder pattern setup
   - test_request_path_parameters: Test multiple path parameter handling
   - test_response_inheritance: Verify BaseResponse inheritance

3. Test nested resource path construction with multiple UUIDs
4. Verify proper parameter validation
```

### Step 4E: Implement Update Document APIs Models

**Implementation Prompt:**
```
Implement the Update Document by File and by Text API models.

Requirements:
1. Create `update_document_by_file_request.py` + `update_document_by_file_request_body.py`:
   - Similar to create-by-file but with document_id path parameter
   - POST method to /v1/datasets/:dataset_id/documents/:document_id/update-by-file
   - Path parameters: dataset_id, document_id
   - Multipart handling for file uploads

2. Create `update_document_by_text_request.py` + `update_document_by_text_request_body.py`:
   - Similar to create-by-text but with document_id path parameter
   - POST method to /v1/datasets/:dataset_id/documents/:document_id/update-by-text
   - Path parameters: dataset_id, document_id

3. Create corresponding response models inheriting from BaseResponse

4. Follow established update patterns with additional path parameters
```

**Testing Prompt:**
```
Create tests for Update Document API models.

Requirements:
1. Add TestUpdateDocumentByFileModels and TestUpdateDocumentByTextModels classes
2. Test methods for each:
   - test_request_builder: Verify builder pattern with multiple path params
   - test_request_body_builder: Test request body handling
   - test_response_inheritance: Verify BaseResponse inheritance

3. Test file upload handling for update-by-file
4. Test text content handling for update-by-text
5. Verify proper nested resource path construction
```

### Step 4F: Implement Delete Document and File Info API Models

**Implementation Prompt:**
```
Implement the Delete Document and Get Upload File Info API models.

Requirements:
1. Create `delete_document_request.py`:
   - Inherit from BaseRequest
   - DELETE method to /v1/datasets/:dataset_id/documents/:document_id
   - Path parameters: dataset_id, document_id
   - No request body needed

2. Create `delete_document_response.py`:
   - Inherit from BaseResponse (MANDATORY)
   - Field: result (str) - "success"

3. Create `get_upload_file_info_request.py`:
   - Inherit from BaseRequest
   - GET method to /v1/datasets/:dataset_id/documents/:document_id/upload-file
   - Path parameters: dataset_id, document_id

4. Create `get_upload_file_info_response.py`:
   - Inherit from FileInfo and BaseResponse (MANDATORY)
   - File metadata information

5. Follow established patterns for DELETE and GET requests
```

**Testing Prompt:**
```
Create tests for Delete Document and File Info API models.

Requirements:
1. Add TestDeleteDocumentModels and TestGetUploadFileInfoModels classes
2. Test methods for each:
   - test_request_builder: Verify builder pattern setup
   - test_response_inheritance: Verify BaseResponse inheritance

3. Test DELETE method configuration and success response
4. Test file info response structure and metadata
5. Verify proper nested resource path handling
```

### Step 4G: Implement Document Status and Batch APIs Models

**Implementation Prompt:**
```
Implement the Document Status Management and Batch Indexing Status API models.

Requirements:
1. Create `update_document_status_request.py` + `update_document_status_request_body.py`:
   - PATCH method to /v1/datasets/:dataset_id/documents/status/:action
   - Path parameters: dataset_id, action ("enable" | "disable")
   - Fields: document_ids (List[str])

2. Create `update_document_status_response.py`:
   - Inherit from BaseResponse (MANDATORY)
   - Field: result (str) - "success"

3. Create `get_batch_indexing_status_request.py`:
   - GET method to /v1/datasets/:dataset_id/documents/:batch/indexing-status
   - Path parameters: dataset_id, batch

4. Create `get_batch_indexing_status_response.py`:
   - Inherit from BatchInfo and BaseResponse (MANDATORY)
   - Batch processing status information

5. Use proper Literal types for action parameter
```

**Testing Prompt:**
```
Create tests for Document Status and Batch API models.

Requirements:
1. Add TestUpdateDocumentStatusModels and TestGetBatchIndexingStatusModels classes
2. Test methods for each:
   - test_request_builder: Verify builder pattern and path parameters
   - test_request_body_builder: Test document IDs array (for status)
   - test_response_inheritance: Verify BaseResponse inheritance

3. Test action parameter validation ("enable" | "disable")
4. Test batch status response structure
5. Verify proper array handling for document_ids
```

### Step 4H: Complete Document API Models Integration

**Implementation Prompt:**
```
Complete the Document API models implementation and integration.

Requirements:
1. Ensure all 12 document API models are properly integrated
2. Update model __init__.py files to export all classes
3. Verify all imports work correctly
4. Test cross-model dependencies (DocumentInfo, FileInfo, BatchInfo, etc.)
5. Validate URI patterns and HTTP methods for all document APIs
6. Ensure proper multipart/form-data handling for file upload APIs

7. Create comprehensive document model integration:
   - All request classes properly inherit from BaseRequest
   - All response classes properly inherit from BaseResponse
   - All request body classes have builder patterns
   - Proper file upload handling for create/update-by-file APIs
   - Proper type safety with Literal types throughout
```

**Testing Prompt:**
```
Create comprehensive integration tests for all Document API models.

Requirements:
1. Complete `tests/knowledge/v1/model/test_document_models.py`
2. Ensure all 10 test classes are implemented
3. Test model integration:
   - Cross-model dependencies work correctly
   - Import statements are correct
   - Type safety is maintained
   - Builder patterns work consistently
   - File upload handling works properly

4. Run all document model tests and ensure 100% pass rate
5. Verify test coverage for all document models
6. Test multipart/form-data handling thoroughly
```

### Step 4: Implement Document API Models (12 APIs)

**Implementation Prompt:**
```
Implement all Document API request and response models for the Knowledge Base module.

Requirements:
1. Create request models for all 12 document APIs with detailed specifications:
   - `create_document_by_file_request.py` + `create_document_by_file_request_body.py`
     * POST /v1/datasets/:dataset_id/document/create-by-file
     * Multipart: file (binary) + data (JSON string)
     * Fields: name, indexing_technique, process_rule (mode, rules)
   - `create_document_by_text_request.py` + `create_document_by_text_request_body.py`
     * POST /v1/datasets/:dataset_id/document/create-by-text
     * Fields: name (required), text (required), indexing_technique (required), process_rule
   - `list_documents_request.py` (GET with query params)
     * GET /v1/datasets/:dataset_id/documents
     * Query params: keyword, page, limit
   - `get_document_request.py` (GET with path params)
     * GET /v1/datasets/:dataset_id/documents/:document_id
     * Path params: dataset_id (UUID), document_id (UUID)
   - `update_document_by_file_request.py` + `update_document_by_file_request_body.py`
     * POST /v1/datasets/:dataset_id/documents/:document_id/update-by-file
     * Same as create-by-file with document_id path param
   - `update_document_by_text_request.py` + `update_document_by_text_request_body.py`
     * POST /v1/datasets/:dataset_id/documents/:document_id/update-by-text
     * Same as create-by-text with document_id path param
   - `delete_document_request.py` (DELETE with path params)
     * DELETE /v1/datasets/:dataset_id/documents/:document_id
     * Path params: dataset_id (UUID), document_id (UUID)
   - `get_upload_file_info_request.py` (GET with path params)
     * GET /v1/datasets/:dataset_id/documents/:document_id/upload-file
     * Path params: dataset_id (UUID), document_id (UUID)
   - `update_document_status_request.py` + `update_document_status_request_body.py`
     * PATCH /v1/datasets/:dataset_id/documents/status/:action
     * Path params: dataset_id (UUID), action ("enable" | "disable")
     * Fields: document_ids (array of UUIDs)
   - `get_batch_indexing_status_request.py` (GET with path params)
     * GET /v1/datasets/:dataset_id/documents/:batch/indexing-status
     * Path params: dataset_id (UUID), batch (string)

2. Handle multipart/form-data for file upload APIs:
   - CreateDocumentByFileRequest must support file uploads
   - UpdateDocumentByFileRequest must support file uploads
   - Use proper multipart handling patterns

3. Create response models for all document APIs:
   - Include proper inheritance from BaseResponse
   - Handle document info, batch info, and file info responses
   - Include pagination for list responses

4. Follow URI patterns:
   - POST /v1/datasets/:dataset_id/document/create-by-file
   - POST /v1/datasets/:dataset_id/document/create-by-text
   - GET /v1/datasets/:dataset_id/documents
   - GET /v1/datasets/:dataset_id/documents/:document_id
   - POST /v1/datasets/:dataset_id/documents/:document_id/update-by-file
   - POST /v1/datasets/:dataset_id/documents/:document_id/update-by-text
   - DELETE /v1/datasets/:dataset_id/documents/:document_id
   - GET /v1/datasets/:dataset_id/documents/:document_id/upload-file
   - PATCH /v1/datasets/:dataset_id/documents/status/:action
   - GET /v1/datasets/:dataset_id/documents/:batch/indexing-status
```

**Testing Prompt:**
```
Create comprehensive tests for all Document API models.

Requirements:
1. Create `tests/knowledge/v1/model/test_document_models.py`
2. Implement test classes for each document API (10 test classes)
3. Special attention to file upload handling:
   - Test multipart/form-data handling
   - Test file parameter validation
   - Test RequestBody data serialization for file uploads

4. Test all request builders, request bodies, and responses
5. Verify proper path parameter handling for nested resources
6. Test query parameter handling for list operations
7. Ensure proper inheritance and type safety
```

### Step 5: Implement Document Resource Class

**Implementation Prompt:**
```
Implement the Document resource class with all 12 document management APIs.

Requirements:
1. Create `dify_oapi/api/knowledge/v1/resource/document.py`
2. Implement Document class with all methods (sync + async versions)
3. Handle file upload operations properly
4. Include proper error handling for file operations
5. Follow the same patterns as Dataset resource
6. Support all document lifecycle operations
```

**Testing Prompt:**
```
Create comprehensive tests for the Document resource class.

Requirements:
1. Create `tests/knowledge/v1/resource/test_document_resource.py`
2. Test all 12 document resource methods
3. Mock file upload operations
4. Test error handling for file operations
5. Verify proper multipart handling
```

### Step 6A: Implement List Segments API Models

**Implementation Prompt:**
```
Implement the List Segments API models with complex nested paths.

Requirements:
1. Create `list_segments_request.py`:
   - Inherit from BaseRequest
   - GET method to /v1/datasets/:dataset_id/documents/:document_id/segments
   - Path parameters: dataset_id, document_id
   - Query parameters: keyword, status ("enabled" | "disabled")
   - Builder with all parameter methods

2. Create `list_segments_response.py`:
   - Inherit from BaseResponse (MANDATORY)
   - Fields: data (List[SegmentInfo]), has_more (bool), limit (int), total (int), page (int)

3. Handle complex nested resource paths properly
4. Use SegmentStatus Literal type for status parameter
```

**Testing Prompt:**
```
Create tests for List Segments API models.

Requirements:
1. Add TestListSegmentsModels class to `test_segment_models.py`
2. Test methods:
   - test_request_builder: Verify complex path parameter handling
   - test_request_query_parameters: Test query parameter handling
   - test_response_inheritance: Verify BaseResponse inheritance

3. Test nested resource path construction (dataset -> document -> segments)
4. Verify status parameter validation with Literal types
```

### Step 6B: Implement Create Segment API Models

**Implementation Prompt:**
```
Implement the Create Segment API models.

Requirements:
1. Create `create_segment_request.py`:
   - Inherit from BaseRequest
   - POST method to /v1/datasets/:dataset_id/documents/:document_id/segments
   - Path parameters: dataset_id, document_id
   - Include request_body attribute

2. Create `create_segment_request_body.py`:
   - Inherit from pydantic.BaseModel
   - Fields: segments (List[SegmentContent])
   - Builder pattern with segments() method

3. Create `create_segment_response.py`:
   - Inherit from BaseResponse (MANDATORY)
   - Fields: data (List[SegmentInfo])

4. Create `segment_content.py`:
   - Public model for segment creation
   - Fields: content (str, required), answer (str), keywords (List[str])
   - Builder pattern required
```

**Testing Prompt:**
```
Create tests for Create Segment API models.

Requirements:
1. Add TestCreateSegmentModels class to `test_segment_models.py`
2. Test methods:
   - test_request_builder: Verify nested path parameter handling
   - test_request_body_builder: Test segments array handling
   - test_response_inheritance: Verify BaseResponse inheritance

3. Add TestSegmentContent class to `test_knowledge_public_models.py`
4. Test segment content validation and array handling
```

### Step 6C: Implement Get and Update Segment API Models

**Implementation Prompt:**
```
Implement the Get and Update Segment API models.

Requirements:
1. Create `get_segment_request.py`:
   - GET method to /v1/datasets/:dataset_id/documents/:document_id/segments/:segment_id
   - Path parameters: dataset_id, document_id, segment_id

2. Create `get_segment_response.py`:
   - Inherit from SegmentInfo and BaseResponse (MANDATORY)

3. Create `update_segment_request.py` + `update_segment_request_body.py`:
   - POST method to /v1/datasets/:dataset_id/documents/:document_id/segments/:segment_id
   - Path parameters: dataset_id, document_id, segment_id
   - Fields: segment (SegmentContent)

4. Create `update_segment_response.py`:
   - Inherit from SegmentInfo and BaseResponse (MANDATORY)

5. Handle 4-level nested resource paths properly
```

**Testing Prompt:**
```
Create tests for Get and Update Segment API models.

Requirements:
1. Add TestGetSegmentModels and TestUpdateSegmentModels classes
2. Test methods for each:
   - test_request_builder: Verify 4-level path parameter handling
   - test_request_body_builder: Test segment content (for update)
   - test_response_inheritance: Verify BaseResponse inheritance

3. Test complex nested resource path construction
4. Verify proper UUID validation for all path parameters
```

### Step 6D: Implement Delete Segment API Models

**Implementation Prompt:**
```
Implement the Delete Segment API models.

Requirements:
1. Create `delete_segment_request.py`:
   - DELETE method to /v1/datasets/:dataset_id/documents/:document_id/segments/:segment_id
   - Path parameters: dataset_id, document_id, segment_id
   - No request body needed

2. Create `delete_segment_response.py`:
   - Inherit from BaseResponse (MANDATORY)
   - Field: result (str) - "success"

3. Follow established patterns for DELETE requests with complex paths
```

**Testing Prompt:**
```
Create tests for Delete Segment API models.

Requirements:
1. Add TestDeleteSegmentModels class to `test_segment_models.py`
2. Test methods:
   - test_request_builder: Verify complex path parameter handling
   - test_response_inheritance: Verify BaseResponse inheritance

3. Test DELETE method configuration with 4-level nested path
4. Verify proper success response handling
```

### Step 6E: Implement Child Chunks API Models

**Implementation Prompt:**
```
Implement all Child Chunks API models (List, Create, Update, Delete).

Requirements:
1. Create `list_child_chunks_request.py`:
   - GET method to /v1/datasets/:dataset_id/documents/:document_id/segments/:segment_id/child_chunks
   - Path parameters: dataset_id, document_id, segment_id

2. Create `create_child_chunk_request.py` + `create_child_chunk_request_body.py`:
   - POST method to same path as list
   - Fields: chunks (List[ChildChunkContent])

3. Create `update_child_chunk_request.py` + `update_child_chunk_request_body.py`:
   - PATCH method to /v1/datasets/:dataset_id/documents/:document_id/segments/:segment_id/child_chunks/:child_chunk_id
   - Path parameters: dataset_id, document_id, segment_id, child_chunk_id
   - Fields: content (str), keywords (List[str])

4. Create `delete_child_chunk_request.py`:
   - DELETE method to same path as update
   - 5-level nested resource path

5. Create corresponding response models inheriting from BaseResponse

6. Create `child_chunk_content.py`:
   - Public model for child chunk creation
   - Fields: content (str, required), keywords (List[str])
   - Builder pattern required
```

**Testing Prompt:**
```
Create tests for all Child Chunks API models.

Requirements:
1. Add TestListChildChunksModels, TestCreateChildChunkModels, TestUpdateChildChunkModels, TestDeleteChildChunkModels classes
2. Test methods for each:
   - test_request_builder: Verify 4-5 level path parameter handling
   - test_request_body_builder: Test chunk content (for create/update)
   - test_response_inheritance: Verify BaseResponse inheritance

3. Add TestChildChunkContent class to `test_knowledge_public_models.py`
4. Test most complex nested resource paths in the system
5. Verify proper handling of 5-level nested resources
```

### Step 6F: Complete Segment API Models Integration

**Implementation Prompt:**
```
Complete the Segment API models implementation and integration.

Requirements:
1. Ensure all 8 segment API models are properly integrated
2. Update model __init__.py files to export all classes
3. Verify all imports work correctly
4. Test cross-model dependencies (SegmentInfo, ChildChunkInfo, etc.)
5. Validate complex nested URI patterns for all segment APIs
6. Ensure proper handling of 4-5 level nested resource paths

7. Create comprehensive segment model integration:
   - All request classes properly handle complex nested paths
   - All response classes properly inherit from BaseResponse
   - All request body classes have builder patterns
   - Proper type safety with Literal types throughout
   - Complex path parameter validation works correctly
```

**Testing Prompt:**
```
Create comprehensive integration tests for all Segment API models.

Requirements:
1. Complete `tests/knowledge/v1/model/test_segment_models.py`
2. Ensure all 8 test classes are implemented
3. Test model integration:
   - Complex nested path handling works correctly
   - Import statements are correct
   - Type safety is maintained
   - Builder patterns work consistently

4. Run all segment model tests and ensure 100% pass rate
5. Verify test coverage for all segment models
6. Test most complex nested resource paths thoroughly
```

### Step 6: Implement Segment API Models (8 APIs)

**Implementation Prompt:**
```
Implement all Segment API request and response models for the Knowledge Base module.

Requirements:
1. Create request models for all 8 segment APIs with complex nested paths:
   - `list_segments_request.py` (GET with path + query params)
     * GET /v1/datasets/:dataset_id/documents/:document_id/segments
     * Path params: dataset_id (UUID), document_id (UUID)
     * Query params: keyword, status ("enabled" | "disabled")
   - `create_segment_request.py` + `create_segment_request_body.py`
     * POST /v1/datasets/:dataset_id/documents/:document_id/segments
     * Fields: segments (array with content, answer, keywords)
   - `get_segment_request.py` (GET with path params)
     * GET /v1/datasets/:dataset_id/documents/:document_id/segments/:segment_id
     * Path params: dataset_id (UUID), document_id (UUID), segment_id (UUID)
   - `update_segment_request.py` + `update_segment_request_body.py`
     * POST /v1/datasets/:dataset_id/documents/:document_id/segments/:segment_id
     * Fields: segment (object with content, answer, keywords)
   - `delete_segment_request.py` (DELETE with path params)
     * DELETE /v1/datasets/:dataset_id/documents/:document_id/segments/:segment_id
     * Path params: dataset_id (UUID), document_id (UUID), segment_id (UUID)
   - `list_child_chunks_request.py` (GET with path params)
     * GET /v1/datasets/:dataset_id/documents/:document_id/segments/:segment_id/child_chunks
     * Path params: dataset_id (UUID), document_id (UUID), segment_id (UUID)
   - `create_child_chunk_request.py` + `create_child_chunk_request_body.py`
     * POST /v1/datasets/:dataset_id/documents/:document_id/segments/:segment_id/child_chunks
     * Fields: chunks (array with content, keywords)
   - `update_child_chunk_request.py` + `update_child_chunk_request_body.py`
     * PATCH /v1/datasets/:dataset_id/documents/:document_id/segments/:segment_id/child_chunks/:child_chunk_id
     * Fields: content, keywords
   - `delete_child_chunk_request.py` (DELETE with path params)
     * DELETE /v1/datasets/:dataset_id/documents/:document_id/segments/:segment_id/child_chunks/:child_chunk_id
     * Path params: dataset_id (UUID), document_id (UUID), segment_id (UUID), child_chunk_id (UUID)

2. Handle complex nested path parameters for segments and child chunks
3. Create appropriate response models with proper inheritance
4. Follow URI patterns for nested resources under documents
```

**Testing Prompt:**
```
Create comprehensive tests for all Segment API models.

Requirements:
1. Create `tests/knowledge/v1/model/test_segment_models.py`
2. Test all segment and child chunk models
3. Verify complex path parameter handling
4. Test nested resource URI construction
5. Validate segment content and metadata handling
```

### Step 7: Implement Segment Resource Class

**Implementation Prompt:**
```
Implement the Segment resource class with all 8 segment management APIs.

Requirements:
1. Create `dify_oapi/api/knowledge/v1/resource/segment.py`
2. Implement all segment and child chunk operations
3. Handle nested resource paths properly
4. Include proper error handling
5. Support both segment and child chunk operations
```

**Testing Prompt:**
```
Create comprehensive tests for the Segment resource class.

Requirements:
1. Create `tests/knowledge/v1/resource/test_segment_resource.py`
2. Test all segment resource methods
3. Verify nested resource handling
4. Test error scenarios for segment operations
```

### Step 8A: Implement List and Create Tag API Models

**Implementation Prompt:**
```
Implement the List and Create Tag API models.

Requirements:
1. Create `list_tags_request.py`:
   - Inherit from BaseRequest
   - GET method to /v1/datasets/tags
   - Query parameter: type ("knowledge_type" | "custom")
   - Builder with type() method using add_query()

2. Create `list_tags_response.py`:
   - Inherit from BaseResponse (MANDATORY)
   - Fields: data (List[TagInfo])

3. Create `create_tag_request.py` + `create_tag_request_body.py`:
   - POST method to /v1/datasets/tags
   - Fields: name (str, required), type (TagType, required)
   - Builder pattern with all field methods

4. Create `create_tag_response.py`:
   - Inherit from TagInfo and BaseResponse (MANDATORY)

5. Use TagType Literal for type field validation
```

**Testing Prompt:**
```
Create tests for List and Create Tag API models.

Requirements:
1. Add TestListTagsModels and TestCreateTagModels classes to `test_tag_models.py`
2. Test methods for each:
   - test_request_builder: Verify builder pattern setup
   - test_request_query_parameters: Test type filtering (for list)
   - test_request_body_builder: Test tag creation fields (for create)
   - test_response_inheritance: Verify BaseResponse inheritance

3. Test TagType Literal validation
4. Verify proper tag type filtering and creation
```

### Step 8B: Implement Update and Delete Tag API Models

**Implementation Prompt:**
```
Implement the Update and Delete Tag API models.

Requirements:
1. Create `update_tag_request.py` + `update_tag_request_body.py`:
   - PATCH method to /v1/datasets/tags
   - Fields: tag_id (str, required), name (str, required)
   - Builder pattern with all field methods

2. Create `update_tag_response.py`:
   - Inherit from TagInfo and BaseResponse (MANDATORY)

3. Create `delete_tag_request.py` + `delete_tag_request_body.py`:
   - DELETE method to /v1/datasets/tags
   - Fields: tag_id (str, required)
   - Builder pattern with tag_id() method

4. Create `delete_tag_response.py`:
   - Inherit from BaseResponse (MANDATORY)
   - Field: result (str) - "success"

5. Note: These APIs use request bodies even for DELETE (unusual pattern)
```

**Testing Prompt:**
```
Create tests for Update and Delete Tag API models.

Requirements:
1. Add TestUpdateTagModels and TestDeleteTagModels classes
2. Test methods for each:
   - test_request_builder: Verify builder pattern setup
   - test_request_body_builder: Test tag_id and name fields
   - test_response_inheritance: Verify BaseResponse inheritance

3. Test unusual DELETE with request body pattern
4. Verify proper tag_id validation and handling
```

### Step 8C: Implement Tag Binding API Models

**Implementation Prompt:**
```
Implement the Tag Binding and Unbinding API models.

Requirements:
1. Create `bind_tags_to_dataset_request.py` + `bind_tags_to_dataset_request_body.py`:
   - POST method to /v1/datasets/tags/binding
   - Fields: dataset_id (str, required), tag_ids (List[str], required)
   - Builder pattern with all field methods

2. Create `bind_tags_to_dataset_response.py`:
   - Inherit from BaseResponse (MANDATORY)
   - Field: result (str) - "success"

3. Create `unbind_tags_from_dataset_request.py` + `unbind_tags_from_dataset_request_body.py`:
   - POST method to /v1/datasets/tags/unbinding
   - Same fields as binding
   - Builder pattern with all field methods

4. Create `unbind_tags_from_dataset_response.py`:
   - Inherit from BaseResponse (MANDATORY)
   - Field: result (str) - "success"

5. Handle tag binding/unbinding operations with array parameters
```

**Testing Prompt:**
```
Create tests for Tag Binding API models.

Requirements:
1. Add TestBindTagsToDatasetModels and TestUnbindTagsFromDatasetModels classes
2. Test methods for each:
   - test_request_builder: Verify builder pattern setup
   - test_request_body_builder: Test dataset_id and tag_ids array
   - test_response_inheritance: Verify BaseResponse inheritance

3. Test array parameter handling for tag_ids
4. Verify proper binding/unbinding operation structure
5. Test UUID validation for dataset_id and tag_ids
```

### Step 8D: Complete Tag API Models Integration

**Implementation Prompt:**
```
Complete the Tag API models implementation and integration.

Requirements:
1. Ensure all 6 tag API models are properly integrated
2. Update model __init__.py files to export all classes
3. Verify all imports work correctly
4. Test cross-model dependencies (TagInfo, etc.)
5. Validate URI patterns and HTTP methods for all tag APIs
6. Ensure proper tag binding/unbinding functionality

7. Create comprehensive tag model integration:
   - All request classes properly inherit from BaseRequest
   - All response classes properly inherit from BaseResponse
   - All request body classes have builder patterns
   - Proper type safety with TagType Literal throughout
   - Tag binding operations work correctly
```

**Testing Prompt:**
```
Create comprehensive integration tests for all Tag API models.

Requirements:
1. Complete `tests/knowledge/v1/model/test_tag_models.py`
2. Ensure all 6 test classes are implemented
3. Test model integration:
   - Cross-model dependencies work correctly
   - Import statements are correct
   - Type safety is maintained
   - Builder patterns work consistently
   - Tag binding operations work properly

4. Run all tag model tests and ensure 100% pass rate
5. Verify test coverage for all tag models
6. Test tag binding/unbinding functionality thoroughly
```

### Step 8: Implement Tag API Models (6 APIs)

**Implementation Prompt:**
```
Implement all Tag API request and response models for the Knowledge Base module.

Requirements:
1. Create request models for all 6 tag APIs with binding operations:
   - `list_tags_request.py` (GET with query params)
     * GET /v1/datasets/tags
     * Query params: type ("knowledge_type" | "custom")
   - `create_tag_request.py` + `create_tag_request_body.py`
     * POST /v1/datasets/tags
     * Fields: name (required), type (required - "knowledge_type" | "custom")
   - `update_tag_request.py` + `update_tag_request_body.py`
     * PATCH /v1/datasets/tags
     * Fields: tag_id (required), name (required)
   - `delete_tag_request.py` + `delete_tag_request_body.py`
     * DELETE /v1/datasets/tags
     * Fields: tag_id (required)
   - `bind_tags_to_dataset_request.py` + `bind_tags_to_dataset_request_body.py`
     * POST /v1/datasets/tags/binding
     * Fields: dataset_id (required), tag_ids (required array)
   - `unbind_tags_from_dataset_request.py` + `unbind_tags_from_dataset_request_body.py`
     * POST /v1/datasets/tags/unbinding
     * Fields: dataset_id (required), tag_ids (required array)

2. Handle tag binding/unbinding operations
3. Create appropriate response models
4. Support tag type filtering and management
```

**Testing Prompt:**
```
Create comprehensive tests for all Tag API models.

Requirements:
1. Create `tests/knowledge/v1/model/test_tag_models.py`
2. Test all tag management models
3. Verify tag binding/unbinding operations
4. Test tag type validation
5. Validate tag metadata handling
```

### Step 9: Implement Tag Resource Class

**Implementation Prompt:**
```
Implement the Tag resource class with all 6 tag management APIs.

Requirements:
1. Create `dify_oapi/api/knowledge/v1/resource/tag.py`
2. Implement all tag operations including binding/unbinding
3. Handle tag type validation
4. Include proper error handling
```

**Testing Prompt:**
```
Create comprehensive tests for the Tag resource class.

Requirements:
1. Create `tests/knowledge/v1/resource/test_tag_resource.py`
2. Test all tag resource methods
3. Verify tag binding/unbinding operations
4. Test tag type filtering and validation
```

### Step 10: Implement Model API Models (1 API)

**Implementation Prompt:**
```
Implement the Model API request and response models for the Knowledge Base module.

Requirements:
1. Create request model:
   - `get_text_embedding_models_request.py` (GET request)
     * GET /v1/workspaces/current/models/model-types/text-embedding
     * No parameters required

2. Create response model:
   - `get_text_embedding_models_response.py` (with model list)
     * Fields: data (array of models with model_name, model_type, provider, credentials, load_balancing)

3. Handle embedding model information and provider details
4. Follow URI pattern: GET /v1/workspaces/current/models/model-types/text-embedding
```

**Testing Prompt:**
```
Create comprehensive tests for the Model API models.

Requirements:
1. Create `tests/knowledge/v1/model/test_model_models.py`
2. Test model request and response handling
3. Verify embedding model information structure
4. Test provider information validation
```

### Step 11: Implement Model Resource Class

**Implementation Prompt:**
```
Implement the Model resource class with the embedding models API.

Requirements:
1. Create `dify_oapi/api/knowledge/v1/resource/model.py`
2. Implement get_text_embedding_models method (sync + async)
3. Handle model information properly
4. Include proper error handling
```

**Testing Prompt:**
```
Create comprehensive tests for the Model resource class.

Requirements:
1. Create `tests/knowledge/v1/resource/test_model_resource.py`
2. Test model resource methods
3. Verify model information handling
4. Test error scenarios
```

### Step 12: Implement Version Integration

**Implementation Prompt:**
```
Implement the Knowledge V1 version class that integrates all resources.

Requirements:
1. Create `dify_oapi/api/knowledge/v1/version.py`
2. Implement V1 class with all 5 resources:
   - self.dataset = Dataset(config)
   - self.document = Document(config)
   - self.segment = Segment(config)
   - self.tag = Tag(config)
   - self.model = Model(config)

3. Follow existing patterns from chat/completion modules
4. Include proper initialization and configuration
5. Ensure all resources are properly exposed
```

**Testing Prompt:**
```
Create comprehensive tests for the Knowledge V1 version integration.

Requirements:
1. Create `tests/knowledge/v1/test_version_integration.py`
2. Test V1 class initialization
3. Verify all resources are properly accessible
4. Test configuration passing to resources
5. Validate resource method accessibility
```

### Step 13: Implement Service Integration

**Implementation Prompt:**
```
Implement the Knowledge service class that provides access to API versions.

Requirements:
1. Create `dify_oapi/api/knowledge/service.py`
2. Implement Knowledge service class with v1 property
3. Follow existing patterns from other API services
4. Include proper initialization and version management
```

**Testing Prompt:**
```
Create tests for the Knowledge service class.

Requirements:
1. Create `tests/knowledge/test_service_integration.py`
2. Test service initialization
3. Verify v1 version accessibility
4. Test configuration propagation
```

### Step 14: Implement Client Integration

**Implementation Prompt:**
```
Integrate the Knowledge API service into the main dify-oapi client.

Requirements:
1. Update `dify_oapi/client.py` to include knowledge service
2. Add self.knowledge = Knowledge(self.config) to Client class
3. Ensure proper initialization order
4. Follow existing patterns for other API services
5. Update any necessary imports and exports
```

**Testing Prompt:**
```
Create comprehensive tests for Knowledge API client integration.

Requirements:
1. Create `tests/knowledge/test_client_integration.py`
2. Test client initialization with knowledge service
3. Verify knowledge API accessibility through client
4. Test end-to-end API access patterns
5. Validate configuration propagation through all layers
```

### Step 15: Create Dataset Examples

**Implementation Prompt:**
```
Create comprehensive examples for all Dataset APIs.

Requirements:
1. Create examples in `examples/knowledge/dataset/`:
   - create_dataset.py: Sync and async examples
   - list_datasets.py: Sync and async examples
   - get_dataset.py: Sync and async examples
   - update_dataset.py: Sync and async examples
   - delete_dataset.py: Sync and async examples (with [Example] prefix safety)
   - retrieve_from_dataset.py: Sync and async examples

2. All examples must:
   - Use "[Example]" prefix for safety
   - Validate environment variables (API_KEY)
   - Include minimal code with essential functionality
   - Demonstrate both sync and async usage
   - Include proper error handling
   - Use realistic test data

3. Fix examples documentation inconsistencies:
   - Verify all 6 dataset APIs have example files
   - Remove any duplicate or redundant files
   - Standardize file naming conventions
```

**Testing Prompt:**
```
Create tests to validate all Dataset examples.

Requirements:
1. Create `tests/knowledge/v1/integration/test_dataset_examples.py`
2. Test all dataset examples for:
   - Syntax validation
   - Import correctness
   - Environment variable handling
   - Safety prefix usage
   - Error handling coverage

3. Mock external API calls
4. Verify example completeness and accuracy
5. Ensure all 6 dataset APIs are covered
```

### Step 16: Create Document Examples

**Implementation Prompt:**
```
Create comprehensive examples for all Document APIs.

Requirements:
1. Create examples in `examples/knowledge/document/`:
   - create_document_by_file.py: File upload examples
   - create_document_by_text.py: Text document examples
   - list_documents.py: Document listing examples
   - get_document.py: Document retrieval examples
   - update_document_by_file.py: File update examples
   - update_document_by_text.py: Text update examples
   - delete_document.py: Document deletion examples
   - update_document_status.py: Status management examples
   - get_batch_indexing_status.py: Processing status examples
   - get_upload_file_info.py: File info examples
   - [2 additional document APIs]: Add missing examples to reach 12 total

2. Include file handling examples with proper multipart handling
3. Follow same safety and quality standards as dataset examples
4. Fix documentation inconsistencies:
   - Ensure all 12 document APIs have example files (not 10)
   - Remove any metadata/ examples that should be part of document APIs
   - Verify no duplicate functionality between document/ and metadata/ directories
```

**Testing Prompt:**
```
Create tests to validate all Document examples.

Requirements:
1. Create `tests/knowledge/v1/integration/test_document_examples.py`
2. Test all document examples including file handling
3. Mock file operations and multipart uploads
4. Verify safety measures and error handling
5. Ensure all 12 document APIs are covered (not 10)
6. Validate no conflicts with metadata examples
```

### Step 17: Create Segment, Tag, and Model Examples

**Implementation Prompt:**
```
Create comprehensive examples for Segment, Tag, and Model APIs.

Requirements:
1. Create examples in `examples/knowledge/segment/`:
   - All 8 segment API examples (list, create, get, update, delete segments and child chunks)
   - Add segment management section to examples/knowledge/README.md

2. Create examples in `examples/knowledge/tag/`:
   - All 7 tag API examples (list, create, update, delete, bind, unbind, get_dataset_tags)
   - Verify tag API count matches knowledge-api.md specification

3. Create examples in `examples/knowledge/model/`:
   - get_text_embedding_models.py example
   - Add model management section to examples/knowledge/README.md

4. Follow same patterns and safety standards
5. Include comprehensive sync/async coverage
6. Fix documentation inconsistencies:
   - Update examples/knowledge/README.md to include all missing sections
   - Correct total API count from 29 to 33
   - Ensure all resource categories are properly documented
7. Fix test structure inconsistencies:
   - Add missing Model API tests
   - Clarify metadata vs document test separation
   - Ensure all 33 APIs have corresponding tests
```

**Testing Prompt:**
```
Create tests to validate all remaining examples (Segment, Tag, Model).

Requirements:
1. Create corresponding test files for each example category
2. Validate all examples for correctness and safety
3. Ensure comprehensive coverage of all 33 APIs (not 29)
4. Verify examples/knowledge/README.md accuracy
5. Test that all documented APIs have corresponding example files
6. Verify all 33 APIs have corresponding test files
7. Ensure test structure matches final API specifications
```

### Step 18: Create Comprehensive Integration Tests

**Implementation Prompt:**
```
Create comprehensive integration tests for the entire Knowledge Base API module.

Requirements:
1. Create `tests/knowledge/v1/integration/test_knowledge_api_integration.py`
2. Test complete API workflows:
   - Dataset creation → Document upload → Segment management → Content retrieval
   - Tag management and binding workflows
   - Model information retrieval
   - Error handling across all APIs

3. Test both sync and async operations
4. Mock external API calls appropriately
5. Verify end-to-end functionality
6. Test error propagation and handling
7. Fix test structure inconsistencies:
   - Add missing Model API integration tests
   - Clarify metadata vs document test coverage
   - Ensure all 33 APIs are covered (not 29)
```

**Testing Prompt:**
```
Create final validation tests for the complete Knowledge Base implementation.

Requirements:
1. Create `tests/knowledge/v1/integration/test_comprehensive_integration.py`
2. Validate complete module integration:
   - All 33 APIs are accessible (not 39)
   - All resources are properly integrated
   - Client integration works correctly
   - Examples are functional
   - Type safety is maintained throughout

3. Performance and reliability testing
4. Edge case and error scenario testing
5. Compatibility testing with existing modules
6. Verify test structure consistency:
   - All 33 APIs have corresponding tests
   - Test structure matches final resource organization
   - No duplicate or missing test coverage
```

### Step 19: Resolve Class Naming Conflicts

**Implementation Prompt:**
```
Resolve all class naming conflicts by ensuring domain-specific prefixes.

Requirements:
1. Verify all classes use proper prefixes:
   - Dataset classes: `Dataset*` (DatasetInfo, DatasetTag, etc.)
   - Document classes: `Document*` (DocumentInfo, DocumentStatus, etc.)
   - Segment classes: `Segment*` (SegmentInfo, ChildChunkInfo, etc.)
   - Tag classes: `Tag*` (TagInfo, TagBinding, etc.)
   - Model classes: `Model*` (ModelInfo, EmbeddingModel, etc.)
   - File classes: `File*` (FileInfo, FileUpload, etc.)

2. Update all import statements and references:
   - Update model files that import renamed classes
   - Update test files to use correct class names
   - Update request/response models that reference classes

3. Ensure consistency:
   - No naming conflicts remain in the module
   - All tests pass with class names
   - All imports work correctly

4. Validate across all 39 APIs:
   - Check all request/response models
   - Verify all public model classes
   - Ensure proper inheritance patterns
```

**Testing Prompt:**
```
Update all tests to use the correct class names and verify no conflicts.

Requirements:
1. Update test imports to use correct class names
2. Update test class names to match model names
3. Update all test method references
4. Ensure all tests pass with correct names
5. Verify no import errors or naming conflicts

Validation:
- All existing tests must pass
- No naming conflicts in test files
- Consistent use of prefixed names throughout
- All 39 APIs properly tested
```

### Step 20: Update Documentation

**Implementation Prompt:**
```
Update project documentation to include the Knowledge Base API module.

Requirements:
1. Update `examples/README.md` to include knowledge base examples
2. Fix `examples/knowledge/README.md` with comprehensive usage guide:
   - Correct total API count from 29 to 33
   - Add missing Segment Management section (8 APIs)
   - Add missing Model Management section (1 API)
   - Correct Document Management to 12 APIs
   - Remove or clarify Metadata Management section
3. Update main project README.md to highlight knowledge base capabilities
4. Ensure all documentation is consistent and accurate
5. Include usage examples and best practices
6. Verify all 33 APIs are properly documented with examples
```

**Testing Prompt:**
```
Validate all documentation for accuracy and completeness.

Requirements:
1. Test all code examples in documentation
2. Verify API coverage is complete (33 APIs, not 29)
3. Check for consistency across all documentation
4. Validate example code syntax and functionality
5. Ensure examples/knowledge/README.md matches knowledge-api.md specifications
6. Verify all documented APIs have corresponding example files
```

### Step 21: Final Quality Assurance and Validation

**Implementation Prompt:**
```
Perform comprehensive final quality assurance for the Knowledge Base API implementation.

Requirements:
1. Complete test suite validation:
   - Run all unit tests and ensure 100% pass rate
   - Run all integration tests and verify functionality
   - Run all example validation tests
   - Verify test coverage meets project standards (>95%)
   - Ensure all 33 APIs have corresponding tests

2. Code quality validation:
   - Run linting tools (ruff) and ensure compliance
   - Run type checking (mypy) and resolve all issues
   - Run security scanning and address vulnerabilities
   - Verify code formatting and style consistency

3. Functionality validation:
   - Test all 33 APIs end-to-end (not 39)
   - Verify all 5 resources work correctly
   - Test complex nested resource paths
   - Validate file upload and multipart handling
   - Test search and retrieval functionality

4. Integration validation:
   - Test client integration with all APIs
   - Verify service and version integration
   - Test compatibility with existing modules
   - Validate configuration propagation

5. Performance validation:
   - Test API response times
   - Verify memory usage is acceptable
   - Test concurrent operation handling
   - Validate resource cleanup

6. Documentation validation:
   - Verify all examples work correctly
   - Test all code snippets in documentation
   - Validate API coverage is complete (33 APIs)
   - Check documentation accuracy and completeness
   - Verify test structure consistency

7. Final deliverables checklist:
   - [ ] 33 fully implemented and tested APIs (not 39)
   - [ ] 5 resource classes with comprehensive functionality
   - [ ] Complete integration with dify-oapi2 client
   - [ ] Comprehensive examples for all APIs
   - [ ] Full test coverage with unit, integration, and example tests
   - [ ] Updated documentation and usage guides
   - [ ] Performance benchmarks and optimization guide
   - [ ] Security validation and compliance report
   - [ ] Test structure consistency validation
```

### Step 22: Performance and Load Testing

**Implementation Prompt:**
```
Perform performance and load testing for the Knowledge Base API implementation.

Requirements:
1. Create performance test suite:
   - Test API response times under normal load
   - Test concurrent request handling
   - Test large file upload performance
   - Test complex nested resource path performance
   - Test search and retrieval performance

2. Load testing scenarios:
   - Multiple simultaneous dataset operations
   - Concurrent document uploads
   - High-frequency segment operations
   - Bulk tag binding/unbinding operations
   - Search query performance under load

3. Memory and resource usage testing:
   - Monitor memory usage during large operations
   - Test garbage collection efficiency
   - Validate resource cleanup after operations
   - Test connection pooling efficiency

4. Create performance benchmarks and optimization recommendations
```

**Testing Prompt:**
```
Validate performance test results and create optimization plan.

Requirements:
1. Analyze performance test results
2. Identify bottlenecks and optimization opportunities
3. Create performance improvement recommendations
4. Validate that performance meets project requirements
5. Document performance characteristics and limitations
```

### Step 23: Security and Validation Testing

**Implementation Prompt:**
```
Perform comprehensive security and validation testing.

Requirements:
1. Security testing:
   - Validate API key handling and security
   - Test input validation and sanitization
   - Verify proper error message handling (no sensitive data leakage)
   - Test file upload security (file type validation, size limits)
   - Validate UUID parameter security

2. Input validation testing:
   - Test all Literal type constraints
   - Validate required field enforcement
   - Test boundary conditions for all parameters
   - Verify proper handling of malformed requests
   - Test SQL injection prevention (if applicable)

3. Authorization and access control:
   - Verify proper API key validation
   - Test resource access permissions
   - Validate cross-resource access controls

4. Create security test report and recommendations
```

**Testing Prompt:**
```
Validate security test results and ensure compliance.

Requirements:
1. Review all security test results
2. Verify no security vulnerabilities exist
3. Ensure proper input validation throughout
4. Validate error handling doesn't leak sensitive information
5. Create security compliance report
```

### Step 24: Backward Compatibility and Migration Testing

**Implementation Prompt:**
```
Test backward compatibility and create migration guides.

Requirements:
1. Backward compatibility testing:
   - Verify existing API patterns still work
   - Test integration with existing modules (chat, completion, workflow)
   - Validate client integration doesn't break existing functionality
   - Test import path compatibility

2. Migration testing:
   - Test upgrade scenarios from previous versions
   - Validate configuration migration
   - Test data structure compatibility
   - Verify no breaking changes in public APIs

3. Create migration documentation:
   - Document any breaking changes
   - Provide upgrade instructions
   - Create compatibility matrix
   - Document deprecated features (if any)

4. Version compatibility validation
```

**Testing Prompt:**
```
Validate backward compatibility and migration procedures.

Requirements:
1. Test all migration scenarios
2. Verify backward compatibility claims
3. Validate migration documentation accuracy
4. Test rollback procedures
5. Ensure smooth upgrade path for users
```

## Success Criteria

The implementation is considered complete and successful when:

### Functionality Criteria
1. **Complete API Coverage**: All 39 knowledge base APIs are fully implemented and functional
2. **Resource Integration**: All 5 resources (dataset, document, segment, tag, model) work correctly
3. **Complex Path Handling**: Nested resource paths (up to 5 levels) work properly
4. **File Upload Support**: Multipart/form-data handling works for document APIs
5. **Search Functionality**: Content retrieval and search operations work correctly

### Quality Criteria
6. **Type Safety**: Complete type safety with Literal types and proper inheritance throughout
7. **Testing Coverage**: Comprehensive test coverage (>95%) with all tests passing
8. **Error Handling**: Robust error handling with proper BaseResponse inheritance
9. **Builder Patterns**: Consistent builder patterns implemented for all models
10. **Code Quality**: Code passes all linting, type checking, and quality gates

### Integration Criteria
11. **Client Integration**: Seamless integration with existing dify-oapi2 client
12. **Service Integration**: Proper service and version integration
13. **Module Compatibility**: No conflicts with existing modules (chat, completion, workflow)
14. **Import Structure**: Clean import structure with flat model organization
15. **Configuration**: Proper configuration propagation through all layers

### Documentation and Examples Criteria
16. **Complete Examples**: Working examples for all 39 APIs with proper safety measures
17. **Documentation**: Complete and accurate documentation including usage guides
18. **Safety Measures**: All examples use "[Example]" prefix for resource safety
19. **Code Minimalism**: Examples follow minimal code principles while maintaining functionality
20. **Environment Validation**: All examples validate required environment variables

### Performance and Security Criteria
21. **Performance**: API performance meets project requirements and expectations
22. **Security**: No security vulnerabilities, proper input validation throughout
23. **Resource Management**: Efficient resource usage and proper cleanup
24. **Concurrent Operations**: Proper handling of concurrent requests and operations
25. **File Handling**: Secure and efficient file upload and processing

### Maintenance and Extensibility Criteria
26. **Code Organization**: Clean, maintainable code structure following project patterns
27. **Extensibility**: Architecture supports future API additions and modifications
28. **Debugging**: Comprehensive logging and debugging capabilities
29. **Monitoring**: Proper error reporting and monitoring integration
30. **Future-Proofing**: Implementation supports future Dify API evolution

## Final Deliverables

Upon successful completion, the following deliverables will be provided:

### Code Deliverables
1. **39 Fully Implemented APIs** across 5 specialized resources
2. **Complete Model Library** with 100+ model classes using flat structure
3. **5 Resource Classes** with comprehensive functionality
4. **Version and Service Integration** with proper client integration
5. **Comprehensive Test Suite** with unit, integration, and example tests

### Documentation Deliverables
6. **API Documentation** with complete usage guides and examples
7. **Implementation Guide** with architecture and design decisions
8. **Migration Guide** with upgrade instructions and compatibility information
9. **Performance Guide** with optimization recommendations
10. **Security Guide** with security best practices and validation

### Quality Assurance Deliverables
11. **Test Coverage Report** with detailed coverage statistics
12. **Performance Benchmark Report** with performance characteristics
13. **Security Audit Report** with security validation results
14. **Code Quality Report** with linting and type checking results
15. **Integration Test Report** with end-to-end validation results

## Summary

This comprehensive implementation plan provides a systematic approach to building the complete Knowledge Base API module with 33 APIs across 5 resources. The plan includes 24 detailed implementation steps, each with specific requirements and corresponding test validation.

### Documentation and Test Consistency Requirements

**Critical Issues Identified**: Multiple consistency issues must be resolved:

**Examples Documentation Inconsistencies**:
- **knowledge-api.md**: Documents 33 APIs (6+12+8+7+1)
- **examples/README.md**: Claims 29 APIs (6+10+7+7+0)
- **Required Fixes**: Update examples documentation, add missing sections, verify file completeness

**Test Structure Inconsistencies**:
- **Missing Model Tests**: No tests for Model Management API (1 API)
- **Metadata vs Document**: Unclear separation between metadata and document tests
- **Test Coverage Gaps**: May not cover all 33 APIs comprehensively
- **Required Fixes**: Add missing tests, clarify test structure, ensure complete coverage

### Key Implementation Principles:
- **Type Safety**: Strict typing with Literal types throughout all 39 APIs
- **Builder Patterns**: Consistent builder patterns for all 100+ model classes
- **Error Handling**: Comprehensive error handling and BaseResponse inheritance
- **Testing**: Each implementation step followed by corresponding tests
- **Safety**: "[Example]" prefix for all example resources across all APIs
- **Minimalism**: Minimal code approach while maintaining full functionality
- **Consistency**: Following established project patterns and conventions
- **Performance**: Optimized for high-performance operations and concurrent usage
- **Security**: Comprehensive security validation and input sanitization
- **Maintainability**: Clean, extensible architecture supporting future growth

### Implementation Scope:
- **33 APIs** implemented across 5 specialized resources
- **100+ Model Classes** with comprehensive type safety
- **Complex Nested Paths** supporting up to 5-level resource nesting
- **File Upload Support** with multipart/form-data handling
- **Search and Retrieval** with advanced query capabilities
- **Tag Management** with binding and unbinding operations
- **Batch Operations** with status monitoring and management
- **Complete Integration** with existing dify-oapi2 architecture
- **Documentation Consistency** with accurate API counts and complete example coverage

The implementation will result in a robust, type-safe, well-tested, and highly performant Knowledge Base API module that seamlessly integrates with the existing dify-oapi2 architecture while providing comprehensive knowledge management capabilities for AI applications. All documentation inconsistencies will be resolved to ensure accurate API coverage and complete example availability.