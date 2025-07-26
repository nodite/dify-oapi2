# Dataset API Implementation Plan

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
   - search_method: str (required)
   - reranking_enable: Optional[bool]
   - reranking_mode: Optional[str]
   - reranking_model: Optional[RerankingModel]
   - weights: Optional[float]
   - top_k: Optional[int]
   - score_threshold_enabled: Optional[bool]
   - score_threshold: Optional[float]
   - metadata_filtering_conditions: Optional[MetadataFilteringConditions]

2. `reranking_model.py` - RerankingModel class with fields:
   - reranking_provider_name: str
   - reranking_model_name: str

3. `external_knowledge_info.py` - ExternalKnowledgeInfo class with fields:
   - external_knowledge_id: Optional[str]
   - external_knowledge_api_id: Optional[str]
   - external_knowledge_api_name: Optional[str]
   - external_knowledge_api_endpoint: Optional[str]

4. `metadata_filtering_conditions.py` - MetadataFilteringConditions class with fields:
   - logical_operator: str
   - conditions: List[FilterCondition]

5. `filter_condition.py` - FilterCondition class with fields:
   - name: str
   - comparison_operator: str
   - value: Optional[Union[str, int, float]]

6. `dataset_info.py` - DatasetInfo class with comprehensive dataset fields based on API response structure
7. `tag_info.py` - TagInfo class for tag information
8. `metadata_info.py` - MetadataInfo class for metadata information

Migrate existing models from `dataset.py` and follow the existing project patterns in dify_oapi, ensure all models have builder methods and proper serialization support using Pydantic.
```

#### Step 2: Test Common Models
**Prompt:**
```
Create comprehensive unit tests for all common models created in Step 1. 

Create test file `tests/knowledge_base/v1/model/test_dataset_models.py` that covers:

1. Model instantiation and validation
2. Builder pattern functionality
3. Serialization/deserialization
4. Edge cases and validation errors
5. Optional field handling
6. Nested model relationships

Use pytest framework and ensure all tests pass with good coverage for the common model functionality.
```

### Phase 2: Dataset Management APIs (6 APIs)

#### Step 3: Dataset Request/Response Models
**Prompt:**
```
Create all request and response models for dataset management APIs in `dify_oapi/api/knowledge_base/v1/model/dataset/`.

Implement the following model files based on the API specifications:

1. `create_request.py` - CreateDatasetRequest with fields:
   - name: str (required)
   - description: Optional[str]
   - indexing_technique: Optional[str]
   - permission: Optional[str]
   - provider: Optional[str]
   - external_knowledge_api_id: Optional[str]
   - external_knowledge_id: Optional[str]
   - embedding_model: Optional[str]
   - embedding_model_provider: Optional[str]
   - retrieval_model: Optional[RetrievalModel]

2. `create_response.py` - CreateDatasetResponse using DatasetInfo
3. `list_request.py` - ListDatasetsRequest with pagination and filtering
4. `list_response.py` - ListDatasetsResponse with data array and pagination
5. `get_request.py` - GetDatasetRequest with dataset_id
6. `get_response.py` - GetDatasetResponse with full dataset details
7. `update_request.py` - UpdateDatasetRequest with partial update fields
8. `update_response.py` - UpdateDatasetResponse using DatasetInfo
9. `delete_request.py` - DeleteDatasetRequest with dataset_id
10. `delete_response.py` - DeleteDatasetResponse (empty for 204 response)
11. `retrieve_request.py` - RetrieveDatasetRequest with query and retrieval config
12. `retrieve_response.py` - RetrieveDatasetResponse with query and records

Use the common models created in Step 1 and follow existing project patterns for builder methods and validation.
```

#### Step 4: Test Dataset Models
**Prompt:**
```
Update the comprehensive unit tests in `tests/knowledge_base/v1/model/test_dataset_models.py` to include all dataset models.

Test all models created in Step 3, covering:
1. Model validation and required fields
2. Builder pattern functionality
3. Serialization/deserialization
4. Integration with common models
5. Edge cases and error handling

Use pytest framework and ensure all tests pass with good coverage.
```

#### Step 5: Dataset Resource Implementation
**Prompt:**
```
Implement the Dataset resource class in `dify_oapi/api/knowledge_base/v1/resource/dataset.py`.

Create a Dataset class with the following methods based on the API endpoints:
1. `create(request: CreateDatasetRequest, request_option: RequestOption) -> CreateDatasetResponse`
2. `acreate(request: CreateDatasetRequest, request_option: RequestOption) -> CreateDatasetResponse`
3. `list(request: ListDatasetsRequest, request_option: RequestOption) -> ListDatasetsResponse`
4. `alist(request: ListDatasetsRequest, request_option: RequestOption) -> ListDatasetsResponse`
5. `get(request: GetDatasetRequest, request_option: RequestOption) -> GetDatasetResponse`
6. `aget(request: GetDatasetRequest, request_option: RequestOption) -> GetDatasetResponse`
7. `update(request: UpdateDatasetRequest, request_option: RequestOption) -> UpdateDatasetResponse`
8. `aupdate(request: UpdateDatasetRequest, request_option: RequestOption) -> UpdateDatasetResponse`
9. `delete(request: DeleteDatasetRequest, request_option: RequestOption) -> DeleteDatasetResponse`
10. `adelete(request: DeleteDatasetRequest, request_option: RequestOption) -> DeleteDatasetResponse`
11. `retrieve(request: RetrieveDatasetRequest, request_option: RequestOption) -> RetrieveDatasetResponse`
12. `aretrieve(request: RetrieveDatasetRequest, request_option: RequestOption) -> RetrieveDatasetResponse`

Follow the existing transport patterns and HTTP method mappings. Map to correct endpoints:
- POST /v1/datasets (create)
- GET /v1/datasets (list)
- GET /v1/datasets/:dataset_id (get)
- PATCH /v1/datasets/:dataset_id (update)
- DELETE /v1/datasets/:dataset_id (delete)
- POST /v1/datasets/:dataset_id/retrieve (retrieve)

**Migration Tasks**:
- Create migration verification tests to compare new vs existing implementations
- Ensure `retrieve` method provides equivalent functionality to existing `hit_test` method
- After validation, remove old model files and update imports

Ensure proper error handling and response parsing.
```

#### Step 6: Test Dataset Resource and Migration Cleanup
**Prompt:**
```
Create comprehensive integration tests for the Dataset resource in `tests/knowledge_base/v1/resource/test_dataset_resource.py`.

Test all methods implemented in Step 5, including:
1. HTTP method and URL mapping verification
2. Request serialization and response deserialization
3. Error handling for various HTTP status codes
4. Both sync and async method variants
5. Mock API responses based on the API documentation
6. **Migration verification tests**: Compare behavior between new and existing implementations
7. **Compatibility tests**: Ensure `retrieve` method matches `hit_test` functionality

After all tests pass:
1. Remove old dataset model files (create_dataset_request.py, list_dataset_request.py, etc.)
2. Remove old hit_test method and related models
3. Update import statements throughout the codebase
4. Remove old test files for migrated functionality

Use pytest fixtures and mock responses to simulate API interactions. Ensure all tests pass.
```

### Phase 3: Metadata Management APIs (7 APIs)

#### Step 7: Metadata Request/Response Models
**Prompt:**
```
Create all request and response models for metadata management APIs in `dify_oapi/api/knowledge_base/v1/model/metadata/`.

Implement the following model files based on the API specifications:

1. `create_metadata_request.py` - CreateMetadataRequest with dataset_id, type, name
2. `create_metadata_response.py` - CreateMetadataResponse using MetadataInfo
3. `list_metadata_request.py` - ListMetadataRequest with dataset_id
4. `list_metadata_response.py` - ListMetadataResponse with doc_metadata array and built_in_field_enabled
5. `update_metadata_request.py` - UpdateMetadataRequest with dataset_id, metadata_id, name
6. `update_metadata_response.py` - UpdateMetadataResponse using MetadataInfo
7. `delete_metadata_request.py` - DeleteMetadataRequest with dataset_id, metadata_id
8. `delete_metadata_response.py` - DeleteMetadataResponse (empty for 204)
9. `toggle_builtin_metadata_request.py` - ToggleBuiltinMetadataRequest with dataset_id, action
10. `toggle_builtin_metadata_response.py` - ToggleBuiltinMetadataResponse with result field
11. `update_document_metadata_request.py` - UpdateDocumentMetadataRequest with operation_data
12. `update_document_metadata_response.py` - UpdateDocumentMetadataResponse with result field

Include proper validation and use common models where applicable.
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

Use pytest framework and ensure all tests pass with good coverage.
```

#### Step 9: Metadata Resource Implementation
**Prompt:**
```
Implement the Metadata resource class in `dify_oapi/api/knowledge_base/v1/resource/metadata.py`.

Create a Metadata class with the following methods based on the API endpoints:
1. `create(request: CreateMetadataRequest, request_option: RequestOption) -> CreateMetadataResponse`
2. `acreate(request: CreateMetadataRequest, request_option: RequestOption) -> CreateMetadataResponse`
3. `list(request: ListMetadataRequest, request_option: RequestOption) -> ListMetadataResponse`
4. `alist(request: ListMetadataRequest, request_option: RequestOption) -> ListMetadataResponse`
5. `update(request: UpdateMetadataRequest, request_option: RequestOption) -> UpdateMetadataResponse`
6. `aupdate(request: UpdateMetadataRequest, request_option: RequestOption) -> UpdateMetadataResponse`
7. `delete(request: DeleteMetadataRequest, request_option: RequestOption) -> DeleteMetadataResponse`
8. `adelete(request: DeleteMetadataRequest, request_option: RequestOption) -> DeleteMetadataResponse`
9. `toggle_builtin(request: ToggleBuiltinMetadataRequest, request_option: RequestOption) -> ToggleBuiltinMetadataResponse`
10. `atoggle_builtin(request: ToggleBuiltinMetadataRequest, request_option: RequestOption) -> ToggleBuiltinMetadataResponse`
11. `update_document(request: UpdateDocumentMetadataRequest, request_option: RequestOption) -> UpdateDocumentMetadataResponse`
12. `aupdate_document(request: UpdateDocumentMetadataRequest, request_option: RequestOption) -> UpdateDocumentMetadataResponse`

Map to correct endpoints:
- POST /datasets/{dataset_id}/metadata (create)
- GET /datasets/{dataset_id}/metadata (list)
- PATCH /datasets/{dataset_id}/metadata/{metadata_id} (update)
- DELETE /datasets/{dataset_id}/metadata/{metadata_id} (delete)
- POST /datasets/{dataset_id}/metadata/built-in/{action} (toggle_builtin)
- POST /datasets/{dataset_id}/documents/metadata (update_document)

Handle path parameters correctly and follow existing patterns.
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

Use pytest fixtures and mock responses. Ensure all tests pass.
```

### Phase 4: Tag Management APIs (7 APIs)

#### Step 11: Tag Request/Response Models
**Prompt:**
```
Create all request and response models for tag management APIs in `dify_oapi/api/knowledge_base/v1/model/tag/`.

Implement the following model files based on the API specifications:

1. `create_tag_request.py` - CreateTagRequest with name field
2. `create_tag_response.py` - CreateTagResponse using TagInfo
3. `list_tags_request.py` - ListTagsRequest (no parameters)
4. `list_tags_response.py` - ListTagsResponse with array of TagInfo
5. `update_tag_request.py` - UpdateTagRequest with name and tag_id
6. `update_tag_response.py` - UpdateTagResponse using TagInfo
7. `delete_tag_request.py` - DeleteTagRequest with tag_id
8. `delete_tag_response.py` - DeleteTagResponse with result field
9. `bind_tags_request.py` - BindTagsRequest with tag_ids array and target_id
10. `bind_tags_response.py` - BindTagsResponse with result field
11. `unbind_tag_request.py` - UnbindTagRequest with tag_id and target_id
12. `unbind_tag_response.py` - UnbindTagResponse with result field
13. `query_bound_tags_request.py` - QueryBoundTagsRequest with dataset_id
14. `query_bound_tags_response.py` - QueryBoundTagsResponse with data array and total

Include proper validation and use TagInfo from common models.
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

Use pytest framework and ensure all tests pass with good coverage.
```

#### Step 13: Tag Resource Implementation
**Prompt:**
```
Implement the Tag resource class in `dify_oapi/api/knowledge_base/v1/resource/tag.py`.

Create a Tag class with the following methods based on the API endpoints:
1. `create(request: CreateTagRequest, request_option: RequestOption) -> CreateTagResponse`
2. `acreate(request: CreateTagRequest, request_option: RequestOption) -> CreateTagResponse`
3. `list(request: ListTagsRequest, request_option: RequestOption) -> ListTagsResponse`
4. `alist(request: ListTagsRequest, request_option: RequestOption) -> ListTagsResponse`
5. `update(request: UpdateTagRequest, request_option: RequestOption) -> UpdateTagResponse`
6. `aupdate(request: UpdateTagRequest, request_option: RequestOption) -> UpdateTagResponse`
7. `delete(request: DeleteTagRequest, request_option: RequestOption) -> DeleteTagResponse`
8. `adelete(request: DeleteTagRequest, request_option: RequestOption) -> DeleteTagResponse`
9. `bind_tags(request: BindTagsRequest, request_option: RequestOption) -> BindTagsResponse`
10. `abind_tags(request: BindTagsRequest, request_option: RequestOption) -> BindTagsResponse`
11. `unbind_tag(request: UnbindTagRequest, request_option: RequestOption) -> UnbindTagResponse`
12. `aunbind_tag(request: UnbindTagRequest, request_option: RequestOption) -> UnbindTagResponse`
13. `query_bound(request: QueryBoundTagsRequest, request_option: RequestOption) -> QueryBoundTagsResponse`
14. `aquery_bound(request: QueryBoundTagsRequest, request_option: RequestOption) -> QueryBoundTagsResponse`

Map to correct endpoints:
- POST /datasets/tags (create)
- GET /datasets/tags (list)
- PATCH /datasets/tags (update)
- DELETE /datasets/tags (delete)
- POST /datasets/tags/binding (bind_tags)
- POST /datasets/tags/unbinding (unbind_tag)
- POST /datasets/{dataset_id}/tags (query_bound)

Handle different URL patterns correctly (global vs dataset-specific endpoints).
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

Use pytest fixtures and mock responses. Ensure all tests pass.
```

### Phase 5: Integration and Version Updates

#### Step 15: Update Version Integration
**Prompt:**
```
Update the knowledge_base v1 version integration to include the new resources.

Modify `dify_oapi/api/knowledge_base/v1/version.py` to:
1. Import the new Metadata and Tag resource classes
2. Add metadata and tag properties to the V1 class
3. Initialize them with the transport instance
4. Ensure backward compatibility with existing resources (document, segment)

Update any necessary import statements and maintain the existing API structure.
```

#### Step 16: Test Version Integration
**Prompt:**
```
Create integration tests for the updated V1 version class in `tests/knowledge_base/v1/integration/test_version_integration.py`.

Test:
1. All resources are properly initialized
2. Transport is correctly passed to all resources
3. New resources (dataset, metadata, tag) are accessible
4. Existing resources still work correctly
5. Client integration works end-to-end

Ensure the complete knowledge_base module works as expected.
```

### Phase 6: Documentation and Examples

#### Step 17: Create Usage Examples
**Prompt:**
```
Create comprehensive usage examples for the dataset management functionality in `examples/knowledge_base/`.

Create examples using resource-based directory structure:

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

Each example file should include:
- Simple, focused API call examples
- Both synchronous and asynchronous implementations
- Basic try-catch error handling
- Clear comments explaining each step
- Realistic but simple test data
- Educational value for developers
- Follow the existing example patterns in the project
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

Use pytest framework and ensure all examples are functional and educational.
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

Use realistic test data and scenarios. Ensure all 19 APIs work together correctly with proper mocking.
```

#### Step 20: Final Quality Assurance and Documentation
**Prompt:**
```
Perform final quality assurance and create comprehensive documentation.

Tasks:
1. Run all tests and ensure 100% pass rate
2. Verify code coverage meets project standards
3. Update API documentation with new functionality
4. Create migration guide for existing users
5. Update README with new dataset management features
6. Perform code review checklist:
   - Type hints are comprehensive
   - Error handling is consistent
   - Builder patterns work correctly
   - Async/sync parity is maintained
   - Documentation is complete

Create a final validation report confirming all requirements are met and all 19 dataset APIs are fully functional.
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

## Migration and Cleanup Notes

### Progressive Migration Strategy
- **Implementation Order**: Create new → Test new → Verify compatibility → Remove old
- **Cleanup Timing**: Remove old interfaces immediately after new implementation validation
- **Compatibility Verification**: Create tests to ensure behavioral consistency between old and new implementations
- **Special Cases**: `hit_test` → `retrieve` requires functional equivalence testing

### Files to Remove During Migration
**Existing Dataset Models** (after Step 6):
- `create_dataset_request.py` → replaced by `dataset/create_request.py`
- `create_dataset_request_body.py` → integrated into new structure
- `list_dataset_request.py` → replaced by `dataset/list_request.py`
- `delete_dataset_request.py` → replaced by `dataset/delete_request.py`
- `hit_test_request.py` → replaced by `dataset/retrieve_request.py`
- `hit_test_response.py` → replaced by `dataset/retrieve_response.py`
- Old `dataset.py` models → replaced by `dataset/dataset_info.py`

**Resource Methods** (after Step 6):
- Remove `hit_test` method from existing resource class
- Update method signatures to use new request/response models

### Implementation Guidelines
- Each implementation step should be followed immediately by its corresponding test step
- Use existing project patterns and maintain consistency with other API modules
- Ensure all 19 dataset APIs are fully functional and well-tested
- Prioritize type safety and developer experience throughout the implementation
- Follow the established directory structure and naming conventions
- All models should use Pydantic with builder patterns following existing project conventions
- Use `:parameter_name` format for path parameters to match existing patterns