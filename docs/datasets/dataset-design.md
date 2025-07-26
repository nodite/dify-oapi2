# Dataset API Design Document

## Overview

This document outlines the design for implementing comprehensive dataset management functionality in the dify-oapi knowledge_base module. The implementation will support all 19 dataset-related APIs covering dataset CRUD operations, metadata management, tag management, and retrieval functionality.

## Design Decisions

### 1. Module Organization
**Decision**: Extend existing `knowledge_base/v1/` module structure
- Continue using the established version-based API organization
- Maintain consistency with existing chat, completion, and workflow modules
- Leverage existing infrastructure and patterns

### 2. Resource Structure
**Decision**: Create comprehensive resource classes within knowledge_base module

**Extended Existing Resources**:
- `dataset` - Extend existing resource with get, update, retrieve methods (3 new APIs)

**New Resource Classes**:
- `metadata` - Dataset metadata management (7 APIs)
- `tag` - Knowledge base type tag management (7 APIs)

### 3. Response Model Strategy
**Decision**: Create dedicated Response models for every API
- Maintain type safety and consistency across all endpoints
- Include specific response models even for simple `{"result": "success"}` responses
- Ensure comprehensive IDE support and validation

### 4. Nested Object Handling
**Decision**: Define all nested objects as independent model class files within their respective functional domains
- Create separate model files regardless of complexity
- Place models within their respective functional domain directories
- Create domain-specific variants for cross-domain models
- Use consistent naming without domain prefixes

**Model Distribution Strategy**:
- Each functional domain contains its own version of shared models
- Models maintain consistent naming across domains (e.g., `RetrievalModel`)
- Domain-specific customizations are handled through separate variants
- No central `common/` directory - models belong to their primary use domain

### 5. Method Naming Convention
**Decision**: Use descriptive method names for clarity
- Core CRUD: `create`, `list`, `get`, `update`, `delete`
- Special operations: `retrieve`, `bind_tags`, `unbind_tags`
- Maintain intuitive and self-documenting API interface

### 6. Migration Strategy
**Decision**: Progressive migration with legacy cleanup
- **Migration Approach**: Create new implementations first, then remove old ones after validation
- **Cleanup Timing**: Remove old interfaces immediately after new implementation passes tests
- **Validation Strategy**: Create migration verification tests to ensure behavioral consistency
- **Legacy Handling**: Maintain functional equivalence during transition period

**Specific Migration Tasks**:
- Migrate existing dataset models from flat structure to domain-organized structure
- Replace `hit_test` method with `retrieve` method (with compatibility verification)
- Remove old model files after new implementations are validated
- Update import paths and references throughout the codebase

### 7. Request/Response Model Code Style Rules (MANDATORY)
**Decision**: Strict adherence to established patterns for consistency across all knowledge base APIs

#### Request Model Architecture
**Request Classes**:
- MUST inherit from `BaseRequest` (never from `BaseModel`)
- MUST include `request_body` attribute of type `RequestBody | None`
- MUST use `request_body()` method in builder to accept entire RequestBody object
- Builder variables MUST use full descriptive names (e.g., `self._create_request`, `self._list_request`)
- MUST set `http_method` and `uri` in builder constructor
- Path parameters MUST use `self._request.paths["param_name"] = value` pattern
- Query parameters MUST use `self._request.add_query("key", value)` pattern

**RequestBody Separation (For POST/PATCH/PUT requests)**:
- RequestBody MUST be in separate file from Request
- RequestBody MUST inherit from `pydantic.BaseModel`
- RequestBody MUST include its own Builder pattern
- File naming convention: `create_request.py` and `create_request_body.py`
- Both Request and RequestBody MUST have Builder classes

#### HTTP Method Patterns
**GET Requests** (list, get):
- No RequestBody file needed
- Use query parameters: `self._request.add_query("key", value)`
- Use path parameters: `self._request.paths["param_name"] = value`

**POST Requests** (create, retrieve, bind, etc.):
- Require separate RequestBody file
- Use `request_body()` method in Request builder
- RequestBody builder methods set fields directly

**PATCH/PUT Requests** (update):
- Require separate RequestBody file
- Support path parameters for resource ID
- Use `request_body()` method in Request builder

**DELETE Requests**:
- No RequestBody file needed
- Use path parameters for resource ID

#### Builder Pattern Rules
**Request Builder**:
- Constructor sets `http_method`, `uri`, and initializes request object
- `build()` method returns the request object
- `request_body()` method calls `request_body.model_dump(exclude_none=True, mode="json")`
- Path parameter methods call `self._request.paths["param"] = value`
- Query parameter methods call `self._request.add_query("key", value)`

**RequestBody Builder**:
- Constructor initializes RequestBody object
- Each field method sets `self._request_body.field = value` then returns self
- `build()` method returns the RequestBody object
- No body serialization in RequestBody builder

#### Class Naming Convention (MANDATORY - ZERO TOLERANCE)
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

#### URI and HTTP Method Configuration
**Dataset APIs**:
- `POST /v1/datasets` → `CreateRequest`
- `GET /v1/datasets` → `ListRequest`
- `GET /v1/datasets/:dataset_id` → `GetRequest`
- `PATCH /v1/datasets/:dataset_id` → `UpdateRequest`
- `DELETE /v1/datasets/:dataset_id` → `DeleteRequest`
- `POST /v1/datasets/:dataset_id/retrieve` → `RetrieveRequest`

**Metadata APIs**:
- `POST /v1/datasets/:dataset_id/metadata` → `CreateRequest`
- `GET /v1/datasets/:dataset_id/metadata` → `ListRequest`
- `PATCH /v1/datasets/:dataset_id/metadata/:metadata_id` → `UpdateRequest`
- `DELETE /v1/datasets/:dataset_id/metadata/:metadata_id` → `DeleteRequest`
- `POST /v1/datasets/:dataset_id/metadata/built-in/:action` → `ToggleBuiltinRequest`
- `POST /v1/datasets/:dataset_id/documents/metadata` → `UpdateDocumentRequest`

**Tag APIs**:
- `POST /v1/datasets/tags` → `CreateRequest`
- `GET /v1/datasets/tags` → `ListRequest`
- `PATCH /v1/datasets/tags` → `UpdateRequest`
- `DELETE /v1/datasets/tags` → `DeleteRequest`
- `POST /v1/datasets/tags/binding` → `BindRequest`
- `POST /v1/datasets/tags/unbinding` → `UnbindRequest`
- `POST /v1/datasets/:dataset_id/tags` → `QueryBoundRequest`

#### Pydantic BaseModel Usage
- All RequestBody and Response models MUST inherit from `pydantic.BaseModel`
- Use pydantic's built-in serialization, validation, and type checking
- NO custom `model_dump()` methods allowed
- Builder patterns MUST use pydantic's `model_dump()` method directly
- All fields MUST have proper type hints
- Optional fields MUST use `Optional[Type]` or `Type | None`
- Response classes MUST follow same naming convention as Request classes (no module prefixes)
- ALL classes (Request, RequestBody, Response) must have consistent naming across all resources
- Builder classes must follow same naming pattern as their corresponding model classes

### 8. Model File Organization
**Decision**: Organize models by resource grouping with shared common models

```
model/
├── dataset/          # Dataset-specific models
│   ├── create_request.py      # CreateRequest + CreateRequestBuilder
│   ├── create_request_body.py # CreateRequestBody + CreateRequestBodyBuilder
│   ├── create_response.py     # CreateResponse
│   ├── list_request.py        # ListRequest + ListRequestBuilder (GET)
│   ├── list_response.py       # ListResponse
│   ├── get_request.py         # GetRequest + GetRequestBuilder (GET)
│   ├── get_response.py        # GetResponse
│   ├── update_request.py      # UpdateRequest + UpdateRequestBuilder
│   ├── update_request_body.py # UpdateRequestBody + UpdateRequestBodyBuilder
│   ├── update_response.py     # UpdateResponse
│   ├── delete_request.py      # DeleteRequest + DeleteRequestBuilder (DELETE)
│   ├── delete_response.py     # DeleteResponse
│   ├── retrieve_request.py    # RetrieveRequest + RetrieveRequestBuilder
│   ├── retrieve_request_body.py # RetrieveRequestBody + RetrieveRequestBodyBuilder
│   ├── retrieve_response.py   # RetrieveResponse
│   ├── list_request.py
│   ├── list_response.py
│   ├── get_request.py
│   ├── get_response.py
│   ├── update_request.py
│   ├── update_response.py
│   ├── delete_request.py
│   ├── delete_response.py
│   ├── retrieve_request.py
│   ├── retrieve_response.py
│   ├── retrieval_model.py
│   ├── reranking_model.py
│   ├── filter_condition.py
│   ├── metadata_filtering_conditions.py
│   ├── external_knowledge_info.py
│   ├── dataset_info.py
│   └── tag_info.py
├── metadata/         # Metadata management models
│   ├── create_request.py
│   ├── create_response.py
│   ├── list_request.py
│   ├── list_response.py
│   ├── update_request.py
│   ├── update_response.py
│   ├── delete_request.py
│   ├── delete_response.py
│   ├── toggle_builtin_request.py
│   ├── toggle_builtin_response.py
│   ├── update_document_request.py
│   ├── update_document_response.py
│   └── metadata_info.py
└── tag/             # Tag management models
    ├── create_request.py
    ├── create_response.py
    ├── list_request.py
    ├── list_response.py
    ├── update_request.py
    ├── update_response.py
    ├── delete_request.py
    ├── delete_response.py
    ├── bind_request.py
    ├── bind_response.py
    ├── unbind_request.py
    ├── unbind_response.py
    ├── query_bound_request.py
    ├── query_bound_response.py
    └── tag_info.py
```

## API Implementation Plan

### Dataset Management APIs (6 APIs)

#### Existing Methods (Mixed Approach)
1. **POST /datasets** → `dataset.create()` - Keep existing, verify compliance
2. **GET /datasets** → `dataset.list()` - Keep existing, verify compliance  
3. **DELETE /datasets/{dataset_id}** → `dataset.delete()` - Keep existing, verify compliance

#### New Methods to Add
4. **GET /datasets/{dataset_id}** → `dataset.get()` - New implementation
5. **PATCH /datasets/{dataset_id}** → `dataset.update()` - New implementation
6. **POST /datasets/{dataset_id}/retrieve** → `dataset.retrieve()` - Replace existing hit_test

### Metadata Management APIs (7 APIs)

#### Metadata CRUD
1. **POST /datasets/{dataset_id}/metadata** → `metadata.create()`
2. **GET /datasets/{dataset_id}/metadata** → `metadata.list()`
3. **PATCH /datasets/{dataset_id}/metadata/{metadata_id}** → `metadata.update()`
4. **DELETE /datasets/{dataset_id}/metadata/{metadata_id}** → `metadata.delete()`

#### Built-in Metadata Management
5. **POST /datasets/{dataset_id}/metadata/built-in/{action}** → `metadata.toggle_builtin()`

#### Document Metadata Operations
6. **POST /datasets/{dataset_id}/documents/metadata** → `metadata.update_document()`

### Tag Management APIs (7 APIs)

#### Tag CRUD (Global Operations)
1. **POST /datasets/tags** → `tag.create()`
2. **GET /datasets/tags** → `tag.list()`
3. **PATCH /datasets/tags** → `tag.update()`
4. **DELETE /datasets/tags** → `tag.delete()`

#### Tag Binding Operations
5. **POST /datasets/tags/binding** → `tag.bind_tags()`
6. **POST /datasets/tags/unbinding** → `tag.unbind_tags()`

#### Tag Query Operations
7. **POST /datasets/{dataset_id}/tags** → `tag.query_bound()`

## Technical Implementation Details

### Resource Class Structure
```python
# Example: dataset resource
class Dataset:
    def __init__(self, config: Config):
        self.config = config
    
    def create(self, request: CreateRequest, request_option: RequestOption) -> CreateResponse:
        return Transport.execute(self.config, request, unmarshal_as=CreateResponse, option=request_option)
    
    async def acreate(self, request: CreateRequest, request_option: RequestOption) -> CreateResponse:
        return await ATransport.aexecute(self.config, request, unmarshal_as=CreateResponse, option=request_option)
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
        self.request_body: CreateRequestBody | None = None

    @staticmethod
    def builder() -> CreateRequestBuilder:
        return CreateRequestBuilder()

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

```python
# create_request_body.py
from typing import Optional
from pydantic import BaseModel
from .retrieval_model import RetrievalModel

class CreateRequestBody(BaseModel):
    name: str | None = None
    description: Optional[str] = None
    retrieval_model: Optional[RetrievalModel] = None
    
    @staticmethod
    def builder() -> CreateRequestBodyBuilder:
        return CreateRequestBodyBuilder()

class CreateRequestBodyBuilder:
    def __init__(self):
        create_request_body = CreateRequestBody()
        self._create_request_body = create_request_body

    def build(self) -> CreateRequestBody:
        return self._create_request_body

    def name(self, name: str) -> CreateRequestBodyBuilder:
        self._create_request_body.name = name
        return self

    def description(self, description: str) -> CreateRequestBodyBuilder:
        self._create_request_body.description = description
        return self
```

#### GET Request Pattern (with query parameters)
```python
# list_request.py
from typing import List
from dify_oapi.core.enum import HttpMethod
from dify_oapi.core.model.base_request import BaseRequest

class ListRequest(BaseRequest):
    def __init__(self):
        super().__init__()

    @staticmethod
    def builder() -> ListRequestBuilder:
        return ListRequestBuilder()

class ListRequestBuilder:
    def __init__(self):
        list_request = ListRequest()
        list_request.http_method = HttpMethod.GET
        list_request.uri = "/v1/datasets"
        self._list_request = list_request

    def build(self) -> ListRequest:
        return self._list_request

    def keyword(self, keyword: str) -> ListRequestBuilder:
        self._list_request.add_query("keyword", keyword)
        return self

    def page(self, page: int) -> ListRequestBuilder:
        self._list_request.add_query("page", page)
        return self
```

#### GET Request Pattern (with path parameters)
```python
# get_request.py
from dify_oapi.core.enum import HttpMethod
from dify_oapi.core.model.base_request import BaseRequest

class GetRequest(BaseRequest):
    def __init__(self):
        super().__init__()
        self.dataset_id: str | None = None

    @staticmethod
    def builder() -> GetRequestBuilder:
        return GetRequestBuilder()

class GetRequestBuilder:
    def __init__(self):
        get_request = GetRequest()
        get_request.http_method = HttpMethod.GET
        get_request.uri = "/v1/datasets/:dataset_id"
        self._get_request = get_request

    def build(self) -> GetRequest:
        return self._get_request

    def dataset_id(self, dataset_id: str) -> GetRequestBuilder:
        self._get_request.dataset_id = dataset_id
        self._get_request.paths["dataset_id"] = dataset_id
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

    @staticmethod
    def builder() -> DeleteRequestBuilder:
        return DeleteRequestBuilder()

class DeleteRequestBuilder:
    def __init__(self):
        delete_request = DeleteRequest()
        delete_request.http_method = HttpMethod.DELETE
        delete_request.uri = "/v1/datasets/:dataset_id"
        self._delete_request = delete_request

    def build(self) -> DeleteRequest:
        return self._delete_request

    def dataset_id(self, dataset_id: str) -> DeleteRequestBuilder:
        self._delete_request.dataset_id = dataset_id
        self._delete_request.paths["dataset_id"] = dataset_id
        return self
```

### Version Integration
Update `v1/version.py` to include new resources:
```python
class V1:
    def __init__(self, config: Config):
        self.dataset = Dataset(config)
        self.document = Document(config)
        self.segment = Segment(config)
        self.metadata = Metadata(config)  # New
        self.tag = Tag(config)            # New
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

### Test Directory Structure
```
tests/
└── knowledge_base/
    └── v1/
        ├── model/
        │   ├── test_dataset_models.py
        │   ├── test_metadata_models.py
        │   └── test_tag_models.py
        ├── resource/
        │   ├── test_dataset_resource.py
        │   ├── test_metadata_resource.py
        │   └── test_tag_resource.py
        ├── integration/
        │   ├── test_dataset_api_integration.py
        │   ├── test_metadata_api_integration.py
        │   ├── test_tag_api_integration.py
        │   ├── test_comprehensive_integration.py
        │   ├── test_examples_validation.py
        │   └── test_version_integration.py
        └── __init__.py
```

### Test Code Quality Requirements
- **Comprehensive typing hints**: All test method parameters and return types must include proper type annotations
- Use `typing.Any` for complex mock objects like `monkeypatch`
- Include return type annotations (typically `-> None` for test methods)
- Import necessary typing modules at the top of test files

## Migration Impact

### Breaking Changes
- Complete rewrite of existing dataset-related functionality
- New model structure requires import path updates
- Method signature changes for existing APIs
- New retrieve method replaces hit_test method

### Benefits
- Full API coverage with 19 dataset management endpoints
- Improved type safety and developer experience
- Consistent architecture across all knowledge base features
- Enhanced maintainability and extensibility

## Examples Strategy

### Examples Organization
**Decision**: Resource-based directory structure with API-specific files
- Each resource gets its own directory under `examples/knowledge_base/`
- Each API gets its own file within the resource directory
- Each file contains both sync and async examples
- Basic try-catch error handling for educational purposes

### Examples Directory Structure
```
examples/knowledge_base/
├── dataset/
│   ├── create.py          # Create dataset examples (sync + async)
│   ├── list.py            # List datasets examples (sync + async)
│   ├── get.py             # Get dataset details examples (sync + async)
│   ├── update.py          # Update dataset examples (sync + async)
│   ├── delete.py          # Delete dataset examples (sync + async)
│   └── retrieve.py        # Dataset retrieval examples (sync + async)
├── metadata/
│   ├── create.py          # Create metadata examples (sync + async)
│   ├── list.py            # List metadata examples (sync + async)
│   ├── update.py          # Update metadata examples (sync + async)
│   ├── delete.py          # Delete metadata examples (sync + async)
│   ├── toggle_builtin.py  # Toggle built-in metadata examples (sync + async)
│   └── update_document.py # Update document metadata examples (sync + async)
├── tag/
│   ├── create.py          # Create tag examples (sync + async)
│   ├── list.py            # List tags examples (sync + async)
│   ├── update.py          # Update tag examples (sync + async)
│   ├── delete.py          # Delete tag examples (sync + async)
│   ├── bind.py            # Bind tags examples (sync + async)
│   ├── unbind.py          # Unbind tag examples (sync + async)
│   └── query_bound.py     # Query bound tags examples (sync + async)
└── README.md              # Examples overview and usage guide
```

### Examples Content Strategy
- **Simple API Calls**: Each example focuses on a single API operation
- **Educational Purpose**: Clear comments explaining each step
- **Dual Versions**: Both synchronous and asynchronous implementations
- **Basic Error Handling**: Simple try-catch blocks for common exceptions
- **Real-world Data**: Use realistic but simple test data
- **Integration Reference**: Examples can serve as integration test references
- **Documentation Support**: Examples complement API documentation
- **Main README Update**: Always update `examples/README.md` to include new examples with proper categorization and descriptions

## Summary

This design provides a comprehensive solution for dataset management in dify-oapi, covering all 19 dataset-related APIs with a clean, maintainable architecture. The implementation prioritizes type safety, consistency, and developer experience while ensuring full compatibility with the latest Dify API specifications.

The modular resource-based organization, combined with shared common models and descriptive method naming, creates an intuitive and powerful interface for dataset management operations including CRUD operations, metadata management, tag management, and advanced retrieval functionality.

The examples strategy ensures developers have clear, educational references for every API operation, supporting both learning and integration testing needs with comprehensive sync/async coverage.