# Newsman

> A news and comments API built with FastAPI, SQLite and tested with Pytest.


The API was built by following best practices for Professional Python projects, using the following tools;

1. Poetry for quality code packaging and dependency management

2. Black for code formatting

3. Flake8 for checking your code base against PEP8 coding style, programming errors and linting.

4. Mypy for type checking in the code base. This help prevent type errors and helps with editor autocompletion

5. Isort for sorting python imports.

6. Pytest for testing the code

## Model

The Article model has the following fields;

- id: primary_key, auto_generated
- title: str = Title of article
- body:str = body of the article
- publication_date: datetime = publication date of the article
- updated_at: datetime = 