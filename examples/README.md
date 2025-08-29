# Dify-OAPI Examples

This directory contains example code for using the Dify-OAPI SDK.

## Chat Examples
- [Blocking Response](./chat/blocking_response.py): Example of using the Chat API with blocking response mode
- [Streaming Response](./chat/streaming_response.py): Example of using the Chat API with streaming response mode
- [Conversation Management](./chat/conversation_management.py): Example of managing conversations and retrieving message history

## Completion Examples

### Message Processing
- [Send Message](./completion/completion/send_message.py): Send completion messages with streaming and blocking modes
- [Stop Response](./completion/completion/stop_response.py): Stop ongoing completion responses

### Annotation Management
- [List Annotations](./completion/annotation/list_annotations.py): List annotations for completion messages
- [Create Annotation](./completion/annotation/create_annotation.py): Create new annotations for messages
- [Update Annotation](./completion/annotation/update_annotation.py): Update existing annotations
- [Delete Annotation](./completion/annotation/delete_annotation.py): Delete specific annotations
- [Annotation Reply Settings](./completion/annotation/annotation_reply_settings.py): Configure annotation reply settings
- [Query Annotation Reply Status](./completion/annotation/query_annotation_reply_status.py): Check annotation reply operation status

### Audio Processing
- [Text to Audio](./completion/audio/text_to_audio.py): Convert text responses to audio format

### Feedback Management
- [Message Feedback](./completion/feedback/message_feedback.py): Submit feedback for completion messages
- [Get Feedbacks](./completion/feedback/get_feedbacks.py): Retrieve feedback data for analysis

### File Management
- [Upload File](./completion/file/upload_file.py): Upload files for use in completion requests

### Application Information
- [Get Application Info](./completion/info/get_info.py): Retrieve application configuration
- [Get Parameters](./completion/info/get_parameters.py): Get application parameters and settings
- [Get Site Info](./completion/info/get_site.py): Retrieve site-specific information

## Knowledge Base Examples

### Dataset Management
- [Create Dataset](./knowledge/dataset/create.py): Create new datasets with various configurations
- [List Datasets](./knowledge/dataset/list.py): List datasets with pagination and search
- [Get Dataset](./knowledge/dataset/get.py): Get detailed dataset information
- [Update Dataset](./knowledge/dataset/update.py): Update dataset configuration and settings
- [Delete Dataset](./knowledge/dataset/delete.py): Delete datasets with confirmation prompts
- [Retrieve from Dataset](./knowledge/dataset/retrieve.py): Perform retrieval search with different methods

### Metadata Management
- [Create Metadata](./knowledge/metadata/create.py): Create custom metadata fields
- [List Metadata](./knowledge/metadata/list.py): List metadata configuration and usage
- [Update Metadata](./knowledge/metadata/update.py): Update metadata field names
- [Delete Metadata](./knowledge/metadata/delete.py): Delete metadata fields with warnings
- [Toggle Built-in Metadata](./knowledge/metadata/toggle_builtin.py): Enable/disable built-in metadata
- [Update Document Metadata](./knowledge/metadata/update_document.py): Update document metadata values

### Tag Management
- [Create Tags](./knowledge/tag/create.py): Create knowledge type tags
- [List Tags](./knowledge/tag/list.py): List all available tags
- [Update Tags](./knowledge/tag/update.py): Update tag names
- [Delete Tags](./knowledge/tag/delete.py): Delete tags with confirmation
- [Bind Tags](./knowledge/tag/bind.py): Bind tags to datasets
- [Unbind Tags](./knowledge/tag/unbind.py): Unbind tags from datasets
- [Query Bound Tags](./knowledge/tag/query_bound.py): Query tags bound to datasets

### Documentation
- [Knowledge Base README](./knowledge/README.md): Comprehensive usage guide with examples and best practices

## Workflow Examples

### Workflow Execution
- [Run Workflow](./workflow/run_workflow.py): Execute workflows with blocking and streaming modes
- [Get Workflow Run Detail](./workflow/get_workflow_run_detail.py): Retrieve workflow execution details and status
- [Stop Workflow](./workflow/stop_workflow.py): Stop running workflow executions

### File Management
- [Upload File](./workflow/upload_file.py): Upload files for multimodal workflow support

### Logging and Monitoring
- [Get Workflow Logs](./workflow/get_workflow_logs.py): Retrieve workflow execution logs with filtering

### Application Configuration
- [Get Application Info](./workflow/get_info.py): Retrieve basic application information
- [Get Application Parameters](./workflow/get_parameters.py): Get application parameter configuration
- [Get WebApp Settings](./workflow/get_site.py): Retrieve WebApp settings and theming

### Documentation
- [Workflow README](./workflow/README.md): Comprehensive workflow API usage guide with safety features
