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
  "inputs": {
    "type": "object",
    "description": "Allows the entry of various variable values defined by the App.",
    "additionalProperties": true
  },
  "query": {
    "type": "string",
    "required": true,
    "description": "User input/question content."
  },
  "response_mode": {
    "type": "string",
    "required": true,
    "description": "Response return mode. 'streaming' (recommended) uses SSE. 'blocking' returns after completion (may be interrupted for long processes; not supported in Agent Assistant mode). Cloudflare timeout is 100s.",
    "enum": ["streaming", "blocking"],
    "default": "streaming"
  },
  "conversation_id": {
    "type": "string",
    "description": "Conversation ID. To start a new conversation, just exclude this parameter."
  },
  "user": {
    "type": "string",
    "required": true,
    "description": "User identifier, defined by the developer's rules, must be unique within the application."
  },
  "files": {
    "type": "array",
    "description": "Files list, suitable for inputting files combined with text, available only when the model supports Vision capability.",
    "items": {
      "type": "object",
      "properties": {
        "type": {
          "type": "string",
          "enum": ["image"],
          "description": "Supported type: image (more types will be added in the future)."
        },
        "transfer_method": {
          "type": "string",
          "enum": ["remote_url", "local_file"],
          "description": "Transfer method, remote_url for image URL, local_file for file upload."
        },
        "url": {
          "type": "string",
          "description": "Image URL (when transfer_method is remote_url)."
        },
        "upload_file_id": {
          "type": "string",
          "description": "Uploaded file ID, must be obtained by uploading through the file upload interface in advance (when transfer_method is local_file)."
        }
      }
    }
  },
  "auto_generate_name": {
    "type": "boolean",
    "default": true,
    "description": "Auto-generate title, default to true. If set to false, the title will be \"New Chat\"."
  }
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
  "event": "message",
  "task_id": "string",
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

**Success (200) - Streaming Mode**
```
Content-Type: text/event-stream

data: {"event": "message", "task_id": "task123", "message_id": "msg123", "conversation_id": "conv123", "answer": "Hello", "created_at": 1679586595}

data: {"event": "message_end", "task_id": "task123", "message_id": "msg123", "conversation_id": "conv123", "metadata": {"usage": {"total_tokens": 10, "latency": 1.0}}}
```

**Streaming Event Types**
- `message` - Incremental message content
- `agent_message` - Agent assistant message content
- `tts_message` - Text-to-speech message
- `tts_message_end` - Text-to-speech completion
- `agent_thought` - Agent reasoning process
- `message_file` - File attachment in message
- `message_end` - Message completion with metadata
- `message_replace` - Message content replacement
- `error` - Error occurred during processing
- `ping` - Keep-alive ping

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
  "data": [
    {
      "id": "string (uuid)",
      "app_id": "string (uuid)",
      "conversation_id": "string (uuid)",
      "message_id": "string (uuid)",
      "rating": "string",
      "content": "string",
      "from_source": "string",
      "from_end_user_id": "string (uuid)",
      "from_account_id": "string (uuid)",
      "created_at": "string (date-time)",
      "updated_at": "string (date-time)"
    }
  ]
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
  "text": "string"
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
  "name": "string",
  "description": "string",
  "tags": ["string"]
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
    "autoPlay": {
      "type": "string",
      "enum": ["enabled", "disabled"]
    }
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
      "transfer_methods": ["remote_url", "local_file"]
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
  "title": "string",
  "chat_color_theme": "string",
  "chat_color_theme_inverted": "boolean",
  "icon_type": {
    "type": "string",
    "enum": ["emoji", "image"]
  },
  "icon": "string",
  "icon_background": "string",
  "icon_url": "string (url)",
  "description": "string",
  "copyright": "string",
  "privacy_policy": "string",
  "custom_disclaimer": "string",
  "default_language": "string",
  "show_workflow_steps": "boolean",
  "use_icon_as_answer_icon": "boolean"
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
  "id": "string (uuid)",
  "question": "string",
  "answer": "string",
  "hit_count": "integer",
  "created_at": "integer (timestamp)"
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
  "id": "string (uuid)",
  "question": "string",
  "answer": "string",
  "hit_count": "integer",
  "created_at": "integer (timestamp)"
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
  "job_id": "string (uuid)",
  "job_status": "string"
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
  "job_id": "string (uuid)",
  "job_status": "string",
  "error_msg": "string"
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