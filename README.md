# Newsman

![NewsAPI](./NewsAPI.gif)

> A news and comments API built with FastAPI, SQLite and tested with Pytest.

## Motivation

FastAPI is an awesome new API framework that makes it both easy and convenient to build API especially Machine Learning. This is because of the cool feature that FastAPI supports like automatic swagger documentation, its speed which is at par with Go and Nodejs, data validation using Pydantic and many others. I am a big fan of FastAPI and I love using it to build API. 

The API was built by following best practices for Professional Python projects, using the following tools;

1. **Poetry** for quality code packaging and dependency management

2. **Black** for code formatting

3. **Flake8** for checking your code base against PEP8 coding style, programming errors and linting.

4. **Mypy** for type checking in the code base. This help prevent type errors and helps with editor autocompletion

5. **Isort** for sorting python imports.

6. **Pytest** for testing the code

## Model

The Article model has the following fields;

- id: primary_key, auto_generated
- title: str = Title of article
- body:str = body of the article
- publication_date: datetime = publication date of the article
- updated_at: datetime = last time article was updated at

The Comment Model has the following properties;

- id: primary_key, auto_generated
- content: string = The text content of the comment
- article_id: int = A relationship with the article

## Features

1. Article CRUD  functionality


2. Comment CRUD functionality

3. Database Migration support

4. Pydantic Data validations

5. Built with FastAPI

6. Docker support for containerization

7. Async Tests for the API using Pytest, Httpx

## How to run the API

first build the docker image by running the following command;

```bash
 sudo docker-compose build
```

and then run the following command to start the container

```bash
sudo docker-compose up -d
```

then visit http://localhost:8008/docs to access the api