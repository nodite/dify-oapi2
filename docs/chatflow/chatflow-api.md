# Chatflow APIs

This document covers all chatflow APIs based on the official Dify OpenAPI specification. Chatflow APIs provide advanced chat functionality with workflow events, file support, conversation management, and comprehensive application settings.

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

The Chatflow API provides 17 endpoints organized into 6 main categories:

**Total API Count**: 17 endpoints

### Chatflow (3 APIs)
- **POST** `/chat-messages` - Send Chat Message
- **POST** `/chat-messages/{task_id}/stop` - Stop Chat Message Generation
- **GET** `/messages/{message_id}/suggested` - Get Next Suggested Questions

### Files (1 API)
- **POST** `/files/upload` - File Upload

### Feedback (2 APIs)
- **POST** `/messages/{message_id}/feedbacks` - Message Feedback
- **GET** `/app/feedbacks` - Get Application Feedbacks

### Conversations (5 APIs)
- **GET** `/messages` - Get Conversation History Messages
- **GET** `/conversations` - Get Conversations List
- **DELETE** `/conversations/{conversation_id}` - Delete Conversation
- **POST** `/conversations/{conversation_id}/name` - Rename Conversation
- **GET** `/conversations/{conversation_id}/variables` - Get Conversation Variables

### TTS (2 APIs)
- **POST** `/audio-to-text` - Speech to Text
- **POST** `/text-to-audio` - Text to Audio

### Application (4 APIs)
- **GET** `/info` - Get Application Basic Information
- **GET** `/parameters` - Get Application Parameters Information
- **GET** `/meta` - Get Application Meta Information
- **GET** `/site` - Get Application WebApp Settings

### Annotations (6 APIs)
- **GET** `/apps/annotations` - Get Annotation List
- **POST** `/apps/annotations` - Create Annotation
- **PUT** `/apps/annotations/{annotation_id}` - Update Annotation
- **DELETE** `/apps/annotations/{annotation_id}` - Delete Annotation
- **POST** `/apps/annotation-reply/{action}` - Initial Annotation Reply Settings
- **GET** `/apps/annotation-reply/{action}/status/{job_id}` - Query Initial Annotation Reply Settings Task Status

## APIs

### Chatflow

#### 1. Send Chat Message

**POST** `/chat-messages`

Send a request to the advanced chat application, supporting various file types and workflow events.

#### Request Body (application/json)
```json
{
  "query": "string (required) - User input/question content",
  "inputs": "object (optional) - Key/value pairs for app variables, default: {}",
  "response_mode": "string (optional) - Response mode, default: streaming",
  "user": "string (required) - User identifier",
  "conversation_id": "string (optional) - Conversation ID to continue",
  "files": "array (optional) - List of files for Vision-capable models or general file input",
  "auto_generate_name": "boolean (optional) - Auto-generate conversation title, default: true"
}
```

**Response Mode Enum Values**: `"streaming"`, `"blocking"`

**File Object Schema**:
```json
{
  "type": "string (required) - File type",
  "transfer_method": "string (required) - Transfer method",
  "url": "string (conditional) - File URL (required when transfer_method is remote_url)",
  "upload_file_id": "string (conditional) - Uploaded file ID (required when transfer_method is local_file)"
}
```

**File Type Enum Values**: `"document"`, `"image"`, `"audio"`, `"video"`, `"custom"`
- `document`: TXT, MD, PDF, HTML, XLSX, DOCX, CSV, EML, MSG, PPTX, XML, EPUB
- `image`: JPG, PNG, GIF, WEBP, SVG
- `audio`: MP3, M4A, WAV, WEBM, AMR
- `video`: MP4, MOV, MPEG, MPGA

**Transfer Method Enum Values**: `"remote_url"`, `"local_file"`

#### Example Request
```json
{
  "inputs": {"user_name": "Alice"},
  "query": "Analyze this document and tell me its sentiment.",
  "response_mode": "streaming",
  "conversation_id": "conv_12345",
  "user": "user_alice",
  "files": [
    {
      "type": "document",
      "transfer_method": "remote_url",
      "url": "https://example.com/mydoc.pdf"
    }
  ],
  "auto_generate_name": true
}
```

#### Response

**Success (200)**

**Blocking Mode (application/json)**:
```json
{
  "event": "string",
  "task_id": "string (uuid)",
  "id": "string (uuid)",
  "message_id": "string (uuid)",
  "conversation_id": "string (uuid)",
  "mode": "string",
  "answer": "string",
  "metadata": {
    "usage": {
      "prompt_tokens": "integer",
      "prompt_unit_price": "string",
      "prompt_price_unit": "string",
      "prompt_price": "string",
      "completion_tokens": "integer",
      "completion_unit_price": "string",
      "completion_price_unit": "string",
      "completion_price": "string",
      "total_tokens": "integer",
      "total_price": "string",
      "currency": "string",
      "latency": "number"
    },
    "retriever_resources": [
      {
        "position": "integer",
        "dataset_id": "string (uuid)",
        "dataset_name": "string",
        "document_id": "string (uuid)",
        "document_name": "string",
        "segment_id": "string (uuid)",
        "score": "number",
        "content": "string"
      }
    ]
  },
  "created_at": "integer (timestamp)"
}
```

**Streaming Mode (text/event-stream)**:

Stream of Server-Sent Events with the following event types:

**Stream Event Enum Values**: `"message"`, `"message_file"`, `"message_end"`, `"tts_message"`, `"tts_message_end"`, `"message_replace"`, `"workflow_started"`, `"node_started"`, `"node_finished"`, `"workflow_finished"`, `"error"`, `"ping"`

**Message File Belongs To Enum Values** (for message_file events): `"assistant"`

- `message` - Chat message content chunk
- `message_file` - File attachment information
- `message_end` - End of message with metadata
- `tts_message` - Text-to-speech audio chunk (Base64 encoded)
- `tts_message_end` - End of TTS conversion
- `message_replace` - Replace message content
- `workflow_started` - Workflow execution started
- `node_started` - Workflow node started
- `node_finished` - Workflow node finished
- `workflow_finished` - Workflow execution finished
- `error` - Error occurred
- `ping` - Keep-alive ping

**Node Status Enum Values**: `"running"`, `"succeeded"`, `"failed"`, `"stopped"`
**Workflow Status Enum Values**: `"running"`, `"succeeded"`, `"failed"`, `"stopped"`

**Error Responses**
- **400**: Bad Request - Invalid parameters
- **404**: Conversation not found
- **500**: Internal server error

#### 2. Stop Chat Message Generation

**POST** `/chat-messages/{task_id}/stop`

Stops an advanced chat message generation task. Only supported in streaming mode.

#### Path Parameters
- `task_id` (string, required): Task ID from the streaming chunk

#### Request Body (application/json)
```json
{
  "user": "string (required) - User identifier, consistent with send message call"
}
```

#### Response

**Success (200)**
```json
{
  "result": "success"
}
```

#### 3. Get Next Suggested Questions

**GET** `/messages/{message_id}/suggested`

Get next questions suggestions for the current message.

#### Path Parameters
- `message_id` (string, required): Message ID

#### Query Parameters
- `user` (string, required): User identifier

#### Response

**Success (200)**
```json
{
  "result": "success",
  "data": ["string"]
}
```

### Files

#### 1. File Upload

**POST** `/files/upload`

Upload a file for use when sending messages, enabling multimodal understanding. Supports any formats supported by your application. Uploaded files are for use by the current end-user only.

#### Request Body (multipart/form-data)
- `file` (binary, required): The file to be uploaded
- `user` (string, required): User identifier

#### Response

**Success (200)**
```json
{
  "id": "string (uuid)",
  "name": "string",
  "size": "integer",
  "extension": "string",
  "mime_type": "string",
  "created_by": "string (uuid)",
  "created_at": "integer (timestamp)"
}
```

**Error Responses**
- **400**: Bad Request for file operation
- **413**: File is too large
- **415**: Unsupported file type
- **503**: S3 storage error
- **500**: Internal server error

### Feedback

#### 1. Message Feedback

**POST** `/messages/{message_id}/feedbacks`

Provide feedback for a message.

#### Path Parameters
- `message_id` (string, required): Message ID

#### Request Body (application/json)
```json
{
  "rating": "string (optional, nullable) - User rating",
  "user": "string (required) - User identifier",
  "content": "string (optional, nullable) - Feedback content/comment"
}
```

**Rating Enum Values**: `"like"`, `"dislike"`, `null`

#### Response

**Success (200)**
```json
{
  "result": "success"
}
```

#### 2. Get Application Feedbacks

**GET** `/app/feedbacks`

Get application's feedbacks.

#### Query Parameters
- `page` (integer, optional): Page number, default: 1
- `limit` (integer, optional): Number of items per page

#### Response

**Success (200)**
```json
{
  "data": [
    {
      "id": "string (uuid)",
      "app_id": "string (uuid)",
      "conversation_id": "string (uuid)",
      "message_id": "string (uuid)",
      "rating": "string (nullable)",
      "content": "string",
      "from_source": "string",
      "from_end_user_id": "string (uuid)",
      "from_account_id": "string (uuid, nullable)",
      "created_at": "string (datetime)",
      "updated_at": "string (datetime)"
    }
  ]
}
```

**Feedback Rating Enum Values**: `"like"`, `"dislike"`, `null`

### Conversations

#### 1. Get Conversation History Messages

**GET** `/messages`

Returns historical chat records in a scrolling load format.

#### Query Parameters
- `conversation_id` (string, required): Conversation ID
- `user` (string, required): User identifier
- `first_id` (string, optional): ID of the first chat record on the current page (for pagination)
- `limit` (integer, optional): Number of items per page, default: 20

#### Response

**Success (200)**
```json
{
  "limit": "integer",
  "has_more": "boolean",
  "data": [
    {
      "id": "string (uuid)",
      "conversation_id": "string (uuid)",
      "inputs": "object",
      "query": "string",
      "answer": "string",
      "message_files": [
        {
          "id": "string (uuid)",
          "type": "string",
          "url": "string (url)",
          "belongs_to": "string"
        }
      ],
      "feedback": {
        "rating": "string"
      },
      "retriever_resources": [
        {
          "position": "integer",
          "dataset_id": "string (uuid)",
          "dataset_name": "string",
          "document_id": "string (uuid)",
          "document_name": "string",
          "segment_id": "string (uuid)",
          "score": "number",
          "content": "string"
        }
      ],
      "created_at": "integer (timestamp)"
    }
  ]
}
```

**Message File Belongs To Enum Values**: `"user"`, `"assistant"`
**Message Feedback Rating Enum Values**: `"like"`, `"dislike"`

#### 2. Get Conversations List

**GET** `/conversations`

Retrieve the conversation list for the current user.

#### Query Parameters
- `user` (string, required): User identifier
- `last_id` (string, optional): ID of the last record for pagination
- `limit` (integer, optional): Number of items per page, default: 20, min: 1, max: 100
- `sort_by` (string, optional): Sorting field, default: "-updated_at"

**Sort By Enum Values**: `"created_at"`, `"-created_at"`, `"updated_at"`, `"-updated_at"`

#### Response

**Success (200)**
```json
{
  "limit": "integer",
  "has_more": "boolean",
  "data": [
    {
      "id": "string (uuid)",
      "name": "string",
      "inputs": "object",
      "status": "string",
      "introduction": "string (nullable)",
      "created_at": "integer (timestamp)",
      "updated_at": "integer (timestamp)"
    }
  ]
}
```

#### 3. Delete Conversation

**DELETE** `/conversations/{conversation_id}`

Delete a conversation.

#### Path Parameters
- `conversation_id` (string, required): Conversation ID

#### Request Body (application/json)
```json
{
  "user": "string (required) - The user identifier"
}
```

#### Response

**Success (204)**
No Content - Conversation deleted successfully.

#### 4. Rename Conversation

**POST** `/conversations/{conversation_id}/name`

Rename the session.

#### Path Parameters
- `conversation_id` (string, required): Conversation ID

#### Request Body (application/json)
```json
{
  "name": "string (optional, nullable) - New conversation name",
  "auto_generate": "boolean (optional) - Auto-generate name, default: false",
  "user": "string (required) - User identifier"
}
```

#### Response

**Success (200)**
```json
{
  "id": "string (uuid)",
  "name": "string",
  "inputs": "object",
  "status": "string",
  "introduction": "string (nullable)",
  "created_at": "integer (timestamp)",
  "updated_at": "integer (timestamp)"
}
```

#### 5. Get Conversation Variables

**GET** `/conversations/{conversation_id}/variables`

Retrieve variables from a specific conversation.

#### Path Parameters
- `conversation_id` (string, required): Conversation ID

#### Query Parameters
- `user` (string, required): User identifier
- `last_id` (string, optional): ID of the last record for pagination
- `limit` (integer, optional): Number of items per page, default: 20, min: 1, max: 100
- `variable_name` (string, optional): Filter by variable name

#### Response

**Success (200)**
```json
{
  "limit": "integer",
  "has_more": "boolean",
  "data": [
    {
      "id": "string (uuid)",
      "name": "string",
      "value_type": "string",
      "value": "string",
      "description": "string (nullable)",
      "created_at": "integer (timestamp)",
      "updated_at": "integer (timestamp)"
    }
  ]
}
```

**Error Responses**
- **404**: Conversation not found

### TTS (Text-to-Speech)

#### 1. Speech to Text

**POST** `/audio-to-text`

Convert audio file to text. File size limit: 15MB.

#### Request Body (multipart/form-data)
- `file` (binary, required): Audio file, max 15MB
- `user` (string, required): User identifier

**Supported Audio Formats**: mp3, mp4, mpeg, mpga, m4a, wav, webm

#### Response

**Success (200)**
```json
{
  "text": "string"
}
```

#### 2. Text to Audio

**POST** `/text-to-audio`

Convert text to speech.

#### Request Body (application/json)
```json
{
  "message_id": "string (optional) - Message ID (priority)",
  "text": "string (optional) - Speech content",
  "user": "string (required) - User identifier",
  "streaming": "boolean (optional) - Stream audio chunks, default: false"
}
```

**Note**: Requires `user`. Provide `message_id` or `text`.

#### Response

**Success (200)**
- **Content-Type**: `audio/wav` or `audio/mp3`
- **Body**: Binary audio data
- **Headers**: 
  - `Content-Type`: Audio format (e.g., "audio/wav")

### Application

#### 1. Get Application Basic Information

**GET** `/info`

Get basic application information.

#### Response

**Success (200)**
```json
{
  "name": "string",
  "description": "string",
  "tags": ["string"]
}
```

#### 2. Get Application Parameters Information

**GET** `/parameters`

Get application parameters.

#### Response

**Success (200)**
```json
{
  "opening_statement": "string",
  "suggested_questions": ["string"],
  "suggested_questions_after_answer": {
    "enabled": "boolean"
  },
  "speech_to_text": {
    "enabled": "boolean"
  },
  "text_to_speech": {
    "enabled": "boolean",
    "voice": "string",
    "language": "string",
    "autoPlay": "string"
  },
  "retriever_resource": {
    "enabled": "boolean"
  },
  "annotation_reply": {
    "enabled": "boolean"
  },
  "user_input_form": [
    {
      "text-input": {
        "label": "string",
        "variable": "string",
        "required": "boolean",
        "default": "string"
      }
    },
    {
      "paragraph": {
        "label": "string",
        "variable": "string",
        "required": "boolean",
        "default": "string"
      }
    },
    {
      "select": {
        "label": "string",
        "variable": "string",
        "required": "boolean",
        "default": "string",
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

**AutoPlay Enum Values**: `"enabled"`, `"disabled"`
**Transfer Methods Enum Values**: `"remote_url"`, `"local_file"`

#### 3. Get Application Meta Information

**GET** `/meta`

Get application meta information (tool icons).

#### Response

**Success (200)**
```json
{
  "tool_icons": {
    "additionalProperties": {
      "oneOf": [
        {
          "type": "string",
          "format": "url"
        },
        {
          "background": "string",
          "content": "string"
        }
      ]
    }
  }
}
```

#### 4. Get Application WebApp Settings

**GET** `/site`

Get WebApp settings.

#### Response

**Success (200)**
```json
{
  "title": "string",
  "chat_color_theme": "string",
  "chat_color_theme_inverted": "boolean",
  "icon_type": "string",
  "icon": "string",
  "icon_background": "string",
  "icon_url": "string (url, nullable)",
  "description": "string",
  "copyright": "string",
  "privacy_policy": "string",
  "custom_disclaimer": "string",
  "default_language": "string",
  "show_workflow_steps": "boolean",
  "use_icon_as_answer_icon": "boolean"
}
```

**Icon Type Enum Values**: `"emoji"`, `"image"`

### Annotations

#### 1. Get Annotation List

**GET** `/apps/annotations`

Get annotation list.

#### Query Parameters
- `page` (integer, optional): Page number, default: 1
- `limit` (integer, optional): Number of items per page, default: 20, min: 1, max: 100

#### Response

**Success (200)**
```json
{
  "data": [
    {
      "id": "string (uuid)",
      "question": "string",
      "answer": "string",
      "hit_count": "integer",
      "created_at": "integer (timestamp)"
    }
  ],
  "has_more": "boolean",
  "limit": "integer",
  "total": "integer",
  "page": "integer"
}
```

#### 2. Create Annotation

**POST** `/apps/annotations`

Create annotation.

#### Request Body (application/json)
```json
{
  "question": "string (required) - Annotation question",
  "answer": "string (required) - Annotation answer"
}
```

#### Response

**Success (200/201)**
```json
{
  "id": "string (uuid)",
  "question": "string",
  "answer": "string",
  "hit_count": "integer",
  "created_at": "integer (timestamp)"
}
```

#### 3. Update Annotation

**PUT** `/apps/annotations/{annotation_id}`

Update annotation.

#### Path Parameters
- `annotation_id` (string, required): Annotation ID (UUID)

#### Request Body (application/json)
```json
{
  "question": "string (required) - Updated annotation question",
  "answer": "string (required) - Updated annotation answer"
}
```

#### Response

**Success (200)**
```json
{
  "id": "string (uuid)",
  "question": "string",
  "answer": "string",
  "hit_count": "integer",
  "created_at": "integer (timestamp)"
}
```

#### 4. Delete Annotation

**DELETE** `/apps/annotations/{annotation_id}`

Delete annotation.

#### Path Parameters
- `annotation_id` (string, required): Annotation ID (UUID)

#### Response

**Success (204)**
No Content - Annotation deleted successfully.

#### 5. Initial Annotation Reply Settings

**POST** `/apps/annotation-reply/{action}`

Initial annotation reply settings.

#### Path Parameters
- `action` (string, required): Action to perform

**Action Enum Values**: `"enable"`, `"disable"`

#### Request Body (application/json)
```json
{
  "embedding_provider_name": "string (optional, nullable) - Embedding provider name",
  "embedding_model_name": "string (optional, nullable) - Embedding model name",
  "score_threshold": "number (required) - Score threshold for matching"
}
```

#### Response

**Success (200/202)**
```json
{
  "job_id": "string (uuid)",
  "job_status": "string"
}
```

#### 6. Query Initial Annotation Reply Settings Task Status

**GET** `/apps/annotation-reply/{action}/status/{job_id}`

Query initial annotation reply settings task status.

#### Path Parameters
- `action` (string, required): Action to perform
- `job_id` (string, required): Job ID (UUID)

**Action Enum Values**: `"enable"`, `"disable"`

#### Response

**Success (200)**
```json
{
  "job_id": "string (uuid)",
  "job_status": "string",
  "error_msg": "string (nullable)"
}
```

## Error Responses

All APIs may return the following error responses:

```json
{
  "status": "integer (nullable)",
  "code": "string (nullable)",
  "message": "string"
}
```

**Common HTTP Status Codes**:
- **200**: OK - Request successful
- **201**: Created - Resource created successfully
- **202**: Accepted - Request accepted for processing
- **204**: No Content - Request successful, no content returned
- **400**: Bad Request - Invalid parameters
- **401**: Unauthorized - Invalid API key
- **403**: Forbidden - Insufficient permissions
- **404**: Resource not found
- **413**: Payload too large
- **415**: Unsupported media type
- **500**: Internal server error
- **503**: Service unavailable

## Streaming Events

When using streaming mode (`response_mode: "streaming"`), the API returns Server-Sent Events with the following event types:

### Message Events
- **message**: Chat message content chunk
- **message_file**: File attachment information
- **message_end**: End of message with metadata
- **message_replace**: Replace previous message content

### TTS Events
- **tts_message**: Text-to-speech audio chunk (Base64 encoded)
- **tts_message_end**: End of TTS conversion

### Workflow Events
- **workflow_started**: Workflow execution started
- **node_started**: Workflow node execution started
- **node_finished**: Workflow node execution finished
- **workflow_finished**: Workflow execution completed

### System Events
- **error**: Error occurred during processing
- **ping**: Keep-alive ping

Each event includes relevant metadata such as `task_id`, `message_id`, `conversation_id`, and `created_at` timestamp.

## Summary

**Total APIs**: 17 endpoints across 6 categories:
- **Chatflow**: 3 APIs
- **Files**: 1 API
- **Feedback**: 2 APIs
- **Conversations**: 5 APIs
- **TTS**: 2 APIs
- **Application**: 4 APIs
- **Annotations**: 6 APIs

All APIs follow RESTful conventions with proper HTTP methods, consistent request/response formats, and comprehensive error handling.