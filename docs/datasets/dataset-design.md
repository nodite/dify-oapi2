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

### 7. Model File Organization
**Decision**: Organize models by resource grouping with shared common models

```
model/
├── dataset/          # Dataset-specific models
│   ├── create_request.py
│   ├── create_response.py
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
# Example: metadata resource
class Metadata:
    def __init__(self, transport: Transport):
        self._transport = transport
    
    def create(self, request: MetadataCreateRequest, request_option: RequestOption) -> MetadataCreateResponse:
        # Implementation
    
    async def acreate(self, request: MetadataCreateRequest, request_option: RequestOption) -> MetadataCreateResponse:
        # Async implementation
```

### Model Class Pattern
```python
# Example: shared common model
@dataclass
class RetrievalModel:
    search_method: str
    reranking_enable: Optional[bool] = None
    reranking_model: Optional[RerankingModel] = None
    top_k: Optional[int] = None
    score_threshold_enabled: Optional[bool] = None
    score_threshold: Optional[float] = None
    
    @classmethod
    def builder(cls) -> "RetrievalModelBuilder":
        return RetrievalModelBuilder()
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

### Error Handling
- Consistent error response handling across all APIs
- Proper HTTP status code mapping
- Detailed error message propagation

### Testing Strategy
- Unit tests for all resource methods
- Integration tests with mock API responses
- Validation tests for all model classes

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

## Summary

This design provides a comprehensive solution for dataset management in dify-oapi, covering all 19 dataset-related APIs with a clean, maintainable architecture. The implementation prioritizes type safety, consistency, and developer experience while ensuring full compatibility with the latest Dify API specifications.

The modular resource-based organization, combined with shared common models and descriptive method naming, creates an intuitive and powerful interface for dataset management operations including CRUD operations, metadata management, tag management, and advanced retrieval functionality.

The examples strategy ensures developers have clear, educational references for every API operation, supporting both learning and integration testing needs with comprehensive sync/async coverage.