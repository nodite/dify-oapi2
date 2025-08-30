# Completion API Examples

This directory contains comprehensive examples for all 9 Completion APIs, organized by resource functionality. Each example demonstrates both synchronous and asynchronous usage patterns with minimal code implementation.

## API Overview

**Total APIs**: 9 endpoints across 5 resource categories

- **Completion APIs (2)**: Message processing and generation control
- **File APIs (1)**: File upload for multimodal understanding
- **Feedback APIs (2)**: Message feedback and application feedback retrieval
- **Audio APIs (1)**: Text-to-speech conversion
- **Info APIs (3)**: Application information and configuration

## Directory Structure

```
completion/
├── completion/          # Message processing examples
├── file/               # File upload examples
├── feedback/           # Feedback system examples
├── audio/              # Audio processing examples
├── info/               # Application info examples
└── README.md           # This file
```

## Environment Setup

```bash
export API_KEY="your-completion-api-key"
export DOMAIN="https://api.dify.ai"
```

## Documentation

For detailed examples, migration guide, and testing strategies, see:
- [Completion Design Document](../../docs/completion/completion-design.md)

## Best Practices

1. **API Key Security**: Store API keys server-side only
2. **Error Handling**: Use BaseResponse properties for consistent error handling
3. **Type Safety**: Use provided Literal types for all predefined values
4. **Resource Management**: Properly manage and cleanup resources
5. **Streaming Usage**: Use streaming mode for better user experience