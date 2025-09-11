# Dify系统级API示例

本目录包含了Dify统一系统级API的使用示例。这些API提供了跨所有模块的通用功能。

## 目录结构

```
dify/
├── audio/                      # 音频处理API示例 (2 APIs)
│   ├── audio_to_text.py        # 音频转文本
│   └── text_to_audio.py        # 文本转音频
├── feedback/                   # 反馈管理API示例 (2 APIs)
│   ├── submit_feedback.py      # 提交用户反馈
│   └── get_feedbacks.py        # 获取反馈列表
├── file/                       # 文件管理API示例 (1 API)
│   └── upload_file.py          # 文件上传
├── info/                       # 应用信息API示例 (4 APIs)
│   ├── get_app_info.py         # 获取应用基本信息
│   ├── get_app_parameters.py   # 获取应用配置参数
│   ├── get_app_meta.py         # 获取应用元数据
│   └── get_site_settings.py    # 获取站点设置
└── README.md                   # 本文档
```

## API概览

### 文件管理 (dify.v1.file)
- **文件上传**: 统一的文件上传接口，支持各种文件类型

### 音频处理 (dify.v1.audio)
- **音频转文本**: 将音频文件转换为文本
- **文本转音频**: 将文本转换为音频文件

### 应用信息 (dify.v1.info)
- **基本信息**: 获取应用的基本信息
- **应用参数**: 获取应用的配置参数
- **应用元数据**: 获取应用的元数据信息
- **站点设置**: 获取站点的配置设置

### 反馈管理 (dify.v1.feedback)
- **提交反馈**: 提交用户反馈（点赞/点踩）
- **获取反馈**: 获取反馈列表和统计信息

## 使用方式

### 直接使用系统级API
```python
from dify_oapi.client import Client

client = Client.builder().domain("https://api.dify.ai").build()

# 文件上传
response = client.dify.v1.file.upload(request, option)

# 音频处理
response = client.dify.v1.audio.to_text(request, option)
response = client.dify.v1.audio.from_text(request, option)

# 应用信息
response = client.dify.v1.info.get(request, option)
response = client.dify.v1.info.parameters(request, option)
response = client.dify.v1.info.meta(request, option)
response = client.dify.v1.info.site(request, option)

# 反馈管理
response = client.dify.v1.feedback.submit(request, option)
response = client.dify.v1.feedback.list(request, option)
```

### 通过业务模块使用（完全兼容）
```python
# 这些调用方式仍然有效，内部会使用dify系统级API
client.chat.v1.file.upload(request, option)
client.completion.v1.audio.text_to_audio(request, option)
client.chatflow.v1.application.info(request, option)
client.workflow.v1.feedback.submit(request, option)
```

## 运行示例

### 环境设置
```bash
export DOMAIN="https://api.dify.ai"
export API_KEY="your-api-key"
```

### 运行单个示例
```bash
# 文件上传示例
python examples/dify/file/upload_file.py

# 音频处理示例
python examples/dify/audio/audio_to_text.py
python examples/dify/audio/text_to_audio.py

# 应用信息示例
python examples/dify/info/get_app_info.py
python examples/dify/info/get_app_parameters.py
python examples/dify/info/get_app_meta.py
python examples/dify/info/get_site_settings.py

# 反馈管理示例
python examples/dify/feedback/submit_feedback.py
python examples/dify/feedback/get_feedbacks.py
```

## 特性

### 统一接口
- 所有系统级功能通过dify模块统一提供
- 一致的API调用方式和响应格式
- 统一的错误处理和异常管理

### 类型安全
- 完整的类型提示支持
- Pydantic模型验证
- 编译时类型检查

### 异步支持
- 所有API都提供同步和异步版本
- 支持高并发场景
- 异步上下文管理

### 向后兼容
- 保持所有原有API调用方式
- 渐进式迁移支持
- 无需修改现有代码

## 最佳实践

1. **优先使用系统级API**: 新项目建议直接使用 `client.dify.v1.*` 接口
2. **统一错误处理**: 使用一致的异常处理模式
3. **资源管理**: 正确关闭文件句柄和网络连接
4. **异步优化**: 在高并发场景下使用异步版本的API
5. **配置管理**: 使用环境变量管理API密钥和域名

## 相关文档

- [项目README](../../README.md) - 项目总体介绍
- [重复清理文档](../../docs/duplication/) - 了解API统一的背景
- [其他模块示例](../) - 查看业务特定的API示例