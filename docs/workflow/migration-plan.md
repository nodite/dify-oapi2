# Workflow API Migration Plan

## Migration Phases

### Phase 1: Model File Migration (37 files)

#### Step 1.1: Move Workflow Models (16 files)
```bash
# Move from model/workflow/ to model/
mv model/workflow/execution_metadata.py model/
mv model/workflow/get_workflow_run_detail_request.py model/
mv model/workflow/get_workflow_run_detail_response.py model/
mv model/workflow/node_info.py model/
mv model/workflow/run_specific_workflow_request_body.py model/
mv model/workflow/run_specific_workflow_request.py model/
mv model/workflow/run_specific_workflow_response.py model/
mv model/workflow/run_workflow_request_body.py model/
mv model/workflow/run_workflow_request.py model/
mv model/workflow/run_workflow_response.py model/
mv model/workflow/stop_workflow_request_body.py model/
mv model/workflow/stop_workflow_request.py model/
mv model/workflow/stop_workflow_response.py model/
mv model/workflow/streaming_event.py model/
mv model/workflow/workflow_file_info.py model/
mv model/workflow/workflow_inputs.py model/
mv model/workflow/workflow_run_data.py model/
mv model/workflow/workflow_run_info.py model/
mv model/workflow/workflow_types.py model/
```

#### Step 1.2: Move File Models (6 files)
```bash
# Move from model/file/ to model/
mv model/file/file_info.py model/
mv model/file/preview_file_request.py model/
mv model/file/preview_file_response.py model/
mv model/file/upload_file_request_body.py model/
mv model/file/upload_file_request.py model/
mv model/file/upload_file_response.py model/
```

#### Step 1.3: Move Log Models (5 files)
```bash
# Move from model/log/ to model/
mv model/log/end_user_info.py model/
mv model/log/get_workflow_logs_request.py model/
mv model/log/get_workflow_logs_response.py model/
mv model/log/log_info.py model/
mv model/log/workflow_run_log_info.py model/
```

#### Step 1.4: Move Info Models (10 files)
```bash
# Move from model/info/ to model/
mv model/info/app_info.py model/
mv model/info/file_upload_config.py model/
mv model/info/get_info_request.py model/
mv model/info/get_info_response.py model/
mv model/info/get_parameters_request.py model/
mv model/info/get_parameters_response.py model/
mv model/info/get_site_request.py model/
mv model/info/get_site_response.py model/
mv model/info/parameters_info.py model/
mv model/info/site_info.py model/
mv model/info/system_parameters.py model/
mv model/info/user_input_form.py model/
```

#### Step 1.5: Update Import Statements
- Update all model files to use flat imports
- Update resource files to use flat model imports
- Remove subdirectory references

#### Step 1.6: Cleanup
```bash
# Remove empty directories
rmdir model/workflow/
rmdir model/file/
rmdir model/log/
rmdir model/info/
```

### Phase 2: Resource Consolidation

#### Step 2.1: Consolidate Methods into Workflow Resource
Add to `resource/workflow.py`:
- `upload_file()` and `aupload_file()` from File resource
- `preview_file()` and `apreview_file()` from File resource  
- `get_workflow_logs()` and `aget_workflow_logs()` from Log resource
- `get_info()` and `aget_info()` from Info resource
- `get_parameters()` and `aget_parameters()` from Info resource
- `get_site()` and `aget_site()` from Info resource

#### Step 2.2: Update Imports in Workflow Resource
- Add imports for file, log, info models
- Update existing imports to use flat structure

#### Step 2.3: Remove Obsolete Resource Files
```bash
rm resource/file.py
rm resource/log.py  
rm resource/info.py
```

### Phase 3: Version Integration Update

#### Step 3.1: Update version.py
```python
# Before:
from .resource.file import File
from .resource.info import Info
from .resource.log import Log
from .resource.workflow import Workflow

class V1:
    def __init__(self, config: Config):
        self.workflow: Workflow = Workflow(config)
        self.file: File = File(config)
        self.log: Log = Log(config)
        self.info: Info = Info(config)

# After:
from .resource.workflow import Workflow

class V1:
    def __init__(self, config: Config):
        self.workflow = Workflow(config)
```

#### Step 3.2: Update resource/__init__.py
Remove exports for File, Log, Info classes

### Phase 4: Validation and Testing

#### Step 4.1: Import Validation
- Verify all model imports work
- Test resource imports
- Check version integration

#### Step 4.2: Functionality Testing  
- Test all 10 existing methods
- Verify streaming support
- Check async methods
- Validate request/response handling

#### Step 4.3: Integration Testing
- Test client access patterns
- Verify no breaking changes
- Check backward compatibility

## Rollback Plan

If issues arise:
1. Restore from git backup
2. Revert import changes
3. Restore original directory structure
4. Re-test functionality

## Success Validation

- [ ] All 37 model files in flat structure
- [ ] All 10 methods in single Workflow resource
- [ ] V1 exposes only workflow resource
- [ ] All imports working correctly
- [ ] No functionality regressions
- [ ] All tests passing