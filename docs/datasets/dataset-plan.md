# Dataset API Implementation Plan - AI Prompts

This document provides step-by-step prompts for implementing the complete dataset management functionality in the dify-oapi knowledge_base module. Each step includes implementation and testing phases to ensure code quality.

## Overview

The implementation covers 19 dataset-related APIs organized into three main resource groups:
- **Dataset Management**: 6 APIs (CRUD + retrieval)
- **Metadata Management**: 7 APIs (CRUD + built-in + document operations)  
- **Tag Management**: 7 APIs (CRUD + binding operations)

## Implementation Steps

### Phase 1: Common Models Foundation

#### Step 1: Create Shared Common Models
**Prompt:**
```
Create the shared common models for the dataset API implementation in `dify_oapi/api/knowledge_base/v1/model/dataset/`. 

Implement the following model files with proper type hints, builder patterns, and Pydantic validation:

1. `retrieval_model.py` - RetrievalModel class with fields:
   - search_method: str | None = None
   - reranking_enable: bool | None = None
   - reranking_mode: str | None = None
   - reranking_model: RerankingModel | None = None
   - weights: float | None = None
   - top_k: int | None = None
   - score_threshold_enabled: bool | None = None
   - score_threshold: float | None = None
   - metadata_filtering_conditions: MetadataFilteringConditions | None = None

2. `reranking_model.py` - RerankingModel class with fields:
   - reranking_provider_name: str | None = None
   - reranking_model_name: str | None = None

3. `external_knowledge_info.py` - ExternalKnowledgeInfo class with fields:
   - external_knowledge_id: str | None = None
   - external_knowledge_api_id: str | None = None
   - external_knowledge_api_name: str | None = None
   - external_knowledge_api_endpoint: str | None = None

4. `metadata_filtering_conditions.py` - MetadataFilteringConditions class with fields:
   - logical_operator: str | None = None
   - conditions: List[FilterCondition] | None = None

5. `filter_condition.py` - FilterCondition class with fields:
   - name: str | None = None
   - comparison_operator: str | None = None
   - value: str | int | float | None = None

6. `dataset_info.py` - DatasetInfo class with comprehensive dataset fields based on API response structure
7. `tag_info.py` - TagInfo class for tag information
8. `metadata_info.py` - MetadataInfo class for metadata information

MANDATORY REQUIREMENTS:
- ALL classes MUST inherit from `pydantic.BaseModel`
- ALL classes MUST include `from __future__ import annotations` at the top
- ALL classes MUST have builder patterns with proper type hints
- Use `@staticmethod` decorator for builder() methods
- Builder classes MUST follow naming pattern: ClassNameBuilder
- All fields MUST use proper type hints with `| None = None` for optional fields
- Follow existing project patterns in dify_oapi for consistency
```

#### Step 2: Test Common Models
**Prompt:**
```
Create comprehensive unit tests for all common models created in Step 1. 

Create test file `tests/knowledge_base/v1/model/test_dataset_models.py` that covers:

1. Model instantiation and validation
2. Builder pattern functionality for all models
3. Serialization/deserialization using Pydantic
4. Edge cases and validation errors
5. Optional field handling
6. Nested model relationships (RetrievalModel with RerankingModel)

MANDATORY REQUIREMENTS:
- ALL test methods MUST include proper type annotations for parameters and return types
- Use `-> None` for test method return types
- Import `typing.Any` for complex mock objects
- Use pytest framework with proper fixtures
- Test both direct instantiation and builder pattern approaches
- Verify method chaining works correctly in builders
- Test serialization with `model_dump()` method
- Ensure all tests pass with good coverage (>90%)
```

### Phase 2: Dataset Management APIs (6 APIs)

#### Step 3: Dataset Request/Response Models
**Prompt:**
```
Create all request and response models for dataset management APIs in `dify_oapi/api/knowledge_base/v1/model/dataset/` following MANDATORY code style rules.

Implement the following model files with STRICT adherence to patterns:

**POST Request Models (with RequestBody)**:
1. `create_request.py` - CreateRequest + CreateRequestBuilder (inherits BaseRequest)
2. `create_request_body.py` - CreateRequestBody + CreateRequestBodyBuilder (inherits BaseModel)
   Fields: name, description, indexing_technique, permission, provider, external_knowledge_api_id, external_knowledge_id, embedding_model, embedding_model_provider, retrieval_model

3. `retrieve_request.py` - RetrieveRequest + RetrieveRequestBuilder (inherits BaseRequest)
4. `retrieve_request_body.py` - RetrieveRequestBody + RetrieveRequestBodyBuilder (inherits BaseModel)
   Fields: query, retrieval_model, external_retrieval_model

**PATCH Request Models (with RequestBody)**:
5. `update_request.py` - UpdateRequest + UpdateRequestBuilder (inherits BaseRequest)
6. `update_request_body.py` - UpdateRequestBody + UpdateRequestBodyBuilder (inherits BaseModel)
   Fields: name, indexing_technique, permission, embedding_model_provider, embedding_model, retrieval_model, partial_member_list

**GET Request Models (no RequestBody)**:
7. `list_request.py` - ListRequest + ListRequestBuilder (inherits BaseRequest)
   Query params: keyword, tag_ids, page, limit, include_all

8. `get_request.py` - GetRequest + GetRequestBuilder (inherits BaseRequest)
   Path params: dataset_id

**DELETE Request Models (no RequestBody)**:
9. `delete_request.py` - DeleteRequest + DeleteRequestBuilder (inherits BaseRequest)
   Path params: dataset_id

**Response Models**:
10. `create_response.py` - CreateResponse (inherits DatasetInfo, BaseResponse)
11. `list_response.py` - ListResponse (inherits BaseResponse) with data, has_more, limit, total, page fields
12. `get_response.py` - GetResponse (inherits DatasetInfo, BaseResponse)
13. `update_response.py` - UpdateResponse (inherits DatasetInfo, BaseResponse)
14. `delete_response.py` - DeleteResponse (inherits BaseResponse) - empty for 204
15. `retrieve_response.py` - RetrieveResponse (inherits BaseResponse) with query and records fields

CRITICAL REQUIREMENTS:
- ALL class names MUST match file names exactly (NO module prefixes)
- Request classes MUST inherit from BaseRequest
- RequestBody classes MUST inherit from BaseModel
- Response classes MUST inherit from BaseResponse (and DatasetInfo where applicable)
- Use `request_body()` method pattern for POST/PATCH requests
- Use `add_query()` for query parameters
- Use `paths["param"]` for path parameters
- Builder variables MUST use full descriptive names (e.g., `self._create_request`)
- Set correct HTTP methods and URIs in builder constructors
- NO Builder patterns for Response classes
```

#### Step 4: Test Dataset Models
**Prompt:**
```
Update the comprehensive unit tests in `tests/knowledge_base/v1/model/test_dataset_models.py` to include all dataset models.

Test all models created in Step 3, covering:
1. Model validation and required fields
2. Builder pattern functionality for Request and RequestBody models
3. Serialization/deserialization
4. Integration with common models
5. Edge cases and error handling
6. HTTP method and URI configuration in Request builders
7. Path and query parameter handling

MANDATORY REQUIREMENTS:
- ALL test methods MUST include proper type annotations: `def test_method(self) -> None:`
- Import necessary typing modules at the top
- Use pytest framework with proper fixtures
- Test both sync and async scenarios where applicable
- Verify Request classes inherit from BaseRequest
- Verify RequestBody classes inherit from BaseModel
- Verify Response classes inherit from BaseResponse
- Ensure all tests pass with good coverage (>90%)
```

#### Step 5: Dataset Resource Implementation
**Prompt:**
```
Implement the Dataset resource class in `dify_oapi/api/knowledge_base/v1/resource/dataset.py`.

Create a Dataset class with the following methods based on the API endpoints:
1. `create(request: CreateRequest, request_option: RequestOption) -> CreateResponse`
2. `acreate(request: CreateRequest, request_option: RequestOption) -> CreateResponse`
3. `list(request: ListRequest, request_option: RequestOption) -> ListResponse`
4. `alist(request: ListRequest, request_option: RequestOption) -> ListResponse`
5. `get(request: GetRequest, request_option: RequestOption) -> GetResponse`
6. `aget(request: GetRequest, request_option: RequestOption) -> GetResponse`
7. `update(request: UpdateRequest, request_option: RequestOption) -> UpdateResponse`
8. `aupdate(request: UpdateRequest, request_option: RequestOption) -> UpdateResponse`
9. `delete(request: DeleteRequest, request_option: RequestOption) -> DeleteResponse`
10. `adelete(request: DeleteRequest, request_option: RequestOption) -> DeleteResponse`
11. `retrieve(request: RetrieveRequest, request_option: RequestOption) -> RetrieveResponse`
12. `aretrieve(request: RetrieveRequest, request_option: RequestOption) -> RetrieveResponse`

Follow the existing transport patterns and HTTP method mappings. Map to correct endpoints:
- POST /v1/datasets (create)
- GET /v1/datasets (list)
- GET /v1/datasets/:dataset_id (get)
- PATCH /v1/datasets/:dataset_id (update)
- DELETE /v1/datasets/:dataset_id (delete)
- POST /v1/datasets/:dataset_id/retrieve (retrieve)

MANDATORY REQUIREMENTS:
- Use Transport.execute() for sync methods
- Use ATransport.aexecute() for async methods
- Include proper error handling and response parsing
- Follow existing resource class patterns in the project
- Import all necessary request/response models
- Use proper type hints for all method parameters and return types
```

#### Step 6: Test Dataset Resource
**Prompt:**
```
Create comprehensive integration tests for the Dataset resource in `tests/knowledge_base/v1/resource/test_dataset_resource.py`.

Test all methods implemented in Step 5, including:
1. HTTP method and URL mapping verification
2. Request serialization and response deserialization
3. Error handling for various HTTP status codes
4. Both sync and async method variants
5. Mock API responses based on the API documentation
6. Transport layer integration

MANDATORY REQUIREMENTS:
- ALL test methods MUST include proper type annotations: `def test_method(self) -> None:`
- Use pytest fixtures and mock responses to simulate API interactions
- Test all 12 methods (6 sync + 6 async)
- Verify correct HTTP methods and URLs are used
- Mock Transport.execute() and ATransport.aexecute() calls
- Test error scenarios (4xx, 5xx responses)
- Ensure all tests pass with good coverage
- Use `typing.Any` for complex mock objects like `monkeypatch`
```

### Phase 3: Metadata Management APIs (7 APIs)

#### Step 7: Metadata Request/Response Models
**Prompt:**
```
Create all request and response models for metadata management APIs in `dify_oapi/api/knowledge_base/v1/model/metadata/`.

Implement the following model files based on the API specifications:

**POST Request Models (with RequestBody)**:
1. `create_request.py` - CreateRequest + CreateRequestBuilder
2. `create_request_body.py` - CreateRequestBody + CreateRequestBodyBuilder
   Fields: type, name

3. `toggle_builtin_request.py` - ToggleBuiltinRequest + ToggleBuiltinRequestBuilder
   Path params: dataset_id, action

4. `update_document_request.py` - UpdateDocumentRequest + UpdateDocumentRequestBuilder
5. `update_document_request_body.py` - UpdateDocumentRequestBody + UpdateDocumentRequestBodyBuilder
   Fields: operation_data (array of objects with document_id, metadata_list)

**PATCH Request Models (with RequestBody)**:
6. `update_request.py` - UpdateRequest + UpdateRequestBuilder
7. `update_request_body.py` - UpdateRequestBody + UpdateRequestBodyBuilder
   Fields: name

**GET Request Models (no RequestBody)**:
8. `list_request.py` - ListRequest + ListRequestBuilder
   Path params: dataset_id

**DELETE Request Models (no RequestBody)**:
9. `delete_request.py` - DeleteRequest + DeleteRequestBuilder
   Path params: dataset_id, metadata_id

**Response Models**:
10. `create_response.py` - CreateResponse (inherits MetadataInfo, BaseResponse)
11. `list_response.py` - ListResponse (inherits BaseResponse) with doc_metadata, built_in_field_enabled
12. `update_response.py` - UpdateResponse (inherits MetadataInfo, BaseResponse)
13. `delete_response.py` - DeleteResponse (inherits BaseResponse) - empty for 204
14. `toggle_builtin_response.py` - ToggleBuiltinResponse (inherits BaseResponse) with result field
15. `update_document_response.py` - UpdateDocumentResponse (inherits BaseResponse) with result field

CRITICAL REQUIREMENTS:
- Follow EXACT same patterns as dataset models
- ALL class names MUST match file names (NO prefixes)
- Use correct URI patterns with dataset_id and metadata_id path parameters
- Include proper validation for complex nested structures (operation_data)
```

#### Step 8: Test Metadata Models
**Prompt:**
```
Create comprehensive unit tests for metadata request/response models in `tests/knowledge_base/v1/model/test_metadata_models.py`.

Test all models created in Step 7, covering:
1. Model validation and required fields
2. Builder pattern functionality
3. Serialization/deserialization
4. Complex nested structures (operation_data)
5. Edge cases and error handling
6. Path parameter handling for dataset_id and metadata_id

MANDATORY REQUIREMENTS:
- ALL test methods MUST include proper type annotations: `def test_method(self) -> None:`
- Use pytest framework with proper fixtures
- Test complex nested data structures
- Verify URI patterns are correct
- Ensure all tests pass with good coverage (>90%)
```

#### Step 9: Metadata Resource Implementation
**Prompt:**
```
Implement the Metadata resource class in `dify_oapi/api/knowledge_base/v1/resource/metadata.py`.

Create a Metadata class with the following methods based on the API endpoints:
1. `create(request: CreateRequest, request_option: RequestOption) -> CreateResponse`
2. `acreate(request: CreateRequest, request_option: RequestOption) -> CreateResponse`
3. `list(request: ListRequest, request_option: RequestOption) -> ListResponse`
4. `alist(request: ListRequest, request_option: RequestOption) -> ListResponse`
5. `update(request: UpdateRequest, request_option: RequestOption) -> UpdateResponse`
6. `aupdate(request: UpdateRequest, request_option: RequestOption) -> UpdateResponse`
7. `delete(request: DeleteRequest, request_option: RequestOption) -> DeleteResponse`
8. `adelete(request: DeleteRequest, request_option: RequestOption) -> DeleteResponse`
9. `toggle_builtin(request: ToggleBuiltinRequest, request_option: RequestOption) -> ToggleBuiltinResponse`
10. `atoggle_builtin(request: ToggleBuiltinRequest, request_option: RequestOption) -> ToggleBuiltinResponse`
11. `update_document(request: UpdateDocumentRequest, request_option: RequestOption) -> UpdateDocumentResponse`
12. `aupdate_document(request: UpdateDocumentRequest, request_option: RequestOption) -> UpdateDocumentResponse`

Map to correct endpoints:
- POST /v1/datasets/:dataset_id/metadata (create)
- GET /v1/datasets/:dataset_id/metadata (list)
- PATCH /v1/datasets/:dataset_id/metadata/:metadata_id (update)
- DELETE /v1/datasets/:dataset_id/metadata/:metadata_id (delete)
- POST /v1/datasets/:dataset_id/metadata/built-in/:action (toggle_builtin)
- POST /v1/datasets/:dataset_id/documents/metadata (update_document)

MANDATORY REQUIREMENTS:
- Follow exact same patterns as Dataset resource
- Handle path parameters correctly (dataset_id, metadata_id, action)
- Use Transport.execute() and ATransport.aexecute()
- Include proper error handling and type hints
```

#### Step 10: Test Metadata Resource
**Prompt:**
```
Create comprehensive integration tests for the Metadata resource in `tests/knowledge_base/v1/resource/test_metadata_resource.py`.

Test all methods implemented in Step 9, including:
1. HTTP method and URL mapping verification (including path parameters)
2. Request serialization and response deserialization
3. Error handling for various HTTP status codes
4. Both sync and async method variants
5. Mock API responses based on the API documentation

MANDATORY REQUIREMENTS:
- ALL test methods MUST include proper type annotations: `def test_method(self) -> None:`
- Use pytest fixtures and mock responses
- Test all 12 methods (6 sync + 6 async)
- Verify correct path parameter handling
- Ensure all tests pass with good coverage
```

### Phase 4: Tag Management APIs (7 APIs)

#### Step 11: Tag Request/Response Models
**Prompt:**
```
Create all request and response models for tag management APIs in `dify_oapi/api/knowledge_base/v1/model/tag/`.

Implement the following model files based on the API specifications:

**POST Request Models (with RequestBody)**:
1. `create_request.py` - CreateRequest + CreateRequestBuilder
2. `create_request_body.py` - CreateRequestBody + CreateRequestBodyBuilder
   Fields: name

3. `bind_request.py` - BindRequest + BindRequestBuilder
4. `bind_request_body.py` - BindRequestBody + BindRequestBodyBuilder
   Fields: tag_ids (array), target_id

5. `unbind_request.py` - UnbindRequest + UnbindRequestBuilder
6. `unbind_request_body.py` - UnbindRequestBody + UnbindRequestBodyBuilder
   Fields: tag_id, target_id

7. `query_bound_request.py` - QueryBoundRequest + QueryBoundRequestBuilder
   Path params: dataset_id

**PATCH Request Models (with RequestBody)**:
8. `update_request.py` - UpdateRequest + UpdateRequestBuilder
9. `update_request_body.py` - UpdateRequestBody + UpdateRequestBodyBuilder
   Fields: name, tag_id

**GET Request Models (no RequestBody)**:
10. `list_request.py` - ListRequest + ListRequestBuilder (no parameters)

**DELETE Request Models (with RequestBody for tag_id)**:
11. `delete_request.py` - DeleteRequest + DeleteRequestBuilder
12. `delete_request_body.py` - DeleteRequestBody + DeleteRequestBodyBuilder
   Fields: tag_id

**Response Models**:
13. `create_response.py` - CreateResponse (inherits TagInfo, BaseResponse)
14. `list_response.py` - ListResponse (inherits BaseResponse) with array of TagInfo
15. `update_response.py` - UpdateResponse (inherits TagInfo, BaseResponse)
16. `delete_response.py` - DeleteResponse (inherits BaseResponse) with result field
17. `bind_response.py` - BindResponse (inherits BaseResponse) with result field
18. `unbind_response.py` - UnbindResponse (inherits BaseResponse) with result field
19. `query_bound_response.py` - QueryBoundResponse (inherits BaseResponse) with data array and total

CRITICAL REQUIREMENTS:
- Follow EXACT same patterns as previous models
- Handle different URL patterns (global vs dataset-specific endpoints)
- DELETE request has RequestBody (unusual pattern for tag_id)
- Use TagInfo from common models
```

#### Step 12: Test Tag Models
**Prompt:**
```
Create comprehensive unit tests for tag request/response models in `tests/knowledge_base/v1/model/test_tag_models.py`.

Test all models created in Step 11, covering:
1. Model validation and required fields
2. Builder pattern functionality
3. Serialization/deserialization
4. Array field handling (tag_ids)
5. Edge cases and error handling
6. Different endpoint patterns (global vs dataset-specific)

MANDATORY REQUIREMENTS:
- ALL test methods MUST include proper type annotations: `def test_method(self) -> None:`
- Use pytest framework with proper fixtures
- Test array field validation (tag_ids)
- Verify different URI patterns are correct
- Ensure all tests pass with good coverage (>90%)
```

#### Step 13: Tag Resource Implementation
**Prompt:**
```
Implement the Tag resource class in `dify_oapi/api/knowledge_base/v1/resource/tag.py`.

Create a Tag class with the following methods based on the API endpoints:
1. `create(request: CreateRequest, request_option: RequestOption) -> CreateResponse`
2. `acreate(request: CreateRequest, request_option: RequestOption) -> CreateResponse`
3. `list(request: ListRequest, request_option: RequestOption) -> ListResponse`
4. `alist(request: ListRequest, request_option: RequestOption) -> ListResponse`
5. `update(request: UpdateRequest, request_option: RequestOption) -> UpdateResponse`
6. `aupdate(request: UpdateRequest, request_option: RequestOption) -> UpdateResponse`
7. `delete(request: DeleteRequest, request_option: RequestOption) -> DeleteResponse`
8. `adelete(request: DeleteRequest, request_option: RequestOption) -> DeleteResponse`
9. `bind_tags(request: BindRequest, request_option: RequestOption) -> BindResponse`
10. `abind_tags(request: BindRequest, request_option: RequestOption) -> BindResponse`
11. `unbind_tag(request: UnbindRequest, request_option: RequestOption) -> UnbindResponse`
12. `aunbind_tag(request: UnbindRequest, request_option: RequestOption) -> UnbindResponse`
13. `query_bound(request: QueryBoundRequest, request_option: RequestOption) -> QueryBoundResponse`
14. `aquery_bound(request: QueryBoundRequest, request_option: RequestOption) -> QueryBoundResponse`

Map to correct endpoints:
- POST /v1/datasets/tags (create)
- GET /v1/datasets/tags (list)
- PATCH /v1/datasets/tags (update)
- DELETE /v1/datasets/tags (delete)
- POST /v1/datasets/tags/binding (bind_tags)
- POST /v1/datasets/tags/unbinding (unbind_tag)
- POST /v1/datasets/:dataset_id/tags (query_bound)

MANDATORY REQUIREMENTS:
- Handle different URL patterns correctly (global vs dataset-specific endpoints)
- Follow exact same patterns as previous resources
- Use Transport.execute() and ATransport.aexecute()
- Include proper error handling and type hints
```

#### Step 14: Test Tag Resource
**Prompt:**
```
Create comprehensive integration tests for the Tag resource in `tests/knowledge_base/v1/resource/test_tag_resource.py`.

Test all methods implemented in Step 13, including:
1. HTTP method and URL mapping verification
2. Request serialization and response deserialization
3. Error handling for various HTTP status codes
4. Both sync and async method variants
5. Mock API responses based on the API documentation
6. Different endpoint patterns (global vs dataset-specific)

MANDATORY REQUIREMENTS:
- ALL test methods MUST include proper type annotations: `def test_method(self) -> None:`
- Use pytest fixtures and mock responses
- Test all 14 methods (7 sync + 7 async)
- Verify different URL patterns work correctly
- Ensure all tests pass with good coverage
```

### Phase 5: Integration and Version Updates

#### Step 15: Update Version Integration
**Prompt:**
```
Update the knowledge_base v1 version integration to include the new resources.

Modify `dify_oapi/api/knowledge_base/v1/version.py` to:
1. Import the new Metadata and Tag resource classes
2. Add metadata and tag properties to the V1 class
3. Initialize them with the config parameter
4. Ensure backward compatibility with existing resources (document, segment)

MANDATORY REQUIREMENTS:
- Follow existing patterns in the V1 class
- Import all necessary resource classes
- Initialize resources with config parameter
- Maintain existing API structure
- Update any necessary import statements
```

#### Step 16: Test Version Integration
**Prompt:**
```
Create integration tests for the updated V1 version class in `tests/knowledge_base/v1/integration/test_version_integration.py`.

Test:
1. All resources are properly initialized
2. Config is correctly passed to all resources
3. New resources (dataset, metadata, tag) are accessible
4. Existing resources still work correctly
5. Client integration works end-to-end

MANDATORY REQUIREMENTS:
- ALL test methods MUST include proper type annotations: `def test_method(self) -> None:`
- Use pytest framework with proper fixtures
- Test resource initialization and accessibility
- Verify config propagation to all resources
- Ensure complete knowledge_base module works as expected
```

### Phase 6: Documentation and Examples

#### Step 17: Create Usage Examples
**Prompt:**
```
Create comprehensive usage examples for the dataset management functionality in `examples/knowledge_base/`.

Create examples using resource-based directory structure with MINIMAL code approach:

**Dataset Examples** (`examples/knowledge_base/dataset/`):
1. `create.py` - Create dataset examples (sync + async)
2. `list.py` - List datasets examples (sync + async)
3. `get.py` - Get dataset details examples (sync + async)
4. `update.py` - Update dataset examples (sync + async)
5. `delete.py` - Delete dataset examples (sync + async)
6. `retrieve.py` - Dataset retrieval examples (sync + async)

**Metadata Examples** (`examples/knowledge_base/metadata/`):
1. `create.py` - Create metadata examples (sync + async)
2. `list.py` - List metadata examples (sync + async)
3. `update.py` - Update metadata examples (sync + async)
4. `delete.py` - Delete metadata examples (sync + async)
5. `toggle_builtin.py` - Toggle built-in metadata examples (sync + async)
6. `update_document.py` - Update document metadata examples (sync + async)

**Tag Examples** (`examples/knowledge_base/tag/`):
1. `create.py` - Create tag examples (sync + async)
2. `list.py` - List tags examples (sync + async)
3. `update.py` - Update tag examples (sync + async)
4. `delete.py` - Delete tag examples (sync + async)
5. `bind.py` - Bind tags examples (sync + async)
6. `unbind.py` - Unbind tag examples (sync + async)
7. `query_bound.py` - Query bound tags examples (sync + async)

**Additional Files**:
8. `README.md` - Examples overview and usage guide

MANDATORY REQUIREMENTS:
- Write ABSOLUTE MINIMAL code needed to demonstrate each API correctly
- ALL resource names MUST use "[Example]" prefix for safety
- Environment variable validation at function start (raise ValueError if missing)
- Both synchronous and asynchronous implementations
- Basic try-catch error handling
- Delete operations MUST check for "[Example]" prefix
- Follow existing example patterns in the project
- Update main `examples/README.md` with new examples
```

#### Step 18: Test Examples
**Prompt:**
```
Create validation tests for all examples created in Step 17.

Create `tests/knowledge_base/v1/integration/test_examples_validation.py` that:
1. Validates example code syntax and imports
2. Mocks API calls to test example logic
3. Ensures examples follow best practices
4. Verifies error handling works correctly
5. Tests both sync and async example variants
6. Validates "[Example]" prefix usage in resource names

MANDATORY REQUIREMENTS:
- ALL test methods MUST include proper type annotations: `def test_method(self) -> None:`
- Use pytest framework and mock API responses
- Test all example files for syntax and functionality
- Verify safety measures (prefix checking) work correctly
- Ensure examples are educational and functional
```

### Phase 7: Final Integration and Quality Assurance

#### Step 19: Comprehensive Integration Testing
**Prompt:**
```
Create comprehensive end-to-end integration tests for all resources:

1. **`tests/knowledge_base/v1/integration/test_dataset_api_integration.py`**:
   - Dataset lifecycle (create → update → retrieve → delete)
   - Error scenarios and edge cases

2. **`tests/knowledge_base/v1/integration/test_metadata_api_integration.py`**:
   - Metadata management workflow
   - Built-in metadata operations
   - Document metadata updates

3. **`tests/knowledge_base/v1/integration/test_tag_api_integration.py`**:
   - Tag management and binding workflow
   - Global tag operations

4. **`tests/knowledge_base/v1/integration/test_comprehensive_integration.py`**:
   - Complete workflows combining all resources
   - Cross-resource interactions and dependencies
   - End-to-end scenarios (create dataset → add metadata → bind tags → retrieve)

MANDATORY REQUIREMENTS:
- ALL test methods MUST include proper type annotations: `def test_method(self) -> None:`
- Use realistic test data and scenarios
- Mock all API calls with proper responses
- Test error scenarios and edge cases
- Ensure all 19 APIs work together correctly
- Verify cross-resource dependencies and workflows
```

#### Step 20: Final Quality Assurance and Documentation
**Prompt:**
```
Perform final quality assurance and create comprehensive documentation.

Tasks:
1. Run all tests and ensure 100% pass rate
2. Verify code coverage meets project standards (>90%)
3. Update API documentation with new functionality
4. Create migration guide for existing users
5. Update README with new dataset management features
6. Perform code review checklist:
   - Type hints are comprehensive and correct
   - Error handling is consistent across all resources
   - Builder patterns work correctly for all models
   - Async/sync parity is maintained
   - Documentation is complete and accurate
   - All 19 APIs are fully functional

Create a final validation report confirming all requirements are met and all dataset APIs are production-ready.

MANDATORY REQUIREMENTS:
- Document any breaking changes from existing implementations
- Provide clear migration paths for existing users
- Ensure all code follows project conventions
- Verify all examples work correctly
- Confirm comprehensive test coverage
```

## Success Criteria

Each step should meet the following criteria:
- ✅ All code follows existing project patterns and conventions
- ✅ Comprehensive type hints and Pydantic validation
- ✅ Both sync and async method variants implemented
- ✅ Builder pattern support for all request models
- ✅ Proper error handling and HTTP status code mapping
- ✅ Unit tests with good coverage (>90%)
- ✅ Integration tests with mock API responses
- ✅ Documentation and examples provided
- ✅ Backward compatibility maintained where possible
- ✅ **Test typing requirements**: All test method parameters and return types must include proper type annotations

## API Coverage Summary

### Dataset Management (6 APIs)
1. POST /v1/datasets - Create empty dataset
2. GET /v1/datasets - List datasets
3. GET /v1/datasets/:dataset_id - Get dataset details
4. PATCH /v1/datasets/:dataset_id - Update dataset details
5. DELETE /v1/datasets/:dataset_id - Delete dataset
6. POST /v1/datasets/:dataset_id/retrieve - Dataset retrieval

### Metadata Management (7 APIs)
7. POST /v1/datasets/:dataset_id/metadata - Create metadata
8. GET /v1/datasets/:dataset_id/metadata - List dataset metadata
9. PATCH /v1/datasets/:dataset_id/metadata/:metadata_id - Update metadata
10. DELETE /v1/datasets/:dataset_id/metadata/:metadata_id - Delete metadata
11. POST /v1/datasets/:dataset_id/metadata/built-in/:action - Toggle built-in metadata
12. POST /v1/datasets/:dataset_id/documents/metadata - Update document metadata

### Tag Management (7 APIs)
13. POST /v1/datasets/tags - Create knowledge type tag
14. GET /v1/datasets/tags - Get knowledge type tags
15. PATCH /v1/datasets/tags - Update knowledge type tag name
16. DELETE /v1/datasets/tags - Delete knowledge type tag
17. POST /v1/datasets/tags/binding - Bind dataset and knowledge type tags
18. POST /v1/datasets/tags/unbinding - Unbind dataset and knowledge type tag
19. POST /v1/datasets/:dataset_id/tags - Query knowledge base bound tags

## Code Style Rules (MANDATORY - NO EXCEPTIONS)

### Request Model Architecture (STRICT COMPLIANCE)
**Request Classes**:
- MUST inherit from `BaseRequest` (NEVER from `BaseModel`)
- MUST include `request_body` attribute of type `RequestBody | None` for POST/PATCH requests
- MUST use `request_body()` method in builder (NOT individual field methods)
- Builder variables MUST use full descriptive names (e.g., `self._create_request`, `self._list_request`)
- MUST set `http_method` and `uri` in builder constructor
- Path parameters MUST use `self._request.paths["param_name"] = value`
- Query parameters MUST use `self._request.add_query("key", value)`

**RequestBody Separation (POST/PATCH/PUT only)**:
- RequestBody MUST be in separate file from Request
- RequestBody MUST inherit from `pydantic.BaseModel`
- RequestBody MUST include its own Builder pattern
- File naming: `create_request.py` + `create_request_body.py`
- Both Request and RequestBody MUST have Builder classes

### HTTP Method Implementation Patterns
**GET Requests** (list, get):
- NO RequestBody file needed
- Use query parameters: `self._request.add_query("key", value)`
- Use path parameters: `self._request.paths["param_name"] = value`

**POST Requests** (create, retrieve, bind, etc.):
- REQUIRE separate RequestBody file
- Use `request_body()` method in Request builder
- RequestBody builder methods set fields directly

**PATCH/PUT Requests** (update):
- REQUIRE separate RequestBody file
- Support path parameters for resource ID
- Use `request_body()` method in Request builder

**DELETE Requests**:
- Usually NO RequestBody file needed
- Use path parameters for resource ID
- Exception: Tag delete uses RequestBody for tag_id

### Class Naming Convention (ZERO TOLERANCE)
**Universal Naming Pattern**:
- File names determine class names exactly (e.g., `create_request.py` → `CreateRequest`)
- Each class has corresponding Builder (e.g., `CreateRequest` + `CreateRequestBuilder`)
- Pattern applies to all model types: Request, RequestBody, Response

**STRICT Naming Rules (NO EXCEPTIONS)**:
- Remove ALL module/domain prefixes from class names
- Class names MUST match file names exactly (case-sensitive)
- Apply uniformly across ALL resources: dataset, metadata, tag
- Use operation-based names: `CreateRequest`, `ListResponse`, `UpdateRequestBody`
- NEVER use domain-specific names: `CreateDatasetRequest`, `CreateMetadataResponse`
- NO legacy naming patterns allowed
- Consistent across all HTTP methods and operation types

### Public Class Inheritance Rules (CRITICAL)
**Public/Common Classes**:
- Public classes (DatasetInfo, TagInfo, MetadataInfo, RetrievalModel, etc.) MUST inherit from `pydantic.BaseModel` ONLY
- Public classes MUST NOT inherit from `BaseResponse`
- Public classes MUST have Builder patterns for consistency and ease of use
- Examples: `DatasetInfo`, `TagInfo`, `MetadataInfo`, `RetrievalModel`, `RerankingModel`

**Response Classes**:
- Response classes MUST inherit from `BaseResponse` for error handling capabilities
- Response classes MAY use multiple inheritance when they need to include public class data
- Pattern: `class CreateResponse(DatasetInfo, BaseResponse):`
- Response classes MUST NOT have Builder patterns

### Builder Pattern Implementation (EXACT SPECIFICATION)
**Request Builder Pattern**:
```python
class CreateRequestBuilder:
    def __init__(self):
        create_request = CreateRequest()
        create_request.http_method = HttpMethod.POST
        create_request.uri = "/v1/datasets"
        self._create_request = create_request

    def build(self) -> CreateRequest:
        return self._create_request

    def request_body(self, request_body: CreateRequestBody) -> CreateRequestBuilder:
        self._create_request.request_body = request_body
        self._create_request.body = request_body.model_dump(exclude_none=True, mode="json")
        return self
```

**RequestBody Builder Pattern**:
```python
class CreateRequestBodyBuilder:
    def __init__(self):
        create_request_body = CreateRequestBody()
        self._create_request_body = create_request_body

    def build(self) -> CreateRequestBody:
        return self._create_request_body

    def name(self, name: str) -> CreateRequestBodyBuilder:
        self._create_request_body.name = name
        return self
```

### Environment Variable Validation (MANDATORY)
**All Examples MUST**:
- Check for required environment variables at function start
- Raise `ValueError` with descriptive message if missing
- NEVER use `print()` statements for missing variables
- Validate `API_KEY` and resource-specific IDs as needed
- Place ALL validations at the very beginning of each function

### Testing Requirements (MANDATORY)
**All Test Methods MUST**:
- Include proper type annotations: `def test_method(self) -> None:`
- Import necessary typing modules (`typing.Any` for complex objects)
- Use pytest framework with proper fixtures
- Achieve >90% code coverage
- Test both sync and async variants where applicable
- Mock API calls appropriately
- Follow consistent patterns across all test files

This comprehensive plan provides step-by-step prompts for implementing all 19 dataset management APIs with proper testing, documentation, and examples. Each step builds upon the previous ones and includes specific requirements to ensure code quality and consistency.