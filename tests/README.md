# Test Structure

Test directory structure organized to match the `dify_oapi/api` code structure and standards.

## Test Structure

```
tests/
├── chat/
│   ├── v1/
│   │   ├── resource/
│   │   │   ├── test_annotation.py
│   │   │   ├── test_chat.py
│   │   │   ├── test_conversation.py
│   │   │   └── test_message.py
│   │   ├── model/
│   │   │   └── test_models.py
│   │   └── test_integration.py
│   └── test_service.py
├── chatflow/
│   ├── v1/
│   │   ├── resource/
│   │   │   ├── test_annotation.py
│   │   │   ├── test_chatflow.py
│   │   │   └── test_conversation.py
│   │   ├── model/
│   │   │   └── test_models.py
│   │   └── test_integration.py
│   └── test_service.py
├── completion/
│   ├── v1/
│   │   ├── resource/
│   │   │   ├── test_annotation.py
│   │   │   └── test_completion.py
│   │   ├── model/
│   │   │   └── test_models.py
│   │   └── test_integration.py
│   └── test_service.py
├── dify/
│   ├── v1/
│   │   ├── resource/
│   │   │   ├── test_audio.py
│   │   │   ├── test_feedback.py
│   │   │   ├── test_file.py
│   │   │   └── test_info.py
│   │   ├── model/
│   │   │   └── test_models.py
│   │   └── test_integration.py
│   └── test_service.py
├── knowledge/
│   ├── v1/
│   │   ├── resource/
│   │   │   ├── test_chunk.py
│   │   │   ├── test_dataset.py
│   │   │   ├── test_document.py
│   │   │   ├── test_model.py
│   │   │   ├── test_segment.py
│   │   │   └── test_tag.py
│   │   ├── model/
│   │   │   └── test_models.py
│   │   └── test_integration.py
│   └── test_service.py
├── workflow/
│   ├── v1/
│   │   ├── resource/
│   │   │   └── test_workflow.py
│   │   ├── model/
│   │   │   └── test_models.py
│   │   └── test_integration.py
│   └── test_service.py
└── test_client.py
```

## Design Principles

1. **Structure Alignment**: Test structure completely matches `dify_oapi/api` structure
2. **Resource Testing**: Each resource class has corresponding test files
3. **Model Testing**: Model tests centralized in `model/test_models.py`
4. **Integration Testing**: Each version has an integration test file
5. **Service Testing**: Each API module has service-level tests
6. **Minimization**: Follow minimal code principles, test only core functionality

## Test Types

- **Unit Tests**: Test individual functions/methods
- **Resource Tests**: Test resource class methods
- **Model Tests**: Test data model validation
- **Integration Tests**: Test complete API call workflows
- **Service Tests**: Test service-level functionality

## API Coverage

- **Chat API**: 18 APIs across 4 resources (annotation, chat, conversation, message)
- **Chatflow API**: 15 APIs across 3 resources (annotation, chatflow, conversation)
- **Completion API**: 10 APIs across 2 resources (annotation, completion)
- **Dify Core API**: 9 APIs across 4 resources (audio, feedback, file, info)
- **Knowledge Base API**: 33 APIs across 6 resources (chunk, dataset, document, model, segment, tag)
- **Workflow API**: 6 APIs across 1 resource (workflow)

**Total**: 91 API methods across 6 services

## Running Tests

```bash
# Set environment variables
export DOMAIN="https://api.dify.ai"
export CHAT_KEY="your-chat-api-key"
export CHATFLOW_KEY="your-chatflow-api-key"
export COMPLETION_KEY="your-completion-api-key"
export DIFY_KEY="your-dify-api-key"
export KNOWLEDGE_KEY="your-knowledge-api-key"
export WORKFLOW_KEY="your-workflow-api-key"

# Run all tests
make test

# Run tests with coverage
make test-cov

# Run specific service tests
pytest tests/chat/
pytest tests/knowledge/
pytest tests/workflow/
```