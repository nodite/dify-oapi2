#!/usr/bin/env python3
"""
Tests for Examples README

This module tests the Examples README for completeness, accuracy,
and consistency with the actual example files and API specifications.
"""

import ast
import os
import re
from pathlib import Path

import pytest


class TestExamplesReadme:
    """Test class for Examples README validation."""

    @pytest.fixture
    def readme_path(self):
        """Get the Examples README path."""
        return Path(__file__).parent.parent.parent.parent.parent / "examples" / "chatflow" / "README.md"

    @pytest.fixture
    def examples_dir(self):
        """Get the chatflow examples directory."""
        return Path(__file__).parent.parent.parent.parent.parent / "examples" / "chatflow"

    @pytest.fixture
    def readme_content(self, readme_path):
        """Get the README content."""
        with open(readme_path, encoding="utf-8") as f:
            return f.read()

    def test_readme_exists(self, readme_path):
        """Test that the README file exists."""
        assert readme_path.exists(), "Examples README.md file does not exist"

    def test_readme_not_empty(self, readme_content):
        """Test that the README is not empty."""
        assert readme_content.strip(), "Examples README.md is empty"

    def test_api_count_accuracy(self, readme_content):
        """Test that the README accurately reflects the API count."""
        # Check total API count
        assert "**17 APIs**" in readme_content or "17 endpoints" in readme_content, "Total API count not mentioned"
        assert "**6 resource" in readme_content or "6 resources" in readme_content, "Resource count not mentioned"

        # Check individual resource counts
        assert "Chatflow (3 APIs)" in readme_content, "Chatflow API count incorrect"
        assert "File (1 API)" in readme_content, "File API count incorrect"
        assert "Feedback (2 APIs)" in readme_content, "Feedback API count incorrect"
        assert "Conversation (5 APIs)" in readme_content, "Conversation API count incorrect"
        assert "TTS (2 APIs)" in readme_content, "TTS API count incorrect"
        assert "Application (4 APIs)" in readme_content, "Application API count incorrect"
        assert "Annotation (6 APIs)" in readme_content, "Annotation API count incorrect"

    def test_directory_structure_accuracy(self, readme_content, examples_dir):
        """Test that the directory structure in README matches actual structure."""
        # Check main directories exist
        expected_dirs = ["chatflow", "file", "feedback", "conversation", "tts", "application", "annotation"]

        for dir_name in expected_dirs:
            dir_path = examples_dir / dir_name
            assert dir_path.exists(), f"Directory {dir_name} does not exist"
            assert f"├── {dir_name}/" in readme_content or f"{dir_name}/" in readme_content, (
                f"Directory {dir_name} not documented in README"
            )

    def test_example_files_documented(self, readme_content, examples_dir):
        """Test that all example files are documented in the README."""
        # Get all Python files in examples directory
        python_files = []
        for root, _dirs, files in os.walk(examples_dir):
            for file in files:
                if file.endswith(".py") and file != "__init__.py":
                    rel_path = Path(root).relative_to(examples_dir) / file
                    python_files.append(str(rel_path))

        # Check that each file is mentioned in README
        for file_path in python_files:
            file_name = Path(file_path).name
            # Check if file is mentioned in README (either as filename or in directory structure)
            assert file_name in readme_content or file_path in readme_content, (
                f"Example file {file_path} not documented in README"
            )

    def test_api_operations_documented(self, readme_content):
        """Test that all API operations are documented."""
        # Chatflow operations
        chatflow_ops = ["Send Chat Message", "Stop Chat Message", "Get Suggested Questions"]
        for op in chatflow_ops:
            assert op in readme_content, f"Chatflow operation '{op}' not documented"

        # File operations
        assert "Upload File" in readme_content, "File upload operation not documented"

        # Feedback operations
        feedback_ops = ["Message Feedback", "Get App Feedbacks"]
        for op in feedback_ops:
            assert op in readme_content, f"Feedback operation '{op}' not documented"

        # Conversation operations
        conversation_ops = [
            "Get Conversation Messages",
            "Get Conversations",
            "Delete Conversation",
            "Rename Conversation",
            "Get Conversation Variables",
        ]
        for op in conversation_ops:
            assert op in readme_content, f"Conversation operation '{op}' not documented"

        # TTS operations
        tts_ops = ["Audio to Text", "Text to Audio"]
        for op in tts_ops:
            assert op in readme_content, f"TTS operation '{op}' not documented"

        # Application operations
        app_ops = ["Get Info", "Get Parameters", "Get Meta", "Get Site"]
        for op in app_ops:
            assert op in readme_content, f"Application operation '{op}' not documented"

        # Annotation operations
        annotation_ops = [
            "Get Annotations",
            "Create Annotation",
            "Update Annotation",
            "Delete Annotation",
            "Annotation Reply Settings",
            "Annotation Reply Status",
        ]
        for op in annotation_ops:
            assert op in readme_content, f"Annotation operation '{op}' not documented"

    def test_environment_setup_documented(self, readme_content):
        """Test that environment setup is properly documented."""
        assert "API_KEY" in readme_content, "API_KEY environment variable not documented"
        assert "export API_KEY" in readme_content, "Environment variable setup not documented"
        assert "Prerequisites" in readme_content, "Prerequisites section missing"
        assert "Python 3.10+" in readme_content, "Python version requirement not documented"

    def test_installation_documented(self, readme_content):
        """Test that installation instructions are documented."""
        assert "pip install dify-oapi2" in readme_content, "Installation instructions missing"
        assert "dify-oapi2" in readme_content, "Package name not mentioned"

    def test_usage_patterns_documented(self, readme_content):
        """Test that common usage patterns are documented."""
        # Check for sync/async patterns
        assert "sync" in readme_content.lower() or "synchronous" in readme_content.lower(), (
            "Synchronous usage not documented"
        )
        assert "async" in readme_content.lower() or "asynchronous" in readme_content.lower(), (
            "Asynchronous usage not documented"
        )

        # Check for streaming patterns
        assert "streaming" in readme_content.lower(), "Streaming usage not documented"
        assert "blocking" in readme_content.lower(), "Blocking mode not documented"

        # Check for error handling patterns
        assert "error handling" in readme_content.lower() or "Error Handling" in readme_content, (
            "Error handling not documented"
        )
        assert "response.success" in readme_content, "Response success checking not documented"

    def test_safety_guidelines_documented(self, readme_content):
        """Test that safety guidelines are documented."""
        assert "[Example]" in readme_content, "Safety prefix not documented"
        assert "Safety" in readme_content or "safety" in readme_content, "Safety guidelines section missing"
        assert "prefix" in readme_content.lower(), "Safety prefix usage not explained"

    def test_code_examples_syntax(self, readme_content):
        """Test that code examples in README have valid Python syntax."""
        # Extract Python code blocks from README
        code_blocks = re.findall(r"```python\n(.*?)\n```", readme_content, re.DOTALL)

        for i, code_block in enumerate(code_blocks):
            try:
                # Try to parse the code block
                ast.parse(code_block)
            except SyntaxError as e:
                pytest.fail(f"Syntax error in code block {i + 1}: {e}")

    def test_import_statements_accuracy(self, readme_content):
        """Test that import statements in README are accurate."""
        # Check for correct import patterns
        expected_imports = [
            "from dify_oapi.client import Client",
            "from dify_oapi.core.model.request_option import RequestOption",
            "from dify_oapi.api.chatflow.v1.model",
        ]

        for import_stmt in expected_imports:
            assert import_stmt in readme_content, f"Import statement '{import_stmt}' not found or incorrect"

    def test_file_type_documentation(self, readme_content):
        """Test that supported file types are documented."""
        # Check document types
        doc_types = ["TXT", "PDF", "HTML", "XLSX", "DOCX", "CSV"]
        for doc_type in doc_types:
            assert doc_type in readme_content, f"Document type {doc_type} not documented"

        # Check image types
        image_types = ["JPG", "PNG", "GIF", "WEBP", "SVG"]
        for image_type in image_types:
            assert image_type in readme_content, f"Image type {image_type} not documented"

        # Check audio types
        audio_types = ["MP3", "WAV", "M4A"]
        for audio_type in audio_types:
            assert audio_type in readme_content, f"Audio type {audio_type} not documented"

    def test_troubleshooting_section(self, readme_content):
        """Test that troubleshooting section is comprehensive."""
        assert "Troubleshooting" in readme_content, "Troubleshooting section missing"
        assert "Common Issues" in readme_content, "Common Issues subsection missing"

        # Check for common error scenarios
        common_errors = ["Missing API Key", "File Upload Errors", "Unsupported File Type", "Conversation Not Found"]
        for error in common_errors:
            assert error in readme_content, f"Common error '{error}' not documented"

    def test_usage_scenarios_documented(self, readme_content):
        """Test that usage scenarios are documented."""
        assert "Usage Scenarios" in readme_content, "Usage Scenarios section missing"

        # Check for key scenarios
        scenarios = ["Basic Chat Application", "Multimodal Chat", "Conversation Management", "Voice Integration"]
        for scenario in scenarios:
            assert scenario in readme_content, f"Usage scenario '{scenario}' not documented"

    def test_resource_links_accuracy(self, readme_content):
        """Test that resource links are accurate."""
        # Check for relative links to other documentation
        assert "README.md" in readme_content, "Links to other README files missing"
        assert "docs/" in readme_content or "documentation" in readme_content.lower(), "Documentation links missing"

    def test_api_endpoint_patterns(self, readme_content):
        """Test that API endpoint patterns are documented."""
        # Check for HTTP methods
        http_methods = ["POST", "GET", "DELETE", "PUT"]
        for method in http_methods:
            assert method in readme_content, f"HTTP method {method} not documented"

        # Check for endpoint patterns
        assert "/v1/" in readme_content, "API version not documented"
        assert "chat-messages" in readme_content, "Chat messages endpoint not documented"
        assert "conversations" in readme_content, "Conversations endpoint not documented"

    def test_streaming_documentation(self, readme_content):
        """Test that streaming functionality is properly documented."""
        assert "streaming" in readme_content.lower(), "Streaming not documented"
        assert "chunk" in readme_content.lower(), "Streaming chunks not documented"
        assert "real-time" in readme_content.lower() or "real time" in readme_content.lower(), (
            "Real-time aspect not documented"
        )

    def test_pagination_documentation(self, readme_content):
        """Test that pagination is documented."""
        assert "pagination" in readme_content.lower(), "Pagination not documented"
        assert "page" in readme_content.lower(), "Page parameter not documented"
        assert "limit" in readme_content.lower(), "Limit parameter not documented"

    def test_builder_pattern_documentation(self, readme_content):
        """Test that builder patterns are documented."""
        assert ".builder()" in readme_content, "Builder pattern not documented"
        assert ".build()" in readme_content, "Build method not documented"

    def test_async_await_patterns(self, readme_content):
        """Test that async/await patterns are documented."""
        assert "await " in readme_content, "Await keyword not documented"
        assert "async def" in readme_content, "Async function definition not documented"
        assert "asyncio.run" in readme_content, "Asyncio.run usage not documented"

    def test_file_upload_workflow(self, readme_content):
        """Test that file upload workflow is documented."""
        assert "upload" in readme_content.lower(), "File upload not documented"
        assert "multipart" in readme_content.lower(), "Multipart form-data not documented"
        assert "BytesIO" in readme_content, "BytesIO usage not documented"

    def test_error_code_documentation(self, readme_content):
        """Test that error codes are documented."""
        error_codes = ["400", "404", "413", "415", "500"]
        for code in error_codes:
            assert code in readme_content, f"Error code {code} not documented"

    def test_contributing_guidelines(self, readme_content):
        """Test that contributing guidelines are present."""
        assert "Contributing" in readme_content, "Contributing section missing"
        assert "naming conventions" in readme_content.lower() or "Naming Conventions" in readme_content, (
            "Naming conventions not documented"
        )

    def test_license_information(self, readme_content):
        """Test that license information is present."""
        assert "License" in readme_content, "License section missing"
        assert "MIT" in readme_content, "MIT license not mentioned"

    def test_example_count_consistency(self, readme_content, examples_dir):
        """Test that the documented example count matches actual files."""
        # Count actual Python files (excluding __init__.py)
        actual_count = 0
        for _root, _dirs, files in os.walk(examples_dir):
            for file in files:
                if file.endswith(".py") and file != "__init__.py":
                    actual_count += 1

        # The README should mention the total number of examples
        assert f"{actual_count} example" in readme_content or f"**{actual_count}**" in readme_content, (
            f"Example count {actual_count} not accurately documented"
        )

    def test_resource_method_patterns(self, readme_content):
        """Test that resource method patterns are documented."""
        # Check for resource access patterns
        assert "client.chatflow.v1." in readme_content, "Chatflow resource access pattern not documented"

        # Check for method names
        method_patterns = [".send(", ".upload(", ".info(", ".list(", ".delete(", ".create("]
        for pattern in method_patterns:
            assert pattern in readme_content, f"Method pattern '{pattern}' not documented"

    def test_configuration_patterns(self, readme_content):
        """Test that configuration patterns are documented."""
        assert "RequestOption" in readme_content, "RequestOption not documented"
        assert ".api_key(" in readme_content, "API key configuration not documented"
        assert "Client.builder()" in readme_content, "Client builder pattern not documented"
        assert ".domain(" in readme_content, "Domain configuration not documented"
