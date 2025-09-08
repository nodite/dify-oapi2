# Chat API Examples

This directory contains comprehensive examples for all 22 Chat APIs organized by resource categories.

## Overview

The Chat API provides 22 endpoints across 7 resource categories:

- **Chat Messages** (3 APIs): Chat message processing
- **File Management** (1 API): File management  
- **Feedback Management** (2 APIs): Feedback management
- **Conversation Management** (5 APIs): Conversation management
- **Audio Processing** (2 APIs): Audio processing
- **Application Information** (4 APIs): Application information
- **Annotation Management** (6 APIs): Annotation management

## Directory Structure

```
examples/chat/
├── chat/                           # Chat Messages (3 APIs)
│   ├── send_chat_message.py        # Send chat message
│   ├── stop_chat_generation.py     # Stop chat generation
│   └── get_suggested_questions.py  # Get suggested questions
├── file/                           # File Management (1 API)
│   └── upload_file.py              # Upload file
├── feedback/                       # Feedback Management (2 APIs)
│   ├── submit_feedback.py          # Submit feedback
│   └── get_feedbacks.py            # Get feedbacks
├── conversation/                   # Conversation Management (5 APIs)
│   ├── get_message_history.py      # Get message history
│   ├── get_conversations.py        # Get conversations
│   ├── delete_conversation.py      # Delete conversation
│   ├── rename_conversation.py      # Rename conversation
│   └── get_conversation_variables.py # Get conversation variables
├── audio/                          # Audio Processing (2 APIs)
│   ├── audio_to_text.py            # Audio to text
│   └── text_to_audio.py            # Text to audio
├── app/                            # Application Information (4 APIs)
│   ├── get_app_info.py             # Get app info
│   ├── get_app_parameters.py       # Get app parameters
│   ├── get_app_meta.py             # Get app meta
│   └── get_site_settings.py        # Get site settings
├── annotation/                     # Annotation Management (6 APIs)
│   ├── list_annotations.py         # List annotations
│   ├── create_annotation.py        # Create annotation
│   ├── update_annotation.py        # Update annotation
│   ├── delete_annotation.py        # Delete annotation
│   ├── configure_annotation_reply.py # Configure annotation reply
│   └── get_annotation_reply_status.py # Get annotation reply status
└── README.md                       # This file
```

## Environment Variables

All examples require the following environment variables:

### Required for All Examples
```bash
export CHAT_API_KEY="your-chat-api-key"
```

### API-Specific Variables
```bash
# For message-related operations
export MESSAGE_ID="your-message-id"
export CONVERSATION_ID="your-conversation-id"

# For task operations
export TASK_ID="your-task-id"

# For file operations
export FILE_PATH="/path/to/your/file.jpg"
export AUDIO_PATH="/path/to/your/audio.mp3"

# For annotation operations
export ANNOTATION_ID="your-annotation-id"
export JOB_ID="your-job-id"

# For pagination
export LAST_ID="your-last-id"
export FIRST_ID="your-first-id"

# For filtering
export VARIABLE_NAME="your-variable-name"
```

## Usage Examples

### Basic Chat Message
```bash
export CHAT_API_KEY="your-api-key"
python examples/chat/chat/send_chat_message.py
```

### File Upload and Chat
```bash
export CHAT_API_KEY="your-api-key"
export FILE_PATH="/path/to/image.jpg"
python examples/chat/file/upload_file.py
```

### Conversation Management
```bash
export CHAT_API_KEY="your-api-key"
export CONVERSATION_ID="your-conversation-id"
python examples/chat/conversation/get_conversations.py
python examples/chat/conversation/get_message_history.py
```

### Audio Processing
```bash
export CHAT_API_KEY="your-api-key"
export AUDIO_PATH="/path/to/audio.mp3"
python examples/chat/audio/audio_to_text.py
python examples/chat/audio/text_to_audio.py
```

### Feedback Management
```bash
export CHAT_API_KEY="your-api-key"
export MESSAGE_ID="your-message-id"
python examples/chat/feedback/submit_feedback.py
python examples/chat/feedback/get_feedbacks.py
```

### Application Information
```bash
export CHAT_API_KEY="your-api-key"
python examples/chat/app/get_app_info.py
python examples/chat/app/get_app_parameters.py
```

### Annotation Management
```bash
export CHAT_API_KEY="your-api-key"
python examples/chat/annotation/list_annotations.py
python examples/chat/annotation/create_annotation.py

# For update/delete operations
export ANNOTATION_ID="your-annotation-id"
python examples/chat/annotation/update_annotation.py
python examples/chat/annotation/delete_annotation.py
```

## Example Features

### Synchronous and Asynchronous Support
All examples include both sync and async implementations:

```python
# Synchronous
def send_chat():
    response = client.chat.v1.chat.chat(req, req_option, False)
    return response

# Asynchronous  
async def send_chat_async():
    response = await client.chat.v1.chat.achat(req, req_option, False)
    return response
```

### Streaming Support
Chat examples demonstrate both blocking and streaming modes:

```python
# Blocking mode
response = client.chat.v1.chat.chat(req, req_option, False)
print(response.answer)

# Streaming mode
response = client.chat.v1.chat.chat(req, req_option, True)
for chunk in response:
    print(chunk.decode('utf-8'), end="", flush=True)
```

### Error Handling
All examples include comprehensive error handling:

```python
try:
    response = client.chat.v1.chat.chat(req, req_option, False)
    print(f"Success: {response.answer}")
    return response
except Exception as e:
    print(f"Error: {e}")
    raise
```

### Environment Validation
Examples validate required environment variables:

```python
api_key = os.getenv("CHAT_API_KEY")
if not api_key:
    raise ValueError("CHAT_API_KEY environment variable is required")
```

## API Categories

### 1. Chat Messages (3 APIs)
- **Send Chat Message**: Send messages with streaming/blocking modes
- **Stop Chat Generation**: Stop ongoing chat generation tasks
- **Get Suggested Questions**: Get AI-suggested follow-up questions

### 2. File Management (1 API)
- **Upload File**: Upload images for multimodal chat interactions

### 3. Feedback Management (2 APIs)
- **Submit Feedback**: Submit like/dislike feedback for messages
- **Get Feedbacks**: Retrieve application feedback with pagination

### 4. Conversation Management (5 APIs)
- **Get Message History**: Retrieve conversation message history
- **Get Conversations**: List user conversations with sorting/pagination
- **Delete Conversation**: Delete conversations
- **Rename Conversation**: Rename conversations (manual or auto-generated)
- **Get Conversation Variables**: Retrieve conversation variables

### 5. Audio Processing (2 APIs)
- **Audio to Text**: Convert audio files to text (speech recognition)
- **Text to Audio**: Convert text to audio (text-to-speech)

### 6. Application Information (4 APIs)
- **Get App Info**: Retrieve basic application information
- **Get App Parameters**: Get application configuration parameters
- **Get App Meta**: Retrieve application metadata and tool icons
- **Get Site Settings**: Get WebApp site settings

### 7. Annotation Management (6 APIs)
- **List Annotations**: List all annotations with pagination
- **Create Annotation**: Create new question-answer annotations
- **Update Annotation**: Update existing annotations
- **Delete Annotation**: Delete annotations
- **Configure Annotation Reply**: Enable/disable annotation reply with embedding models
- **Get Annotation Reply Status**: Check configuration job status

## File Format Support

### Image Files (for Vision Models)
- PNG, JPG, JPEG, WEBP, GIF

### Audio Files (for Speech Processing)
- MP3, MP4, MPEG, MPGA, M4A, WAV, WEBM
- File size limit: 15MB

## Best Practices

### 1. Environment Management
- Store API keys securely in environment variables
- Validate required variables before API calls
- Use different API keys for different environments

### 2. Error Handling
- Always wrap API calls in try-catch blocks
- Handle specific error types appropriately
- Provide meaningful error messages

### 3. Resource Management
- Use context managers for file operations
- Close file handles properly
- Clean up temporary files

### 4. Async Operations
- Use async/await for better performance
- Handle async exceptions properly
- Consider using asyncio.gather for concurrent operations

### 5. Pagination
- Handle pagination for list operations
- Check `has_more` flag for additional pages
- Use appropriate page sizes

### 6. Streaming
- Process streaming responses chunk by chunk
- Handle connection interruptions
- Implement proper cleanup for streaming operations

## Testing

### Unit Testing
Each example can be tested individually:

```bash
# Test specific example
python examples/chat/chat/send_chat_message.py

# Test with different parameters
export CHAT_API_KEY="test-key"
python examples/chat/feedback/submit_feedback.py
```

### Integration Testing
Test complete workflows:

```bash
# Complete chat workflow
python examples/chat/chat/send_chat_message.py
python examples/chat/feedback/submit_feedback.py
python examples/chat/chat/get_suggested_questions.py
```

## Troubleshooting

### Common Issues

1. **Missing Environment Variables**
   ```
   ValueError: CHAT_API_KEY environment variable is required
   ```
   Solution: Set the required environment variable

2. **File Not Found**
   ```
   FileNotFoundError: [Errno 2] No such file or directory
   ```
   Solution: Check file paths and ensure files exist

3. **API Authentication Error**
   ```
   401 Unauthorized
   ```
   Solution: Verify API key is correct and has proper permissions

4. **Rate Limiting**
   ```
   429 Too Many Requests
   ```
   Solution: Implement retry logic with exponential backoff

### Debug Mode
Enable debug logging for troubleshooting:

```python
import logging
logging.basicConfig(level=logging.DEBUG)
```

## Contributing

When adding new examples:

1. Follow the established directory structure
2. Include both sync and async implementations
3. Add comprehensive error handling
4. Validate environment variables
5. Include clear documentation
6. Test with various scenarios

## Support

For issues or questions:

1. Check the main project documentation
2. Review API specifications
3. Test with minimal examples
4. Check environment variable configuration
5. Verify API key permissions

## License

These examples are part of the dify-oapi2 project and follow the same MIT license.