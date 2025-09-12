# Knowledge Model Management Examples

This directory contains examples for managing embedding models in the Knowledge Base API.

## 📋 Available Examples

- **`get_text_embedding_models.py`** - Get available text embedding models

## 🚀 Quick Start

### Get Embedding Models

```python
from dify_oapi.api.knowledge.v1.model.get_text_embedding_models_request import GetTextEmbeddingModelsRequest

req = GetTextEmbeddingModelsRequest.builder().build()
response = client.knowledge.v1.model.get_text_embedding_models(req, req_option)

for model in response.data:
    print(f"Model: {model.model_name}, Provider: {model.model_provider}")
```

## 🔧 Features

- **Model Discovery**: List available embedding models
- **Provider Information**: Get model provider details
- **Configuration Support**: Model-specific configuration options