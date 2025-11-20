FROM python:3.12-slim
WORKDIR /app

# Copy project metadata first for cacheable installs
COPY pyproject.toml uv.lock* ./

# Create venv, install project (and uv/uvicorn) into it
RUN python -m venv /app/.venv \
 && /app/.venv/bin/python -m pip install --upgrade pip build \
 && /app/.venv/bin/pip install . || ( /app/.venv/bin/pip install uvicorn[standard] && true )

# Copy the rest of the app
COPY . .

EXPOSE 8000

# Run uvicorn from the venv (adjust target if your project exposes a different CLI)
CMD ["/app/.venv/bin/uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]