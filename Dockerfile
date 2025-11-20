FROM python:3.12-slim
WORKDIR /app

# Copy project metadata first for cacheable installs
COPY pyproject.toml uv.lock* ./

# Create venv, install uv into the venv, then sync deps into that venv
RUN python -m venv /app/.venv \
 && /app/.venv/bin/python -m pip install --upgrade pip uv \
 && /app/.venv/bin/uv sync --frozen || /app/.venv/bin/uv sync

# Copy the rest of the app
COPY . .

EXPOSE 8000

# Run uv from the venv so the environment is correct
CMD ["/app/.venv/bin/uv", "run", "fastapi", "dev", "app/main.py", "--host", "0.0.0.0", "--port", "8000"]
