# 测试结构重组

根据 `dify_oapi/api` 下的代码规范和目录结构，重新调整测试目录结构。

## 新的测试结构

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

## 设计原则

1. **结构对应**: 测试结构与 `dify_oapi/api` 结构完全对应
2. **资源测试**: 每个资源类有对应的测试文件
3. **模型测试**: 模型测试集中在 `model/test_models.py`
4. **集成测试**: 每个版本有一个集成测试文件
5. **服务测试**: 每个 API 模块有一个服务级别测试
6. **最小化**: 遵循最小化代码原则，只测试核心功能

## 测试类型

- **单元测试**: 测试单个函数/方法
- **资源测试**: 测试资源类的方法
- **模型测试**: 测试数据模型的验证
- **集成测试**: 测试完整的 API 调用流程
- **服务测试**: 测试服务级别的功能