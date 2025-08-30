# Development Guide

This guide covers the development setup and workflow for the dify-oapi project.

## Prerequisites

- Python 3.10+
- Poetry
- VS Code (recommended)

## Development Setup

### 1. Clone and Setup

```bash
git clone https://github.com/nodite/dify-oapi2.git
cd dify-oapi
make dev-setup
```

This will:
- Install all dependencies (including dev and format groups)
- Install pre-commit hooks
- Set up the development environment

### Manual Pre-commit Setup

If pre-commit hooks are not working, install them manually:

```bash
# Install pre-commit hooks
make install-hooks
```

### 2. VS Code Setup

If you're using VS Code, install the recommended extensions:

1. Open the project in VS Code
2. When prompted, install the recommended extensions
3. The workspace is pre-configured for automatic formatting on save

#### Recommended Extensions

- **Ruff** (`charliermarsh.ruff`) - Primary linter and formatter
- **Python** (`ms-python.python`) - Python language support
- **Pylance** (`ms-python.vscode-pylance`) - Python language server

## Code Formatting and Linting

This project uses **Ruff** for both linting and formatting, configured to be compatible with Black's formatting style.

### Automatic Formatting

- **VS Code**: Files are automatically formatted on save
- **Pre-commit**: Code is automatically formatted before each commit

### Manual Commands

```bash
# Format all code
make format

# Check for linting issues
make lint

# Fix auto-fixable linting issues
make fix

# Run all checks (lint + type check)
make check
```

### Configuration

Ruff configuration is in `pyproject.toml`:

```toml
[tool.ruff]
line-length = 120
target-version = "py310"

[tool.ruff.lint]
select = ["E", "F", "I", "N", "UP", "B", "A", "RUF"]
ignore = ["B904", "N805", "N806"]

[tool.ruff.format]
quote-style = "double"
indent-style = "space"
skip-magic-trailing-comma = false
```

## Testing

### Running Tests

```bash
# Run all tests
make test

# Run tests with coverage
make test-cov

# Run specific test file
poetry run pytest tests/knowledge/v1/model/test_dataset_models.py -v

# Run tests matching a pattern
poetry run pytest tests/ -k "test_create" -v
```

### Test Structure

```
tests/
├── knowledge/
│   └── v1/
│       ├── model/          # Model tests
│       ├── resource/       # Resource tests
│       └── integration/    # Integration tests
├── test_chat.py
├── test_completion.py
└── ...
```

## Type Checking

This project uses MyPy for static type checking:

```bash
# Run type checking
poetry run mypy .

# Type checking is also included in 'make check'
make check
```

## Pre-commit Hooks

Pre-commit hooks are automatically installed during setup and will run:

- Ruff formatting
- Ruff linting with auto-fix
- Pylint checks

To run pre-commit manually:

```bash
make pre-commit
```

## Development Workflow

### 1. Before Starting Work

```bash
# Pull latest changes
git pull origin main

# Install/update dependencies
make install
```

### 2. During Development

- Code is automatically formatted on save in VS Code
- Run tests frequently: `make test`
- Check for issues: `make check`

### 3. Before Committing

Pre-commit hooks will automatically run, but you can also run manually:

```bash
# Format and check code
make format
make check

# Run tests
make test

# Run pre-commit hooks
make pre-commit
```

### 4. Commit and Push

```bash
git add .
git commit -m "Your commit message"
git push origin your-branch
```

## Publishing Configuration

### PyPI Token Setup

Before publishing packages, configure Poetry with your PyPI tokens:

```bash
# Configure TestPyPI token
poetry config http-basic.testpypi __token__ <your-testpypi-token>

# Configure PyPI token
poetry config http-basic.pypi __token__ <your-pypi-token>
```

## Available Make Commands

Run `make help` to see all available commands:

```bash
make help
```

Common commands:
- `make dev-setup` - Setup development environment
- `make install` - Install dependencies
- `make format` - Format code with ruff
- `make lint` - Lint code with ruff
- `make fix` - Fix linting issues with ruff
- `make check` - Run all checks (lint + type check)
- `make test` - Run tests
- `make test-cov` - Run tests with coverage
- `make clean` - Clean build artifacts
- `make build` - Build package
- `make publish` - Build and publish package to PyPI
- `make publish-test` - Build and publish package to TestPyPI
- `make pre-commit` - Run pre-commit hooks
- `make install-hooks` - Install pre-commit hooks

## VS Code Configuration

The project includes VS Code configuration in `.vscode/`:

- `settings.json` - Workspace settings with Ruff integration
- `extensions.json` - Recommended extensions
- `tasks.json` - Quick tasks for formatting, linting, and testing

### Key VS Code Features

- **Format on Save**: Automatically formats Python files using Ruff
- **Auto Import Organization**: Organizes imports on save
- **Auto Fix**: Fixes linting issues on save
- **Integrated Terminal**: Pre-configured for Poetry environment

## Troubleshooting

### Ruff Not Working in VS Code

1. Ensure the Ruff extension is installed
2. Check that the Python interpreter is set to the Poetry virtual environment
3. Reload VS Code window: `Ctrl+Shift+P` → "Developer: Reload Window"

### Pre-commit Hooks Failing

```bash
# Update pre-commit hooks
poetry run pre-commit autoupdate

# Run hooks manually to debug
poetry run pre-commit run --all-files
```

### Import Errors

```bash
# Reinstall dependencies
make install

# Check Python path in VS Code
# Ctrl+Shift+P → "Python: Select Interpreter"
```

## Contributing

1. Fork the repository
2. Create a feature branch
3. Follow the development workflow above
4. Ensure all tests pass and code is properly formatted
5. Submit a pull request

## Code Style Guidelines

- Line length: 120 characters
- Use double quotes for strings
- Follow PEP 8 naming conventions
- Add type hints to all functions and methods
- Write docstrings for public APIs
- Keep functions focused and small
- Use meaningful variable names

The Ruff configuration enforces most of these automatically.
