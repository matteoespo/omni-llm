# Contributing to Omni-LLM

Thank you for your interest in contributing to **Omni-LLM**! We welcome contributions of all kinds, including new adapters, bug fixes, documentation improvements, and feature requests.

## How to Contribute

### 1. Find or Open an Issue
Before writing code, please check the existing issues or open a new one to discuss the changes you would like to make.

### 2. Set Up Your Development Environment
Ensure you have Python 3.12+ and [uv](https://github.com/astral-sh/uv) installed.

1. Fork and clone the repository.
2. Create a virtual environment:
   ```bash
   uv venv
   ```
3. Activate the virtual environment:
   - On Linux/macOS:
     ```bash
     source .venv/bin/activate
     ```
   - On Windows:
     ```cmd
     .venv\Scripts\activate
     ```
4. Install the package in editable mode:
   ```bash
   uv pip install -e .
   ```

### 3. Add a New LLM Adapter (Example)
To add support for a new backend adapter (e.g., `vllm`, `llamafile`, or `koboldcpp`):
1. Create a new file under `omnillm/adapters/` (e.g., `vllm_adapter.py`) implementing the `LLMBackend` interface.
2. Register the adapter inside the `LocalLLMManager` constructor in `omnillm/core/manager.py`.
3. Add unit tests for your adapter under the `tests/` directory.

### 4. Running Tests
Before submitting a pull request, verify that all tests pass:
```bash
uv run pytest
```

### 5. Submit a Pull Request
1. Commit your changes to a new feature branch.
2. Push the branch to your fork.
3. Open a Pull Request against the `main` branch with a clear description of the implementation.

---

## Guidelines
- Keep code simple, clean, and self-documenting.
- Maintain test coverage for new backends or features.
- Preserve existing docstrings and comments.
