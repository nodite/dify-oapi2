# Document API Implementation Plan

This document provides step-by-step prompts for implementing Document API functionality in the dify-oapi knowledge_base module. Each implementation step is followed by a testing step to ensure code quality.

## Project Background

**Project**: Dify-OAPI Python SDK for interacting with Dify Service-API
**Module**: `dify_oapi/api/knowledge_base/v1/`
**Task**: Implement comprehensive document management functionality (10 APIs)
**Architecture**: Builder pattern, sync/async support, Pydantic validation, comprehensive type hints

## Implementation Steps

### Phase 1: Create Shared Document Models

#### Step 1.1: Create Document-Specific Shared Models

**Prompt:**
```
You are implementing Document API for the dify-oapi Python SDK. Create the following shared model files in `dify_oapi/api/knowledge_base/v1/model/document/`:

1. **document_info.py** - Document information model with fields:
   - id: str | None
   - position: int | None  
   - data_source_type: str | None
   - data_source_info: dict | None
   - dataset_process_rule_id: str | None
   - name: str | None
   - created_from: str | None
   - created_by: str | None
   - created_at: int | None
   - tokens: int | None
   - indexing_status: str | None
   - error: str | None
   - enabled: bool | None
   - disabled_at: int | None
   - disabled_by: str | None
   - archived: bool | None
   - display_status: str | None
   - word_count: int | None
   - hit_count: int | None
   - doc_form: str | None
   - doc_language: str | None
   - completed_at: int | None
   - updated_at: int | None
   - indexing_latency: float | None
   - segment_count: int | None
   - average_segment_length: int | None
   - dataset_process_rule: dict | None
   - document_process_rule: dict | None

2. **process_rule.py** - Processing rule model with fields:
   - mode: str | None
   - rules: dict | None

3. **pre_processing_rule.py** - Pre-processing rule model with fields:
   - id: str | None
   - enabled: bool | None

4. **segmentation.py** - Segmentation rule model with fields:
   - separator: str | None
   - max_tokens: int | None
   - chunk_overlap: int | None

5. **subchunk_segmentation.py** - Sub-chunk segmentation model with fields:
   - separator: str | None
   - max_tokens: int | None
   - chunk_overlap: int | None

6. **data_source_info.py** - Data source information model with fields:
   - upload_file_id: str | None
   - upload_file: dict | None

7. **upload_file_info.py** - Upload file information model with fields:
   - id: str | None
   - name: str | None
   - size: int | None
   - extension: str | None
   - url: str | None
   - download_url: str | None
   - mime_type: str | None
   - created_by: str | None
   - created_at: int | None

8. **indexing_status_info.py** - Indexing status information model with fields:
   - id: str | None
   - indexing_status: str | None
   - processing_started_at: float | None
   - parsing_completed_at: float | None
   - cleaning_completed_at: float | None
   - splitting_completed_at: float | None
   - completed_at: float | None
   - paused_at: float | None
   - error: str | None
   - stopped_at: float | None
   - completed_segments: int | None
   - total_segments: int | None

9. **retrieval_model.py** - Document-specific retrieval model with fields:
   - search_method: str | None
   - reranking_enable: bool | None
   - reranking_model: dict | None
   - top_k: int | None
   - score_threshold_enabled: bool | None
   - score_threshold: float | None

Requirements:
- All models MUST inherit from `pydantic.BaseModel`
- Use `| None` type hints for optional fields
- Follow existing dataset model code style patterns
- Include comprehensive docstrings
- These shared models do NOT need Builder patterns
```

#### Step 1.2: Test Shared Document Models

**Prompt:**
```
Create comprehensive unit tests for the shared document models created in Step 1.1. Create test file `tests/knowledge_base/v1/model/document/test_shared_models.py`:

Requirements:
- Test all model classes for correct instantiation
- Test field validation and type checking
- Test optional field handling (None values)
- Test model serialization/deserialization
- Use pytest framework
- Include proper type hints for all test methods
- Test edge cases and invalid data
- Ensure all tests pass before proceeding

Example test structure:
```python
def test_document_info_creation() -> None:
    # Test valid document info creation
    
def test_document_info_optional_fields() -> None:
    # Test None values
    
def test_process_rule_validation() -> None:
    # Test process rule validation
```

Run tests: `poetry run pytest tests/knowledge_base/v1/model/document/test_shared_models.py -v`
```

### Phase 2: Migrate Existing Document APIs (7 APIs)

#### Step 2.1: Create Text Creation API Models

**Prompt:**
```
You are migrating existing Document APIs to the new model structure. Create text creation API models in `dify_oapi/api/knowledge_base/v1/model/document/`:

1. **create_by_text_request.py** - Request model:
   - Inherit from `BaseRequest`
   - Fields: dataset_id (str | None), request_body (CreateByTextRequestBody | None)
   - HTTP method: POST
   - URI: "/v1/datasets/:dataset_id/document/create-by-text"
   - Builder pattern with methods: dataset_id(), request_body()
   - Handle dataset_id path parameter

2. **create_by_text_request_body.py** - Request body model:
   - Inherit from `pydantic.BaseModel`
   - Fields based on API specification:
     - name: str | None
     - text: str | None
     - indexing_technique: str | None
     - doc_form: str | None
     - doc_language: str | None
     - process_rule: ProcessRule | None
     - retrieval_model: RetrievalModel | None
     - embedding_model: str | None
     - embedding_model_provider: str | None
   - Builder pattern with method for each field

3. **create_by_text_response.py** - Response model:
   - Inherit from `pydantic.BaseModel`
   - Fields: document (DocumentInfo | None), batch (str | None)
   - No builder pattern needed

Requirements:
- Follow design document's mandatory code style rules
- Use exact class naming: CreateByTextRequest, CreateByTextRequestBuilder, etc.
- Import shared models from same directory
- Include comprehensive type hints and docstrings
- Follow existing dataset model patterns
```

#### Step 2.2: Test Text Creation API Models

**Prompt:**
```
Create comprehensive unit tests for text creation API models. Create `tests/knowledge_base/v1/model/document/test_create_by_text_models.py`:

Requirements:
- Test CreateByTextRequest builder pattern
- Test CreateByTextRequestBody validation and builder
- Test CreateByTextResponse model
- Test path parameter handling
- Test request body serialization
- Verify HTTP method and URI configuration
- Include edge cases and validation errors
- All test methods must have proper type hints

Run tests: `poetry run pytest tests/knowledge_base/v1/model/document/test_create_by_text_models.py -v`
```

#### Step 2.3: Create File Creation API Models

**Prompt:**
```
Create file creation API models in `dify_oapi/api/knowledge_base/v1/model/document/`:

1. **create_by_file_request.py** - Request model:
   - Inherit from `BaseRequest`
   - Fields: dataset_id (str | None), request_body (CreateByFileRequestBody | None)
   - HTTP method: POST
   - URI: "/v1/datasets/:dataset_id/document/create-by-file"
   - Builder with dataset_id() and request_body() methods

2. **create_by_file_request_body.py** - Request body model for multipart/form-data:
   - Inherit from `pydantic.BaseModel`
   - Fields:
     - data: str | None (JSON string for multipart data)
     - file: str | None (file path or content)
     - original_document_id: str | None
     - indexing_technique: str | None
     - doc_form: str | None
     - doc_language: str | None
     - process_rule: ProcessRule | None
     - retrieval_model: RetrievalModel | None
     - embedding_model: str | None
     - embedding_model_provider: str | None
   - Builder pattern with method for each field

3. **create_by_file_response.py** - Response model:
   - Same structure as create_by_text_response
   - Fields: document (DocumentInfo | None), batch (str | None)

Requirements:
- Handle multipart/form-data specifics
- Follow same patterns as create-by-text models
- Use exact class naming conventions
```

#### Step 2.4: Test File Creation API Models

**Prompt:**
```
Create unit tests for file creation API models. Create `tests/knowledge_base/v1/model/document/test_create_by_file_models.py`:

Requirements:
- Test multipart/form-data handling
- Test file upload scenarios
- Test original_document_id handling for updates
- Test all builder methods and validation
- Include proper type hints for all test methods

Run tests: `poetry run pytest tests/knowledge_base/v1/model/document/test_create_by_file_models.py -v`
```

#### Step 2.5: Create Text Update API Models

**Prompt:**
```
Create text update API models in `dify_oapi/api/knowledge_base/v1/model/document/`:

1. **update_by_text_request.py** - Request model:
   - Inherit from `BaseRequest`
   - Fields: dataset_id (str | None), document_id (str | None), request_body (UpdateByTextRequestBody | None)
   - HTTP method: POST
   - URI: "/v1/datasets/:dataset_id/documents/:document_id/update-by-text"
   - Builder with dataset_id(), document_id(), request_body() methods

2. **update_by_text_request_body.py** - Request body model:
   - Inherit from `pydantic.BaseModel`
   - Fields:
     - name: str | None
     - text: str | None
     - process_rule: ProcessRule | None
   - Builder pattern with method for each field

3. **update_by_text_response.py** - Response model:
   - Same structure as create responses
   - Fields: document (DocumentInfo | None), batch (str | None)

Requirements:
- Handle both dataset_id and document_id path parameters
- Follow established patterns from create models
- Include comprehensive type hints
```

#### Step 2.6: Test Text Update API Models

**Prompt:**
```
Create unit tests for text update API models. Create `tests/knowledge_base/v1/model/document/test_update_by_text_models.py`:

Requirements:
- Test dual path parameter handling (dataset_id, document_id)
- Test UpdateByTextRequestBody validation
- Test optional field handling in updates
- Include proper type hints for all test methods

Run tests: `poetry run pytest tests/knowledge_base/v1/model/document/test_update_by_text_models.py -v`
```

#### Step 2.7: Create File Update API Models

**Prompt:**
```
Create file update API models in `dify_oapi/api/knowledge_base/v1/model/document/`:

1. **update_by_file_request.py** - Request model:
   - Inherit from `BaseRequest`
   - Fields: dataset_id (str | None), document_id (str | None), request_body (UpdateByFileRequestBody | None)
   - HTTP method: POST
   - URI: "/v1/datasets/:dataset_id/documents/:document_id/update-by-file"
   - Builder with dataset_id(), document_id(), request_body() methods

2. **update_by_file_request_body.py** - Request body model for multipart/form-data:
   - Inherit from `pydantic.BaseModel`
   - Fields:
     - name: str | None
     - file: str | None
     - process_rule: ProcessRule | None
   - Builder pattern with method for each field

3. **update_by_file_response.py** - Response model:
   - Same structure as other responses
   - Fields: document (DocumentInfo | None), batch (str | None)

Requirements:
- Handle multipart/form-data for file updates
- Support dual path parameters
- Follow established patterns
```

#### Step 2.8: Test File Update API Models

**Prompt:**
```
Create unit tests for file update API models. Create `tests/knowledge_base/v1/model/document/test_update_by_file_models.py`:

Requirements:
- Test multipart/form-data handling for updates
- Test dual path parameter configuration
- Test file replacement scenarios
- Include proper type hints for all test methods

Run tests: `poetry run pytest tests/knowledge_base/v1/model/document/test_update_by_file_models.py -v`
```

#### Step 2.9: Create Indexing Status API Models

**Prompt:**
```
Create indexing status API models in `dify_oapi/api/knowledge_base/v1/model/document/`:

1. **indexing_status_request.py** - Request model:
   - Inherit from `BaseRequest`
   - Fields: dataset_id (str | None), batch (str | None)
   - HTTP method: GET
   - URI: "/v1/datasets/:dataset_id/documents/:batch/indexing-status"
   - Builder with dataset_id() and batch() methods

2. **indexing_status_response.py** - Response model:
   - Inherit from `pydantic.BaseModel`
   - Fields: data (list[IndexingStatusInfo] | None)

Requirements:
- Handle batch parameter in path
- Use IndexingStatusInfo from shared models
- Follow GET request patterns
```

#### Step 2.10: Test Indexing Status API Models

**Prompt:**
```
Create unit tests for indexing status API models. Create `tests/knowledge_base/v1/model/document/test_indexing_status_models.py`:

Requirements:
- Test batch parameter handling
- Test response data array structure
- Test IndexingStatusInfo integration
- Include proper type hints for all test methods

Run tests: `poetry run pytest tests/knowledge_base/v1/model/document/test_indexing_status_models.py -v`
```

#### Step 2.11: Create Delete API Models

**Prompt:**
```
Create delete API models in `dify_oapi/api/knowledge_base/v1/model/document/`:

1. **delete_request.py** - Request model:
   - Inherit from `BaseRequest`
   - Fields: dataset_id (str | None), document_id (str | None)
   - HTTP method: DELETE
   - URI: "/v1/datasets/:dataset_id/documents/:document_id"
   - Builder with dataset_id() and document_id() methods

2. **delete_response.py** - Response model:
   - Inherit from `pydantic.BaseModel`
   - Empty response for 204 No Content

Requirements:
- Handle DELETE method with dual path parameters
- Support 204 No Content response
- Follow established patterns
```

#### Step 2.12: Test Delete API Models

**Prompt:**
```
Create unit tests for delete API models. Create `tests/knowledge_base/v1/model/document/test_delete_models.py`:

Requirements:
- Test DELETE method configuration
- Test dual path parameter handling
- Test empty response handling
- Include proper type hints for all test methods

Run tests: `poetry run pytest tests/knowledge_base/v1/model/document/test_delete_models.py -v`
```

#### Step 2.13: Create List API Models

**Prompt:**
```
Create list API models in `dify_oapi/api/knowledge_base/v1/model/document/`:

1. **list_request.py** - Request model:
   - Inherit from `BaseRequest`
   - Fields: dataset_id (str | None)
   - HTTP method: GET
   - URI: "/v1/datasets/:dataset_id/documents"
   - Builder with dataset_id(), keyword(), page(), limit() methods
   - Handle query parameters: keyword, page, limit

2. **list_response.py** - Response model:
   - Inherit from `pydantic.BaseModel`
   - Fields:
     - data: list[DocumentInfo] | None
     - has_more: bool | None
     - limit: int | None
     - total: int | None
     - page: int | None

Requirements:
- Handle query parameters with add_query()
- Use DocumentInfo from shared models
- Follow pagination patterns
```

#### Step 2.14: Test List API Models

**Prompt:**
```
Create unit tests for list API models. Create `tests/knowledge_base/v1/model/document/test_list_models.py`:

Requirements:
- Test query parameter handling (keyword, page, limit)
- Test pagination response structure
- Test DocumentInfo array integration
- Include proper type hints for all test methods

Run tests: `poetry run pytest tests/knowledge_base/v1/model/document/test_list_models.py -v`
```

### Phase 3: Implement New Document APIs (3 APIs)

#### Step 3.1: Create Get Document API Models

**Prompt:**
```
Create get document API models in `dify_oapi/api/knowledge_base/v1/model/document/`:

1. **get_request.py** - Request model:
   - Inherit from `BaseRequest`
   - Fields: dataset_id (str | None), document_id (str | None)
   - HTTP method: GET
   - URI: "/v1/datasets/:dataset_id/documents/:document_id"
   - Builder with dataset_id(), document_id(), metadata() methods
   - Handle metadata query parameter

2. **get_response.py** - Response model:
   - Inherit from `DocumentInfo` and `BaseResponse` (multiple inheritance)
   - This allows the response to have all DocumentInfo fields plus error handling

Requirements:
- Handle metadata query parameter
- Use multiple inheritance pattern for response
- Follow GET request patterns with dual path parameters
```

#### Step 3.2: Test Get Document API Models

**Prompt:**
```
Create unit tests for get document API models. Create `tests/knowledge_base/v1/model/document/test_get_models.py`:

Requirements:
- Test dual path parameter handling
- Test metadata query parameter
- Test multiple inheritance in response model
- Test DocumentInfo field inheritance
- Include proper type hints for all test methods

Run tests: `poetry run pytest tests/knowledge_base/v1/model/document/test_get_models.py -v`
```

#### Step 3.3: Create Update Status API Models

**Prompt:**
```
Create update status API models in `dify_oapi/api/knowledge_base/v1/model/document/`:

1. **update_status_request.py** - Request model:
   - Inherit from `BaseRequest`
   - Fields: dataset_id (str | None), action (str | None), request_body (UpdateStatusRequestBody | None)
   - HTTP method: PATCH
   - URI: "/v1/datasets/:dataset_id/documents/status/:action"
   - Builder with dataset_id(), action(), request_body() methods

2. **update_status_request_body.py** - Request body model:
   - Inherit from `pydantic.BaseModel`
   - Fields: document_ids (list[str] | None)
   - Builder pattern with document_ids() method

3. **update_status_response.py** - Response model:
   - Inherit from `pydantic.BaseModel`
   - Fields: result (str | None)

Requirements:
- Handle action path parameter (enable, disable, archive, un_archive)
- Support batch document ID operations
- Follow PATCH request patterns
```

#### Step 3.4: Test Update Status API Models

**Prompt:**
```
Create unit tests for update status API models. Create `tests/knowledge_base/v1/model/document/test_update_status_models.py`:

Requirements:
- Test action parameter validation
- Test document_ids array handling
- Test PATCH method configuration
- Test batch operation scenarios
- Include proper type hints for all test methods

Run tests: `poetry run pytest tests/knowledge_base/v1/model/document/test_update_status_models.py -v`
```

#### Step 3.5: Create Get Upload File API Models

**Prompt:**
```
Create get upload file API models in `dify_oapi/api/knowledge_base/v1/model/document/`:

1. **get_upload_file_request.py** - Request model:
   - Inherit from `BaseRequest`
   - Fields: dataset_id (str | None), document_id (str | None)
   - HTTP method: GET
   - URI: "/v1/datasets/:dataset_id/documents/:document_id/upload-file"
   - Builder with dataset_id() and document_id() methods

2. **get_upload_file_response.py** - Response model:
   - Inherit from `UploadFileInfo` and `BaseResponse` (multiple inheritance)
   - This allows the response to have all UploadFileInfo fields plus error handling

Requirements:
- Handle dual path parameters
- Use multiple inheritance pattern for response
- Use UploadFileInfo from shared models
```

#### Step 3.6: Test Get Upload File API Models

**Prompt:**
```
Create unit tests for get upload file API models. Create `tests/knowledge_base/v1/model/document/test_get_upload_file_models.py`:

Requirements:
- Test dual path parameter handling
- Test multiple inheritance in response model
- Test UploadFileInfo field inheritance
- Include proper type hints for all test methods

Run tests: `poetry run pytest tests/knowledge_base/v1/model/document/test_get_upload_file_models.py -v`
```

### Phase 4: Update Resource Class

#### Step 4.1: Update Document Resource Class

**Prompt:**
```
Update the document resource class in `dify_oapi/api/knowledge_base/v1/resource/document.py`:

1. **Update Imports**: Replace all old model imports with new document model imports
2. **Add New Methods**: Implement the 3 missing methods:
   - get() - Get document details
   - update_status() - Batch update document status  
   - get_upload_file() - Get upload file information
3. **Update Existing Methods**: Update all existing method implementations to use new models

Requirements:
- Each method must have both sync and async versions
- Use Transport.execute() for sync and ATransport.aexecute() for async
- Follow existing method patterns in the class
- Import all new models from model/document/ directory
- Maintain backward compatibility with method names
- Include proper type hints and docstrings

Example method structure:
```python
def get(self, request: GetRequest, request_option: RequestOption) -> GetResponse:
    return Transport.execute(self.config, request, unmarshal_as=GetResponse, option=request_option)

async def aget(self, request: GetRequest, request_option: RequestOption) -> GetResponse:
    return await ATransport.aexecute(self.config, request, unmarshal_as=GetResponse, option=request_option)
```
```

#### Step 4.2: Test Updated Document Resource Class

**Prompt:**
```
Create comprehensive unit tests for the updated document resource class. Create `tests/knowledge_base/v1/resource/test_document_resource.py`:

Requirements:
- Test all 10 methods (7 existing + 3 new)
- Test both sync and async versions of each method
- Mock Transport.execute() and ATransport.aexecute() calls
- Verify correct request/response model usage
- Test error handling scenarios
- Include proper type hints for all test methods

Test structure:
```python
def test_create_by_text_sync() -> None:
    # Test sync create_by_text method

def test_create_by_text_async() -> None:
    # Test async acreate_by_text method

def test_get_sync() -> None:
    # Test new get method

def test_get_async() -> None:
    # Test new aget method
```

Run tests: `poetry run pytest tests/knowledge_base/v1/resource/test_document_resource.py -v`
```

### Phase 5: Clean Up Legacy Models

#### Step 5.1: Remove Legacy Model Files

**Prompt:**
```
Remove all legacy document model files from `dify_oapi/api/knowledge_base/v1/model/`:

Files to remove:
- create_document_by_file_request_body_data.py
- create_document_by_file_request_body.py
- create_document_by_file_request.py
- create_document_by_text_request_body.py
- create_document_by_text_request.py
- create_document_response.py
- delete_document_request.py
- delete_document_response.py
- document_request_pre_processing_rule.py
- document_request_process_rule.py
- document_request_rules.py
- document_request_segmentation.py
- document.py
- index_status_request.py
- index_status_response.py
- list_document_request.py
- list_document_response.py
- update_document_by_file_request_body_data.py
- update_document_by_file_request_body.py
- update_document_by_file_request.py
- update_document_by_text_request_body.py
- update_document_by_text_request.py
- update_document_response.py

Requirements:
- Verify no other files import these legacy models before deletion
- Update any remaining import statements to use new models
- Ensure all tests pass after cleanup
```

#### Step 5.2: Verify Legacy Cleanup

**Prompt:**
```
Verify that legacy model cleanup is complete:

1. **Search for Legacy Imports**: Search the entire codebase for any remaining imports of deleted model files
2. **Update Import Statements**: Replace any found legacy imports with new model imports
3. **Run Full Test Suite**: Execute all tests to ensure no broken imports
4. **Verify Functionality**: Test that all document operations still work correctly

Commands to run:
```bash
# Search for potential legacy imports
grep -r "from.*knowledge_base.*model.*document" dify_oapi/
grep -r "import.*document" dify_oapi/api/knowledge_base/

# Run full test suite
poetry run pytest tests/knowledge_base/ -v

# Run specific document tests
poetry run pytest tests/knowledge_base/v1/model/document/ -v
poetry run pytest tests/knowledge_base/v1/resource/test_document_resource.py -v
```

Requirements:
- All tests must pass
- No import errors should occur
- Document functionality should remain intact
```

### Phase 6: Create Examples

#### Step 6.1: Create Basic Document Examples

**Prompt:**
```
Create document API examples in `examples/knowledge_base/document/`. Follow the minimalism principles from other knowledge base examples:

Create these files:
1. **create_by_text.py** - Create document by text (sync + async)
2. **create_by_file.py** - Create document by file (sync + async)
3. **list.py** - List documents (sync + async)
4. **get.py** - Get document details (sync + async)
5. **delete.py** - Delete document (sync + async)

Requirements:
- MANDATORY: Validate API_KEY and DATASET_ID environment variables at function start
- MANDATORY: Use "[Example]" prefix for all created resources
- MANDATORY: Apply code minimalism - write only essential code
- Include both sync and async examples in each file
- Use try-catch error handling
- Follow patterns from other knowledge base examples
- Include proper type hints

Environment variable validation pattern:
```python
def create_document_by_text_sync() -> None:
    try:
        # Check required environment variables (MUST be first)
        api_key = os.getenv("API_KEY")
        if not api_key:
            raise ValueError("API_KEY environment variable is required")
        
        dataset_id = os.getenv("DATASET_ID")
        if not dataset_id:
            raise ValueError("DATASET_ID environment variable is required")
        
        # Initialize client and continue...
```
```

#### Step 6.2: Test Basic Document Examples

**Prompt:**
```
Test the basic document examples created in Step 6.1:

1. **Set Environment Variables**:
   ```bash
   export API_KEY="your-api-key"
   export DATASET_ID="your-dataset-id"
   export DOMAIN="https://api.dify.ai"
   ```

2. **Run Examples**:
   ```bash
   cd examples/knowledge_base/document/
   python create_by_text.py
   python create_by_file.py
   python list.py
   python get.py
   python delete.py
   ```

3. **Verify**:
   - All examples run without errors
   - Resources are created with "[Example]" prefix
   - Both sync and async functions work correctly
   - Environment variable validation works
   - Error handling functions properly

Requirements:
- All examples must execute successfully
- No runtime errors should occur
- Resources should be properly created and cleaned up
```

#### Step 6.3: Create Advanced Document Examples

**Prompt:**
```
Create advanced document API examples:

Create these files:
6. **update_by_text.py** - Update document by text (sync + async)
7. **update_by_file.py** - Update document by file (sync + async)
8. **indexing_status.py** - Get indexing status (sync + async)
9. **update_status.py** - Update document status (sync + async)
10. **get_upload_file.py** - Get upload file info (sync + async)

Requirements:
- Follow same patterns as basic examples
- MANDATORY: Environment variable validation at function start
- MANDATORY: "[Example]" prefix for resources
- MANDATORY: Code minimalism principles
- Include both sync and async examples
- Handle document updates and status changes
- Test batch operations for update_status
- Include proper error handling
```

#### Step 6.4: Test Advanced Document Examples

**Prompt:**
```
Test the advanced document examples created in Step 6.3:

1. **Run Advanced Examples**:
   ```bash
   cd examples/knowledge_base/document/
   python update_by_text.py
   python update_by_file.py
   python indexing_status.py
   python update_status.py
   python get_upload_file.py
   ```

2. **Integration Testing**:
   - Create a document using create_by_text.py
   - Update it using update_by_text.py
   - Check status using indexing_status.py
   - Modify status using update_status.py
   - Get file info using get_upload_file.py
   - Clean up using delete.py

Requirements:
- All advanced examples must work correctly
- Integration workflow should complete successfully
- Status operations should work on multiple documents
- File operations should handle uploads properly
```

#### Step 6.5: Create Example Documentation

**Prompt:**
```
Create documentation for document examples in `examples/knowledge_base/document/README.md`:

Include:
1. **Overview** - Brief description of document management capabilities
2. **Setup** - Environment variable requirements
3. **Basic Examples** - Description of create, list, get, delete examples
4. **Advanced Examples** - Description of update, status, and file examples
5. **Integration Workflow** - Step-by-step example of complete document lifecycle
6. **Safety Features** - Explanation of "[Example]" prefix and validation
7. **Troubleshooting** - Common issues and solutions

Requirements:
- Follow documentation style from other knowledge base examples
- Include code snippets for key operations
- Explain environment variable setup
- Document safety measures and best practices
- Keep documentation concise but comprehensive
```

### Phase 7: Integration Testing

#### Step 7.1: Create Integration Tests

**Prompt:**
```
Create comprehensive integration tests in `tests/knowledge_base/v1/integration/test_document_api_integration.py`:

Test scenarios:
1. **Complete Document Lifecycle**:
   - Create document by text
   - Get document details
   - Update document content
   - Check indexing status
   - Update document status
   - Delete document

2. **File Operations**:
   - Create document by file
   - Update document by file
   - Get upload file information
   - Verify file handling

3. **Batch Operations**:
   - Create multiple documents
   - List documents with pagination
   - Batch status updates
   - Batch cleanup

4. **Error Scenarios**:
   - Invalid dataset IDs
   - Missing documents
   - Invalid file formats
   - Network errors

Requirements:
- Use mock responses for API calls
- Test both sync and async operations
- Verify request/response model handling
- Include comprehensive error testing
- Use proper type hints throughout
```

#### Step 7.2: Run Integration Tests

**Prompt:**
```
Execute integration tests and verify results:

Commands:
```bash
# Run document integration tests
poetry run pytest tests/knowledge_base/v1/integration/test_document_api_integration.py -v

# Run all document-related tests
poetry run pytest tests/knowledge_base/v1/model/document/ -v
poetry run pytest tests/knowledge_base/v1/resource/test_document_resource.py -v

# Run full knowledge base test suite
poetry run pytest tests/knowledge_base/ -v
```

Verification:
- All integration tests pass
- No model validation errors
- Resource methods work correctly
- Error handling functions properly
- Both sync and async operations succeed

Requirements:
- 100% test pass rate
- No import or runtime errors
- Comprehensive test coverage
- Proper error handling validation
```

### Phase 8: Final Validation

#### Step 8.1: Complete System Test

**Prompt:**
```
Perform final system validation:

1. **Model Validation**:
   - All 10 API models are correctly implemented
   - Shared models work across all APIs
   - Builder patterns function properly
   - Type hints are comprehensive

2. **Resource Validation**:
   - All 10 resource methods are implemented
   - Both sync and async versions work
   - Error handling is consistent
   - Import statements are correct

3. **Example Validation**:
   - All 10 examples run successfully
   - Environment variable validation works
   - "[Example]" prefix is used consistently
   - Code minimalism is applied

4. **Test Validation**:
   - All unit tests pass
   - Integration tests succeed
   - No legacy code remains
   - Full test coverage achieved

Commands to run:
```bash
# Full test suite
poetry run pytest tests/ -v

# Specific document tests
poetry run pytest tests/knowledge_base/v1/model/document/ -v
poetry run pytest tests/knowledge_base/v1/resource/test_document_resource.py -v
poetry run pytest tests/knowledge_base/v1/integration/test_document_api_integration.py -v

# Example validation
cd examples/knowledge_base/document/
python -m pytest --doctest-modules *.py
```

Requirements:
- All tests must pass
- No errors in examples
- Complete API coverage
- Clean codebase with no legacy files
```

#### Step 8.2: Documentation and Cleanup

**Prompt:**
```
Complete final documentation and cleanup:

1. **Update API Documentation**:
   - Update any references to old model names
   - Document new API methods (get, update_status, get_upload_file)
   - Verify all examples are referenced correctly

2. **Code Quality Check**:
   - Run linting tools (ruff, mypy)
   - Verify type hints are complete
   - Check for any unused imports
   - Ensure consistent code style

3. **Performance Verification**:
   - Test API response times
   - Verify memory usage is reasonable
   - Check for any performance regressions

Commands:
```bash
# Code quality checks
poetry run ruff check dify_oapi/api/knowledge_base/v1/model/document/
poetry run ruff format dify_oapi/api/knowledge_base/v1/model/document/
poetry run mypy dify_oapi/api/knowledge_base/v1/model/document/

# Final test run
poetry run pytest tests/knowledge_base/ -v --cov=dify_oapi.api.knowledge_base
```

Requirements:
- All quality checks pass
- Documentation is up to date
- Performance is acceptable
- Code is production-ready
```

## Summary

This implementation plan provides a comprehensive, step-by-step approach to implementing all 10 Document API endpoints in the dify-oapi knowledge_base module. Each step includes specific requirements and is followed by a testing step to ensure code quality and functionality.

The plan follows the established architecture patterns while ensuring:
- Complete API coverage (10 endpoints)
- Consistent code style and patterns
- Comprehensive testing at each step
- Clean migration from legacy models
- Practical examples for all operations
- Proper error handling and validation

By following this plan, you will have a fully functional, well-tested, and maintainable document management system that integrates seamlessly with the existing dify-oapi architecture.