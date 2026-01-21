# Chat Annotation Examples

This directory contains examples for managing annotations in the Chat API (6 APIs). Annotations allow you to add metadata, corrections, and reply settings to chat messages for improved content quality and automated responses.

## 📋 Available Examples

### Core Operations
- **`create_annotation.py`** - Create new annotations for chat messages
- **`update_annotation.py`** - Update existing annotation content
- **`delete_annotation.py`** - Delete annotations
- **`list_annotations.py`** - List all annotations with pagination

### Reply Management
- **`configure_annotation_reply.py`** - Configure annotation reply settings
- **`get_annotation_reply_status.py`** - Check annotation reply status

## 🚀 Quick Start

### Create Annotation

```python
from dify_oapi.api.chat.v1.model.create_annotation_request import CreateAnnotationRequest
from dify_oapi.api.chat.v1.model.create_annotation_request_body import CreateAnnotationRequestBody

req_body = (
    CreateAnnotationRequestBody.builder()
    .question("What is AI?")
    .answer("Artificial Intelligence is...")
    .build()
)

req = CreateAnnotationRequest.builder().request_body(req_body).build()
response = client.chat.v1.annotation.create_annotation(req, req_option)
```

### Configure Reply Settings

```python
from dify_oapi.api.chat.v1.model.configure_annotation_reply_request import ConfigureAnnotationReplyRequest
from dify_oapi.api.chat.v1.model.configure_annotation_reply_request_body import ConfigureAnnotationReplyRequestBody

req_body = (
    ConfigureAnnotationReplyRequestBody.builder()
    .enabled(True)
    .score_threshold(0.8)
    .build()
)

req = ConfigureAnnotationReplyRequest.builder().request_body(req_body).build()
response = client.chat.v1.annotation.configure_annotation_reply(req, req_option)
```

## 🔧 Features

### Annotation Management (4 APIs)
- **Create Annotation**: Add new annotations to chat messages
- **Update Annotation**: Modify existing annotation content
- **Delete Annotation**: Remove annotations
- **List Annotations**: Retrieve annotations with pagination support

### Reply Configuration (2 APIs)
- **Configure Reply Settings**: Set up automatic annotation-based replies
- **Check Reply Status**: Monitor annotation reply configuration status

### Advanced Capabilities
- **Content Quality Control**: Improve response accuracy through annotations
- **Automated Responses**: Set up intelligent auto-replies based on annotations
- **Threshold Management**: Configure similarity thresholds for annotation matching
- **Pagination Support**: Handle large annotation datasets efficiently
- **Type Safety**: Full type validation with Pydantic models
- **Error Handling**: Comprehensive error management and recovery

## 📖 Use Cases

- **Content Moderation**: Add moderation notes to messages
- **Quality Control**: Annotate messages for training purposes
- **User Feedback**: Collect and organize user feedback
- **Automated Replies**: Set up automatic responses based on annotations
