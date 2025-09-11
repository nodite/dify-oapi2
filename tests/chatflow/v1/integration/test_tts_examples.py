#!/usr/bin/env python3

import ast
from pathlib import Path

import pytest


class TestTTSExamples:
    """Test TTS examples for syntax and structure validation."""

    @pytest.fixture
    def examples_dir(self):
        """Get the TTS examples directory."""
        return Path(__file__).parent.parent.parent.parent.parent / "examples" / "chatflow" / "tts"

    def test_audio_to_text_example_exists(self, examples_dir):
        """Test that audio_to_text.py example exists."""
        example_file = examples_dir / "audio_to_text.py"
        assert example_file.exists(), "audio_to_text.py example should exist"

    def test_text_to_audio_example_exists(self, examples_dir):
        """Test that text_to_audio.py example exists."""
        example_file = examples_dir / "text_to_audio.py"
        assert example_file.exists(), "text_to_audio.py example should exist"

    def test_audio_to_text_syntax_valid(self, examples_dir):
        """Test that audio_to_text.py has valid Python syntax."""
        example_file = examples_dir / "audio_to_text.py"
        with open(example_file) as f:
            content = f.read()

        # Parse the file to check syntax
        try:
            ast.parse(content)
        except SyntaxError as e:
            pytest.fail(f"Syntax error in audio_to_text.py: {e}")

    def test_text_to_audio_syntax_valid(self, examples_dir):
        """Test that text_to_audio.py has valid Python syntax."""
        example_file = examples_dir / "text_to_audio.py"
        with open(example_file) as f:
            content = f.read()

        # Parse the file to check syntax
        try:
            ast.parse(content)
        except SyntaxError as e:
            pytest.fail(f"Syntax error in text_to_audio.py: {e}")

    def test_audio_to_text_imports(self, examples_dir):
        """Test that audio_to_text.py has correct imports."""
        example_file = examples_dir / "audio_to_text.py"
        with open(example_file) as f:
            content = f.read()

        # Check for required imports
        required_imports = [
            "from dify_oapi.api.chatflow.v1.model.audio_to_text_request import AudioToTextRequest",
            "from dify_oapi.client import Client",
            "from dify_oapi.core.model.request_option import RequestOption",
            "import asyncio",
            "import os",
            "from io import BytesIO",
        ]

        for import_stmt in required_imports:
            assert import_stmt in content, f"Missing import: {import_stmt}"

    def test_text_to_audio_imports(self, examples_dir):
        """Test that text_to_audio.py has correct imports."""
        example_file = examples_dir / "text_to_audio.py"
        with open(example_file) as f:
            content = f.read()

        # Check for required imports
        required_imports = [
            "from dify_oapi.api.chatflow.v1.model.text_to_audio_request import TextToAudioRequest",
            "from dify_oapi.api.chatflow.v1.model.text_to_audio_request_body import TextToAudioRequestBody",
            "from dify_oapi.client import Client",
            "from dify_oapi.core.model.request_option import RequestOption",
            "import asyncio",
            "import os",
        ]

        for import_stmt in required_imports:
            assert import_stmt in content, f"Missing import: {import_stmt}"

    def test_audio_to_text_environment_validation(self, examples_dir):
        """Test that audio_to_text.py validates environment variables."""
        example_file = examples_dir / "audio_to_text.py"
        with open(example_file) as f:
            content = f.read()

        # Check for environment variable validation
        assert 'os.getenv("API_KEY")' in content, "Should validate API_KEY environment variable"
        assert 'raise ValueError("API_KEY environment variable is required")' in content, (
            "Should raise error for missing API_KEY"
        )

    def test_text_to_audio_environment_validation(self, examples_dir):
        """Test that text_to_audio.py validates environment variables."""
        example_file = examples_dir / "text_to_audio.py"
        with open(example_file) as f:
            content = f.read()

        # Check for environment variable validation
        assert 'os.getenv("API_KEY")' in content, "Should validate API_KEY environment variable"
        assert 'raise ValueError("API_KEY environment variable is required")' in content, (
            "Should raise error for missing API_KEY"
        )

    def test_audio_to_text_functions(self, examples_dir):
        """Test that audio_to_text.py has required functions."""
        example_file = examples_dir / "audio_to_text.py"
        with open(example_file) as f:
            content = f.read()

        # Check for required functions
        required_functions = [
            "def audio_to_text_sync():",
            "async def audio_to_text_async():",
            "def audio_to_text_with_different_formats():",
        ]

        for func in required_functions:
            assert func in content, f"Missing function: {func}"

    def test_text_to_audio_functions(self, examples_dir):
        """Test that text_to_audio.py has required functions."""
        example_file = examples_dir / "text_to_audio.py"
        with open(example_file) as f:
            content = f.read()

        # Check for required functions
        required_functions = [
            "def text_to_audio_sync():",
            "async def text_to_audio_async():",
            "def text_to_audio_with_message_id():",
            "def text_to_audio_streaming():",
        ]

        for func in required_functions:
            assert func in content, f"Missing function: {func}"

    def test_audio_to_text_error_handling(self, examples_dir):
        """Test that audio_to_text.py has proper error handling."""
        example_file = examples_dir / "audio_to_text.py"
        with open(example_file) as f:
            content = f.read()

        # Check for error handling patterns
        assert "try:" in content, "Should have try-except blocks"
        assert "except Exception as e:" in content, "Should catch exceptions"
        assert "if response.success:" in content, "Should check response success"
        assert "else:" in content, "Should handle error responses"

    def test_text_to_audio_error_handling(self, examples_dir):
        """Test that text_to_audio.py has proper error handling."""
        example_file = examples_dir / "text_to_audio.py"
        with open(example_file) as f:
            content = f.read()

        # Check for error handling patterns
        assert "try:" in content, "Should have try-except blocks"
        assert "except Exception as e:" in content, "Should catch exceptions"
        assert "if response.success:" in content, "Should check response success"
        assert "else:" in content, "Should handle error responses"

    def test_audio_to_text_client_usage(self, examples_dir):
        """Test that audio_to_text.py uses client correctly."""
        example_file = examples_dir / "audio_to_text.py"
        with open(example_file) as f:
            content = f.read()

        # Check for correct client usage
        assert "Client.builder().domain(" in content, "Should use Client builder"
        assert "client.chatflow.v1.tts.speech_to_text(" in content, "Should call speech_to_text method"
        assert "client.chatflow.v1.tts.aspeech_to_text(" in content, "Should call async speech_to_text method"

    def test_text_to_audio_client_usage(self, examples_dir):
        """Test that text_to_audio.py uses client correctly."""
        example_file = examples_dir / "text_to_audio.py"
        with open(example_file) as f:
            content = f.read()

        # Check for correct client usage
        assert "Client.builder().domain(" in content, "Should use Client builder"
        assert "client.chatflow.v1.tts.text_to_audio(" in content, "Should call text_to_audio method"
        assert "client.chatflow.v1.tts.atext_to_audio(" in content, "Should call async text_to_audio method"

    def test_audio_to_text_file_handling(self, examples_dir):
        """Test that audio_to_text.py handles files correctly."""
        example_file = examples_dir / "audio_to_text.py"
        with open(example_file) as f:
            content = f.read()

        # Check for file handling
        assert "BytesIO(" in content, "Should use BytesIO for file handling"
        assert ".file(" in content, "Should set file in request"
        assert "audio_file" in content, "Should create audio file object"

    def test_text_to_audio_request_body(self, examples_dir):
        """Test that text_to_audio.py uses request body correctly."""
        example_file = examples_dir / "text_to_audio.py"
        with open(example_file) as f:
            content = f.read()

        # Check for request body usage
        assert "TextToAudioRequestBody.builder()" in content, "Should use request body builder"
        assert ".text(" in content, "Should set text in request body"
        assert ".user(" in content, "Should set user in request body"
        assert ".streaming(" in content, "Should set streaming in request body"
        assert ".message_id(" in content, "Should set message_id in request body"

    def test_audio_to_text_main_execution(self, examples_dir):
        """Test that audio_to_text.py has main execution block."""
        example_file = examples_dir / "audio_to_text.py"
        with open(example_file) as f:
            content = f.read()

        # Check for main execution
        assert 'if __name__ == "__main__":' in content, "Should have main execution block"
        assert "audio_to_text_sync()" in content, "Should call sync function"
        assert "asyncio.run(audio_to_text_async())" in content, "Should call async function"

    def test_text_to_audio_main_execution(self, examples_dir):
        """Test that text_to_audio.py has main execution block."""
        example_file = examples_dir / "text_to_audio.py"
        with open(example_file) as f:
            content = f.read()

        # Check for main execution
        assert 'if __name__ == "__main__":' in content, "Should have main execution block"
        assert "text_to_audio_sync()" in content, "Should call sync function"
        assert "asyncio.run(text_to_audio_async())" in content, "Should call async function"

    def test_audio_formats_coverage(self, examples_dir):
        """Test that audio_to_text.py covers different audio formats."""
        example_file = examples_dir / "audio_to_text.py"
        with open(example_file) as f:
            content = f.read()

        # Check for different audio formats
        formats = ["mp3", "wav", "m4a", "webm"]
        for fmt in formats:
            assert fmt in content, f"Should include {fmt} format example"

    def test_streaming_support(self, examples_dir):
        """Test that text_to_audio.py includes streaming support."""
        example_file = examples_dir / "text_to_audio.py"
        with open(example_file) as f:
            content = f.read()

        # Check for streaming support
        assert ".streaming(True)" in content, "Should include streaming enabled example"
        assert ".streaming(False)" in content, "Should include streaming disabled example"

    def test_message_id_support(self, examples_dir):
        """Test that text_to_audio.py includes message ID support."""
        example_file = examples_dir / "text_to_audio.py"
        with open(example_file) as f:
            content = f.read()

        # Check for message ID support
        assert 'os.getenv("MESSAGE_ID")' in content, "Should check for MESSAGE_ID environment variable"
        assert ".message_id(" in content, "Should set message_id in request"

    def test_examples_completeness(self, examples_dir):
        """Test that all required TTS examples are present."""
        expected_files = ["audio_to_text.py", "text_to_audio.py"]

        for filename in expected_files:
            example_file = examples_dir / filename
            assert example_file.exists(), f"Missing TTS example: {filename}"

    def test_examples_executable(self, examples_dir):
        """Test that example files are executable."""
        example_files = ["audio_to_text.py", "text_to_audio.py"]

        for filename in example_files:
            example_file = examples_dir / filename
            # Check if file has shebang
            with open(example_file) as f:
                first_line = f.readline().strip()
            assert first_line.startswith("#!/usr/bin/env python3"), f"{filename} should have Python shebang"
