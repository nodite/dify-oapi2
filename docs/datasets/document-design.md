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

### Test Directory Structure
```
tests/knowledge_base/v1/
├── model/
│   └── document/
│       ├── test_create_by_text_models.py
│       ├── test_create_by_file_models.py
│       ├── test_update_models.py
│       ├── test_status_models.py
│       └── test_shared_models.py
├── resource/
│   └── test_document_resource.py
├── integration/
│   ├── test_document_api_integration.py
│   ├── test_migration_verification.py
│   └── test_examples_validation.py
└── __init__.py
```

## Summary

This design provides a comprehensive solution for document management in dify-oapi, covering all 10 document-related APIs with a clean, maintainable architecture. The implementation prioritizes consistency with existing patterns while ensuring full migration to the new model organization structure.

The complete migration approach ensures long-term maintainability by eliminating legacy code patterns and establishing a unified architecture across all knowledge base features. The preservation of existing method names maintains backward compatibility while the new model structure provides improved developer experience and type safety.

The examples strategy ensures developers have clear, educational references for every API operation, supporting both learning and integration testing needs with comprehensive sync/async coverage.