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

## APIs

### Completion

#### 1. Create Completion Message

**POST** `/completion-messages`

Send a request to the text generation application.

#### Request Body (application/json)
```json
{
  "inputs": {
    "type": "object",
    "required": true,
    "description": "Variable values defined by the App. Contains multiple key/value pairs.",
    "properties": {
      "query": {
        "type": "string",
        "required": true,
        "description": "The input text, the content to be processed."
      }
    },
    "additionalProperties": {
      "type": "string"
    }
  },
  "response_mode": {
    "type": "string",
    "description": "The mode of response return.",
    "enum": ["streaming", "blocking"]
  },
  "user": {
    "type": "string",
    "description": "User identifier, used to define the identity of the end-user for retrieval and statistics."
  },
  "files": {
    "type": "array",
    "items": {
      "$ref": "InputFileObject"
    },
    "description": "File list, suitable for inputting files (images) combined with text understanding."
  }
}
```

#### InputFileObject
```json
{
  "type": {
    "type": "string",
    "enum": ["image"],
    "required": true,
    "description": "Supported type: image (currently only supports image type)."
  },
  "transfer_method": {
    "type": "string",
    "enum": ["remote_url", "local_file"],
    "required": true,
    "description": "Transfer method, remote_url for image URL / local_file for file upload"
  },
  "url": {
    "type": "string",
    "format": "url",
    "description": "Image URL (when transfer_method is remote_url)"
  },
  "upload_file_id": {
    "type": "string",
    "description": "Uploaded file ID (when transfer_method is local_file)"
  }
}
```

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
```json
{
  "event": {
    "type": "string",
    "description": "Event type, typically 'message' for blocking mode",
    "example": "message"
  },
  "message_id": {
    "type": "string",
    "format": "uuid",
    "description": "Unique message ID"
  },
  "mode": {
    "type": "string",
    "description": "App mode, fixed as 'completion'",
    "example": "completion"
  },
  "answer": {
    "type": "string",
    "description": "Complete response content"
  },
  "metadata": {
    "type": "object",
    "properties": {
      "usage": {
        "type": "object",
        "properties": {
          "prompt_tokens": "integer",
          "prompt_unit_price": "string (decimal)",
          "prompt_price_unit": "string (decimal)",
          "prompt_price": "string (decimal)",
          "completion_tokens": "integer",
          "completion_unit_price": "string (decimal)",
          "completion_price_unit": "string (decimal)",
          "completion_price": "string (decimal)",
          "total_tokens": "integer",
          "total_price": "string (decimal)",
          "currency": "string",
          "latency": "number (double)"
        }
      },
      "retriever_resources": {
        "type": "array",
        "items": {
          "type": "object",
          "properties": {
            "document_id": "string",
            "segment_id": "string",
            "score": "number (float)",
            "content": "string"
          }
        },
        "description": "Citation and Attribution List"
      }
    }
  },
  "created_at": {
    "type": "integer",
    "format": "int64",
    "description": "Message creation timestamp (Unix epoch)",
    "example": 1705395332
  }
}
```

For **streaming mode** (text/event-stream):
Server-Sent Events with the following event types:

#### Stream Event Types
- `message` - LLM returns text chunk
- `message_end` - Message end event with metadata  
- `tts_message` - TTS audio stream event (base64 encoded)
- `tts_message_end` - TTS audio stream end
- `message_replace` - Content replacement event
- `error` - Error event
- `ping` - Keep-alive ping every 10 seconds

#### Stream Event Structure
```json
{
  "event": {
    "type": "string",
    "enum": ["message", "message_end", "tts_message", "tts_message_end", "message_replace", "error", "ping"],
    "description": "The type of event"
  },
  "task_id": {
    "type": "string",
    "format": "uuid",
    "description": "Task ID, used for request tracking and Stop Generate API. Not present in 'ping' event"
  },
  "message_id": {
    "type": "string",
    "format": "uuid",
    "description": "Unique message ID. Not present in 'ping' event"
  },
  "created_at": {
    "type": "integer",
    "format": "int64",
    "description": "Creation timestamp (Unix epoch). Not present in 'ping' event",
    "example": 1705395332
  }
}
```

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
```json
{
  "user": {
    "type": "string",
    "required": true,
    "description": "User identifier, must be consistent with the user in send message interface."
  }
}
```

#### Example Request
```json
{
  "user": "abc-123"
}
```

#### Response

**Success (200)**
```json
{
  "result": "success"
}
```

### Files

#### 1. File Upload

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

#### Example Request
```bash
curl -X POST 'https://api.dify.ai/v1/files/upload' \
  -H 'Authorization: Bearer {API_KEY}' \
  -F 'file=@/path/to/image.png' \
  -F 'user=abc-123'
```

#### Response

**Success (200)**
```json
{
  "id": {
    "type": "string",
    "format": "uuid",
    "description": "ID of the uploaded file"
  },
  "name": {
    "type": "string",
    "description": "File name"
  },
  "size": {
    "type": "integer",
    "description": "File size (bytes)"
  },
  "extension": {
    "type": "string",
    "description": "File extension"
  },
  "mime_type": {
    "type": "string",
    "description": "File mime-type"
  },
  "created_by": {
    "type": "string",
    "format": "uuid",
    "description": "End-user ID who uploaded the file"
  },
  "created_at": {
    "type": "integer",
    "format": "int64",
    "description": "Creation timestamp (Unix epoch)",
    "example": 1577836800
  }
}
```

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
```json
{
  "rating": {
    "type": "string",
    "enum": ["like", "dislike", null],
    "nullable": true,
    "description": "Upvote as 'like', downvote as 'dislike', revoke as null."
  },
  "user": {
    "type": "string",
    "required": true,
    "description": "User identifier, must be unique within the application."
  },
  "content": {
    "type": "string",
    "description": "The specific content of message feedback."
  }
}
```

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
```json
{
  "result": "success"
}
```

#### 2. Get Application Feedbacks

**GET** `/app/feedbacks`

Get application's feedbacks.

#### Query Parameters
- `page` (integer, optional): Pagination page number, default 1
- `limit` (integer, optional): Records per page, default 20

#### Response

**Success (200)**
```json
{
  "data": {
    "type": "array",
    "items": {
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
        "content": {
          "type": "string"
        },
        "from_source": {
          "type": "string"
        },
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
    },
    "description": "List of application feedback items"
  }
}
```

### TTS

#### 1. Text to Audio

**POST** `/text-to-audio`

Convert text to speech.

#### Request Body (application/json)
```json
{
  "message_id": {
    "type": "string",
    "format": "uuid",
    "description": "Message ID for Dify-generated text. Takes priority over text field."
  },
  "text": {
    "type": "string",
    "description": "Speech generated content. Used if message_id is not provided."
  },
  "user": {
    "type": "string",
    "required": true,
    "description": "User identifier, must be unique within the app."
  }
}
```

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
- Content-Type: `audio/wav` or `audio/mp3`
- Body: Binary audio file

#### Response Headers
```
Content-Type: audio/wav (or audio/mp3 depending on server configuration)
```

### Application

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
    "items": {
      "type": "string"
    },
    "description": "Application tags"
  }
}
```

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

#### User Input Form Control Types

1. **Text Input Control** - Single line text input
2. **Paragraph Control** - Multi-line text input  
3. **Select Control** - Dropdown selection with predefined options

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

#### Icon Type Enum
- `emoji` - Icon is an emoji symbol
- `image` - Icon is an image URL

## Error Response Format

All error responses follow this structure:

```json
{
  "status": {
    "type": "integer",
    "description": "HTTP status code"
  },
  "code": {
    "type": "string",
    "description": "Error code specific to the application"
  },
  "message": {
    "type": "string",
    "description": "A human-readable error message"
  }
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