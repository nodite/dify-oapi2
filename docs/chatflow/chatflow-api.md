# Chatflow APIs

This document covers all chatflow APIs based on the official Dify OpenAPI specification. Chatflow APIs provide advanced chat functionality with workflow events, file support, conversation management, and comprehensive application settings.

> **Updated with Detailed Data Types**: This documentation has been enhanced with comprehensive schema definitions and detailed data types extracted from the official Dify OpenAPI specification (openapi_chatflow.json).

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

**Schema**: `AdvancedChatRequest`

```json
{
  "query": "string (required) - User input/question content",
  "inputs": {
    "type": "object (optional)",
    "description": "Key/value pairs for app variables. For file type variables, value should be an InputFileObject",
    "additionalProperties": {
      "oneOf": [
        {"type": "string"},
        {"type": "number"},
        {"type": "boolean"},
        {"$ref": "InputFileObjectAdvanced"}
      ]
    },
    "default": {}
  },
  "response_mode": {
    "type": "string (optional)",
    "enum": ["streaming", "blocking"],
    "default": "streaming",
    "description": "Response mode. Cloudflare timeout is 100s for blocking"
  },
  "user": "string (required) - User identifier",
  "conversation_id": "string (optional) - Conversation ID to continue",
  "files": {
    "type": "array (optional)",
    "items": {"$ref": "InputFileObjectAdvanced"},
    "description": "List of files for Vision-capable models or general file input"
  },
  "auto_generate_name": {
    "type": "boolean (optional)",
    "default": true,
    "description": "Auto-generate conversation title"
  }
}
```

**InputFileObjectAdvanced Schema**:
```json
{
  "type": "object",
  "required": ["type", "transfer_method"],
  "properties": {
    "type": {
      "type": "string",
      "enum": ["document", "image", "audio", "video", "custom"],
      "description": "Type of the file. 'document' covers TXT, MD, PDF, HTML, XLSX, DOCX, CSV, EML, MSG, PPTX, XML, EPUB. 'image' covers JPG, PNG, GIF, WEBP, SVG. 'audio' covers MP3, M4A, WAV, WEBM, AMR. 'video' covers MP4, MOV, MPEG, MPGA."
    },
    "transfer_method": {
      "type": "string",
      "enum": ["remote_url", "local_file"],
      "description": "Transfer method, remote_url for file URL / local_file for file upload"
    },
    "url": {
      "type": "string",
      "format": "url",
      "description": "File URL (when the transfer method is remote_url)"
    },
    "upload_file_id": {
      "type": "string",
      "description": "Uploaded file ID, which must be obtained by uploading through the File Upload API in advance (when the transfer method is local_file)"
    }
  },
  "anyOf": [
    {
      "properties": {
        "transfer_method": {"enum": ["remote_url"]},
        "url": {"type": "string", "format": "url"}
      },
      "required": ["url"],
      "not": {"required": ["upload_file_id"]}
    },
    {
      "properties": {
        "transfer_method": {"enum": ["local_file"]},
        "upload_file_id": {"type": "string"}
      },
      "required": ["upload_file_id"],
      "not": {"required": ["url"]}
    }
  ]
}
```

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

**Blocking Mode (application/json)** - Schema: `ChatCompletionResponse`:
```json
{
  "event": {
    "type": "string",
    "example": "message"
  },
  "task_id": {
    "type": "string",
    "format": "uuid"
  },
  "id": {
    "type": "string",
    "format": "uuid",
    "description": "Unique ID of this response event"
  },
  "message_id": {
    "type": "string",
    "format": "uuid"
  },
  "conversation_id": {
    "type": "string",
    "format": "uuid"
  },
  "mode": {
    "type": "string",
    "example": "chat"
  },
  "answer": {
    "type": "string"
  },
  "metadata": {
    "$ref": "ResponseMetadata"
  },
  "created_at": {
    "type": "integer",
    "format": "int64"
  }
}
```

**ResponseMetadata Schema**:
```json
{
  "type": "object",
  "properties": {
    "usage": {"$ref": "Usage"},
    "retriever_resources": {
      "type": "array",
      "items": {"$ref": "RetrieverResource"}
    }
  }
}
```

**Usage Schema**:
```json
{
  "type": "object",
  "properties": {
    "prompt_tokens": {"type": "integer"},
    "prompt_unit_price": {"type": "string"},
    "prompt_price_unit": {"type": "string"},
    "prompt_price": {"type": "string"},
    "completion_tokens": {"type": "integer"},
    "completion_unit_price": {"type": "string"},
    "completion_price_unit": {"type": "string"},
    "completion_price": {"type": "string"},
    "total_tokens": {"type": "integer"},
    "total_price": {"type": "string"},
    "currency": {"type": "string"},
    "latency": {
      "type": "number",
      "format": "double"
    }
  }
}
```

**RetrieverResource Schema**:
```json
{
  "type": "object",
  "properties": {
    "position": {"type": "integer"},
    "dataset_id": {
      "type": "string",
      "format": "uuid"
    },
    "dataset_name": {"type": "string"},
    "document_id": {
      "type": "string",
      "format": "uuid"
    },
    "document_name": {"type": "string"},
    "segment_id": {
      "type": "string",
      "format": "uuid"
    },
    "score": {
      "type": "number",
      "format": "float"
    },
    "content": {"type": "string"}
  }
}
```

**Streaming Mode (text/event-stream)** - Schema: `ChunkAdvancedChatEvent`:

Stream of Server-Sent Events with discriminated union based on `event` property:

**Base Event Schema**:
```json
{
  "type": "object",
  "required": ["event"],
  "properties": {
    "event": {
      "type": "string",
      "enum": ["message", "message_file", "message_end", "tts_message", "tts_message_end", "message_replace", "workflow_started", "node_started", "node_finished", "workflow_finished", "error", "ping"]
    }
  }
}
```

**StreamEventBaseAdv** (common properties):
```json
{
  "type": "object",
  "properties": {
    "task_id": {
      "type": "string",
      "format": "uuid"
    },
    "message_id": {
      "type": "string",
      "format": "uuid"
    },
    "conversation_id": {
      "type": "string",
      "format": "uuid"
    },
    "created_at": {
      "type": "integer",
      "format": "int64"
    }
  }
}
```

**Event Type Schemas**:

1. **message** - `StreamEventAdvChatMessage`:
```json
{
  "allOf": [
    {"$ref": "ChunkAdvancedChatEvent"},
    {"$ref": "StreamEventBaseAdv"},
    {
      "type": "object",
      "required": ["answer"],
      "properties": {
        "answer": {"type": "string"}
      }
    }
  ]
}
```

2. **message_file** - `StreamEventAdvMessageFile`:
```json
{
  "allOf": [
    {"$ref": "ChunkAdvancedChatEvent"},
    {
      "type": "object",
      "required": ["id", "type", "belongs_to", "url", "conversation_id"],
      "properties": {
        "id": {
          "type": "string",
          "format": "uuid"
        },
        "type": {
          "type": "string",
          "description": "File type, e.g., 'image'"
        },
        "belongs_to": {
          "type": "string",
          "enum": ["assistant"]
        },
        "url": {
          "type": "string",
          "format": "url"
        },
        "conversation_id": {
          "type": "string",
          "format": "uuid"
        }
      }
    }
  ]
}
```

3. **message_end** - `StreamEventAdvMessageEnd`:
```json
{
  "allOf": [
    {"$ref": "ChunkAdvancedChatEvent"},
    {"$ref": "StreamEventBaseAdv"},
    {
      "type": "object",
      "required": ["metadata"],
      "properties": {
        "metadata": {"$ref": "ResponseMetadata"}
      }
    }
  ]
}
```

4. **tts_message** - `StreamEventAdvTtsMessage`:
```json
{
  "allOf": [
    {"$ref": "ChunkAdvancedChatEvent"},
    {"$ref": "StreamEventBaseAdv"},
    {
      "type": "object",
      "required": ["audio"],
      "properties": {
        "audio": {
          "type": "string",
          "format": "byte",
          "description": "Base64 encoded audio"
        }
      }
    }
  ]
}
```

5. **tts_message_end** - `StreamEventAdvTtsMessageEnd`:
```json
{
  "allOf": [
    {"$ref": "ChunkAdvancedChatEvent"},
    {"$ref": "StreamEventBaseAdv"},
    {
      "type": "object",
      "required": ["audio"],
      "properties": {
        "audio": {
          "type": "string",
          "description": "Empty string"
        }
      }
    }
  ]
}
```

6. **message_replace** - `StreamEventAdvMessageReplace`:
```json
{
  "allOf": [
    {"$ref": "ChunkAdvancedChatEvent"},
    {"$ref": "StreamEventBaseAdv"},
    {
      "type": "object",
      "required": ["answer"],
      "properties": {
        "answer": {
          "type": "string",
          "description": "Replacement content"
        }
      }
    }
  ]
}
```

7. **workflow_started** - `StreamEventAdvWorkflowStarted`:
```json
{
  "allOf": [
    {"$ref": "ChunkAdvancedChatEvent"},
    {
      "type": "object",
      "required": ["task_id", "workflow_run_id", "data"],
      "properties": {
        "task_id": {
          "type": "string",
          "format": "uuid"
        },
        "workflow_run_id": {
          "type": "string",
          "format": "uuid"
        },
        "data": {"$ref": "WorkflowStartedData"}
      }
    }
  ]
}
```

**WorkflowStartedData Schema**:
```json
{
  "type": "object",
  "required": ["id", "workflow_id", "sequence_number", "created_at"],
  "properties": {
    "id": {
      "type": "string",
      "format": "uuid"
    },
    "workflow_id": {
      "type": "string",
      "format": "uuid"
    },
    "sequence_number": {"type": "integer"},
    "created_at": {
      "type": "integer",
      "format": "int64"
    }
  }
}
```

8. **node_started** - `StreamEventAdvNodeStarted`:
```json
{
  "allOf": [
    {"$ref": "ChunkAdvancedChatEvent"},
    {
      "type": "object",
      "required": ["task_id", "workflow_run_id", "data"],
      "properties": {
        "task_id": {
          "type": "string",
          "format": "uuid"
        },
        "workflow_run_id": {
          "type": "string",
          "format": "uuid"
        },
        "data": {"$ref": "NodeStartedData"}
      }
    }
  ]
}
```

**NodeStartedData Schema**:
```json
{
  "type": "object",
  "required": ["id", "node_id", "node_type", "title", "index", "created_at"],
  "properties": {
    "id": {
      "type": "string",
      "format": "uuid",
      "description": "Unique ID of this node execution instance"
    },
    "node_id": {
      "type": "string",
      "format": "uuid",
      "description": "ID of the node definition"
    },
    "node_type": {"type": "string"},
    "title": {"type": "string"},
    "index": {"type": "integer"},
    "predecessor_node_id": {
      "type": "string",
      "format": "uuid",
      "nullable": true
    },
    "inputs": {
      "type": "object",
      "additionalProperties": true,
      "description": "Variables used by the node"
    },
    "created_at": {
      "type": "integer",
      "format": "int64"
    }
  }
}
```

9. **node_finished** - `StreamEventAdvNodeFinished`:
```json
{
  "allOf": [
    {"$ref": "ChunkAdvancedChatEvent"},
    {
      "type": "object",
      "required": ["task_id", "workflow_run_id", "data"],
      "properties": {
        "task_id": {
          "type": "string",
          "format": "uuid"
        },
        "workflow_run_id": {
          "type": "string",
          "format": "uuid"
        },
        "data": {"$ref": "NodeFinishedData"}
      }
    }
  ]
}
```

**NodeFinishedData Schema**:
```json
{
  "type": "object",
  "required": ["id", "node_id", "node_type", "title", "index", "status", "created_at"],
  "properties": {
    "id": {
      "type": "string",
      "format": "uuid"
    },
    "node_id": {
      "type": "string",
      "format": "uuid"
    },
    "node_type": {"type": "string"},
    "title": {"type": "string"},
    "index": {"type": "integer"},
    "predecessor_node_id": {
      "type": "string",
      "format": "uuid",
      "nullable": true
    },
    "inputs": {
      "type": "object",
      "additionalProperties": true,
      "nullable": true
    },
    "process_data": {
      "type": "object",
      "additionalProperties": true,
      "nullable": true,
      "description": "Node process data (JSON)"
    },
    "outputs": {
      "type": "object",
      "additionalProperties": true,
      "nullable": true,
      "description": "Output content (JSON)"
    },
    "status": {
      "type": "string",
      "enum": ["running", "succeeded", "failed", "stopped"]
    },
    "error": {
      "type": "string",
      "nullable": true
    },
    "elapsed_time": {
      "type": "number",
      "format": "float",
      "nullable": true
    },
    "execution_metadata": {
      "$ref": "NodeExecutionMetadata",
      "nullable": true
    },
    "created_at": {
      "type": "integer",
      "format": "int64"
    }
  }
}
```

**NodeExecutionMetadata Schema**:
```json
{
  "type": "object",
  "properties": {
    "total_tokens": {
      "type": "integer",
      "nullable": true
    },
    "total_price": {
      "type": "number",
      "format": "float",
      "nullable": true,
      "description": "Using float for price compatibility"
    },
    "currency": {
      "type": "string",
      "nullable": true,
      "example": "USD"
    }
  }
}
```

10. **workflow_finished** - `StreamEventAdvWorkflowFinished`:
```json
{
  "allOf": [
    {"$ref": "ChunkAdvancedChatEvent"},
    {
      "type": "object",
      "required": ["task_id", "workflow_run_id", "data"],
      "properties": {
        "task_id": {
          "type": "string",
          "format": "uuid"
        },
        "workflow_run_id": {
          "type": "string",
          "format": "uuid"
        },
        "data": {"$ref": "WorkflowFinishedData"}
      }
    }
  ]
}
```

**WorkflowFinishedData Schema**:
```json
{
  "type": "object",
  "required": ["id", "workflow_id", "status", "created_at", "finished_at"],
  "properties": {
    "id": {
      "type": "string",
      "format": "uuid"
    },
    "workflow_id": {
      "type": "string",
      "format": "uuid"
    },
    "status": {
      "type": "string",
      "enum": ["running", "succeeded", "failed", "stopped"]
    },
    "outputs": {
      "type": "object",
      "additionalProperties": true,
      "nullable": true,
      "description": "Output content (JSON)"
    },
    "error": {
      "type": "string",
      "nullable": true
    },
    "elapsed_time": {
      "type": "number",
      "format": "float",
      "nullable": true
    },
    "total_tokens": {
      "type": "integer",
      "nullable": true
    },
    "total_steps": {
      "type": "integer",
      "default": 0
    },
    "created_at": {
      "type": "integer",
      "format": "int64"
    },
    "finished_at": {
      "type": "integer",
      "format": "int64"
    }
  }
}
```

11. **error** - `StreamEventAdvError`:
```json
{
  "allOf": [
    {"$ref": "ChunkAdvancedChatEvent"},
    {
      "type": "object",
      "required": ["task_id", "status", "code", "message"],
      "properties": {
        "task_id": {
          "type": "string",
          "format": "uuid"
        },
        "message_id": {
          "type": "string",
          "format": "uuid",
          "nullable": true,
          "description": "May not always be present in a generic error"
        },
        "status": {"type": "integer"},
        "code": {"type": "string"},
        "message": {"type": "string"}
      }
    }
  ]
}
```

12. **ping** - `StreamEventAdvPing`:
```json
{
  "allOf": [
    {"$ref": "ChunkAdvancedChatEvent"},
    {"type": "object"}
  ]
}
```

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

**Success (200)** - Schema: `SuggestedQuestionsResponse`:
```json
{
  "type": "object",
  "properties": {
    "result": {
      "type": "string",
      "example": "success"
    },
    "data": {
      "type": "array",
      "items": {"type": "string"}
    }
  }
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

**Success (200)** - Schema: `FileUploadResponse`:
```json
{
  "type": "object",
  "properties": {
    "id": {
      "type": "string",
      "format": "uuid"
    },
    "name": {"type": "string"},
    "size": {"type": "integer"},
    "extension": {"type": "string"},
    "mime_type": {"type": "string"},
    "created_by": {
      "type": "string",
      "format": "uuid"
    },
    "created_at": {
      "type": "integer",
      "format": "int64"
    }
  }
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

#### Request Body (application/json) - Schema: `MessageFeedbackRequest`:
```json
{
  "type": "object",
  "required": ["user"],
  "properties": {
    "rating": {
      "type": "string",
      "enum": ["like", "dislike", null],
      "nullable": true
    },
    "user": {"type": "string"},
    "content": {
      "type": "string",
      "nullable": true
    }
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
- `page` (integer, optional): Page number, default: 1
- `limit` (integer, optional): Number of items per page

#### Response

**Success (200)** - Schema: `AppFeedbacksResponse`:
```json
{
  "type": "object",
  "properties": {
    "data": {
      "type": "array",
      "items": {"$ref": "FeedbackItem"}
    }
  }
}
```

**FeedbackItem Schema**:
```json
{
  "type": "object",
  "properties": {
    "id": {
      "type": "string",
      "format": "uuid"
    },
    "app_id": {
      "type": "string",
      "format": "uuid"
    },
    "conversation_id": {
      "type": "string",
      "format": "uuid"
    },
    "message_id": {
      "type": "string",
      "format": "uuid"
    },
    "rating": {
      "type": "string",
      "enum": ["like", "dislike", null],
      "nullable": true
    },
    "content": {"type": "string"},
    "from_source": {"type": "string"},
    "from_end_user_id": {
      "type": "string",
      "format": "uuid"
    },
    "from_account_id": {
      "type": "string",
      "format": "uuid",
      "nullable": true
    },
    "created_at": {
      "type": "string",
      "format": "date-time"
    },
    "updated_at": {
      "type": "string",
      "format": "date-time"
    }
  }
}
```

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

**Success (200)** - Schema: `ConversationHistoryResponse`:
```json
{
  "type": "object",
  "properties": {
    "limit": {"type": "integer"},
    "has_more": {"type": "boolean"},
    "data": {
      "type": "array",
      "items": {"$ref": "ConversationMessageItem"}
    }
  }
}
```

**ConversationMessageItem Schema**:
```json
{
  "type": "object",
  "properties": {
    "id": {
      "type": "string",
      "format": "uuid"
    },
    "conversation_id": {
      "type": "string",
      "format": "uuid"
    },
    "inputs": {
      "type": "object",
      "additionalProperties": true
    },
    "query": {"type": "string"},
    "answer": {"type": "string"},
    "message_files": {
      "type": "array",
      "items": {"$ref": "MessageFileItem"}
    },
    "feedback": {
      "type": "object",
      "nullable": true,
      "properties": {
        "rating": {
          "type": "string",
          "enum": ["like", "dislike"]
        }
      }
    },
    "retriever_resources": {
      "type": "array",
      "items": {"$ref": "RetrieverResource"}
    },
    "created_at": {
      "type": "integer",
      "format": "int64"
    }
  }
}
```

**MessageFileItem Schema**:
```json
{
  "type": "object",
  "properties": {
    "id": {
      "type": "string",
      "format": "uuid"
    },
    "type": {"type": "string"},
    "url": {
      "type": "string",
      "format": "url"
    },
    "belongs_to": {
      "type": "string",
      "enum": ["user", "assistant"]
    }
  }
}
```

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

**Success (200)** - Schema: `ConversationsListResponse`:
```json
{
  "type": "object",
  "properties": {
    "limit": {"type": "integer"},
    "has_more": {"type": "boolean"},
    "data": {
      "type": "array",
      "items": {"$ref": "ConversationListItem"}
    }
  }
}
```

**ConversationListItem Schema**:
```json
{
  "type": "object",
  "properties": {
    "id": {
      "type": "string",
      "format": "uuid"
    },
    "name": {"type": "string"},
    "inputs": {
      "type": "object",
      "additionalProperties": true
    },
    "status": {"type": "string"},
    "introduction": {
      "type": "string",
      "nullable": true
    },
    "created_at": {
      "type": "integer",
      "format": "int64"
    },
    "updated_at": {
      "type": "integer",
      "format": "int64"
    }
  }
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

#### Request Body (application/json) - Schema: `ConversationRenameRequest`:
```json
{
  "type": "object",
  "required": ["user"],
  "properties": {
    "name": {
      "type": "string",
      "nullable": true
    },
    "auto_generate": {
      "type": "boolean",
      "default": false
    },
    "user": {"type": "string"}
  }
}
```

#### Response

**Success (200)** - Schema: `ConversationRenameResponse` (same as `ConversationListItem`):
```json
{
  "type": "object",
  "properties": {
    "id": {
      "type": "string",
      "format": "uuid"
    },
    "name": {"type": "string"},
    "inputs": {
      "type": "object",
      "additionalProperties": true
    },
    "status": {"type": "string"},
    "introduction": {
      "type": "string",
      "nullable": true
    },
    "created_at": {
      "type": "integer",
      "format": "int64"
    },
    "updated_at": {
      "type": "integer",
      "format": "int64"
    }
  }
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

**Success (200)** - Schema: `ConversationVariablesResponse`:
```json
{
  "type": "object",
  "properties": {
    "limit": {"type": "integer"},
    "has_more": {"type": "boolean"},
    "data": {
      "type": "array",
      "items": {"$ref": "ConversationVariableItem"}
    }
  }
}
```

**ConversationVariableItem Schema**:
```json
{
  "type": "object",
  "properties": {
    "id": {
      "type": "string",
      "format": "uuid"
    },
    "name": {"type": "string"},
    "value_type": {"type": "string"},
    "value": {"type": "string"},
    "description": {
      "type": "string",
      "nullable": true
    },
    "created_at": {
      "type": "integer",
      "format": "int64"
    },
    "updated_at": {
      "type": "integer",
      "format": "int64"
    }
  }
}
```

**Error Responses**
- **404**: Conversation not found

### TTS (Text-to-Speech)

#### 1. Speech to Text

**POST** `/audio-to-text`

Convert audio file to text. File size limit: 15MB.

#### Request Body (multipart/form-data) - Schema: `AudioToTextRequest`:
```json
{
  "type": "object",
  "required": ["file", "user"],
  "properties": {
    "file": {
      "type": "string",
      "format": "binary",
      "description": "Audio file. Formats: mp3, mp4, mpeg, mpga, m4a, wav, webm. Limit: 15MB."
    },
    "user": {"type": "string"}
  }
}
```

#### Response

**Success (200)** - Schema: `AudioToTextResponse`:
```json
{
  "type": "object",
  "properties": {
    "text": {"type": "string"}
  }
}
```

#### 2. Text to Audio

**POST** `/text-to-audio`

Convert text to speech.

#### Request Body (application/json) - Schema: `TextToAudioJsonRequest`:
```json
{
  "type": "object",
  "required": ["user"],
  "properties": {
    "message_id": {
      "type": "string",
      "format": "uuid",
      "description": "Message ID (priority)."
    },
    "text": {
      "type": "string",
      "description": "Speech content."
    },
    "user": {"type": "string"},
    "streaming": {
      "type": "boolean",
      "default": false,
      "description": "If true, response will be a stream of audio chunks."
    }
  },
  "description": "Requires user. Provide message_id or text."
}
```

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

**Success (200)** - Schema: `AppInfoResponse`:
```json
{
  "type": "object",
  "properties": {
    "name": {"type": "string"},
    "description": {"type": "string"},
    "tags": {
      "type": "array",
      "items": {"type": "string"}
    }
  }
}
```

#### 2. Get Application Parameters Information

**GET** `/parameters`

Get application parameters.

#### Response

**Success (200)** - Schema: `ChatAppParametersResponse`:
```json
{
  "type": "object",
  "properties": {
    "opening_statement": {"type": "string"},
    "suggested_questions": {
      "type": "array",
      "items": {"type": "string"}
    },
    "suggested_questions_after_answer": {
      "type": "object",
      "properties": {
        "enabled": {"type": "boolean"}
      }
    },
    "speech_to_text": {
      "type": "object",
      "properties": {
        "enabled": {"type": "boolean"}
      }
    },
    "text_to_speech": {
      "type": "object",
      "properties": {
        "enabled": {"type": "boolean"},
        "voice": {"type": "string"},
        "language": {"type": "string"},
        "autoPlay": {
          "type": "string",
          "enum": ["enabled", "disabled"]
        }
      }
    },
    "retriever_resource": {
      "type": "object",
      "properties": {
        "enabled": {"type": "boolean"}
      }
    },
    "annotation_reply": {
      "type": "object",
      "properties": {
        "enabled": {"type": "boolean"}
      }
    },
    "user_input_form": {
      "type": "array",
      "items": {"$ref": "UserInputFormItem"}
    },
    "file_upload": {
      "type": "object",
      "properties": {
        "image": {
          "type": "object",
          "properties": {
            "enabled": {"type": "boolean"},
            "number_limits": {"type": "integer"},
            "detail": {"type": "string"},
            "transfer_methods": {
              "type": "array",
              "items": {
                "type": "string",
                "enum": ["remote_url", "local_file"]
              }
            }
          }
        }
      }
    },
    "system_parameters": {
      "type": "object",
      "properties": {
        "file_size_limit": {"type": "integer"},
        "image_file_size_limit": {"type": "integer"},
        "audio_file_size_limit": {"type": "integer"},
        "video_file_size_limit": {"type": "integer"}
      }
    }
  }
}
```

**UserInputFormItem Schema** (oneOf):
```json
{
  "type": "object",
  "oneOf": [
    {"$ref": "TextInputControlWrapper"},
    {"$ref": "ParagraphControlWrapper"},
    {"$ref": "SelectControlWrapper"}
  ]
}
```

**TextInputControlWrapper Schema**:
```json
{
  "type": "object",
  "properties": {
    "text-input": {"$ref": "TextInputControl"}
  },
  "required": ["text-input"]
}
```

**ParagraphControlWrapper Schema**:
```json
{
  "type": "object",
  "properties": {
    "paragraph": {"$ref": "ParagraphControl"}
  },
  "required": ["paragraph"]
}
```

**SelectControlWrapper Schema**:
```json
{
  "type": "object",
  "properties": {
    "select": {"$ref": "SelectControl"}
  },
  "required": ["select"]
}
```

**TextInputControl Schema**:
```json
{
  "type": "object",
  "required": ["label", "variable", "required"],
  "properties": {
    "label": {"type": "string"},
    "variable": {"type": "string"},
    "required": {"type": "boolean"},
    "default": {"type": "string"}
  }
}
```

**ParagraphControl Schema**:
```json
{
  "type": "object",
  "required": ["label", "variable", "required"],
  "properties": {
    "label": {"type": "string"},
    "variable": {"type": "string"},
    "required": {"type": "boolean"},
    "default": {"type": "string"}
  }
}
```

**SelectControl Schema**:
```json
{
  "type": "object",
  "required": ["label", "variable", "required", "options"],
  "properties": {
    "label": {"type": "string"},
    "variable": {"type": "string"},
    "required": {"type": "boolean"},
    "default": {"type": "string"},
    "options": {
      "type": "array",
      "items": {"type": "string"}
    }
  }
}
```

#### 3. Get Application Meta Information

**GET** `/meta`

Get application meta information (tool icons).

#### Response

**Success (200)** - Schema: `AppMetaResponse`:
```json
{
  "type": "object",
  "properties": {
    "tool_icons": {
      "type": "object",
      "additionalProperties": {
        "oneOf": [
          {
            "type": "string",
            "format": "url"
          },
          {"$ref": "ToolIconDetail"}
        ]
      }
    }
  }
}
```

**ToolIconDetail Schema**:
```json
{
  "type": "object",
  "properties": {
    "background": {"type": "string"},
    "content": {"type": "string"}
  }
}
```

#### 4. Get Application WebApp Settings

**GET** `/site`

Get WebApp settings.

#### Response

**Success (200)** - Schema: `WebAppSettingsResponse`:
```json
{
  "type": "object",
  "properties": {
    "title": {"type": "string"},
    "chat_color_theme": {"type": "string"},
    "chat_color_theme_inverted": {"type": "boolean"},
    "icon_type": {
      "type": "string",
      "enum": ["emoji", "image"]
    },
    "icon": {"type": "string"},
    "icon_background": {"type": "string"},
    "icon_url": {
      "type": "string",
      "format": "url",
      "nullable": true
    },
    "description": {"type": "string"},
    "copyright": {"type": "string"},
    "privacy_policy": {"type": "string"},
    "custom_disclaimer": {"type": "string"},
    "default_language": {"type": "string"},
    "show_workflow_steps": {"type": "boolean"},
    "use_icon_as_answer_icon": {"type": "boolean"}
  }
}
```

### Annotations

#### 1. Get Annotation List

**GET** `/apps/annotations`

Get annotation list.

#### Query Parameters
- `page` (integer, optional): Page number, default: 1
- `limit` (integer, optional): Number of items per page, default: 20, min: 1, max: 100

#### Response

**Success (200)** - Schema: `AnnotationListResponse`:
```json
{
  "type": "object",
  "properties": {
    "data": {
      "type": "array",
      "items": {"$ref": "AnnotationItem"}
    },
    "has_more": {"type": "boolean"},
    "limit": {"type": "integer"},
    "total": {"type": "integer"},
    "page": {"type": "integer"}
  }
}
```

**AnnotationItem Schema**:
```json
{
  "type": "object",
  "properties": {
    "id": {
      "type": "string",
      "format": "uuid"
    },
    "question": {"type": "string"},
    "answer": {"type": "string"},
    "hit_count": {"type": "integer"},
    "created_at": {
      "type": "integer",
      "format": "int64"
    }
  }
}
```

#### 2. Create Annotation

**POST** `/apps/annotations`

Create annotation.

#### Request Body (application/json) - Schema: `CreateAnnotationRequest`:
```json
{
  "type": "object",
  "required": ["question", "answer"],
  "properties": {
    "question": {"type": "string"},
    "answer": {"type": "string"}
  }
}
```

#### Response

**Success (200/201)** - Schema: `AnnotationItem`:
```json
{
  "type": "object",
  "properties": {
    "id": {
      "type": "string",
      "format": "uuid"
    },
    "question": {"type": "string"},
    "answer": {"type": "string"},
    "hit_count": {"type": "integer"},
    "created_at": {
      "type": "integer",
      "format": "int64"
    }
  }
}
```

#### 3. Update Annotation

**PUT** `/apps/annotations/{annotation_id}`

Update annotation.

#### Path Parameters
- `annotation_id` (string, required): Annotation ID (UUID)

#### Request Body (application/json) - Schema: `UpdateAnnotationRequest`:
```json
{
  "type": "object",
  "required": ["question", "answer"],
  "properties": {
    "question": {"type": "string"},
    "answer": {"type": "string"}
  }
}
```

#### Response

**Success (200)** - Schema: `AnnotationItem`:
```json
{
  "type": "object",
  "properties": {
    "id": {
      "type": "string",
      "format": "uuid"
    },
    "question": {"type": "string"},
    "answer": {"type": "string"},
    "hit_count": {"type": "integer"},
    "created_at": {
      "type": "integer",
      "format": "int64"
    }
  }
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

#### Request Body (application/json) - Schema: `InitialAnnotationReplySettingsRequest`:
```json
{
  "type": "object",
  "required": ["score_threshold"],
  "properties": {
    "embedding_provider_name": {
      "type": "string",
      "nullable": true
    },
    "embedding_model_name": {
      "type": "string",
      "nullable": true
    },
    "score_threshold": {
      "type": "number",
      "format": "float"
    }
  }
}
```

#### Response

**Success (200/202)** - Schema: `InitialAnnotationReplySettingsResponse`:
```json
{
  "type": "object",
  "properties": {
    "job_id": {
      "type": "string",
      "format": "uuid"
    },
    "job_status": {"type": "string"}
  }
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

**Success (200)** - Schema: `InitialAnnotationReplySettingsStatusResponse`:
```json
{
  "type": "object",
  "properties": {
    "job_id": {
      "type": "string",
      "format": "uuid"
    },
    "job_status": {"type": "string"},
    "error_msg": {
      "type": "string",
      "nullable": true
    }
  }
}
```

## Error Responses

All APIs may return the following error responses - Schema: `ErrorResponse`:

```json
{
  "type": "object",
  "properties": {
    "status": {
      "type": "integer",
      "nullable": true
    },
    "code": {
      "type": "string",
      "nullable": true
    },
    "message": {"type": "string"}
  }
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