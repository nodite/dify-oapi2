# Dify Completion API Documentation

This document provides comprehensive documentation for the Dify Completion API, organized into functional modules for better understanding and implementation.

## API Modules

### [Completion Management APIs](#completion-management)
- Send Message
- Stop Response

### [Annotation Management APIs](#annotation-management)
- List Annotations
- Create Annotation
- Update Annotation
- Delete Annotation
- Annotation Reply Settings
- Query Annotation Reply Status

### [Audio Processing APIs](#audio-processing)
- Text to Audio

### [Feedback Management APIs](#feedback-management)
- Message Feedback
- Get Feedbacks

### [File Management APIs](#file-management)
- Upload File

### [Application Information APIs](#application-information)
- Get Application Info
- Get Parameters
- Get Site Info

## Authentication

All Service API requests use `API-Key` for authentication. Include your `API-Key` in the **`Authorization`** HTTP Header:

```
Authorization: Bearer {API_KEY}
```

## API Details

### Completion Management

#### Send Message
Send a completion message to the AI model with support for both streaming and blocking responses.

**Endpoint**: `POST /v1/completion-messages`

**Features**:
- Streaming and blocking response modes
- Custom input parameters
- File attachment support
- User context management

#### Stop Response
Stop an ongoing completion response.

**Endpoint**: `POST /v1/completion-messages/:task_id/stop`

### Annotation Management

#### List Annotations
Retrieve a list of annotations for completion messages.

#### Create Annotation
Create a new annotation for a completion message.

#### Update Annotation
Update an existing annotation.

#### Delete Annotation
Delete a specific annotation.

#### Annotation Reply Settings
Configure annotation reply settings.

#### Query Annotation Reply Status
Check the status of annotation reply operations.

### Audio Processing

#### Text to Audio
Convert text responses to audio format.

**Features**:
- Text-to-speech conversion
- Multiple audio format support
- Quality configuration options

### Feedback Management

#### Message Feedback
Submit feedback for completion messages.

**Features**:
- Like/dislike feedback
- Custom feedback messages
- User attribution

#### Get Feedbacks
Retrieve feedback data for analysis.

### File Management

#### Upload File
Upload files for use in completion requests.

**Features**:
- Multiple file format support
- File validation
- Secure file handling

### Application Information

#### Get Application Info
Retrieve basic application information and configuration.

#### Get Parameters
Get application parameters and settings.

#### Get Site Info
Retrieve site-specific information and branding.

## Summary

The Dify Completion API provides comprehensive functionality organized into 6 modules with a total of **15 APIs**:

- **Completion Management**: 2 APIs for core completion functionality including message sending and response control
- **Annotation Management**: 6 APIs for managing annotations, reply settings, and status tracking
- **Audio Processing**: 1 API for text-to-audio conversion
- **Feedback Management**: 2 APIs for collecting and retrieving user feedback
- **File Management**: 1 API for file upload and handling
- **Application Information**: 3 APIs for retrieving application configuration and metadata

All APIs support both synchronous and asynchronous operations, providing flexibility for different integration patterns and performance requirements.