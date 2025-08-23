# Segment API Implementation Plan - AI Prompts

This document provides step-by-step prompts for implementing the complete segment management functionality in the dify-oapi knowledge_base module. Each step includes implementation and testing phases to ensure code quality.

## Overview

The implementation covers 9 segment-related APIs organized into two main categories:
- **Core Segment Operations**: 5 APIs (create, list, get, update, delete)
- **Child Chunk Operations**: 4 APIs (create, list, update, delete child chunks)

## Implementation Steps

### Phase 1: Common Models Foundation

#### Step 1: Create Shared Segment Models
**Prompt:**
```
Create the shared common models for the segment API implementation in `dify_oapi/api/knowledge_base/v1/model/segment/`. 

Implement the following model files with proper type hints, builder patterns, and Pydantic validation:

1. `segment_info.py` - SegmentInfo class with fields:
   - id: str | None = None
   - position: int | None = None
   - document_id: str | None = None
   - content: str | None = None
   - answer: str | None = None
   - word_count: int | None = None
   - tokens: int | None = None
   - keywords: list[str] | None = None
   - index_node_id: str | None = None
   - index_node_hash: str | None = None
   - hit_count: int | None = None
   - enabled: bool | None = None
   - disabled_at: int | None = None
   - disabled_by: str | None = None
   - status: str | None = None
   - created_by: str | None = None
   - created_at: int | None = None
   - indexing_at: int | None = None
   - completed_at: int | None = None
   - error: str | None = None
   - stopped_at: int | None = None

2. `child_chunk_info.py` - ChildChunkInfo class with fields:
   - id: str | None = None
   - segment_id: str | None = None
   - content: str | None = None
   - word_count: int | None = None
   - tokens: int | None = None
   - index_node_id: str | None = None
   - index_node_hash: str | None = None
   - status: str | None = None
   - created_by: str | None = None
   - created_at: int | None = None
   - indexing_at: int | None = None
   - completed_at: int | None = None
   - error: str | None = None
   - stopped_at: int | None = None

3. `segment_data.py` - SegmentData class for update operations with fields:
   - content: str | None = None
   - answer: str | None = None
   - keywords: list[str] | None = None
   - enabled: bool | None = None
   - regenerate_child_chunks: bool | None = None

MANDATORY REQUIREMENTS:
- ALL classes MUST inherit from `pydantic.BaseModel`
- ALL classes MUST include `from __future__ import annotations` at the top
- ALL classes MUST have builder patterns with proper type hints
- Use `@staticmethod` decorator for builder() methods
- Builder classes MUST follow naming pattern: ClassNameBuilder
- All fields MUST use proper type hints with `| None = None` for optional fields
- Follow existing project patterns in dify_oapi for consistency
- Builder methods must return the builder instance for method chaining
```

#### Step 2: Test Common Models
**Prompt:**
```
Create comprehensive unit tests for all common models created in Step 1. 

Create test file `tests/knowledge_base/v1/model/test_segment_models.py` that covers:

1. Model instantiation and validation
2. Builder pattern functionality for all models
3. Serialization/deserialization using Pydantic
4. Edge cases and validation errors
5. Optional field handling
6. Array field validation (keywords)

MANDATORY REQUIREMENTS:
- ALL test methods MUST include proper type annotations for parameters and return types
- Use `-> None` for test method return types
- Import `typing.Any` for complex mock objects
- Use pytest framework with proper fixtures
- Test both direct instantiation and builder pattern approaches
- Verify method chaining works correctly in builders
- Test serialization with `model_dump()` method
- Ensure all tests pass with good coverage (>90%)

Example test structure:
```python
# ===== SHARED SEGMENT MODELS TESTS =====

def test_segment_info_creation() -> None:
    # Test valid segment info creation

def test_segment_info_builder_pattern() -> None:
    # Test builder pattern functionality

def test_child_chunk_info_validation() -> None:
    # Test child chunk info validation

def test_segment_data_builder() -> None:
    # Test segment data builder pattern
```

Note: This file will be extended in subsequent steps to include all API model tests.
```

### Phase 2: Core Segment Operations (5 APIs)

#### Step 3: Create Segment Request/Response Models
**Prompt:**
```
Create all request and response models for core segment operations in `dify_oapi/api/knowledge_base/v1/model/segment/` following MANDATORY code style rules.

Implement the following model files with STRICT adherence to patterns:

**POST Request Models (with RequestBody)**:
1. `create_request.py` - CreateRequest + CreateRequestBuilder (inherits BaseRequest)
2. `create_request_body.py` - CreateRequestBody + CreateRequestBodyBuilder (inherits BaseModel)
   Fields: segments (list[SegmentInfo])

3. `update_request.py` - UpdateRequest + UpdateRequestBuilder (inherits BaseRequest)
4. `update_request_body.py` - UpdateRequestBody + UpdateRequestBodyBuilder (inherits BaseModel)
   Fields: segment (SegmentData)

**GET Request Models (no RequestBody)**:
5. `list_request.py` - ListRequest + ListRequestBuilder (inherits BaseRequest)
   Query params: keyword, status, page, limit
   Path params: dataset_id, document_id

6. `get_request.py` - GetRequest + GetRequestBuilder (inherits BaseRequest)
   Path params: dataset_id, document_id, segment_id

**DELETE Request Models (no RequestBody)**:
7. `delete_request.py` - DeleteRequest + DeleteRequestBuilder (inherits BaseRequest)
   Path params: dataset_id, document_id, segment_id

**Response Models**:
8. `create_response.py` - CreateResponse (inherits BaseResponse) with data, doc_form fields
9. `list_response.py` - ListResponse (inherits BaseResponse) with data, doc_form, has_more, limit, total, page fields
10. `get_response.py` - GetResponse (inherits BaseResponse) with data, doc_form fields
11. `update_response.py` - UpdateResponse (inherits BaseResponse) with data, doc_form fields
12. `delete_response.py` - DeleteResponse (inherits BaseResponse) - empty for 204

CRITICAL REQUIREMENTS:
- ALL class names MUST match file names exactly (NO module prefixes)
- Request classes MUST inherit from BaseRequest
- RequestBody classes MUST inherit from BaseModel
- Response classes MUST inherit from BaseResponse (MANDATORY - ZERO TOLERANCE)
- Use `request_body()` method pattern for POST requests
- Use `add_query()` for query parameters
- Use `paths["param"]` for path parameters
- Builder variables MUST use full descriptive names (e.g., `self._create_request`)
- Set correct HTTP methods and URIs in builder constructors
- NO Builder patterns for Response classes

URI Patterns:
- POST /v1/datasets/:dataset_id/documents/:document_id/segments (create)
- GET /v1/datasets/:dataset_id/documents/:document_id/segments (list)
- GET /v1/datasets/:dataset_id/documents/:document_id/segments/:segment_id (get)
- POST /v1/datasets/:dataset_id/documents/:document_id/segments/:segment_id (update)
- DELETE /v1/datasets/:dataset_id/documents/:document_id/segments/:segment_id (delete)
```

#### Step 4: Test Core Segment Models
**Prompt:**
```
Add comprehensive unit tests for core segment models to the existing `tests/knowledge_base/v1/model/test_segment_models.py` file:

Add a new section for Core Segment API models:

Requirements:
- Add tests to the existing consolidated test file
- Test all Request builder patterns
- Test all RequestBody validation and builders
- Test all Response models
- Test path parameter handling (dataset_id, document_id, segment_id)
- Test query parameter handling (keyword, status, page, limit)
- Test request body serialization
- Verify HTTP method and URI configuration
- Include edge cases and validation errors
- All test methods must have proper type hints
- Test builder method chaining
- Use clear section comments to organize tests

Example test structure addition:
```python
# ===== CORE SEGMENT API MODELS TESTS =====

def test_create_request_builder() -> None:
    # Test CreateRequest builder pattern

def test_create_request_body_validation() -> None:
    # Test CreateRequestBody validation and builder

def test_list_request_query_params() -> None:
    # Test ListRequest query parameter handling

def test_response_models_inheritance() -> None:
    # Test all Response models inherit from BaseResponse
```

Run tests: `poetry run pytest tests/knowledge_base/v1/model/test_segment_models.py -v`
```

### Phase 3: Child Chunk Operations (4 APIs)

#### Step 5: Create Child Chunk Request/Response Models
**Prompt:**
```
Create all request and response models for child chunk operations in `dify_oapi/api/knowledge_base/v1/model/segment/`.

Implement the following model files based on the API specifications:

**POST Request Models (with RequestBody)**:
1. `create_child_chunk_request.py` - CreateChildChunkRequest + CreateChildChunkRequestBuilder
2. `create_child_chunk_request_body.py` - CreateChildChunkRequestBody + CreateChildChunkRequestBodyBuilder
   Fields: content (str)

**PATCH Request Models (with RequestBody)**:
3. `update_child_chunk_request.py` - UpdateChildChunkRequest + UpdateChildChunkRequestBuilder
4. `update_child_chunk_request_body.py` - UpdateChildChunkRequestBody + UpdateChildChunkRequestBodyBuilder
   Fields: content (str)

**GET Request Models (no RequestBody)**:
5. `list_child_chunks_request.py` - ListChildChunksRequest + ListChildChunksRequestBuilder
   Query params: keyword, page, limit
   Path params: dataset_id, document_id, segment_id

**DELETE Request Models (no RequestBody)**:
6. `delete_child_chunk_request.py` - DeleteChildChunkRequest + DeleteChildChunkRequestBuilder
   Path params: dataset_id, document_id, segment_id, child_chunk_id

**Response Models**:
7. `create_child_chunk_response.py` - CreateChildChunkResponse (inherits BaseResponse) with data field
8. `list_child_chunks_response.py` - ListChildChunksResponse (inherits BaseResponse) with data, total, total_pages, page, limit fields
9. `update_child_chunk_response.py` - UpdateChildChunkResponse (inherits BaseResponse) with data field
10. `delete_child_chunk_response.py` - DeleteChildChunkResponse (inherits BaseResponse) - empty for 204

CRITICAL REQUIREMENTS:
- Follow EXACT same patterns as core segment models
- ALL class names MUST match file names exactly (NO prefixes)
- Use correct URI patterns with all required path parameters
- Handle PATCH method for update_child_chunk
- Include proper validation for content fields

URI Patterns:
- POST /v1/datasets/:dataset_id/documents/:document_id/segments/:segment_id/child_chunks (create)
- GET /v1/datasets/:dataset_id/documents/:document_id/segments/:segment_id/child_chunks (list)
- PATCH /v1/datasets/:dataset_id/documents/:document_id/segments/:segment_id/child_chunks/:child_chunk_id (update)
- DELETE /v1/datasets/:dataset_id/documents/:document_id/segments/:segment_id/child_chunks/:child_chunk_id (delete)
```

#### Step 6: Test Child Chunk Models
**Prompt:**
```
Add comprehensive unit tests for child chunk models to the existing `tests/knowledge_base/v1/model/test_segment_models.py` file:

Add a new section for Child Chunk API models:

Requirements:
- Add tests to the existing consolidated test file
- Test all child chunk Request builder patterns
- Test all child chunk RequestBody validation and builders
- Test all child chunk Response models
- Test complex path parameter handling (dataset_id, document_id, segment_id, child_chunk_id)
- Test query parameter handling for list operations
- Test PATCH method configuration for updates
- Include proper type hints for all test methods
- Test builder patterns and method chaining
- Use clear section comments to organize tests

Example test structure addition:
```python
# ===== CHILD CHUNK API MODELS TESTS =====

def test_create_child_chunk_request_builder() -> None:
    # Test CreateChildChunkRequest builder pattern

def test_list_child_chunks_request_params() -> None:
    # Test ListChildChunksRequest parameter handling

def test_update_child_chunk_patch_method() -> None:
    # Test UpdateChildChunkRequest PATCH method configuration
```

Run tests: `poetry run pytest tests/knowledge_base/v1/model/test_segment_models.py -v`
```

### Phase 4: Segment Resource Implementation

#### Step 7: Segment Resource Implementation
**Prompt:**
```
Implement the Segment resource class in `dify_oapi/api/knowledge_base/v1/resource/segment.py`.

Create a Segment class with the following methods based on the API endpoints:

**Core Segment Operations**:
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

**Child Chunk Operations**:
11. `create_child_chunk(request: CreateChildChunkRequest, request_option: RequestOption) -> CreateChildChunkResponse`
12. `acreate_child_chunk(request: CreateChildChunkRequest, request_option: RequestOption) -> CreateChildChunkResponse`
13. `list_child_chunks(request: ListChildChunksRequest, request_option: RequestOption) -> ListChildChunksResponse`
14. `alist_child_chunks(request: ListChildChunksRequest, request_option: RequestOption) -> ListChildChunksResponse`
15. `update_child_chunk(request: UpdateChildChunkRequest, request_option: RequestOption) -> UpdateChildChunkResponse`
16. `aupdate_child_chunk(request: UpdateChildChunkRequest, request_option: RequestOption) -> UpdateChildChunkResponse`
17. `delete_child_chunk(request: DeleteChildChunkRequest, request_option: RequestOption) -> DeleteChildChunkResponse`
18. `adelete_child_chunk(request: DeleteChildChunkRequest, request_option: RequestOption) -> DeleteChildChunkResponse`

Follow the existing transport patterns and HTTP method mappings.

MANDATORY REQUIREMENTS:
- Use Transport.execute() for sync methods
- Use ATransport.aexecute() for async methods
- Include proper error handling and response parsing
- Follow existing resource class patterns in the project
- Import all necessary request/response models
- Use proper type hints for all method parameters and return types
- Initialize with config parameter in constructor
```

#### Step 8: Test Segment Resource
**Prompt:**
```
Create comprehensive integration tests for the Segment resource in `tests/knowledge_base/v1/resource/test_segment_resource.py`.

Test all methods implemented in Step 7, including:
1. HTTP method and URL mapping verification
2. Request serialization and response deserialization
3. Error handling for various HTTP status codes
4. Both sync and async method variants
5. Mock API responses based on the API documentation
6. Transport layer integration
7. All 18 methods (9 core + 9 child chunk operations)

MANDATORY REQUIREMENTS:
- ALL test methods MUST include proper type annotations: `def test_method(self) -> None:`
- Use pytest fixtures and mock responses to simulate API interactions
- Test all 18 methods (9 sync + 9 async)
- Verify correct HTTP methods and URLs are used
- Mock Transport.execute() and ATransport.aexecute() calls
- Test error scenarios (4xx, 5xx responses)
- Ensure all tests pass with good coverage
- Use `typing.Any` for complex mock objects like `monkeypatch`

Test structure:
```python
def test_create_sync() -> None:
    # Test sync create method

def test_create_async() -> None:
    # Test async acreate method

def test_create_child_chunk_sync() -> None:
    # Test sync create_child_chunk method

def test_create_child_chunk_async() -> None:
    # Test async acreate_child_chunk method
```
```

### Phase 5: Version Integration

#### Step 9: Update Version Integration
**Prompt:**
```
Update the knowledge_base v1 version integration to include the new segment resource.

Modify `dify_oapi/api/knowledge_base/v1/version.py` to:
1. Import the new Segment resource class
2. Add segment property to the V1 class
3. Initialize it with the config parameter
4. Ensure backward compatibility with existing resources (dataset, document, metadata, tag)

MANDATORY REQUIREMENTS:
- Follow existing patterns in the V1 class
- Import Segment resource class
- Initialize segment resource with config parameter
- Maintain existing API structure
- Update any necessary import statements

Example integration:
```python
from .resource.segment import Segment

class V1:
    def __init__(self, config: Config):
        self.dataset = Dataset(config)
        self.document = Document(config)
        self.segment = Segment(config)  # New
        self.metadata = Metadata(config)
        self.tag = Tag(config)
```
```

#### Step 10: Test Version Integration
**Prompt:**
```
Create integration tests for the updated V1 version class in `tests/knowledge_base/v1/integration/test_version_integration.py`.

Test:
1. All resources are properly initialized
2. Config is correctly passed to all resources
3. New segment resource is accessible
4. Existing resources still work correctly
5. Client integration works end-to-end

MANDATORY REQUIREMENTS:
- ALL test methods MUST include proper type annotations: `def test_method(self) -> None:`
- Use pytest framework with proper fixtures
- Test resource initialization and accessibility
- Verify config propagation to all resources
- Ensure complete knowledge_base module works as expected
- Test segment resource alongside existing resources
```

### Phase 6: Examples and Documentation

#### Step 11: Create Segment Examples
**Prompt:**
```
Create comprehensive usage examples for the segment management functionality in `examples/knowledge_base/segment/`.

Create examples using resource-based directory structure with MINIMAL code approach:

**Core Segment Examples**:
1. `create.py` - Create segments examples (sync + async)
2. `list.py` - List segments examples (sync + async)
3. `get.py` - Get segment details examples (sync + async)
4. `update.py` - Update segment examples (sync + async)
5. `delete.py` - Delete segment examples (sync + async)

**Child Chunk Examples**:
6. `create_child_chunk.py` - Create child chunk examples (sync + async)
7. `list_child_chunks.py` - List child chunks examples (sync + async)
8. `update_child_chunk.py` - Update child chunk examples (sync + async)
9. `delete_child_chunk.py` - Delete child chunk examples (sync + async)

MANDATORY REQUIREMENTS:
- Write ABSOLUTE MINIMAL code needed to demonstrate each API correctly
- ALL resource names MUST use "[Example]" prefix for safety
- Environment variable validation at function start (raise ValueError if missing)
- Both synchronous and asynchronous implementations
- Basic try-catch error handling
- Delete operations MUST check for "[Example]" prefix
- Follow existing example patterns in the project
- Validate API_KEY, DATASET_ID, DOCUMENT_ID environment variables

Environment variable validation pattern:
```python
def create_segment_sync() -> None:
    try:
        # Check required environment variables (MUST be first)
        api_key = os.getenv("API_KEY")
        if not api_key:
            raise ValueError("API_KEY environment variable is required")

        dataset_id = os.getenv("DATASET_ID")
        if not dataset_id:
            raise ValueError("DATASET_ID environment variable is required")

        document_id = os.getenv("DOCUMENT_ID")
        if not document_id:
            raise ValueError("DOCUMENT_ID environment variable is required")

        # Initialize client and continue...
```
```

#### Step 12: Test Examples
**Prompt:**
```
Create validation tests for all examples created in Step 11.

Create `tests/knowledge_base/v1/integration/test_segment_examples_validation.py` that:
1. Validates example code syntax and imports
2. Mocks API calls to test example logic
3. Ensures examples follow best practices
4. Verifies error handling works correctly
5. Tests both sync and async example variants
6. Validates "[Example]" prefix usage in resource names
7. Tests environment variable validation

MANDATORY REQUIREMENTS:
- ALL test methods MUST include proper type annotations: `def test_method(self) -> None:`
- Use pytest framework and mock API responses
- Test all example files for syntax and functionality
- Verify safety measures (prefix checking) work correctly
- Ensure examples are educational and functional
- Test environment variable validation logic
```

### Phase 7: Integration Testing

#### Step 13: Comprehensive Integration Testing
**Prompt:**
```
Create comprehensive end-to-end integration tests for all segment resources:

Create `tests/knowledge_base/v1/integration/test_segment_api_integration.py`:

Test scenarios:
1. **Complete Segment Lifecycle**:
   - Create segments
   - List segments with filtering
   - Get segment details
   - Update segment content
   - Delete segments

2. **Child Chunk Management**:
   - Create child chunks for segments
   - List child chunks with pagination
   - Update child chunk content
   - Delete child chunks

3. **Cross-Operation Integration**:
   - Create segment → Create child chunks → Update both → Delete all
   - List operations with various filters and pagination
   - Error scenarios and edge cases

4. **Error Scenarios**:
   - Invalid dataset/document/segment IDs
   - Missing required fields
   - Network errors
   - Permission errors

MANDATORY REQUIREMENTS:
- ALL test methods MUST include proper type annotations: `def test_method(self) -> None:`
- Use realistic test data and scenarios
- Mock all API calls with proper responses
- Test error scenarios and edge cases
- Ensure all 9 APIs work together correctly
- Verify cross-operation dependencies and workflows
- Test both sync and async operations
```

#### Step 14: Final Quality Assurance
**Prompt:**
```
Perform final quality assurance and create comprehensive validation.

Tasks:
1. Run all tests and ensure 100% pass rate
2. Verify code coverage meets project standards (>90%)
3. Validate all 9 segment APIs are fully functional
4. Test integration with existing knowledge_base resources
5. Perform code review checklist:
   - Type hints are comprehensive and correct
   - Error handling is consistent across all resources
   - Builder patterns work correctly for all models
   - Async/sync parity is maintained
   - All Response classes inherit from BaseResponse
   - Documentation is complete and accurate

Create a final validation report confirming all requirements are met and all segment APIs are production-ready.

MANDATORY REQUIREMENTS:
- Document any breaking changes from existing implementations
- Provide clear integration paths with existing knowledge_base module
- Ensure all code follows project conventions
- Verify all examples work correctly
- Confirm comprehensive test coverage
- Validate all 9 APIs function correctly

Commands to run for validation:
```bash
# Full test suite
poetry run pytest tests/knowledge_base/v1/model/test_segment_models.py -v
poetry run pytest tests/knowledge_base/v1/resource/test_segment_resource.py -v
poetry run pytest tests/knowledge_base/v1/integration/test_segment_api_integration.py -v

# Code quality checks
poetry run ruff check dify_oapi/api/knowledge_base/v1/model/segment/
poetry run ruff format dify_oapi/api/knowledge_base/v1/model/segment/
poetry run mypy dify_oapi/api/knowledge_base/v1/model/segment/

# Example validation
cd examples/knowledge_base/segment/
python create.py
python list.py
python get.py
python update.py
python delete.py
python create_child_chunk.py
python list_child_chunks.py
python update_child_chunk.py
python delete_child_chunk.py
```
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
- ✅ **CRITICAL**: All Response classes MUST inherit from BaseResponse (ZERO TOLERANCE)
- ✅ **Test typing requirements**: All test method parameters and return types must include proper type annotations

## API Coverage Summary

### Core Segment Operations (5 APIs)
1. POST /v1/datasets/:dataset_id/documents/:document_id/segments - Create segments
2. GET /v1/datasets/:dataset_id/documents/:document_id/segments - List segments
3. GET /v1/datasets/:dataset_id/documents/:document_id/segments/:segment_id - Get segment details
4. POST /v1/datasets/:dataset_id/documents/:document_id/segments/:segment_id - Update segment
5. DELETE /v1/datasets/:dataset_id/documents/:document_id/segments/:segment_id - Delete segment

### Child Chunk Operations (4 APIs)
6. POST /v1/datasets/:dataset_id/documents/:document_id/segments/:segment_id/child_chunks - Create child chunk
7. GET /v1/datasets/:dataset_id/documents/:document_id/segments/:segment_id/child_chunks - List child chunks
8. PATCH /v1/datasets/:dataset_id/documents/:document_id/segments/:segment_id/child_chunks/:child_chunk_id - Update child chunk
9. DELETE /v1/datasets/:dataset_id/documents/:document_id/segments/:segment_id/child_chunks/:child_chunk_id - Delete child chunk

## Code Style Rules (MANDATORY - NO EXCEPTIONS)

### Response Model Inheritance (CRITICAL - ZERO TOLERANCE)
**MANDATORY RULE**: Every single Response class in the segment module MUST inherit from `BaseResponse`
- **Rationale**: Ensures all API responses have consistent error handling capabilities
- **Properties Provided**: `success`, `code`, `msg`, `raw` for comprehensive error management
- **Zero Exceptions**: No Response class may inherit directly from `pydantic.BaseModel`
- **Validation**: All examples and tests must check `response.success` before accessing data
- **Implementation**: Use `from dify_oapi.core.model.base_response import BaseResponse`

**Correct Response Class Patterns**:
```python
# ✅ CORRECT: Simple response inheriting from BaseResponse
class DeleteResponse(BaseResponse):
    pass

# ✅ CORRECT: Response with data using multiple inheritance
class CreateResponse(BaseResponse):
    data: list[SegmentInfo] | None = None
    doc_form: str | None = None

# ❌ WRONG: Direct BaseModel inheritance
class CreateResponse(BaseModel):  # NEVER DO THIS
    pass
```

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
**GET Requests** (list, get, list_child_chunks):
- NO RequestBody file needed
- Use query parameters: `self._request.add_query("key", value)`
- Use path parameters: `self._request.paths["param_name"] = value`

**POST Requests** (create, update, create_child_chunk):
- REQUIRE separate RequestBody file
- Use `request_body()` method in Request builder
- RequestBody builder methods set fields directly

**PATCH Requests** (update_child_chunk):
- REQUIRE separate RequestBody file
- Support path parameters for resource ID
- Use `request_body()` method in Request builder

**DELETE Requests** (delete, delete_child_chunk):
- NO RequestBody file needed
- Use path parameters for resource ID

### Class Naming Convention (ZERO TOLERANCE)
**Universal Naming Pattern**:
- File names determine class names exactly (e.g., `create_request.py` → `CreateRequest`)
- Each class has corresponding Builder (e.g., `CreateRequest` + `CreateRequestBuilder`)
- Pattern applies to all model types: Request, RequestBody, Response

**STRICT Naming Rules (NO EXCEPTIONS)**:
- Remove ALL module/domain prefixes from class names
- Class names MUST match file names exactly (case-sensitive)
- Apply uniformly across ALL operations: core segment and child chunk
- Use operation-based names: `CreateRequest`, `ListResponse`, `UpdateRequestBody`
- NEVER use domain-specific names: `CreateSegmentRequest`, `SegmentCreateResponse`
- NO legacy naming patterns allowed
- Consistent across all HTTP methods and operation types

### Public Class Inheritance Rules (CRITICAL)
**Public/Common Classes**:
- Public classes (SegmentInfo, ChildChunkInfo, SegmentData) MUST inherit from `pydantic.BaseModel` ONLY
- Public classes MUST NOT inherit from `BaseResponse`
- Public classes MUST have Builder patterns for consistency and ease of use
- Examples: `SegmentInfo`, `ChildChunkInfo`, `SegmentData`

**Response Classes**:
- Response classes MUST inherit from `BaseResponse` for error handling capabilities
- Response classes MAY use multiple inheritance when they need to include public class data
- Pattern: `class CreateResponse(BaseResponse):`
- Response classes MUST NOT have Builder patterns

### Environment Variable Validation (MANDATORY)
**All Examples MUST**:
- Check for required environment variables at function start
- Raise `ValueError` with descriptive message if missing
- NEVER use `print()` statements for missing variables
- Validate `API_KEY`, `DATASET_ID`, `DOCUMENT_ID` as needed
- Place ALL validations at the very beginning of each function

#### Minimalism Principles:
1. **Concise Variable Initialization**: Combine client and request option creation where possible
2. **Simplified Output Messages**: Replace verbose success messages with concise status indicators
3. **Reduced Function Count**: Remove redundant demonstration functions, keep only sync/async pairs
4. **Streamlined Error Handling**: Maintain essential error handling without verbose explanations
5. **Essential Comments Only**: Remove explanatory comments that don't add technical value
6. **Consistent Patterns**: Apply the same minimization approach across all resource examples

#### Safety Features:
- Environment variable validation at function start
- "[Example]" prefix checking for delete operations
- Basic error handling with try-catch blocks
- Resource existence verification before operations
- Consistent API key and resource ID validation

### Testing Requirements (MANDATORY)
**All Test Methods MUST**:
- Include proper type annotations: `def test_method(self) -> None:`
- Import necessary typing modules (`typing.Any` for complex objects)
- Use pytest framework with proper fixtures
- Achieve >90% code coverage
- Test both sync and async variants where applicable
- Mock API calls appropriately
- Follow consistent patterns across all test files

## Latest Improvements and Optimizations

### 1. Enhanced Segment Processing
**Recent Updates**:
- **Intelligent Segmentation**: Advanced algorithms for better content organization and chunking
- **Context Preservation**: Improved context preservation across segment boundaries
- **Quality Scoring**: Automatic quality assessment for segment content
- **Batch Operations**: Enhanced batch processing capabilities for multiple segments

### 2. Child Chunk Management
**Implementation Enhancements**:
- **Hierarchical Structure**: Better support for hierarchical content organization
- **Relationship Tracking**: Enhanced tracking of parent-child relationships
- **Content Synchronization**: Improved synchronization between segments and child chunks
- **Performance Optimization**: Optimized operations for large segment collections

### 3. Search and Retrieval
**Latest Features**:
- **Advanced Filtering**: Enhanced filtering capabilities for segment search
- **Relevance Scoring**: Improved relevance scoring algorithms
- **Faceted Search**: Support for faceted search across segment attributes
- **Real-time Updates**: Real-time updates for segment search indices

### 4. Developer Experience Improvements
**Recent Enhancements**:
- **Enhanced Type Safety**: More comprehensive type annotations for better IDE support
- **Improved Documentation**: Better inline documentation and examples
- **Simplified API Usage**: More intuitive method signatures and parameter handling
- **Better Error Messages**: More descriptive error messages for debugging

### 5. Testing and Quality Assurance
**Quality Improvements**:
- **Comprehensive Test Coverage**: Expanded test suite covering all edge cases
- **Performance Testing**: Added performance benchmarks and optimization tests
- **Integration Testing**: Enhanced integration tests with real API scenarios
- **Code Quality Metrics**: Improved code quality monitoring and enforcement

## Summary

This comprehensive plan provides step-by-step prompts for implementing all 9 segment management APIs with proper testing, documentation, and examples. Each step builds upon the previous ones and includes specific requirements to ensure code quality and consistency.

The modular resource-based organization, combined with shared common models and descriptive method naming, creates an intuitive and powerful interface for segment management operations including core segment CRUD operations and child chunk management.

The examples strategy ensures developers have clear, educational references for every API operation, supporting both learning and integration testing needs with comprehensive sync/async coverage. The code minimalism approach optimizes all examples for clarity while maintaining full functionality and safety features.

### Key Features
- **Code Minimalism**: All segment examples follow minimal code principles
- **Improved Readability**: Simplified output messages and reduced verbose logging
- **Maintained Safety**: All safety features and validation remain intact
- **Consistent Patterns**: Uniform minimization approach across all 9 API examples
- **Educational Focus**: Examples focus purely on demonstrating API functionality without unnecessary complexity
- **Performance Optimization**: Enhanced segment processing and child chunk management
- **Enhanced Type Safety**: Improved type annotations and validation mechanisms
- **Better Error Handling**: Robust error propagation and user-friendly error messages
- **Advanced Features**: Support for intelligent segmentation, hierarchical structures, and advanced search capabilities