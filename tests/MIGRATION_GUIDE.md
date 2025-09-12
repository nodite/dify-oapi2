# 测试结构迁移指南

## 概述

本次重组将测试结构调整为与 `dify_oapi/api` 代码结构完全对应的规范化结构。

## 主要变化

### 1. 目录结构对应
- 新结构与 `dify_oapi/api` 完全对应
- 每个 API 模块都有对应的测试目录
- 资源、模型、集成测试分离

### 2. 测试文件简化
- 遵循最小化代码原则
- 每个资源类对应一个测试文件
- 集中测试核心功能

### 3. 测试类型分层
```
tests/
├── {api}/                    # API 模块测试
│   ├── v1/                   # 版本测试
│   │   ├── resource/         # 资源测试
│   │   ├── model/            # 模型测试
│   │   └── test_integration.py # 集成测试
│   └── test_service.py       # 服务测试
└── test_client.py            # 客户端测试
```

## 迁移步骤

1. **运行迁移脚本**:
   ```bash
   python migrate_tests.py
   ```

2. **验证新结构**:
   ```bash
   pytest tests/ -v
   ```

3. **更新 CI/CD 配置**:
   - 确保测试路径正确
   - 更新覆盖率配置

## 新测试结构优势

1. **结构清晰**: 与源代码结构完全对应
2. **易于维护**: 每个资源有独立的测试文件
3. **测试分层**: 单元测试、集成测试分离
4. **代码最小化**: 只测试核心功能，避免冗余

## 测试编写规范

### 资源测试
```python
class TestResource:
    @pytest.fixture
    def resource(self):
        return Resource()
    
    def test_method(self, resource):
        with patch('...') as mock:
            mock.return_value = MagicMock(result="success")
            result = resource.method(MagicMock(), MagicMock())
            assert result.result == "success"
```

### 模型测试
```python
class TestModels:
    def test_valid_model(self):
        model = Model.builder().field("value").build()
        assert model.field == "value"
    
    def test_invalid_model(self):
        with pytest.raises(ValidationError):
            Model.builder().build()
```

### 集成测试
```python
class TestIntegration:
    @pytest.fixture
    def client(self):
        return Client.builder().domain("https://api.dify.ai").build()
    
    def test_workflow(self, client):
        with patch('...') as mock:
            mock.return_value = MagicMock(id="123")
            result = client.api.v1.resource.method(req, option)
            assert result.id == "123"
```

## 注意事项

1. **备份**: 旧测试已备份到 `tests_backup/`
2. **依赖**: 确保所有测试依赖正确导入
3. **Mock**: 使用统一的 Mock 模式
4. **断言**: 使用简单明确的断言

## 后续工作

1. 根据实际 API 调整测试内容
2. 添加更多边界情况测试
3. 完善错误处理测试
4. 优化测试性能