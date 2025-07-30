# Document API Design Document

## Overview

This document outlines the design for implementing comprehensive document management functionality in the dify-oapi knowledge_base module. The implementation will support all 10 document-related APIs covering document CRUD operations, file management, status management, and indexing operations.

## Design Decisions

### 1. Resource Organization
**Decision**: Extend existing `document` resource class within knowledge_base module
- Continue using the established single resource class approach
- Add 3 missing methods to existing `document` resource: `get()`, `update_status()`, `get_upload_file()`
- Maintain consistency with current implementation patterns
- Leverage existing infrastructure and method naming conventions

### 2. Model File Organization Strategy
**Decision**: Complete migration to new directory structure with full legacy cleanup
- **Migration Approach**: Create new `model/document/` directory structure
- **Scope**: Migrate ALL existing 7 APIs + add 3 new APIs (total 10 APIs)
- **Naming Convention**: Use simplified names following dataset design patterns
- **Legacy Cleanup**: Remove all old model files after migration completion
- **Import Updates**: Update all import paths throughout the codebase

### 3. Method Naming Convention
**Decision**: Preserve existing method names for backward compatibility
- **Existing Methods**: Keep current naming patterns
  - `create_by_text()`, `create_by_file()`
  - `update_by_text()`, `update_by_file()`
  - `indexing_status()`
  - `list()`, `delete()`
- **New Methods**: Add with descriptive names
  - `get()` - Get document details
  - `update_status()` - Batch update document status
  - `get_upload_file()` - Get upload file information

### 4. Shared Model Strategy
**Decision**: Independent model files for each resource domain
- Each resource maintains its own version of shared models
- `model/document/` contains all document-specific models
- No central `common/` directory - models belong to their primary use domain
- Allow domain-specific customizations through separate variants
- Consistent naming without domain prefixes

### 5. Request/Response Model Code Style Rules (MANDATORY)
**Decision**: Strict adherence to established patterns for consistency

#### Request Model Architecture
**Request Classes**:
- MUST inherit from `BaseRequest` (never from `BaseModel`)
- MUST include `request_body` attribute of type `RequestBody | None` for POST/PATCH requests
- MUST use `request_body()` method in builder to accept entire RequestBody object
- Builder variables MUST use full descriptive names (e.g., `self._create_by_text_request`)
- MUST set `http_method` and `uri` in builder constructor
- Path parameters MUST use `self._request.paths["param_name"] = value` pattern
- Query parameters MUST use `self._request.add_query("key", value)` pattern

**RequestBody Separation (For POST/PATCH requests)**:
- RequestBody MUST be in separate file from Request
- RequestBody MUST inherit from `pydantic.BaseModel`
- RequestBody MUST include its own Builder pattern
- File naming convention: `create_by_text_request.py` and `create_by_text_request_body.py`
- Both Request and RequestBody MUST have Builder classes

#### HTTP Method Patterns
**GET Requests** (list, get, get_upload_file):
- No RequestBody file needed
- Use query parameters: `self._request.add_query("key", value)`
- Use path parameters: `self._request.paths["param_name"] = value`

**POST Requests** (create_by_text, create_by_file, update_status):
- Require separate RequestBody file
- Use `request_body()` method in Request builder
- RequestBody builder methods set fields directly

**PATCH Requests** (update_by_text, update_by_file):
- Require separate RequestBody file
- Support path parameters for resource ID
- Use `request_body()` method in Request builder

**DELETE Requests** (delete):
- No RequestBody file needed
- Use path parameters for resource ID

#### Class Naming Convention (MANDATORY - ZERO TOLERANCE)
**Universal Naming Pattern**:
- File names determine class names exactly (e.g., `create_by_text_request.py` → `CreateByTextRequest`)
- Each class has corresponding Builder (e.g., `CreateByTextRequest` + `CreateByTextRequestBuilder`)
- Pattern applies to all model types: Request, RequestBody, Response

**STRICT Naming Rules (NO EXCEPTIONS)**:
- Remove ALL module/domain prefixes from class names
- Class names MUST match file names exactly (case-sensitive)
- Use operation-based names: `CreateByTextRequest`, `ListResponse`, `UpdateByTextRequestBody`
- NEVER use domain-specific names: `CreateDocumentByTextRequest`, `DocumentListResponse`
- NO legacy naming patterns allowed
- Consistent across all HTTP methods and operation types

#### URI and HTTP Method Configuration
**Document APIs**:
- `POST /v1/datasets/:dataset_id/document/create-by-text` → `CreateByTextRequest`
- `POST /v1/datasets/:dataset_id/document/create-by-file` → `CreateByFileRequest`
- `POST /v1/datasets/:dataset_id/documents/:document_id/update-by-text` → `UpdateByTextRequest`
- `POST /v1/datasets/:dataset_id/documents/:document_id/update-by-file` → `UpdateByFileRequest`
- `GET /v1/datasets/:dataset_id/documents/:batch/indexing-status` → `IndexingStatusRequest`
- `DELETE /v1/datasets/:dataset_id/documents/:document_id` → `DeleteRequest`
- `GET /v1/datasets/:dataset_id/documents` → `ListRequest`
- `GET /v1/datasets/:dataset_id/documents/:document_id` → `GetRequest`
- `PATCH /v1/datasets/:dataset_id/documents/status/:action` → `UpdateStatusRequest`
- `GET /v1/datasets/:dataset_id/documents/:document_id/upload-file` → `GetUploadFileRequest`

#### Public Class Inheritance Rules (CRITICAL)
**Public/Common Classes**:
- Public classes (DocumentInfo, ProcessRule, PreProcessingRule, Segmentation, etc.) MUST inherit from `pydantic.BaseModel` ONLY
- Public classes MUST NOT inherit from `BaseResponse`
- Public classes MUST have Builder patterns for consistency and ease of use
- Public classes are reusable components that can be used across different contexts
- Examples: `DocumentInfo`, `ProcessRule`, `PreProcessingRule`, `Segmentation`, `DataSourceInfo`, `UploadFileInfo`

**Response Classes**:
- Response classes MUST inherit from `BaseResponse` for error handling capabilities
- Response classes MAY use multiple inheritance when they need to include public class data
- Pattern: `class CreateByTextResponse(DocumentInfo, BaseResponse):`
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
class DocumentInfo(BaseModel):
    id: Optional[str] = None
    name: Optional[str] = None
    # ... other fields
    
    @staticmethod
    def builder() -> DocumentInfoBuilder:
        return DocumentInfoBuilder()

class DocumentInfoBuilder:
    def __init__(self):
        self._document_info = DocumentInfo()
    
    def build(self) -> DocumentInfo:
        return self._document_info
    
    def id(self, id: str) -> DocumentInfoBuilder:
        self._document_info.id = id
        return self
    
    def name(self, name: str) -> DocumentInfoBuilder:
        self._document_info.name = name
        return self

# ✅ CORRECT: Response class uses multiple inheritance, no Builder
class CreateByTextResponse(DocumentInfo, BaseResponse):
    """Response model for create document by text API"""
    pass  # NO builder() method or Builder class

# ✅ CORRECT: Public classes can be instantiated directly OR via builder
document_info = DocumentInfo(id="123", name="Test Document")
# OR
document_info = DocumentInfo.builder().id("123").name("Test Document").build()

# ❌ WRONG: Public class inheriting from BaseResponse
class DocumentInfo(BaseResponse):  # DON'T DO THIS
    # ...

# ❌ WRONG: Response class only inheriting from public class
class CreateByTextResponse(DocumentInfo):  # Missing BaseResponse
    # ...
```

### 8. Public Class Builder Pattern Rules (MANDATORY)
**Decision**: All public classes MUST implement builder patterns for consistency and usability

#### Builder Pattern Implementation Requirements
**Scope**: All public/common classes that inherit from `pydantic.BaseModel`
- **Target Classes**: `DocumentInfo`, `ProcessRule`, `PreProcessingRule`, `Segmentation`, `DataSourceInfo`, `UploadFileInfo`, `IndexingStatusInfo`, `Document`, `DocumentDataSourceInfo`, `DocumentDataSourceDetailDict`, `DocumentDataSourceDetailDictUploadFile`, `Segment`, and all other public model classes
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

#### Document-Specific Implementation Examples
**Document Processing Rule**:
```python
from __future__ import annotations
from pydantic import BaseModel
from .segmentation import Segmentation
from .pre_processing_rule import PreProcessingRule

class ProcessRule(BaseModel):
    mode: str | None = None
    pre_processing_rules: list[PreProcessingRule] | None = None
    segmentation: Segmentation | None = None

    @staticmethod
    def builder() -> ProcessRuleBuilder:
        return ProcessRuleBuilder()

class ProcessRuleBuilder:
    def __init__(self):
        self._process_rule = ProcessRule()

    def build(self) -> ProcessRule:
        return self._process_rule

    def mode(self, mode: str) -> ProcessRuleBuilder:
        self._process_rule.mode = mode
        return self

    def pre_processing_rules(self, pre_processing_rules: list[PreProcessingRule]) -> ProcessRuleBuilder:
        self._process_rule.pre_processing_rules = pre_processing_rules
        return self

    def segmentation(self, segmentation: Segmentation) -> ProcessRuleBuilder:
        self._process_rule.segmentation = segmentation
        return self
```

**Document Information**:
```python
from __future__ import annotations
from pydantic import BaseModel
from .data_source_info import DataSourceInfo

class DocumentInfo(BaseModel):
    id: str | None = None
    name: str | None = None
    data_source_type: str | None = None
    data_source_info: DataSourceInfo | None = None
    tokens: int | None = None
    indexing_status: str | None = None
    enabled: bool | None = None
    word_count: int | None = None
    hit_count: int | None = None

    @staticmethod
    def builder() -> DocumentInfoBuilder:
        return DocumentInfoBuilder()

class DocumentInfoBuilder:
    def __init__(self):
        self._document_info = DocumentInfo()

    def build(self) -> DocumentInfo:
        return self._document_info

    def id(self, id: str) -> DocumentInfoBuilder:
        self._document_info.id = id
        return self

    def name(self, name: str) -> DocumentInfoBuilder:
        self._document_info.name = name
        return self

    def data_source_type(self, data_source_type: str) -> DocumentInfoBuilder:
        self._document_info.data_source_type = data_source_type
        return self

    def data_source_info(self, data_source_info: DataSourceInfo) -> DocumentInfoBuilder:
        self._document_info.data_source_info = data_source_info
        return self

    def tokens(self, tokens: int) -> DocumentInfoBuilder:
        self._document_info.tokens = tokens
        return self

    def indexing_status(self, indexing_status: str) -> DocumentInfoBuilder:
        self._document_info.indexing_status = indexing_status
        return self

    def enabled(self, enabled: bool) -> DocumentInfoBuilder:
        self._document_info.enabled = enabled
        return self

    def word_count(self, word_count: int) -> DocumentInfoBuilder:
        self._document_info.word_count = word_count
        return self

    def hit_count(self, hit_count: int) -> DocumentInfoBuilder:
        self._document_info.hit_count = hit_count
        return self
```

## API Implementation Plan

### Document Management APIs (10 APIs)

#### Existing Methods (Migration Required)
1. **POST /datasets/{dataset_id}/document/create-by-text** → `document.create_by_text()` - Migrate models
2. **POST /datasets/{dataset_id}/document/create-by-file** → `document.create_by_file()` - Migrate models
3. **POST /datasets/{dataset_id}/documents/{document_id}/update-by-text** → `document.update_by_text()` - Migrate models
4. **POST /datasets/{dataset_id}/documents/{document_id}/update-by-file** → `document.update_by_file()` - Migrate models
5. **GET /datasets/{dataset_id}/documents/{batch}/indexing-status** → `document.indexing_status()` - Migrate models
6. **DELETE /datasets/{dataset_id}/documents/{document_id}** → `document.delete()` - Migrate models
7. **GET /datasets/{dataset_id}/documents** → `document.list()` - Migrate models

#### New Methods to Add
8. **GET /datasets/{dataset_id}/documents/{document_id}** → `document.get()` - New implementation
9. **PATCH /datasets/{dataset_id}/documents/status/{action}** → `document.update_status()` - New implementation
10. **GET /datasets/{dataset_id}/documents/{document_id}/upload-file** → `document.get_upload_file()` - New implementation

## Model File Organization

### New Directory Structure
```
model/document/          # Document-specific models
├── create_by_text_request.py      # CreateByTextRequest + CreateByTextRequestBuilder
├── create_by_text_request_body.py # CreateByTextRequestBody + CreateByTextRequestBodyBuilder
├── create_by_text_response.py     # CreateByTextResponse
├── create_by_file_request.py      # CreateByFileRequest + CreateByFileRequestBuilder
├── create_by_file_request_body.py # CreateByFileRequestBody + CreateByFileRequestBodyBuilder
├── create_by_file_response.py     # CreateByFileResponse
├── update_by_text_request.py      # UpdateByTextRequest + UpdateByTextRequestBuilder
├── update_by_text_request_body.py # UpdateByTextRequestBody + UpdateByTextRequestBodyBuilder
├── update_by_text_response.py     # UpdateByTextResponse
├── update_by_file_request.py      # UpdateByFileRequest + UpdateByFileRequestBuilder
├── update_by_file_request_body.py # UpdateByFileRequestBody + UpdateByFileRequestBodyBuilder
├── update_by_file_response.py     # UpdateByFileResponse
├── indexing_status_request.py     # IndexingStatusRequest + IndexingStatusRequestBuilder
├── indexing_status_response.py    # IndexingStatusResponse
├── delete_request.py              # DeleteRequest + DeleteRequestBuilder
├── delete_response.py             # DeleteResponse
├── list_request.py                # ListRequest + ListRequestBuilder
├── list_response.py               # ListResponse
├── get_request.py                 # GetRequest + GetRequestBuilder (NEW)
├── get_response.py                # GetResponse (NEW)
├── update_status_request.py       # UpdateStatusRequest + UpdateStatusRequestBuilder (NEW)
├── update_status_request_body.py  # UpdateStatusRequestBody + UpdateStatusRequestBodyBuilder (NEW)
├── update_status_response.py      # UpdateStatusResponse (NEW)
├── get_upload_file_request.py     # GetUploadFileRequest + GetUploadFileRequestBuilder (NEW)
├── get_upload_file_response.py    # GetUploadFileResponse (NEW)
├── document_info.py               # DocumentInfo model
├── process_rule.py                # ProcessRule model
├── pre_processing_rule.py         # PreProcessingRule model
├── segmentation.py                # Segmentation model
├── subchunk_segmentation.py       # SubchunkSegmentation model
├── data_source_info.py            # DataSourceInfo model
├── upload_file_info.py            # UploadFileInfo model
├── indexing_status_info.py        # IndexingStatusInfo model
└── retrieval_model.py             # RetrievalModel (document-specific version)
```

### Legacy Files to Remove (After Migration)
```
# Files to be removed from v1/model/ root directory:
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
```

## Technical Implementation Details

### Resource Class Structure
```python
# Updated document resource
class Document:
    def __init__(self, config: Config):
        self.config = config
    
    # Existing methods (with new model imports)
    def create_by_text(self, request: CreateByTextRequest, request_option: RequestOption) -> CreateByTextResponse:
        return Transport.execute(self.config, request, unmarshal_as=CreateByTextResponse, option=request_option)
    
    async def acreate_by_text(self, request: CreateByTextRequest, request_option: RequestOption) -> CreateByTextResponse:
        return await ATransport.aexecute(self.config, request, unmarshal_as=CreateByTextResponse, option=request_option)
    
    # ... other existing methods with updated imports
    
    # New methods
    def get(self, request: GetRequest, request_option: RequestOption) -> GetResponse:
        return Transport.execute(self.config, request, unmarshal_as=GetResponse, option=request_option)
    
    async def aget(self, request: GetRequest, request_option: RequestOption) -> GetResponse:
        return await ATransport.aexecute(self.config, request, unmarshal_as=GetResponse, option=request_option)
    
    def update_status(self, request: UpdateStatusRequest, request_option: RequestOption) -> UpdateStatusResponse:
        return Transport.execute(self.config, request, unmarshal_as=UpdateStatusResponse, option=request_option)
    
    async def aupdate_status(self, request: UpdateStatusRequest, request_option: RequestOption) -> UpdateStatusResponse:
        return await ATransport.aexecute(self.config, request, unmarshal_as=UpdateStatusResponse, option=request_option)
    
    def get_upload_file(self, request: GetUploadFileRequest, request_option: RequestOption) -> GetUploadFileResponse:
        return Transport.execute(self.config, request, unmarshal_as=GetUploadFileResponse, option=request_option)
    
    async def aget_upload_file(self, request: GetUploadFileRequest, request_option: RequestOption) -> GetUploadFileResponse:
        return await ATransport.aexecute(self.config, request, unmarshal_as=GetUploadFileResponse, option=request_option)
```

### Complete Code Style Examples

#### POST Request Pattern (with RequestBody and multipart/form-data)
```python
# create_by_file_request.py
from dify_oapi.core.enum import HttpMethod
from dify_oapi.core.model.base_request import BaseRequest
from .create_by_file_request_body import CreateByFileRequestBody

class CreateByFileRequest(BaseRequest):
    def __init__(self):
        super().__init__()
        self.dataset_id: str | None = None
        self.request_body: CreateByFileRequestBody | None = None

    @staticmethod
    def builder() -> CreateByFileRequestBuilder:
        return CreateByFileRequestBuilder()

class CreateByFileRequestBuilder:
    def __init__(self):
        create_by_file_request = CreateByFileRequest()
        create_by_file_request.http_method = HttpMethod.POST
        create_by_file_request.uri = "/v1/datasets/:dataset_id/document/create-by-file"
        self._create_by_file_request = create_by_file_request

    def build(self) -> CreateByFileRequest:
        return self._create_by_file_request

    def dataset_id(self, dataset_id: str) -> CreateByFileRequestBuilder:
        self._create_by_file_request.dataset_id = dataset_id
        self._create_by_file_request.paths["dataset_id"] = dataset_id
        return self

    def request_body(self, request_body: CreateByFileRequestBody) -> CreateByFileRequestBuilder:
        self._create_by_file_request.request_body = request_body
        self._create_by_file_request.body = request_body.model_dump(exclude_none=True, mode="json")
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
        self.document_id: str | None = None

    @staticmethod
    def builder() -> GetRequestBuilder:
        return GetRequestBuilder()

class GetRequestBuilder:
    def __init__(self):
        get_request = GetRequest()
        get_request.http_method = HttpMethod.GET
        get_request.uri = "/v1/datasets/:dataset_id/documents/:document_id"
        self._get_request = get_request

    def build(self) -> GetRequest:
        return self._get_request

    def dataset_id(self, dataset_id: str) -> GetRequestBuilder:
        self._get_request.dataset_id = dataset_id
        self._get_request.paths["dataset_id"] = dataset_id
        return self

    def document_id(self, document_id: str) -> GetRequestBuilder:
        self._get_request.document_id = document_id
        self._get_request.paths["document_id"] = document_id
        return self
```

#### PATCH Request Pattern (with RequestBody and path parameters)
```python
# update_status_request.py
from dify_oapi.core.enum import HttpMethod
from dify_oapi.core.model.base_request import BaseRequest
from .update_status_request_body import UpdateStatusRequestBody

class UpdateStatusRequest(BaseRequest):
    def __init__(self):
        super().__init__()
        self.dataset_id: str | None = None
        self.action: str | None = None
        self.request_body: UpdateStatusRequestBody | None = None

    @staticmethod
    def builder() -> UpdateStatusRequestBuilder:
        return UpdateStatusRequestBuilder()

class UpdateStatusRequestBuilder:
    def __init__(self):
        update_status_request = UpdateStatusRequest()
        update_status_request.http_method = HttpMethod.PATCH
        update_status_request.uri = "/v1/datasets/:dataset_id/documents/status/:action"
        self._update_status_request = update_status_request

    def build(self) -> UpdateStatusRequest:
        return self._update_status_request

    def dataset_id(self, dataset_id: str) -> UpdateStatusRequestBuilder:
        self._update_status_request.dataset_id = dataset_id
        self._update_status_request.paths["dataset_id"] = dataset_id
        return self

    def action(self, action: str) -> UpdateStatusRequestBuilder:
        self._update_status_request.action = action
        self._update_status_request.paths["action"] = action
        return self

    def request_body(self, request_body: UpdateStatusRequestBody) -> UpdateStatusRequestBuilder:
        self._update_status_request.request_body = request_body
        self._update_status_request.body = request_body.model_dump(exclude_none=True, mode="json")
        return self
```

## Migration Impact

### Breaking Changes
- Complete rewrite of existing document model structure
- New model file organization requires import path updates
- All existing document model files will be removed
- Import statements throughout codebase need updates

### Benefits
- Full API coverage with all 10 document management endpoints
- Consistent architecture with dataset/metadata/tag patterns
- Improved type safety and developer experience
- Enhanced maintainability and extensibility
- Unified code style across all knowledge base features

## Examples Strategy

### Examples Organization
**Decision**: Resource-based directory structure with API-specific files
- Each API gets its own file within `examples/knowledge_base/document/`
- Each file contains both sync and async examples
- Basic try-catch error handling for educational purposes

### Environment Variable Validation (MANDATORY)
**Decision**: All examples MUST validate required environment variables and raise errors
- **Validation Rule**: Check for required environment variables at the start of each function
- **Error Handling**: Raise `ValueError` with descriptive message if required variables are missing
- **No Print Fallbacks**: NEVER use `print()` statements for missing environment variables
- **Required Variables**: All examples must validate `API_KEY`, document examples must validate `DATASET_ID`
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

### Resource Naming Convention (MANDATORY)
**Decision**: All example resources MUST use "[Example]" prefix for safety
- **Creation Rule**: All resources created in examples MUST have "[Example]" prefix in their names
- **Deletion Rule**: Delete operations MUST only target resources with "[Example]" prefix
- **Safety Measure**: This prevents accidental deletion of production or important resources
- **Applies to**: Document names, file names, and any other named resources
- **Examples**:
  - Document names: "[Example] API Documentation", "[Example] User Guide"
  - File names: "[Example] sample.pdf", "[Example] tutorial.txt"
- **Cleanup Functions**: Delete examples should include functions that remove all "[Example]" prefixed resources

### Code Minimalism Strategy
**Decision**: Apply the same minimal code principles used in other knowledge base examples
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
6. **Consistent Patterns**: Apply the same minimization approach used in other knowledge base examples

#### Safety Features:
- Environment variable validation at function start
- "[Example]" prefix checking for delete operations
- Basic error handling with try-catch blocks
- Resource existence verification before operations
- Consistent API key and resource ID validation

### Examples Directory Structure
```
examples/knowledge_base/document/
├── create_by_text.py      # Create document by text examples (sync + async)
├── create_by_file.py      # Create document by file examples (sync + async)
├── update_by_text.py      # Update document by text examples (sync + async)
├── update_by_file.py      # Update document by file examples (sync + async)
├── indexing_status.py     # Get indexing status examples (sync + async)
├── delete.py              # Delete document examples (sync + async)
├── list.py                # List documents examples (sync + async)
├── get.py                 # Get document details examples (sync + async)
├── update_status.py       # Update document status examples (sync + async)
└── get_upload_file.py     # Get upload file examples (sync + async)
```



## Quality Assurance

### Type Safety
- Comprehensive type hints for all models and methods
- Pydantic validation for request/response models
- Builder pattern support for all request models

### Error Handling
- Consistent error response handling across all APIs
- Proper HTTP status code mapping
- Detailed error message propagation

### Testing Strategy
- Unit tests for all resource methods
- Integration tests with mock API responses
- Validation tests for all model classes
- Migration verification tests to ensure behavioral consistency
- **Test File Organization**: All model tests MUST follow flat structure in `tests/knowledge_base/v1/model/` directory
- **Naming Consistency**: Use `test_{resource}_models.py` pattern for all model test files
- **No Nested Directories**: Avoid creating resource-specific test subdirectories
- **Consolidated Document Testing**: ALL document model tests MUST be in single `test_document_models.py` file
- **Comprehensive Coverage**: Single test file covers shared models + all 10 API models with proper organization

### Test File Organization Rules (MANDATORY)
**Decision**: Test files MUST be organized in a flat structure within the model directory
- **Flat Structure**: All model test files are placed directly in `tests/knowledge_base/v1/model/` directory
- **No Subdirectories**: Do NOT create resource-specific subdirectories like `model/document/`
- **Naming Convention**: Use `test_{resource}_models.py` pattern (e.g., `test_document_models.py`)
- **Consistency**: Follow the same pattern as existing test files (`test_dataset_models.py`, `test_metadata_models.py`, `test_tag_models.py`)
- **Consolidated Testing**: ALL document-related model tests MUST be in a single `test_document_models.py` file
- **Rationale**: Maintains consistency with existing codebase structure and simplifies test discovery

### Test Directory Structure
```
tests/knowledge_base/v1/
├── model/
│   ├── test_dataset_models.py         # Existing dataset model tests
│   ├── test_metadata_models.py        # Existing metadata model tests
│   ├── test_tag_models.py             # Existing tag model tests
│   └── test_document_models.py        # ALL document model tests (shared + API models)
├── resource/
│   └── test_document_resource.py
├── integration/
│   ├── test_document_api_integration.py
│   ├── test_migration_verification.py
│   └── test_examples_validation.py
└── __init__.py
```

### Document Model Test Organization (MANDATORY)
**Decision**: Single consolidated test file for all document models
- **File**: `tests/knowledge_base/v1/model/test_document_models.py`
- **Scope**: ALL document-related model tests in one file
- **Coverage**: 
  - Shared models (DocumentInfo, ProcessRule, etc.)
  - All 10 API request/response models
  - Builder pattern tests for all models
  - Integration tests between models
- **Structure**: Organize tests by model type with clear section comments
- **Benefits**: 
  - Single source of truth for all document model tests
  - Easier maintenance and discovery
  - Consistent with other resource test patterns
  - Simplified test execution and coverage reporting

## Latest Improvements and Optimizations

### 1. Advanced File Handling
**Recent Enhancements**:
- **Multi-format Support**: Enhanced support for various document formats (PDF, DOCX, TXT, etc.)
- **Streaming Upload**: Optimized file upload with streaming support for large documents
- **File Validation**: Improved file type and size validation mechanisms
- **Batch Processing**: Enhanced batch document processing capabilities

### 2. Document Processing Optimizations
**Implementation Improvements**:
- **Intelligent Segmentation**: Advanced text segmentation algorithms for better content organization
- **Metadata Extraction**: Automatic metadata extraction from document content
- **Content Indexing**: Optimized indexing strategies for faster search and retrieval
- **Processing Status Tracking**: Real-time processing status monitoring and updates

### 3. Enhanced API Performance
**Performance Enhancements**:
- **Async Processing**: Improved asynchronous document processing workflows
- **Caching Mechanisms**: Intelligent caching for frequently accessed documents
- **Resource Optimization**: Better memory and CPU usage during document operations
- **Parallel Processing**: Support for parallel document processing operations

### 4. Developer Experience Improvements
**Latest Features**:
- **Progress Callbacks**: Real-time progress tracking for long-running operations
- **Error Recovery**: Improved error handling and recovery mechanisms
- **Validation Helpers**: Built-in validation utilities for document formats and content
- **Debug Support**: Enhanced debugging capabilities for document processing workflows

### 5. Security and Compliance
**Security Enhancements**:
- **Content Sanitization**: Advanced content sanitization for uploaded documents
- **Access Control**: Improved access control mechanisms for document operations
- **Audit Logging**: Comprehensive audit logging for document management activities
- **Data Privacy**: Enhanced data privacy protection during document processing

### 6. Integration and Compatibility
**Integration Improvements**:
- **Third-party Integrations**: Better support for external document management systems
- **Format Conversion**: Built-in document format conversion capabilities
- **API Versioning**: Improved API versioning and backward compatibility
- **Migration Tools**: Enhanced tools for migrating from legacy document systems

## Summary

This design provides a comprehensive solution for document management in dify-oapi, covering all 10 document-related APIs with a clean, maintainable architecture. The implementation prioritizes consistency with existing patterns while ensuring full migration to the new model organization structure.

The complete migration approach ensures long-term maintainability by eliminating legacy code patterns and establishing a unified architecture across all knowledge base features. The preservation of existing method names maintains backward compatibility while the new model structure provides improved developer experience and type safety.

The examples strategy ensures developers have clear, educational references for every API operation, supporting both learning and integration testing needs with comprehensive sync/async coverage. The code minimalism principles successfully applied to dataset, metadata, and tag examples should be extended to document examples for consistency.

### Alignment with Knowledge Base Architecture
- **Consistent Minimalism**: Document examples follow the same minimal code principles applied to other knowledge base examples
- **Unified Approach**: Maintain consistency across all knowledge base resource examples (dataset, metadata, tag, document)
- **Educational Focus**: Examples focus purely on demonstrating API functionality without unnecessary complexity
- **Safety Preservation**: All safety features and validation patterns remain intact across all examples
- **Performance Optimization**: Enhanced document processing and file handling capabilities
- **Advanced Features**: Support for complex document workflows and batch operations
- **Security Focus**: Comprehensive security measures for document management operations