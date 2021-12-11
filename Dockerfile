# Builds a considerably smaller image
FROM python:3.9-slim


# set env variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
ENV PORT 8008
ENV PATH="$PATH:$HOME/.poetry/bin"

# set working directory
WORKDIR /app


# install poetry
RUN pip3 install poetry

# install dependencies
COPY pyproject.toml poetry.lock ./
RUN poetry install --no-root --no-dev

# copy project
COPY . .
RUN poetry install --no-dev

EXPOSE 8008


# command to run on container start 
CMD ["poetry run", "uvicorn", "app.main:api", "--host", "0.0.0.0", "--port", "8008"]