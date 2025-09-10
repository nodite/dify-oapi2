#!/usr/bin/env python3
"""
Tests for File Examples

This module tests file examples for syntax validation, import correctness,
environment variable handling, safety prefix usage, and error handling coverage.
"""

import ast
import os
import sys
from pathlib import Path
from unittest.mock import MagicMock, patch

import pytest


class TestFileExamples:
    """Test class for file examples."""

    @pytest.fixture
    def examples_dir(self):
        """Get the file examples directory."""
        return Path(__file__).parent.parent.parent.parent.parent / "examples" / "chatflow" / "file"

    @pytest.fixture
    def example_files(self, examples_dir):
        """Get all Python example files."""
        return list(examples_dir.glob("*.py"))

    def test_example_files_exist(self, examples_dir):
        """Test that all required example files exist."""
        required_files = ["upload_file.py"]

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

            # Check for [Example] prefix in file names and content
            assert "[Example]" in content, f"Missing [Example] safety prefix in {file_path.name}"

            # Check for safe user identifiers
            if "user-" in content:
                assert "user-123" in content, f"Missing safe user identifier in {file_path.name}"

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

    def test_file_handling_functions(self, example_files):
        """Test that examples include proper file handling functions."""
        for file_path in example_files:
            with open(file_path, encoding="utf-8") as f:
                content = f.read()

            # Check for file creation functions
            assert "create_sample" in content, f"Missing sample file creation functions in {file_path.name}"

            # Check for BytesIO usage
            assert "BytesIO" in content, f"Missing BytesIO usage in {file_path.name}"

            # Check for file upload functionality
            assert "upload" in content, f"Missing upload functionality in {file_path.name}"

    @patch.dict(os.environ, {"API_KEY": "test-api-key"})
    @patch("dify_oapi.client.Client")
    def test_upload_file_example(self, mock_client_class):
        """Test upload_file.py example execution."""
        # Mock the client and its methods
        mock_client = MagicMock()
        mock_client_class.builder.return_value.domain.return_value.build.return_value = mock_client

        # Mock successful response
        mock_response = MagicMock()
        mock_response.success = True
        mock_response.id = "file-123"
        mock_response.name = "[Example]_sample_document.txt"
        mock_response.size = 1024
        mock_response.extension = "txt"
        mock_response.mime_type = "text/plain"

        mock_client.chatflow.v1.file.upload.return_value = mock_response
        mock_client.chatflow.v1.file.aupload.return_value = mock_response

        # Import and test the example
        examples_dir = Path(__file__).parent.parent.parent.parent.parent / "examples" / "chatflow" / "file"
        sys.path.insert(0, str(examples_dir))

        try:
            import upload_file

            # Test individual functions
            upload_file.upload_text_file()
            upload_file.upload_json_file()
            upload_file.upload_csv_file()
            upload_file.upload_file_with_error_handling()
            upload_file.demonstrate_file_usage_workflow()

            # Verify client was called
            assert mock_client.chatflow.v1.file.upload.called

        finally:
            sys.path.remove(str(examples_dir))
            if "upload_file" in sys.modules:
                del sys.modules["upload_file"]

    def test_example_completeness(self, examples_dir):
        """Test that the file API is covered in examples."""
        expected_apis = {"upload_file.py": ["upload", "file", "BytesIO", "async", "multipart"]}

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

    def test_file_type_coverage(self, example_files):
        """Test that examples cover different file types."""
        for file_path in example_files:
            with open(file_path, encoding="utf-8") as f:
                content = f.read()

            # Check for different file type examples
            file_types = ["text", "json", "csv"]
            for file_type in file_types:
                assert file_type in content.lower(), f"Missing {file_type} file type example in {file_path.name}"

    def test_error_scenarios_coverage(self, example_files):
        """Test that examples cover various error scenarios."""
        for file_path in example_files:
            with open(file_path, encoding="utf-8") as f:
                content = f.read()

            # Check for error handling scenarios
            error_codes = ["413", "415", "400"]  # File too large, unsupported type, bad request
            for error_code in error_codes:
                assert error_code in content, f"Missing error code {error_code} handling in {file_path.name}"

    def test_workflow_demonstration(self, example_files):
        """Test that examples demonstrate complete workflows."""
        for file_path in example_files:
            with open(file_path, encoding="utf-8") as f:
                content = f.read()

            # Check for workflow demonstration
            assert "workflow" in content.lower(), f"Missing workflow demonstration in {file_path.name}"
            assert "file_id" in content, f"Missing file_id usage demonstration in {file_path.name}"


if __name__ == "__main__":
    pytest.main([__file__])
