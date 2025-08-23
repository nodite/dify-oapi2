# Workflow Application APIs

This document covers all workflow application APIs. Workflow applications have no conversation support and are suitable for translation, article writing, summarization AI, etc.

## Base URL

```
http://localhost/v1
```

## Authentication

Service API uses `API-Key` for authentication. **It is strongly recommended that developers store the `API-Key` in the backend rather than sharing or storing it on the client side to prevent `API-Key` leakage and financial loss.**

All API requests should include your `API-Key` in the **`Authorization`** HTTP Header:

```
Authorization: Bearer {API_KEY}
```

## APIs

### 1. Execute Workflow

**POST** `/workflows/run`

Executes a workflow. Cannot be executed without a published workflow.

#### Request Body
- `inputs` (object, required): Allows passing values for variables defined in the App. The inputs parameter contains multiple key-value pairs, where each key corresponds to a specific variable and each value is the specific value of that variable. Variables can be file list types.
  File list type variables are suitable for passing files combined with text understanding and answering questions, only available when the model supports the file parsing capability of that type. If the variable is a file list type, the corresponding value should be in list format, with each element containing the following:
  - `type` (string): Supported types:
    - `document`: Specific types include: 'TXT', 'MD', 'MARKDOWN', 'PDF', 'HTML', 'XLSX', 'XLS', 'DOCX', 'CSV', 'EML', 'MSG', 'PPTX', 'PPT', 'XML', 'EPUB'
    - `image`: Specific types include: 'JPG', 'JPEG', 'PNG', 'GIF', 'WEBP', 'SVG'
    - `audio`: Specific types include: 'MP3', 'M4A', 'WAV', 'WEBM', 'AMR'
    - `video`: Specific types include: 'MP4', 'MOV', 'MPEG', 'MPGA'
    - `custom`: Specific types include: other file types
  - `transfer_method` (string): Transfer method, `remote_url` for image URL / `local_file` for uploaded file
  - `url` (string): Image URL (only when transfer method is `remote_url`)
  - `upload_file_id` (string): Upload file ID (only when transfer method is `local_file`)
- `response_mode` (string, required): Response mode
  - `streaming`: Streaming mode (recommended). Implements typewriter-style streaming output based on SSE (Server-Sent Events)
  - `blocking`: Blocking mode, waits for execution to complete before returning results. (Requests may be interrupted if the process is lengthy). *Due to Cloudflare limitations, requests will be interrupted after 100 seconds without response.*
- `user` (string, required): User identifier, used to define the identity of the end user for retrieval and statistics. Defined by developers, must ensure user identifier is unique within the application. API cannot access sessions created by WebApp.
- `files` (array[object], optional): Uploaded files
- `trace_id` (string, optional): Trace ID. Suitable for integrating with existing trace components in business systems to achieve end-to-end distributed tracing scenarios. If not specified, the system will automatically generate a `trace_id`. Supports the following three ways of passing, with priority in order:
  1. Header: Recommended to pass through HTTP Header `X-Trace-Id`, highest priority
  2. Query parameter: Pass through URL query parameter `trace_id`
  3. Request Body: Pass through request body field `trace_id` (this field)

#### Response

When `response_mode` is `blocking`, returns WorkflowResponse object.
When `response_mode` is `streaming`, returns ChunkWorkflowResponse object stream sequence.

##### WorkflowResponse

Returns complete App result, `Content-Type` is `application/json`.

- `workflow_run_id` (string): Workflow execution ID
- `task_id` (string): Task ID, used for request tracking and stop response interface
- `data` (object): Detailed content
  - `id` (string): Workflow execution ID
  - `workflow_id` (string): Associated Workflow ID
  - `status` (string): Execution status, `running` / `succeeded` / `failed` / `stopped`
  - `outputs` (json, optional): Output content
  - `error` (string, optional): Error reason
  - `elapsed_time` (float, optional): Time consumed (s)
  - `total_tokens` (int, optional): Total tokens used
  - `total_steps` (int): Total steps (redundant), default 0
  - `created_at` (timestamp): Start time
  - `finished_at` (timestamp): End time

##### ChunkWorkflowResponse

Returns App output streaming blocks, `Content-Type` is `text/event-stream`.
Each streaming block starts with data: and blocks are separated by `\n\n` (two newlines):

```
data: {"event": "text_chunk", "workflow_run_id": "b85e5fc5-751b-454d-b14e-dc5f240b0a31", "task_id": "bd029338-b068-4d34-a331-fc85478922c2", "data": {"text": "为了", "from_variable_selector": ["1745912968134", "text"]}}\n\n
```

Streaming blocks have different structures based on different `event` types:

- `event: workflow_started` - Workflow start execution
  - `task_id` (string): Task ID, used for request tracking and stop response interface
  - `workflow_run_id` (string): Workflow execution ID
  - `event` (string): Fixed as `workflow_started`
  - `data` (object): Detailed content
    - `id` (string): Workflow execution ID
    - `workflow_id` (string): Associated Workflow ID
    - `created_at` (timestamp): Start time

- `event: node_started` - Node start execution
  - `task_id` (string): Task ID, used for request tracking and stop response interface
  - `workflow_run_id` (string): Workflow execution ID
  - `event` (string): Fixed as `node_started`
  - `data` (object): Detailed content
    - `id` (string): Workflow execution ID
    - `node_id` (string): Node ID
    - `node_type` (string): Node type
    - `title` (string): Node name
    - `index` (int): Execution sequence number, used to display Tracing Node order
    - `predecessor_node_id` (string): Predecessor node ID, used for canvas display execution path
    - `inputs` (object): All predecessor node variable content used in the node
    - `created_at` (timestamp): Start time

- `event: text_chunk` - Text fragment
  - `task_id` (string): Task ID, used for request tracking and stop response interface
  - `workflow_run_id` (string): Workflow execution ID
  - `event` (string): Fixed as `text_chunk`
  - `data` (object): Detailed content
    - `text` (string): Text content
    - `from_variable_selector` (array): Text source path, helps developers understand which node's which variable generated the text

- `event: node_finished` - Node execution end, success and failure are different states in the same event
  - `task_id` (string): Task ID, used for request tracking and stop response interface
  - `workflow_run_id` (string): Workflow execution ID
  - `event` (string): Fixed as `node_finished`
  - `data` (object): Detailed content
    - `id` (string): Node execution ID
    - `node_id` (string): Node ID
    - `index` (int): Execution sequence number, used to display Tracing Node order
    - `predecessor_node_id` (string, optional): Predecessor node ID, used for canvas display execution path
    - `inputs` (object): All predecessor node variable content used in the node
    - `process_data` (json, optional): Node process data
    - `outputs` (json, optional): Output content
    - `status` (string): Execution status `running` / `succeeded` / `failed` / `stopped`
    - `error` (string, optional): Error reason
    - `elapsed_time` (float, optional): Time consumed (s)
    - `execution_metadata` (json): Metadata
      - `total_tokens` (int, optional): Total tokens used
      - `total_price` (decimal, optional): Total cost
      - `currency` (string, optional): Currency, such as `USD` / `RMB`
    - `created_at` (timestamp): Start time

- `event: workflow_finished` - Workflow execution end, success and failure are different states in the same event
  - `task_id` (string): Task ID, used for request tracking and stop response interface
  - `workflow_run_id` (string): Workflow execution ID
  - `event` (string): Fixed as `workflow_finished`
  - `data` (object): Detailed content
    - `id` (string): Workflow execution ID
    - `workflow_id` (string): Associated Workflow ID
    - `status` (string): Execution status `running` / `succeeded` / `failed` / `stopped`
    - `outputs` (json, optional): Output content
    - `error` (string, optional): Error reason
    - `elapsed_time` (float, optional): Time consumed (s)
    - `total_tokens` (int, optional): Total tokens used
    - `total_steps` (int): Total steps (redundant), default 0
    - `created_at` (timestamp): Start time
    - `finished_at` (timestamp): End time

- `event: tts_message` - TTS audio stream event, i.e., speech synthesis output. Content is Mp3 format audio blocks, base64 encoded strings, can be decoded directly for playback. (Only available when auto-play is enabled)
  - `task_id` (string): Task ID, used for request tracking and stop response interface
  - `message_id` (string): Message unique ID
  - `audio` (string): Audio blocks after speech synthesis using Base64 encoding, can be decoded directly and sent to player for playback
  - `created_at` (int): Creation timestamp, e.g., 1705395332

- `event: tts_message_end` - TTS audio stream end event, receiving this event means audio stream return has ended
  - `task_id` (string): Task ID, used for request tracking and stop response interface
  - `message_id` (string): Message unique ID
  - `audio` (string): End event has no audio, so this is an empty string
  - `created_at` (int): Creation timestamp, e.g., 1705395332

- `event: ping` - Ping event every 10s to keep connection alive

#### Errors
- 400, `invalid_param`: Invalid parameters
- 400, `app_unavailable`: App configuration unavailable
- 400, `provider_not_initialize`: No available model credential configuration
- 400, `provider_quota_exceeded`: Model call quota exceeded
- 400, `model_currently_not_support`: Current model unavailable
- 400, `workflow_request_error`: Workflow execution failed
- 500: Internal server error

### 2. Execute Specific Version Workflow

**POST** `/workflows/:workflow_id/run`

Executes a specific version of the workflow by specifying the workflow ID through path parameters.

#### Path Parameters
- `workflow_id` (string, required): Workflow ID, used to specify a specific version of the workflow
  How to obtain: You can query the workflow ID of a specific version in the version history.

#### Request Body
Same as Execute Workflow API above.

#### Response
Same as Execute Workflow API above.

#### Errors
- 400, `invalid_param`: Invalid parameters
- 400, `app_unavailable`: App configuration unavailable
- 400, `provider_not_initialize`: No available model credential configuration
- 400, `provider_quota_exceeded`: Model call quota exceeded
- 400, `model_currently_not_support`: Current model unavailable
- 400, `workflow_not_found`: Specified workflow version not found
- 400, `draft_workflow_error`: Cannot use draft workflow version
- 400, `workflow_id_format_error`: Workflow ID format error, UUID format required
- 400, `workflow_request_error`: Workflow execution failed
- 500: Internal server error

### 3. Get Workflow Execution Details

**GET** `/workflows/run/:workflow_run_id`

Gets the current execution result of a workflow task based on the workflow execution ID.

#### Path Parameters
- `workflow_run_id` (string, required): Workflow execution ID, can be obtained from streaming return Chunk

#### Response
- `id` (string): Workflow execution ID
- `workflow_id` (string): Associated Workflow ID
- `status` (string): Execution status `running` / `succeeded` / `failed` / `stopped`
- `inputs` (json): Task input content
- `outputs` (json): Task output content
- `error` (string): Error reason
- `total_steps` (int): Total task execution steps
- `total_tokens` (int): Total task execution tokens
- `created_at` (timestamp): Task start time
- `finished_at` (timestamp): Task end time
- `elapsed_time` (float): Time consumed (s)

### 4. Stop Response

**POST** `/workflows/tasks/:task_id/stop`

Only supports streaming mode.

#### Path Parameters
- `task_id` (string, required): Task ID, can be obtained from streaming return Chunk

#### Request Body
- `user` (string, required): User identifier, used to define the identity of the end user, must be consistent with the user passed in the send message interface. API cannot access sessions created by WebApp.

#### Response
- `result` (string): Fixed return "success"

### 5. Upload File

**POST** `/files/upload`

Uploads files for use when sending messages, enabling multimodal understanding.
Supports any format supported by your workflow.
*Uploaded files are only available for the current end user.*

#### Request Body (multipart/form-data)
- `file` (file, required): File to upload
- `user` (string, required): User identifier, used to define the identity of the end user, must be consistent with the user passed in the send message interface

#### Response

After successful upload, the server returns the file ID and related information.

- `id` (uuid): ID
- `name` (string): File name
- `size` (int): File size (bytes)
- `extension` (string): File extension
- `mime_type` (string): File mime-type
- `created_by` (uuid): Uploader ID
- `created_at` (timestamp): Upload time

#### Errors
- 400, `no_file_uploaded`: Must provide file
- 400, `too_many_files`: Currently only accepts one file
- 400, `unsupported_preview`: This file does not support preview
- 400, `unsupported_estimate`: This file does not support estimation
- 413, `file_too_large`: File too large
- 415, `unsupported_file_type`: Unsupported extension, currently only accepts document files
- 503, `s3_connection_failed`: Unable to connect to S3 service
- 503, `s3_permission_denied`: No permission to upload files to S3
- 503, `s3_file_too_large`: File exceeds S3 size limit

### 6. File Preview

**GET** `/files/:file_id/preview`

Preview or download uploaded files. This endpoint allows you to access files previously uploaded through the file upload API.
*Files can only be accessed within the scope of messages belonging to the requesting application.*

#### Path Parameters
- `file_id` (string, required): Unique identifier of the file to preview, obtained from the file upload API response

#### Query Parameters
- `as_attachment` (boolean, optional): Whether to force download the file as an attachment. Default is `false` (preview in browser)

#### Response
Returns file content with appropriate headers for browser display or download.

- `Content-Type`: Set according to file MIME type
- `Content-Length`: File size in bytes (if available)
- `Content-Disposition`: Set to "attachment" if `as_attachment=true`
- `Cache-Control`: Cache headers for performance
- `Accept-Ranges`: Set to "bytes" for audio/video files

#### Errors
- 400, `invalid_param`: Invalid parameters
- 403, `file_access_denied`: File access denied or file does not belong to current application
- 404, `file_not_found`: File not found or has been deleted
- 500: Internal server error

### 7. Get Workflow Logs

**GET** `/workflows/logs`

Returns workflow logs in reverse order.

#### Query Parameters
- `keyword` (string, optional): Keyword
- `status` (string, optional): Execution status succeeded/failed/stopped
- `page` (int, optional): Current page number, default 1
- `limit` (int, optional): Records per page, default 20
- `created_by_end_user_session_id` (string, optional): Created by which endUser, e.g., `abc-123`
- `created_by_account` (string, optional): Created by which email account, e.g., lizb@test.com

#### Response
- `page` (int): Current page number
- `limit` (int): Records per page
- `total` (int): Total records
- `has_more` (bool): Whether there is more data
- `data` (array[object]): Current page data
  - `id` (string): Identifier
  - `workflow_run` (object): Workflow execution log
    - `id` (string): Identifier
    - `version` (string): Version
    - `status` (string): Execution status, `running` / `succeeded` / `failed` / `stopped`
    - `error` (string, optional): Error
    - `elapsed_time` (float): Time consumed, in seconds
    - `total_tokens` (int): Number of tokens consumed
    - `total_steps` (int): Execution step length
    - `created_at` (timestamp): Start time
    - `finished_at` (timestamp): End time
  - `created_from` (string): Source
  - `created_by_role` (string): Role
  - `created_by_account` (string, optional): Account
  - `created_by_end_user` (object): User
    - `id` (string): Identifier
    - `type` (string): Type
    - `is_anonymous` (bool): Whether anonymous
    - `session_id` (string): Session identifier
  - `created_at` (timestamp): Creation time

### 8. Get Application Basic Information

**GET** `/info`

Used to get basic information of the application.

#### Response
- `name` (string): Application name
- `description` (string): Application description
- `tags` (array[string]): Application tags
- `mode` (string): Application mode
- `author_name` (string): Author name

### 9. Get Application Parameters

**GET** `/parameters`

Used to get function switches, input parameter names, types and default values when entering the page.

#### Response
- `user_input_form` (array[object]): User input form configuration
  - `text-input` (object): Text input control
    - `label` (string): Control display label name
    - `variable` (string): Control ID
    - `required` (bool): Whether required
    - `default` (string): Default value
  - `paragraph` (object): Paragraph text input control
    - `label` (string): Control display label name
    - `variable` (string): Control ID
    - `required` (bool): Whether required
    - `default` (string): Default value
  - `select` (object): Dropdown control
    - `label` (string): Control display label name
    - `variable` (string): Control ID
    - `required` (bool): Whether required
    - `default` (string): Default value
    - `options` (array[string]): Option values
- `file_upload` (object): File upload configuration
  - `document` (object): Document settings
    Currently only supports document types: `txt`, `md`, `markdown`, `pdf`, `html`, `xlsx`, `xls`, `docx`, `csv`, `eml`, `msg`, `pptx`, `ppt`, `xml`, `epub`
    - `enabled` (bool): Whether enabled
    - `number_limits` (int): Document quantity limit, default 3
    - `transfer_methods` (array[string]): Transfer method list, remote_url, local_file, must choose one
  - `image` (object): Image settings
    Currently only supports image types: `png`, `jpg`, `jpeg`, `webp`, `gif`
    - `enabled` (bool): Whether enabled
    - `number_limits` (int): Image quantity limit, default 3
    - `transfer_methods` (array[string]): Transfer method list, remote_url, local_file, must choose one
  - `audio` (object): Audio settings
    Currently only supports audio types: `mp3`, `m4a`, `wav`, `webm`, `amr`
    - `enabled` (bool): Whether enabled
    - `number_limits` (int): Audio quantity limit, default 3
    - `transfer_methods` (array[string]): Transfer method list, remote_url, local_file, must choose one
  - `video` (object): Video settings
    Currently only supports video types: `mp4`, `mov`, `mpeg`, `mpga`
    - `enabled` (bool): Whether enabled
    - `number_limits` (int): Video quantity limit, default 3
    - `transfer_methods` (array[string]): Transfer method list, remote_url, local_file, must choose one
  - `custom` (object): Custom settings
    - `enabled` (bool): Whether enabled
    - `number_limits` (int): Custom quantity limit, default 3
    - `transfer_methods` (array[string]): Transfer method list, remote_url, local_file, must choose one
- `system_parameters` (object): System parameters
  - `file_size_limit` (int): Document upload size limit (MB)
  - `image_file_size_limit` (int): Image file upload size limit (MB)
  - `audio_file_size_limit` (int): Audio file upload size limit (MB)
  - `video_file_size_limit` (int): Video file upload size limit (MB)

### 10. Get Application WebApp Settings

**GET** `/site`

Used to get application's WebApp settings.

#### Response
- `title` (string): WebApp name
- `icon_type` (string): Icon type, `emoji`-emoji, `image`-image
- `icon` (string): Icon, if `emoji` type, then emoji symbol, if `image` type, then image URL
- `icon_background` (string): Background color in hex format
- `icon_url` (string): Icon URL
- `description` (string): Description
- `copyright` (string): Copyright information
- `privacy_policy` (string): Privacy policy link
- `custom_disclaimer` (string): Custom disclaimer
- `default_language` (string): Default language
- `show_workflow_steps` (bool): Whether to show workflow details