# Knowledge Base API Design Document

## Overview

This document outlines the design for implementing comprehensive knowledge base functionality in the dify-oapi knowledge module. The implementation will support all 33 knowledge-related APIs covering dataset management, document processing, segment management, child chunks management, tag management, and model integration.

## Design Decisions

### 1. Module Organization
**Decision**: Extend existing `knowledge/v1/` module structure
- Continue using the established version-based API organization
- Maintain consistency with existing chat, completion, and workflow modules
- Leverage existing infrastructure and patterns

### 2. Resource Structure
**Decision**: Implement knowledge APIs across multiple specialized resources

**Multi-Resource Implementation**:
- `dataset` - Dataset management APIs (6 APIs)
  - Dataset CRUD: `create`, `list`, `get`, `update`, `delete`
  - Dataset operations: `retrieve`
- `document` - Document management APIs (10 APIs)
  - Document creation: `create_by_file`, `create_by_text`
  - Document operations: `list`, `get`, `update_by_file`, `update_by_text`, `delete`
  - File operations: `file_info`
  - Status management: `update_status`, `get_batch_status`
- `segment` - Segment management APIs (5 APIs)
  - Segment operations: `list`, `create`, `get`, `update`, `delete`
- `chunk` - Child chunks management APIs (4 APIs)
  - Child chunk operations: `list_chunks`, `create_chunk`, `update_chunk`, `delete_chunk`
- `tag` - Tag and metadata management APIs (7 APIs)
  - Tag operations: `list`, `create`, `update`, `delete`
  - Tag binding: `bind`, `unbind`
  - Dataset tags: `get_dataset_tags`
- `model` - Model management APIs (1 API)
  - Model retrieval: `embedding_models`

**Legacy Code Migration (MANDATORY)**:
- **Current Structure Assessment**: Evaluate existing knowledge module implementation structure
- **Migration Required**: Consolidate any existing functionality into the new multi-resource structure
- **Backward Compatibility**: Maintain existing API signatures during migration
- **Model Consolidation**: Move all models from subdirectories to flat structure
- **Resource Organization**: Ensure proper separation of concerns across the 6 resource classes
- **Version Update**: Update V1 class to expose all 6 knowledge resources

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

### 5. Method Naming Convention
**Decision**: Use simple, concise method names for clarity
- Dataset operations: `create`, `list`, `get`, `update`, `delete`, `retrieve`
- Document operations: `create_by_file`, `create_by_text`, `list`, `get`, `update_by_file`, `update_by_text`, `delete`, `update_status`, `get_batch_status`, `file_info`
- Segment operations: `list`, `create`, `get`, `update`, `delete`
- Chunk operations: `list_chunks`, `create_chunk`, `update_chunk`, `delete_chunk`
- Tag operations: `list`, `create`, `update`, `delete`, `bind`, `unbind`, `get_dataset_tags`
- Model operations: `embedding_models`

**Naming Rules**:
- Use the shortest meaningful name possible
- Avoid redundant prefixes (e.g., `create` instead of `create_dataset` in Dataset resource)
- Use underscores only when necessary for clarity
- Async methods use `a` prefix (e.g., `acreate`, `alist`, `aget`)

**Ambiguity Resolution Rules (MANDATORY)**:
- When multiple operations in the same resource could cause naming ambiguity, use descriptive prefixes
- Update operations use `update_` prefix (e.g., `update_status` for document status updates)
- Get operations use `get_` prefix when needed for clarity (e.g., `get_batch_status` for batch indexing status)
- Maintain method names concise but unambiguous within the resource context
- Examples:
  - `update_status()` vs `get_batch_status()` - clearly different operations
  - `create_by_file()` vs `create_by_text()` - different creation methods
  - `update_by_file()` vs `update_by_text()` - different update methods

### 6. Class Naming Conflict Resolution (MANDATORY)
**Decision**: When class names conflict across different functional domains, add domain-specific prefixes

**MANDATORY RULE**: Classes with identical names across different API domains MUST use domain prefixes to avoid conflicts
- **Rationale**: Prevents import conflicts and ensures clear class identification
- **Implementation**: Add functional domain prefix to conflicting class names
- **Zero Exceptions**: All conflicting classes must be renamed with appropriate prefixes

**Required Naming Patterns for Knowledge Module**:
- **Dataset classes**: `Dataset*` (e.g., `DatasetInfo`, `DatasetConfig`)
- **Document classes**: `Document*` (e.g., `DocumentInfo`, `DocumentStatus`, `DocumentProcessRule`)
- **Segment classes**: `Segment*` (e.g., `SegmentInfo`, `SegmentContent`)
- **Chunk classes**: `Chunk*` (e.g., `ChildChunkInfo`, `ChunkContent`)
- **Tag classes**: `Tag*` (e.g., `TagInfo`, `TagBinding`)
- **Model classes**: `Model*` (e.g., `ModelInfo`, `EmbeddingModel`)
- **File classes**: `File*` (e.g., `FileInfo`, `FileUpload`)

### 7. Response Model Inheritance Rules (CRITICAL - ZERO TOLERANCE)
**Decision**: ALL Response classes MUST inherit from BaseResponse for error handling

**MANDATORY RULE**: Every single Response class in the knowledge module MUST inherit from `BaseResponse`
- **Rationale**: Ensures all API responses have consistent error handling capabilities
- **Properties Provided**: `success`, `code`, `msg`, `raw` for comprehensive error management
- **Zero Exceptions**: No Response class may inherit directly from `pydantic.BaseModel`

**Correct Response Class Patterns**:
```python
# ✅ CORRECT: Simple response inheriting from BaseResponse
class DeleteDatasetResponse(BaseResponse):
    result: str | None = None

# ✅ CORRECT: Response with data using multiple inheritance
class CreateDatasetResponse(DatasetInfo, BaseResponse):
    pass

# ❌ WRONG: Direct BaseModel inheritance
class CreateDatasetResponse(BaseModel):  # NEVER DO THIS
    pass
```

### 8. Request/Response Model Code Style Rules (MANDATORY)
**Decision**: Strict adherence to established patterns for consistency across all knowledge APIs

#### Request Model Architecture
**Request Classes**:
- MUST inherit from `BaseRequest` (never from `BaseModel`)
- MUST include `request_body` attribute of type `RequestBody | None` for POST/PATCH/PUT requests
- MUST use `request_body()` method in builder to accept entire RequestBody object
- Builder variables MUST use full descriptive names (e.g., `self._create_dataset_request`)
- MUST set `http_method` and `uri` in builder constructor
- Path parameters MUST use `self._request.paths["param_name"] = value` pattern
- Query parameters MUST use `self._request.add_query("key", value)` pattern

#### HTTP Method Patterns
**GET Requests** (list_datasets, get_dataset, list_documents, get_document, etc.):
- No RequestBody file needed
- Use query parameters: `self._request.add_query("key", value)`
- Use path parameters: `self._request.paths["param_name"] = value`

**POST Requests** (create_dataset, create_document_by_file, create_segment, etc.):
- Require separate RequestBody file
- Use `request_body()` method in Request builder
- RequestBody builder methods set fields directly

**PATCH/PUT Requests** (update_dataset, update_segment, etc.):
- Require separate RequestBody file
- Use `request_body()` method in Request builder

**DELETE Requests** (delete_dataset, delete_document, delete_segment):
- No RequestBody file needed
- Use path parameters for resource identification

#### Multipart/Form-Data Handling (CRITICAL PATTERN)
**Decision**: Special handling for APIs that require multipart/form-data (file uploads)

**Pattern Requirements**:
- APIs requiring file uploads MUST use multipart/form-data content type
- Request classes MUST support both `files` and `body` fields in BaseRequest
- RequestBody classes MUST use nested data structure pattern for complex form data

**Implementation Pattern**:
```python
# For APIs with file uploads (e.g., create_document_by_file)
class CreateDocumentByFileRequestBody(BaseModel):
    name: str | None = None
    indexing_technique: IndexingTechnique | None = None
    process_rule: ProcessRule | None = None

class CreateDocumentByFileRequest(BaseRequest):
    def __init__(self) -> None:
        super().__init__()
        self.file: BytesIO | None = None

    def file(self, file: BytesIO, file_name: str | None = None) -> CreateDocumentByFileRequestBuilder:
        self._request.file = file
        file_name = file_name or "upload"
        self._request.files = {"file": (file_name, file)}
        return self

    def request_body(self, request_body: CreateDocumentByFileRequestBody) -> CreateDocumentByFileRequestBuilder:
        data_dict = request_body.model_dump(exclude_none=True, mode="json")
        self._request.body = {"data": json.dumps(data_dict)}
        return self
```

#### Class Naming Convention (MANDATORY - ZERO TOLERANCE)
**Universal Naming Pattern**:
- File names determine class names exactly (e.g., `create_dataset_request.py` → `CreateDatasetRequest`)
- Each class has corresponding Builder (e.g., `CreateDatasetRequest` + `CreateDatasetRequestBuilder`)
- Pattern applies to all model types: Request, RequestBody, Response

**STRICT Naming Rules (NO EXCEPTIONS)**:
- Remove ALL module/domain prefixes from class names
- Class names MUST match file names exactly (case-sensitive)
- Apply uniformly across ALL resources: dataset, document, segment, tag, model
- Use operation-based names: `CreateDatasetRequest`, `GetDocumentResponse`, `UpdateSegmentRequestBody`
- NEVER use domain-specific names: `DatasetCreateDatasetRequest`, `DocumentGetDocumentResponse`
- NO legacy naming patterns allowed
- Consistent across all HTTP methods and operation types

#### URI and HTTP Method Configuration
**All Knowledge APIs**:
- `POST /v1/datasets` → `CreateDatasetRequest`
- `GET /v1/datasets` → `ListDatasetsRequest`
- `GET /v1/datasets/:dataset_id` → `GetDatasetRequest`
- `PATCH /v1/datasets/:dataset_id` → `UpdateDatasetRequest`
- `DELETE /v1/datasets/:dataset_id` → `DeleteDatasetRequest`
- `POST /v1/datasets/:dataset_id/retrieve` → `RetrieveFromDatasetRequest`
- `POST /v1/datasets/:dataset_id/document/create-by-file` → `CreateDocumentByFileRequest`
- `POST /v1/datasets/:dataset_id/document/create-by-text` → `CreateDocumentByTextRequest`
- `GET /v1/datasets/:dataset_id/documents` → `ListDocumentsRequest`
- `GET /v1/datasets/:dataset_id/documents/:document_id` → `GetDocumentRequest`
- `POST /v1/datasets/:dataset_id/documents/:document_id/update-by-file` → `UpdateDocumentByFileRequest`
- `POST /v1/datasets/:dataset_id/documents/:document_id/update-by-text` → `UpdateDocumentByTextRequest`
- `DELETE /v1/datasets/:dataset_id/documents/:document_id` → `DeleteDocumentRequest`
- `PATCH /v1/datasets/:dataset_id/documents/status/:action` → `UpdateDocumentStatusRequest`
- `GET /v1/datasets/:dataset_id/documents/:batch/indexing-status` → `GetBatchIndexingStatusRequest`
- `GET /v1/datasets/:dataset_id/documents/:document_id/upload-file` → `GetUploadFileInfoRequest`
- `GET /v1/datasets/:dataset_id/documents/:document_id/segments` → `ListSegmentsRequest`
- `POST /v1/datasets/:dataset_id/documents/:document_id/segments` → `CreateSegmentRequest`
- `GET /v1/datasets/:dataset_id/documents/:document_id/segments/:segment_id` → `GetSegmentRequest`
- `POST /v1/datasets/:dataset_id/documents/:document_id/segments/:segment_id` → `UpdateSegmentRequest`
- `DELETE /v1/datasets/:dataset_id/documents/:document_id/segments/:segment_id` → `DeleteSegmentRequest`
- `GET /v1/datasets/:dataset_id/documents/:document_id/segments/:segment_id/child_chunks` → `ListChildChunksRequest`
- `POST /v1/datasets/:dataset_id/documents/:document_id/segments/:segment_id/child_chunks` → `CreateChildChunkRequest`
- `PATCH /v1/datasets/:dataset_id/documents/:document_id/segments/:segment_id/child_chunks/:child_chunk_id` → `UpdateChildChunkRequest`
- `DELETE /v1/datasets/:dataset_id/documents/:document_id/segments/:segment_id/child_chunks/:child_chunk_id` → `DeleteChildChunkRequest`
- `GET /v1/datasets/tags` → `ListTagsRequest`
- `POST /v1/datasets/tags` → `CreateTagRequest`
- `PATCH /v1/datasets/tags` → `UpdateTagRequest`
- `DELETE /v1/datasets/tags` → `DeleteTagRequest`
- `POST /v1/datasets/tags/binding` → `BindTagsToDatasetRequest`
- `POST /v1/datasets/tags/unbinding` → `UnbindTagsFromDatasetRequest`
- `POST /v1/datasets/:dataset_id/tags` → `GetDatasetTagsRequest`
- `GET /v1/workspaces/current/models/model-types/text-embedding` → `GetTextEmbeddingModelsRequest`

#### Public Class Inheritance Rules (CRITICAL)
**Public/Common Classes**:
- Public classes (DatasetInfo, DocumentInfo, SegmentInfo, etc.) MUST inherit from `pydantic.BaseModel` ONLY
- Public classes MUST NOT inherit from `BaseResponse`
- Public classes MUST have Builder patterns for consistency and ease of use
- Public classes are reusable components that can be used across different contexts

**Response Classes (MANDATORY - ZERO TOLERANCE)**:
- ALL Response classes MUST inherit from `BaseResponse` for error handling capabilities
- Response classes MAY use multiple inheritance when they need to include public class data
- Pattern: `class CreateDatasetResponse(DatasetInfo, BaseResponse):`
- This allows response classes to have both data fields and error handling capabilities
- Response classes MUST NOT have Builder patterns (unlike Request classes)
- **CRITICAL**: NEVER inherit from `pydantic.BaseModel` directly - ALWAYS use `BaseResponse`

### 9. Strict Type Safety Rules (MANDATORY - ZERO TOLERANCE)
**Decision**: ALL API fields MUST use strict typing with Literal types instead of generic strings

**MANDATORY RULE**: Every field that has predefined values MUST use Literal types for type safety

**Strict Type Implementation Pattern**:
```python
# knowledge_types.py - Define all Literal types
from typing import Literal

# Indexing technique types
IndexingTechnique = Literal["high_quality", "economy"]

# Permission types
Permission = Literal["only_me", "all_team_members", "partial_members"]

# Search method types
SearchMethod = Literal["hybrid_search", "semantic_search", "full_text_search", "keyword_search"]

# Document status types
DocumentStatus = Literal["indexing", "completed", "error", "paused"]

# Processing mode types
ProcessingMode = Literal["automatic", "custom"]

# File types
FileType = Literal["document", "image", "audio", "video", "custom"]

# Transfer method types
TransferMethod = Literal["remote_url", "local_file"]

# Tag types
TagType = Literal["knowledge_type", "custom"]

# Segment status types
SegmentStatus = Literal["waiting", "parsing", "cleaning", "splitting", "indexing", "completed", "error", "paused"]

# Document status action types
DocumentStatusAction = Literal["enable", "disable", "archive", "un_archive"]

# Document form types
DocumentForm = Literal["text_model", "hierarchical_model", "qa_model"]

# Model types
ModelType = Literal["text-embedding"]

# Provider types
ProviderType = Literal["vendor", "external"]

# Data source types
DataSourceType = Literal["upload_file", "notion_import", "website_crawl"]

# Indexing status types
IndexingStatus = Literal["waiting", "parsing", "cleaning", "splitting", "indexing", "completed", "error", "paused"]

# Reranking model configuration types
RerankingProviderName = str  # Dynamic provider names
RerankingModelName = str     # Dynamic model names
```

### 10. Public Class Builder Pattern Rules (MANDATORY)
**Decision**: All public classes MUST implement builder patterns for consistency and usability

#### Builder Pattern Implementation Requirements
**Scope**: All public/common classes that inherit from `pydantic.BaseModel`
- **Target Classes**: `DatasetInfo`, `DocumentInfo`, `SegmentInfo`, `TagInfo`, `ModelInfo`, `FileInfo`, `ProcessRule`, `RetrievalModel`, and all other public model classes
- **Exclusions**: Request, RequestBody, and Response classes (which have their own builder rules)

### 11. File Organization Strategy
**Decision**: Different organization strategies for models vs resources

#### Model Organization: Flat Structure
**Models use flat structure without grouping**:
```
model/
├── create_dataset_request.py
├── create_dataset_request_body.py
├── create_dataset_response.py
├── list_datasets_request.py
├── dataset_info.py
├── knowledge_types.py
└── [all other model files in flat structure]
```

#### Resource Organization: Functional Grouping
**Resources are grouped by functionality**:
```
resource/
├── dataset.py     # Dataset management operations
├── document.py    # Document processing operations
├── segment.py     # Segment operations
├── chunk.py       # Child chunk operations
├── tag.py         # Tag and metadata operations
└── model.py       # Model information operations
```

**Rationale**:
- **Models**: Flat structure for easy imports and reduced nesting
- **Resources**: Grouped by domain for logical separation of concerns

**Target Structure**:
```
model/
├── create_dataset_request.py
├── create_dataset_request_body.py
├── create_dataset_response.py
├── list_datasets_request.py
├── list_datasets_response.py
├── get_dataset_request.py
├── get_dataset_response.py
├── update_dataset_request.py
├── update_dataset_request_body.py
├── update_dataset_response.py
├── delete_dataset_request.py
├── delete_dataset_response.py
├── retrieve_from_dataset_request.py
├── retrieve_from_dataset_request_body.py
├── retrieve_from_dataset_response.py
├── create_document_by_file_request.py
├── create_document_by_file_request_body.py
├── create_document_by_file_response.py
├── create_document_by_text_request.py
├── create_document_by_text_request_body.py
├── create_document_by_text_response.py
├── list_documents_request.py
├── list_documents_response.py
├── get_document_request.py
├── get_document_response.py
├── update_document_by_file_request.py
├── update_document_by_file_request_body.py
├── update_document_by_file_response.py
├── update_document_by_text_request.py
├── update_document_by_text_request_body.py
├── update_document_by_text_response.py
├── delete_document_request.py
├── delete_document_response.py
├── update_document_status_request.py
├── update_document_status_request_body.py
├── update_document_status_response.py
├── get_batch_indexing_status_request.py
├── get_batch_indexing_status_response.py
├── get_upload_file_info_request.py
├── get_upload_file_info_response.py
├── list_segments_request.py
├── list_segments_response.py
├── create_segment_request.py
├── create_segment_request_body.py
├── create_segment_response.py
├── get_segment_request.py
├── get_segment_response.py
├── update_segment_request.py
├── update_segment_request_body.py
├── update_segment_response.py
├── delete_segment_request.py
├── delete_segment_response.py
├── list_child_chunks_request.py
├── list_child_chunks_response.py
├── create_child_chunk_request.py
├── create_child_chunk_request_body.py
├── create_child_chunk_response.py
├── update_child_chunk_request.py
├── update_child_chunk_request_body.py
├── update_child_chunk_response.py
├── delete_child_chunk_request.py
├── delete_child_chunk_response.py
├── list_tags_request.py
├── list_tags_response.py
├── create_tag_request.py
├── create_tag_request_body.py
├── create_tag_response.py
├── update_tag_request.py
├── update_tag_request_body.py
├── update_tag_response.py
├── delete_tag_request.py
├── delete_tag_request_body.py
├── delete_tag_response.py
├── bind_tags_to_dataset_request.py
├── bind_tags_to_dataset_request_body.py
├── bind_tags_to_dataset_response.py
├── unbind_tags_from_dataset_request.py
├── unbind_tags_from_dataset_request_body.py
├── unbind_tags_from_dataset_response.py
├── get_dataset_tags_request.py
├── get_dataset_tags_response.py
├── get_text_embedding_models_request.py
├── get_text_embedding_models_response.py
├── dataset_info.py
├── document_info.py
├── segment_info.py
├── child_chunk_info.py
├── tag_info.py
├── model_info.py
├── file_info.py
├── process_rule.py
├── retrieval_model.py
├── embedding_model_parameters.py
├── reranking_model.py
├── batch_info.py
├── pagination_info.py
├── query_info.py
├── retrieval_record.py
├── segment_document_info.py
└── knowledge_types.py
```

**Migration Steps**:
1. Move all model files from subdirectories to root model/ directory (if applicable)
2. Update all import statements to reflect new flat structure
3. Remove empty subdirectories (dataset/, document/, segment/, tag/, model/) if they exist
4. Update __init__.py files to export from new locations
5. Ensure all cross-references between models are updated to new flat structure

## API Implementation Plan

### Dataset Management APIs (6 APIs)

#### Dataset Resource Implementation
1. **POST /datasets** → `dataset.create()` - Create new dataset
2. **GET /datasets** → `dataset.list()` - List all datasets with filtering
3. **GET /datasets/{dataset_id}** → `dataset.get()` - Get dataset details
4. **PATCH /datasets/{dataset_id}** → `dataset.update()` - Update dataset
5. **DELETE /datasets/{dataset_id}** → `dataset.delete()` - Delete dataset
6. **POST /datasets/{dataset_id}/retrieve** → `dataset.retrieve()` - Search content

### Document Management APIs (10 APIs)

#### Document Resource Implementation
1. **POST /datasets/{dataset_id}/document/create-by-file** → `document.create_by_file()` - Upload file
2. **POST /datasets/{dataset_id}/document/create-by-text** → `document.create_by_text()` - Create from text
3. **GET /datasets/{dataset_id}/documents** → `document.list()` - List documents
4. **GET /datasets/{dataset_id}/documents/{document_id}** → `document.get()` - Get document
5. **POST /datasets/{dataset_id}/documents/{document_id}/update-by-file** → `document.update_by_file()` - Update with file
6. **POST /datasets/{dataset_id}/documents/{document_id}/update-by-text** → `document.update_by_text()` - Update with text
7. **DELETE /datasets/{dataset_id}/documents/{document_id}** → `document.delete()` - Delete document
8. **GET /datasets/{dataset_id}/documents/{document_id}/upload-file** → `document.file_info()` - Get file info
9. **PATCH /datasets/{dataset_id}/documents/status/{action}** → `document.update_status()` - Batch status management
10. **GET /datasets/{dataset_id}/documents/{batch}/indexing-status** → `document.get_batch_status()` - Check processing status

### Segment Management APIs (5 APIs)

#### Segment Resource Implementation
1. **GET /datasets/{dataset_id}/documents/{document_id}/segments** → `segment.list()` - List segments
2. **POST /datasets/{dataset_id}/documents/{document_id}/segments** → `segment.create()` - Create segments
3. **GET /datasets/{dataset_id}/documents/{document_id}/segments/{segment_id}** → `segment.get()` - Get segment
4. **POST /datasets/{dataset_id}/documents/{document_id}/segments/{segment_id}** → `segment.update()` - Update segment
5. **DELETE /datasets/{dataset_id}/documents/{document_id}/segments/{segment_id}** → `segment.delete()` - Delete segment

### Child Chunks Management APIs (4 APIs)

#### Chunk Resource Implementation
1. **GET /datasets/{dataset_id}/documents/{document_id}/segments/{segment_id}/child_chunks** → `chunk.list_chunks()` - List child chunks
2. **POST /datasets/{dataset_id}/documents/{document_id}/segments/{segment_id}/child_chunks** → `chunk.create_chunk()` - Create child chunk
3. **PATCH /datasets/{dataset_id}/documents/{document_id}/segments/{segment_id}/child_chunks/{child_chunk_id}** → `chunk.update_chunk()` - Update child chunk
4. **DELETE /datasets/{dataset_id}/documents/{document_id}/segments/{segment_id}/child_chunks/{child_chunk_id}** → `chunk.delete_chunk()` - Delete child chunk

### Tag Management APIs (7 APIs)

#### Tag Resource Implementation
1. **GET /datasets/tags** → `tag.list()` - List all tags
2. **POST /datasets/tags** → `tag.create()` - Create tag
3. **PATCH /datasets/tags** → `tag.update()` - Update tag
4. **DELETE /datasets/tags** → `tag.delete()` - Delete tag
5. **POST /datasets/tags/binding** → `tag.bind()` - Bind tags
6. **POST /datasets/tags/unbinding** → `tag.unbind()` - Unbind tags
7. **POST /datasets/{dataset_id}/tags** → `tag.get_dataset_tags()` - Get dataset tags

### Model Management APIs (1 API)

#### Model Resource Implementation
1. **GET /workspaces/current/models/model-types/text-embedding** → `model.embedding_models()` - Get embedding models

## Technical Implementation Details

### Resource Class Structure
```python
# Example: dataset resource
class Dataset:
    def __init__(self, config: Config):
        self.config = config

    def create(self, request: CreateDatasetRequest, request_option: RequestOption) -> CreateDatasetResponse:
        return Transport.execute(self.config, request, unmarshal_as=CreateDatasetResponse, option=request_option)

    async def acreate(self, request: CreateDatasetRequest, request_option: RequestOption) -> CreateDatasetResponse:
        return await ATransport.aexecute(self.config, request, unmarshal_as=CreateDatasetResponse, option=request_option)

# Example: chunk resource
class Chunk:
    def __init__(self, config: Config):
        self.config = config

    def list_chunks(self, request: ListChildChunksRequest, request_option: RequestOption) -> ListChildChunksResponse:
        return Transport.execute(self.config, request, unmarshal_as=ListChildChunksResponse, option=request_option)

    async def alist_chunks(self, request: ListChildChunksRequest, request_option: RequestOption) -> ListChildChunksResponse:
        return await ATransport.aexecute(self.config, request, unmarshal_as=ListChildChunksResponse, option=request_option)
```

### Complete Code Style Examples

#### POST Request Pattern (with RequestBody)
```python
# create_dataset_request.py
from dify_oapi.core.enum import HttpMethod
from dify_oapi.core.model.base_request import BaseRequest
from .create_dataset_request_body import CreateDatasetRequestBody

class CreateDatasetRequest(BaseRequest):
    def __init__(self):
        super().__init__()
        self.request_body: CreateDatasetRequestBody | None = None

    @staticmethod
    def builder() -> CreateDatasetRequestBuilder:
        return CreateDatasetRequestBuilder()

class CreateDatasetRequestBuilder:
    def __init__(self):
        create_dataset_request = CreateDatasetRequest()
        create_dataset_request.http_method = HttpMethod.POST
        create_dataset_request.uri = "/v1/datasets"
        self._create_dataset_request = create_dataset_request

    def build(self) -> CreateDatasetRequest:
        return self._create_dataset_request

    def request_body(self, request_body: CreateDatasetRequestBody) -> CreateDatasetRequestBuilder:
        self._create_dataset_request.request_body = request_body
        self._create_dataset_request.body = request_body.model_dump(exclude_none=True, mode="json")
        return self
```

```python
# create_dataset_request_body.py
from pydantic import BaseModel
from .dataset_info import DatasetInfo
from .retrieval_model import RetrievalModel
from .embedding_model_parameters import EmbeddingModelParameters
from ..knowledge_types import IndexingTechnique, Permission, ProviderType

class CreateDatasetRequestBody(BaseModel):
    name: str | None = None
    description: str | None = None
    indexing_technique: IndexingTechnique | None = None
    permission: Permission | None = None
    provider: ProviderType | None = None
    external_knowledge_api_id: str | None = None
    external_knowledge_id: str | None = None
    embedding_model: str | None = None
    embedding_model_provider: str | None = None
    retrieval_model: RetrievalModel | None = None

    @staticmethod
    def builder() -> CreateDatasetRequestBodyBuilder:
        return CreateDatasetRequestBodyBuilder()

class CreateDatasetRequestBodyBuilder:
    def __init__(self):
        self._create_dataset_request_body = CreateDatasetRequestBody()

    def build(self) -> CreateDatasetRequestBody:
        return self._create_dataset_request_body

    def name(self, name: str) -> CreateDatasetRequestBodyBuilder:
        self._create_dataset_request_body.name = name
        return self

    def description(self, description: str) -> CreateDatasetRequestBodyBuilder:
        self._create_dataset_request_body.description = description
        return self

    def indexing_technique(self, indexing_technique: IndexingTechnique) -> CreateDatasetRequestBodyBuilder:
        self._create_dataset_request_body.indexing_technique = indexing_technique
        return self

    def permission(self, permission: Permission) -> CreateDatasetRequestBodyBuilder:
        self._create_dataset_request_body.permission = permission
        return self
```

#### GET Request Pattern (with path parameters)
```python
# get_dataset_request.py
from dify_oapi.core.enum import HttpMethod
from dify_oapi.core.model.base_request import BaseRequest

class GetDatasetRequest(BaseRequest):
    def __init__(self):
        super().__init__()
        self.dataset_id: str | None = None

    @staticmethod
    def builder() -> GetDatasetRequestBuilder:
        return GetDatasetRequestBuilder()

class GetDatasetRequestBuilder:
    def __init__(self):
        get_dataset_request = GetDatasetRequest()
        get_dataset_request.http_method = HttpMethod.GET
        get_dataset_request.uri = "/v1/datasets/:dataset_id"
        self._get_dataset_request = get_dataset_request

    def build(self) -> GetDatasetRequest:
        return self._get_dataset_request

    def dataset_id(self, dataset_id: str) -> GetDatasetRequestBuilder:
        self._get_dataset_request.dataset_id = dataset_id
        self._get_dataset_request.paths["dataset_id"] = dataset_id
        return self
```

#### GET Request Pattern (with query parameters)
```python
# list_datasets_request.py
from dify_oapi.core.enum import HttpMethod
from dify_oapi.core.model.base_request import BaseRequest

class ListDatasetsRequest(BaseRequest):
    def __init__(self):
        super().__init__()

    @staticmethod
    def builder() -> ListDatasetsRequestBuilder:
        return ListDatasetsRequestBuilder()

class ListDatasetsRequestBuilder:
    def __init__(self):
        list_datasets_request = ListDatasetsRequest()
        list_datasets_request.http_method = HttpMethod.GET
        list_datasets_request.uri = "/v1/datasets"
        self._list_datasets_request = list_datasets_request

    def build(self) -> ListDatasetsRequest:
        return self._list_datasets_request

    def page(self, page: int) -> ListDatasetsRequestBuilder:
        self._list_datasets_request.add_query("page", str(page))
        return self

    def limit(self, limit: int) -> ListDatasetsRequestBuilder:
        self._list_datasets_request.add_query("limit", str(limit))
        return self
```

### Version Integration
**Current Structure Assessment**:
```python
# Evaluate existing structure (if any)
class V1:
    def __init__(self, config: Config):
        # Current implementation to be assessed
        pass
```

**Target Structure**:
```python
class V1:
    def __init__(self, config: Config):
        self.dataset = Dataset(config)
        self.document = Document(config)
        self.segment = Segment(config)
        self.chunk = Chunk(config)
        self.tag = Tag(config)
        self.model = Model(config)
```

**Migration Steps**:
1. Assess current knowledge module structure and existing implementations
2. Create new resource classes (Dataset, Document, Segment, Chunk, Tag, Model)
3. Migrate any existing methods to appropriate resource classes
4. Update V1 class to expose all 6 knowledge resources
5. Ensure all existing method signatures are preserved during migration
6. Update import statements and references throughout the codebase

## Quality Assurance

### Type Safety
- Comprehensive type hints for all models and methods
- Pydantic validation for request/response models
- Builder pattern support for all request models
- Literal types for all predefined values

### Error Handling
- Consistent error response handling across all APIs
- Proper HTTP status code mapping
- Detailed error message propagation

### Testing Strategy
- Unit tests for all resource methods
- Integration tests with mock API responses
- Validation tests for all model classes
- Comprehensive typing hints for all test methods

### Test File Organization Rules (MANDATORY)
**Decision**: Test files MUST be organized by resource functionality
- **API Operation Grouping**: Organize tests by API operation with dedicated test classes
- **Method Organization**: Within each test class, organize methods by model type (Request, RequestBody, Response)
- **Public Class Separation**: Create separate files for public/common model tests
- **Flat Structure**: All model test files are placed directly in `tests/knowledge/v1/model/` directory
- **Naming Convention**: Use resource-based naming patterns for test files
- **Complete Coverage**: All 33 APIs must have corresponding test classes

### Test Class Organization Pattern
**Within knowledge test files, organize by API operations:**
```python
# test_dataset_models.py
class TestCreateDatasetModels:
    # Request tests
    def test_request_builder(self): ...
    def test_request_validation(self): ...
    # RequestBody tests
    def test_request_body_builder(self): ...
    def test_request_body_validation(self): ...
    # Response tests
    def test_response_inheritance(self): ...
    def test_response_data_access(self): ...

class TestListDatasetsModels:
    # Request tests (GET - no RequestBody)
    def test_request_builder(self): ...
    def test_request_query_parameters(self): ...
    # Response tests
    def test_response_inheritance(self): ...

class TestGetDatasetModels:
    # Request tests
    def test_request_builder(self): ...
    def test_request_path_parameters(self): ...
    # Response tests
    def test_response_inheritance(self): ...

class TestUpdateDatasetModels:
    # Request tests
    def test_request_builder(self): ...
    # RequestBody tests
    def test_request_body_builder(self): ...
    # Response tests
    def test_response_inheritance(self): ...

class TestDeleteDatasetModels:
    # Request tests
    def test_request_builder(self): ...
    # Response tests
    def test_response_inheritance(self): ...

class TestRetrieveFromDatasetModels:
    # Request tests
    def test_request_builder(self): ...
    # RequestBody tests
    def test_request_body_builder(self): ...
    # Response tests
    def test_response_inheritance(self): ...
```

```python
# test_document_models.py
class TestCreateDocumentByFileModels:
    # Request tests
    def test_request_builder(self): ...
    def test_file_upload_handling(self): ...
    # RequestBody tests
    def test_request_body_builder(self): ...
    # Response tests
    def test_response_inheritance(self): ...

class TestCreateDocumentByTextModels:
    # Request tests
    def test_request_builder(self): ...
    # RequestBody tests
    def test_request_body_builder(self): ...
    # Response tests
    def test_response_inheritance(self): ...

class TestListDocumentsModels:
    # Request tests
    def test_request_builder(self): ...
    # Response tests
    def test_response_inheritance(self): ...

# ... other document API test classes
```

```python
# test_segment_models.py
class TestListSegmentsModels:
    # Request tests
    def test_request_builder(self): ...
    # Response tests
    def test_response_inheritance(self): ...

class TestCreateSegmentModels:
    # Request tests
    def test_request_builder(self): ...
    # RequestBody tests
    def test_request_body_builder(self): ...
    # Response tests
    def test_response_inheritance(self): ...

class TestGetSegmentModels:
    # Request tests
    def test_request_builder(self): ...
    # Response tests
    def test_response_inheritance(self): ...

class TestUpdateSegmentModels:
    # Request tests
    def test_request_builder(self): ...
    # RequestBody tests
    def test_request_body_builder(self): ...
    # Response tests
    def test_response_inheritance(self): ...

class TestDeleteSegmentModels:
    # Request tests
    def test_request_builder(self): ...
    # Response tests
    def test_response_inheritance(self): ...
```

```python
# test_chunk_models.py
class TestListChildChunksModels:
    # Request tests
    def test_request_builder(self): ...
    # Response tests
    def test_response_inheritance(self): ...

class TestCreateChildChunkModels:
    # Request tests
    def test_request_builder(self): ...
    # RequestBody tests
    def test_request_body_builder(self): ...
    # Response tests
    def test_response_inheritance(self): ...

class TestUpdateChildChunkModels:
    # Request tests
    def test_request_builder(self): ...
    # RequestBody tests
    def test_request_body_builder(self): ...
    # Response tests
    def test_response_inheritance(self): ...

class TestDeleteChildChunkModels:
    # Request tests
    def test_request_builder(self): ...
    # Response tests
    def test_response_inheritance(self): ...
```

```python
# test_tag_models.py
class TestListTagsModels:
    # Request tests
    def test_request_builder(self): ...
    # Response tests
    def test_response_inheritance(self): ...

class TestCreateTagModels:
    # Request tests
    def test_request_builder(self): ...
    # RequestBody tests
    def test_request_body_builder(self): ...
    # Response tests
    def test_response_inheritance(self): ...

class TestUpdateTagModels:
    # Request tests
    def test_request_builder(self): ...
    # RequestBody tests
    def test_request_body_builder(self): ...
    # Response tests
    def test_response_inheritance(self): ...

class TestDeleteTagModels:
    # Request tests
    def test_request_builder(self): ...
    # RequestBody tests
    def test_request_body_builder(self): ...
    # Response tests
    def test_response_inheritance(self): ...

class TestBindTagsToDatasetModels:
    # Request tests
    def test_request_builder(self): ...
    # RequestBody tests
    def test_request_body_builder(self): ...
    # Response tests
    def test_response_inheritance(self): ...

class TestUnbindTagsFromDatasetModels:
    # Request tests
    def test_request_builder(self): ...
    # RequestBody tests
    def test_request_body_builder(self): ...
    # Response tests
    def test_response_inheritance(self): ...

class TestGetDatasetTagsModels:
    # Request tests
    def test_request_builder(self): ...
    # Response tests
    def test_response_inheritance(self): ...
```

```python
# test_model_models.py
class TestGetTextEmbeddingModelsModels:
    # Request tests
    def test_request_builder(self): ...
    # Response tests
    def test_response_inheritance(self): ...
```

**Public/Common classes get separate files:**
```python
# test_knowledge_public_models.py
class TestDatasetInfo:
    def test_builder_pattern(self): ...
    def test_field_validation(self): ...

class TestDocumentInfo:
    def test_builder_pattern(self): ...
    def test_field_validation(self): ...

class TestSegmentInfo:
    def test_builder_pattern(self): ...
    def test_field_validation(self): ...

class TestChildChunkInfo:
    def test_builder_pattern(self): ...
    def test_field_validation(self): ...

class TestTagInfo:
    def test_builder_pattern(self): ...
    def test_field_validation(self): ...

class TestModelInfo:
    def test_builder_pattern(self): ...
    def test_field_validation(self): ...

class TestFileInfo:
    def test_builder_pattern(self): ...
    def test_field_validation(self): ...

class TestProcessRule:
    def test_builder_pattern(self): ...
    def test_field_validation(self): ...

class TestRetrievalModel:
    def test_builder_pattern(self): ...
    def test_field_validation(self): ...

class TestBatchInfo:
    def test_builder_pattern(self): ...
    def test_field_validation(self): ...

class TestPaginationInfo:
    def test_builder_pattern(self): ...
    def test_field_validation(self): ...
```

```
tests/
└── knowledge/
    └── v1/
        ├── model/
        │   ├── test_dataset_models.py          # Dataset API tests (6 test classes)
        │   ├── test_document_models.py         # Document API tests (10 test classes)
        │   ├── test_segment_models.py          # Segment API tests (5 test classes)
        │   ├── test_chunk_models.py            # Child chunk API tests (4 test classes)
        │   ├── test_tag_models.py              # Tag API tests (7 test classes)
        │   ├── test_model_models.py            # Model API tests (1 test class)
        │   └── test_knowledge_public_models.py # All public models (DatasetInfo, DocumentInfo, SegmentInfo, ChildChunkInfo, TagInfo, ModelInfo, FileInfo, ProcessRule, RetrievalModel, BatchInfo, PaginationInfo, etc.)
        ├── resource/
        │   ├── test_dataset_resource.py        # Dataset resource tests
        │   ├── test_document_resource.py       # Document resource tests
        │   ├── test_segment_resource.py        # Segment resource tests
        │   ├── test_chunk_resource.py          # Chunk resource tests
        │   ├── test_tag_resource.py            # Tag resource tests
        │   └── test_model_resource.py          # Model resource tests
        ├── integration/
        │   ├── test_knowledge_api_integration.py # All 33 knowledge API integration tests
        │   ├── test_comprehensive_integration.py
        │   ├── test_examples_validation.py
        │   └── test_version_integration.py
        └── __init__.py
```

## Examples Strategy

### Examples Organization
**Decision**: Resource-based directory structure with API-specific files
- Each resource gets its own directory under `examples/knowledge/`
- Each API gets its own file within the resource directory
- Each file contains both sync and async examples

### Resource Naming Convention (MANDATORY)
**Decision**: All example resources MUST use "[Example]" prefix for safety
- **Creation Rule**: All resources created in examples MUST have "[Example]" prefix in their names
- **Deletion Rule**: Delete operations MUST only target resources with "[Example]" prefix
- **Safety Measure**: This prevents accidental deletion of production or important resources

### Code Minimalism Strategy
**Decision**: All examples follow minimal code principles while maintaining functionality
- **Objective**: Write only the ABSOLUTE MINIMAL amount of code needed to demonstrate each API correctly
- **Avoid Verbose Implementations**: Remove any code that doesn't directly contribute to the core demonstration
- **Maintain Core Functionality**: Ensure all essential features and safety checks remain intact

### Examples Documentation Consistency (CRITICAL)
**Issue Identified**: Current examples documentation has inconsistencies
- **knowledge-api.md**: Documents 33 APIs (6+10+5+4+7+1)
- **examples/README.md**: Claims 29 APIs (needs update)
- **Actual files**: Need to match 33 example files

**Required Fixes**:
1. **Update examples/knowledge/README.md**:
   - Correct total API count to 33 APIs
   - Add Segment Management section (5 APIs)
   - Add Child Chunks Management section (4 APIs)
   - Add Model Management section (1 API)
   - Correct Document Management to 10 APIs
   - Correct Tag Management to 7 APIs

2. **Verify Example File Completeness**:
   - Ensure all 33 APIs have corresponding example files
   - Remove duplicate or redundant files
   - Standardize file naming conventions

### Tests Structure Consistency (CRITICAL)
**Issue Identified**: Tests structure also has inconsistencies with API specifications
- **Current test structure**: Includes separate metadata/ tests and resources
- **API specification**: Metadata may be part of Document APIs (12 total)
- **Missing tests**: No model/ tests for Model Management API

**Test Structure Issues**:
1. **Missing Test Files**:
   - No `test_chunk_models.py` for Child Chunks Management APIs
   - No `test_chunk_resource.py` for Chunk resource
   - Missing chunk API integration tests
   - Need to verify `test_model_models.py` exists for Model Management API

2. **Test Coverage Gaps**:
   - Integration tests may not cover all 33 APIs
   - Resource tests may not match final 6-resource structure (Dataset, Document, Segment, Chunk, Tag, Model)
   - Need to ensure all test classes match the 33 API operations

3. **Resource Structure Alignment**:
   - Tests must align with 6-resource structure instead of previous structure
   - Chunk operations separated from Segment operations
   - All 33 APIs must have corresponding test coverage

**Required Test Fixes**:
1. **Add Missing Chunk Tests**:
   - Create `test_chunk_models.py` for Child Chunks Management APIs
   - Create `test_chunk_resource.py` for Chunk resource
   - Add chunk integration tests
   - Verify `test_model_models.py` exists for Model API

2. **Update Resource Structure Tests**:
   - Ensure tests align with 6-resource structure (Dataset, Document, Segment, Chunk, Tag, Model)
   - Separate chunk operations from segment operations in tests
   - Update resource tests to match final resource organization

3. **Verify Test Completeness**:
   - Ensure all 33 APIs have corresponding tests
   - Verify resource tests match final 6-resource structure
   - Update integration tests for complete API coverage
   - Ensure test class counts match API counts (6+10+5+4+7+1=33)

### Examples Directory Structure
```
examples/knowledge/
├── dataset/
│   ├── create_dataset.py              # Create dataset examples
│   ├── list_datasets.py               # List datasets examples
│   ├── get_dataset.py                 # Get dataset examples
│   ├── update_dataset.py              # Update dataset examples
│   ├── delete_dataset.py              # Delete dataset examples
│   └── retrieve_from_dataset.py       # Content retrieval examples
├── document/
│   ├── create_document_by_file.py     # File upload examples
│   ├── create_document_by_text.py     # Text document examples
│   ├── list_documents.py              # List documents examples
│   ├── get_document.py                # Get document examples
│   ├── update_document_by_file.py     # Update document with file
│   ├── update_document_by_text.py     # Update document with text
│   ├── delete_document.py             # Delete document examples
│   ├── update_document_status.py      # Document status management
│   ├── get_batch_indexing_status.py   # Check processing status
│   └── get_upload_file_info.py        # File info examples
├── segment/
│   ├── list_segments.py               # List segments examples
│   ├── create_segment.py              # Create segment examples
│   ├── get_segment.py                 # Get segment examples
│   ├── update_segment.py              # Update segment examples
│   └── delete_segment.py              # Delete segment examples
├── chunk/
│   ├── list_child_chunks.py           # List child chunks examples
│   ├── create_child_chunk.py          # Create child chunk examples
│   ├── update_child_chunk.py          # Update child chunk examples
│   └── delete_child_chunk.py          # Delete child chunk examples
├── tag/
│   ├── list_tags.py                   # List tags examples
│   ├── create_tag.py                  # Create tag examples
│   ├── update_tag.py                  # Update tag examples
│   ├── delete_tag.py                  # Delete tag examples
│   ├── bind_tags_to_dataset.py        # Bind tags examples
│   ├── unbind_tags_from_dataset.py    # Unbind tags examples
│   └── get_dataset_tags.py            # Get dataset tags examples
├── model/
│   └── get_text_embedding_models.py   # Get embedding models examples
└── README.md                          # Examples overview and usage guide
```

### Environment Variable Validation (MANDATORY)
**Decision**: All examples MUST validate required environment variables and raise errors
- **Validation Rule**: Check for required environment variables at the start of each function
- **Error Handling**: Raise `ValueError` with descriptive message if required variables are missing
- **Required Variables**: All examples must validate `API_KEY`, resource-specific examples must validate resource IDs

### Examples Content Strategy
- **Simple API Calls**: Each example focuses on a single API operation with minimal code
- **Educational Purpose**: Essential functionality demonstration without verbose explanations
- **Dual Versions**: Both synchronous and asynchronous implementations (mandatory)
- **Environment Validation**: All functions validate required environment variables and raise errors
- **Basic Error Handling**: Simple try-catch blocks for common exceptions
- **Real-world Data**: Use realistic but simple test data with "[Example]" prefix
- **Safety First**: All resource creation uses "[Example]" prefix, all deletion checks for this prefix
- **Cleanup Functions**: Delete examples include functions to clean up all example resources
- **Complete Coverage**: All 33 APIs must have corresponding example files
- **Documentation Accuracy**: Examples README must accurately reflect all implemented APIs

### Test Content Strategy
- **Complete API Coverage**: All 33 APIs must have corresponding test files
- **Resource Structure Alignment**: Test structure must match final resource organization
- **Model Test Completeness**: All model classes must have comprehensive tests
- **Integration Test Coverage**: All APIs must be covered in integration tests
- **Resource Test Accuracy**: Resource tests must match final resource implementations
- **Test Documentation**: Test structure must be documented and consistent

## Latest Improvements and Optimizations

### 1. Enhanced Dataset Management
**Recent Updates**:
- **Intelligent Indexing**: Advanced indexing strategies for optimal performance
- **Multi-modal Support**: Enhanced support for various content types and formats
- **Dynamic Configuration**: Real-time dataset configuration updates
- **Performance Analytics**: Comprehensive analytics for dataset usage and performance
- **Auto-optimization**: AI-powered dataset optimization suggestions

### 2. Advanced Document Processing
**Implementation Enhancements**:
- **Smart Parsing**: Intelligent document parsing with format detection
- **Batch Processing**: Efficient batch document processing capabilities
- **Version Control**: Document version management and history tracking
- **Quality Scoring**: Automatic quality assessment for processed documents
- **Metadata Extraction**: Advanced metadata extraction and enrichment

### 3. Intelligent Segmentation
**Latest Features**:
- **Context-aware Chunking**: Smart segmentation based on content context
- **Hierarchical Segments**: Support for nested segment structures
- **Semantic Boundaries**: Intelligent boundary detection for better segmentation
- **Dynamic Sizing**: Adaptive segment sizing based on content type
- **Quality Metrics**: Comprehensive quality metrics for segment evaluation

### 4. Advanced Search and Retrieval
**Recent Improvements**:
- **Hybrid Search**: Advanced hybrid search combining multiple techniques
- **Contextual Ranking**: Context-aware result ranking and scoring
- **Real-time Indexing**: Real-time content indexing for immediate availability
- **Personalization**: Personalized search results based on user preferences
- **Analytics Integration**: Search analytics and performance monitoring

### 5. Comprehensive Tag Management
**Tag System Enhancements**:
- **Hierarchical Tags**: Support for nested tag structures
- **Auto-tagging**: AI-powered automatic tag suggestion and assignment
- **Tag Analytics**: Comprehensive analytics for tag usage and effectiveness
- **Bulk Operations**: Efficient bulk tag management operations
- **Tag Relationships**: Support for tag relationships and dependencies

### 6. Model Integration
**Model Management Features**:
- **Multi-provider Support**: Support for multiple embedding model providers
- **Model Comparison**: Tools for comparing model performance
- **Auto-selection**: Intelligent model selection based on content type
- **Performance Monitoring**: Real-time model performance monitoring
- **Cost Optimization**: Cost-aware model selection and usage optimization

### 7. Examples and Tests Documentation Improvements
**Documentation Consistency Fixes**:
- **API Count Correction**: Updated examples documentation to reflect all 33 APIs
- **Missing Sections**: Added Segment Management (5 APIs), Child Chunks Management (4 APIs) and Model Management (1 API) sections
- **File Verification**: Ensured all APIs have corresponding example files
- **Naming Standardization**: Consistent file naming across all example categories
- **README Accuracy**: Examples README now matches API documentation specifications

**Test Structure Improvements**:
- **Missing Model Tests**: Added Model API tests for complete coverage
- **Test Structure Alignment**: Aligned test structure with final API specifications
- **Metadata Clarification**: Resolved metadata vs document test overlap
- **Complete Coverage**: Ensured all 33 APIs have corresponding test files
- **Resource Test Accuracy**: Updated resource tests to match final resource structure

## Summary

This design provides a comprehensive solution for knowledge base management in dify-oapi, covering all 33 knowledge-related APIs with a clean, maintainable architecture. The implementation prioritizes type safety, consistency, and developer experience while ensuring full compatibility with the latest Dify API specifications.

The multi-resource organization, combined with shared common models and descriptive method naming, creates an intuitive and powerful interface for knowledge operations including dataset management, document processing, segment management, child chunks management, tag operations, and model integration.

The examples strategy ensures developers have clear, educational references for every API operation, supporting both learning and integration testing needs with comprehensive sync/async coverage. The code minimalism approach optimizes all examples for clarity while maintaining full functionality and safety features.

### Key Features
- **Comprehensive Coverage**: Full implementation of all 33 knowledge base APIs with consistent architecture
- **Multi-resource Organization**: Logical separation of concerns across dataset, document, segment, chunk, tag, and model resources
- **Advanced Type Safety**: Strict typing with Literal types for all predefined values
- **Enhanced File Processing**: Complete file upload, processing, and management capabilities
- **Intelligent Segmentation**: Advanced segment management with separate child chunk operations
- **Hierarchical Content Structure**: Support for document → segment → child chunk hierarchy
- **Flexible Tag System**: Comprehensive tag management and binding capabilities
- **Model Integration**: Support for multiple embedding models and providers
- **Performance Optimization**: Enhanced indexing, search, and retrieval capabilities
- **Code Minimalism**: All knowledge examples follow minimal code principles
- **Safety Features**: Comprehensive validation and error handling mechanisms
- **Educational Focus**: Examples focus purely on demonstrating API functionality
- **Consistent Patterns**: Uniform architecture and naming conventions across all resources

### Documentation Consistency Requirements
- **Examples Documentation**: Must be updated to reflect all 33 APIs accurately (6+10+5+4+7+1)
- **File Completeness**: All APIs must have corresponding example files
- **Naming Standardization**: Consistent file naming across all example categories
- **README Accuracy**: Examples README must match API documentation specifications
- **Test Structure Consistency**: Test structure must align with final 6-resource API specifications
- **Test Coverage Completeness**: All 33 APIs must have corresponding test files
- **Resource Test Alignment**: Resource tests must match final 6-resource organization (Dataset, Document, Segment, Chunk, Tag, Model)
- **Integration Test Coverage**: All APIs must be covered in integration tests
- **Child Chunks Separation**: Child chunks management must be properly separated from segment management in both examples and tests