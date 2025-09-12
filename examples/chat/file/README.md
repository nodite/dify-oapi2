# Chat File Management Examples

This directory contains examples for uploading and managing files in the Chat API.

## 📋 Available Examples

- **`upload_file.py`** - Upload images and documents for chat interactions

## 🚀 Quick Start

### Upload Image File

```python
from dify_oapi.api.chat.v1.model.chat_file import ChatFile

req_file = (
    ChatFile.builder()
    .type("image")
    .transfer_method("remote_url")
    .url("https://example.com/image.jpg")
    .build()
)

# Use in chat request
req_body = (
    ChatRequestBody.builder()
    .query("What do you see in this image?")
    .files([req_file])
    .response_mode("blocking")
    .user("user-123")
    .build()
)
```

## 🔧 Supported File Types

- **Images**: JPG, PNG, GIF, WebP
- **Documents**: PDF, TXT, DOCX, MD
- **Transfer Methods**: `remote_url`, `local_file`

## 🔗 Related Examples

- [Chat Operations](../chat/) - Use files in chat
- [Dify File Management](../../dify/file/) - Core file upload functionality