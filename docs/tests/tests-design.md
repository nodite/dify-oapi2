# Tests Design Document

## Overview

This document defines the standardized test file organization and implementation patterns for the dify-oapi2 project. All test files must follow these rules to ensure consistency, maintainability, and clarity.

## Test File Organization Rules (MANDATORY)

### Mixed Approach Strategy
**Decision**: Test files MUST be organized using mixed approach - by resource type, then by functionality

1. **Resource Separation**: Each resource gets its own test file
2. **API Operation Grouping**: Within each resource file, organize tests by API operation with dedicated test classes
3. **Method Organization**: Within each test class, organize methods by model type (Request, RequestBody, Response)
4. **Public Class Separation**: Create separate files for public/common model tests
5. **Flat Structure**: All model test files are placed directly in `tests/{module}/v1/model/` directory

### Naming Convention
- **API Test Files**: `test_{resource}_models.py` (e.g., `test_completion_models.py`, `test_file_models.py`)
- **Public Model Files**: `test_{resource}_public_models.py` (e.g., `test_completion_public_models.py`)

## Test Class Organization Pattern

### API-Specific Test Classes
**Within each resource test file, organize by API operations:**

```python
# test_completion_models.py
class TestSendMessageModels:
    # Request tests
    def test_request_builder(self) -> None: ...
    def test_request_validation(self) -> None: ...
    # RequestBody tests  
    def test_request_body_builder(self) -> None: ...
    def test_request_body_validation(self) -> None: ...
    # Response tests
    def test_response_inheritance(self) -> None: ...
    def test_response_data_access(self) -> None: ...

class TestStopResponseModels:
    # Request tests
    def test_request_builder(self) -> None: ...
    def test_request_validation(self) -> None: ...
    # RequestBody tests
    def test_request_body_builder(self) -> None: ...
    # Response tests
    def test_response_inheritance(self) -> None: ...
```

### Public Model Test Classes
**Public/Common classes get separate files:**

```python
# test_completion_public_models.py
class TestCompletionMessageInfo:
    def test_builder_pattern(self) -> None: ...
    def test_field_validation(self) -> None: ...
    def test_serialization(self) -> None: ...
    def test_direct_instantiation(self) -> None: ...

class TestUsage:
    def test_builder_pattern(self) -> None: ...
    def test_field_validation(self) -> None: ...
```

## Method Organization Rules

### Standard Method Types per Test Class

#### For Request Classes
- `test_request_builder()` - Test builder pattern functionality
- `test_request_validation()` - Test field validation and constraints
- `test_request_path_parameters()` - Test path parameter handling (if applicable)
- `test_request_query_parameters()` - Test query parameter handling (if applicable)
- `test_request_file_handling()` - Test file upload handling (for multipart requests)

#### For RequestBody Classes
- `test_request_body_builder()` - Test builder pattern functionality
- `test_request_body_validation()` - Test field validation and constraints
- `test_request_body_serialization()` - Test model_dump functionality
- `test_request_body_data_serialization()` - Test nested data serialization (for multipart)

#### For Response Classes
- `test_response_inheritance()` - Verify BaseResponse inheritance (MANDATORY)
- `test_response_data_access()` - Test data field access and validation
- `test_response_error_handling()` - Test error response scenarios

#### For Public Classes
- `test_builder_pattern()` - Test fluent interface functionality
- `test_field_validation()` - Test pydantic field validation
- `test_serialization()` - Test model_dump and serialization
- `test_direct_instantiation()` - Test both builder and direct creation

## Code Quality Requirements (MANDATORY)

### Type Annotations
**ALL test methods MUST include proper type annotations:**

```python
def test_request_builder(self) -> None:
    """Test request builder pattern functionality."""
    # Implementation

def test_response_inheritance(self) -> None:
    """Test that response inherits from BaseResponse."""
    # Implementation
```

### Inheritance Testing
**CRITICAL**: ALL Response classes MUST be tested for BaseResponse inheritance:

```python
def test_response_inheritance(self) -> None:
    """Test SendMessageResponse inherits from BaseResponse."""
    response = SendMessageResponse()
    assert isinstance(response, BaseResponse)
    assert hasattr(response, 'success')
    assert hasattr(response, 'code')
    assert hasattr(response, 'msg')
    assert hasattr(response, 'raw')
```

### Builder Pattern Testing
**ALL classes with builders MUST test the builder pattern:**

```python
def test_request_builder(self) -> None:
    """Test SendMessageRequest builder pattern."""
    request = (
        SendMessageRequest.builder()
        .request_body(request_body)
        .build()
    )
    assert request.request_body is not None
    assert request.http_method == HttpMethod.POST
```

### Minimal Code Principle
- Write only essential test code
- Remove verbose implementations
- Focus on critical functionality
- Avoid redundant test cases
- Keep setup and teardown minimal

## Directory Structure

### Completion Module
```
tests/completion/v1/model/
├── test_completion_models.py        # SendMessage, StopResponse API tests
├── test_completion_public_models.py # CompletionMessageInfo, Usage, etc.
├── test_file_models.py              # UploadFile API tests
├── test_file_public_models.py       # FileInfo, etc.
├── test_feedback_models.py          # MessageFeedback, GetFeedbacks API tests
├── test_feedback_public_models.py   # FeedbackInfo, etc.
├── test_audio_models.py             # TextToAudio API tests
├── test_audio_public_models.py      # AudioInfo, etc.
├── test_info_models.py              # GetInfo, GetParameters, GetSite API tests
├── test_info_public_models.py       # AppInfo, ParametersInfo, SiteInfo, etc.
├── test_annotation_models.py        # All annotation API tests
└── test_annotation_public_models.py # AnnotationInfo, JobStatusInfo, etc.
```

### Workflow Module
```
tests/workflow/v1/model/
├── test_workflow_models.py          # RunWorkflow, RunSpecificWorkflow, GetWorkflowRunDetail, StopWorkflow API tests
├── test_workflow_public_models.py   # WorkflowRunInfo, NodeInfo, ExecutionMetadata, etc.
├── test_file_models.py              # UploadFile, PreviewFile API tests
├── test_file_public_models.py       # FileInfo, etc.
├── test_log_models.py               # GetWorkflowLogs API tests
├── test_log_public_models.py        # LogInfo, EndUserInfo, etc.
├── test_info_models.py              # GetInfo, GetParameters, GetSite API tests
└── test_info_public_models.py       # AppInfo, ParametersInfo, SiteInfo, etc.
```

### Knowledge Base Module
```
tests/knowledge_base/v1/model/
├── test_dataset_models.py           # Create, List, Get, Update, Delete, Retrieve API tests
├── test_dataset_public_models.py    # DatasetInfo, RetrievalModel, RerankingModel, etc.
├── test_document_models.py          # All document API tests
├── test_document_public_models.py   # DocumentInfo, ProcessRule, etc.
├── test_segment_models.py           # All segment API tests
├── test_segment_public_models.py    # SegmentInfo, ChildChunkInfo, etc.
├── test_metadata_models.py          # All metadata API tests
├── test_metadata_public_models.py   # MetadataInfo, etc.
├── test_tag_models.py               # All tag API tests
└── test_tag_public_models.py        # TagInfo, etc.
```

## HTTP Method Specific Patterns

### GET Request Tests
```python
class TestListModels:
    def test_request_builder(self) -> None:
        """Test GET request builder with query parameters."""
        request = (
            ListRequest.builder()
            .keyword("test")
            .page(1)
            .limit(10)
            .build()
        )
        assert request.http_method == HttpMethod.GET
        # No RequestBody tests for GET requests
    
    def test_response_inheritance(self) -> None:
        """Test response inherits from BaseResponse."""
        # Standard response inheritance test
```

### POST Request Tests
```python
class TestCreateModels:
    def test_request_builder(self) -> None:
        """Test POST request builder."""
        # Test request builder
    
    def test_request_body_builder(self) -> None:
        """Test POST request body builder."""
        # Test request body builder
    
    def test_response_inheritance(self) -> None:
        """Test response inherits from BaseResponse."""
        # Standard response inheritance test
```

### DELETE Request Tests
```python
class TestDeleteModels:
    def test_request_builder(self) -> None:
        """Test DELETE request builder with path parameters."""
        request = (
            DeleteRequest.builder()
            .resource_id("123")
            .build()
        )
        assert request.resource_id == "123"
        # No RequestBody tests for DELETE requests
    
    def test_response_inheritance(self) -> None:
        """Test response inherits from BaseResponse."""
        # Standard response inheritance test
```

### Multipart/Form-Data Request Tests
```python
class TestCreateByFileModels:
    def test_request_file_handling(self) -> None:
        """Test file upload handling in multipart requests."""
        file_io = BytesIO(b"test content")
        request = (
            CreateByFileRequest.builder()
            .file(file_io, "test.txt")
            .build()
        )
        assert request.file is not None
        assert request.files is not None
    
    def test_request_body_data_serialization(self) -> None:
        """Test nested data serialization for multipart form."""
        # Test complex form data handling
```

## Special Testing Requirements

### BaseResponse Inheritance (CRITICAL)
**EVERY Response class MUST be tested for BaseResponse inheritance:**

```python
def test_response_inheritance(self) -> None:
    """Test {ResponseClass} inherits from BaseResponse."""
    response = {ResponseClass}()
    
    # Test inheritance
    assert isinstance(response, BaseResponse)
    
    # Test required properties
    assert hasattr(response, 'success')
    assert hasattr(response, 'code') 
    assert hasattr(response, 'msg')
    assert hasattr(response, 'raw')
    
    # Test property types
    assert isinstance(response.success, (bool, type(None)))
    assert isinstance(response.code, (str, type(None)))
    assert isinstance(response.msg, (str, type(None)))
```

### Builder Pattern Testing
**ALL classes with builders MUST test builder functionality:**

```python
def test_builder_pattern(self) -> None:
    """Test {ClassName} builder pattern."""
    instance = (
        {ClassName}.builder()
        .field1("value1")
        .field2("value2")
        .build()
    )
    
    assert instance.field1 == "value1"
    assert instance.field2 == "value2"
    
    # Test method chaining
    builder = {ClassName}.builder()
    assert builder.field1("test") is builder  # Returns self
```

### Public Class Testing
**Public classes MUST test both builder and direct instantiation:**

```python
def test_direct_instantiation(self) -> None:
    """Test {ClassName} direct instantiation alongside builder."""
    # Direct instantiation
    direct = {ClassName}(field1="value1", field2="value2")
    
    # Builder instantiation  
    builder = (
        {ClassName}.builder()
        .field1("value1")
        .field2("value2")
        .build()
    )
    
    # Both should work and be equivalent
    assert direct.field1 == builder.field1
    assert direct.field2 == builder.field2
```

## Testing Best Practices

### Fixtures and Setup
```python
import pytest
from typing import Any

@pytest.fixture
def sample_request_body() -> RequestBodyClass:
    """Provide sample request body for tests."""
    return (
        RequestBodyClass.builder()
        .field1("test")
        .field2(123)
        .build()
    )

class TestApiModels:
    def test_with_fixture(self, sample_request_body: RequestBodyClass) -> None:
        """Test using pytest fixture."""
        # Use fixture in test
```

### Error Testing
```python
def test_validation_errors(self) -> None:
    """Test field validation errors."""
    with pytest.raises(ValidationError):
        InvalidClass(required_field=None)
```

### Async Testing
```python
@pytest.mark.asyncio
async def test_async_functionality(self) -> None:
    """Test async functionality where applicable."""
    # Test async scenarios
```

## Migration Guidelines

### From Old Structure
1. **Identify Resource Groups**: Determine which tests belong to which resources
2. **Extract API Operations**: Group tests by API operations within each resource
3. **Separate Public Classes**: Move public class tests to separate files
4. **Maintain Coverage**: Ensure no test coverage is lost during migration
5. **Update Imports**: Update all import statements after migration
6. **Verify Functionality**: Run all tests to ensure migration success

### Validation Checklist
- [ ] All test methods have type annotations
- [ ] All Response classes test BaseResponse inheritance
- [ ] All builder patterns are tested
- [ ] Public classes test both builder and direct instantiation
- [ ] File organization follows the established pattern
- [ ] No test coverage is lost
- [ ] All tests pass after migration

## Success Criteria

### Code Quality
- All tests pass without errors
- Proper type annotations on all methods
- Minimal code while maintaining coverage
- Follows established patterns

### Organization
- Clear separation by resource type
- API operations properly grouped
- Public classes in separate files
- Consistent naming conventions

### Functionality
- No loss of test coverage
- All builder patterns tested
- BaseResponse inheritance verified
- Both sync and async scenarios covered

### Performance
- Test execution time reasonable
- No significant performance degradation
- Proper test isolation maintained

## Notes

- Keep original files until migration is confirmed successful
- Update import statements only after verifying new files work
- Maintain backward compatibility during transition
- Focus on minimal code while preserving full functionality
- Each test class should be focused and cohesive
- Avoid cross-dependencies between test files
- Use descriptive test method names that explain what is being tested