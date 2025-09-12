# API 迁移指南

## 概述

本指南说明如何从各模块的重复API迁移到统一的系统级API。迁移后，所有系统级功能将通过 `client.dify.v1` 访问。

## 迁移映射

### 1. 文件上传 API

**迁移前:**
```python
# Chat 模块
client.chat.v1.file.upload(request, option)

# Completion 模块  
client.completion.v1.file.upload_file(request, option)

# Chatflow 模块
client.chatflow.v1.file.upload(request, option)

# Workflow 模块
client.workflow.v1.workflow.upload(request, option)
```

**迁移后:**
```python
# 统一使用 dify 模块
client.dify.v1.file.upload(request, option)
```

### 2. 音频处理 API

**迁移前:**
```python
# Chat 模块
client.chat.v1.audio.to_text(request, option)
client.chat.v1.audio.to_audio(request, option)

# Completion 模块
client.completion.v1.audio.text_to_audio(request, option)

# Chatflow 模块
client.chatflow.v1.tts.speech_to_text(request, option)
client.chatflow.v1.tts.text_to_audio(request, option)
```

**迁移后:**
```python
# 统一使用 dify 模块
client.dify.v1.audio.to_text(request, option)      # 音频转文本
client.dify.v1.audio.from_text(request, option)    # 文本转音频
```

### 3. 应用信息 API

**迁移前:**
```python
# Chat 模块
client.chat.v1.app.info(request, option)
client.chat.v1.app.parameters(request, option)
client.chat.v1.app.meta(request, option)
client.chat.v1.app.site(request, option)

# Completion 模块
client.completion.v1.info.get_info(request, option)
client.completion.v1.info.get_parameters(request, option)
client.completion.v1.info.get_site(request, option)

# Chatflow 模块
client.chatflow.v1.application.info(request, option)
client.chatflow.v1.application.parameters(request, option)
client.chatflow.v1.application.meta(request, option)
client.chatflow.v1.application.site(request, option)

# Workflow 模块
client.workflow.v1.workflow.info(request, option)
client.workflow.v1.workflow.parameters(request, option)
client.workflow.v1.workflow.site(request, option)
```

**迁移后:**
```python
# 统一使用 dify 模块
client.dify.v1.info.get(request, option)           # 获取应用信息
client.dify.v1.info.parameters(request, option)    # 获取应用参数
client.dify.v1.info.meta(request, option)          # 获取应用元数据
client.dify.v1.info.site(request, option)          # 获取站点设置
```

### 4. 反馈 API

**迁移前:**
```python
# Chat 模块
client.chat.v1.feedback.submit(request, option)
client.chat.v1.feedback.list(request, option)

# Completion 模块
client.completion.v1.feedback.message_feedback(request, option)
client.completion.v1.feedback.get_feedbacks(request, option)

# Chatflow 模块
client.chatflow.v1.feedback.message(request, option)
client.chatflow.v1.feedback.list(request, option)
```

**迁移后:**
```python
# 统一使用 dify 模块
client.dify.v1.feedback.submit(request, option)    # 提交反馈
client.dify.v1.feedback.list(request, option)      # 获取反馈列表
```

## 迁移步骤

### 步骤 1: 更新导入语句

**迁移前:**
```python
from dify_oapi.api.chat.v1.model.upload_file_request import UploadFileRequest
from dify_oapi.api.completion.v1.model.audio.text_to_audio_request import TextToAudioRequest
```

**迁移后:**
```python
from dify_oapi.api.dify.v1.model.upload_file_request import UploadFileRequest
from dify_oapi.api.dify.v1.model.text_to_audio_request import TextToAudioRequest
```

### 步骤 2: 更新API调用

将所有系统级API调用更改为使用 `client.dify.v1` 前缀。

### 步骤 3: 测试验证

确保所有功能正常工作，API响应格式保持一致。

## 向后兼容性

- 原有的API调用方式仍然可用
- 模型类保持相同的接口
- 响应格式保持不变

## 最佳实践

1. **优先使用系统级API**: 对于文件上传、音频处理、应用信息和反馈功能，优先使用 `client.dify.v1` 中的API
2. **保留业务逻辑API**: 各模块特有的业务逻辑API（如聊天、完成、工作流执行）保持在原模块中
3. **统一错误处理**: 系统级API使用统一的错误处理机制
4. **文档更新**: 更新相关文档和示例代码

## 示例代码

完整的使用示例请参考 `examples/dify_system_apis.py` 文件。

## 常见问题

### Q: 原有代码是否需要立即迁移？
A: 不需要。原有API调用方式仍然可用，可以渐进式迁移。

### Q: 迁移后性能是否有影响？
A: 没有性能影响，底层实现保持不变。

### Q: 如何处理模型类的变化？
A: 大部分模型类保持不变，只是导入路径发生变化。

### Q: 是否所有API都需要迁移？
A: 只有系统级的通用API需要迁移，业务特定的API保持在原模块中。