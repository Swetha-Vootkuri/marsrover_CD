# Marsrover CD

This project is a small Python starter application that includes a Hello World walking skeleton and a Windows CI/CD workflow for packaging and deployment.

## Quick start

```bash
python3 -m venv .venv
source .venv/bin/activate
python -m pip install --upgrade pip
python -m pip install -r requirements.txt
python -m unittest discover -s tests -q
python -m build
```

## Features

- Simple Hello World module
- Unit tests
- Python packaging via `pyproject.toml`
- GitHub Actions workflow for Windows packaging and deployment
