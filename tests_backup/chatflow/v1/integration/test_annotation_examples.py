#!/usr/bin/env python3
"""
Tests for Annotation Examples

This module tests annotation examples for syntax validation, import correctness,
environment variable handling, safety prefix usage, and error handling coverage.
"""

import ast
import os
import sys
from pathlib import Path
from unittest.mock import MagicMock, patch

import pytest


class TestAnnotationExamples:
    """Test class for annotation examples."""

    @pytest.fixture
    def examples_dir(self):
        """Get the annotation examples directory."""
        return Path(__file__).parent.parent.parent.parent.parent / "examples" / "chatflow" / "annotation"

    @pytest.fixture
    def example_files(self, examples_dir):
        """Get all Python example files."""
        return list(examples_dir.glob("*.py"))

    def test_example_files_exist(self, examples_dir):
        """Test that all required example files exist."""
        required_files = [
            "get_annotations.py",
            "create_annotation.py",
            "update_annotation.py",
            "delete_annotation.py",
            "annotation_reply_settings.py",
            "annotation_reply_status.py",
        ]

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
                        assert node.module.startswith("dify_oapi") or node.module in ["asyncio", "os"], (
                            f"Unexpected import in {file_path.name}: {node.module}"
                        )

    def test_environment_variable_handling(self, example_files):
        """Test that all examples validate required environment variables."""
        for file_path in example_files:
            with open(file_path, encoding="utf-8") as f:
                content = f.read()

            # Check for API_KEY validation
            assert "API_KEY" in content, f"Missing API_KEY validation in {file_path.name}"

            # Check for ValueError raising
            assert "ValueError" in content, f"Missing ValueError handling in {file_path.name}"

            # Check for environment variable validation
            assert "os.getenv" in content, f"Missing environment variable access in {file_path.name}"

    def test_safety_prefix_usage(self, example_files):
        """Test that examples use safety prefixes where appropriate."""
        for file_path in example_files:
            with open(file_path, encoding="utf-8") as f:
                content = f.read()

            # Check for [Example] prefix in annotation content
            # Only files that create or modify annotations need [Example] prefix
            if file_path.name in ["create_annotation.py", "update_annotation.py", "delete_annotation.py"]:
                assert "[Example]" in content, f"Missing [Example] safety prefix in {file_path.name}"

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
        """Test that all examples have a main guard."""
        for file_path in example_files:
            with open(file_path, encoding="utf-8") as f:
                content = f.read()

            assert 'if __name__ == "__main__":' in content, f"Missing main guard in {file_path.name}"

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

    @patch.dict(os.environ, {"API_KEY": "test-api-key"})
    @patch("dify_oapi.client.Client")
    def test_get_annotations_example(self, mock_client_class):
        """Test get_annotations.py example execution."""
        # Mock the client and its methods
        mock_client = MagicMock()
        mock_client_class.builder.return_value.domain.return_value.build.return_value = mock_client

        # Mock successful response
        mock_annotation = MagicMock()
        mock_annotation.id = "annotation-123"
        mock_annotation.question = "[Example] What is AI?"
        mock_annotation.answer = "[Example] AI is artificial intelligence..."
        mock_annotation.hit_count = 5
        mock_annotation.created_at = 1234567890

        mock_response = MagicMock()
        mock_response.success = True
        mock_response.data = [mock_annotation]
        mock_response.page = 1
        mock_response.limit = 20
        mock_response.total = 1
        mock_response.has_more = False

        mock_client.chatflow.v1.annotation.list.return_value = mock_response
        mock_client.chatflow.v1.annotation.alist.return_value = mock_response

        # Import and test the example
        examples_dir = Path(__file__).parent.parent.parent.parent.parent / "examples" / "chatflow" / "annotation"
        sys.path.insert(0, str(examples_dir))

        try:
            import get_annotations

            # Test individual functions
            get_annotations.get_annotations_sync()
            get_annotations.get_annotations_with_pagination()

            # Verify client was called
            assert mock_client.chatflow.v1.annotation.list.called

        finally:
            sys.path.remove(str(examples_dir))
            if "get_annotations" in sys.modules:
                del sys.modules["get_annotations"]

    @patch.dict(os.environ, {"API_KEY": "test-api-key"})
    @patch("dify_oapi.client.Client")
    def test_create_annotation_example(self, mock_client_class):
        """Test create_annotation.py example execution."""
        # Mock the client and its methods
        mock_client = MagicMock()
        mock_client_class.builder.return_value.domain.return_value.build.return_value = mock_client

        # Mock successful response
        mock_response = MagicMock()
        mock_response.success = True
        mock_response.id = "annotation-123"
        mock_response.question = "[Example] What is machine learning?"
        mock_response.answer = "[Example] Machine learning is a subset of AI..."
        mock_response.hit_count = 0
        mock_response.created_at = 1234567890

        mock_client.chatflow.v1.annotation.create.return_value = mock_response
        mock_client.chatflow.v1.annotation.acreate.return_value = mock_response

        # Import and test the example
        examples_dir = Path(__file__).parent.parent.parent.parent.parent / "examples" / "chatflow" / "annotation"
        sys.path.insert(0, str(examples_dir))

        try:
            import create_annotation

            # Test individual functions
            create_annotation.create_annotation_sync()

            # Verify client was called
            assert mock_client.chatflow.v1.annotation.create.called

        finally:
            sys.path.remove(str(examples_dir))
            if "create_annotation" in sys.modules:
                del sys.modules["create_annotation"]

    @patch.dict(os.environ, {"API_KEY": "test-api-key", "ANNOTATION_ID": "test-annotation-123"})
    @patch("dify_oapi.client.Client")
    def test_update_annotation_example(self, mock_client_class):
        """Test update_annotation.py example execution."""
        # Mock the client and its methods
        mock_client = MagicMock()
        mock_client_class.builder.return_value.domain.return_value.build.return_value = mock_client

        # Mock successful response
        mock_response = MagicMock()
        mock_response.success = True
        mock_response.id = "annotation-123"
        mock_response.question = "[Example] What is deep learning?"
        mock_response.answer = "[Example] Deep learning is a subset of machine learning..."
        mock_response.hit_count = 3
        mock_response.created_at = 1234567890

        mock_client.chatflow.v1.annotation.update.return_value = mock_response
        mock_client.chatflow.v1.annotation.aupdate.return_value = mock_response

        # Import and test the example
        examples_dir = Path(__file__).parent.parent.parent.parent.parent / "examples" / "chatflow" / "annotation"
        sys.path.insert(0, str(examples_dir))

        try:
            import update_annotation

            # Test individual functions
            update_annotation.update_annotation_sync()

            # Verify client was called
            assert mock_client.chatflow.v1.annotation.update.called

        finally:
            sys.path.remove(str(examples_dir))
            if "update_annotation" in sys.modules:
                del sys.modules["update_annotation"]

    @patch.dict(os.environ, {"API_KEY": "test-api-key", "ANNOTATION_ID": "test-annotation-123"})
    @patch("dify_oapi.client.Client")
    def test_delete_annotation_example(self, mock_client_class):
        """Test delete_annotation.py example execution."""
        # Mock the client and its methods
        mock_client = MagicMock()
        mock_client_class.builder.return_value.domain.return_value.build.return_value = mock_client

        # Mock successful response (204 No Content)
        mock_response = MagicMock()
        mock_response.success = True

        mock_client.chatflow.v1.annotation.delete.return_value = mock_response
        mock_client.chatflow.v1.annotation.adelete.return_value = mock_response

        # Import and test the example
        examples_dir = Path(__file__).parent.parent.parent.parent.parent / "examples" / "chatflow" / "annotation"
        sys.path.insert(0, str(examples_dir))

        try:
            import delete_annotation

            # Test individual functions
            delete_annotation.delete_annotation_sync()

            # Verify client was called
            assert mock_client.chatflow.v1.annotation.delete.called

        finally:
            sys.path.remove(str(examples_dir))
            if "delete_annotation" in sys.modules:
                del sys.modules["delete_annotation"]

    @patch.dict(os.environ, {"API_KEY": "test-api-key"})
    @patch("dify_oapi.client.Client")
    def test_annotation_reply_settings_example(self, mock_client_class):
        """Test annotation_reply_settings.py example execution."""
        # Mock the client and its methods
        mock_client = MagicMock()
        mock_client_class.builder.return_value.domain.return_value.build.return_value = mock_client

        # Mock successful response
        mock_response = MagicMock()
        mock_response.success = True
        mock_response.job_id = "job-123"
        mock_response.job_status = "waiting"

        mock_client.chatflow.v1.annotation.reply_settings.return_value = mock_response
        mock_client.chatflow.v1.annotation.areply_settings.return_value = mock_response

        # Import and test the example
        examples_dir = Path(__file__).parent.parent.parent.parent.parent / "examples" / "chatflow" / "annotation"
        sys.path.insert(0, str(examples_dir))

        try:
            import annotation_reply_settings

            # Test individual functions
            annotation_reply_settings.enable_annotation_reply_sync()
            annotation_reply_settings.disable_annotation_reply_sync()

            # Verify client was called
            assert mock_client.chatflow.v1.annotation.reply_settings.called

        finally:
            sys.path.remove(str(examples_dir))
            if "annotation_reply_settings" in sys.modules:
                del sys.modules["annotation_reply_settings"]

    @patch.dict(os.environ, {"API_KEY": "test-api-key", "JOB_ID": "test-job-123"})
    @patch("dify_oapi.client.Client")
    def test_annotation_reply_status_example(self, mock_client_class):
        """Test annotation_reply_status.py example execution."""
        # Mock the client and its methods
        mock_client = MagicMock()
        mock_client_class.builder.return_value.domain.return_value.build.return_value = mock_client

        # Mock successful response
        mock_response = MagicMock()
        mock_response.success = True
        mock_response.job_id = "job-123"
        mock_response.job_status = "completed"
        mock_response.error_msg = None

        mock_client.chatflow.v1.annotation.reply_status.return_value = mock_response
        mock_client.chatflow.v1.annotation.areply_status.return_value = mock_response

        # Import and test the example
        examples_dir = Path(__file__).parent.parent.parent.parent.parent / "examples" / "chatflow" / "annotation"
        sys.path.insert(0, str(examples_dir))

        try:
            import annotation_reply_status

            # Test individual functions (use correct function name)
            annotation_reply_status.get_annotation_reply_status_sync()

            # Verify client was called
            assert mock_client.chatflow.v1.annotation.reply_status.called

        finally:
            sys.path.remove(str(examples_dir))
            if "annotation_reply_status" in sys.modules:
                del sys.modules["annotation_reply_status"]

    def test_example_completeness(self, examples_dir):
        """Test that all annotation APIs are covered in examples."""
        expected_apis = {
            "get_annotations.py": ["list", "alist", "pagination", "has_more"],
            "create_annotation.py": ["create", "acreate", "question", "answer"],
            "update_annotation.py": ["update", "aupdate", "annotation_id"],
            "delete_annotation.py": ["delete", "adelete", "annotation_id"],
            "annotation_reply_settings.py": ["reply_settings", "areply_settings", "enable", "disable"],
            "annotation_reply_status.py": ["reply_status", "areply_status", "job_id", "job_status"],
        }

        for filename, keywords in expected_apis.items():
            file_path = examples_dir / filename
            assert file_path.exists(), f"Missing example file: {filename}"

            with open(file_path, encoding="utf-8") as f:
                content = f.read()

            for keyword in keywords:
                assert keyword in content, f"Missing keyword '{keyword}' in {filename}"

    def test_docstring_presence(self, example_files):
        """Test that all example functions have proper docstrings."""
        for file_path in example_files:
            with open(file_path, encoding="utf-8") as f:
                content = f.read()

            # Check for function docstrings
            tree = ast.parse(content)

            for node in ast.walk(tree):
                if isinstance(node, ast.FunctionDef):
                    # Check if function has docstring
                    if (
                        node.body
                        and isinstance(node.body[0], ast.Expr)
                        and isinstance(node.body[0].value, ast.Constant)
                    ):
                        docstring = node.body[0].value.value
                        assert isinstance(docstring, str), (
                            f"Missing docstring for function {node.name} in {file_path.name}"
                        )
                        assert len(docstring.strip()) > 0, (
                            f"Empty docstring for function {node.name} in {file_path.name}"
                        )

    def test_pagination_handling(self, example_files):
        """Test that list examples handle pagination properly."""
        for file_path in example_files:
            if "get_annotations" in file_path.name:
                with open(file_path, encoding="utf-8") as f:
                    content = f.read()

                # Check for pagination parameters
                assert ".page(" in content, f"Missing page parameter in {file_path.name}"
                assert ".limit(" in content, f"Missing limit parameter in {file_path.name}"
                assert "has_more" in content, f"Missing has_more check in {file_path.name}"

    def test_annotation_action_handling(self, example_files):
        """Test that reply settings examples handle actions properly."""
        for file_path in example_files:
            if "reply_settings" in file_path.name:
                with open(file_path, encoding="utf-8") as f:
                    content = f.read()

                # Check for action handling
                assert "enable" in content, f"Missing enable action in {file_path.name}"
                assert "disable" in content, f"Missing disable action in {file_path.name}"
                assert "score_threshold" in content, f"Missing score_threshold in {file_path.name}"

    def test_job_status_handling(self, example_files):
        """Test that reply status examples handle job status properly."""
        for file_path in example_files:
            if "reply_status" in file_path.name:
                with open(file_path, encoding="utf-8") as f:
                    content = f.read()

                # Check for job status handling
                assert "job_id" in content, f"Missing job_id in {file_path.name}"
                assert "job_status" in content, f"Missing job_status in {file_path.name}"
                assert "error_msg" in content, f"Missing error_msg handling in {file_path.name}"

    def test_annotation_resource_access(self, example_files):
        """Test that examples access the annotation resource correctly."""
        for file_path in example_files:
            with open(file_path, encoding="utf-8") as f:
                content = f.read()

            # Check for correct resource access path
            assert "client.chatflow.v1.annotation." in content, (
                f"Missing annotation resource access in {file_path.name}"
            )

    def test_request_model_imports(self, example_files):
        """Test that examples import the correct request models."""
        import_mapping = {
            "get_annotations.py": "GetAnnotationsRequest",
            "create_annotation.py": "CreateAnnotationRequest",
            "update_annotation.py": "UpdateAnnotationRequest",
            "delete_annotation.py": "DeleteAnnotationRequest",
            "annotation_reply_settings.py": "AnnotationReplySettingsRequest",
            "annotation_reply_status.py": "AnnotationReplyStatusRequest",
        }

        for file_path in example_files:
            with open(file_path, encoding="utf-8") as f:
                content = f.read()

            expected_import = import_mapping.get(file_path.name)
            if expected_import:
                assert expected_import in content, f"Missing {expected_import} import in {file_path.name}"

    def test_print_statements(self, example_files):
        """Test that examples include informative print statements."""
        for file_path in example_files:
            with open(file_path, encoding="utf-8") as f:
                content = f.read()

            # Check for print statements
            assert "print(" in content, f"Missing print statements in {file_path.name}"

            # Check for informative output
            assert "===" in content, f"Missing section headers in {file_path.name}"

    def test_error_response_handling(self, example_files):
        """Test that examples handle error responses properly."""
        for file_path in example_files:
            with open(file_path, encoding="utf-8") as f:
                content = f.read()

            # Check for error response handling
            assert "else:" in content, f"Missing else clause for error handling in {file_path.name}"
            assert "Error:" in content, f"Missing error message formatting in {file_path.name}"

    def test_annotation_field_access(self, example_files):
        """Test that examples properly access annotation fields."""
        for file_path in example_files:
            with open(file_path, encoding="utf-8") as f:
                content = f.read()

            # Check for annotation field access
            if (
                "get_annotations" in file_path.name
                or "create_annotation" in file_path.name
                or "update_annotation" in file_path.name
            ):
                assert "annotation.id" in content or "response.id" in content, (
                    f"Missing id field access in {file_path.name}"
                )
                assert "question" in content, f"Missing question field access in {file_path.name}"
                assert "answer" in content, f"Missing answer field access in {file_path.name}"


if __name__ == "__main__":
    pytest.main([__file__])
