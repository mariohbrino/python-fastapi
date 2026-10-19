# FastAPI REST API Project

## Initial set up

Install UV package manager using the following command:

```bash
pip install uv
```

Using UV to install the dependencies and create a virtual environment for the FastAPI project.

```bash
uv sync
source .venv/bin/activate
```

> [!IMPORTANT]
> When working with Apple Silicon (ARM64), it requires to install python 3.13 using homebrew,
> then use flag --python /opt/homebrew/bin/python3.13 due to architecture-specific
> dependencies.

## Development

To start the development server, run the following command:

```bash
fastapi dev
```

Linting check and format for python using Ruff.

```bash
ruff check .
ruff format .
```

Type checking for python using Ty.

```bash
ty check .
```
