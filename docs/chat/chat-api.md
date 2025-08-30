# Chat APIs

This document covers all chat APIs based on the official Dify OpenAPI specification. Chat APIs provide comprehensive conversation management, message processing, file handling, and application configuration capabilities for AI-powered chat applications.

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

**Note**: The Service API does not share conversations created by the WebApp. Conversations created through the API are isolated from those created in the WebApp interface.

## API Overview

The Chat API provides 22 endpoints organized into 7 main categories:

### Chat Messages (3 APIs)
- **POST** `/chat-messages` - Send Chat Message
- **POST** `/chat-messages/{task_id}/stop` - Stop Chat Message Generation
- **GET** `/messages/{message_id}/suggested` - Get Next Suggested Questions

### File Management (1 API)
- **POST** `/files/upload` - Upload File

### Feedback Management (2 APIs)
- **POST** `/messages/{message_id}/feedbacks` - Submit Message Feedback
- **GET** `/app/feedbacks` - Get Application Feedbacks

### Conversation Management (5 APIs)
- **GET** `/messages` - Get Conversation History Messages
- **GET** `/conversations` - Get Conversations List
- **DELETE** `/conversations/{conversation_id}` - Delete Conversation
- **POST** `/conversations/{conversation_id}/name` - Rename Conversation
- **GET** `/conversations/{conversation_id}/variables` - Get Conversation Variables

### Text-to-Speech & Speech-to-Text (2 APIs)
- **POST** `/audio-to-text` - Convert Speech to Text
- **POST** `/text-to-audio` - Convert Text to Audio

### Application Information (4 APIs)
- **GET** `/info` - Get Application Basic Information
- **GET** `/parameters` - Get Application Parameters
- **GET** `/meta` - Get Application Meta Information
- **GET** `/site` - Get WebApp Settings

### Annotation Management (6 APIs)
- **GET** `/apps/annotations` - Get Annotation List
- **POST** `/apps/annotations` - Create Annotation
- **PUT** `/apps/annotations/{annotation_id}` - Update Annotation
- **DELETE** `/apps/annotations/{annotation_id}` - Delete Annotation
- **POST** `/apps/annotation-reply/{action}` - Configure Annotation Reply Settings
- **GET** `/apps/annotation-reply/{action}/status/{job_id}` - Get Annotation Reply Settings Status

## APIs

### Chat Messages

#### 1. Send Chat Message

**POST** `/chat-messages`

Sends a message to the chat application and receives a response. Supports both blocking and streaming modes.

#### Request Body (application/json)
```json
{
  "query": {
    "type": "string",
    "required": true,
    "description": "User Input/Question content."
  },
  "inputs": {
    "type": "object",
    "description": "Allows the entry of various variable values defined by the App. Contains key/value pairs.",
    "additionalProperties": true,
    "default": {}
  },
  "response_mode": {
    "type": "string",
    "enum": ["streaming", "blocking"],
    "description": "Mode of response return. 'streaming' (recommended) uses SSE. 'blocking' returns after completion (may be interrupted for long processes; not supported in Agent Assistant mode). Cloudflare timeout is 100s.",
    "default": "streaming"
  },
  "user": {
    "type": "string",
    "required": true,
    "description": "User identifier, unique within the application. Note: The Service API does not share conversations created by the WebApp. Conversations created through the API are isolated from those created in the WebApp interface."
  },
  "conversation_id": {
    "type": "string",
    "description": "Conversation ID to continue a conversation. Pass the previous message's conversation_id."
  },
  "files": {
    "type": "array",
    "description": "File list (images) for Vision-capable models.",
    "items": {
      "$ref": "#/components/schemas/InputFileObject"
    }
  },
  "auto_generate_name": {
    "type": "boolean",
    "description": "Auto-generate conversation title. Default true. If false, use conversation rename API with auto_generate: true for async title generation.",
    "default": true
  }
}
```

#### InputFileObject Schema
```json
{
  "type": "object",
  "required": ["type", "transfer_method"],
  "properties": {
    "type": {
      "type": "string",
      "enum": ["image"],
      "description": "Supported type: image."
    },
    "transfer_method": {
      "type": "string",
      "enum": ["remote_url", "local_file"],
      "description": "Transfer method, remote_url for image URL / local_file for file upload"
    },
    "url": {
      "type": "string",
      "format": "url",
      "description": "Image URL (when the transfer method is remote_url)"
    },
    "upload_file_id": {
      "type": "string",
      "description": "Uploaded file ID, which must be obtained by uploading through the File Upload API in advance (when the transfer method is local_file)"
    }
  },
  "anyOf": [
    {
      "properties": { 
        "transfer_method": { "enum": ["remote_url"] },
        "url": { "type": "string", "format": "url" }
      },
      "required": ["url"],
      "not": { "required": ["upload_file_id"] }
    },
    {
      "properties": { 
        "transfer_method": { "enum": ["local_file"] },
        "upload_file_id": { "type": "string" }
      },
      "required": ["upload_file_id"],
      "not": { "required": ["url"] }
    }
  ]
}
```

#### Example Request
```json
{
  "inputs": {},
  "query": "What can you help me with?",
  "response_mode": "blocking",
  "user": "user-123",
  "auto_generate_name": true
}
```

#### Response

**Success (200) - Blocking Mode**
```json
{
  "event": {
    "type": "string",
    "description": "Event type, fixed as 'message'.",
    "example": "message"
  },
  "task_id": {
    "type": "string",
    "format": "uuid",
    "description": "Task ID for request tracking and stop response API."
  },
  "id": {
    "type": "string",
    "format": "uuid",
    "description": "Unique ID of this response/message event."
  },
  "message_id": {
    "type": "string",
    "format": "uuid",
    "description": "Unique message ID."
  },
  "conversation_id": {
    "type": "string",
    "format": "uuid",
    "description": "Conversation ID."
  },
  "mode": {
    "type": "string",
    "description": "App mode, fixed as 'chat'.",
    "example": "chat"
  },
  "answer": {
    "type": "string",
    "description": "Complete response content."
  },
  "metadata": {
    "type": "object",
    "properties": {
      "usage": { "$ref": "#/components/schemas/Usage" },
      "retriever_resources": {
        "type": "array",
        "items": { "$ref": "#/components/schemas/RetrieverResource" }
      }
    }
  },
  "created_at": {
    "type": "integer",
    "format": "int64",
    "description": "Message creation timestamp (Unix epoch seconds)."
  }
}
```

**Success (200) - Streaming Mode**
```
Content-Type: text/event-stream

data: {"event": "message", "task_id": "task123", "message_id": "msg123", "conversation_id": "conv123", "answer": "Hello", "created_at": 1679586595}

data: {"event": "message_end", "task_id": "task123", "message_id": "msg123", "conversation_id": "conv123", "metadata": {"usage": {"total_tokens": 10, "latency": 1.0}}}
```

#### Streaming Event Types

**Base Event Schema**
```json
{
  "event": {
    "type": "string",
    "enum": ["message", "agent_message", "tts_message", "tts_message_end", "agent_thought", "message_file", "message_end", "message_replace", "error", "ping"]
  },
  "task_id": { "type": "string", "format": "uuid" },
  "message_id": { "type": "string", "format": "uuid" },
  "conversation_id": { "type": "string", "format": "uuid" },
  "created_at": { "type": "integer", "format": "int64" }
}
```

**Event Types:**
- **`message`** - LLM returned text chunk
  ```json
  { "answer": "string" }
  ```
- **`agent_message`** - LLM returned text chunk (Agent mode)
  ```json
  { "answer": "string" }
  ```
- **`tts_message`** - TTS audio stream event (base64 encoded Mp3)
  ```json
  { "audio": "string (base64)" }
  ```
- **`tts_message_end`** - TTS audio stream end event
  ```json
  { "audio": "" }
  ```
- **`agent_thought`** - Agent thought, LLM thinking, tool call details
  ```json
  {
    "id": "string (uuid)",
    "position": "integer",
    "thought": "string",
    "observation": "string",
    "tool": "string",
    "tool_input": "string (JSON)",
    "message_files": ["string (uuid)"]
  }
  ```
- **`message_file`** - New file created by a tool
  ```json
  {
    "id": "string (uuid)",
    "type": "string (enum: image)",
    "belongs_to": "string (enum: assistant)",
    "url": "string (url)"
  }
  ```
- **`message_end`** - Message completion with metadata
  ```json
  {
    "metadata": {
      "usage": { "$ref": "#/components/schemas/Usage" },
      "retriever_resources": [{ "$ref": "#/components/schemas/RetrieverResource" }]
    }
  }
  ```
- **`message_replace`** - Message content replacement (e.g., content moderation)
  ```json
  { "answer": "string" }
  ```
- **`error`** - Error during streaming
  ```json
  {
    "status": "integer",
    "code": "string",
    "message": "string"
  }
  ```
- **`ping`** - Keep-alive ping (no additional properties)

**Error Responses**
- **400**: Bad Request - Invalid parameters, app unavailable, provider issues
- **404**: Conversation does not exist
- **500**: Internal server error

#### 2. Stop Chat Message Generation

**POST** `/chat-messages/{task_id}/stop`

Stops a chat message generation task. Only supported in streaming mode.

#### Path Parameters
- `task_id` (string, required): Task ID from streaming response

#### Request Body (application/json)
```json
{
  "user": {
    "type": "string",
    "required": true,
    "description": "User identifier, must be consistent with the user passed in the send message interface."
  }
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
  "data": [
    "string",
    "string",
    "string"
  ]
}
```

### File Management

#### 1. Upload File

**POST** `/files/upload`

Upload a file (currently only images are supported) for use when sending messages, enabling multimodal understanding of images and text.

#### Request Body (multipart/form-data)
```json
{
  "file": {
    "type": "string",
    "format": "binary",
    "required": true,
    "description": "The file to be uploaded. Supported image types: png, jpg, jpeg, webp, gif."
  },
  "user": {
    "type": "string",
    "required": true,
    "description": "User identifier, defined by the developer's rules, must be unique within the application."
  }
}
```

#### Response

**Success (200)**
```json
{
  "id": {
    "type": "string",
    "format": "uuid",
    "description": "Unique file identifier"
  },
  "name": {
    "type": "string",
    "description": "Original filename"
  },
  "size": {
    "type": "integer",
    "description": "File size in bytes"
  },
  "extension": {
    "type": "string",
    "description": "File extension"
  },
  "mime_type": {
    "type": "string",
    "description": "MIME type of the file"
  },
  "created_by": {
    "type": "string",
    "format": "uuid",
    "description": "User ID who uploaded the file"
  },
  "created_at": {
    "type": "integer",
    "format": "int64",
    "description": "Upload timestamp (Unix epoch seconds)"
  }
}
```

**Error Responses**
- **400**: Bad Request - Invalid file parameters
- **413**: File Too Large
- **415**: Unsupported File Type
- **503**: S3 Storage Error
- **500**: Internal Server Error

### Feedback Management

#### 1. Submit Message Feedback

**POST** `/messages/{message_id}/feedbacks`

End-users can provide feedback messages, facilitating application developers to optimize expected outputs.

#### Path Parameters
- `message_id` (string, required): Message ID for which feedback is being provided

#### Request Body (application/json)
```json
{
  "rating": {
    "type": "string",
    "enum": ["like", "dislike", null],
    "nullable": true,
    "description": "User rating for the message."
  },
  "user": {
    "type": "string",
    "required": true,
    "description": "User identifier."
  },
  "content": {
    "type": "string",
    "description": "Feedback content/comment."
  }
}
```

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
- `page` (integer, optional): Pagination page number. Default: 1
- `limit` (integer, optional): Records per page. Default: 20

#### Response

**Success (200)**
```json
{
  "data": {
    "type": "array",
    "items": {
      "type": "object",
      "properties": {
        "id": { "type": "string", "format": "uuid" },
        "app_id": { "type": "string", "format": "uuid" },
        "conversation_id": { "type": "string", "format": "uuid" },
        "message_id": { "type": "string", "format": "uuid" },
        "rating": { "type": "string", "enum": ["like", "dislike", null], "nullable": true },
        "content": { "type": "string" },
        "from_source": { "type": "string" },
        "from_end_user_id": { "type": "string", "format": "uuid" },
        "from_account_id": { "type": "string", "format": "uuid", "nullable": true },
        "created_at": { "type": "string", "format": "date-time" },
        "updated_at": { "type": "string", "format": "date-time" }
      }
    }
  }
}
```

### Conversation Management

#### 1. Get Conversation History Messages

**GET** `/messages`

Returns historical chat records in a scrolling load format, with the first page returning the latest messages in reverse order.

#### Query Parameters
- `conversation_id` (string, required): Conversation ID
- `user` (string, required): User identifier
- `first_id` (string, optional): The ID of the first chat record on the current page, default is null
- `limit` (integer, optional): How many chat history messages to return, default is 20

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
          "belongs_to": {
            "type": "string",
            "enum": ["user", "assistant"]
          }
        }
      ],
      "feedback": {
        "rating": {
          "type": "string",
          "enum": ["like", "dislike"]
        }
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
      "agent_thoughts": [
        {
          "id": "string (uuid)",
          "message_id": "string (uuid)",
          "position": "integer",
          "thought": "string",
          "tool": "string",
          "tool_input": "string",
          "observation": "string",
          "files": ["string (uuid)"],
          "created_at": "integer (timestamp)"
        }
      ],
      "created_at": "integer (timestamp)"
    }
  ]
}
```

#### 2. Get Conversations List

**GET** `/conversations`

Retrieve the conversation list for the current user, defaulting to the most recent 20 entries.

#### Query Parameters
- `user` (string, required): User identifier
- `last_id` (string, optional): The ID of the last record on the current page (for pagination)
- `limit` (integer, optional): How many records to return. Default 20, Min 1, Max 100
- `sort_by` (string, optional): Sorting field. Default: -updated_at
  - Enum: `["created_at", "-created_at", "updated_at", "-updated_at"]`

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
      "introduction": "string",
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
  "user": {
    "type": "string",
    "required": true,
    "description": "The user identifier."
  }
}
```

#### Response

**Success (204)**
No Content - Conversation deleted successfully.

#### 4. Rename Conversation

**POST** `/conversations/{conversation_id}/name`

Rename the session. The session name is used for display on clients that support multiple sessions.

#### Path Parameters
- `conversation_id` (string, required): Conversation ID

#### Request Body (application/json)
```json
{
  "name": {
    "type": "string",
    "description": "(Optional) The name of the conversation. Omit if auto_generate is true."
  },
  "auto_generate": {
    "type": "boolean",
    "default": false,
    "description": "(Optional) Automatically generate the title. Default false."
  },
  "user": {
    "type": "string",
    "required": true,
    "description": "The user identifier."
  }
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
  "introduction": "string",
  "created_at": "integer (timestamp)",
  "updated_at": "integer (timestamp)"
}
```

#### 5. Get Conversation Variables

**GET** `/conversations/{conversation_id}/variables`

Retrieve variables from a specific conversation.

#### Path Parameters
- `conversation_id` (string, required): The ID of the conversation to retrieve variables from

#### Query Parameters
- `user` (string, required): The user identifier
- `last_id` (string, optional): The ID of the last record on the current page (for pagination)
- `limit` (integer, optional): How many records to return. Default 20, Min 1, Max 100
- `variable_name` (string, optional): Filter variables by a specific name

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
      "description": "string",
      "created_at": "integer (timestamp)",
      "updated_at": "integer (timestamp)"
    }
  ]
}
```

**Error Responses**
- **404**: Conversation Not Found

### Text-to-Speech & Speech-to-Text

#### 1. Convert Speech to Text

**POST** `/audio-to-text`

Convert audio file to text. Supported formats: mp3, mp4, mpeg, mpga, m4a, wav, webm. File size limit: 15MB.

#### Request Body (multipart/form-data)
```json
{
  "file": {
    "type": "string",
    "format": "binary",
    "required": true,
    "description": "Audio file. Supported: mp3, mp4, mpeg, mpga, m4a, wav, webm. Limit: 15MB."
  },
  "user": {
    "type": "string",
    "required": true,
    "description": "User identifier."
  }
}
```

#### Response

**Success (200)**
```json
{
  "text": {
    "type": "string",
    "description": "Output text from speech recognition."
  }
}
```

#### 2. Convert Text to Audio

**POST** `/text-to-audio`

Convert text to speech.

#### Request Body (multipart/form-data)
```json
{
  "message_id": {
    "type": "string",
    "format": "uuid",
    "description": "Message ID (priority if both text and message_id provided)."
  },
  "text": {
    "type": "string",
    "description": "Speech content."
  },
  "user": {
    "type": "string",
    "required": true,
    "description": "User identifier."
  }
}
```

#### Response

**Success (200)**
Returns audio file in binary format (audio/wav or audio/mp3).

### Application Information

#### 1. Get Application Basic Information

**GET** `/info`

Used to get basic information about this application.

#### Response

**Success (200)**
```json
{
  "name": {
    "type": "string",
    "description": "Application name"
  },
  "description": {
    "type": "string",
    "description": "Application description"
  },
  "tags": {
    "type": "array",
    "items": { "type": "string" },
    "description": "Application tags"
  }
}
```

#### 2. Get Application Parameters

**GET** `/parameters`

Used at the start of entering the page to obtain information such as features, input parameter names, types, and default values.

#### Query Parameters
- `user` (string, required): User identifier

#### Response

**Success (200)**
```json
{
  "opening_statement": { "type": "string" },
  "suggested_questions": { "type": "array", "items": { "type": "string" } },
  "suggested_questions_after_answer": {
    "type": "object",
    "properties": { "enabled": { "type": "boolean" } }
  },
  "speech_to_text": {
    "type": "object",
    "properties": { "enabled": { "type": "boolean" } }
  },
  "text_to_speech": {
    "type": "object",
    "properties": {
      "enabled": { "type": "boolean" },
      "voice": { "type": "string" },
      "language": { "type": "string" },
      "autoPlay": { "type": "string", "enum": ["enabled", "disabled"] }
    }
  },
  "retriever_resource": {
    "type": "object",
    "properties": { "enabled": { "type": "boolean" } }
  },
  "annotation_reply": {
    "type": "object",
    "properties": { "enabled": { "type": "boolean" } }
  },
  "user_input_form": {
    "type": "array",
    "items": { "$ref": "#/components/schemas/UserInputFormItem" }
  },
  "file_upload": {
    "type": "object",
    "properties": {
      "image": {
        "type": "object",
        "properties": {
          "enabled": { "type": "boolean" },
          "number_limits": { "type": "integer" },
          "detail": { "type": "string" },
          "transfer_methods": { "type": "array", "items": { "type": "string", "enum": ["remote_url", "local_file"] } }
        }
      }
    }
  },
  "system_parameters": {
    "type": "object",
    "properties": {
      "file_size_limit": { "type": "integer" },
      "image_file_size_limit": { "type": "integer" },
      "audio_file_size_limit": { "type": "integer" },
      "video_file_size_limit": { "type": "integer" }
    }
  }
}
```

#### 3. Get Application Meta Information

**GET** `/meta`

Used to get icons of tools in this application.

#### Response

**Success (200)**
```json
{
  "tool_icons": {
    "additionalProperties": {
      "oneOf": [
        {
          "type": "string",
          "format": "url",
          "description": "URL of the icon."
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

#### 4. Get WebApp Settings

**GET** `/site`

Used to get the WebApp settings of the application.

#### Response

**Success (200)**
```json
{
  "title": { "type": "string" },
  "chat_color_theme": { "type": "string" },
  "chat_color_theme_inverted": { "type": "boolean" },
  "icon_type": { "type": "string", "enum": ["emoji", "image"] },
  "icon": { "type": "string" },
  "icon_background": { "type": "string" },
  "icon_url": { "type": "string", "format": "url", "nullable": true },
  "description": { "type": "string" },
  "copyright": { "type": "string" },
  "privacy_policy": { "type": "string" },
  "custom_disclaimer": { "type": "string" },
  "default_language": { "type": "string" },
  "show_workflow_steps": { "type": "boolean" },
  "use_icon_as_answer_icon": { "type": "boolean" }
}
```

### Annotation Management

#### 1. Get Annotation List

**GET** `/apps/annotations`

Retrieves a list of annotations for the application.

#### Query Parameters
- `page` (integer, optional): Page number. Default: 1
- `limit` (integer, optional): Number of items returned, default 20, range 1-100

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

Creates a new annotation.

#### Request Body (application/json)
```json
{
  "question": {
    "type": "string",
    "required": true,
    "description": "Annotation question."
  },
  "answer": {
    "type": "string",
    "required": true,
    "description": "Annotation answer."
  }
}
```

#### Response

**Success (200)**
```json
{
  "id": { "type": "string", "format": "uuid" },
  "question": { "type": "string" },
  "answer": { "type": "string" },
  "hit_count": { "type": "integer" },
  "created_at": { "type": "integer", "format": "int64" }
}
```

#### 3. Update Annotation

**PUT** `/apps/annotations/{annotation_id}`

Updates an existing annotation.

#### Path Parameters
- `annotation_id` (string, required): Annotation ID

#### Request Body (application/json)
```json
{
  "question": {
    "type": "string",
    "required": true,
    "description": "Updated annotation question."
  },
  "answer": {
    "type": "string",
    "required": true,
    "description": "Updated annotation answer."
  }
}
```

#### Response

**Success (200)**
```json
{
  "id": { "type": "string", "format": "uuid" },
  "question": { "type": "string" },
  "answer": { "type": "string" },
  "hit_count": { "type": "integer" },
  "created_at": { "type": "integer", "format": "int64" }
}
```

#### 4. Delete Annotation

**DELETE** `/apps/annotations/{annotation_id}`

Deletes an annotation.

#### Path Parameters
- `annotation_id` (string, required): Annotation ID

#### Response

**Success (204)**
No Content - Annotation deleted successfully.

#### 5. Configure Annotation Reply Settings

**POST** `/apps/annotation-reply/{action}`

Enable or disable annotation reply settings and configure embedding models. This interface is executed asynchronously.

#### Path Parameters
- `action` (string, required): Action, can only be 'enable' or 'disable'
  - **Enum**: `["enable", "disable"]`

#### Request Body (application/json)
```json
{
  "embedding_provider_name": {
    "type": "string",
    "description": "Specified embedding model provider name (Optional)."
  },
  "embedding_model_name": {
    "type": "string",
    "description": "Specified embedding model name (Optional)."
  },
  "score_threshold": {
    "type": "number",
    "format": "float",
    "required": true,
    "description": "Similarity threshold for matching annotated replies."
  }
}
```

#### Response

**Success (200)**
```json
{
  "job_id": { "type": "string", "format": "uuid" },
  "job_status": { "type": "string" }
}
```

#### 6. Get Annotation Reply Settings Status

**GET** `/apps/annotation-reply/{action}/status/{job_id}`

Queries the status of an asynchronously executed annotation reply settings task.

#### Path Parameters
- `action` (string, required): Action, must be the same as in the initial settings call
  - **Enum**: `["enable", "disable"]`
- `job_id` (string, required): Job ID obtained from the initial settings call

#### Response

**Success (200)**
```json
{
  "job_id": { "type": "string", "format": "uuid" },
  "job_status": { "type": "string" },
  "error_msg": { "type": "string", "nullable": true }
}
```

## Error Responses

All APIs return standard HTTP status codes with detailed error information:

- **200 OK**: Request successful
- **204 No Content**: Request successful with no content returned
- **400 Bad Request**: Invalid parameters or request format
  - **Error codes**: `invalid_param`, `app_unavailable`, `provider_not_initialize`, `provider_quota_exceeded`, `model_currently_not_support`, `completion_request_error`
- **401 Unauthorized**: Missing or invalid API key
- **403 Forbidden**: Insufficient permissions
- **404 Not Found**: Resource not found (conversation, message, etc.)
- **413 Payload Too Large**: File size exceeds limits
- **415 Unsupported Media Type**: Invalid file format
- **429 Too Many Requests**: Rate limit exceeded
- **500 Internal Server Error**: Server error
- **503 Service Unavailable**: Service temporarily unavailable

### Error Response Format

```json
{
  "status": "integer",
  "code": "string",
  "message": "string"
}
```

## Usage Examples

### Basic Chat
```bash
curl -X POST 'https://api.dify.ai/v1/chat-messages' \
--header 'Authorization: Bearer {api_key}' \
--header 'Content-Type: application/json' \
--data-raw '{
    "inputs": {},
    "query": "Hello, how are you?",
    "response_mode": "blocking",
    "user": "user-123"
}'
```

### Streaming Chat
```bash
curl -X POST 'https://api.dify.ai/v1/chat-messages' \
--header 'Authorization: Bearer {api_key}' \
--header 'Content-Type: application/json' \
--data-raw '{
    "inputs": {},
    "query": "Tell me a story",
    "response_mode": "streaming",
    "user": "user-123"
}'
```

### File Upload
```bash
curl -X POST 'https://api.dify.ai/v1/files/upload' \
--header 'Authorization: Bearer {api_key}' \
--form 'file=@"/path/to/image.jpg"' \
--form 'user="user-123"'
```

### Conversation Management
```bash
# Get conversations list
curl -X GET 'https://api.dify.ai/v1/conversations?user=user-123&limit=20' \
--header 'Authorization: Bearer {api_key}'

# Get conversation history
curl -X GET 'https://api.dify.ai/v1/messages?conversation_id={conv_id}&user=user-123' \
--header 'Authorization: Bearer {api_key}'

# Rename conversation
curl -X POST 'https://api.dify.ai/v1/conversations/{conv_id}/name' \
--header 'Authorization: Bearer {api_key}' \
--header 'Content-Type: application/json' \
--data-raw '{
    "name": "My Important Chat",
    "user": "user-123"
}'
```

### Audio Processing
```bash
# Speech to Text
curl -X POST 'https://api.dify.ai/v1/audio-to-text' \
--header 'Authorization: Bearer {api_key}' \
--form 'file=@"/path/to/audio.mp3"' \
--form 'user="user-123"'

# Text to Speech
curl -X POST 'https://api.dify.ai/v1/text-to-audio' \
--header 'Authorization: Bearer {api_key}' \
--form 'text="Hello, how are you?"' \
--form 'user="user-123"'
```

### Feedback and Annotations
```bash
# Submit feedback
curl -X POST 'https://api.dify.ai/v1/messages/{message_id}/feedbacks' \
--header 'Authorization: Bearer {api_key}' \
--header 'Content-Type: application/json' \
--data-raw '{
    "rating": "like",
    "user": "user-123",
    "content": "Great response!"
}'

# Create annotation
curl -X POST 'https://api.dify.ai/v1/apps/annotations' \
--header 'Authorization: Bearer {api_key}' \
--header 'Content-Type: application/json' \
--data-raw '{
    "question": "What is AI?",
    "answer": "Artificial Intelligence is..."
}'
```

## Best Practices

1. **Response Mode Selection**: Use `streaming` for real-time user experience, `blocking` for simple integrations
2. **User Identification**: Ensure unique user identifiers across sessions for proper conversation isolation
3. **File Upload**: Pre-upload files before sending chat messages with file attachments
4. **Error Handling**: Implement proper retry logic with exponential backoff for production applications
5. **Streaming Processing**: Handle different event types appropriately in streaming mode
6. **Conversation Management**: Use conversation IDs to maintain context across multiple messages
7. **Feedback Collection**: Implement feedback mechanisms to improve AI responses over time
8. **Rate Limiting**: Respect API rate limits and implement queuing for high-volume applications
9. **Security**: Store API keys securely in backend services, never expose in client-side code
10. **Monitoring**: Track usage metrics and error rates for production deployments

## Supported File Formats

### Image Files (for Vision Models)
- **PNG**: Portable Network Graphics
- **JPG/JPEG**: Joint Photographic Experts Group
- **WEBP**: Web Picture format
- **GIF**: Graphics Interchange Format

### Audio Files (for Speech Processing)
- **MP3**: MPEG Audio Layer III
- **MP4**: MPEG-4 Audio
- **MPEG**: Motion Picture Experts Group
- **MPGA**: MPEG Audio
- **M4A**: MPEG-4 Audio
- **WAV**: Waveform Audio File Format
- **WEBM**: WebM Audio

*File size limits: Images up to system limit, Audio files up to 15MB*

## Data Schemas

### Usage Schema
```json
{
  "type": "object",
  "description": "Model usage information.",
  "properties": {
    "prompt_tokens": { "type": "integer" },
    "prompt_unit_price": { "type": "string", "format": "decimal" },
    "prompt_price_unit": { "type": "string", "format": "decimal" },
    "prompt_price": { "type": "string", "format": "decimal" },
    "completion_tokens": { "type": "integer" },
    "completion_unit_price": { "type": "string", "format": "decimal" },
    "completion_price_unit": { "type": "string", "format": "decimal" },
    "completion_price": { "type": "string", "format": "decimal" },
    "total_tokens": { "type": "integer" },
    "total_price": { "type": "string", "format": "decimal" },
    "currency": { "type": "string", "example": "USD" },
    "latency": { "type": "number", "format": "double" }
  }
}
```

### RetrieverResource Schema
```json
{
  "type": "object",
  "description": "Citation and Attribution information for a resource.",
  "properties": {
    "position": { "type": "integer", "description": "Position of the resource in the list." },
    "dataset_id": { "type": "string", "format": "uuid", "description": "ID of the dataset." },
    "dataset_name": { "type": "string", "description": "Name of the dataset." },
    "document_id": { "type": "string", "format": "uuid", "description": "ID of the document." },
    "document_name": { "type": "string", "description": "Name of the document." },
    "segment_id": { "type": "string", "format": "uuid", "description": "ID of the specific segment within the document." },
    "score": { "type": "number", "format": "float", "description": "Relevance score of the resource." },
    "content": { "type": "string", "description": "Content snippet from the resource." }
  }
}
```

### MessageFileItem Schema
```json
{
  "type": "object",
  "properties": {
    "id": { "type": "string", "format": "uuid" },
    "type": { "type": "string", "description": "File type, e.g., 'image'." },
    "url": { "type": "string", "format": "url", "description": "Preview image URL." },
    "belongs_to": { "type": "string", "enum": ["user", "assistant"], "description": "Who this file belongs to." }
  }
}
```

### AgentThoughtItem Schema
```json
{
  "type": "object",
  "properties": {
    "id": { "type": "string", "format": "uuid", "description": "Agent thought ID." },
    "message_id": { "type": "string", "format": "uuid", "description": "Unique message ID this thought belongs to." },
    "position": { "type": "integer", "description": "Position of this thought." },
    "thought": { "type": "string", "description": "What LLM is thinking." },
    "tool": { "type": "string", "description": "Tools called, split by ';'." },
    "tool_input": { "type": "string", "description": "Input of tools in JSON format." },
    "observation": { "type": "string", "description": "Response from tool calls." },
    "files": {
      "type": "array",
      "items": { "type": "string", "format": "uuid" },
      "description": "File IDs related to this thought."
    },
    "created_at": { "type": "integer", "format": "int64", "description": "Creation timestamp." }
  }
}
```

### UserInputFormItem Schema
```json
{
  "type": "object",
  "oneOf": [
    {
      "type": "object",
      "properties": {
        "text-input": {
          "type": "object",
          "required": ["label", "variable", "required"],
          "properties": {
            "label": { "type": "string" },
            "variable": { "type": "string" },
            "required": { "type": "boolean" },
            "default": { "type": "string" }
          }
        }
      },
      "required": ["text-input"]
    },
    {
      "type": "object",
      "properties": {
        "paragraph": {
          "type": "object",
          "required": ["label", "variable", "required"],
          "properties": {
            "label": { "type": "string" },
            "variable": { "type": "string" },
            "required": { "type": "boolean" },
            "default": { "type": "string" }
          }
        }
      },
      "required": ["paragraph"]
    },
    {
      "type": "object",
      "properties": {
        "select": {
          "type": "object",
          "required": ["label", "variable", "required", "options"],
          "properties": {
            "label": { "type": "string" },
            "variable": { "type": "string" },
            "required": { "type": "boolean" },
            "default": { "type": "string" },
            "options": { "type": "array", "items": { "type": "string" } }
          }
        }
      },
      "required": ["select"]
    }
  ]
}
```

### ToolIconDetail Schema
```json
{
  "type": "object",
  "properties": {
    "background": { "type": "string", "description": "Background color in hex format." },
    "content": { "type": "string", "description": "Emoji content." }
  }
}
```

## Error Response Codes

### File Upload Errors
- **`no_file_uploaded`**: A file must be provided
- **`too_many_files`**: Currently only one file is accepted
- **`unsupported_preview`**: The file does not support preview
- **`unsupported_estimate`**: The file does not support estimation
- **`file_too_large`**: The file is too large
- **`unsupported_file_type`**: Unsupported extension

### S3 Storage Errors
- **`s3_connection_failed`**: Unable to connect to S3 service
- **`s3_permission_denied`**: No permission to upload files to S3
- **`s3_file_too_large`**: File exceeds S3 size limit

### Conversation Errors
- **`conversation_not_exists`**: Conversation not found

## API Summary

Total APIs: **22 endpoints** across 7 categories:
- **Chat Messages**: 3 APIs
- **File Management**: 1 API
- **Feedback Management**: 2 APIs
- **Conversation Management**: 5 APIs
- **Text-to-Speech & Speech-to-Text**: 2 APIs
- **Application Information**: 4 APIs
- **Annotation Management**: 6 APIs

All APIs follow RESTful conventions with proper HTTP methods, consistent request/response formats, comprehensive error handling, and support for both synchronous and asynchronous operations.