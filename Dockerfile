# syntax=docker/dockerfile:1

ARG PYTHON_VERSION=3.13.5
FROM python:${PYTHON_VERSION}-slim AS base
WORKDIR /app

# Install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy project
COPY . .

# Copy entrypoint ke root
COPY deploy/entrypoint.sh /entrypoint.sh
RUN chmod +x /entrypoint.sh

# Buat folder static
RUN mkdir -p /app/staticfiles

# Jalankan sebagai user non-root (opsional)
RUN useradd -m appuser
RUN chown -R appuser:appuser /app/staticfiles
USER appuser

CMD ["/entrypoint.sh"]
