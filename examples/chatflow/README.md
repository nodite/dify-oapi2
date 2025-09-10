# Chatflow API Examples

This directory contains comprehensive examples for all **17 Chatflow APIs** across **6 resource categories**. The Chatflow API provides advanced chat functionality with workflow events, file support, conversation management, and comprehensive application settings.

## 📋 API Overview

**Total APIs**: 17 endpoints across 6 resources:

### 🔄 Chatflow (3 APIs)
- **Send Chat Message** - Advanced chat with streaming support and file attachments
- **Stop Chat Message** - Stop ongoing chat generation
- **Get Suggested Questions** - Get next question suggestions

### 📁 File (1 API)
- **Upload File** - Upload files for multimodal chat interactions

### 💬 Feedback (2 APIs)
- **Message Feedback** - Provide feedback on chat messages
- **Get App Feedbacks** - Retrieve application feedback history

### 🗨️ Conversation (5 APIs)
- **Get Conversation Messages** - Retrieve message history
- **Get Conversations** - List all conversations
- **Delete Conversation** - Remove conversations
- **Rename Conversation** - Update conversation names
- **Get Conversation Variables** - Access conversation variables

### 🔊 TTS (2 APIs)
- **Audio to Text** - Convert speech to text
- **Text to Audio** - Convert text to speech

### ⚙️ Application (4 APIs)
- **Get Info** - Basic application information
- **Get Parameters** - Application configuration parameters
- **Get Meta** - Application metadata and tool icons
- **Get Site** - WebApp settings and customization

### 📝 Annotation (6 APIs)
- **Get Annotations** - List annotation entries
- **Create Annotation** - Add new annotations
- **Update Annotation** - Modify existing annotations
- **Delete Annotation** - Remove annotations
- **Annotation Reply Settings** - Configure annotation reply behavior
- **Annotation Reply Status** - Check annotation reply job status

## 🚀 Quick Start

### Prerequisites

1. **Python 3.10+** installed
2. **dify-oapi2** package installed:
   ```bash
   pip install dify-oapi2
   ```
3. **API Key** from your Dify application

### Environment Setup

Set your API key as an environment variable:

```bash
export API_KEY="your-dify-api-key-here"
```

### Basic Usage

```python
from dify_oapi.client import Client
from dify_oapi.core.model.request_option import RequestOption

# Initialize client
client = Client.builder().domain("https://api.dify.ai").build()

# Create request option with API key
request_option = RequestOption.builder().api_key("your-api-key").build()

# Use any chatflow API
response = client.chatflow.v1.application.info(request, request_option)
```

## 📂 Directory Structure

```
examples/chatflow/
├── chatflow/                    # Core chatflow operations (3 APIs)
│   ├── send_chat_message.py     # Send messages with streaming/blocking modes
│   ├── stop_chat_message.py     # Stop message generation
│   └── get_suggested_questions.py # Get question suggestions
├── file/                        # File operations (1 API)
│   └── upload_file.py           # Upload files for multimodal support
├── feedback/                    # Feedback operations (2 APIs)
│   ├── message_feedback.py      # Provide message feedback
│   └── get_app_feedbacks.py     # Get feedback history
├── conversation/                # Conversation management (5 APIs)
│   ├── get_conversation_messages.py # Message history
│   ├── get_conversations.py     # Conversation list
│   ├── delete_conversation.py   # Delete conversations
│   ├── rename_conversation.py   # Rename conversations
│   └── get_conversation_variables.py # Conversation variables
├── tts/                         # Text-to-Speech operations (2 APIs)
│   ├── audio_to_text.py         # Speech-to-text conversion
│   └── text_to_audio.py         # Text-to-speech conversion
├── application/                 # Application configuration (4 APIs)
│   ├── get_info.py              # Basic app information
│   ├── get_parameters.py        # App parameters
│   ├── get_meta.py              # App metadata
│   └── get_site.py              # WebApp settings
├── annotation/                  # Annotation management (6 APIs)
│   ├── get_annotations.py       # List annotations
│   ├── create_annotation.py     # Create annotations
│   ├── update_annotation.py     # Update annotations
│   ├── delete_annotation.py     # Delete annotations
│   ├── annotation_reply_settings.py # Configure reply settings
│   └── annotation_reply_status.py   # Check reply status
└── README.md                    # This file
```

## 🔄 Chatflow Examples

### Send Chat Message

**File**: `chatflow/send_chat_message.py`

The most comprehensive example demonstrating:
- **Blocking Mode**: Synchronous chat with complete response
- **Streaming Mode**: Real-time response streaming
- **File Attachments**: Multimodal chat with documents/images
- **Conversation Continuation**: Continue existing conversations
- **Async Support**: Both sync and async operations

**Key Features**:
```python
# Blocking mode
response = client.chatflow.v1.chatflow.send(request, option, False)

# Streaming mode
response = client.chatflow.v1.chatflow.send(request, option, True)
for chunk in response:
    print(chunk.decode("utf-8"), end="", flush=True)

# With file attachment
chat_file = ChatFile.builder()
    .type("document")
    .transfer_method("remote_url")
    .url("https://example.com/doc.pdf")
    .build()
```

### Stop Chat Message

**File**: `chatflow/stop_chat_message.py`

Stop ongoing chat message generation:
```python
# Stop streaming chat
response = client.chatflow.v1.chatflow.stop(request, option)
```

### Get Suggested Questions

**File**: `chatflow/get_suggested_questions.py`

Get AI-generated follow-up questions:
```python
response = client.chatflow.v1.chatflow.suggested(request, option)
print(f"Suggested questions: {response.data}")
```

## 📁 File Examples

### Upload File

**File**: `file/upload_file.py`

Comprehensive file upload examples:
- **Multiple File Types**: Text, JSON, CSV, images, documents
- **Multipart Upload**: Proper form-data handling
- **Error Handling**: File size limits, unsupported formats
- **Workflow Integration**: Upload → Get ID → Use in chat

**Supported File Types**:
- **Documents**: TXT, MD, PDF, HTML, XLSX, DOCX, CSV, EML, MSG, PPTX, XML, EPUB
- **Images**: JPG, PNG, GIF, WEBP, SVG
- **Audio**: MP3, M4A, WAV, WEBM, AMR
- **Video**: MP4, MOV, MPEG, MPGA

```python
# Upload file
file_data = BytesIO(content.encode("utf-8"))
request = UploadFileRequest.builder()
    .file(file_data, "[Example]_document.txt")
    .user("user-123")
    .build()

response = client.chatflow.v1.file.upload(request, option)
file_id = response.id  # Use in ChatFile objects
```

## 💬 Feedback Examples

### Message Feedback

**File**: `feedback/message_feedback.py`

Provide feedback on chat messages:
```python
# Like/dislike with optional comment
request_body = MessageFeedbackRequestBody.builder()
    .rating("like")  # "like" | "dislike" | None
    .user("user-123")
    .content("This response was very helpful!")
    .build()
```

### Get App Feedbacks

**File**: `feedback/get_app_feedbacks.py`

Retrieve feedback history with pagination:
```python
# Get feedbacks with pagination
request = GetAppFeedbacksRequest.builder()
    .page(1)
    .limit(20)
    .build()
```

## 🗨️ Conversation Examples

### Get Conversation Messages

**File**: `conversation/get_conversation_messages.py`

Retrieve message history with pagination:
```python
request = GetConversationMessagesRequest.builder()
    .conversation_id("conv-123")
    .user("user-123")
    .limit(20)
    .build()
```

### Get Conversations

**File**: `conversation/get_conversations.py`

List conversations with sorting and pagination:
```python
request = GetConversationsRequest.builder()
    .user("user-123")
    .sort_by("-updated_at")  # Sort by most recent
    .limit(20)
    .build()
```

### Delete Conversation

**File**: `conversation/delete_conversation.py`

Safely delete conversations:
```python
# Only delete conversations with [Example] prefix for safety
request = DeleteConversationRequest.builder()
    .conversation_id("conv-123")
    .request_body(
        DeleteConversationRequestBody.builder()
        .user("user-123")
        .build()
    )
    .build()
```

### Rename Conversation

**File**: `conversation/rename_conversation.py`

Rename conversations manually or auto-generate:
```python
# Manual rename
request_body = RenameConversationRequestBody.builder()
    .name("[Example] New Conversation Name")
    .user("user-123")
    .build()

# Auto-generate name
request_body = RenameConversationRequestBody.builder()
    .auto_generate(True)
    .user("user-123")
    .build()
```

### Get Conversation Variables

**File**: `conversation/get_conversation_variables.py`

Access conversation variables:
```python
request = GetConversationVariablesRequest.builder()
    .conversation_id("conv-123")
    .user("user-123")
    .variable_name("specific_var")  # Optional filter
    .build()
```

## 🔊 TTS Examples

### Audio to Text

**File**: `tts/audio_to_text.py`

Convert speech to text:
```python
# Upload audio file for transcription
audio_data = open("audio.mp3", "rb").read()
request = AudioToTextRequest.builder()
    .file(BytesIO(audio_data), "audio.mp3")
    .user("user-123")
    .build()

response = client.chatflow.v1.tts.speech_to_text(request, option)
print(f"Transcription: {response.text}")
```

**Supported Audio Formats**: mp3, mp4, mpeg, mpga, m4a, wav, webm

### Text to Audio

**File**: `tts/text_to_audio.py`

Convert text to speech:
```python
# Convert text to audio
request_body = TextToAudioRequestBody.builder()
    .text("Hello, this is a test message")
    .user("user-123")
    .streaming(False)
    .build()

# Returns binary audio data
response = client.chatflow.v1.tts.text_to_audio(request, option)
```

## ⚙️ Application Examples

### Get Info

**File**: `application/get_info.py`

Get basic application information:
```python
response = client.chatflow.v1.application.info(request, option)
print(f"App: {response.name}")
print(f"Description: {response.description}")
print(f"Tags: {response.tags}")
```

### Get Parameters

**File**: `application/get_parameters.py`

Get comprehensive application parameters:
```python
response = client.chatflow.v1.application.parameters(request, option)
print(f"Opening statement: {response.opening_statement}")
print(f"Suggested questions: {response.suggested_questions}")
print(f"TTS enabled: {response.text_to_speech.enabled}")
print(f"File upload enabled: {response.file_upload.image.enabled}")
```

### Get Meta

**File**: `application/get_meta.py`

Get application metadata and tool icons:
```python
response = client.chatflow.v1.application.meta(request, option)
print(f"Tool icons: {response.tool_icons}")
```

### Get Site

**File**: `application/get_site.py`

Get WebApp settings and customization:
```python
response = client.chatflow.v1.application.site(request, option)
print(f"Title: {response.title}")
print(f"Theme: {response.chat_color_theme}")
print(f"Icon: {response.icon}")
```

## 📝 Annotation Examples

### Get Annotations

**File**: `annotation/get_annotations.py`

List annotation entries with pagination:
```python
request = GetAnnotationsRequest.builder()
    .page(1)
    .limit(20)
    .build()
```

### Create Annotation

**File**: `annotation/create_annotation.py`

Create new annotation entries:
```python
request_body = CreateAnnotationRequestBody.builder()
    .question("What is machine learning?")
    .answer("Machine learning is a subset of AI...")
    .build()
```

### Update Annotation

**File**: `annotation/update_annotation.py`

Modify existing annotations:
```python
request_body = UpdateAnnotationRequestBody.builder()
    .question("Updated question")
    .answer("Updated answer")
    .build()
```

### Delete Annotation

**File**: `annotation/delete_annotation.py`

Remove annotation entries:
```python
# Only delete annotations with [Example] prefix for safety
request = DeleteAnnotationRequest.builder()
    .annotation_id("annotation-123")
    .build()
```

### Annotation Reply Settings

**File**: `annotation/annotation_reply_settings.py`

Configure annotation reply behavior:
```python
# Enable annotation replies
request_body = AnnotationReplySettingsRequestBody.builder()
    .embedding_provider_name("openai")
    .embedding_model_name("text-embedding-ada-002")
    .score_threshold(0.8)
    .build()

request = AnnotationReplySettingsRequest.builder()
    .action("enable")  # "enable" | "disable"
    .request_body(request_body)
    .build()
```

### Annotation Reply Status

**File**: `annotation/annotation_reply_status.py`

Check annotation reply job status:
```python
request = AnnotationReplyStatusRequest.builder()
    .action("enable")
    .job_id("job-123")
    .build()

response = client.chatflow.v1.annotation.reply_status(request, option)
print(f"Job status: {response.job_status}")
```

## 🔧 Common Patterns

### Error Handling

All examples include comprehensive error handling:

```python
try:
    response = client.chatflow.v1.resource.method(request, option)
    
    if response.success:
        print("✅ Success!")
        # Handle successful response
    else:
        print(f"❌ Error: {response.msg}")
        print(f"Error code: {response.code}")
        
except Exception as e:
    print(f"❌ Unexpected error: {e}")
```

### Environment Validation

All examples validate required environment variables:

```python
def validate_environment():
    api_key = os.getenv("API_KEY")
    if not api_key:
        raise ValueError("API_KEY environment variable is required")
    return api_key
```

### Safety Prefixes

All examples use `[Example]` prefixes for safety:

```python
# Safe resource naming
conversation_name = "[Example] Test Conversation"
file_name = "[Example]_document.txt"
annotation_question = "[Example] What is AI?"
```

### Sync and Async Support

Most examples demonstrate both synchronous and asynchronous usage:

```python
# Synchronous
def sync_example():
    response = client.chatflow.v1.resource.method(request, option)
    return response

# Asynchronous
async def async_example():
    response = await client.chatflow.v1.resource.amethod(request, option)
    return response

# Usage
sync_example()
asyncio.run(async_example())
```

## 🎯 Usage Scenarios

### 1. Basic Chat Application

```python
# 1. Send chat message
response = client.chatflow.v1.chatflow.send(chat_request, option)

# 2. Get suggested follow-up questions
suggestions = client.chatflow.v1.chatflow.suggested(suggestion_request, option)

# 3. Collect user feedback
feedback = client.chatflow.v1.feedback.message(feedback_request, option)
```

### 2. Multimodal Chat with Files

```python
# 1. Upload file
file_response = client.chatflow.v1.file.upload(upload_request, option)

# 2. Use file in chat
chat_file = ChatFile.builder()
    .type("document")
    .transfer_method("local_file")
    .upload_file_id(file_response.id)
    .build()

# 3. Send chat with file
chat_request = SendChatMessageRequestBody.builder()
    .query("Analyze this document")
    .files([chat_file])
    .build()
```

### 3. Conversation Management

```python
# 1. List conversations
conversations = client.chatflow.v1.conversation.list(list_request, option)

# 2. Get message history
messages = client.chatflow.v1.conversation.messages(messages_request, option)

# 3. Rename conversation
renamed = client.chatflow.v1.conversation.rename(rename_request, option)
```

### 4. Voice Integration

```python
# 1. Convert speech to text
text_response = client.chatflow.v1.tts.speech_to_text(audio_request, option)

# 2. Send text to chat
chat_response = client.chatflow.v1.chatflow.send(chat_request, option)

# 3. Convert response to speech
audio_response = client.chatflow.v1.tts.text_to_audio(tts_request, option)
```

### 5. Application Configuration

```python
# 1. Get app info
info = client.chatflow.v1.application.info(info_request, option)

# 2. Get app parameters
params = client.chatflow.v1.application.parameters(params_request, option)

# 3. Get WebApp settings
site = client.chatflow.v1.application.site(site_request, option)
```

## 🚨 Safety Guidelines

### Resource Naming
- **Always use `[Example]` prefix** for any resources created in examples
- This prevents accidental deletion of production resources
- Examples include safety checks to only operate on `[Example]` prefixed resources

### Environment Variables
- **Never hardcode API keys** in example code
- Always validate environment variables before API calls
- Use descriptive error messages for missing configuration

### Error Handling
- **Always check `response.success`** before accessing response data
- Handle common error scenarios (file too large, unsupported format, etc.)
- Provide helpful error messages and suggestions

### Rate Limiting
- Be mindful of API rate limits when running multiple examples
- Add delays between requests if needed
- Use pagination appropriately for list operations

## 🔍 Troubleshooting

### Common Issues

1. **Missing API Key**
   ```
   ValueError: API_KEY environment variable is required
   ```
   **Solution**: Set your API key: `export API_KEY="your-key"`

2. **File Upload Errors**
   ```
   Error 413: File is too large
   ```
   **Solution**: Check file size limits in application parameters

3. **Unsupported File Type**
   ```
   Error 415: Unsupported media type
   ```
   **Solution**: Verify file type is supported (see file upload examples)

4. **Conversation Not Found**
   ```
   Error 404: Conversation not found
   ```
   **Solution**: Verify conversation ID exists and belongs to the user

5. **Streaming Connection Issues**
   ```
   Connection timeout during streaming
   ```
   **Solution**: Check network connectivity and API endpoint availability

### Debug Tips

1. **Enable Verbose Logging**: Add debug prints to track request/response flow
2. **Check Response Objects**: Always inspect `response.success`, `response.code`, and `response.msg`
3. **Validate Input Data**: Ensure all required fields are provided
4. **Test with Simple Cases**: Start with basic examples before complex scenarios

## 📚 Additional Resources

- **Main Documentation**: [Project README](../../README.md)
- **API Specification**: [Chatflow API Documentation](../../docs/chatflow/chatflow-api.md)
- **Other Examples**: 
  - [Chat API Examples](../chat/README.md)
  - [Completion API Examples](../completion/README.md)
  - [Knowledge API Examples](../knowledge/README.md)
  - [Workflow API Examples](../workflow/README.md)

## 🤝 Contributing

When adding new examples:

1. **Follow Naming Conventions**: Use descriptive file names matching API operations
2. **Include Both Sync/Async**: Demonstrate both synchronous and asynchronous usage
3. **Add Error Handling**: Include comprehensive error handling and validation
4. **Use Safety Prefixes**: Always use `[Example]` prefixes for created resources
5. **Document Usage**: Add clear docstrings and comments explaining functionality
6. **Test Thoroughly**: Ensure examples work with real API endpoints

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](../../LICENSE) file for details.

---

**Total Examples**: 17 example files covering all Chatflow APIs
**Resources Covered**: 6 resource categories with complete functionality
**Features Demonstrated**: Streaming, file uploads, conversation management, TTS, application configuration, and annotation management