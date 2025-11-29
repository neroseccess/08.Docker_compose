# ---- build stage ----
FROM python:3.12-slim AS builder

WORKDIR /w
ENV VENV_PATH=/opt/venv

# Tools for building wheels (psycopg2 etc.)
RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential gcc libpq-dev \
 && rm -rf /var/lib/apt/lists/*

COPY app/requirements.txt ./requirements.txt

# Create venv and prebuild dependencies into it (fast + clean runtime)
RUN python -m venv ${VENV_PATH} \
 && ${VENV_PATH}/bin/pip install --no-cache-dir --upgrade pip \
 && ${VENV_PATH}/bin/pip install --no-cache-dir -r requirements.txt

# ---- runtime stage ----
FROM python:3.12-slim AS runtime

WORKDIR /app
ENV VENV_PATH=/opt/venv
ENV PATH="${VENV_PATH}/bin:${PATH}"
ENV PYTHONUNBUFFERED=1

# copy only ready venv + app code (no build tools in runtime)
COPY --from=builder ${VENV_PATH} ${VENV_PATH}
COPY app/app.py ./app.py

EXPOSE 5000
CMD ["python", "app.py"]
