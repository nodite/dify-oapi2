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

#### Public Class Inheritance Rules (CRITICAL)
**Public/Common Classes**:
- Public classes (DatasetInfo, TagInfo, MetadataInfo, RetrievalModel, etc.) MUST inherit from `pydantic.BaseModel` ONLY
- Public classes MUST NOT inherit from `BaseResponse`
- Public classes MUST have Builder patterns for consistency and ease of use
- Public classes are reusable components that can be used across different contexts
- Examples: `DatasetInfo`, `TagInfo`, `MetadataInfo`, `RetrievalModel`, `RerankingModel`, `ExternalKnowledgeInfo`

**Response Classes**:
- Response classes MUST inherit from `BaseResponse` for error handling capabilities
- Response classes MAY use multiple inheritance when they need to include public class data
- Pattern: `class CreateResponse(DatasetInfo, BaseResponse):`
- This allows response classes to have both data fields and error handling capabilities
- Response classes MUST NOT have Builder patterns (unlike Request classes)

**Builder Pattern Rules**:
- Request, RequestBody, and Public/Common classes MUST have Builder patterns
- Public/common classes can be instantiated directly using Pydantic's standard initialization OR via builder pattern
- Response classes should be instantiated by the transport layer, not manually
- Builder patterns provide fluent interface for complex object construction

**Inheritance Examples**:
```python
# ✅ CORRECT: Public class inherits from BaseModel with Builder pattern
class DatasetInfo(BaseModel):
    id: Optional[str] = None
    name: Optional[str] = None
    # ... other fields
    
    @staticmethod
    def builder() -> DatasetInfoBuilder:
        return DatasetInfoBuilder()

class DatasetInfoBuilder:
    def __init__(self):
        self._dataset_info = DatasetInfo()
    
    def build(self) -> DatasetInfo:
        return self._dataset_info
    
    def id(self, id: str) -> DatasetInfoBuilder:
        self._dataset_info.id = id
        return self
    
    def name(self, name: str) -> DatasetInfoBuilder:
        self._dataset_info.name = name
        return self

# ✅ CORRECT: Response class uses multiple inheritance, no Builder
class CreateResponse(DatasetInfo, BaseResponse):
    """Response model for dataset creation API"""
    pass  # NO builder() method or Builder class

# ✅ CORRECT: Public classes can be instantiated directly OR via builder
dataset_info = DatasetInfo(id="123", name="Test Dataset")
# OR
dataset_info = DatasetInfo.builder().id("123").name("Test Dataset").build()

# ❌ WRONG: Public class inheriting from BaseResponse
class DatasetInfo(BaseResponse):  # DON'T DO THIS
    # ...

# ❌ WRONG: Response class only inheriting from public class
class CreateResponse(DatasetInfo):  # Missing BaseResponse
    # ...
```

### 8. Public Class Builder Pattern Rules (MANDATORY)
**Decision**: All public classes MUST implement builder patterns for consistency and usability

#### Builder Pattern Implementation Requirements
**Scope**: All public/common classes that inherit from `pydantic.BaseModel`
- **Target Classes**: `DatasetInfo`, `TagInfo`, `MetadataInfo`, `RetrievalModel`, `RerankingModel`, `ExternalKnowledgeInfo`, `FilterCondition`, `MetadataFilteringConditions`, `KeywordSetting`, `VectorSetting`, `Weights`, `Document`, `DocumentDataSourceInfo`, `DocumentDataSourceDetailDict`, `DocumentDataSourceDetailDictUploadFile`, `Segment`, and all other public model classes
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

#### Builder Method Naming Rules
**Field Method Names**:
- Method names MUST match field names exactly
- Use snake_case for method names (matching field names)
- Handle reserved keywords by using trailing underscore (e.g., `id_()` for `id` field)
- Complex nested objects should accept the nested object type as parameter

#### Forward Reference Handling
**Import Requirements**:
- ALL public class files MUST include `from __future__ import annotations` at the top
- This prevents forward reference issues when builder methods reference the builder class
- Essential for proper type hints in `@staticmethod` decorators

#### Usage Flexibility
**Instantiation Options**:
- Direct instantiation: `obj = PublicClass(field1="value", field2=123)`
- Builder pattern: `obj = PublicClass.builder().field1("value").field2(123).build()`
- Both approaches are valid and should be supported
- Builder pattern provides fluent interface for complex object construction
- Direct instantiation is suitable for simple cases

#### Validation and Type Safety
**Requirements**:
- All builder methods MUST include proper type hints
- Builder methods MUST return the builder instance for method chaining
- `build()` method MUST return the target class instance
- Leverage Pydantic's built-in validation (no custom validation in builders)
- Use `Optional[Type]` or `Type | None` for optional fields

#### Testing Requirements
**Builder Testing**:
- Unit tests MUST verify builder pattern functionality for all public classes
- Test both direct instantiation and builder pattern approaches
- Verify method chaining works correctly
- Test serialization/deserialization with builder-created objects
- Validate type hints and return types

#### Benefits of Public Class Builders
**Developer Experience**:
- Consistent API across all public classes
- Fluent interface for complex object construction
- Better IDE support with method chaining
- Improved readability for complex object initialization
- Easier testing and mocking
- Enhanced maintainability

#### Implementation Examples
**Simple Public Class**:
```python
from __future__ import annotations
from pydantic import BaseModel

class TagInfo(BaseModel):
    id: str
    name: str
    type: str | None = None
    binding_count: int | None = None

    @staticmethod
    def builder() -> TagInfoBuilder:
        return TagInfoBuilder()

class TagInfoBuilder:
    def __init__(self):
        self._tag_info = TagInfo(id="", name="")

    def build(self) -> TagInfo:
        return self._tag_info

    def id(self, id: str) -> TagInfoBuilder:
        self._tag_info.id = id
        return self

    def name(self, name: str) -> TagInfoBuilder:
        self._tag_info.name = name
        return self

    def type(self, type: str) -> TagInfoBuilder:
        self._tag_info.type = type
        return self

    def binding_count(self, binding_count: int) -> TagInfoBuilder:
        self._tag_info.binding_count = binding_count
        return self
```

**Complex Public Class with Nested Objects**:
```python
from __future__ import annotations
from pydantic import BaseModel
from .reranking_model import RerankingModel
from .metadata_filtering_conditions import MetadataFilteringConditions

class RetrievalModel(BaseModel):
    search_method: str | None = None
    reranking_enable: bool | None = None
    reranking_model: RerankingModel | None = None
    top_k: int | None = None
    metadata_filtering_conditions: MetadataFilteringConditions | None = None

    @staticmethod
    def builder() -> RetrievalModelBuilder:
        return RetrievalModelBuilder()

class RetrievalModelBuilder:
    def __init__(self):
        self._retrieval_model = RetrievalModel()

    def build(self) -> RetrievalModel:
        return self._retrieval_model

    def search_method(self, search_method: str) -> RetrievalModelBuilder:
        self._retrieval_model.search_method = search_method
        return self

    def reranking_enable(self, reranking_enable: bool) -> RetrievalModelBuilder:
        self._retrieval_model.reranking_enable = reranking_enable
        return self

    def reranking_model(self, reranking_model: RerankingModel) -> RetrievalModelBuilder:
        self._retrieval_model.reranking_model = reranking_model
        return self

    def top_k(self, top_k: int) -> RetrievalModelBuilder:
        self._retrieval_model.top_k = top_k
        return self

    def metadata_filtering_conditions(self, metadata_filtering_conditions: MetadataFilteringConditions) -> RetrievalModelBuilder:
        self._retrieval_model.metadata_filtering_conditions = metadata_filtering_conditions
        return self
```

### 9. Model File Organization
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
- **Test File Organization**: All model tests MUST follow flat structure in `tests/knowledge_base/v1/model/` directory
- **Naming Consistency**: Use `test_{resource}_models.py` pattern for all model test files
- **No Nested Directories**: Avoid creating resource-specific test subdirectories

### Test File Organization Rules (MANDATORY)
**Decision**: Test files MUST be organized in a flat structure within the model directory
- **Flat Structure**: All model test files are placed directly in `tests/knowledge_base/v1/model/` directory
- **No Subdirectories**: Do NOT create resource-specific subdirectories like `model/dataset/`, `model/metadata/`
- **Naming Convention**: Use `test_{resource}_models.py` pattern (e.g., `test_dataset_models.py`, `test_metadata_models.py`)
- **Consistency**: Follow the same pattern across all knowledge base resources
- **Rationale**: Maintains consistency with existing codebase structure and simplifies test discovery

### Test Directory Structure
```
tests/
└── knowledge_base/
    └── v1/
        ├── model/
        │   ├── test_dataset_models.py     # Dataset model tests (flat structure)
        │   ├── test_metadata_models.py    # Metadata model tests (flat structure)
        │   ├── test_tag_models.py         # Tag model tests (flat structure)
        │   └── test_document_models.py    # Document model tests (flat structure)
        ├── resource/
        │   ├── test_dataset_resource.py
        │   ├── test_metadata_resource.py
        │   ├── test_tag_resource.py
        │   └── test_document_resource.py
        ├── integration/
        │   ├── test_dataset_api_integration.py
        │   ├── test_metadata_api_integration.py
        │   ├── test_tag_api_integration.py
        │   ├── test_document_api_integration.py
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

### Resource Naming Convention (MANDATORY)
**Decision**: All example resources MUST use "[Example]" prefix for safety
- **Creation Rule**: All resources created in examples MUST have "[Example]" prefix in their names
- **Deletion Rule**: Delete operations MUST only target resources with "[Example]" prefix
- **Safety Measure**: This prevents accidental deletion of production or important resources
- **Applies to**: Datasets, tags, metadata fields, and any other named resources
- **Examples**:
  - Dataset names: "[Example] My Test Dataset", "[Example] API Documentation"
  - Tag names: "[Example] Tutorial", "[Example] API Reference"
  - Metadata names: "[Example] category", "[Example] priority"
- **Cleanup Functions**: Each delete example should include a cleanup function that removes all "[Example]" prefixed resources

### Code Minimalism Strategy
**Decision**: All examples follow minimal code principles while maintaining functionality
- **Objective**: Write only the ABSOLUTE MINIMAL amount of code needed to demonstrate each API correctly
- **Avoid Verbose Implementations**: Remove any code that doesn't directly contribute to the core demonstration
- **Simplify Output**: Reduce verbose logging and status messages to essential information only
- **Remove Redundant Functions**: Eliminate multiple similar functions that don't add educational value
- **Maintain Core Functionality**: Ensure all essential features and safety checks remain intact

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

### Environment Variable Validation (MANDATORY)
**Decision**: All examples MUST validate required environment variables and raise errors
- **Validation Rule**: Check for required environment variables at the start of each function
- **Error Handling**: Raise `ValueError` with descriptive message if required variables are missing
- **No Print Fallbacks**: NEVER use `print()` statements for missing environment variables
- **Required Variables**: All examples must validate `API_KEY`, resource-specific examples must validate resource IDs
- **Validation Order**: ALL environment variable validations MUST be placed at the very beginning of each function, immediately after the try block
- **Examples**:
  ```python
  def example_function() -> None:
      try:
          # Check required environment variables (MUST be first)
          api_key = os.getenv("API_KEY")
          if not api_key:
              raise ValueError("API_KEY environment variable is required")
          
          dataset_id = os.getenv("DATASET_ID")
          if not dataset_id:
              raise ValueError("DATASET_ID environment variable is required")
          
          # Initialize client and other logic after validation
          client = Client.builder().domain(os.getenv("DOMAIN", "https://api.dify.ai")).build()
          # ... rest of function
  ```
- **Consistency**: Apply this pattern to ALL functions in ALL examples
- **Main Function**: Remove environment variable checks from main() functions
- **Zero Tolerance**: This rule applies to ALL knowledge base examples without exception

### Examples Content Strategy
- **Simple API Calls**: Each example focuses on a single API operation with minimal code
- **Educational Purpose**: Essential functionality demonstration without verbose explanations
- **Dual Versions**: Both synchronous and asynchronous implementations (mandatory)
- **Environment Validation**: All functions validate required environment variables and raise errors
- **Basic Error Handling**: Simple try-catch blocks for common exceptions
- **Real-world Data**: Use realistic but simple test data with "[Example]" prefix
- **Safety First**: All resource creation uses "[Example]" prefix, all deletion checks for this prefix
- **Cleanup Functions**: Delete examples include functions to clean up all example resources
- **Integration Reference**: Examples can serve as integration test references
- **Documentation Support**: Examples complement API documentation with minimal overhead
- **Main README Update**: Always update `examples/README.md` to include new examples with proper categorization and descriptions
- **Code Minimalism**: Follow the principle of writing only essential code that directly demonstrates the API functionality

## Latest Improvements and Optimizations

### 1. Enhanced Code Architecture
**Recent Updates**:
- **Streamlined Model Organization**: Refined the model file structure for better maintainability
- **Improved Builder Patterns**: Enhanced builder pattern implementation for better type safety
- **Optimized Import Structure**: Simplified import paths and reduced circular dependencies
- **Enhanced Error Handling**: Improved error propagation and handling mechanisms

### 2. Performance Optimizations
**Implementation Enhancements**:
- **Reduced Memory Footprint**: Optimized model instantiation and data handling
- **Faster Request Processing**: Streamlined request building and validation
- **Improved Async Support**: Enhanced asynchronous operation handling
- **Better Resource Management**: Optimized resource allocation and cleanup

### 3. Developer Experience Improvements
**Latest Features**:
- **Enhanced Type Hints**: More comprehensive type annotations for better IDE support
- **Improved Documentation**: Better inline documentation and examples
- **Simplified API Usage**: More intuitive method signatures and parameter handling
- **Better Error Messages**: More descriptive error messages for debugging

### 4. Testing and Quality Assurance
**Recent Enhancements**:
- **Comprehensive Test Coverage**: Expanded test suite covering all edge cases
- **Performance Testing**: Added performance benchmarks and optimization tests
- **Integration Testing**: Enhanced integration tests with real API scenarios
- **Code Quality Metrics**: Improved code quality monitoring and enforcement

### 5. Examples and Documentation
**Latest Updates**:
- **Interactive Examples**: More practical, real-world usage examples
- **Performance Guidelines**: Best practices for optimal API usage
- **Troubleshooting Guide**: Common issues and solutions documentation
- **Migration Assistance**: Detailed migration guides for existing users

## Summary

This design provides a comprehensive solution for dataset management in dify-oapi, covering all 19 dataset-related APIs with a clean, maintainable architecture. The implementation prioritizes type safety, consistency, and developer experience while ensuring full compatibility with the latest Dify API specifications.

The modular resource-based organization, combined with shared common models and descriptive method naming, creates an intuitive and powerful interface for dataset management operations including CRUD operations, metadata management, tag management, and advanced retrieval functionality.

The examples strategy ensures developers have clear, educational references for every API operation, supporting both learning and integration testing needs with comprehensive sync/async coverage. The recent refactoring effort has optimized all examples for code minimalism while maintaining full functionality and safety features.

### Key Features
- **Code Minimalism**: All knowledge base examples follow minimal code principles
- **Improved Readability**: Simplified output messages and reduced verbose logging
- **Maintained Safety**: All safety features and validation remain intact
- **Consistent Patterns**: Uniform minimization approach across all 19 API examples
- **Educational Focus**: Examples focus purely on demonstrating API functionality without unnecessary complexity
- **Performance Optimization**: Enhanced request processing and resource management
- **Enhanced Type Safety**: Improved type annotations and validation mechanisms
- **Better Error Handling**: Robust error propagation and user-friendly error messages