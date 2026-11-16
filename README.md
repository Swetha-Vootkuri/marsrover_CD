# Marsrover CD

This project is a small Python starter application that includes a Hello World walking skeleton and a Windows CI/CD workflow for packaging and deployment.

## Installing a release (no repo access needed)

Requires Python 3.8+. Download the `.whl` file from the
[Releases page](https://github.com/Swetha-Vootkuri/marsrover_CD/releases), or install it directly from the release URL:

```bash
python -m pip install https://github.com/Swetha-Vootkuri/marsrover_CD/releases/download/v0.1.0/marsrover_cd-0.1.0-py3-none-any.whl
marsrover-cd
```

On Windows, use `py -m pip install ...` if `python` is not on your PATH.

## Publishing a release

From an up-to-date, clean `main`:

```bash
python scripts/release.py 0.2.0
```

The script checks the version is valid `MAJOR.MINOR.PATCH` and greater than both the current `pyproject.toml` version and
the latest release tag, then runs the tests, asks for confirmation, bumps the version, commits, tags `v0.2.0` and pushes.
If the push fails, the local commit and tag are rolled back. Use `--yes` to skip the prompt.

The workflow tests, builds, verifies the wheel installs and runs on Windows and macOS, then creates a GitHub Release
with the wheel attached. It fails if the tag does not match the `pyproject.toml` version.

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
