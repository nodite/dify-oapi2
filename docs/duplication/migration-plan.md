# Dify API 迁移计划

## 概述

根据分析，各个模块中存在大量重复的系统级API，这些API应该迁移到 `dify_oapi/api/dify` 目录下作为系统级的通用API。

## 重复API分析

### 1. 文件上传 API (File Upload)
**重复位置:**
- `chat/v1/resource/file.py` - `upload()` 方法
- `completion/v1/resource/file.py` - `upload_file()` 方法  
- `chatflow/v1/resource/file.py` - `upload()` 方法
- `workflow/v1/resource/workflow.py` - `upload()` 方法

**目标位置:** `dify/v1/resource/file.py` (已存在，需要统一)

### 2. 音频处理 API (Audio/TTS)
**重复位置:**
- `chat/v1/resource/audio.py` - `to_text()`, `to_audio()` 方法
- `completion/v1/resource/audio.py` - `text_to_audio()` 方法
- `chatflow/v1/resource/tts.py` - `speech_to_text()`, `text_to_audio()` 方法

**目标位置:** `dify/v1/resource/audio.py` (已存在，需要扩展)

### 3. 应用信息 API (Application Info)
**重复位置:**
- `chat/v1/resource/app.py` - `info()`, `parameters()`, `meta()`, `site()` 方法
- `completion/v1/resource/info.py` - `get_info()`, `get_parameters()`, `get_site()` 方法
- `chatflow/v1/resource/application.py` - `info()`, `parameters()`, `meta()`, `site()` 方法
- `workflow/v1/resource/workflow.py` - `info()`, `parameters()`, `site()` 方法

**目标位置:** `dify/v1/resource/info.py` (已存在，需要扩展)

### 4. 消息反馈 API (Message Feedback)
**重复位置:**
- `chat/v1/resource/feedback.py` - `submit()`, `list()` 方法
- `completion/v1/resource/feedback.py` - `message_feedback()`, `get_feedbacks()` 方法
- `chatflow/v1/resource/feedback.py` - `message()`, `list()` 方法

**目标位置:** `dify/v1/resource/message.py` (已存在，需要扩展)

## 迁移步骤

### 步骤 1: 扩展 dify/v1/resource/file.py ✅
- [x] 统一文件上传API接口
- [x] 添加通用的文件上传方法
- [x] 确保兼容所有模块的文件上传需求

### 步骤 2: 扩展 dify/v1/resource/audio.py ✅
- [x] 添加 `speech_to_text()` 方法 (音频转文本)
- [x] 统一 `text_to_audio()` 方法 (文本转音频)
- [x] 确保支持所有音频处理场景

### 步骤 3: 扩展 dify/v1/resource/info.py ✅
- [x] 添加 `parameters()` 方法 (获取应用参数)
- [x] 添加 `meta()` 方法 (获取应用元数据)
- [x] 添加 `site()` 方法 (获取站点设置)
- [x] 统一应用信息获取接口

### 步骤 4: 创建 dify/v1/resource/feedback.py ✅
- [x] 创建新的反馈资源文件
- [x] 添加 `submit()` 方法 (提交反馈)
- [x] 添加 `list()` 方法 (获取反馈列表)
- [x] 从 message.py 中迁移相关功能

### 步骤 5: 更新 dify/v1/version.py ✅
- [x] 添加新的 Feedback 资源引用
- [x] 确保所有资源都正确初始化

### 步骤 6: 更新各模块引用 ✅
- [x] 创建系统级API使用示例
- [x] 更新 chat 模块，使用 dify 的通用API
- [x] 更新 completion 模块，使用 dify 的通用API
- [x] 更新 chatflow 模块，使用 dify 的通用API
- [x] 更新 workflow 模块，使用 dify 的通用API

### 步骤 7: 清理重复代码 ✅
- [x] 删除各模块中的重复API实现
- [x] 保留模块特有的业务逻辑API
- [x] 更新相关的模型文件引用

### 步骤 8: 更新测试和示例 ✅
- [x] 创建系统级API使用示例
- [x] 创建迁移指南文档
- [x] 创建统一API使用示例
- [x] 展示迁移优势和模块专业化
- [x] 确保向后兼容性

## 迁移原则

1. **保持向后兼容**: 原有的API调用方式仍然可用
2. **统一接口**: 所有模块使用相同的系统级API
3. **减少重复**: 消除代码重复，提高维护性
4. **模块化设计**: 系统级API独立于业务模块
5. **渐进式迁移**: 分步骤进行，确保每步都可验证

## 预期收益

1. **代码复用**: 减少重复代码约60%
2. **维护性**: 系统级API统一维护
3. **一致性**: 所有模块使用相同的API接口
4. **扩展性**: 新模块可直接使用系统级API
5. **测试覆盖**: 集中测试系统级功能

## 风险评估

1. **兼容性风险**: 低 - 保持原有接口
2. **功能风险**: 低 - 逐步迁移验证
3. **性能风险**: 无 - 不改变底层实现
4. **维护风险**: 低 - 减少重复代码

## 完成标准

- [x] 所有重复API成功迁移到dify模块
- [x] 原有功能完全保持
- [x] 清理各模块中的重复代码
- [x] 创建系统级API使用示例
- [x] 创建迁移指南文档
- [x] 实现模块专业化分工