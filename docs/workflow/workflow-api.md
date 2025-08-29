# Workflow Application APIs

This document covers all workflow application APIs based on the official Dify OpenAPI specification. Workflow applications offer non-session support and are ideal for translation, article writing, summarization AI, and more.

## Base URL

```
https://api.dify.ai/v1
```

## Authentication

Service API uses `API-Key` for authentication. **It is strongly recommended that developers store the `API-Key` in the backend rather than sharing or storing it on the client side to prevent `API-Key` leakage and financial loss.**

All API requests should include your `API-Key` in the **`Authorization`** HTTP Header:

```
Authorization: Bearer {API_KEY}
```

## API Overview

The Workflow API provides 8 main endpoints organized into 3 categories:

### Workflow Execution (4 APIs)
- Execute Workflow - Run a published workflow
- Get Workflow Run Detail - Retrieve execution results
- Stop Workflow Task Generation - Stop streaming execution
- Get Workflow Logs - Retrieve execution history

### Files (1 API)
- File Upload - Upload files for workflow use

### Application (3 APIs)
- Get Application Basic Information - App metadata
- Get Application Parameters Information - Input configuration
- Get Application WebApp Settings - UI settings

## APIs

### 1. Execute Workflow

**POST** `/workflows/run`

Executes a workflow. Cannot be executed without a published workflow.

#### Request Body
- `inputs` (object, required): Key/value pairs for workflow variables. Value for a file array type variable should be a list of InputFileObjectWorkflow.
  - For file list variables, each element should contain:
    - `type` (string): File type - `document`, `image`, `audio`, `video`, `custom`
    - `transfer_method` (string): Transfer method - `remote_url` or `local_file`
    - `url` (string): Image URL (when transfer_method is `remote_url`)
    - `upload_file_id` (string): Upload file ID (when transfer_method is `local_file`)
- `response_mode` (string, required): Response mode
  - `streaming`: Streaming mode (recommended). Based on SSE (Server-Sent Events)
  - `blocking`: Blocking mode, waits for execution to complete before returning results. *Due to Cloudflare limitations, requests will be interrupted after 100 seconds without response.*
- `user` (string, required): User identifier, used to define the identity of the end user. Must be unique within the application.

#### Example Requests

**Basic Execution:**
```json
{
  "inputs": {
    "query": "Summarize this text: ..."
  },
  "response_mode": "streaming",
  "user": "user_workflow_123"
}
```

**With File Array Variable:**
```json
{
  "inputs": {
    "my_documents": [
      {
        "type": "document",
        "transfer_method": "local_file",
        "upload_file_id": "uploaded_file_id_abc"
      },
      {
        "type": "image",
        "transfer_method": "remote_url",
        "url": "https://example.com/image.jpg"
      }
    ]
  },
  "response_mode": "blocking",
  "user": "user_workflow_456"
}
```

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

### 2. Get Workflow Run Detail

**GET** `/workflows/run/{workflow_run_id}`

Retrieve the current execution results of a workflow task based on the workflow execution ID.

#### Path Parameters
- `workflow_run_id` (string, required): Workflow Run ID, can be obtained from workflow execution response or streaming events (UUID format)

#### Response
- `id` (string): Workflow execution ID (UUID)
- `workflow_id` (string): Associated Workflow ID (UUID)
- `status` (string): Execution status `running` / `succeeded` / `failed` / `stopped`
- `inputs` (string): JSON string of input content
- `outputs` (object): JSON object of output content (nullable)
- `error` (string): Error reason (nullable)
- `total_steps` (int): Total task execution steps
- `total_tokens` (int): Total task execution tokens
- `created_at` (timestamp): Task start time (int64)
- `finished_at` (timestamp): Task end time (int64, nullable)
- `elapsed_time` (float): Time consumed in seconds (nullable)

#### Errors
- 404: Workflow run not found

### 3. Stop Workflow Task Generation

**POST** `/workflows/tasks/{task_id}/stop`

Stops a workflow task generation. Only supported in streaming mode.

#### Path Parameters
- `task_id` (string, required): Task ID from the streaming chunk (UUID format)

#### Request Body
- `user` (string, required): User identifier

#### Response
- `result` (string): Fixed return "success"

### 4. File Upload for Workflow

**POST** `/files/upload`

Upload a file for use in workflows. Supports any formats supported by your workflow. Uploaded files are for the current end-user only.

#### Request Body (multipart/form-data)
- `file` (binary, required): The file to be uploaded
- `user` (string, required): User identifier

#### Response

After successful upload, the server returns the file ID and related information.

- `id` (uuid): File ID
- `name` (string): File name
- `size` (int): File size (bytes)
- `extension` (string): File extension
- `mime_type` (string): File mime-type
- `created_by` (uuid): Uploader ID
- `created_at` (timestamp): Upload time (int64)

#### Errors
- 400: Bad Request for file operation
- 413: File is too large
- 415: Unsupported file type for upload
- 500: Internal server error
- 503: S3 storage error

### 5. Get Workflow Logs

**GET** `/workflows/logs`

Returns workflow logs, with the first page returning the latest `{limit}` messages, i.e., in reverse order.

#### Query Parameters
- `keyword` (string, optional): Keyword to search
- `status` (string, optional): Filter by status: `succeeded`, `failed`, `stopped`, `running`
- `page` (int, optional): Current page number, default 1
- `limit` (int, optional): Number of items per page, default 20

#### Response
- `page` (int): Current page number
- `limit` (int): Records per page
- `total` (int): Total records
- `has_more` (bool): Whether there is more data
- `data` (array[object]): Current page data
  - `id` (string): Identifier (UUID)
  - `workflow_run` (object): Workflow execution log
    - `id` (string): Identifier (UUID)
    - `version` (string): Version
    - `status` (string): Execution status, `running` / `succeeded` / `failed` / `stopped`
    - `error` (string, nullable): Error
    - `elapsed_time` (float): Time consumed, in seconds
    - `total_tokens` (int): Number of tokens consumed
    - `total_steps` (int): Execution step length
    - `created_at` (timestamp): Start time (int64)
    - `finished_at` (timestamp): End time (int64, nullable)
  - `created_from` (string): Source
  - `created_by_role` (string): Role
  - `created_by_account` (string, nullable): Account (UUID)
  - `created_by_end_user` (object): End user summary
    - `id` (string): Identifier (UUID)
    - `type` (string): Type
    - `is_anonymous` (bool): Whether anonymous
    - `session_id` (string): Session identifier
  - `created_at` (timestamp): Creation time (int64)

### 6. Get Application Basic Information

**GET** `/info`

Get basic information of the application.

#### Response
- `name` (string): Application name
- `description` (string): Application description
- `tags` (array[string]): Application tags

### 7. Get Application Parameters Information

**GET** `/parameters`

Get application parameters information including input configuration and file upload settings.

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
  - `image` (object): Image settings
    - `enabled` (bool): Whether enabled
    - `number_limits` (int): Image quantity limit
    - `detail` (string): Detail level
    - `transfer_methods` (array[string]): Transfer method list (`remote_url`, `local_file`)
- `system_parameters` (object): System parameters
  - `file_size_limit` (int): Document upload size limit (MB)
  - `image_file_size_limit` (int): Image file upload size limit (MB)
  - `audio_file_size_limit` (int): Audio file upload size limit (MB)
  - `video_file_size_limit` (int): Video file upload size limit (MB)

### 8. Get Application WebApp Settings

**GET** `/site`

Get application's WebApp settings.

#### Response
- `title` (string): WebApp name
- `icon_type` (string): Icon type, `emoji` or `image`
- `icon` (string): Icon, if `emoji` type, then emoji symbol, if `image` type, then image URL
- `icon_background` (string): Background color in hex format
- `icon_url` (string): Icon URL (nullable)
- `description` (string): Description
- `copyright` (string): Copyright information
- `privacy_policy` (string): Privacy policy link
- `custom_disclaimer` (string): Custom disclaimer
- `default_language` (string): Default language
- `show_workflow_steps` (bool): Whether to show workflow steps