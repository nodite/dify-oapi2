#!/usr/bin/env python3
"""
Tests for Chatflow Examples

This module tests all chatflow examples for syntax validation, import correctness,
environment variable handling, safety prefix usage, and error handling coverage.
"""

import ast
import os
import sys
from pathlib import Path
from unittest.mock import MagicMock, patch

import pytest


class TestChatflowExamples:
    """Test class for all chatflow examples."""

    @pytest.fixture
    def examples_dir(self):
        """Get the chatflow examples directory."""
        return Path(__file__).parent.parent.parent.parent.parent / "examples" / "chatflow" / "chatflow"

    @pytest.fixture
    def example_files(self, examples_dir):
        """Get all Python example files."""
        return list(examples_dir.glob("*.py"))

    def test_example_files_exist(self, examples_dir):
        """Test that all required example files exist."""
        required_files = ["send_chat_message.py", "stop_chat_message.py", "get_suggested_questions.py"]

        for filename in required_files:
            file_path = examples_dir / filename
            assert file_path.exists(), f"Required example file {filename} does not exist"

    def test_syntax_validation(self, example_files):
        """Test that all example files have valid Python syntax."""
        for file_path in example_files:
            with open(file_path, encoding="utf-8") as f:
                content = f.read()

            try:
                ast.parse(content)
            except SyntaxError as e:
                pytest.fail(f"Syntax error in {file_path.name}: {e}")

    def test_import_correctness(self, example_files):
        """Test that all imports in example files are correct."""
        for file_path in example_files:
            with open(file_path, encoding="utf-8") as f:
                content = f.read()

            # Parse the AST to check imports
            tree = ast.parse(content)

            for node in ast.walk(tree):
                if isinstance(node, ast.ImportFrom):
                    # Check that imports start with expected modules
                    if node.module:
                        assert node.module.startswith("dify_oapi") or node.module in ["asyncio", "os", "io"], (
                            f"Unexpected import in {file_path.name}: {node.module}"
                        )

    def test_environment_variable_handling(self, example_files):
        """Test that all examples validate required environment variables."""
        for file_path in example_files:
            with open(file_path, encoding="utf-8") as f:
                content = f.read()

            # Check for validate_environment function
            assert "validate_environment" in content, f"Missing validate_environment function in {file_path.name}"

            # Check for API_KEY validation
            assert "API_KEY" in content, f"Missing API_KEY validation in {file_path.name}"

            # Check for ValueError raising
            assert "ValueError" in content, f"Missing ValueError handling in {file_path.name}"

    def test_safety_prefix_usage(self, example_files):
        """Test that examples use safety prefixes where appropriate."""
        for file_path in example_files:
            with open(file_path, encoding="utf-8") as f:
                content = f.read()

            # Check for user identifiers with safe prefixes
            if "user-" in content:
                # Examples should use safe user identifiers
                assert any(safe_id in content for safe_id in ["user-123", "user-alice", "user-bob", "user-charlie"]), (
                    f"Missing safe user identifiers in {file_path.name}"
                )

    def test_error_handling_coverage(self, example_files):
        """Test that all examples include proper error handling."""
        for file_path in example_files:
            with open(file_path, encoding="utf-8") as f:
                content = f.read()

            # Check for try-except blocks
            assert "try:" in content, f"Missing try-except blocks in {file_path.name}"
            assert "except" in content, f"Missing exception handling in {file_path.name}"

            # Check for success/error response handling
            assert "response.success" in content, f"Missing response.success check in {file_path.name}"
            assert "response.msg" in content, f"Missing response.msg handling in {file_path.name}"

    def test_main_function_exists(self, example_files):
        """Test that all examples have a main function."""
        for file_path in example_files:
            with open(file_path, encoding="utf-8") as f:
                content = f.read()

            assert "def main():" in content, f"Missing main function in {file_path.name}"
            assert 'if __name__ == "__main__":' in content, f"Missing main guard in {file_path.name}"

    @patch.dict(os.environ, {"API_KEY": "test-api-key"})
    @patch("dify_oapi.client.Client")
    def test_send_chat_message_example(self, mock_client_class):
        """Test send_chat_message.py example execution."""
        # Mock the client and its methods
        mock_client = MagicMock()
        mock_client_class.builder.return_value.domain.return_value.build.return_value = mock_client

        # Mock successful response
        mock_response = MagicMock()
        mock_response.success = True
        mock_response.id = "msg-123"
        mock_response.conversation_id = "conv-123"
        mock_response.answer = "Test answer"
        mock_response.message_files = []

        mock_client.chatflow.v1.chatflow.send.return_value = mock_response
        mock_client.chatflow.v1.chatflow.asend.return_value = mock_response

        # Import and test the example
        examples_dir = Path(__file__).parent.parent.parent.parent.parent / "examples" / "chatflow" / "chatflow"
        sys.path.insert(0, str(examples_dir))

        try:
            import send_chat_message

            # Test individual functions
            send_chat_message.send_chat_message_blocking()
            send_chat_message.send_chat_message_with_file()
            send_chat_message.send_chat_message_with_conversation()

            # Verify client was called
            assert mock_client.chatflow.v1.chatflow.send.called

        finally:
            sys.path.remove(str(examples_dir))
            if "send_chat_message" in sys.modules:
                del sys.modules["send_chat_message"]

    @patch.dict(os.environ, {"API_KEY": "test-api-key"})
    @patch("dify_oapi.client.Client")
    def test_stop_chat_message_example(self, mock_client_class):
        """Test stop_chat_message.py example execution."""
        # Mock the client and its methods
        mock_client = MagicMock()
        mock_client_class.builder.return_value.domain.return_value.build.return_value = mock_client

        # Mock successful response
        mock_response = MagicMock()
        mock_response.success = True
        mock_response.result = "success"

        mock_client.chatflow.v1.chatflow.stop.return_value = mock_response
        mock_client.chatflow.v1.chatflow.astop.return_value = mock_response

        # Import and test the example
        examples_dir = Path(__file__).parent.parent.parent.parent.parent / "examples" / "chatflow" / "chatflow"
        sys.path.insert(0, str(examples_dir))

        try:
            import stop_chat_message

            # Test individual functions
            stop_chat_message.stop_chat_message()
            stop_chat_message.demonstrate_streaming_with_stop()

            # Verify client was called
            assert mock_client.chatflow.v1.chatflow.stop.called

        finally:
            sys.path.remove(str(examples_dir))
            if "stop_chat_message" in sys.modules:
                del sys.modules["stop_chat_message"]

    @patch.dict(os.environ, {"API_KEY": "test-api-key"})
    @patch("dify_oapi.client.Client")
    def test_get_suggested_questions_example(self, mock_client_class):
        """Test get_suggested_questions.py example execution."""
        # Mock the client and its methods
        mock_client = MagicMock()
        mock_client_class.builder.return_value.domain.return_value.build.return_value = mock_client

        # Mock successful response
        mock_response = MagicMock()
        mock_response.success = True
        mock_response.result = "success"
        mock_response.data = ["What is AI?", "How does machine learning work?", "Tell me more about this topic"]

        mock_client.chatflow.v1.chatflow.suggested.return_value = mock_response
        mock_client.chatflow.v1.chatflow.asuggested.return_value = mock_response

        # Import and test the example
        examples_dir = Path(__file__).parent.parent.parent.parent.parent / "examples" / "chatflow" / "chatflow"
        sys.path.insert(0, str(examples_dir))

        try:
            import get_suggested_questions

            # Test individual functions
            get_suggested_questions.get_suggested_questions()
            get_suggested_questions.demonstrate_conversation_flow()

            # Verify client was called
            assert mock_client.chatflow.v1.chatflow.suggested.called

        finally:
            sys.path.remove(str(examples_dir))
            if "get_suggested_questions" in sys.modules:
                del sys.modules["get_suggested_questions"]

    def test_example_completeness(self, examples_dir):
        """Test that all 3 chatflow APIs are covered in examples."""
        expected_apis = {
            "send_chat_message.py": ["send", "streaming", "blocking", "async"],
            "stop_chat_message.py": ["stop", "task_id", "async"],
            "get_suggested_questions.py": ["suggested", "message_id", "async"],
        }

        for filename, keywords in expected_apis.items():
            file_path = examples_dir / filename
            assert file_path.exists(), f"Missing example file: {filename}"

            with open(file_path, encoding="utf-8") as f:
                content = f.read()

            for keyword in keywords:
                assert keyword in content, f"Missing keyword '{keyword}' in {filename}"

    def test_docstring_presence(self, example_files):
        """Test that all example files have proper docstrings."""
        for file_path in example_files:
            with open(file_path, encoding="utf-8") as f:
                content = f.read()

            # Check for module docstring
            tree = ast.parse(content)
            if tree.body and isinstance(tree.body[0], ast.Expr) and isinstance(tree.body[0].value, ast.Constant):
                docstring = tree.body[0].value.value
                assert isinstance(docstring, str), f"Missing module docstring in {file_path.name}"
                assert len(docstring.strip()) > 0, f"Empty module docstring in {file_path.name}"
            else:
                pytest.fail(f"Missing module docstring in {file_path.name}")

    def test_async_support(self, example_files):
        """Test that examples include both sync and async variants."""
        for file_path in example_files:
            with open(file_path, encoding="utf-8") as f:
                content = f.read()

            # Check for async imports and usage
            assert "import asyncio" in content, f"Missing asyncio import in {file_path.name}"
            assert "async def" in content, f"Missing async functions in {file_path.name}"
            assert "await " in content, f"Missing await usage in {file_path.name}"
            assert "asyncio.run(" in content, f"Missing asyncio.run usage in {file_path.name}"

    def test_builder_pattern_usage(self, example_files):
        """Test that examples use builder patterns correctly."""
        for file_path in example_files:
            with open(file_path, encoding="utf-8") as f:
                content = f.read()

            # Check for builder pattern usage
            assert ".builder()" in content, f"Missing builder pattern usage in {file_path.name}"
            assert ".build()" in content, f"Missing build() calls in {file_path.name}"

    def test_request_option_usage(self, example_files):
        """Test that examples use RequestOption correctly."""
        for file_path in example_files:
            with open(file_path, encoding="utf-8") as f:
                content = f.read()

            # Check for RequestOption usage
            assert "RequestOption" in content, f"Missing RequestOption usage in {file_path.name}"
            assert ".api_key(" in content, f"Missing api_key configuration in {file_path.name}"


if __name__ == "__main__":
    pytest.main([__file__])
