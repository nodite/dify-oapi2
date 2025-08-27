# Tests Refactoring Plan

## Overview

This document provides step-by-step prompts for refactoring the oversized test files in the dify-oapi2 project. The current test files are too large (1394-1925 lines) and need to be split using a mixed approach: by resource type first, then by functionality.

## Current Issues

- `test_completion_models.py` - 1394 lines
- `test_document_models.py` - 1504 lines
- `test_workflow_models.py` - 1925 lines

## Refactoring Strategy

**Mixed Approach**: Resource type → API operations → Model types
- Each resource gets separate test files
- Within each file, organize by API operations (test classes)
- Within each class, organize by model types (methods)
- Public/common classes get separate files

## Step-by-Step Implementation

### Phase 1: Completion Module Refactoring

#### Step 1.1: Analyze Current Completion Tests
**Prompt:**
```
Analyze the current `tests/completion/v1/model/test_completion_models.py` file and provide:

1. List all test classes and methods currently in the file
2. Identify which tests belong to which resources (completion, file, feedback, audio, info, annotation)
3. Identify which tests are for public/common classes vs API-specific classes
4. Provide a breakdown of line counts per resource
5. List all the APIs being tested and their corresponding model types (Request, RequestBody, Response)

Output format:
- Resource breakdown with line counts
- API operations per resource
- Public classes identified
- Recommended file split structure
```

#### Step 1.2: Create Completion Core Tests
**Prompt:**
```
Create `tests/completion/v1/model/test_completion_models.py` with the following requirements:

**Test Organization:**
- `TestSendMessageModels` class for send_message API
- `TestStopResponseModels` class for stop_response API

**Within each test class, organize methods by model type:**
- Request tests: `test_request_builder()`, `test_request_validation()`
- RequestBody tests: `test_request_body_builder()`, `test_request_body_validation()`
- Response tests: `test_response_inheritance()`, `test_response_data_access()`

**Requirements:**
- All test methods must have proper type annotations
- Use pytest fixtures for common setup
- Test builder patterns for all models
- Verify BaseResponse inheritance for all Response classes
- Test both sync and async scenarios where applicable
- Keep only essential tests, remove verbose implementations

**Extract from existing test_completion_models.py:**
- SendMessageRequest, SendMessageRequestBody, SendMessageResponse tests
- StopResponseRequest, StopResponseRequestBody, StopResponseResponse tests
- Remove any public class tests (those go in separate file)

Ensure minimal code while maintaining full test coverage.
```

#### Step 1.3: Test Completion Core Implementation
**Prompt:**
```
Run the completion core tests and verify:

1. All tests pass without errors
2. Test coverage includes all critical paths
3. Builder patterns work correctly
4. BaseResponse inheritance is properly tested
5. Type annotations are correct

Fix any issues found and ensure the test file follows the established patterns from the design documents.

Report:
- Test execution results
- Coverage metrics
- Any issues found and fixed
- Confirmation that the file structure matches the design requirements
```

#### Step 1.4: Create Completion Public Models Tests
**Prompt:**
```
Create `tests/completion/v1/model/test_completion_public_models.py` with:

**Test Classes for Public Models:**
- `TestCompletionMessageInfo` - test builder pattern and field validation
- `TestUsage` - test builder pattern and field validation
- `TestRetrieverResource` - test builder pattern and field validation
- `TestMetadata` - test builder pattern and field validation

**Each test class should include:**
- `test_builder_pattern()` - verify fluent interface works
- `test_field_validation()` - verify pydantic validation
- `test_serialization()` - verify model_dump works correctly
- `test_direct_instantiation()` - verify both builder and direct creation work

**Requirements:**
- Extract public class tests from original test_completion_models.py
- All methods must have type annotations
- Test both builder pattern and direct instantiation
- Verify all public classes inherit from BaseModel (not BaseResponse)
- Keep tests minimal but comprehensive

Focus only on classes that inherit from BaseModel and have builder patterns.
```

#### Step 1.5: Test Completion Public Models
**Prompt:**
```
Run the completion public models tests and verify:

1. All public model tests pass
2. Builder patterns work correctly for all public classes
3. Direct instantiation works alongside builder patterns
4. Pydantic validation is properly tested
5. No public class inherits from BaseResponse (should be BaseModel only)

Fix any issues and ensure consistency with design requirements.

Report test results and confirm the public models are properly separated from API-specific models.
```

#### Step 1.6: Create File Resource Tests
**Prompt:**
```
Create `tests/completion/v1/model/test_file_models.py` with:

**Test Classes:**
- `TestUploadFileModels` class for upload_file API

**Method Organization:**
- Request tests: `test_request_builder()`, `test_request_validation()`, `test_request_file_handling()`
- RequestBody tests: `test_request_body_builder()`, `test_request_body_validation()`
- Response tests: `test_response_inheritance()`, `test_response_data_access()`

**Special Requirements:**
- Test multipart/form-data handling for file uploads
- Verify file stream handling in request builder
- Test both files and body fields in BaseRequest
- Ensure proper content-type handling

Extract file-related tests from original test_completion_models.py and organize according to the new structure.
```

#### Step 1.7: Test File Resource Implementation
**Prompt:**
```
Run the file resource tests and verify:

1. File upload functionality is properly tested
2. Multipart/form-data handling works correctly
3. File stream handling is tested
4. All file-related models follow the established patterns

Fix any issues and ensure file upload tests are comprehensive but minimal.
```

#### Step 1.8: Create Feedback Resource Tests
**Prompt:**
```
Create `tests/completion/v1/model/test_feedback_models.py` with:

**Test Classes:**
- `TestMessageFeedbackModels` class for message_feedback API
- `TestGetFeedbacksModels` class for get_feedbacks API

**Method Organization per class:**
- Request tests: `test_request_builder()`, `test_request_validation()`
- RequestBody tests: `test_request_body_builder()` (for POST requests only)
- Response tests: `test_response_inheritance()`, `test_response_data_access()`

Extract feedback-related tests from original test_completion_models.py.
```

#### Step 1.9: Test Feedback Resource Implementation
**Prompt:**
```
Run feedback resource tests and verify all feedback functionality is properly tested with minimal code.
```

#### Step 1.10: Create Audio Resource Tests
**Prompt:**
```
Create `tests/completion/v1/model/test_audio_models.py` with:

**Test Classes:**
- `TestTextToAudioModels` class for text_to_audio API

**Method Organization:**
- Request tests: `test_request_builder()`, `test_request_validation()`
- RequestBody tests: `test_request_body_builder()`, `test_request_body_validation()`
- Response tests: `test_response_inheritance()`, `test_response_data_access()`

Extract audio-related tests from original test_completion_models.py.
```

#### Step 1.11: Test Audio Resource Implementation
**Prompt:**
```
Run audio resource tests and verify all audio functionality is properly tested.
```

#### Step 1.12: Create Info Resource Tests
**Prompt:**
```
Create `tests/completion/v1/model/test_info_models.py` with:

**Test Classes:**
- `TestGetInfoModels` class for get_info API
- `TestGetParametersModels` class for get_parameters API
- `TestGetSiteModels` class for get_site API

**Method Organization per class:**
- Request tests: `test_request_builder()`, `test_request_validation()` (GET requests, no RequestBody)
- Response tests: `test_response_inheritance()`, `test_response_data_access()`

Extract info-related tests from original test_completion_models.py.
```

#### Step 1.13: Test Info Resource Implementation
**Prompt:**
```
Run info resource tests and verify all info functionality is properly tested.
```

#### Step 1.14: Create Annotation Resource Tests
**Prompt:**
```
Create `tests/completion/v1/model/test_annotation_models.py` with:

**Test Classes:**
- `TestListAnnotationsModels` class
- `TestCreateAnnotationModels` class
- `TestUpdateAnnotationModels` class
- `TestDeleteAnnotationModels` class
- `TestAnnotationReplySettingsModels` class
- `TestQueryAnnotationReplyStatusModels` class

**Method Organization per class:**
- Request tests: `test_request_builder()`, `test_request_validation()`
- RequestBody tests: `test_request_body_builder()` (for POST/PUT requests)
- Response tests: `test_response_inheritance()`, `test_response_data_access()`

Extract annotation-related tests from original test_completion_models.py.
```

#### Step 1.15: Test Annotation Resource Implementation
**Prompt:**
```
Run annotation resource tests and verify all annotation functionality is properly tested.
```

#### Step 1.16: Create Remaining Public Model Tests
**Prompt:**
```
Create additional public model test files as needed:

- `tests/completion/v1/model/test_file_public_models.py` - FileInfo, etc.
- `tests/completion/v1/model/test_feedback_public_models.py` - FeedbackInfo, etc.
- `tests/completion/v1/model/test_audio_public_models.py` - AudioInfo, etc.
- `tests/completion/v1/model/test_info_public_models.py` - AppInfo, ParametersInfo, SiteInfo, etc.
- `tests/completion/v1/model/test_annotation_public_models.py` - AnnotationInfo, JobStatusInfo, etc.

Each file should follow the same pattern as test_completion_public_models.py.
```

#### Step 1.17: Test All Public Model Files
**Prompt:**
```
Run all public model tests and verify they work correctly with minimal code.
```

#### Step 1.18: Cleanup Original Completion Test File
**Prompt:**
```
After confirming all new test files work correctly:

1. Verify all tests from original test_completion_models.py have been migrated
2. Run all new completion test files to ensure 100% pass rate
3. Delete the original `tests/completion/v1/model/test_completion_models.py` file
4. Update any import statements that reference the old file

Provide a summary of:
- Total number of new test files created
- Line count reduction achieved
- Test coverage maintained
- Any issues encountered during migration
```

### Phase 2: Workflow Module Refactoring

#### Step 2.1: Analyze Current Workflow Tests
**Prompt:**
```
Analyze `tests/workflow/v1/model/test_workflow_models.py` (1925 lines) and provide:

1. List all test classes and methods
2. Identify which tests belong to which resources (workflow, file, log, info)
3. Identify public/common classes vs API-specific classes
4. Provide breakdown of line counts per resource
5. List all APIs being tested and their model types

Output the recommended file split structure for workflow module.
```

#### Step 2.2: Create Workflow Core Tests
**Prompt:**
```
Create `tests/workflow/v1/model/test_workflow_models.py` with:

**Test Classes:**
- `TestRunWorkflowModels` class for run_workflow API
- `TestRunSpecificWorkflowModels` class for run_specific_workflow API
- `TestGetWorkflowRunDetailModels` class for get_workflow_run_detail API
- `TestStopWorkflowModels` class for stop_workflow API

**Method Organization per class:**
- Request tests: `test_request_builder()`, `test_request_validation()`
- RequestBody tests: `test_request_body_builder()` (for POST requests)
- Response tests: `test_response_inheritance()`, `test_response_data_access()`

**Special Requirements:**
- Test streaming response handling for workflow execution
- Verify path parameter handling for workflow_id and task_id
- Test both sync and async scenarios

Extract workflow-related tests from original test_workflow_models.py.
```

#### Step 2.3: Test Workflow Core Implementation
**Prompt:**
```
Run workflow core tests and verify all workflow functionality is properly tested.
```

#### Step 2.4: Create Workflow Public Models Tests
**Prompt:**
```
Create `tests/workflow/v1/model/test_workflow_public_models.py` with:

**Test Classes:**
- `TestWorkflowRunInfo` - test builder pattern and field validation
- `TestNodeInfo` - test builder pattern and field validation
- `TestExecutionMetadata` - test builder pattern and field validation
- `TestStreamingEvent` - test builder pattern and field validation

Extract public class tests from original test_workflow_models.py.
```

#### Step 2.5: Test Workflow Public Models
**Prompt:**
```
Run workflow public models tests and verify they work correctly.
```

#### Step 2.6: Create Workflow File Tests
**Prompt:**
```
Create `tests/workflow/v1/model/test_file_models.py` with:

**Test Classes:**
- `TestUploadFileModels` class for upload_file API
- `TestPreviewFileModels` class for preview_file API

**Method Organization:**
- Request tests with file handling for upload
- Response tests for both APIs

Extract file-related tests from original test_workflow_models.py.
```

#### Step 2.7: Test Workflow File Implementation
**Prompt:**
```
Run workflow file tests and verify file functionality is properly tested.
```

#### Step 2.8: Create Workflow Log Tests
**Prompt:**
```
Create `tests/workflow/v1/model/test_log_models.py` with:

**Test Classes:**
- `TestGetWorkflowLogsModels` class for get_workflow_logs API

**Method Organization:**
- Request tests: `test_request_builder()`, `test_request_query_parameters()`
- Response tests: `test_response_inheritance()`, `test_response_data_access()`

Extract log-related tests from original test_workflow_models.py.
```

#### Step 2.9: Test Workflow Log Implementation
**Prompt:**
```
Run workflow log tests and verify log functionality is properly tested.
```

#### Step 2.10: Create Workflow Info Tests
**Prompt:**
```
Create `tests/workflow/v1/model/test_info_models.py` with:

**Test Classes:**
- `TestGetInfoModels` class for get_info API
- `TestGetParametersModels` class for get_parameters API
- `TestGetSiteModels` class for get_site API

Extract info-related tests from original test_workflow_models.py.
```

#### Step 2.11: Test Workflow Info Implementation
**Prompt:**
```
Run workflow info tests and verify info functionality is properly tested.
```

#### Step 2.12: Create Remaining Workflow Public Model Tests
**Prompt:**
```
Create additional workflow public model test files:
- `test_file_public_models.py` - FileInfo, etc.
- `test_log_public_models.py` - LogInfo, EndUserInfo, etc.
- `test_info_public_models.py` - AppInfo, ParametersInfo, SiteInfo, etc.
```

#### Step 2.13: Test All Workflow Public Models
**Prompt:**
```
Run all workflow public model tests and verify they work correctly.
```

#### Step 2.14: Cleanup Original Workflow Test File
**Prompt:**
```
After confirming all new workflow test files work:
1. Verify complete migration from original test_workflow_models.py
2. Run all new workflow test files
3. Delete original file
4. Update import statements
5. Provide migration summary
```

### Phase 3: Knowledge Base Module Refactoring

#### Step 3.1: Analyze Current Knowledge Base Tests
**Prompt:**
```
Analyze `tests/knowledge_base/v1/model/test_document_models.py` (1504 lines) and provide:

1. List all test classes and methods
2. Identify which tests belong to document APIs vs public classes
3. Provide breakdown of line counts per API operation
4. List all document APIs being tested (create_by_text, create_by_file, update_by_text, etc.)

Output the recommended file split structure for document module.
```

#### Step 3.2: Create Document Core Tests
**Prompt:**
```
Create `tests/knowledge_base/v1/model/test_document_models.py` with:

**Test Classes:**
- `TestCreateByTextModels` class for create_by_text API
- `TestCreateByFileModels` class for create_by_file API
- `TestUpdateByTextModels` class for update_by_text API
- `TestUpdateByFileModels` class for update_by_file API
- `TestIndexingStatusModels` class for indexing_status API
- `TestDeleteModels` class for delete API
- `TestListModels` class for list API
- `TestGetModels` class for get API
- `TestUpdateStatusModels` class for update_status API
- `TestGetUploadFileModels` class for get_upload_file API

**Method Organization per class:**
- Request tests: `test_request_builder()`, `test_request_validation()`
- RequestBody tests: `test_request_body_builder()` (for POST/PATCH requests)
- Response tests: `test_response_inheritance()`, `test_response_data_access()`

**Special Requirements:**
- Test multipart/form-data handling for file upload APIs
- Test nested data structure pattern for complex form data
- Verify file stream handling and form data separation

Extract document API tests from original test_document_models.py.
```

#### Step 3.3: Test Document Core Implementation
**Prompt:**
```
Run document core tests and verify all document API functionality is properly tested.
```

#### Step 3.4: Create Document Public Models Tests
**Prompt:**
```
Create `tests/knowledge_base/v1/model/test_document_public_models.py` with:

**Test Classes:**
- `TestDocumentInfo` - test builder pattern and field validation
- `TestProcessRule` - test builder pattern and field validation
- `TestPreProcessingRule` - test builder pattern and field validation
- `TestSegmentation` - test builder pattern and field validation
- `TestDataSourceInfo` - test builder pattern and field validation
- `TestUploadFileInfo` - test builder pattern and field validation
- `TestIndexingStatusInfo` - test builder pattern and field validation

Extract public class tests from original test_document_models.py.
```

#### Step 3.5: Test Document Public Models
**Prompt:**
```
Run document public models tests and verify they work correctly.
```

#### Step 3.6: Analyze and Refactor Dataset Tests
**Prompt:**
```
Analyze `tests/knowledge_base/v1/model/test_dataset_models.py` and create:

1. `test_dataset_models.py` - with TestCreateModels, TestListModels, TestGetModels, TestUpdateModels, TestDeleteModels, TestRetrieveModels classes
2. `test_dataset_public_models.py` - with TestDatasetInfo, TestRetrievalModel, TestRerankingModel classes

Follow the same pattern as document tests.
```

#### Step 3.7: Test Dataset Implementation
**Prompt:**
```
Run all dataset tests and verify they work correctly.
```

#### Step 3.8: Analyze and Refactor Segment Tests
**Prompt:**
```
Analyze `tests/knowledge_base/v1/model/test_segment_models.py` and create:

1. `test_segment_models.py` - with TestCreateModels, TestListModels, TestDeleteModels, TestGetModels, TestUpdateModels, TestCreateChildChunkModels, TestListChildChunksModels, TestDeleteChildChunkModels, TestUpdateChildChunkModels classes
2. `test_segment_public_models.py` - with TestSegmentInfo, TestChildChunkInfo, TestSegmentData classes

Follow the same pattern as previous tests.
```

#### Step 3.9: Test Segment Implementation
**Prompt:**
```
Run all segment tests and verify they work correctly.
```

#### Step 3.10: Refactor Metadata and Tag Tests
**Prompt:**
```
Analyze and refactor:
1. `test_metadata_models.py` - split into API tests and public models
2. `test_tag_models.py` - split into API tests and public models

Follow the established patterns.
```

#### Step 3.11: Test Metadata and Tag Implementation
**Prompt:**
```
Run all metadata and tag tests and verify they work correctly.
```

#### Step 3.12: Cleanup Original Knowledge Base Test Files
**Prompt:**
```
After confirming all new knowledge base test files work:
1. Verify complete migration from all original files
2. Run all new test files
3. Delete original files
4. Update import statements
5. Provide comprehensive migration summary for knowledge base module
```

### Phase 4: Final Verification and Cleanup

#### Step 4.1: Run Complete Test Suite
**Prompt:**
```
Run the complete test suite for all modules and verify:

1. All tests pass without errors
2. No test coverage is lost during refactoring
3. All new test files follow the established patterns
4. Test execution time is reasonable
5. No import errors or missing dependencies

Provide a comprehensive report of:
- Total test files before vs after refactoring
- Line count reduction achieved
- Test execution performance
- Any issues found and resolved
```

#### Step 4.2: Update Test Configuration
**Prompt:**
```
Update any test configuration files, CI/CD pipelines, or documentation that references the old test file structure:

1. Check pytest configuration files
2. Update GitHub Actions workflows if needed
3. Update any documentation that references test files
4. Verify test discovery works correctly with new structure

Provide a list of all files updated and changes made.
```

#### Step 4.3: Create Migration Summary Report
**Prompt:**
```
Create a comprehensive migration summary report including:

1. **Before/After Comparison:**
   - Original file count and line counts
   - New file count and line counts
   - Percentage reduction in file sizes

2. **Test Organization Improvements:**
   - Resource-based separation achieved
   - API operation grouping implemented
   - Public class separation completed

3. **Quality Improvements:**
   - Test maintainability enhanced
   - Code readability improved
   - Test discovery simplified

4. **Migration Statistics:**
   - Total files created
   - Total files removed
   - Test coverage maintained
   - Performance impact

5. **Future Maintenance Benefits:**
   - Easier to add new tests
   - Better test isolation
   - Clearer test organization
   - Reduced merge conflicts

Save this report as `docs/tests-migration-report.md`
```

## Success Criteria

Each step must meet these criteria before proceeding:

1. **Code Quality:**
   - All tests pass without errors
   - Proper type annotations on all methods
   - Minimal code while maintaining coverage
   - Follows established patterns from design documents

2. **Organization:**
   - Clear separation by resource type
   - API operations properly grouped
   - Public classes in separate files
   - Consistent naming conventions

3. **Functionality:**
   - No loss of test coverage
   - All builder patterns tested
   - BaseResponse inheritance verified
   - Both sync and async scenarios covered

4. **Performance:**
   - Test execution time reasonable
   - No significant performance degradation
   - Proper test isolation maintained

## Notes

- Each step should be completed and tested before moving to the next
- Keep the original files until migration is confirmed successful
- Update import statements only after verifying new files work
- Maintain backward compatibility during transition
- Focus on minimal code while preserving full functionality
