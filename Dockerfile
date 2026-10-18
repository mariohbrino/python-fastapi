FROM python:3.13
ARG USERNAME=ubuntu
ARG USER_UID=1000
ARG USER_GID=1000

RUN groupadd -g ${USER_GID} ${USERNAME}
RUN useradd -u ${USER_UID} -g ${USER_GID} -m -s /bin/bash ${USERNAME}

WORKDIR /app
ENV PORT=8000
ENV PYTHONPATH=/app/src
ENV PYTHONUNBUFFERED="1"

COPY pyproject.toml .
COPY . .
RUN pip install --upgrade pip
RUN pip install . --no-cache-dir
CMD ["uvicorn", "src.server:app", "--host", "0.0.0.0", "--port", "${PORT}"]
