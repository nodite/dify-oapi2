# Document API Implementation Plan

This document provides step-by-step prompts for implementing the Document API functionality in the dify-oapi knowledge_base module. Each implementation step is followed by a testing step to ensure code quality.

## Project Context

**Project**: Dify-OAPI Python SDK for interacting with Dify Service-API
**Module**: `dify_oapi/api/knowledge_base/v1/`
**Task**: Implement comprehensive document management functionality (10 APIs)
**Architecture**: Builder pattern with sync/async support, Pydantic validation, comprehensive type hints

## Implementation Steps

### Phase 1: Create Shared Document Models

#### Step 1.1: Create Document-Specific Shared Models

**Prompt:**
```
You are implementing the Document API for the dify-oapi Python SDK. Create the following shared model files in `dify_oapi/api/knowledge_base/v1/model/document/`:

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

3. **pre_processing_rule.py** - Preprocessing rule model with fields:
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
- Use proper type hints with `| None` for optional fields
- Follow existing code style patterns from dataset models
- Include comprehensive docstrings
- No Builder patterns needed for these shared models
```

#### Step 1.2: Test Shared Document Models

**Prompt:**
```
Create comprehensive unit tests for the shared document models created in Step 1.1. Create the test file `tests/knowledge_base/v1/model/document/test_shared_models.py`:

Requirements:
- Test all model classes for proper instantiation
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
    # Test with None values
    
def test_process_rule_validation() -> None:
    # Test process rule validation
```

Run tests with: `poetry run pytest tests/knowledge_base/v1/model/document/test_shared_models.py -v`
```

### Phase 2: Migrate Existing Document APIs (7 APIs)

#### Step 2.1: Create Create-by-Text API Models

**Prompt:**
```
You are migrating existing Document APIs to the new model structure. Create the create-by-text API models in `dify_oapi/api/knowledge_base/v1/model/document/`:

1. **create_by_text_request.py** - Request model:
   - Inherit from `BaseRequest`
   - Fields: dataset_id (str | None), request_body (CreateByTextRequestBody | None)
   - HTTP method: POST
   - URI: "/v1/datasets/:dataset_id/document/create-by-text"
   - Builder pattern with methods: dataset_id(), request_body()
   - Path parameter handling for dataset_id

2. **create_by_text_request_body.py** - Request body model:
   - Inherit from `pydantic.BaseModel`
   - Fields based on API spec:
     - name: str | None
     - text: str | None
     - indexing_technique: str | None
     - doc_form: str | None
     - doc_language: str | None
     - process_rule: ProcessRule | None
     - retrieval_model: RetrievalModel | None
     - embedding_model: str | None
     - embedding_model_provider: str | None
   - Builder pattern with methods for each field

3. **create_by_text_response.py** - Response model:
   - Inherit from `pydantic.BaseModel`
   - Fields: document (DocumentInfo | None), batch (str | None)
   - No builder pattern needed

Requirements:
- Follow MANDATORY code style rules from design document
- Use exact class naming: CreateByTextRequest, CreateByTextRequestBuilder, etc.
- Import shared models from same directory
- Include comprehensive type hints and docstrings
- Follow existing patterns from dataset models
```

#### Step 2.2: Test Create-by-Text API Models

**Prompt:**
```
Create comprehensive unit tests for the create-by-text API models. Create `tests/knowledge_base/v1/model/document/test_create_by_text_models.py`:

Requirements:
- Test CreateByTextRequest builder pattern
- Test CreateByTextRequestBody validation and builder
- Test CreateByTextResponse model
- Test path parameter handling
- Test request body serialization
- Verify HTTP method and URI configuration
- Include edge cases and validation errors
- All test methods must have proper type hints

Run tests with: `poetry run pytest tests/knowledge_base/v1/model/document/test_create_by_text_models.py -v`
```

#### Step 2.3: Create Create-by-File API Models

**Prompt:**
```
Create the create-by-file API models in `dify_oapi/api/knowledge_base/v1/model/document/`:

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
   - Builder pattern with methods for each field

3. **create_by_file_response.py** - Response model:
   - Same structure as create_by_text_response
   - Fields: document (DocumentInfo | None), batch (str | None)

Requirements:
- Handle multipart/form-data specifics
- Follow same patterns as create-by-text models
- Use exact class naming convention
```

#### Step 2.4: Test Create-by-File API Models

**Prompt:**
```
Create unit tests for create-by-file API models. Create `tests/knowledge_base/v1/model/document/test_create_by_file_models.py`:

Requirements:
- Test multipart/form-data handling
- Test file upload scenarios
- Test original_document_id handling for updates
- Test all builder methods and validation
- Include proper type hints for all test methods

Run tests: `poetry run pytest tests/knowledge_base/v1/model/document/test_create_by_file_models.py -v`
```

#### Step 2.5: Create Update-by-Text API Models

**Prompt:**
```
Create the update-by-text API models in `dify_oapi/api/knowledge_base/v1/model/document/`:

1. **update_by_text_request.py** - Request model:
   - Inherit from `BaseRequest`
   - Fields: dataset_id (str | None), document_id (str | None), request_body (UpdateByTextRequestBody | None)
   - HTTP method: POST
   - URI: "/v1/datasets/:dataset_id/documents/:document_id/update-by-text"
   - Builder with dataset_id(), document_id(), request_body() methods
   - Handle both path parameters

2. **update_by_text_request_body.py** - Request body model:
   - Inherit from `pydantic.BaseModel`
   - Fields (all optional for updates):
     - name: str | None
     - text: str | None
     - process_rule: ProcessRule | None
   - Builder pattern

3. **update_by_text_response.py** - Response model:
   - Fields: document (DocumentInfo | None), batch (str | None)

Requirements:
- Handle two path parameters (dataset_id and document_id)
- All request body fields are optional for updates
- Follow established patterns
```

#### Step 2.6: Test Update-by-Text API Models

**Prompt:**
```
Create unit tests for update-by-text API models. Create `tests/knowledge_base/v1/model/document/test_update_by_text_models.py`:

Requirements:
- Test dual path parameter handling
- Test optional field updates
- Test partial update scenarios
- Include proper type hints

Run tests: `poetry run pytest tests/knowledge_base/v1/model/document/test_update_by_text_models.py -v`
```

#### Step 2.7: Create Update-by-File API Models

**Prompt:**
```
Create the update-by-file API models in `dify_oapi/api/knowledge_base/v1/model/document/`:

1. **update_by_file_request.py** - Request model:
   - Inherit from `BaseRequest`
   - Fields: dataset_id (str | None), document_id (str | None), request_body (UpdateByFileRequestBody | None)
   - HTTP method: POST
   - URI: "/v1/datasets/:dataset_id/documents/:document_id/update-by-file"
   - Builder with dataset_id(), document_id(), request_body() methods

2. **update_by_file_request_body.py** - Request body model:
   - Inherit from `pydantic.BaseModel`
   - Fields (all optional):
     - name: str | None
     - file: str | None
     - process_rule: ProcessRule | None
   - Builder pattern

3. **update_by_file_response.py** - Response model:
   - Fields: document (DocumentInfo | None), batch (str | None)

Requirements:
- Handle multipart/form-data for file updates
- All fields optional for partial updates
- Dual path parameter support
```

#### Step 2.8: Test Update-by-File API Models

**Prompt:**
```
Create unit tests for update-by-file API models. Create `tests/knowledge_base/v1/model/document/test_update_by_file_models.py`:

Requirements:
- Test file update scenarios
- Test multipart handling
- Test partial updates
- Include proper type hints

Run tests: `poetry run pytest tests/knowledge_base/v1/model/document/test_update_by_file_models.py -v`
```

#### Step 2.9: Create Indexing Status API Models

**Prompt:**
```
Create the indexing status API models in `dify_oapi/api/knowledge_base/v1/model/document/`:

1. **indexing_status_request.py** - Request model:
   - Inherit from `BaseRequest`
   - Fields: dataset_id (str | None), batch (str | None)
   - HTTP method: GET
   - URI: "/v1/datasets/:dataset_id/documents/:batch/indexing-status"
   - Builder with dataset_id() and batch() methods
   - No request body needed (GET request)

2. **indexing_status_response.py** - Response model:
   - Inherit from `pydantic.BaseModel`
   - Fields: data (list[IndexingStatusInfo] | None)

Requirements:
- GET request pattern (no RequestBody)
- Handle batch parameter in path
- Response contains array of indexing status info
```

#### Step 2.10: Test Indexing Status API Models

**Prompt:**
```
Create unit tests for indexing status API models. Create `tests/knowledge_base/v1/model/document/test_indexing_status_models.py`:

Requirements:
- Test GET request pattern
- Test batch parameter handling
- Test response array handling
- Include proper type hints

Run tests: `poetry run pytest tests/knowledge_base/v1/model/document/test_indexing_status_models.py -v`
```

#### Step 2.11: Create Delete API Models

**Prompt:**
```
Create the delete API models in `dify_oapi/api/knowledge_base/v1/model/document/`:

1. **delete_request.py** - Request model:
   - Inherit from `BaseRequest`
   - Fields: dataset_id (str | None), document_id (str | None)
   - HTTP method: DELETE
   - URI: "/v1/datasets/:dataset_id/documents/:document_id"
   - Builder with dataset_id() and document_id() methods
   - No request body needed (DELETE request)

2. **delete_response.py** - Response model:
   - Inherit from `pydantic.BaseModel`
   - Empty response for 204 No Content
   - Can be minimal or empty class

Requirements:
- DELETE request pattern
- Dual path parameters
- Handle 204 No Content response
```

#### Step 2.12: Test Delete API Models

**Prompt:**
```
Create unit tests for delete API models. Create `tests/knowledge_base/v1/model/document/test_delete_models.py`:

Requirements:
- Test DELETE request pattern
- Test dual path parameter handling
- Test empty response handling
- Include proper type hints

Run tests: `poetry run pytest tests/knowledge_base/v1/model/document/test_delete_models.py -v`
```

#### Step 2.13: Create List API Models

**Prompt:**
```
Create the list API models in `dify_oapi/api/knowledge_base/v1/model/document/`:

1. **list_request.py** - Request model:
   - Inherit from `BaseRequest`
   - Fields: dataset_id (str | None)
   - HTTP method: GET
   - URI: "/v1/datasets/:dataset_id/documents"
   - Builder with dataset_id(), keyword(), page(), limit() methods
   - Query parameters: keyword, page, limit

2. **list_response.py** - Response model:
   - Inherit from `pydantic.BaseModel`
   - Fields:
     - data: list[DocumentInfo] | None
     - has_more: bool | None
     - limit: int | None
     - total: int | None
     - page: int | None

Requirements:
- GET request with query parameters
- Pagination support
- Array response with metadata
```

#### Step 2.14: Test List API Models

**Prompt:**
```
Create unit tests for list API models. Create `tests/knowledge_base/v1/model/document/test_list_models.py`:

Requirements:
- Test query parameter handling
- Test pagination parameters
- Test response array and metadata
- Include proper type hints

Run tests: `poetry run pytest tests/knowledge_base/v1/model/document/test_list_models.py -v`
```

### Phase 3: Create New Document APIs (3 APIs)

#### Step 3.1: Create Get Document API Models

**Prompt:**
```
Create the get document API models in `dify_oapi/api/knowledge_base/v1/model/document/`:

1. **get_request.py** - Request model:
   - Inherit from `BaseRequest`
   - Fields: dataset_id (str | None), document_id (str | None)
   - HTTP method: GET
   - URI: "/v1/datasets/:dataset_id/documents/:document_id"
   - Builder with dataset_id(), document_id(), metadata() methods
   - Query parameter: metadata (optional)

2. **get_response.py** - Response model:
   - Inherit from `pydantic.BaseModel`
   - Single DocumentInfo object with all detailed fields
   - Use DocumentInfo model directly

Requirements:
- GET request with dual path parameters
- Optional metadata query parameter
- Detailed document response
```

#### Step 3.2: Test Get Document API Models

**Prompt:**
```
Create unit tests for get document API models. Create `tests/knowledge_base/v1/model/document/test_get_models.py`:

Requirements:
- Test dual path parameters
- Test metadata query parameter
- Test detailed response handling
- Include proper type hints

Run tests: `poetry run pytest tests/knowledge_base/v1/model/document/test_get_models.py -v`
```

#### Step 3.3: Create Update Status API Models

**Prompt:**
```
Create the update status API models in `dify_oapi/api/knowledge_base/v1/model/document/`:

1. **update_status_request.py** - Request model:
   - Inherit from `BaseRequest`
   - Fields: dataset_id (str | None), action (str | None), request_body (UpdateStatusRequestBody | None)
   - HTTP method: PATCH
   - URI: "/v1/datasets/:dataset_id/documents/status/:action"
   - Builder with dataset_id(), action(), request_body() methods

2. **update_status_request_body.py** - Request body model:
   - Inherit from `pydantic.BaseModel`
   - Fields: document_ids (list[str] | None)
   - Builder pattern

3. **update_status_response.py** - Response model:
   - Inherit from `pydantic.BaseModel`
   - Fields: result (str | None)

Requirements:
- PATCH request with action parameter
- Batch operation on multiple documents
- Simple success response
```

#### Step 3.4: Test Update Status API Models

**Prompt:**
```
Create unit tests for update status API models. Create `tests/knowledge_base/v1/model/document/test_update_status_models.py`:

Requirements:
- Test action parameter handling
- Test batch document ID processing
- Test PATCH request pattern
- Include proper type hints

Run tests: `poetry run pytest tests/knowledge_base/v1/model/document/test_update_status_models.py -v`
```

#### Step 3.5: Create Get Upload File API Models

**Prompt:**
```
Create the get upload file API models in `dify_oapi/api/knowledge_base/v1/model/document/`:

1. **get_upload_file_request.py** - Request model:
   - Inherit from `BaseRequest`
   - Fields: dataset_id (str | None), document_id (str | None)
   - HTTP method: GET
   - URI: "/v1/datasets/:dataset_id/documents/:document_id/upload-file"
   - Builder with dataset_id() and document_id() methods

2. **get_upload_file_response.py** - Response model:
   - Inherit from `pydantic.BaseModel`
   - Use UploadFileInfo model directly or include fields:
     - id, name, size, extension, url, download_url, mime_type, created_by, created_at

Requirements:
- GET request with dual path parameters
- File information response
```

#### Step 3.6: Test Get Upload File API Models

**Prompt:**
```
Create unit tests for get upload file API models. Create `tests/knowledge_base/v1/model/document/test_get_upload_file_models.py`:

Requirements:
- Test dual path parameters
- Test file information response
- Include proper type hints

Run tests: `poetry run pytest tests/knowledge_base/v1/model/document/test_get_upload_file_models.py -v`
```

### Phase 4: Create Model Directory Structure

#### Step 4.1: Create Document Model __init__.py

**Prompt:**
```
Create the `dify_oapi/api/knowledge_base/v1/model/document/__init__.py` file that exports all document models:

Requirements:
- Import and export all Request, RequestBody, and Response classes
- Import and export all shared model classes
- Follow the pattern from dataset/__init__.py
- Use explicit imports (not *)
- Organize imports by category (requests, responses, shared models)
- Include proper type checking imports

Example structure:
```python
# Request models
from .create_by_text_request import CreateByTextRequest, CreateByTextRequestBuilder
from .create_by_text_request_body import CreateByTextRequestBody, CreateByTextRequestBodyBuilder
# ... other imports

# Response models  
from .create_by_text_response import CreateByTextResponse
# ... other imports

# Shared models
from .document_info import DocumentInfo
# ... other imports

__all__ = [
    # Request classes
    "CreateByTextRequest", "CreateByTextRequestBuilder",
    # ... all other classes
]
```
```

#### Step 4.2: Test Document Model Imports

**Prompt:**
```
Create a test to verify all document model imports work correctly. Create `tests/knowledge_base/v1/model/document/test_imports.py`:

Requirements:
- Test that all classes can be imported from the __init__.py
- Test that all classes are properly exported in __all__
- Verify no import errors
- Test instantiation of key classes

Run tests: `poetry run pytest tests/knowledge_base/v1/model/document/test_imports.py -v`
```

### Phase 5: Update Document Resource Class

#### Step 5.1: Update Document Resource Implementation

**Prompt:**
```
Update the existing `dify_oapi/api/knowledge_base/v1/resource/document.py` file to use the new model imports and add the 3 missing methods:

Requirements:
1. **Update existing method imports** - Replace all old model imports with new document model imports
2. **Add new methods**:
   - get() and aget() for document details
   - update_status() and aupdate_status() for batch status updates  
   - get_upload_file() and aget_upload_file() for file information

3. **Method signatures** (follow existing patterns):
```python
def get(self, request: GetRequest, option: RequestOption | None = None) -> GetResponse:
    return Transport.execute(self.config, request, unmarshal_as=GetResponse, option=option)

async def aget(self, request: GetRequest, option: RequestOption | None = None) -> GetResponse:
    return await ATransport.aexecute(self.config, request, unmarshal_as=GetResponse, option=option)
```

4. **Update existing method type hints** to use new model classes
5. **Maintain backward compatibility** - keep all existing method names and signatures
6. **Import all new models** from the document model directory

Requirements:
- Update all import statements to use new model structure
- Add 3 new methods with sync/async versions
- Maintain existing method names and signatures
- Follow established patterns for Transport.execute calls
```

#### Step 5.2: Test Updated Document Resource

**Prompt:**
```
Create comprehensive tests for the updated document resource. Create `tests/knowledge_base/v1/resource/test_document_resource.py`:

Requirements:
- Test all 10 methods (7 existing + 3 new)
- Test both sync and async versions of each method
- Mock Transport.execute and ATransport.aexecute calls
- Test proper request/response handling
- Test error scenarios
- Include proper type hints for all test methods

Test structure:
```python
def test_create_by_text_sync() -> None:
    # Test sync create_by_text method

async def test_create_by_text_async() -> None:
    # Test async create_by_text method

def test_get_sync() -> None:
    # Test new get method

# ... tests for all methods
```

Run tests: `poetry run pytest tests/knowledge_base/v1/resource/test_document_resource.py -v`
```

### Phase 6: Clean Up Legacy Files

#### Step 6.1: Remove Legacy Model Files

**Prompt:**
```
Remove all legacy document model files from `dify_oapi/api/knowledge_base/v1/model/` root directory:

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
- Verify no other files import these legacy models before removal
- Update any remaining import statements if found
- Ensure all tests still pass after removal
```

#### Step 6.2: Test Legacy Cleanup

**Prompt:**
```
Run comprehensive tests to ensure legacy cleanup didn't break anything:

Requirements:
- Run all document-related tests: `poetry run pytest tests/knowledge_base/v1/model/document/ -v`
- Run document resource tests: `poetry run pytest tests/knowledge_base/v1/resource/test_document_resource.py -v`
- Run any integration tests that use document functionality
- Verify no import errors throughout the codebase
- Check that all 10 document APIs work correctly

If any tests fail, identify and fix the issues before proceeding.
```

### Phase 7: Create Examples

#### Step 7.1: Create Document Examples Directory Structure

**Prompt:**
```
Create the examples directory structure and implement document examples:

Create directory: `examples/knowledge_base/document/`

Create the following example files (each with sync and async examples):

1. **create_by_text.py** - Examples for creating documents with text content
2. **create_by_file.py** - Examples for creating documents with file upload
3. **update_by_text.py** - Examples for updating documents with text
4. **update_by_file.py** - Examples for updating documents with files
5. **indexing_status.py** - Examples for checking indexing status
6. **delete.py** - Examples for deleting documents
7. **list.py** - Examples for listing documents
8. **get.py** - Examples for getting document details
9. **update_status.py** - Examples for batch status updates
10. **get_upload_file.py** - Examples for getting upload file info

Requirements for each example:
- Include both sync and async versions
- Use environment variables for configuration (DOMAIN, API_KEY, DATASET_ID, etc.)
- Include proper error handling with try-catch blocks
- Add educational comments explaining each step
- Use realistic test data
- Follow the pattern from existing dataset examples

Example structure:
```python
#!/usr/bin/env python3
"""
Document Create by Text Example
"""

import asyncio
import os
from dify_oapi.api.knowledge_base.v1.model.document.create_by_text_request import CreateByTextRequest
# ... other imports

def create_document_sync() -> None:
    """Create document synchronously."""
    try:
        # Implementation
    except Exception as e:
        print(f"Error: {e}")

async def create_document_async() -> None:
    """Create document asynchronously."""
    # Implementation

def main() -> None:
    # Check environment variables and run examples

if __name__ == "__main__":
    main()
```
```

#### Step 7.2: Test Document Examples

**Prompt:**
```
Test all document examples to ensure they work correctly:

Requirements:
- Set up test environment variables:
  ```bash
  export DOMAIN="https://api.dify.ai"
  export API_KEY="your-api-key"
  export DATASET_ID="your-dataset-id"
  ```
- Run each example file individually
- Verify both sync and async functions work
- Check error handling works properly
- Ensure examples are educational and easy to follow

Test commands:
```bash
poetry run python examples/knowledge_base/document/create_by_text.py
poetry run python examples/knowledge_base/document/create_by_file.py
# ... test all examples
```

Fix any issues found during testing.
```

### Phase 8: Integration Testing

#### Step 8.1: Create Integration Tests

**Prompt:**
```
Create comprehensive integration tests for the document API. Create `tests/knowledge_base/v1/integration/test_document_api_integration.py`:

Requirements:
- Test complete workflows (create → list → get → update → delete)
- Test both text and file-based operations
- Test error scenarios and edge cases
- Mock HTTP responses based on API documentation
- Test all 10 document APIs in realistic scenarios
- Include proper type hints for all test methods

Test scenarios:
1. Complete document lifecycle with text
2. Complete document lifecycle with file
3. Batch status operations
4. Indexing status monitoring
5. Error handling and validation

Use pytest fixtures for common setup and teardown.
```

#### Step 8.2: Run Integration Tests

**Prompt:**
```
Run the integration tests and ensure they all pass:

Requirements:
- Run integration tests: `poetry run pytest tests/knowledge_base/v1/integration/test_document_api_integration.py -v`
- Verify all test scenarios pass
- Check test coverage is comprehensive
- Fix any failing tests
- Ensure tests are reliable and repeatable

If tests fail, debug and fix the issues before proceeding.
```

### Phase 9: Final Validation

#### Step 9.1: Run Complete Test Suite

**Prompt:**
```
Run the complete test suite to ensure everything works correctly:

Commands to run:
```bash
# Run all document model tests
poetry run pytest tests/knowledge_base/v1/model/document/ -v

# Run document resource tests  
poetry run pytest tests/knowledge_base/v1/resource/test_document_resource.py -v

# Run integration tests
poetry run pytest tests/knowledge_base/v1/integration/test_document_api_integration.py -v

# Run any existing knowledge base tests to ensure no regressions
poetry run pytest tests/knowledge_base/ -v
```

Requirements:
- All tests must pass
- No import errors or missing dependencies
- Test coverage should be comprehensive
- Performance should be acceptable
```

#### Step 9.2: Update Documentation

**Prompt:**
```
Update the main examples README to include the new document examples:

Update `examples/README.md` to include:
- Document API examples section
- Description of each example file
- Usage instructions
- Environment variable requirements

Follow the existing format and style in the README.
```

## Summary

This implementation plan provides a comprehensive, step-by-step approach to implementing the Document API functionality. Each step includes specific requirements and is followed by testing to ensure code quality. The plan covers:

1. **Shared Models** - Create reusable document-specific models
2. **API Migration** - Migrate 7 existing APIs to new structure  
3. **New APIs** - Implement 3 missing APIs
4. **Resource Updates** - Update document resource class
5. **Legacy Cleanup** - Remove old model files
6. **Examples** - Create educational examples
7. **Testing** - Comprehensive unit and integration tests
8. **Validation** - Final testing and documentation

Following this plan will result in a complete, well-tested, and maintainable Document API implementation that follows the established patterns and provides full coverage of all 10 document management endpoints.