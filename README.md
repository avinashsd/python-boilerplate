Pre requisites:
    - UV - for Python package and environment management.
        Install uv(https://github.com/astral-sh/uv)
    - Docker
Steps:
    - Create new boilerplate directory
        mkdir python-boilerplate && cd python-boilerplate
    - Create separate backend and frontend folders
        mkdir backend frontend
    - Create gitignore and dockerignore files files in each folders above and add ignore patterns
    - Go inside backend and initialize uv project:
        cd backend && uv init --name Python-Boilerplate-with-UV-and-Docker
    Create and activate venv using uv
        uv venv & source .venv/bin/activate
    Remove unwanted files:
        rm hello.py README.md .python-version
    Install ruff, pytest, pre-commit as dev dependency
        uv add --dev ruff pytest pre-commit mypy coverage
    Install flask(change framework)
        uv add flask
    Create app inside backend/app and make necessary changes for run command in Dockerfile

Development Commands:
    - Run Ruff checks
        uv run ruff check
        uv run ruff format
    - Run pytest
        uv run pytest
    - Run type checking
        uv run mypy <APP_NAME>
