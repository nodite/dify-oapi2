# Completion APIs

This document covers all completion APIs based on the official Dify OpenAPI specification (v1.0.0). The text generation application offers non-session support and is ideal for translation, article writing, summarization AI, and more. Completion APIs provide text generation, file upload, feedback management, text-to-speech, and application configuration capabilities for AI applications.

## Base URL

```
https://api.dify.ai/v1
```

**Note**: Replace with the actual API base URL provided for your application (e.g., from `props.appDetail.api_base_url`).

## Authentication

Service API uses `API-Key` for authentication. **It is strongly recommended that developers store the `API-Key` in the backend rather than sharing or storing it on the client side to prevent `API-Key` leakage and financial loss.**

All API requests should include your `API-Key` in the **`Authorization`** HTTP Header:

```
Authorization: Bearer {API_KEY}
```

## API Overview

The Completion API provides 9 endpoints organized into 5 main categories:

**Total Endpoints**: 9 APIs across 5 categories

### Completion (2 APIs)
- **POST** `/completion-messages` - Create Completion Message
- **POST** `/completion-messages/{task_id}/stop` - Stop Generate

### Files (1 API)
- **POST** `/files/upload` - File Upload

### Feedback (2 APIs)
- **POST** `/messages/{message_id}/feedbacks` - Message Feedback
- **GET** `/app/feedbacks` - Get Application Feedbacks

### TTS (1 API)
- **POST** `/text-to-audio` - Text to Audio

### Application (3 APIs)
- **GET** `/info` - Get Application Basic Information
- **GET** `/parameters` - Get Application Parameters Information
- **GET** `/site` - Get Application WebApp Settings

## Data Types

### CompletionRequest
```typescript
interface CompletionRequest {
  inputs: {
    query: string;  // Required: The input text content to be processed
    [key: string]: string;  // Additional variable values defined by the App
  };
  response_mode?: "streaming" | "blocking";  // Default: streaming
  user?: string;  // User identifier for retrieval and statistics
  files?: InputFileObject[];  // File list for multimodal understanding
}
```

### InputFileObject
```typescript
interface InputFileObject {
  type: "image";  // Currently only supports image type
  transfer_method: "remote_url" | "local_file";
  url?: string;  // Required when transfer_method is "remote_url"
  upload_file_id?: string;  // Required when transfer_method is "local_file"
}
```

### CompletionResponse (Blocking Mode)
```typescript
interface CompletionResponse {
  event: string;  // Typically "message" for blocking mode
  message_id: string;  // UUID format
  mode: string;  // Fixed as "completion"
  answer: string;  // Complete response content
  metadata: {
    usage: Usage;
    retriever_resources?: RetrieverResource[];
  };
  created_at: number;  // Unix timestamp
}
```

### Usage
```typescript
interface Usage {
  prompt_tokens: number;
  prompt_unit_price: string;  // Decimal format
  prompt_price_unit: string;  // Decimal format
  prompt_price: string;  // Decimal format
  completion_tokens: number;
  completion_unit_price: string;  // Decimal format
  completion_price_unit: string;  // Decimal format
  completion_price: string;  // Decimal format
  total_tokens: number;
  total_price: string;  // Decimal format
  currency: string;  // e.g., "USD"
  latency: number;  // Double format
}
```

### RetrieverResource
```typescript
interface RetrieverResource {
  document_id: string;
  segment_id: string;
  score: number;  // Float format
  content: string;
}
```

### Stream Event Types
```typescript
type StreamEvent = 
  | StreamEventMessage
  | StreamEventMessageEnd
  | StreamEventTtsMessage
  | StreamEventTtsMessageEnd
  | StreamEventMessageReplace
  | StreamEventError
  | StreamEventPing;

interface StreamEventMessage {
  event: "message";
  task_id: string;  // UUID format
  message_id: string;  // UUID format
  answer: string;  // Text chunk content
  created_at: number;  // Unix timestamp
}

interface StreamEventMessageEnd {
  event: "message_end";
  task_id: string;
  message_id: string;
  metadata: {
    usage: Usage;
    retriever_resources?: RetrieverResource[];
  };
}

interface StreamEventTtsMessage {
  event: "tts_message";
  task_id: string;
  message_id: string;
  audio: string;  // Base64 encoded audio content
  created_at: number;
}

interface StreamEventTtsMessageEnd {
  event: "tts_message_end";
  task_id: string;
  message_id: string;
  audio: string;  // Empty string for end event
  created_at: number;
}

interface StreamEventMessageReplace {
  event: "message_replace";
  task_id: string;
  message_id: string;
  answer: string;  // Replacement content
  created_at: number;
}

interface StreamEventError {
  event: "error";
  task_id: string;
  message_id: string;
  status: number;  // HTTP status code
  code: string;  // Error code
  message: string;  // Error message
}

interface StreamEventPing {
  event: "ping";
  // No other fields for ping events
}
```

### FileUploadResponse
```typescript
interface FileUploadResponse {
  id: string;  // UUID format
  name: string;
  size: number;  // File size in bytes
  extension: string;
  mime_type: string;
  created_by: string;  // UUID format
  created_at: number;  // Unix timestamp
}
```

### MessageFeedbackRequest
```typescript
interface MessageFeedbackRequest {
  rating?: "like" | "dislike" | null;  // Nullable
  user: string;  // Required
  content?: string;
}
```

### FeedbackItem
```typescript
interface FeedbackItem {
  id: string;  // UUID format
  app_id: string;  // UUID format
  conversation_id: string;  // UUID format
  message_id: string;  // UUID format
  rating: "like" | "dislike" | null;
  content: string;
  from_source: string;
  from_end_user_id: string;  // UUID format
  from_account_id: string | null;  // UUID format, nullable
  created_at: string;  // ISO date-time format
  updated_at: string;  // ISO date-time format
}
```

### TextToAudioRequest
```typescript
interface TextToAudioRequest {
  message_id?: string;  // UUID format, takes priority over text
  text?: string;  // Used if message_id not provided
  user: string;  // Required
}
// Note: At least one of message_id or text must be provided
```

### AppInfoResponse
```typescript
interface AppInfoResponse {
  name: string;
  description: string;
  tags: string[];
}
```

### AppParametersResponse
```typescript
interface AppParametersResponse {
  opening_statement: string;
  suggested_questions: string[];
  suggested_questions_after_answer: {
    enabled: boolean;
  };
  speech_to_text: {
    enabled: boolean;
  };
  retriever_resource: {
    enabled: boolean;
  };
  annotation_reply: {
    enabled: boolean;
  };
  user_input_form: UserInputFormItem[];
  file_upload: {
    image: {
      enabled: boolean;
      number_limits: number;  // Default: 3
      detail: string;  // e.g., "high"
      transfer_methods: ("remote_url" | "local_file")[];
    };
  };
  system_parameters: {
    file_size_limit: number;  // MB
    image_file_size_limit: number;  // MB
    audio_file_size_limit: number;  // MB
    video_file_size_limit: number;  // MB
  };
}
```

### UserInputFormItem
```typescript
type UserInputFormItem = 
  | { "text-input": TextInputControl }
  | { paragraph: ParagraphControl }
  | { select: SelectControl };

interface TextInputControl {
  label: string;
  variable: string;
  required: boolean;
  default?: string;
}

interface ParagraphControl {
  label: string;
  variable: string;
  required: boolean;
  default?: string;
}

interface SelectControl {
  label: string;
  variable: string;
  required: boolean;
  default?: string;
  options: string[];
}
```

### WebAppSettingsResponse
```typescript
interface WebAppSettingsResponse {
  title: string;
  chat_color_theme: string;  // Hex format (e.g., #RRGGBB)
  chat_color_theme_inverted: boolean;
  icon_type: "emoji" | "image";
  icon: string;  // Emoji symbol or image URL
  icon_background: string;  // Hex format
  icon_url: string | null;  // URL format, nullable
  description: string;
  copyright: string;
  privacy_policy: string;
  custom_disclaimer: string;
  default_language: string;  // e.g., "en-US"
  show_workflow_steps: boolean;
  use_icon_as_answer_icon: boolean;
}
```

### ErrorResponse
```typescript
interface ErrorResponse {
  status: number;  // HTTP status code
  code: string;  // Application-specific error code
  message: string;  // Human-readable error message
}
```

## APIs

### Completion

#### 1. Create Completion Message

**POST** `/completion-messages`

Send a request to the text generation application.

#### Request Body (application/json)

**Schema**: `CompletionRequest`

**Required Fields**:
- `inputs` (object, required): Variable values defined by the App
  - `query` (string, required): The input text content to be processed
  - Additional properties (string): Other variable values as key/value pairs

**Optional Fields**:
- `response_mode` (string): Response mode - "streaming" (default) or "blocking"
- `user` (string): User identifier for retrieval and statistics
- `files` (array): File list for multimodal understanding (InputFileObject[])

**InputFileObject Schema**:
- `type` (string, required): "image" (currently only supports image type)
- `transfer_method` (string, required): "remote_url" or "local_file"
- `url` (string): Image URL (required when transfer_method is "remote_url")
- `upload_file_id` (string): Uploaded file ID (required when transfer_method is "local_file")

**Validation Rules**:
- For `remote_url` transfer method: `url` is required, `upload_file_id` must not be provided
- For `local_file` transfer method: `upload_file_id` is required, `url` must not be provided
- Files are only supported when the model has Vision capability

#### Example Requests

**Streaming Mode Example**
```json
{
  "inputs": {
    "query": "Hello, world!"
  },
  "response_mode": "streaming",
  "user": "abc-123"
}
```

**Blocking Mode Example**
```json
{
  "inputs": {
    "query": "Translate this to French: Hello"
  },
  "response_mode": "blocking",
  "user": "def-456"
}
```

**With File Upload Example**
```json
{
  "inputs": {
    "query": "What's in this image?"
  },
  "response_mode": "streaming",
  "user": "abc-123",
  "files": [
    {
      "type": "image",
      "transfer_method": "remote_url",
      "url": "https://example.com/image.png"
    }
  ]
}
```

#### Response

**Success (200)**

For **blocking mode** (application/json):

**Schema**: `CompletionResponse`

**Response Fields**:
- `event` (string): Event type, typically "message" for blocking mode
- `message_id` (string): Unique message ID (UUID format)
- `mode` (string): App mode, fixed as "completion"
- `answer` (string): Complete response content
- `metadata` (object):
  - `usage` (Usage): Token usage and pricing information
  - `retriever_resources` (RetrieverResource[], optional): Citation and attribution list
- `created_at` (number): Message creation timestamp (Unix epoch)

**Usage Object**:
- `prompt_tokens` (number): Number of tokens in the prompt
- `prompt_unit_price` (string): Unit price for prompt tokens (decimal)
- `prompt_price_unit` (string): Price unit for prompt (decimal)
- `prompt_price` (string): Total price for prompt tokens (decimal)
- `completion_tokens` (number): Number of tokens in the completion
- `completion_unit_price` (string): Unit price for completion tokens (decimal)
- `completion_price_unit` (string): Price unit for completion (decimal)
- `completion_price` (string): Total price for completion tokens (decimal)
- `total_tokens` (number): Total number of tokens
- `total_price` (string): Total price (decimal)
- `currency` (string): Currency code (e.g., "USD")
- `latency` (number): Response latency in seconds (double)

**RetrieverResource Object**:
- `document_id` (string): ID of the retrieved document
- `segment_id` (string): ID of the specific segment within the document
- `score` (number): Relevance score of the resource (float)
- `content` (string): Content snippet from the resource

For **streaming mode** (text/event-stream):

**Content-Type**: `text/event-stream`
**Format**: Server-Sent Events (SSE)

**Schema**: Stream of `ChunkCompletionEvent` objects

#### Stream Event Types

1. **message** - LLM returns text chunk
   - `event`: "message"
   - `task_id` (string): Task ID (UUID)
   - `message_id` (string): Message ID (UUID)
   - `answer` (string): Text chunk content
   - `created_at` (number): Unix timestamp

2. **message_end** - Message end event with metadata
   - `event`: "message_end"
   - `task_id` (string): Task ID (UUID)
   - `message_id` (string): Message ID (UUID)
   - `metadata` (object): Usage and retriever resources

3. **tts_message** - TTS audio stream event
   - `event`: "tts_message"
   - `task_id` (string): Task ID (UUID)
   - `message_id` (string): Message ID (UUID)
   - `audio` (string): Base64 encoded audio content
   - `created_at` (number): Unix timestamp

4. **tts_message_end** - TTS audio stream end
   - `event`: "tts_message_end"
   - `task_id` (string): Task ID (UUID)
   - `message_id` (string): Message ID (UUID)
   - `audio` (string): Empty string for end event
   - `created_at` (number): Unix timestamp

5. **message_replace** - Content replacement event
   - `event`: "message_replace"
   - `task_id` (string): Task ID (UUID)
   - `message_id` (string): Message ID (UUID)
   - `answer` (string): Replacement content
   - `created_at` (number): Unix timestamp

6. **error** - Error event
   - `event`: "error"
   - `task_id` (string): Task ID (UUID)
   - `message_id` (string): Message ID (UUID)
   - `status` (number): HTTP status code
   - `code` (string): Error code
   - `message` (string): Error message

7. **ping** - Keep-alive ping every 10 seconds
   - `event`: "ping"
   - No other fields

**Event Format**: Each event is prefixed with `data: ` and suffixed with `\n\n`

**Error Responses**
- **400**: Bad Request
  - `invalid_param` - Abnormal parameter input
  - `app_unavailable` - App configuration unavailable
  - `provider_not_initialize` - No available model credential configuration
  - `provider_quota_exceeded` - Model invocation quota insufficient
  - `model_currently_not_support` - Current model unavailable
  - `completion_request_error` - Text generation failed
- **404**: Conversation does not exist
- **500**: Internal server error

#### 2. Stop Generate

**POST** `/completion-messages/{task_id}/stop`

Stops a generation task. Only supported in streaming mode.

#### Path Parameters
- `task_id` (string, required): Task ID from streaming chunk return

#### Request Body (application/json)

**Required Fields**:
- `user` (string, required): User identifier
  - Must be consistent with the user in send message interface

#### Example Request
```json
{
  "user": "abc-123"
}
```

#### Response

**Success (200)**

**Response Fields**:
- `result` (string): "success" when stop request is successful

### Files

#### 1. File Upload

**POST** `/files/upload`

Upload a file (currently only images are supported) for use when sending messages, enabling multimodal understanding of images and text.

#### Request Body (multipart/form-data)

**Required Fields**:
- `file` (binary, required): The file to be uploaded
  - **Supported formats**: png, jpg, jpeg, webp, gif
  - **Type**: Binary file data
- `user` (string, required): User identifier
  - Must be unique within the application
  - Defined by developer's rules

#### Example Request
```bash
curl -X POST 'https://api.dify.ai/v1/files/upload' \
  -H 'Authorization: Bearer {API_KEY}' \
  -F 'file=@/path/to/image.png' \
  -F 'user=abc-123'
```

#### Response

**Success (200)**

**Schema**: `FileUploadResponse`

**Response Fields**:
- `id` (string): ID of the uploaded file (UUID format)
- `name` (string): Original file name
- `size` (number): File size in bytes
- `extension` (string): File extension (e.g., "png")
- `mime_type` (string): File MIME type (e.g., "image/png")
- `created_by` (string): End-user ID who uploaded the file (UUID format)
- `created_at` (number): Creation timestamp (Unix epoch)

#### Example Response
```json
{
  "id": "72fa9618-8f89-4a37-9b33-7e1178a24a67",
  "name": "example.png",
  "size": 1024,
  "extension": "png",
  "mime_type": "image/png",
  "created_by": "6ad1ab0a-73ff-4ac1-b9e4-cdb312f71f13",
  "created_at": 1577836800
}
```

**Error Responses**
- **400**: Bad Request
  - `no_file_uploaded` - A file must be provided
  - `too_many_files` - Currently only one file is accepted
  - `unsupported_preview` - The file does not support preview
  - `unsupported_estimate` - The file does not support estimation
- **413**: File Too Large
  - `file_too_large` - The file is too large
- **415**: Unsupported Media Type
  - `unsupported_file_type` - Unsupported extension. Currently only document files are accepted
- **503**: Service Unavailable
  - `s3_connection_failed` - Unable to connect to S3 service
  - `s3_permission_denied` - No permission to upload files to S3
  - `s3_file_too_large` - File exceeds S3 size limit
- **500**: Internal server error

### Feedback

#### 1. Message Feedback

**POST** `/messages/{message_id}/feedbacks`

End-users can provide feedback messages, facilitating application developers to optimize expected outputs.

#### Path Parameters
- `message_id` (string, required): Message ID for which feedback is being provided

#### Request Body (application/json)

**Schema**: `MessageFeedbackRequest`

**Required Fields**:
- `user` (string, required): User identifier, must be unique within the application

**Optional Fields**:
- `rating` (string, nullable): Feedback rating
  - Values: "like", "dislike", or null
  - "like" for upvote, "dislike" for downvote, null to revoke
- `content` (string): Specific content of message feedback

#### Example Request
```json
{
  "rating": "like",
  "user": "abc-123",
  "content": "message feedback information"
}
```

#### Response

**Success (200)**

**Response Fields**:
- `result` (string): "success" when feedback is submitted successfully

#### 2. Get Application Feedbacks

**GET** `/app/feedbacks`

Get application's feedbacks.

#### Query Parameters
- `page` (integer, optional): Pagination page number, default 1
- `limit` (integer, optional): Records per page, default 20

#### Response

**Success (200)**

**Schema**: `AppFeedbacksResponse`

**Response Fields**:
- `data` (FeedbackItem[]): List of application feedback items

**FeedbackItem Fields**:
- `id` (string): Feedback ID (UUID format)
- `app_id` (string): Application ID (UUID format)
- `conversation_id` (string): Conversation ID (UUID format)
- `message_id` (string): Message ID (UUID format)
- `rating` (string, nullable): Feedback rating ("like", "dislike", or null)
- `content` (string): Feedback content
- `from_source` (string): Source of the feedback
- `from_end_user_id` (string): End-user ID (UUID format)
- `from_account_id` (string, nullable): Account ID (UUID format, nullable)
- `created_at` (string): Creation timestamp (ISO date-time format)
- `updated_at` (string): Update timestamp (ISO date-time format)

### TTS

#### 1. Text to Audio

**POST** `/text-to-audio`

Convert text to speech.

#### Request Body (application/json)

**Schema**: `TextToAudioRequest`

**Required Fields**:
- `user` (string, required): User identifier, must be unique within the app

**Optional Fields** (at least one required):
- `message_id` (string): Message ID for Dify-generated text (UUID format)
  - Takes priority over text field if both provided
  - Used to look up corresponding content for synthesis
- `text` (string): Speech generated content
  - Used if message_id is not provided or not found

**Validation**: At least one of `message_id` or `text` must be provided

#### Example Request
```json
{
  "message_id": "5ad4cb98-f0c7-4085-b384-88c403be6290",
  "text": "Hello Dify",
  "user": "abc-123"
}
```

#### Response

**Success (200)**

**Content-Type**: `audio/wav` or `audio/mp3` (depending on server configuration)
**Body**: Binary audio file data

**Response Headers**:
- `Content-Type`: "audio/wav" or "audio/mp3"

### Application

#### 1. Get Application Basic Information

**GET** `/info`

Used to get basic information about this application.

#### Response

**Success (200)**

**Schema**: `AppInfoResponse`

**Response Fields**:
- `name` (string): Application name
- `description` (string): Application description
- `tags` (string[]): Application tags

#### 2. Get Application Parameters Information

**GET** `/parameters`

Used at the start of entering the page to obtain information such as features, input parameter names, types, and default values.

#### Response

**Success (200)**
```json
{
  "opening_statement": {
    "type": "string",
    "description": "Opening statement"
  },
  "suggested_questions": {
    "type": "array",
    "items": {
      "type": "string"
    },
    "description": "List of suggested questions for the opening"
  },
  "suggested_questions_after_answer": {
    "type": "object",
    "properties": {
      "enabled": {
        "type": "boolean",
        "description": "Whether suggesting questions after an answer is enabled"
      }
    }
  },
  "speech_to_text": {
    "type": "object",
    "properties": {
      "enabled": {
        "type": "boolean",
        "description": "Whether speech to text is enabled"
      }
    }
  },
  "retriever_resource": {
    "type": "object",
    "properties": {
      "enabled": {
        "type": "boolean",
        "description": "Whether citation and attribution (retriever resource) is enabled"
      }
    }
  },
  "annotation_reply": {
    "type": "object",
    "properties": {
      "enabled": {
        "type": "boolean",
        "description": "Whether annotation reply is enabled"
      }
    }
  },
  "user_input_form": {
    "type": "array",
    "items": {
      "oneOf": [
        {
          "type": "object",
          "properties": {
            "text-input": {
              "type": "object",
              "properties": {
                "label": {
                  "type": "string",
                  "description": "Variable display label name"
                },
                "variable": {
                  "type": "string",
                  "description": "Variable ID"
                },
                "required": {
                  "type": "boolean",
                  "description": "Whether it is required"
                },
                "default": {
                  "type": "string",
                  "description": "Default value"
                }
              },
              "required": ["label", "variable", "required"]
            }
          },
          "required": ["text-input"]
        },
        {
          "type": "object",
          "properties": {
            "paragraph": {
              "type": "object",
              "properties": {
                "label": {
                  "type": "string",
                  "description": "Variable display label name"
                },
                "variable": {
                  "type": "string",
                  "description": "Variable ID"
                },
                "required": {
                  "type": "boolean",
                  "description": "Whether it is required"
                },
                "default": {
                  "type": "string",
                  "description": "Default value"
                }
              },
              "required": ["label", "variable", "required"]
            }
          },
          "required": ["paragraph"]
        },
        {
          "type": "object",
          "properties": {
            "select": {
              "type": "object",
              "properties": {
                "label": {
                  "type": "string",
                  "description": "Variable display label name"
                },
                "variable": {
                  "type": "string",
                  "description": "Variable ID"
                },
                "required": {
                  "type": "boolean",
                  "description": "Whether it is required"
                },
                "default": {
                  "type": "string",
                  "description": "Default value"
                },
                "options": {
                  "type": "array",
                  "items": {
                    "type": "string"
                  },
                  "description": "Option values"
                }
              },
              "required": ["label", "variable", "required", "options"]
            }
          },
          "required": ["select"]
        }
      ]
    },
    "description": "User input form configuration"
  },
  "file_upload": {
    "type": "object",
    "description": "File upload configuration",
    "properties": {
      "image": {
        "type": "object",
        "description": "Image settings. Currently only supports image types: png, jpg, jpeg, webp, gif",
        "properties": {
          "enabled": {
            "type": "boolean",
            "description": "Whether image upload is enabled"
          },
          "number_limits": {
            "type": "integer",
            "description": "Image number limit, default is 3"
          },
          "detail": {
            "type": "string",
            "description": "Detail level for image processing (e.g., 'high')"
          },
          "transfer_methods": {
            "type": "array",
            "items": {
              "type": "string",
              "enum": ["remote_url", "local_file"]
            },
            "description": "List of transfer methods, must choose at least one if enabled"
          }
        }
      }
    }
  },
  "system_parameters": {
    "type": "object",
    "description": "System parameters",
    "properties": {
      "file_size_limit": {
        "type": "integer",
        "description": "Document upload size limit (MB)"
      },
      "image_file_size_limit": {
        "type": "integer",
        "description": "Image file upload size limit (MB)"
      },
      "audio_file_size_limit": {
        "type": "integer",
        "description": "Audio file upload size limit (MB)"
      },
      "video_file_size_limit": {
        "type": "integer",
        "description": "Video file upload size limit (MB)"
      }
    }
  }
}
```

**User Input Form Control Types**:

1. **Text Input Control** (`text-input`): Single line text input
   - `label` (string): Variable display label name
   - `variable` (string): Variable ID
   - `required` (boolean): Whether it is required
   - `default` (string, optional): Default value

2. **Paragraph Control** (`paragraph`): Multi-line text input
   - `label` (string): Variable display label name
   - `variable` (string): Variable ID
   - `required` (boolean): Whether it is required
   - `default` (string, optional): Default value

3. **Select Control** (`select`): Dropdown selection with predefined options
   - `label` (string): Variable display label name
   - `variable` (string): Variable ID
   - `required` (boolean): Whether it is required
   - `default` (string, optional): Default value
   - `options` (string[]): Option values

#### 3. Get Application WebApp Settings

**GET** `/site`

Used to get the WebApp settings of the application.

#### Response

**Success (200)**
```json
{
  "title": {
    "type": "string",
    "description": "WebApp name"
  },
  "chat_color_theme": {
    "type": "string",
    "description": "Chat color theme, in hex format (e.g., #RRGGBB)"
  },
  "chat_color_theme_inverted": {
    "type": "boolean",
    "description": "Whether the chat color theme is inverted"
  },
  "icon_type": {
    "type": "string",
    "enum": ["emoji", "image"],
    "description": "Icon type"
  },
  "icon": {
    "type": "string",
    "description": "Icon. If it's 'emoji' type, it's an emoji symbol; if it's 'image' type, it's an image URL"
  },
  "icon_background": {
    "type": "string",
    "description": "Background color in hex format (e.g., #RRGGBB)"
  },
  "icon_url": {
    "type": "string",
    "format": "url",
    "nullable": true,
    "description": "Icon URL (likely refers to image type if icon field is just a name/id)"
  },
  "description": {
    "type": "string",
    "description": "Description"
  },
  "copyright": {
    "type": "string",
    "description": "Copyright information"
  },
  "privacy_policy": {
    "type": "string",
    "description": "Privacy policy link"
  },
  "custom_disclaimer": {
    "type": "string",
    "description": "Custom disclaimer"
  },
  "default_language": {
    "type": "string",
    "description": "Default language (e.g., en-US)"
  },
  "show_workflow_steps": {
    "type": "boolean",
    "description": "Whether to show workflow details"
  },
  "use_icon_as_answer_icon": {
    "type": "boolean",
    "description": "Whether to replace 🤖 in chat with the WebApp icon"
  }
}
```

**Icon Type Values**:
- `"emoji"` - Icon is an emoji symbol
- `"image"` - Icon is an image URL

## Error Response Format

**Schema**: `ErrorResponse`

All error responses follow this structure:

**Error Fields**:
- `status` (number): HTTP status code
- `code` (string): Error code specific to the application
- `message` (string): A human-readable error message

**Example**:
```json
{
  "status": 400,
  "code": "invalid_param",
  "message": "Abnormal parameter input"
}
```

## Response Mode Details

### Streaming Mode
- Returns `text/event-stream` content type
- Implements Server-Sent Events (SSE)
- Provides real-time typewriter-like output
- Supports stopping generation via Stop Generate API
- Recommended for better user experience

### Blocking Mode
- Returns `application/json` content type
- Returns complete result after execution
- May be interrupted after 100 seconds due to Cloudflare restrictions
- Suitable for shorter generation tasks

## File Upload Specifications

### Supported Image Types
- PNG (.png)
- JPEG (.jpg, .jpeg)
- WebP (.webp)
- GIF (.gif)

### Transfer Methods
- `remote_url` - Provide image URL
- `local_file` - Upload file via File Upload API

### File Upload Requirements
- Only one file per request
- File must be provided in multipart/form-data format
- User identifier is required for all uploads
- Files are associated with the uploading end-user only

## Usage Tracking

The API provides detailed usage information including:
- Token counts (prompt, completion, total)
- Pricing information (unit prices, total cost)
- Currency information
- Latency metrics

## Rate Limiting and Quotas

Applications may encounter quota limitations based on:
- Model provider quotas
- Application-specific limits
- User-specific restrictions

Monitor error codes like `provider_quota_exceeded` to handle quota issues appropriately.

## Vision Capability

File upload and multimodal understanding is available only when the model supports Vision capability. Check the model configuration to ensure Vision support before using file upload features.

## Text-to-Speech (TTS)

TTS functionality requires:
- Either `message_id` (from Dify-generated text) or `text` parameter
- `message_id` takes priority if both are provided
- User identifier is required for all TTS requests
- Returns binary audio data in WAV or MP3 format
- At least one of `message_id` or `text` must be provided, along with `user`

## Security Considerations

- **API Key Storage**: Store API keys on the server-side only
- **Authentication**: All endpoints require Bearer token authentication
- **User Isolation**: Files and feedback are isolated per end-user
- **Content Moderation**: Message replacement events handle flagged content

## Pagination

The `/app/feedbacks` endpoint supports pagination:
- `page`: Page number (default: 1)
- `limit`: Records per page (default: 20)

## Required Fields Summary

### Create Completion Message
- `inputs` (object, required)
  - `inputs.query` (string, required)

### File Upload
- `file` (binary, required)
- `user` (string, required)

### Message Feedback
- `user` (string, required)

### Text to Audio
- `user` (string, required)
- Either `message_id` or `text` (at least one required)

### Stop Generate
- `user` (string, required)

## API Characteristics

### Non-Session Support
Completion APIs are designed for stateless interactions and do not maintain conversation context between requests. Each request is independent.

### Ideal Use Cases
- Translation services
- Article writing assistance
- Text summarization
- Content generation
- Language processing tasks

### Model Support
- Vision capability required for file upload features
- TTS capability required for text-to-audio conversion
- Check model configuration for supported features

## Best Practices

1. **API Key Security**: Always store API keys server-side
2. **Error Handling**: Implement proper error handling for all error codes
3. **File Upload**: Validate file types and sizes before upload
4. **Streaming**: Use streaming mode for better user experience
5. **Rate Limiting**: Monitor quota usage and implement appropriate limits
6. **User Identification**: Ensure unique user identifiers across your application