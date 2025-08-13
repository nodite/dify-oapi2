.PHONY: help install format lint check test clean build publish publish-test

help: ## Show this help message
	@echo "Available commands:"
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | sort | awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-20s\033[0m %s\n", $$1, $$2}'

install: ## Install dependencies
	poetry install --with dev,format

format: ## Format code with ruff
	poetry run ruff format .

lint: ## Lint code with ruff
	poetry run ruff check .

fix: ## Fix linting issues with ruff
	poetry run ruff check --fix .

check: ## Run all checks (lint + type check)
	poetry run ruff check .
	poetry run mypy .

test: ## Run tests
	poetry run pytest tests/ -v

test-cov: ## Run tests with coverage
	poetry run pytest tests/ -v --cov=dify_oapi --cov-report=html --cov-report=term

clean: ## Clean build artifacts
	rm -rf build/
	rm -rf dist/
	rm -rf *.egg-info/
	find . -type d -name __pycache__ -exec rm -rf {} +
	find . -type f -name "*.pyc" -delete
	find . -type d -name ".pytest_cache" -exec rm -rf {} +
	find . -type d -name ".mypy_cache" -exec rm -rf {} +
	find . -type d -name ".ruff_cache" -exec rm -rf {} +

build: ## Build package
	poetry build

publish: clean build ## Build and publish package to PyPI
	poetry publish

publish-test: clean build ## Build and publish package to TestPyPI
	poetry publish --repository testpypi

pre-commit: ## Run pre-commit hooks
	poetry run pre-commit run --all-files

install-hooks: ## Install pre-commit hooks
	poetry run pre-commit install

dev-setup: install install-hooks ## Setup development environment
	@echo "Development environment setup complete!"
	@echo "VS Code users: Install the recommended extensions for the best experience."
	@echo "Run 'make help' to see available commands."