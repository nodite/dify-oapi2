# Completion Application APIs

This document covers all text generation application APIs. Text generation applications have no conversation support and are suitable for translation, article writing, summarization AI, etc.

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

### 1. Send Message

**POST** `/completion-messages`

Sends a request to a text generation application.

#### Request Body
- `inputs` (object, optional): Allows passing values for variables defined in the App. The inputs parameter contains multiple key-value pairs, where each key corresponds to a specific variable and each value is the specific value of that variable. Text generation applications require at least one key-value pair.
  - `query` (string, required): User input text content
- `response_mode` (string, required): Response mode
  - `streaming`: Streaming mode (recommended). Implements typewriter-style streaming output based on SSE (Server-Sent Events)
  - `blocking`: Blocking mode, waits for execution to complete before returning results. (Requests may be interrupted if the process is lengthy). *Due to Cloudflare limitations, requests will be interrupted after 100 seconds without response.*
- `user` (string, required): User identifier, used to define the identity of the end user for retrieval and statistics. Defined by developers, must ensure user identifier is unique within the application.
- `files` (array[object], optional): Uploaded files
  - `type` (string): Supported types: image `image` (currently only supports image formats)
  - `transfer_method` (string): Transfer method:
    - `remote_url`: Image URL
    - `local_file`: Upload file
  - `url` (string): Image URL (only when transfer method is `remote_url`)
  - `upload_file_id` (string): Upload file ID (only when transfer method is `local_file`)

#### Response

When `response_mode` is `blocking`, returns ChatCompletionResponse object.
When `response_mode` is `streaming`, returns ChunkChatCompletionResponse object stream sequence.

##### ChatCompletionResponse

Returns complete App result, `Content-Type` is `application/json`.

- `message_id` (string): Message unique ID
- `mode` (string): App mode, fixed as completion
- `answer` (string): Complete response content
- `metadata` (object): Metadata
  - `usage` (Usage): Model usage information
  - `retriever_resources` (array[RetrieverResource]): Reference and attribution segment list
- `created_at` (int): Message creation timestamp, e.g., 1705395332

##### ChunkChatCompletionResponse

Returns App output streaming blocks, `Content-Type` is `text/event-stream`.
Each streaming block starts with data: and blocks are separated by `\n\n` (two newlines):

```
data: {"event": "message", "task_id": "900bbd43-dc0b-4383-a372-aa6e6c414227", "id": "663c5084-a254-4040-8ad3-51f2a3c1a77c", "answer": "Hi", "created_at": 1705398420}\n\n
```

Streaming blocks have different structures based on different `event` types:

- `event: message` - LLM returns text block event, i.e., complete text output in chunks
  - `task_id` (string): Task ID, used for request tracking and stop response interface below
  - `message_id` (string): Message unique ID
  - `answer` (string): LLM returned text block content
  - `created_at` (int): Creation timestamp, e.g., 1705395332

- `event: message_end` - Message end event, receiving this event means text streaming return has ended
  - `task_id` (string): Task ID, used for request tracking and stop response interface below
  - `message_id` (string): Message unique ID
  - `metadata` (object): Metadata
    - `usage` (Usage): Model usage information
    - `retriever_resources` (array[RetrieverResource]): Reference and attribution segment list

- `event: tts_message` - TTS audio stream event, i.e., speech synthesis output. Content is Mp3 format audio blocks, base64 encoded strings, can be decoded directly for playback. (Only available when auto-play is enabled)
  - `task_id` (string): Task ID, used for request tracking and stop response interface below
  - `message_id` (string): Message unique ID
  - `audio` (string): Audio blocks after speech synthesis using Base64 encoding, can be decoded directly and sent to player for playback
  - `created_at` (int): Creation timestamp, e.g., 1705395332

- `event: tts_message_end` - TTS audio stream end event, receiving this event means audio stream return has ended
  - `task_id` (string): Task ID, used for request tracking and stop response interface below
  - `message_id` (string): Message unique ID
  - `audio` (string): End event has no audio, so this is an empty string
  - `created_at` (int): Creation timestamp, e.g., 1705395332

- `event: message_replace` - Message content replacement event. When content review is enabled and review output content is enabled, if review conditions are met, this event will replace message content with preset reply
  - `task_id` (string): Task ID, used for request tracking and stop response interface below
  - `message_id` (string): Message unique ID
  - `answer` (string): Replacement content (directly replaces all LLM reply text)
  - `created_at` (int): Creation timestamp, e.g., 1705395332

- `event: error` - Exceptions during streaming output will be output as stream events, ending after receiving exception events
  - `task_id` (string): Task ID, used for request tracking and stop response interface below
  - `message_id` (string): Message unique ID
  - `status` (int): HTTP status code
  - `code` (string): Error code
  - `message` (string): Error message

- `event: ping` - Ping event every 10s to keep connection alive

#### Errors
- 404: Conversation does not exist
- 400, `invalid_param`: Invalid parameters
- 400, `app_unavailable`: App configuration unavailable
- 400, `provider_not_initialize`: No available model credential configuration
- 400, `provider_quota_exceeded`: Model call quota exceeded
- 400, `model_currently_not_support`: Current model unavailable
- 400, `completion_request_error`: Text generation failed
- 500: Internal server error

### 2. Upload File

**POST** `/files/upload`

Uploads files (currently only supports images) for use when sending messages, enabling multimodal image-text understanding.
Supports png, jpg, jpeg, webp, gif formats.
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

### 3. Stop Response

**POST** `/completion-messages/:task_id/stop`

Only supports streaming mode.

#### Path Parameters
- `task_id` (string, required): Task ID, can be obtained from streaming return Chunk

#### Request Body
- `user` (string, required): User identifier, used to define the identity of the end user, must be consistent with the user passed in the send message interface. API cannot access sessions created by WebApp.

#### Response
- `result` (string): Fixed return success

### 4. Message Feedback (Like)

**POST** `/messages/:message_id/feedbacks`

Message end user feedback, like, to help application developers optimize output expectations.

#### Path Parameters
- `message_id` (string, required): Message ID

#### Request Body
- `rating` (string, required): Like `like`, dislike `dislike`, cancel like `null`
- `user` (string, required): User identifier, defined by developers, must ensure user identifier is unique within the application
- `content` (string, optional): Specific information of message feedback

#### Response
- `result` (string): Fixed return success

### 5. Get Application Feedbacks

**GET** `/app/feedbacks`

Get application's feedbacks.

#### Query Parameters
- `page` (string, optional): Pagination, default: 1
- `limit` (string, optional): Records per page, default: 20

#### Response
- `data` (List): Return apps feedback list

### 6. Text to Audio

**POST** `/text-to-audio`

Text to speech.

#### Request Body
- `message_id` (str, optional): Dify generated text message, then directly pass the generated message-id, the backend will find the corresponding content through message_id and directly synthesize voice information. If both message_id and text are passed, message_id takes priority.
- `text` (str, optional): Voice generation content. If message-id is not passed, the content of this field will be used
- `user` (string, required): User identifier, defined by developers, must ensure user identifier is unique within the application

#### Response
Returns audio file with `Content-Type: audio/wav`

### 7. Get Application Basic Information

**GET** `/info`

Used to get basic information of the application.

#### Response
- `name` (string): Application name
- `description` (string): Application description
- `tags` (array[string]): Application tags
- `mode` (string): Application mode
- `author_name` (string): Author name

### 8. Get Application Parameters

**GET** `/parameters`

Used to get function switches, input parameter names, types and default values when entering the page.

#### Response
- `opening_statement` (string): Opening statement
- `suggested_questions` (array[string]): Opening suggested question list
- `suggested_questions_after_answer` (object): Enable suggested questions after answer
  - `enabled` (bool): Whether enabled
- `speech_to_text` (object): Speech to text
  - `enabled` (bool): Whether enabled
- `retriever_resource` (object): Reference and attribution
  - `enabled` (bool): Whether enabled
- `annotation_reply` (object): Annotation reply
  - `enabled` (bool): Whether enabled
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
    Currently only supports image types: `png`, `jpg`, `jpeg`, `webp`, `gif`
    - `enabled` (bool): Whether enabled
    - `number_limits` (int): Image quantity limit, default 3
    - `transfer_methods` (array[string]): Transfer method list, remote_url, local_file, must choose one
- `system_parameters` (object): System parameters
  - `file_size_limit` (int): Document upload size limit (MB)
  - `image_file_size_limit` (int): Image file upload size limit (MB)
  - `audio_file_size_limit` (int): Audio file upload size limit (MB)
  - `video_file_size_limit` (int): Video file upload size limit (MB)

### 9. Get Application WebApp Settings

**GET** `/site`

Used to get application's WebApp settings.

#### Response
- `title` (string): WebApp name
- `chat_color_theme` (string): Chat color theme, hex format
- `chat_color_theme_inverted` (bool): Whether chat color theme is inverted
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
- `use_icon_as_answer_icon` (bool): Whether to use WebApp icon to replace 🤖 in chat

### 10. Get Annotation List

**GET** `/apps/annotations`

#### Query Parameters
- `page` (string, optional): Page number
- `limit` (string, optional): Number per page

#### Response
```json
{
  "data": [
    {
      "id": "69d48372-ad81-4c75-9c46-2ce197b4d402",
      "question": "What is your name?",
      "answer": "I am Dify.",
      "hit_count": 0,
      "created_at": 1735625869
    }
  ],
  "has_more": false,
  "limit": 20,
  "total": 1,
  "page": 1
}
```

### 11. Create Annotation

**POST** `/apps/annotations`

#### Request Body
- `question` (string, required): Question
- `answer` (string, required): Answer content

#### Response
```json
{
  "id": "69d48372-ad81-4c75-9c46-2ce197b4d402",
  "question": "What is your name?",
  "answer": "I am Dify.",
  "hit_count": 0,
  "created_at": 1735625869
}
```

### 12. Update Annotation

**PUT** `/apps/annotations/{annotation_id}`

#### Path Parameters
- `annotation_id` (string, required): Annotation ID

#### Request Body
- `question` (string, required): Question
- `answer` (string, required): Answer content

#### Response
```json
{
  "id": "69d48372-ad81-4c75-9c46-2ce197b4d402",
  "question": "What is your name?",
  "answer": "I am Dify.",
  "hit_count": 0,
  "created_at": 1735625869
}
```

### 13. Delete Annotation

**DELETE** `/apps/annotations/{annotation_id}`

#### Path Parameters
- `annotation_id` (string, required): Annotation ID

#### Response
```
204 No Content
```

### 14. Annotation Reply Initial Settings

**POST** `/apps/annotation-reply/{action}`

The embedding model provider and model name can be obtained through the following interface: v1/workspaces/current/models/model-types/text-embedding, see: Maintaining Knowledge Base through API. The Authorization used is the Dataset's API Token.
This interface is executed asynchronously, so it will return a job_id, and the final execution result can be obtained by querying the job status interface.

#### Path Parameters
- `action` (string, required): Action, can only be 'enable' or 'disable'

#### Request Body
- `embedding_provider_name` (string, required): Specified embedding model provider, must be set up in the system first, corresponds to the provider field
- `embedding_model_name` (string, required): Specified embedding model, corresponds to the model field
- `score_threshold` (number, required): Similarity threshold, when similarity is greater than this threshold, the system will automatically reply, otherwise it will not reply

#### Response
```json
{
  "job_id": "b15c8f68-1cf4-4877-bf21-ed7cf2011802",
  "job_status": "waiting"
}
```

### 15. Query Annotation Reply Initial Settings Task Status

**GET** `/apps/annotation-reply/{action}/status/{job_id}`

#### Path Parameters
- `action` (string, required): Action, can only be 'enable' or 'disable', and must be consistent with the action of the annotation reply initial settings interface
- `job_id` (string, required): Task ID, job_id returned from the annotation reply initial settings interface

#### Response
```json
{
  "job_id": "b15c8f68-1cf4-4877-bf21-ed7cf2011802",
  "job_status": "waiting",
  "error_msg": ""
}
```