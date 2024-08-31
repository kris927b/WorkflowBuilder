# Use the official Python image.
# https://hub.docker.com/_/python
FROM python:3.12-slim

# Set environment variables for Poetry installation
ENV POETRY_VERSION=1.8.3 \
    POETRY_HOME="/opt/poetry" \
    POETRY_VIRTUALENVS_IN_PROJECT=true \
    PATH="$POETRY_HOME/bin:$PATH"

# Install Poetry
RUN curl -sSL https://install.python-poetry.org | python3 -

# Set the working directory in the container
WORKDIR /app

# Copy only the necessary files for installing dependencies
COPY pyproject.toml poetry.lock ./

# Install dependencies
RUN poetry install --no-root

# Copy the rest of the application code to the working directory
COPY . .

# Run the FastAPI application
CMD ["poetry", "run", "uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
