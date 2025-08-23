# Segment API Design Document

## Overview

This document outlines the design for implementing comprehensive segment management functionality in the dify-oapi knowledge_base module. The implementation will support all 9 segment-related APIs covering segment CRUD operations, child chunk management, and detailed segment information retrieval.

## Design Decisions

### 1. Resource Organization
**Decision**: Create new `segment` resource class within knowledge_base module
- Follow established resource class pattern used by document and dataset resources
- Create comprehensive resource class with all 9 segment management methods
- Maintain consistency with existing knowledge base module architecture
- Leverage existing infrastructure and method naming conventions

### 2. Model File Organization Strategy
**Decision**: Complete new directory structure following established patterns
- **Directory Structure**: Create new `model/segment/` directory structure
- **Scope**: Implement ALL 9 segment APIs with comprehensive model coverage
- **Naming Convention**: Use simplified names following dataset/document design patterns
- **Child Chunk Integration**: Include child chunk management within segment resource
- **Import Consistency**: Follow established import path patterns

### 3. Method Naming Convention
**Decision**: Use descriptive method names for clarity and consistency
- **Core CRUD**: `create()`, `list()`, `get()`, `update()`, `delete()`
- **Child Chunk Operations**: `create_child_chunk()`, `list_child_chunks()`, `update_child_chunk()`, `delete_child_chunk()`
- **Intuitive API**: Self-documenting method names that clearly indicate functionality
- **Consistency**: Align with document and dataset resource naming patterns

### 4. Response Model Inheritance Rules (CRITICAL - ZERO TOLERANCE)
**Decision**: ALL Response classes MUST inherit from BaseResponse for error handling

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
class CreateResponse(SegmentInfo, BaseResponse):
    pass

# ❌ WRONG: Direct BaseModel inheritance
class CreateResponse(BaseModel):  # NEVER DO THIS
    pass
```

### 5. Request/Response Model Code Style Rules (MANDATORY)
**Decision**: Strict adherence to established patterns for consistency

#### Request Model Architecture
**Request Classes**:
- MUST inherit from `BaseRequest` (never from `BaseModel`)
- MUST include `request_body` attribute of type `RequestBody | None` for POST/PATCH requests
- MUST use `request_body()` method in builder to accept entire RequestBody object
- Builder variables MUST use full descriptive names (e.g., `self._create_request`)
- MUST set `http_method` and `uri` in builder constructor
- Path parameters MUST use `self._request.paths["param_name"] = value` pattern
- Query parameters MUST use `self._request.add_query("key", value)` pattern

**RequestBody Separation (For POST/PATCH requests)**:
- RequestBody MUST be in separate file from Request
- RequestBody MUST inherit from `pydantic.BaseModel`
- RequestBody MUST include its own Builder pattern
- File naming convention: `create_request.py` and `create_request_body.py`
- Both Request and RequestBody MUST have Builder classes

#### HTTP Method Patterns
**GET Requests** (list, get, list_child_chunks):
- No RequestBody file needed
- Use query parameters: `self._request.add_query("key", value)`
- Use path parameters: `self._request.paths["param_name"] = value`

**POST Requests** (create, create_child_chunk):
- Require separate RequestBody file
- Use `request_body()` method in Request builder
- RequestBody builder methods set fields directly

**PATCH Requests** (update, update_child_chunk):
- Require separate RequestBody file
- Support path parameters for resource ID
- Use `request_body()` method in Request builder

**DELETE Requests** (delete, delete_child_chunk):
- No RequestBody file needed
- Use path parameters for resource ID

#### Class Naming Convention (MANDATORY - ZERO TOLERANCE)
**Universal Naming Pattern**:
- File names determine class names exactly (e.g., `create_request.py` → `CreateRequest`)
- Each class has corresponding Builder (e.g., `CreateRequest` + `CreateRequestBuilder`)
- Pattern applies to all model types: Request, RequestBody, Response

**STRICT Naming Rules (NO EXCEPTIONS)**:
- Remove ALL module/domain prefixes from class names
- Class names MUST match file names exactly (case-sensitive)
- Use operation-based names: `CreateRequest`, `ListResponse`, `UpdateRequestBody`
- NEVER use domain-specific names: `CreateSegmentRequest`, `SegmentListResponse`
- NO legacy naming patterns allowed
- Consistent across all HTTP methods and operation types

#### URI and HTTP Method Configuration
**Segment APIs**:
- `POST /v1/datasets/:dataset_id/documents/:document_id/segments` → `CreateRequest`
- `GET /v1/datasets/:dataset_id/documents/:document_id/segments` → `ListRequest`
- `DELETE /v1/datasets/:dataset_id/documents/:document_id/segments/:segment_id` → `DeleteRequest`
- `GET /v1/datasets/:dataset_id/documents/:document_id/segments/:segment_id` → `GetRequest`
- `POST /v1/datasets/:dataset_id/documents/:document_id/segments/:segment_id` → `UpdateRequest`

**Child Chunk APIs**:
- `POST /v1/datasets/:dataset_id/documents/:document_id/segments/:segment_id/child_chunks` → `CreateChildChunkRequest`
- `GET /v1/datasets/:dataset_id/documents/:document_id/segments/:segment_id/child_chunks` → `ListChildChunksRequest`
- `DELETE /v1/datasets/:dataset_id/documents/:document_id/segments/:segment_id/child_chunks/:child_chunk_id` → `DeleteChildChunkRequest`
- `PATCH /v1/datasets/:dataset_id/documents/:document_id/segments/:segment_id/child_chunks/:child_chunk_id` → `UpdateChildChunkRequest`

#### Public Class Inheritance Rules (CRITICAL)
**Public/Common Classes**:
- Public classes (SegmentInfo, ChildChunkInfo, etc.) MUST inherit from `pydantic.BaseModel` ONLY
- Public classes MUST NOT inherit from `BaseResponse`
- Public classes MUST have Builder patterns for consistency and ease of use
- Public classes are reusable components that can be used across different contexts
- Examples: `SegmentInfo`, `ChildChunkInfo`, `SegmentData`

**Response Classes (MANDATORY - ZERO TOLERANCE)**:
- ALL Response classes MUST inherit from `BaseResponse` for error handling capabilities
- Response classes MAY use multiple inheritance when they need to include public class data
- Pattern: `class CreateResponse(SegmentInfo, BaseResponse):`
- This allows response classes to have both data fields and error handling capabilities
- Response classes MUST NOT have Builder patterns (unlike Request classes)
- **CRITICAL**: NEVER inherit from `pydantic.BaseModel` directly - ALWAYS use `BaseResponse`
- This ensures all responses have `success`, `code`, `msg`, and error handling properties

**Builder Pattern Rules**:
- Request, RequestBody, and Public/Common classes MUST have Builder patterns
- Public/common classes can be instantiated directly using Pydantic's standard initialization OR via builder pattern
- Response classes should be instantiated by the transport layer, not manually
- Builder patterns provide fluent interface for complex object construction

### 6. Strict Type Safety Rules (MANDATORY - ZERO TOLERANCE)
**Decision**: ALL API fields MUST use strict typing with Literal types instead of generic strings

**MANDATORY RULE**: Every field that has predefined values MUST use Literal types for type safety
- **Rationale**: Ensures compile-time validation and prevents invalid values
- **Implementation**: Use `from typing import Literal` and define type aliases
- **Zero Exceptions**: No field with predefined values may use generic `str` type
- **Validation**: IDE and type checkers will catch invalid values at development time

**Strict Type Implementation Pattern**:
```python
# segment_types.py - Define all Literal types
from typing import Literal

# Segment status types
SegmentStatus = Literal["waiting", "indexing", "completed", "error", "paused"]

# Segment enabled status types
SegmentEnabledStatus = Literal["enabled", "disabled"]

# Child chunk status types
ChildChunkStatus = Literal["waiting", "indexing", "completed", "error"]

# Segment search status types
SearchStatus = Literal["all", "enabled", "disabled"]

# Sort order types
SortOrder = Literal["created_at", "position", "word_count", "hit_count"]

# Sort direction types
SortDirection = Literal["asc", "desc"]
```

**Model Usage Pattern**:
```python
# Use Literal types in models
from .segment_types import SegmentStatus, SegmentEnabledStatus

class SegmentInfo(BaseModel):
    status: SegmentStatus | None = None
    enabled: bool | None = None  # Can be converted to SegmentEnabledStatus if needed
    # NOT: status: str | None = None
```

**Structured Input Objects (MANDATORY)**:
- Replace generic `dict[str, Any]` with structured classes
- Create dedicated input classes with builder patterns
- Provide type safety for complex nested objects

**Example - Structured Segment Data**:
```python
# segment_data.py
class SegmentData(BaseModel):
    content: str | None = None
    answer: str | None = None
    keywords: list[str] | None = None
    enabled: bool | None = None
    
    @staticmethod
    def builder() -> SegmentDataBuilder:
        return SegmentDataBuilder()

# Usage in RequestBody
class UpdateRequestBody(BaseModel):
    segment: SegmentData | None = None
    # NOT: segment: dict[str, Any] | None = None
```

**Strict Type Coverage**:
- **Segment Status**: `"waiting"` | `"indexing"` | `"completed"` | `"error"` | `"paused"`
- **Enabled Status**: `"enabled"` | `"disabled"`
- **Child Chunk Status**: `"waiting"` | `"indexing"` | `"completed"` | `"error"`
- **Search Status**: `"all"` | `"enabled"` | `"disabled"`
- **Sort Orders**: `"created_at"` | `"position"` | `"word_count"` | `"hit_count"`
- **Sort Directions**: `"asc"` | `"desc"`

**Benefits of Strict Typing**:
- **Compile-time Validation**: Catch invalid values during development
- **IDE Support**: Auto-completion and error highlighting
- **Documentation**: Self-documenting code with clear valid values
- **Refactoring Safety**: Type-safe refactoring across the codebase
- **API Consistency**: Ensures consistent usage of predefined values

### 7. Public Class Builder Pattern Rules (MANDATORY)
**Decision**: All public classes MUST implement builder patterns for consistency and usability

#### Builder Pattern Implementation Requirements
**Scope**: All public/common classes that inherit from `pydantic.BaseModel`
- **Target Classes**: `SegmentInfo`, `ChildChunkInfo`, `SegmentData`, and all other public model classes
- **Exclusions**: Request, RequestBody, and Response classes (which have their own builder rules)

#### Implementation Pattern
**Standard Builder Structure**:
```python
class PublicClass(BaseModel):
    field1: str | None = None
    field2: int | None = None
    # ... other fields
    
    @staticmethod
    def builder() -> PublicClassBuilder:
        return PublicClassBuilder()

class PublicClassBuilder:
    def __init__(self):
        self._public_class = PublicClass()
    
    def build(self) -> PublicClass:
        return self._public_class
    
    def field1(self, field1: str) -> PublicClassBuilder:
        self._public_class.field1 = field1
        return self
    
    def field2(self, field2: int) -> PublicClassBuilder:
        self._public_class.field2 = field2
        return self
```

#### Forward Reference Handling
**Import Requirements**:
- ALL public class files MUST include `from __future__ import annotations` at the top
- This prevents forward reference issues when builder methods reference the builder class
- Essential for proper type hints in `@staticmethod` decorators

## API Implementation Plan

### Segment Management APIs (9 APIs)

#### Core Segment Operations (5 APIs)
1. **POST /datasets/{dataset_id}/documents/{document_id}/segments** → `segment.create()` - New implementation
2. **GET /datasets/{dataset_id}/documents/{document_id}/segments** → `segment.list()` - New implementation
3. **DELETE /datasets/{dataset_id}/documents/{document_id}/segments/{segment_id}** → `segment.delete()` - New implementation
4. **GET /datasets/{dataset_id}/documents/{document_id}/segments/{segment_id}** → `segment.get()` - New implementation
5. **POST /datasets/{dataset_id}/documents/{document_id}/segments/{segment_id}** → `segment.update()` - New implementation

#### Child Chunk Operations (4 APIs)
6. **POST /datasets/{dataset_id}/documents/{document_id}/segments/{segment_id}/child_chunks** → `segment.create_child_chunk()` - New implementation
7. **GET /datasets/{dataset_id}/documents/{document_id}/segments/{segment_id}/child_chunks** → `segment.list_child_chunks()` - New implementation
8. **DELETE /datasets/{dataset_id}/documents/{document_id}/segments/{segment_id}/child_chunks/{child_chunk_id}** → `segment.delete_child_chunk()` - New implementation
9. **PATCH /datasets/{dataset_id}/documents/{document_id}/segments/{segment_id}/child_chunks/{child_chunk_id}** → `segment.update_child_chunk()` - New implementation

## Model File Organization

### New Directory Structure
```
model/segment/          # Segment-specific models
├── create_request.py              # CreateRequest + CreateRequestBuilder
├── create_request_body.py         # CreateRequestBody + CreateRequestBodyBuilder
├── create_response.py             # CreateResponse
├── list_request.py                # ListRequest + ListRequestBuilder
├── list_response.py               # ListResponse
├── delete_request.py              # DeleteRequest + DeleteRequestBuilder
├── delete_response.py             # DeleteResponse
├── get_request.py                 # GetRequest + GetRequestBuilder
├── get_response.py                # GetResponse
├── update_request.py              # UpdateRequest + UpdateRequestBuilder
├── update_request_body.py         # UpdateRequestBody + UpdateRequestBodyBuilder
├── update_response.py             # UpdateResponse
├── create_child_chunk_request.py      # CreateChildChunkRequest + CreateChildChunkRequestBuilder
├── create_child_chunk_request_body.py # CreateChildChunkRequestBody + CreateChildChunkRequestBodyBuilder
├── create_child_chunk_response.py     # CreateChildChunkResponse
├── list_child_chunks_request.py       # ListChildChunksRequest + ListChildChunksRequestBuilder
├── list_child_chunks_response.py      # ListChildChunksResponse
├── delete_child_chunk_request.py      # DeleteChildChunkRequest + DeleteChildChunkRequestBuilder
├── delete_child_chunk_response.py     # DeleteChildChunkResponse
├── update_child_chunk_request.py      # UpdateChildChunkRequest + UpdateChildChunkRequestBuilder
├── update_child_chunk_request_body.py # UpdateChildChunkRequestBody + UpdateChildChunkRequestBodyBuilder
├── update_child_chunk_response.py     # UpdateChildChunkResponse
├── segment_info.py                # SegmentInfo model
├── child_chunk_info.py            # ChildChunkInfo model
└── segment_data.py                # SegmentData model (for update operations)
```

## Technical Implementation Details

### Resource Class Structure
```python
# New segment resource
class Segment:
    def __init__(self, config: Config):
        self.config = config
    
    # Core segment operations
    def create(self, request: CreateRequest, request_option: RequestOption) -> CreateResponse:
        return Transport.execute(self.config, request, unmarshal_as=CreateResponse, option=request_option)
    
    async def acreate(self, request: CreateRequest, request_option: RequestOption) -> CreateResponse:
        return await ATransport.aexecute(self.config, request, unmarshal_as=CreateResponse, option=request_option)
    
    def list(self, request: ListRequest, request_option: RequestOption) -> ListResponse:
        return Transport.execute(self.config, request, unmarshal_as=ListResponse, option=request_option)
    
    async def alist(self, request: ListRequest, request_option: RequestOption) -> ListResponse:
        return await ATransport.aexecute(self.config, request, unmarshal_as=ListResponse, option=request_option)
    
    def delete(self, request: DeleteRequest, request_option: RequestOption) -> DeleteResponse:
        return Transport.execute(self.config, request, unmarshal_as=DeleteResponse, option=request_option)
    
    async def adelete(self, request: DeleteRequest, request_option: RequestOption) -> DeleteResponse:
        return await ATransport.aexecute(self.config, request, unmarshal_as=DeleteResponse, option=request_option)
    
    def get(self, request: GetRequest, request_option: RequestOption) -> GetResponse:
        return Transport.execute(self.config, request, unmarshal_as=GetResponse, option=request_option)
    
    async def aget(self, request: GetRequest, request_option: RequestOption) -> GetResponse:
        return await ATransport.aexecute(self.config, request, unmarshal_as=GetResponse, option=request_option)
    
    def update(self, request: UpdateRequest, request_option: RequestOption) -> UpdateResponse:
        return Transport.execute(self.config, request, unmarshal_as=UpdateResponse, option=request_option)
    
    async def aupdate(self, request: UpdateRequest, request_option: RequestOption) -> UpdateResponse:
        return await ATransport.aexecute(self.config, request, unmarshal_as=UpdateResponse, option=request_option)
    
    # Child chunk operations
    def create_child_chunk(self, request: CreateChildChunkRequest, request_option: RequestOption) -> CreateChildChunkResponse:
        return Transport.execute(self.config, request, unmarshal_as=CreateChildChunkResponse, option=request_option)
    
    async def acreate_child_chunk(self, request: CreateChildChunkRequest, request_option: RequestOption) -> CreateChildChunkResponse:
        return await ATransport.aexecute(self.config, request, unmarshal_as=CreateChildChunkResponse, option=request_option)
    
    def list_child_chunks(self, request: ListChildChunksRequest, request_option: RequestOption) -> ListChildChunksResponse:
        return Transport.execute(self.config, request, unmarshal_as=ListChildChunksResponse, option=request_option)
    
    async def alist_child_chunks(self, request: ListChildChunksRequest, request_option: RequestOption) -> ListChildChunksResponse:
        return await ATransport.aexecute(self.config, request, unmarshal_as=ListChildChunksResponse, option=request_option)
    
    def delete_child_chunk(self, request: DeleteChildChunkRequest, request_option: RequestOption) -> DeleteChildChunkResponse:
        return Transport.execute(self.config, request, unmarshal_as=DeleteChildChunkResponse, option=request_option)
    
    async def adelete_child_chunk(self, request: DeleteChildChunkRequest, request_option: RequestOption) -> DeleteChildChunkResponse:
        return await ATransport.aexecute(self.config, request, unmarshal_as=DeleteChildChunkResponse, option=request_option)
    
    def update_child_chunk(self, request: UpdateChildChunkRequest, request_option: RequestOption) -> UpdateChildChunkResponse:
        return Transport.execute(self.config, request, unmarshal_as=UpdateChildChunkResponse, option=request_option)
    
    async def aupdate_child_chunk(self, request: UpdateChildChunkRequest, request_option: RequestOption) -> UpdateChildChunkResponse:
        return await ATransport.aexecute(self.config, request, unmarshal_as=UpdateChildChunkResponse, option=request_option)
```

### Complete Code Style Examples

#### POST Request Pattern (with RequestBody)
```python
# create_request.py
from dify_oapi.core.enum import HttpMethod
from dify_oapi.core.model.base_request import BaseRequest
from .create_request_body import CreateRequestBody

class CreateRequest(BaseRequest):
    def __init__(self):
        super().__init__()
        self.dataset_id: str | None = None
        self.document_id: str | None = None
        self.request_body: CreateRequestBody | None = None

    @staticmethod
    def builder() -> CreateRequestBuilder:
        return CreateRequestBuilder()

class CreateRequestBuilder:
    def __init__(self):
        create_request = CreateRequest()
        create_request.http_method = HttpMethod.POST
        create_request.uri = "/v1/datasets/:dataset_id/documents/:document_id/segments"
        self._create_request = create_request

    def build(self) -> CreateRequest:
        return self._create_request

    def dataset_id(self, dataset_id: str) -> CreateRequestBuilder:
        self._create_request.dataset_id = dataset_id
        self._create_request.paths["dataset_id"] = dataset_id
        return self

    def document_id(self, document_id: str) -> CreateRequestBuilder:
        self._create_request.document_id = document_id
        self._create_request.paths["document_id"] = document_id
        return self

    def request_body(self, request_body: CreateRequestBody) -> CreateRequestBuilder:
        self._create_request.request_body = request_body
        self._create_request.body = request_body.model_dump(exclude_none=True, mode="json")
        return self
```

```python
# create_request_body.py
from __future__ import annotations
from pydantic import BaseModel
from .segment_info import SegmentInfo

class CreateRequestBody(BaseModel):
    segments: list[SegmentInfo] | None = None

    @staticmethod
    def builder() -> CreateRequestBodyBuilder:
        return CreateRequestBodyBuilder()

class CreateRequestBodyBuilder:
    def __init__(self):
        self._create_request_body = CreateRequestBody()

    def build(self) -> CreateRequestBody:
        return self._create_request_body

    def segments(self, segments: list[SegmentInfo]) -> CreateRequestBodyBuilder:
        self._create_request_body.segments = segments
        return self
```

#### GET Request Pattern (with path and query parameters)
```python
# list_request.py
from dify_oapi.core.enum import HttpMethod
from dify_oapi.core.model.base_request import BaseRequest

class ListRequest(BaseRequest):
    def __init__(self):
        super().__init__()
        self.dataset_id: str | None = None
        self.document_id: str | None = None

    @staticmethod
    def builder() -> ListRequestBuilder:
        return ListRequestBuilder()

class ListRequestBuilder:
    def __init__(self):
        list_request = ListRequest()
        list_request.http_method = HttpMethod.GET
        list_request.uri = "/v1/datasets/:dataset_id/documents/:document_id/segments"
        self._list_request = list_request

    def build(self) -> ListRequest:
        return self._list_request

    def dataset_id(self, dataset_id: str) -> ListRequestBuilder:
        self._list_request.dataset_id = dataset_id
        self._list_request.paths["dataset_id"] = dataset_id
        return self

    def document_id(self, document_id: str) -> ListRequestBuilder:
        self._list_request.document_id = document_id
        self._list_request.paths["document_id"] = document_id
        return self

    def keyword(self, keyword: str) -> ListRequestBuilder:
        self._list_request.add_query("keyword", keyword)
        return self

    def status(self, status: str) -> ListRequestBuilder:
        self._list_request.add_query("status", status)
        return self

    def page(self, page: int) -> ListRequestBuilder:
        self._list_request.add_query("page", page)
        return self

    def limit(self, limit: int) -> ListRequestBuilder:
        self._list_request.add_query("limit", limit)
        return self
```

#### DELETE Request Pattern
```python
# delete_request.py
from dify_oapi.core.enum import HttpMethod
from dify_oapi.core.model.base_request import BaseRequest

class DeleteRequest(BaseRequest):
    def __init__(self):
        super().__init__()
        self.dataset_id: str | None = None
        self.document_id: str | None = None
        self.segment_id: str | None = None

    @staticmethod
    def builder() -> DeleteRequestBuilder:
        return DeleteRequestBuilder()

class DeleteRequestBuilder:
    def __init__(self):
        delete_request = DeleteRequest()
        delete_request.http_method = HttpMethod.DELETE
        delete_request.uri = "/v1/datasets/:dataset_id/documents/:document_id/segments/:segment_id"
        self._delete_request = delete_request

    def build(self) -> DeleteRequest:
        return self._delete_request

    def dataset_id(self, dataset_id: str) -> DeleteRequestBuilder:
        self._delete_request.dataset_id = dataset_id
        self._delete_request.paths["dataset_id"] = dataset_id
        return self

    def document_id(self, document_id: str) -> DeleteRequestBuilder:
        self._delete_request.document_id = document_id
        self._delete_request.paths["document_id"] = document_id
        return self

    def segment_id(self, segment_id: str) -> DeleteRequestBuilder:
        self._delete_request.segment_id = segment_id
        self._delete_request.paths["segment_id"] = segment_id
        return self
```

#### Public Class with Builder Pattern
```python
# segment_info.py
from __future__ import annotations
from pydantic import BaseModel

class SegmentInfo(BaseModel):
    id: str | None = None
    position: int | None = None
    document_id: str | None = None
    content: str | None = None
    answer: str | None = None
    word_count: int | None = None
    tokens: int | None = None
    keywords: list[str] | None = None
    index_node_id: str | None = None
    index_node_hash: str | None = None
    hit_count: int | None = None
    enabled: bool | None = None
    disabled_at: int | None = None
    disabled_by: str | None = None
    status: str | None = None
    created_by: str | None = None
    created_at: int | None = None
    indexing_at: int | None = None
    completed_at: int | None = None
    error: str | None = None
    stopped_at: int | None = None

    @staticmethod
    def builder() -> SegmentInfoBuilder:
        return SegmentInfoBuilder()

class SegmentInfoBuilder:
    def __init__(self):
        self._segment_info = SegmentInfo()

    def build(self) -> SegmentInfo:
        return self._segment_info

    def id(self, id: str) -> SegmentInfoBuilder:
        self._segment_info.id = id
        return self

    def content(self, content: str) -> SegmentInfoBuilder:
        self._segment_info.content = content
        return self

    def answer(self, answer: str) -> SegmentInfoBuilder:
        self._segment_info.answer = answer
        return self

    def keywords(self, keywords: list[str]) -> SegmentInfoBuilder:
        self._segment_info.keywords = keywords
        return self

    def enabled(self, enabled: bool) -> SegmentInfoBuilder:
        self._segment_info.enabled = enabled
        return self

    # ... other builder methods for all fields
```

#### Response Class with Multiple Inheritance
```python
# create_response.py
from dify_oapi.core.model.base_response import BaseResponse
from .segment_info import SegmentInfo

class CreateResponse(BaseResponse):
    data: list[SegmentInfo] | None = None
    doc_form: str | None = None
```

### Version Integration
Update `v1/version.py` to include new segment resource:
```python
class V1:
    def __init__(self, config: Config):
        self.dataset = Dataset(config)
        self.document = Document(config)
        self.segment = Segment(config)  # New
        self.metadata = Metadata(config)
        self.tag = Tag(config)
```

## Quality Assurance

### Type Safety
- Comprehensive type hints for all models and methods
- Pydantic validation for request/response models
- Builder pattern support for all request models
- **Test typing requirements**: All test methods must include proper type annotations for parameters and return types

### Error Handling
- Consistent error response handling across all APIs
- Proper HTTP status code mapping
- Detailed error message propagation

### Testing Strategy
- Unit tests for all resource methods
- Integration tests with mock API responses
- Validation tests for all model classes
- **Comprehensive typing hints**: All test method parameters and return types must include proper type annotations
- **Test File Organization**: All model tests MUST follow flat structure in `tests/knowledge_base/v1/model/` directory
- **Naming Consistency**: Use `test_segment_models.py` pattern for segment model test files
- **No Nested Directories**: Avoid creating resource-specific test subdirectories

## Migration Impact

### Breaking Changes
- New segment resource class with comprehensive API coverage
- New model file organization requires proper import path setup
- All segment model files are new implementations
- Import statements need to be established for new segment functionality

### Benefits
- Full API coverage with all 9 segment management endpoints
- Consistent architecture with document/dataset/metadata/tag patterns
- Improved type safety and developer experience
- Enhanced maintainability and extensibility
- Unified code style across all knowledge base features

## Examples Strategy

### Examples Organization
**Decision**: Resource-based directory structure with API-specific files
- Each API gets its own file within `examples/knowledge_base/segment/`
- Each file contains both sync and async examples
- Basic try-catch error handling for educational purposes

### Environment Variable Validation (MANDATORY)
**Decision**: All examples MUST validate required environment variables and raise errors
- **Validation Rule**: Check for required environment variables at the start of each function
- **Error Handling**: Raise `ValueError` with descriptive message if required variables are missing
- **No Print Fallbacks**: NEVER use `print()` statements for missing environment variables
- **Required Variables**: All examples must validate `API_KEY`, `DATASET_ID`, `DOCUMENT_ID`
- **Validation Order**: ALL environment variable validations MUST be placed at the very beginning of each function, immediately after the try block

### Resource Naming Convention (MANDATORY)
**Decision**: All example resources MUST use "[Example]" prefix for safety
- **Creation Rule**: All resources created in examples MUST have "[Example]" prefix in their names
- **Deletion Rule**: Delete operations MUST only target resources with "[Example]" prefix
- **Safety Measure**: This prevents accidental deletion of production or important resources
- **Applies to**: Segment content, child chunk content, and any other named resources

### Code Minimalism Strategy
**Decision**: Apply the same minimal code principles used in other knowledge base examples
- **Objective**: Write only the ABSOLUTE MINIMAL amount of code needed to demonstrate each API correctly
- **Avoid Verbose Implementations**: Remove any code that doesn't directly contribute to the core demonstration
- **Simplify Output**: Reduce verbose logging and status messages to essential information only
- **Remove Redundant Functions**: Eliminate multiple similar functions that don't add educational value
- **Maintain Core Functionality**: Ensure all essential features and safety checks remain intact

### Examples Directory Structure
```
examples/knowledge_base/segment/
├── create.py              # Create segments examples (sync + async)
├── list.py                # List segments examples (sync + async)
├── delete.py              # Delete segment examples (sync + async)
├── get.py                 # Get segment details examples (sync + async)
├── update.py              # Update segment examples (sync + async)
├── create_child_chunk.py  # Create child chunk examples (sync + async)
├── list_child_chunks.py   # List child chunks examples (sync + async)
├── delete_child_chunk.py  # Delete child chunk examples (sync + async)
└── update_child_chunk.py  # Update child chunk examples (sync + async)
```