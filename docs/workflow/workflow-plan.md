# Workflow API Implementation Plan

This document provides step-by-step prompts for implementing the complete Workflow API functionality in the dify-oapi2 SDK. Each step includes implementation and testing phases to ensure code quality.

## Prerequisites

Before starting, ensure you understand:
- The existing dify-oapi2 project structure
- Current workflow implementation with separate resources (workflow, file, log, info)
- Pydantic models and builder patterns
- HTTP request/response handling
- Type safety with Literal types
- BaseRequest and BaseResponse inheritance patterns
- Migration requirements from nested to flat model structure
- File organization strategy: flat models, grouped resources
- Simple method naming convention

## File Organization Strategy

**Models**: Use flat structure in `v1/model/` directory
- All model files are placed directly in the model directory
- No subdirectories or grouping for models
- Enables easy imports and reduces nesting complexity

**Resources**: Use functional grouping in `v1/resource/` directory
- `workflow.py` - All workflow operations consolidated (run, detail, stop, upload, logs, info, parameters, site)

**Method Naming**: Use simple, concise names
- Core operations: `run`, `detail`, `stop`
- File operations: `upload`
- Log operations: `logs`
- Info operations: `info`, `parameters`, `site`
- Avoid redundant prefixes (e.g., `run` instead of `run_workflow` in Workflow resource)
- Async methods use `a` prefix (e.g., `arun`, `adetail`, `astop`)

**Ambiguity Resolution Rules (MANDATORY)**:
- When multiple operations in the same resource could cause naming ambiguity, use descriptive prefixes
- Update operations use `update_` prefix (e.g., `update_status` for document status updates)
- Get operations use `get_` prefix when needed for clarity (e.g., `get_batch_status` for batch indexing status)
- Maintain method names concise but unambiguous within the resource context
- Examples:
  - `update_status()` vs `get_batch_status()` - clearly different operations
  - `create_by_file()` vs `create_by_text()` - different creation methods
  - `update_by_file()` vs `update_by_text()` - different update methods

## Implementation Steps

### Step 0: Analyze and Plan Legacy Code Migration

**Analysis Prompt:**
```
Analyze the existing workflow implementation to plan the migration strategy.

Requirements:
1. Examine current structure:
   - dify_oapi/api/workflow/v1/model/ (nested directories: workflow/, file/, log/, info/)
   - dify_oapi/api/workflow/v1/resource/ (separate files: workflow.py, file.py, log.py, info.py)
   - dify_oapi/api/workflow/v1/version.py (multiple resource attributes)

2. Document existing functionality:
   - List all existing model files and their locations
   - Identify all existing resource methods
   - Map current API endpoints to new consolidated structure
   - Note any existing tests that need updating

3. Create migration plan:
   - Model file movement strategy (nested → flat)
   - Resource method consolidation plan
   - Import statement update requirements
   - Test migration strategy

4. Identify potential conflicts:
   - Duplicate model names across directories
   - Method signature differences
   - Import path dependencies
```

**Migration Planning Prompt:**
```
Create detailed migration steps for the legacy code consolidation.

Requirements:
1. Create migration checklist:
   - [ ] Backup existing implementation
   - [ ] Document current API surface
   - [ ] Plan model file movements
   - [ ] Plan resource consolidation
   - [ ] Update import statements
   - [ ] Migrate tests
   - [ ] Update version.py

2. Risk assessment:
   - Identify breaking changes
   - Plan backward compatibility measures
   - Document rollback procedures

3. Validation strategy:
   - Ensure all existing functionality preserved
   - Verify no API signature changes
   - Confirm test coverage maintained
```

### Step 1: Create Workflow Types and Base Models

**Implementation Prompt:**
```
Create the workflow types definition file and core data models for the workflow API.

Requirements:
1. Create `dify_oapi/api/workflow/v1/model/workflow_types.py` with all Literal types:

**CRITICAL: Class Naming Conflict Resolution**
All classes must use domain-specific prefixes to avoid naming conflicts:
- File-related: `WorkflowFile*` (e.g., `WorkflowFileInfo`)
- Log-related: `WorkflowLog*` (e.g., `WorkflowLogInfo`) 
- User-related: `WorkflowUser*` (e.g., `WorkflowEndUserInfo`)
- App-related: `WorkflowApp*` (e.g., `WorkflowAppInfo`)

2. Create `dify_oapi/api/workflow/v1/model/workflow_types.py` with all Literal types:
   - ResponseMode: "streaming" | "blocking"
   - FileType: "document" | "image" | "audio" | "video" | "custom"
   - TransferMethod: "remote_url" | "local_file"
   - WorkflowStatus: "running" | "succeeded" | "failed" | "stopped"
   - EventType: "workflow_started" | "node_started" | "text_chunk" | "node_finished" | "workflow_finished" | "tts_message" | "tts_message_end" | "ping"
   - IconType: "emoji" | "image"

3. Create core data models with builder patterns (using context-specific names):
   - `workflow_inputs.py`: Dynamic workflow input container
   - `workflow_file_info.py`: File information model for workflow execution
   - `file_upload_info.py`: File information model for upload responses
   - `workflow_node_info.py`: Workflow node information  
   - `workflow_execution_metadata.py`: Execution metadata with tokens, price, currency

4. All models must:
   - Inherit from pydantic.BaseModel
   - Include builder patterns with proper type hints
   - Use Literal types from workflow_types.py
   - Follow prefixed naming conventions to avoid conflicts

File structure:
- dify_oapi/api/workflow/v1/model/workflow_types.py
- dify_oapi/api/workflow/v1/model/workflow_inputs.py
- dify_oapi/api/workflow/v1/model/workflow_file_info.py
- dify_oapi/api/workflow/v1/model/file_upload_info.py
- dify_oapi/api/workflow/v1/model/workflow_node_info.py
- dify_oapi/api/workflow/v1/model/workflow_execution_metadata.py
```

**Testing Prompt:**
```
Create comprehensive tests for the workflow types and base models.

Requirements:
1. Create `tests/workflow/v1/model/test_workflow_public_models.py`
2. Test classes for each model (using context-specific names):
   - TestWorkflowInputs: builder pattern, field validation
   - TestWorkflowFileInfo: builder pattern, type validation, transfer method validation
   - TestFileUploadInfo: builder pattern, file metadata validation
   - TestWorkflowNodeInfo: builder pattern, field validation
   - TestWorkflowExecutionMetadata: builder pattern, numeric field validation

3. Test coverage must include:
   - Builder pattern functionality
   - Type validation with Literal types
   - Field assignment and retrieval
   - Invalid value rejection
   - Model serialization/deserialization

4. All test methods must have proper type annotations
5. Use pytest fixtures for common test data
```

### Step 2: Implement Run Workflow API Models

**Implementation Prompt:**
```
Implement the Run Workflow API request, request body, and response models.

Requirements:
1. Create `run_workflow_request.py`:
   - Inherit from BaseRequest
   - POST method to /v1/workflows/run
   - Include request_body attribute
   - Builder pattern with request_body() method

2. Create `run_workflow_request_body.py`:
   - Inherit from pydantic.BaseModel
   - Fields: inputs (WorkflowInputs), response_mode (ResponseMode), user (str), files (List[FileInfo])
   - Builder pattern with all field methods

3. Create `run_workflow_response.py`:
   - Inherit from BaseResponse (MANDATORY)
   - Fields: workflow_run_id, task_id, data (WorkflowRunInfo)
   - No builder pattern for response classes

4. Create `workflow_run_info.py`:
   - Public model inheriting from BaseModel
   - Fields: id, workflow_id, status, outputs, error, elapsed_time, total_tokens, total_steps, created_at, finished_at
   - Builder pattern required

5. All models must use proper type hints and Literal types
```

**Testing Prompt:**
```
Create tests for Run Workflow API models.

Requirements:
1. Add TestRunWorkflowModels class to `test_workflow_models.py`
2. Test methods:
   - test_request_builder: Verify builder pattern and URI/method setup
   - test_request_validation: Validate request structure
   - test_request_body_builder: Test all builder methods
   - test_request_body_validation: Validate field types and constraints
   - test_response_inheritance: Verify BaseResponse inheritance
   - test_response_data_access: Test response data access patterns

3. Add TestWorkflowRunInfo class to `test_workflow_public_models.py`
4. Test builder pattern and field validation for WorkflowRunInfo
5. Verify proper type safety with invalid inputs
```

### Step 3: Implement Get Workflow Run Detail API Models

**Implementation Prompt:**
```
Implement the Get Workflow Run Detail API models.

Requirements:
1. Create `get_workflow_run_detail_request.py`:
   - Inherit from BaseRequest
   - GET method to /v1/workflows/run/:workflow_run_id
   - Path parameter: workflow_run_id
   - Builder with workflow_run_id() method using paths["workflow_run_id"]

2. Create `get_workflow_run_detail_response.py`:
   - Inherit from BaseResponse (MANDATORY)
   - Fields: id, workflow_id, status, inputs (str), outputs (dict), error, total_steps, total_tokens, created_at, finished_at, elapsed_time
   - Use WorkflowStatus Literal type

3. Follow established patterns for GET requests with path parameters
4. Ensure proper type hints and validation
```

**Testing Prompt:**
```
Create tests for Get Workflow Run Detail API models.

Requirements:
1. Add TestGetWorkflowRunDetailModels class to `test_workflow_models.py`
2. Test methods:
   - test_request_builder: Verify builder pattern setup
   - test_request_path_parameters: Test path parameter handling
   - test_response_inheritance: Verify BaseResponse inheritance
   - test_response_field_types: Validate response field types

3. Test path parameter assignment and URI construction
4. Verify proper handling of nullable fields in response
```

### Step 4: Implement Stop Workflow API Models

**Implementation Prompt:**
```
Implement the Stop Workflow API models.

Requirements:
1. Create `stop_workflow_request.py`:
   - Inherit from BaseRequest
   - POST method to /v1/workflows/tasks/:task_id/stop
   - Path parameter: task_id
   - Include request_body attribute

2. Create `stop_workflow_request_body.py`:
   - Inherit from pydantic.BaseModel
   - Field: user (str, required)
   - Builder pattern with user() method

3. Create `stop_workflow_response.py`:
   - Inherit from BaseResponse (MANDATORY)
   - Field: result (str) - fixed return "success"

4. Follow established patterns for POST requests with path parameters and request body
```

**Testing Prompt:**
```
Create tests for Stop Workflow API models.

Requirements:
1. Add TestStopWorkflowModels class to `test_workflow_models.py`
2. Test methods:
   - test_request_builder: Verify builder pattern and path parameter handling
   - test_request_body_builder: Test request body builder
   - test_response_inheritance: Verify BaseResponse inheritance
   - test_response_success_result: Test fixed "success" result

3. Validate path parameter and request body integration
4. Test proper error handling patterns
```

### Step 5: Implement Upload File API Models

**Implementation Prompt:**
```
Implement the Upload File API models with multipart/form-data support.

Requirements:
1. Create `upload_file_request.py`:
   - Inherit from BaseRequest
   - POST method to /v1/files/upload
   - Special handling for multipart/form-data
   - Fields: file (BytesIO), request_body
   - Builder methods: file() and request_body()
   - Set files and body attributes for multipart handling

2. Create `upload_file_request_body.py`:
   - Inherit from pydantic.BaseModel
   - Field: user (str, required)
   - Builder pattern with user() method

3. Create `upload_file_response.py`:
   - Inherit from BaseResponse (MANDATORY)
   - Fields: id, name, size, extension, mime_type, created_by, created_at
   - Use proper UUID and timestamp types

4. Follow multipart/form-data pattern from design document
```

**Testing Prompt:**
```
Create tests for Upload File API models.

Requirements:
1. Add TestUploadFileModels class to `test_workflow_models.py`
2. Test methods:
   - test_request_builder: Verify multipart handling
   - test_request_file_handling: Test file upload mechanics
   - test_request_body_builder: Test request body builder
   - test_response_inheritance: Verify BaseResponse inheritance
   - test_response_file_metadata: Test file metadata fields

3. Mock BytesIO objects for file testing
4. Validate multipart/form-data structure
5. Test file name handling and metadata extraction
```

### Step 6: Implement Workflow Logs API Models

**Implementation Prompt:**
```
Implement the Get Workflow Logs API models.

Requirements:
1. Create `get_workflow_logs_request.py`:
   - Inherit from BaseRequest
   - GET method to /v1/workflows/logs
   - Query parameters: keyword, status, page, limit
   - Builder methods for all query parameters using add_query()

2. Create `get_workflow_logs_response.py`:
   - Inherit from BaseResponse (MANDATORY)
   - Fields: page, limit, total, has_more, data (List[LogInfo])

3. Create `log_info.py`:
   - Public model inheriting from BaseModel
   - Fields: id, workflow_run, created_from, created_by_role, created_by_account, created_by_end_user, created_at
   - Builder pattern required

4. Create `end_user_info.py`:
   - Public model for end user summary
   - Fields: id, type, is_anonymous, session_id
   - Builder pattern required

5. Use proper Literal types for status and role fields
```

**Testing Prompt:**
```
Create tests for Workflow Logs API models.

Requirements:
1. Add TestGetWorkflowLogsModels class to `test_workflow_models.py`
2. Test methods:
   - test_request_builder: Verify query parameter handling
   - test_request_query_parameters: Test all query parameter methods
   - test_response_inheritance: Verify BaseResponse inheritance
   - test_response_pagination: Test pagination fields

3. Add TestLogInfo and TestEndUserInfo classes to `test_workflow_public_models.py`
4. Test builder patterns and field validation
5. Verify proper query parameter encoding
```

### Step 7: Implement Application Info API Models

**Implementation Prompt:**
```
Implement the Application Information API models (info, parameters, site).

Requirements:
1. Create `get_info_request.py`, `get_parameters_request.py`, `get_site_request.py`:
   - All inherit from BaseRequest
   - GET methods to /v1/info, /v1/parameters, /v1/site respectively
   - Simple builders with no parameters

2. Create response models inheriting from BaseResponse:
   - `get_info_response.py`: name, description, tags
   - `get_parameters_response.py`: user_input_form, file_upload, system_parameters
   - `get_site_response.py`: title, icon_type, icon, icon_background, etc.

3. Create supporting public models with builders:
   - `app_info.py`: Basic app information
   - `parameters_info.py`: Parameter configuration
   - `site_info.py`: WebApp settings
   - `user_input_form.py`: Form configuration
   - `file_upload_config.py`: Upload settings
   - `system_parameters.py`: System limits

4. Use IconType Literal for icon_type field
```

**Testing Prompt:**
```
Create tests for Application Info API models.

Requirements:
1. Add test classes to `test_workflow_models.py`:
   - TestGetInfoModels
   - TestGetParametersModels
   - TestGetSiteModels

2. Test methods for each:
   - test_request_builder: Verify simple GET request setup
   - test_response_inheritance: Verify BaseResponse inheritance
   - test_response_fields: Validate response field types

3. Add test classes to `test_workflow_public_models.py`:
   - TestAppInfo, TestParametersInfo, TestSiteInfo
   - TestUserInputForm, TestFileUploadConfig, TestSystemParameters

4. Test builder patterns and field validation for all public models
5. Verify Literal type usage for icon_type and other constrained fields
```

### Step 8: Migrate and Consolidate Workflow Resource Classes

**Migration Prompt:**
```
Migrate existing resource classes into a single consolidated Workflow resource.

Requirements:
1. Analyze existing resource classes:
   - dify_oapi/api/workflow/v1/resource/workflow.py (existing methods)
   - dify_oapi/api/workflow/v1/resource/file.py (file methods to migrate)
   - dify_oapi/api/workflow/v1/resource/log.py (log methods to migrate)
   - dify_oapi/api/workflow/v1/resource/info.py (info methods to migrate)

2. Consolidate into single Workflow class:
   - Preserve all existing method signatures
   - Merge methods from File, Log, Info classes
   - Maintain backward compatibility
   - Update import statements for new model locations

3. New consolidated methods:
   - run(request, request_option, stream=False)
   - detail(request, request_option)
   - stop(request, request_option)
   - upload(request, request_option) # from File class
   - logs(request, request_option) # from Log class
   - info(request, request_option) # from Info class
   - parameters(request, request_option) # from Info class
   - site(request, request_option) # from Info class

4. Remove obsolete resource files after migration
```

**Implementation Prompt:**
```
Implement the consolidated Workflow resource class with all migrated functionality.

Requirements:
1. Update `dify_oapi/api/workflow/v1/resource/workflow.py`:
   - Extend existing Workflow class with methods from other resources
   - Maintain all existing method signatures for backward compatibility
   - Add new methods from File, Log, Info resources
   - Update imports to use flat model structure

2. Each method must have:
   - Sync and async versions (arun, etc.)
   - Proper type hints for parameters and return types
   - Stream support for run (Iterator[str] | AsyncIterator[str])
   - Transport.execute() for non-streaming
   - Transport.stream() for streaming

3. Migration validation:
   - Ensure no method signatures changed
   - Verify all existing functionality preserved
   - Test import path updates work correctly
```

**Testing Prompt:**
```
Create comprehensive tests for the Workflow resource class.

Requirements:
1. Create `tests/workflow/v1/resource/test_workflow_resource.py`
2. Test class TestWorkflowResource with methods:
   - test_run_sync: Test sync execution
   - test_run_async: Test async execution
   - test_run_streaming: Test streaming mode
   - test_detail: Test detail retrieval
   - test_stop: Test workflow stopping
   - test_upload: Test file upload
   - test_logs: Test log retrieval
   - test_info: Test app info
   - test_parameters: Test parameters
   - test_site: Test site settings

3. Use mock objects for Transport.execute() and Transport.stream()
4. Test both sync and async versions of all methods
5. Verify proper request/response handling and error propagation
```

### Step 9: Migrate Version Integration and Clean Up

**Migration Prompt:**
```
Migrate the version integration from multi-resource to single-resource structure.

Requirements:
1. Update `dify_oapi/api/workflow/v1/version.py`:
   - Current structure has: workflow, file, log, info attributes
   - Target structure: only workflow attribute
   - Remove imports for File, Log, Info classes
   - Update V1 class to only expose consolidated Workflow resource

2. Clean up obsolete files:
   - Remove `dify_oapi/api/workflow/v1/resource/file.py`
   - Remove `dify_oapi/api/workflow/v1/resource/log.py`
   - Remove `dify_oapi/api/workflow/v1/resource/info.py`
   - Remove empty model subdirectories (workflow/, file/, log/, info/)

3. Update resource __init__.py:
   - Remove exports for File, Log, Info classes
   - Keep only Workflow class export

4. Backward compatibility considerations:
   - Document breaking changes in access patterns
   - Provide migration guide for users
```

**Implementation Prompt:**
```
Implement the consolidated version integration and perform cleanup.

Requirements:
1. Update `dify_oapi/api/workflow/v1/version.py`:
   ```python
   # Before:
   class V1:
       def __init__(self, config: Config):
           self.workflow: Workflow = Workflow(config)
           self.file: File = File(config)
           self.log: Log = Log(config)
           self.info: Info = Info(config)
   
   # After:
   class V1:
       def __init__(self, config: Config):
           self.workflow = Workflow(config)  # All APIs consolidated
   ```

2. Verify service integration still works:
   - Check `dify_oapi/api/workflow/service.py`
   - Ensure V1 is properly exposed
   - Test client access: client.workflow.v1.workflow.method()

3. Clean up and validate:
   - Remove obsolete resource files
   - Update import statements throughout codebase
   - Verify no broken imports remain
```

**Testing Prompt:**
```
Create integration tests for migrated version and service integration.

Requirements:
1. Create `tests/workflow/v1/integration/test_version_integration.py`
2. Test methods:
   - test_v1_workflow_resource_access: Verify consolidated resource accessibility
   - test_workflow_service_integration: Test service integration after migration
   - test_client_workflow_access: Test end-to-end client access
   - test_legacy_api_compatibility: Verify existing API signatures still work
   - test_migration_completeness: Ensure all methods from old resources available

3. Migration validation tests:
   - test_no_broken_imports: Verify all imports work with new structure
   - test_obsolete_resources_removed: Confirm old resource files are gone
   - test_model_flat_structure: Verify models accessible from flat structure

4. Create `tests/workflow/v1/integration/test_workflow_api_integration.py`
5. Integration tests for all 8 APIs with mock responses
6. Test complete request/response cycles
7. Verify proper error handling and response parsing
8. Test both migrated and new functionality
```

### Step 10: Create Workflow Examples

**Implementation Prompt:**
```
Create comprehensive examples for all workflow APIs.

Requirements:
1. Create examples in `examples/workflow/` directory:
   - run_workflow.py: Basic and streaming execution examples
   - get_workflow_run_detail.py: Detail retrieval examples
   - stop_workflow.py: Workflow stopping examples
   - upload_file.py: File upload examples
   - get_workflow_logs.py: Log retrieval with filtering
   - get_info.py: App information examples
   - get_parameters.py: Parameters retrieval examples
   - get_site.py: Site settings examples

2. Each example must include:
   - Sync and async versions of each function
   - Environment variable validation (API_KEY required)
   - Proper error handling with try-catch blocks
   - "[Example]" prefix for all created resources
   - Minimal code following the minimalism principles

3. Follow established patterns:
   - Validate environment variables at function start
   - Use realistic but simple test data
   - Include basic success/error logging
   - Demonstrate both blocking and streaming modes where applicable

4. Update `examples/workflow/README.md` with usage instructions
```

**Testing Prompt:**
```
Create validation tests for all workflow examples.

Requirements:
1. Create `tests/workflow/v1/integration/test_examples_validation.py`
2. Test methods for each example:
   - test_run_workflow_example: Validate example structure
   - test_get_workflow_run_detail_example: Check detail example
   - test_stop_workflow_example: Validate stop example
   - test_upload_file_example: Check upload example
   - test_get_workflow_logs_example: Validate logs example
   - test_get_info_example: Check info example
   - test_get_parameters_example: Validate parameters example
   - test_get_site_example: Check site example

3. Validation checks:
   - Environment variable validation presence
   - "[Example]" prefix usage in test data
   - Proper error handling structure
   - Sync/async function pairs
   - Code minimalism compliance

4. Mock environment variables and API responses for testing
5. Verify examples can be imported and executed without errors
```

### Step 11: Comprehensive Testing and Migration Validation

**Implementation Prompt:**
```
Perform comprehensive testing including migration validation.

Requirements:
1. Run all existing tests and ensure they pass after migration
2. Check test coverage for all migrated and new code (aim for >90%)
3. Verify type checking with mypy passes with new import structure
4. Run linting with ruff and ensure compliance
5. Test integration with existing codebase after consolidation

Migration validation:
1. All existing API functionality preserved
2. No breaking changes in method signatures
3. Import paths updated correctly throughout codebase
4. Obsolete files properly removed
5. Model accessibility from flat structure

Quality checks:
1. All Response classes inherit from BaseResponse
2. All public models have builder patterns
3. Literal types used for all constrained fields
4. Proper error handling in all examples
5. Environment variable validation in examples
6. "[Example]" prefix usage in test data
7. Migration completeness verified

Create any missing tests or fix any issues found.
```

**Testing Prompt:**
```
Create final comprehensive integration tests including migration validation.

Requirements:
1. Create `tests/workflow/v1/integration/test_comprehensive_integration.py`
2. End-to-end workflow tests:
   - test_complete_workflow_cycle: Run → Detail → Stop
   - test_file_upload_and_workflow: Upload → Use in workflow
   - test_workflow_monitoring: Logs and status tracking
   - test_application_configuration: Info → Parameters → Site
   - test_migrated_functionality: Verify all migrated methods work

3. Migration validation tests:
   - test_legacy_api_parity: Compare old vs new API behavior
   - test_consolidated_resource_access: Verify single resource provides all functionality
   - test_import_path_migration: Ensure all imports work with flat structure
   - test_no_regression: Verify existing functionality unchanged

4. Performance and reliability tests:
   - test_streaming_performance: Streaming response handling
   - test_concurrent_requests: Multiple simultaneous requests
   - test_error_recovery: Error handling and recovery
   - test_timeout_handling: Request timeout scenarios

5. Mock all external API calls
6. Test complete request/response cycles
7. Verify proper resource cleanup
8. Test both sync and async execution paths
9. Validate migration completeness and correctness
```

### Step 12: Resolve Class Naming Conflicts

**Implementation Prompt:**
```
Resolve all class naming conflicts by adding domain-specific prefixes.

Requirements:
1. Rename conflicting classes with context-specific names:
   - `FileInfo` → `FileUploadInfo` (for file upload responses)
   - `LogInfo` → `WorkflowLogInfo` (for workflow log entries)
   - Keep `EndUserInfo` (no conflicts detected)
   - Keep `WorkflowRunLogInfo` (already context-specific)
   - Any other conflicting classes discovered during implementation

2. Update all import statements and references:
   - Update model files that import renamed classes
   - Update test files to use new class names
   - Update request/response models that reference renamed classes

3. Ensure consistency:
   - All workflow-domain classes use `Workflow*` prefix
   - No naming conflicts remain in the module
   - All tests pass with new class names

4. File operations:
   - Rename model files if needed for consistency
   - Update __init__.py exports
   - Verify no broken imports
```

**Testing Prompt:**
```
Update all tests to use the new prefixed class names.

Requirements:
1. Update test imports to use new class names
2. Update test class names to match new model names
3. Update all test method references to new classes
4. Ensure all tests pass with renamed classes
5. Verify no import errors or naming conflicts

Validation:
- All existing tests must pass
- No naming conflicts in test files
- Consistent use of prefixed names throughout
```

### Step 13: Documentation and Final Validation

**Implementation Prompt:**
```
Complete documentation and perform final validation.

Requirements:
1. Update project documentation:
   - Add workflow API section to main README.md
   - Update examples/README.md with workflow examples
   - Ensure all docstrings are complete and accurate

2. Create workflow-specific documentation:
   - API usage patterns and best practices
   - Common use cases and examples
   - Error handling guidelines
   - Performance optimization tips

3. Validate against design requirements:
   - All 8 APIs implemented correctly
   - Proper inheritance patterns followed
   - Type safety maintained throughout
   - Builder patterns implemented consistently

4. Prepare for release:
   - Version compatibility checks
   - Backward compatibility verification
   - Performance benchmarking
   - Security review of examples
```

**Testing Prompt:**
```
Perform final validation and acceptance testing.

Requirements:
1. Execute complete test suite and ensure 100% pass rate
2. Validate test coverage meets requirements (>90%)
3. Run integration tests against mock API responses
4. Verify examples work correctly with proper environment setup
5. Confirm no class naming conflicts remain

Acceptance criteria:
1. All 8 workflow APIs fully functional
2. Streaming support working correctly
3. File upload handling proper
4. Error handling robust and consistent
5. Examples educational and safe
6. Documentation complete and accurate
7. Type safety maintained throughout
8. Performance meets expectations
9. No class naming conflicts in entire module

Create final test report documenting:
- Test coverage statistics
- Performance benchmarks
- Known limitations or issues
- Recommendations for future improvements
- Class naming conflict resolution summary
```

## Success Criteria

The implementation is considered complete when:

1. **Functionality**: All 8 workflow APIs are fully implemented and functional
2. **Migration**: All existing functionality successfully migrated to consolidated structure
3. **Type Safety**: Complete type safety with Literal types and proper inheritance
4. **Testing**: Comprehensive test coverage (>90%) with all tests passing
5. **Examples**: Working examples for all APIs with proper safety measures
6. **Documentation**: Complete and accurate documentation including migration guide
7. **Integration**: Seamless integration with existing dify-oapi2 codebase
8. **Quality**: Code passes all linting, type checking, and quality gates
9. **Performance**: Streaming and file upload performance meets expectations
10. **Backward Compatibility**: No breaking changes in existing API signatures
11. **Clean Migration**: All obsolete files removed, imports updated, flat structure implemented

## Notes

- Each step builds upon the previous ones - complete them in order
- Test each step thoroughly before proceeding to the next
- Follow the established patterns from existing API implementations
- Maintain consistency with the overall project architecture
- Prioritize type safety and error handling throughout
- Keep examples minimal but functional and safe