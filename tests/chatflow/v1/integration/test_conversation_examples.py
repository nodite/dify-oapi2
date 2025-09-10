#!/usr/bin/env python3

import ast
import os
import sys
import unittest
from unittest.mock import MagicMock, patch

# Add the project root to the Python path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "../../../../.."))


class TestConversationExamples(unittest.TestCase):
    """Test conversation examples for syntax and structure validation."""

    def setUp(self):
        """Set up test environment."""
        self.examples_dir = os.path.join(os.path.dirname(__file__), "../../../../../examples/chatflow/conversation")
        self.example_files = [
            "get_conversation_messages.py",
            "get_conversations.py",
            "delete_conversation.py",
            "rename_conversation.py",
            "get_conversation_variables.py",
        ]

    def test_example_files_exist(self):
        """Test that all conversation example files exist."""
        for filename in self.example_files:
            file_path = os.path.join(self.examples_dir, filename)
            self.assertTrue(os.path.exists(file_path), f"Example file {filename} does not exist")

    def test_example_syntax_validation(self):
        """Test that all example files have valid Python syntax."""
        for filename in self.example_files:
            file_path = os.path.join(self.examples_dir, filename)

            with open(file_path, encoding="utf-8") as f:
                content = f.read()

            try:
                ast.parse(content)
            except SyntaxError as e:
                self.fail(f"Syntax error in {filename}: {e}")

    def test_required_imports(self):
        """Test that examples have required imports."""
        required_imports = ["asyncio", "os", "Client", "RequestOption"]

        for filename in self.example_files:
            file_path = os.path.join(self.examples_dir, filename)

            with open(file_path, encoding="utf-8") as f:
                content = f.read()

            for import_name in required_imports:
                self.assertIn(import_name, content, f"Required import '{import_name}' missing in {filename}")

    def test_environment_variable_validation(self):
        """Test that examples validate required environment variables."""
        for filename in self.example_files:
            file_path = os.path.join(self.examples_dir, filename)

            with open(file_path, encoding="utf-8") as f:
                content = f.read()

            # Check for API_KEY validation
            self.assertIn("API_KEY", content, f"API_KEY validation missing in {filename}")
            self.assertIn("ValueError", content, f"ValueError for missing env vars not found in {filename}")

    def test_safety_prefix_usage(self):
        """Test that examples use [Example] prefix for safety."""
        safety_files = ["delete_conversation.py", "rename_conversation.py"]

        for filename in safety_files:
            file_path = os.path.join(self.examples_dir, filename)

            with open(file_path, encoding="utf-8") as f:
                content = f.read()

            self.assertIn("[Example]", content, f"Safety prefix '[Example]' missing in {filename}")

    def test_error_handling_coverage(self):
        """Test that examples include proper error handling."""
        for filename in self.example_files:
            file_path = os.path.join(self.examples_dir, filename)

            with open(file_path, encoding="utf-8") as f:
                content = f.read()

            # Check for try-except blocks
            self.assertIn("try:", content, f"Error handling (try block) missing in {filename}")
            self.assertIn("except Exception", content, f"Exception handling missing in {filename}")

            # Check for response success validation
            self.assertIn("response.success", content, f"Response success check missing in {filename}")

    def test_sync_async_coverage(self):
        """Test that examples include both sync and async variants."""
        for filename in self.example_files:
            file_path = os.path.join(self.examples_dir, filename)

            with open(file_path, encoding="utf-8") as f:
                content = f.read()

            # Check for async functions
            self.assertIn("async def", content, f"Async function missing in {filename}")
            self.assertIn("await", content, f"Await keyword missing in {filename}")
            self.assertIn("asyncio.run", content, f"Asyncio.run missing in {filename}")

    def test_pagination_examples(self):
        """Test that list examples include pagination."""
        pagination_files = ["get_conversation_messages.py", "get_conversations.py", "get_conversation_variables.py"]

        for filename in pagination_files:
            file_path = os.path.join(self.examples_dir, filename)

            with open(file_path, encoding="utf-8") as f:
                content = f.read()

            self.assertIn("pagination", content.lower(), f"Pagination example missing in {filename}")
            self.assertIn("has_more", content, f"has_more check missing in {filename}")

    def test_conversation_specific_features(self):
        """Test conversation-specific features in examples."""
        # Test get_conversations.py for sorting
        conversations_file = os.path.join(self.examples_dir, "get_conversations.py")
        with open(conversations_file, encoding="utf-8") as f:
            content = f.read()

        self.assertIn("sort_by", content, "Sorting feature missing in get_conversations.py")

        # Test rename_conversation.py for auto-generate
        rename_file = os.path.join(self.examples_dir, "rename_conversation.py")
        with open(rename_file, encoding="utf-8") as f:
            content = f.read()

        self.assertIn("auto_generate", content, "Auto-generate feature missing in rename_conversation.py")

        # Test get_conversation_variables.py for filtering
        variables_file = os.path.join(self.examples_dir, "get_conversation_variables.py")
        with open(variables_file, encoding="utf-8") as f:
            content = f.read()

        self.assertIn("variable_name", content, "Variable name filter missing in get_conversation_variables.py")

    @patch("dify_oapi.client.Client")
    def test_get_conversation_messages_mock(self, mock_client_class):
        """Test get_conversation_messages example with mocked client."""
        # Mock the client and response
        mock_client = MagicMock()
        mock_client_class.builder.return_value.domain.return_value.build.return_value = mock_client

        mock_response = MagicMock()
        mock_response.success = True
        mock_response.data = []
        mock_response.has_more = False
        mock_response.limit = 20

        mock_client.chatflow.v1.conversation.messages.return_value = mock_response

        # Set environment variables
        with patch.dict(os.environ, {"API_KEY": "test-api-key", "CONVERSATION_ID": "test-conversation-id"}):
            # Import and run the function
            sys.path.insert(0, self.examples_dir)
            try:
                from get_conversation_messages import get_conversation_messages_sync

                get_conversation_messages_sync()

                # Verify client was called
                mock_client.chatflow.v1.conversation.messages.assert_called_once()
            finally:
                sys.path.remove(self.examples_dir)

    @patch("dify_oapi.client.Client")
    def test_delete_conversation_safety_check(self, mock_client_class):
        """Test delete_conversation safety check."""
        # Mock the client
        mock_client = MagicMock()
        mock_client_class.builder.return_value.domain.return_value.build.return_value = mock_client

        # Set environment variables with unsafe conversation ID
        with patch.dict(os.environ, {"API_KEY": "test-api-key", "CONVERSATION_ID": "unsafe-conversation-id"}):
            # Import and run the safety check function
            sys.path.insert(0, self.examples_dir)
            try:
                from delete_conversation import delete_conversation_with_confirmation

                # This should not call the delete method due to safety check
                with patch("builtins.print") as mock_print:
                    delete_conversation_with_confirmation()

                    # Verify safety message was printed
                    mock_print.assert_called()

                # Verify delete was not called
                mock_client.chatflow.v1.conversation.delete.assert_not_called()
            finally:
                sys.path.remove(self.examples_dir)

    def test_main_function_coverage(self):
        """Test that all examples have main function with proper coverage."""
        for filename in self.example_files:
            file_path = os.path.join(self.examples_dir, filename)

            with open(file_path, encoding="utf-8") as f:
                content = f.read()

            # Check for main function
            self.assertIn('if __name__ == "__main__":', content, f"Main function missing in {filename}")

            # Check for multiple examples in main
            main_section = content.split('if __name__ == "__main__":')[1]
            example_count = main_section.count("Example")
            self.assertGreaterEqual(example_count, 2, f"Insufficient examples in main function of {filename}")

    def test_request_builder_patterns(self):
        """Test that examples use proper request builder patterns."""
        for filename in self.example_files:
            file_path = os.path.join(self.examples_dir, filename)

            with open(file_path, encoding="utf-8") as f:
                content = f.read()

            # Check for builder pattern usage
            self.assertIn(".builder()", content, f"Builder pattern missing in {filename}")
            self.assertIn(".build()", content, f"Build method missing in {filename}")

    def test_client_initialization_pattern(self):
        """Test that examples use consistent client initialization."""
        for filename in self.example_files:
            file_path = os.path.join(self.examples_dir, filename)

            with open(file_path, encoding="utf-8") as f:
                content = f.read()

            # Check for consistent client initialization
            self.assertIn(
                'Client.builder().domain("https://api.dify.ai").build()',
                content,
                f"Consistent client initialization missing in {filename}",
            )
            self.assertIn(
                "RequestOption.builder().api_key(api_key).build()",
                content,
                f"Consistent request option initialization missing in {filename}",
            )


if __name__ == "__main__":
    unittest.main()
