# Dify-OAPI2 项目概览

## 项目描述
Dify-OAPI2 是一个用于与 Dify Service-API 交互的 Python SDK。该 SDK 为开发者提供了流畅、类型安全的接口，用于构建基于 Dify API 服务的 AI 应用，包括聊天、文本补全、知识库和工作流功能。

> 本项目基于 https://github.com/QiMington/dify-oapi 重构，支持最新的 Dify API。

## 目录结构

### 主要模块

```
dify-oapi2/
├── dify_oapi/                    # SDK 根包
│   ├── __init__.py              # 包初始化
│   ├── client.py                # 主客户端接口
│   ├── api/                     # API 服务模块
│   │   ├── chat/                # 聊天 API 服务
│   │   │   ├── service.py       # 服务类
│   │   │   └── v1/              # v1 版本实现
│   │   │       ├── version.py   # 版本访问器
│   │   │       ├── model/       # 数据模型
│   │   │       └── resource/    # 资源实现
│   │   ├── completion/          # 文本补全 API 服务
│   │   ├── dify/                # 核心 Dify API 服务
│   │   ├── knowledge/      # 知识库 API 服务 (39个API)
│   │   │   └── v1/
│   │   │       └── model/
│   │   │           ├── dataset/     # 数据集模型
│   │   │           ├── document/    # 文档模型
│   │   │           ├── metadata/    # 元数据模型
│   │   │           ├── segment/     # 分段模型
│   │   │           └── tag/         # 标签模型
│   │   └── workflow/            # 工作流 API 服务
│   └── core/                    # 核心功能
│       ├── http/                # HTTP 传输层
│       │   └── transport/       # 同步/异步传输实现
│       │       ├── sync_transport.py
│       │       └── async_transport.py
│       ├── model/               # 基础模型
│       │   ├── base_request.py  # 基础请求模型
│       │   ├── base_response.py # 基础响应模型
│       │   ├── config.py        # 配置模型
│       │   └── request_option.py # 请求选项
│       ├── utils/               # 工具函数
│       ├── const.py             # 常量定义
│       ├── enum.py              # 枚举定义
│       ├── json.py              # JSON 处理
│       ├── log.py               # 日志配置
│       ├── misc.py              # 杂项工具
│       └── type.py              # 类型定义
├── docs/                        # 文档
│   ├── overview.md              # 项目概览
│   ├── datasets/                # 知识库 API 文档
│   └── completion/              # 补全 API 文档
├── examples/                    # 使用示例
│   ├── chat/                    # 聊天示例
│   ├── completion/              # 补全示例
│   └── knowledge/          # 知识库示例
├── tests/                       # 测试套件
│   └── knowledge/          # 知识库测试
├── .github/workflows/           # GitHub Actions
├── pyproject.toml               # 项目配置
├── Makefile                     # 构建脚本
└── README.md                    # 项目说明
```

### API 结构模式
每个 API 服务遵循一致的结构：
- **service.py**: 服务类，初始化版本特定的实现
- **v1/**: API 的 v1 版本实现
  - **version.py**: 提供对不同资源的访问
  - **model/**: 请求和响应的数据模型
  - **resource/**: 实现实际 API 端点的资源类

## 技术栈

### 编程语言
- **Python 3.10+**: SDK 基于 Python 3.10 或更高版本构建

### 核心依赖
- **pydantic** (>=1.10,<3.0.0): 数据验证和设置管理
- **httpx** (>=0.24,<1.0): 现代 HTTP 客户端

### 开发依赖
- **pytest** (^8.3.3): 测试框架
- **pytest-asyncio** (^1.1.0): 异步测试支持
- **pytest-env** (^1.1.5): 测试环境变量
- **pre-commit** (^4.2.0): Git 钩子
- **commitizen** (^3.29.0): 提交规范

### 代码质量工具
- **ruff** (^0.6.0): 快速 Python 代码检查和格式化
- **mypy** (^1.16.1): 静态类型检查
- **black** (^24.0.0): 代码格式化
- **pre-commit** (^4.0.1): Git 钩子管理

### 构建系统
- **poetry-core**: 构建后端
- **Poetry**: 依赖管理和打包

## 核心特性

1. **构建器模式**: SDK 使用构建器模式创建请求，提供流畅的链式接口
2. **同步和异步支持**: 支持同步和异步 API 调用
3. **流式响应**: 支持聊天和补全 API 的实时流式响应
4. **类型安全**: 全面的类型提示和 Pydantic 验证
5. **文件上传**: 支持图片和文档上传
6. **现代 HTTP 客户端**: 基于 httpx 构建可靠的 API 通信
7. **多服务支持**: 支持多种 Dify 服务（聊天、补全、知识库等）

## API 服务

### 聊天 API
提供与 Dify 聊天功能的交互，包括：
- 创建聊天消息
- 管理对话历史
- 音频转文本处理
- 流式聊天响应
- 文件上传支持（图片、文档）

### 补全 API
通过 Dify API 提供文本生成和补全功能：
- 文本生成和补全
- 自定义输入参数
- 流式支持

### 知识库 API (39个API)
与 Dify 知识库功能接口，包括：
- **数据集管理**: 数据集的 CRUD 操作
- **文档管理**: 上传、处理和管理文档
- **分段管理**: 细粒度内容分段
- **元数据和标签**: 自定义元数据和知识类型标签
- **检索功能**: 高级搜索和检索功能

### 工作流 API
提供对 Dify 工作流功能的访问：
- 自动化工作流执行
- 参数配置
- 状态监控

### Dify 核心 API
Dify 服务的基础功能。
