#!/usr/bin/env python3
"""
Tests for Application Examples

This module tests application examples for syntax validation, import correctness,
environment variable handling, safety prefix usage, and error handling coverage.
"""

import ast
import os
import sys
from pathlib import Path
from unittest.mock import MagicMock, patch

import pytest


class TestApplicationExamples:
    """Test class for application examples."""

    @pytest.fixture
    def examples_dir(self):
        """Get the application examples directory."""
        return Path(__file__).parent.parent.parent.parent.parent / "examples" / "chatflow" / "application"

    @pytest.fixture
    def example_files(self, examples_dir):
        """Get all Python example files."""
        return list(examples_dir.glob("*.py"))

    def test_example_files_exist(self, examples_dir):
        """Test that all required example files exist."""
        required_files = ["get_info.py", "get_parameters.py", "get_meta.py", "get_site.py"]

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
    def test_get_info_example(self, mock_client_class):
        """Test get_info.py example execution."""
        # Mock the client and its methods
        mock_client = MagicMock()
        mock_client_class.builder.return_value.domain.return_value.build.return_value = mock_client

        # Mock successful response
        mock_response = MagicMock()
        mock_response.success = True
        mock_response.name = "[Example] Test Application"
        mock_response.description = "Test application description"
        mock_response.tags = ["test", "example"]

        mock_client.chatflow.v1.application.info.return_value = mock_response
        mock_client.chatflow.v1.application.ainfo.return_value = mock_response

        # Import and test the example
        examples_dir = Path(__file__).parent.parent.parent.parent.parent / "examples" / "chatflow" / "application"
        sys.path.insert(0, str(examples_dir))

        try:
            import get_info

            # Test individual functions
            get_info.get_info_sync()

            # Verify client was called
            assert mock_client.chatflow.v1.application.info.called

        finally:
            sys.path.remove(str(examples_dir))
            if "get_info" in sys.modules:
                del sys.modules["get_info"]

    @patch.dict(os.environ, {"API_KEY": "test-api-key"})
    @patch("dify_oapi.client.Client")
    def test_get_parameters_example(self, mock_client_class):
        """Test get_parameters.py example execution."""
        # Mock the client and its methods
        mock_client = MagicMock()
        mock_client_class.builder.return_value.domain.return_value.build.return_value = mock_client

        # Mock successful response with complex parameters
        mock_response = MagicMock()
        mock_response.success = True
        mock_response.opening_statement = "Welcome to the application"
        mock_response.suggested_questions = ["What can you do?", "How does this work?"]
        mock_response.suggested_questions_after_answer = MagicMock()
        mock_response.suggested_questions_after_answer.enabled = True
        mock_response.speech_to_text = MagicMock()
        mock_response.speech_to_text.enabled = False
        mock_response.text_to_speech = MagicMock()
        mock_response.text_to_speech.enabled = True
        mock_response.text_to_speech.voice = "alloy"
        mock_response.text_to_speech.language = "en"
        mock_response.text_to_speech.autoPlay = "enabled"

        mock_client.chatflow.v1.application.parameters.return_value = mock_response
        mock_client.chatflow.v1.application.aparameters.return_value = mock_response

        # Import and test the example
        examples_dir = Path(__file__).parent.parent.parent.parent.parent / "examples" / "chatflow" / "application"
        sys.path.insert(0, str(examples_dir))

        try:
            import get_parameters

            # Test individual functions
            get_parameters.get_parameters_sync()

            # Verify client was called
            assert mock_client.chatflow.v1.application.parameters.called

        finally:
            sys.path.remove(str(examples_dir))
            if "get_parameters" in sys.modules:
                del sys.modules["get_parameters"]

    @patch.dict(os.environ, {"API_KEY": "test-api-key"})
    @patch("dify_oapi.client.Client")
    def test_get_meta_example(self, mock_client_class):
        """Test get_meta.py example execution."""
        # Mock the client and its methods
        mock_client = MagicMock()
        mock_client_class.builder.return_value.domain.return_value.build.return_value = mock_client

        # Mock successful response
        mock_response = MagicMock()
        mock_response.success = True
        mock_response.tool_icons = {
            "search": "https://example.com/search-icon.png",
            "calculator": {"background": "#FF5733", "content": "🧮"},
        }

        mock_client.chatflow.v1.application.meta.return_value = mock_response
        mock_client.chatflow.v1.application.ameta.return_value = mock_response

        # Import and test the example
        examples_dir = Path(__file__).parent.parent.parent.parent.parent / "examples" / "chatflow" / "application"
        sys.path.insert(0, str(examples_dir))

        try:
            import get_meta

            # Test individual functions
            get_meta.get_meta_sync()

            # Verify client was called
            assert mock_client.chatflow.v1.application.meta.called

        finally:
            sys.path.remove(str(examples_dir))
            if "get_meta" in sys.modules:
                del sys.modules["get_meta"]

    @patch.dict(os.environ, {"API_KEY": "test-api-key"})
    @patch("dify_oapi.client.Client")
    def test_get_site_example(self, mock_client_class):
        """Test get_site.py example execution."""
        # Mock the client and its methods
        mock_client = MagicMock()
        mock_client_class.builder.return_value.domain.return_value.build.return_value = mock_client

        # Mock successful response
        mock_response = MagicMock()
        mock_response.success = True
        mock_response.title = "[Example] Test WebApp"
        mock_response.chat_color_theme = "blue"
        mock_response.chat_color_theme_inverted = False
        mock_response.icon_type = "emoji"
        mock_response.icon = "🤖"
        mock_response.icon_background = "#FFFFFF"
        mock_response.icon_url = None
        mock_response.description = "Example WebApp description"
        mock_response.copyright = "© 2024 Example Corp"
        mock_response.privacy_policy = "https://example.com/privacy"
        mock_response.custom_disclaimer = "This is an example application"
        mock_response.default_language = "en-US"
        mock_response.show_workflow_steps = True
        mock_response.use_icon_as_answer_icon = False

        mock_client.chatflow.v1.application.site.return_value = mock_response
        mock_client.chatflow.v1.application.asite.return_value = mock_response

        # Import and test the example
        examples_dir = Path(__file__).parent.parent.parent.parent.parent / "examples" / "chatflow" / "application"
        sys.path.insert(0, str(examples_dir))

        try:
            import get_site

            # Test individual functions
            get_site.get_site_sync()

            # Verify client was called
            assert mock_client.chatflow.v1.application.site.called

        finally:
            sys.path.remove(str(examples_dir))
            if "get_site" in sys.modules:
                del sys.modules["get_site"]

    def test_example_completeness(self, examples_dir):
        """Test that all application APIs are covered in examples."""
        expected_apis = {
            "get_info.py": ["info", "name", "description", "tags"],
            "get_parameters.py": ["parameters", "opening_statement", "suggested_questions", "text_to_speech"],
            "get_meta.py": ["meta", "tool_icons"],
            "get_site.py": ["site", "title", "chat_color_theme", "icon_type", "default_language"],
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

    def test_response_field_access(self, example_files):
        """Test that examples properly access response fields."""
        for file_path in example_files:
            with open(file_path, encoding="utf-8") as f:
                content = f.read()

            # Check for proper response field access
            assert "response." in content, f"Missing response field access in {file_path.name}"

            # Check for specific field access patterns based on file
            if "get_info" in file_path.name:
                assert "response.name" in content, f"Missing name field access in {file_path.name}"
                assert "response.description" in content, f"Missing description field access in {file_path.name}"
                assert "response.tags" in content, f"Missing tags field access in {file_path.name}"
            elif "get_parameters" in file_path.name:
                assert "opening_statement" in content, f"Missing opening_statement access in {file_path.name}"
                assert "suggested_questions" in content, f"Missing suggested_questions access in {file_path.name}"
            elif "get_meta" in file_path.name:
                assert "tool_icons" in content, f"Missing tool_icons access in {file_path.name}"
            elif "get_site" in file_path.name:
                assert "response.title" in content, f"Missing title field access in {file_path.name}"
                assert "chat_color_theme" in content, f"Missing chat_color_theme access in {file_path.name}"

    def test_client_method_calls(self, example_files):
        """Test that examples call the correct client methods."""
        method_mapping = {
            "get_info.py": ["info", "ainfo"],
            "get_parameters.py": ["parameters", "aparameters"],
            "get_meta.py": ["meta", "ameta"],
            "get_site.py": ["site", "asite"],
        }

        for file_path in example_files:
            with open(file_path, encoding="utf-8") as f:
                content = f.read()

            expected_methods = method_mapping.get(file_path.name, [])
            for method in expected_methods:
                assert f".{method}(" in content, f"Missing {method} method call in {file_path.name}"

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

    def test_application_resource_access(self, example_files):
        """Test that examples access the application resource correctly."""
        for file_path in example_files:
            with open(file_path, encoding="utf-8") as f:
                content = f.read()

            # Check for correct resource access path
            assert "client.chatflow.v1.application." in content, (
                f"Missing application resource access in {file_path.name}"
            )

    def test_request_model_imports(self, example_files):
        """Test that examples import the correct request models."""
        import_mapping = {
            "get_info.py": "GetInfoRequest",
            "get_parameters.py": "GetParametersRequest",
            "get_meta.py": "GetMetaRequest",
            "get_site.py": "GetSiteRequest",
        }

        for file_path in example_files:
            with open(file_path, encoding="utf-8") as f:
                content = f.read()

            expected_import = import_mapping.get(file_path.name)
            if expected_import:
                assert expected_import in content, f"Missing {expected_import} import in {file_path.name}"


if __name__ == "__main__":
    pytest.main([__file__])
