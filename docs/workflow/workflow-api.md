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
- **POST** `/workflows/run` - Execute Workflow
- **GET** `/workflows/run/{workflow_run_id}` - Get Workflow Run Detail
- **POST** `/workflows/tasks/{task_id}/stop` - Stop Workflow Task Generation
- **GET** `/workflows/logs` - Get Workflow Logs

### Files (1 API)
- **POST** `/files/upload` - File Upload for Workflow

### Application (3 APIs)
- **GET** `/info` - Get Application Basic Information
- **GET** `/parameters` - Get Application Parameters Information
- **GET** `/site` - Get Application WebApp Settings

## APIs

### 1. Execute Workflow

**POST** `/workflows/run`

Executes a workflow. Cannot be executed without a published workflow.

#### Request Body (application/json)
```json
{
  "inputs": {
    "type": "object",
    "required": true,
    "description": "Key/value pairs for workflow variables. Value for a file array type variable should be a list of InputFileObjectWorkflow.",
    "additionalProperties": {
      "oneOf": [
        {"type": "string"},
        {"type": "number"},
        {"type": "boolean"},
        {"type": "object"},
        {
          "type": "array",
          "items": {"$ref": "#/InputFileObjectWorkflow"}
        }
      ]
    }
  },
  "response_mode": {
    "type": "string",
    "required": true,
    "enum": ["streaming", "blocking"],
    "description": "Response mode. Cloudflare timeout is 100s for blocking."
  },
  "user": {
    "type": "string",
    "required": true,
    "description": "User identifier, used to define the identity of the end user. Must be unique within the application."
  }
}
```

##### InputFileObjectWorkflow
```json
{
  "type": {
    "type": "string",
    "required": true,
    "enum": ["document", "image", "audio", "video", "custom"],
    "description": "File type"
  },
  "transfer_method": {
    "type": "string",
    "required": true,
    "enum": ["remote_url", "local_file"],
    "description": "Transfer method"
  },
  "url": {
    "type": "string",
    "format": "url",
    "description": "Image URL (required when transfer_method is remote_url)"
  },
  "upload_file_id": {
    "type": "string",
    "description": "Upload file ID (required when transfer_method is local_file)"
  }
}
```

**Validation Rules**:
- When `transfer_method` is `remote_url`: `url` is required, `upload_file_id` must not be present
- When `transfer_method` is `local_file`: `upload_file_id` is required, `url` must not be present

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

**Success (200)**
- **Content-Type**: Depends on `response_mode`
  - `blocking`: `application/json` with `WorkflowCompletionResponse`
  - `streaming`: `text/event-stream` with `ChunkWorkflowEvent` stream

**Error Responses**
- **400**: Bad Request for workflow operation
  - **Error codes**: `invalid_param`, `app_unavailable`, `provider_not_initialize`, `provider_quota_exceeded`, `model_currently_not_support`, `workflow_request_error`
- **500**: Internal server error

##### WorkflowCompletionResponse (Blocking Mode)

Returns complete workflow result, `Content-Type` is `application/json`.

```json
{
  "workflow_run_id": "string (uuid)",
  "task_id": "string (uuid)",
  "data": {
    "id": "string (uuid)",
    "workflow_id": "string (uuid)",
    "status": "string",
    "outputs": "object (nullable)",
    "error": "string (nullable)",
    "elapsed_time": "number (float, nullable)",
    "total_tokens": "integer (nullable)",
    "total_steps": "integer (default: 0)",
    "created_at": "integer (int64)",
    "finished_at": "integer (int64)"
  }
}
```

**Status Enum Values**: `running`, `succeeded`, `failed`, `stopped`

##### ChunkWorkflowEvent (Streaming Mode)

Returns workflow output streaming blocks, `Content-Type` is `text/event-stream`.
Each streaming block starts with `data:` and blocks are separated by `\n\n` (two newlines):

```
data: {"event": "text_chunk", "workflow_run_id": "b85e5fc5-751b-454d-b14e-dc5f240b0a31", "task_id": "bd029338-b068-4d34-a331-fc85478922c2", "data": {"text": "为了", "from_variable_selector": ["1745912968134", "text"]}}\n\n
```

**Event Types**: `workflow_started`, `node_started`, `text_chunk`, `node_finished`, `workflow_finished`, `tts_message`, `tts_message_end`, `ping`

Streaming blocks have different structures based on different `event` types:

##### workflow_started Event
```json
{
  "event": "workflow_started",
  "task_id": "string (uuid)",
  "workflow_run_id": "string (uuid)",
  "data": {
    "id": "string (uuid)",
    "workflow_id": "string (uuid)",
    "sequence_number": "integer",
    "created_at": "integer (int64)"
  }
}
```

##### node_started Event
```json
{
  "event": "node_started",
  "task_id": "string (uuid)",
  "workflow_run_id": "string (uuid)",
  "data": {
    "id": "string (uuid)",
    "node_id": "string (uuid)",
    "node_type": "string",
    "title": "string",
    "index": "integer",
    "predecessor_node_id": "string (uuid, nullable)",
    "inputs": "object",
    "created_at": "integer (int64)"
  }
}
```

##### text_chunk Event
```json
{
  "event": "text_chunk",
  "task_id": "string (uuid)",
  "workflow_run_id": "string (uuid)",
  "data": {
    "text": "string",
    "from_variable_selector": ["string"]
  }
}
```

##### node_finished Event
```json
{
  "event": "node_finished",
  "task_id": "string (uuid)",
  "workflow_run_id": "string (uuid)",
  "data": {
    "id": "string (uuid)",
    "node_id": "string (uuid)",
    "node_type": "string",
    "title": "string",
    "index": "integer",
    "predecessor_node_id": "string (uuid, nullable)",
    "inputs": "object (nullable)",
    "process_data": "object (nullable)",
    "outputs": "object (nullable)",
    "status": "string",
    "error": "string (nullable)",
    "elapsed_time": "number (float, nullable)",
    "execution_metadata": {
      "total_tokens": "integer (nullable)",
      "total_price": "number (float, nullable)",
      "currency": "string (nullable)"
    },
    "created_at": "integer (int64)"
  }
}
```

**Node Status Enum Values**: `running`, `succeeded`, `failed`, `stopped`

##### workflow_finished Event
```json
{
  "event": "workflow_finished",
  "task_id": "string (uuid)",
  "workflow_run_id": "string (uuid)",
  "data": {
    "id": "string (uuid)",
    "workflow_id": "string (uuid)",
    "status": "string",
    "outputs": "object (nullable)",
    "error": "string (nullable)",
    "elapsed_time": "number (float, nullable)",
    "total_tokens": "integer (nullable)",
    "total_steps": "integer",
    "created_at": "integer (int64)",
    "finished_at": "integer (int64)"
  }
}
```

**Workflow Status Enum Values**: `running`, `succeeded`, `failed`, `stopped`

##### tts_message Event
```json
{
  "event": "tts_message",
  "task_id": "string (uuid)",
  "workflow_run_id": "string (uuid)",
  "message_id": "string (uuid)",
  "audio": "string (base64)",
  "created_at": "integer (int64)"
}
```

##### tts_message_end Event
```json
{
  "event": "tts_message_end",
  "task_id": "string (uuid)",
  "workflow_run_id": "string (uuid)",
  "message_id": "string (uuid)",
  "audio": "string (empty)",
  "created_at": "integer (int64)"
}
```

##### ping Event
```json
{
  "event": "ping"
}
```

#### Error Codes
- **400 Bad Request**:
  - `invalid_param`: Invalid parameters
  - `app_unavailable`: App configuration unavailable
  - `provider_not_initialize`: No available model credential configuration
  - `provider_quota_exceeded`: Model call quota exceeded
  - `model_currently_not_support`: Current model unavailable
  - `workflow_request_error`: Workflow execution failed
- **500**: Internal server error

### 2. Get Workflow Run Detail

**GET** `/workflows/run/{workflow_run_id}`

Retrieve the current execution results of a workflow task based on the workflow execution ID.

#### Path Parameters
- `workflow_run_id` (string, required): Workflow Run ID, can be obtained from workflow execution response or streaming events (UUID format)

#### Response (200)
```json
{
  "id": "string (uuid)",
  "workflow_id": "string (uuid)",
  "status": "string",
  "inputs": "string (JSON string of input content)",
  "outputs": "object (nullable, JSON object of output content)",
  "error": "string (nullable)",
  "total_steps": "integer",
  "total_tokens": "integer",
  "created_at": "integer (int64)",
  "finished_at": "integer (int64, nullable)",
  "elapsed_time": "number (float, nullable)"
}
```

**Status Enum Values**: `running`, `succeeded`, `failed`, `stopped`

#### Error Responses
- **404**: Workflow run not found

### 3. Stop Workflow Task Generation

**POST** `/workflows/tasks/{task_id}/stop`

Stops a workflow task generation. Only supported in streaming mode.

#### Path Parameters
- `task_id` (string, required): Task ID from the streaming chunk (UUID format)

#### Request Body (application/json)
```json
{
  "user": "string"
}
```

#### Response (200)
```json
{
  "result": "success"
}
```

### 4. File Upload for Workflow

**POST** `/files/upload`

Upload a file for use in workflows. Supports any formats supported by your workflow. Uploaded files are for the current end-user only.

#### Request Body (multipart/form-data)
```json
{
  "file": {
    "type": "string",
    "format": "binary",
    "required": true,
    "description": "The file to be uploaded"
  },
  "user": {
    "type": "string",
    "required": true,
    "description": "User identifier"
  }
}
```

#### Response

**Success (200/201)**
```json
{
  "id": "string (uuid)",
  "name": "string",
  "size": "integer",
  "extension": "string",
  "mime_type": "string",
  "created_by": "string (uuid)",
  "created_at": "integer (int64)"
}
```

#### Error Responses
- **400**: Bad Request for file operation
- **413**: File is too large
- **415**: Unsupported file type for upload
- **500**: Internal server error
- **503**: S3 storage error

### 5. Get Workflow Logs

**GET** `/workflows/logs`

Returns workflow logs, with the first page returning the latest `{limit}` messages, i.e., in reverse order.

#### Query Parameters
- `keyword` (string, optional): Keyword to search
- `status` (string, optional): Filter by status
  - **Enum values**: `succeeded`, `failed`, `stopped`, `running`
- `page` (integer, optional): Current page number (default: 1)
- `limit` (integer, optional): Number of items per page (default: 20)

#### Response (200)
```json
{
  "page": "integer",
  "limit": "integer",
  "total": "integer",
  "has_more": "boolean",
  "data": [
    {
      "id": "string (uuid)",
      "workflow_run": {
        "id": "string (uuid)",
        "version": "string",
        "status": "string",
        "error": "string (nullable)",
        "elapsed_time": "number (float)",
        "total_tokens": "integer",
        "total_steps": "integer",
        "created_at": "integer (int64)",
        "finished_at": "integer (int64, nullable)"
      },
      "created_from": "string",
      "created_by_role": "string",
      "created_by_account": "string (uuid, nullable)",
      "created_by_end_user": {
        "id": "string (uuid)",
        "type": "string",
        "is_anonymous": "boolean",
        "session_id": "string"
      },
      "created_at": "integer (int64)"
    }
  ]
}
```

**Workflow Run Status Enum Values**: `running`, `succeeded`, `failed`, `stopped`

### 6. Get Application Basic Information

**GET** `/info`

Get basic information of the application.

#### Response (200)
```json
{
  "name": "string",
  "description": "string",
  "tags": ["string"]
}
```

### 7. Get Application Parameters Information

**GET** `/parameters`

Get application parameters information including input configuration and file upload settings.

#### Response (200)
```json
{
  "user_input_form": [
    {
      "text-input": {
        "label": "string",
        "variable": "string",
        "required": "boolean",
        "default": "string (optional)"
      }
    },
    {
      "paragraph": {
        "label": "string",
        "variable": "string",
        "required": "boolean",
        "default": "string (optional)"
      }
    },
    {
      "select": {
        "label": "string",
        "variable": "string",
        "required": "boolean",
        "default": "string (optional)",
        "options": ["string"]
      }
    }
  ],
  "file_upload": {
    "image": {
      "enabled": "boolean",
      "number_limits": "integer",
      "detail": "string",
      "transfer_methods": ["string"]
    }
  },
  "system_parameters": {
    "file_size_limit": "integer",
    "image_file_size_limit": "integer",
    "audio_file_size_limit": "integer",
    "video_file_size_limit": "integer"
  }
}
```

**User Input Form Types**: `text-input`, `paragraph`, `select`
**Transfer Methods Enum Values**: `remote_url`, `local_file`

### 8. Get Application WebApp Settings

**GET** `/site`

Get application's WebApp settings.

#### Response (200)
```json
{
  "title": "string",
  "icon_type": "string",
  "icon": "string",
  "icon_background": "string",
  "icon_url": "string (url, nullable)",
  "description": "string",
  "copyright": "string",
  "privacy_policy": "string",
  "custom_disclaimer": "string",
  "default_language": "string",
  "show_workflow_steps": "boolean"
}
```

**Icon Type Enum Values**: `emoji`, `image`