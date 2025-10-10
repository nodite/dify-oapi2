# Dify-OAPI2 项目概览

## 项目简介

Dify-OAPI2 是一个现代化的 Python SDK，用于与 Dify Service-API 进行交互。该项目基于 [dify-oapi](https://github.com/QiMington/dify-oapi) 完全重构，采用现代 Python 实践，全面支持最新的 Dify API。

- **项目名称**: dify-oapi2
- **版本**: 1.0.1
- **许可证**: MIT
- **Python 版本**: 3.10+
- **PyPI**: https://pypi.org/project/dify-oapi2/
- **源代码**: https://github.com/nodite/dify-oapi2

## 技术栈

### 核心技术

- **编程语言**: Python 3.10+
- **HTTP 客户端**: httpx (支持同步/异步，带连接池优化)
- **类型系统**: Pydantic 2.x (数据验证和类型安全)
- **架构模式**:
  - Builder 模式 (流式 API 设计)
  - Service 层模式 (服务分层)
- **异步支持**: 完整的 async/await 支持，AsyncGenerator 流式响应

### 开发工具

- **代码质量**:
  - Ruff (^0) - 快速的 Python linter 和 formatter (替代 Black + isort + flake8)
  - MyPy (^1) - 静态类型检查
  - Black (^25) - 代码格式化备选

- **测试框架**:
  - pytest (^8) - 测试框架
  - pytest-asyncio (^1) - 异步测试支持
  - pytest-env (^1) - 环境变量管理

- **开发流程**:
  - pre-commit (^4) - Git hooks 自动化代码质量检查
  - commitizen (^4) - 语义化版本控制和 changelog 生成
  - Poetry - 依赖管理和打包工具

### 核心依赖

```toml
[tool.poetry.dependencies]
python = ">=3.10"
pydantic = "^2"    # 数据验证和类型安全
httpx = "^0"       # 现代 HTTP 客户端
```

## 项目结构

```
dify-oapi2/
├── dify_oapi/              # 主 SDK 包
│   ├── __init__.py
│   ├── client.py           # 主客户端接口 (Builder 模式)
│   ├── api/                # API 服务模块
│   │   ├── chat/           # Chat API (18 APIs)
│   │   │   ├── service.py  # 服务层
│   │   │   └── v1/         # v1 版本实现
│   │   │       ├── resource/   # 资源层 (annotation, chat, conversation, message)
│   │   │       └── model/      # 数据模型
│   │   ├── chatflow/       # Chatflow API (15 APIs)
│   │   │   ├── service.py
│   │   │   └── v1/         # 资源: annotation, chatflow, conversation
│   │   ├── completion/     # Completion API (10 APIs)
│   │   │   ├── service.py
│   │   │   └── v1/         # 资源: annotation, completion
│   │   ├── dify/           # Dify Core API (9 APIs)
│   │   │   ├── service.py
│   │   │   └── v1/         # 资源: audio, feedback, file, info
│   │   ├── knowledge/      # Knowledge Base API (33 APIs)
│   │   │   ├── service.py
│   │   │   └── v1/         # 资源: chunk, dataset, document, model, segment, tag
│   │   └── workflow/       # Workflow API (4 APIs)
│   │       ├── service.py
│   │       └── v1/         # 资源: workflow
│   └── core/               # 核心功能
│       ├── http/           # HTTP 传输层
│       │   └── transport/  # 传输实现
│       │       ├── sync_transport.py      # 同步传输
│       │       ├── async_transport.py     # 异步传输
│       │       ├── connection_pool.py     # 连接池管理
│       │       └── _misc.py               # 辅助工具
│       ├── model/          # 基础模型
│       │   ├── base_request.py    # 请求基类
│       │   ├── base_response.py   # 响应基类
│       │   ├── config.py          # 配置模型
│       │   ├── request_option.py  # 请求选项
│       │   ├── raw_request.py     # 原始请求
│       │   └── raw_response.py    # 原始响应
│       ├── utils/          # 工具函数
│       │   └── strings.py  # 字符串处理
│       ├── const.py        # 常量定义
│       ├── enum.py         # 枚举类型
│       ├── json.py         # JSON 处理
│       ├── log.py          # 日志配置
│       ├── misc.py         # 杂项工具
│       └── type.py         # 类型定义
├── docs/                   # 文档
│   ├── overview.md         # 项目概览 (本文档)
│   ├── chat/               # Chat API 文档
│   ├── chatflow/           # Chatflow API 文档
│   ├── completion/         # Completion API 文档
│   ├── dify/               # Dify Core API 文档
│   ├── knowledge/          # Knowledge Base API 文档
│   └── workflow/           # Workflow API 文档
├── examples/               # 完整示例代码
│   ├── README.md           # 示例总览
│   ├── connection_pool_example.py  # 连接池优化示例
│   ├── chat/               # Chat API 示例
│   ├── chatflow/           # Chatflow API 示例
│   ├── completion/         # Completion API 示例
│   ├── dify/               # Dify Core API 示例
│   ├── knowledge/          # Knowledge Base API 示例
│   └── workflow/           # Workflow API 示例
├── tests/                  # 测试套件
│   ├── conftest.py         # pytest 配置
│   ├── test_client.py      # 客户端测试
│   ├── chat/               # Chat API 测试
│   ├── chatflow/           # Chatflow API 测试
│   ├── completion/         # Completion API 测试
│   ├── dify/               # Dify Core API 测试
│   ├── knowledge/          # Knowledge Base API 测试
│   ├── workflow/           # Workflow API 测试
│   ├── core/               # 核心功能测试
│   │   ├── test_config.py
│   │   ├── test_error_handling.py
│   │   └── test_streaming.py
│   └── integration/        # 集成测试
│       ├── test_edge_cases.py
│       ├── test_end_to_end.py
│       └── test_performance.py
├── pyproject.toml          # 项目配置 (Poetry + 工具配置)
├── poetry.lock             # 依赖锁定文件
├── poetry.toml             # Poetry 配置
├── Makefile                # 开发自动化
├── .pre-commit-config.yaml # Pre-commit hooks 配置
├── .editorconfig           # 编辑器配置
├── .gitignore              # Git 忽略文件
├── README.md               # 项目说明
├── DEVELOPMENT.md          # 开发指南
├── LICENSE                 # MIT 许可证
└── MANIFEST.in             # 打包清单
```

## API 服务模块

### 1. Chat API (18 APIs)

**资源**: annotation (6), chat (3), conversation (6), message (3)

**功能特性**:
- 交互式对话: 发送消息，支持阻塞/流式响应
- 会话管理: 完整的会话生命周期操作
- 标注系统: 创建、更新、删除标注，配置回复设置
- 消息操作: 基础消息处理和历史记录检索
- 流式支持: 实时流式聊天响应
- 类型安全: 全面的类型提示，严格的 Literal 类型

### 2. Chatflow API (15 APIs)

**资源**: annotation (6), chatflow (3), conversation (6)

**功能特性**:
- 增强聊天: 高级聊天功能，支持工作流事件
- 会话管理: 完整的会话操作，支持变量
- 标注系统: 完整的标注管理和回复配置
- 工作流集成: 与工作流事件无缝集成
- 事件流: 实时流式传输，全面的事件处理
- 类型安全: 所有预定义值使用严格的 Literal 类型

### 3. Completion API (10 APIs)

**资源**: annotation (6), completion (4)

**功能特性**:
- 文本生成: 高级文本补全和生成
- 消息处理: 发送消息并控制文本生成
- 标注管理: 创建、更新和管理标注
- 生成控制: 停止正在进行的文本生成过程
- 流式支持: 实时文本生成，支持流式响应
- 类型安全: 使用 Pydantic 模型进行完整类型验证

### 4. Knowledge Base API (33 APIs)

**资源**: chunk (4), dataset (6), document (10), model (1), segment (5), tag (7)

**功能特性**:
- 数据集管理: 完整的数据集 CRUD 操作和内容检索
- 文档处理: 文件上传、文本处理和批量管理
- 内容组织: 细粒度的分段和块管理
- 标签系统: 灵活的标签和分类系统
- 模型集成: 嵌入模型信息和配置
- 搜索检索: 高级搜索，支持多种检索策略

### 5. Workflow API (4 APIs)

**资源**: workflow (4)

**功能特性**:
- 工作流执行: 运行工作流，支持阻塞或流式响应
- 执行控制: 停止运行中的工作流并监控进度
- 日志管理: 检索详细的执行日志和运行详情
- 参数支持: 灵活的工作流参数配置

### 6. Dify Core API (9 APIs)

**资源**: audio (2), feedback (2), file (1), info (4)

**功能特性**:
- 音频处理: 语音转文本和文本转语音转换
- 反馈系统: 提交和检索用户反馈
- 文件管理: 统一的文件上传和处理
- 应用信息: 应用配置、参数和元数据访问

**总计**: 89 个 API 方法，覆盖 6 个服务

## 核心架构设计

### 1. Builder 模式

客户端和请求对象都采用 Builder 模式，提供流式、可链式调用的接口:

```python
# 客户端构建
client = (
    Client.builder()
    .domain("https://api.dify.ai")
    .max_connections(100)
    .keepalive_expiry(30.0)
    .timeout(60.0)
    .build()
)

# 请求构建
request = (
    ChatRequest.builder()
    .query("Hello")
    .user("user-123")
    .build()
)
```

### 2. 连接池优化

使用 httpx 的连接池功能，优化 TCP 连接复用，减少资源开销:

```python
# 配置参数
max_keepalive_connections: int = 20  # 每个池的最大保活连接数
max_connections: int = 100           # 每个池的最大总连接数
keepalive_expiry: float = 30.0      # 保活连接过期时间(秒)
```

### 3. 同步/异步支持

完整支持同步和异步操作:

```python
# 同步
response = client.chat.chat(request, request_option)

# 异步
response = await client.chat.achat(request, request_option)

# 流式同步
for chunk in client.chat.chat_stream(request, request_option):
    print(chunk)

# 流式异步
async for chunk in client.chat.achat_stream(request, request_option):
    print(chunk)
```

### 4. 类型安全

使用 Pydantic 2.x 进行全面的类型验证:

- 所有请求/响应模型都有完整的类型提示
- 使用 Literal 类型定义预定义值
- MyPy 静态类型检查确保类型安全

### 5. 错误处理

统一的错误处理机制:

- HTTP 错误自动重试 (可配置重试次数)
- 详细的错误信息和日志
- 异常类型层次结构

## 开发工具配置

### Ruff 配置

```toml
[tool.ruff]
line-length = 120
indent-width = 4

[tool.ruff.lint]
select = ["A", "B", "F", "N", "I", "UP", "E101", "RUF019", "RUF100", "RUF101", "S506", "W191", "W605"]
ignore = ["A002", "B904", "N805", "N806"]

[tool.ruff.format]
quote-style = "double"
indent-style = "space"
```

### MyPy 配置

```toml
[tool.mypy]
files = ["dify_oapi"]
python_version = "3.10"
strict_optional = true
ignore_missing_imports = true
check_untyped_defs = true
warn_return_any = true
warn_unreachable = true
```

### Pytest 配置

```toml
[tool.pytest.ini_options]
asyncio_mode = "auto"
testpaths = ["tests"]
python_files = ["test_*.py"]
addopts = ["--strict-markers", "--strict-config", "-ra"]
```

## 开发流程

### 环境设置

```bash
# 克隆仓库
git clone https://github.com/nodite/dify-oapi2.git
cd dify-oapi2

# 设置开发环境 (安装依赖和 pre-commit hooks)
make dev-setup
```

### 代码质量检查

```bash
# 格式化代码
make format

# 检查代码规范
make lint

# 修复可自动修复的问题
make fix

# 运行所有检查 (lint + 类型检查)
make check

# 运行 pre-commit hooks
make pre-commit
```

### 测试

```bash
# 设置环境变量
export DOMAIN="https://api.dify.ai"
export CHAT_KEY="your-chat-api-key"
export KNOWLEDGE_KEY="your-knowledge-api-key"

# 运行测试
make test

# 运行测试并生成覆盖率报告
make test-cov

# 运行特定模块测试
poetry run pytest tests/knowledge/ -v
```

### 构建和发布

```bash
# 配置 PyPI tokens (一次性设置)
poetry config http-basic.testpypi __token__ <your-testpypi-token>
poetry config http-basic.pypi __token__ <your-pypi-token>

# 构建包
make build

# 发布到 TestPyPI (测试用)
make publish-test

# 发布到 PyPI (仅维护者)
make publish
```

## 主要特性

### 1. 完整的 API 覆盖

- 89 个 API 方法
- 6 个主要服务
- 20+ 个资源类型
- 完整的 CRUD 操作

### 2. 现代 Python 实践

- Python 3.10+ 特性
- 类型提示和验证
- 异步/同步双支持
- Builder 模式设计

### 3. 性能优化

- HTTP 连接池
- TCP 连接复用
- 可配置的超时和重试
- 流式响应支持

### 4. 开发者友好

- 流式 API 设计
- 完整的文档和示例
- 全面的测试覆盖
- 自动化开发工具

### 5. 生产就绪

- 严格的类型检查
- 全面的错误处理
- 日志和监控支持
- SSL/TLS 支持

## 使用示例

### 基础用法

```python
from dify_oapi.client import Client
from dify_oapi.core.model.request_option import RequestOption
from dify_oapi.api.chat.v1.model.chat_request import ChatRequest

# 初始化客户端
client = (
    Client.builder()
    .domain("https://api.dify.ai")
    .max_connections(100)
    .keepalive_expiry(30.0)
    .build()
)

# 创建请求选项
req_option = RequestOption.builder().api_key("your-api-key").build()

# 使用 Chat API
response = client.chat.chat(
    request=ChatRequest.builder()
    .query("Hello, how are you?")
    .user("user-123")
    .build(),
    request_option=req_option
)

print(response.answer)
```

### 流式响应

```python
# 同步流式
for event in client.chat.chat_stream(request, req_option):
    if event.event == "message":
        print(event.answer, end="", flush=True)

# 异步流式
async for event in client.chat.achat_stream(request, req_option):
    if event.event == "message":
        print(event.answer, end="", flush=True)
```

### 文件上传

```python
from dify_oapi.api.dify.v1.model.file_upload_request import FileUploadRequest

# 上传文件
with open("document.pdf", "rb") as f:
    response = client.dify.file_upload(
        request=FileUploadRequest.builder()
        .file(("document.pdf", f, "application/pdf"))
        .user("user-123")
        .build(),
        request_option=req_option
    )
```

## 测试覆盖

### 单元测试

- 核心功能测试 (config, error_handling, streaming)
- 各服务 API 测试
- 模型验证测试

### 集成测试

- 端到端测试
- 边缘情况测试
- 性能测试

### 测试结构

```
tests/
├── chat/           # Chat API 测试 (18 APIs)
├── chatflow/       # Chatflow API 测试 (15 APIs)
├── completion/     # Completion API 测试 (10 APIs)
├── dify/           # Dify Core API 测试 (9 APIs)
├── knowledge/      # Knowledge Base API 测试 (33 APIs)
├── workflow/       # Workflow API 测试 (4 APIs)
├── core/           # 核心功能测试
└── integration/    # 集成测试
```

## 文档资源

- **README.md**: 项目说明和快速开始
- **DEVELOPMENT.md**: 开发指南和工作流程
- **docs/**: API 文档和使用指南
- **examples/**: 完整的示例代码集合

## 贡献指南

1. Fork 仓库
2. 创建特性分支 (`git checkout -b feature/amazing-feature`)
3. 编写代码和测试
4. 确保代码质量通过 (`make check`)
5. 运行完整测试套件 (`make test`)
6. 提交更改 (`git commit -m 'Add amazing feature'`)
7. 推送到分支 (`git push origin feature/amazing-feature`)
8. 提交 Pull Request

## 许可证

MIT License - 详见 [LICENSE](../LICENSE) 文件

## 相关链接

- **PyPI 包**: https://pypi.org/project/dify-oapi2/
- **源代码**: https://github.com/nodite/dify-oapi2
- **Dify 平台**: https://dify.ai/
- **Dify API 文档**: https://docs.dify.ai/

## 关键词

dify, ai, nlp, language-processing, python-sdk, async, type-safe, api-client
