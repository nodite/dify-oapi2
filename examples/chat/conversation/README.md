# Chat Conversation Management Examples

This directory contains examples for managing conversation lifecycle, metadata, and history in the Chat API.

## 📋 Available Examples

### Conversation Operations
- **`get_conversations.py`** - List all conversations with pagination
- **`delete_conversation.py`** - Delete specific conversations
- **`rename_conversation.py`** - Rename conversation titles

### Conversation Data
- **`get_conversation_variables.py`** - Retrieve conversation variables and context
- **`get_message_history.py`** - Get complete message history for a conversation

### Advanced Management
- **`conversation_management.py`** - Comprehensive conversation management example

## 🚀 Quick Start

### List Conversations

```python
from dify_oapi.api.chat.v1.model.get_conversations_request import GetConversationsRequest

req = GetConversationsRequest.builder()
    .user("user-123")
    .limit(20)
    .build()

response = client.chat.v1.conversation.get_conversations(req, req_option)
for conversation in response.data:
    print(f"ID: {conversation.id}, Name: {conversation.name}")
```

### Get Message History

```python
from dify_oapi.api.chat.v1.model.message_history_request import MessageHistoryRequest

req = MessageHistoryRequest.builder()
    .conversation_id("conversation-id")
    .user("user-123")
    .limit(50)
    .build()

response = client.chat.v1.conversation.get_message_history(req, req_option)
for message in response.data:
    print(f"{message.role}: {message.content}")
```

### Rename Conversation

```python
from dify_oapi.api.chat.v1.model.rename_conversation_request import RenameConversationRequest
from dify_oapi.api.chat.v1.model.rename_conversation_request_body import RenameConversationRequestBody

req_body = RenameConversationRequestBody.builder()
    .name("New Conversation Name")
    .build()

req = RenameConversationRequest.builder()
    .conversation_id("conversation-id")
    .request_body(req_body)
    .build()

response = client.chat.v1.conversation.rename_conversation(req, req_option)
```

## 🔧 Features

### Conversation Lifecycle
- **Creation**: Conversations are created automatically with first message
- **Management**: Rename, organize, and categorize conversations
- **Deletion**: Clean up old or unwanted conversations
- **Archival**: Maintain conversation history and context

### Data Access
- **Message History**: Access complete conversation history
- **Variables**: Retrieve conversation context and variables
- **Metadata**: Access conversation metadata and settings
- **Pagination**: Handle large conversation lists efficiently

### Organization
- **User-based**: Organize conversations by user
- **Naming**: Meaningful conversation titles
- **Filtering**: Filter conversations by various criteria
- **Sorting**: Sort by date, activity, or custom criteria

## 📖 Best Practices

1. **Regular Cleanup**: Periodically delete old conversations
2. **Meaningful Names**: Use descriptive conversation names
3. **User Isolation**: Always filter by user ID for privacy
4. **Pagination**: Handle large conversation lists with pagination
5. **Error Handling**: Gracefully handle missing conversations
6. **Context Preservation**: Maintain conversation context for continuity

## 🔗 Related Examples

- [Chat Operations](../chat/) - Core chat functionality
- [Message Operations](../message/) - Message-specific operations
- [Annotation Management](../annotation/) - Message annotations