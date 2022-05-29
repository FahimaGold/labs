# Framework to be used in this project

*FastAPI* ([official docs here](https://fastapi.tiangolo.com/features/)) will be used in this project for the following reasons:
- Production ready
- High performance
- It meets the requirements for this project
- Well documented
- Easy integration with databases and frontends

# Best practices

The best practices recommended to structure a **Fastapi** project are:

- Under the project name (in this example, it is `app_python`), a subdirectory named `core` is created.
- The `core` subdirectory contains another sub-directory `models`, and another one `schemas` which contain database code, and schemas respectively.
- Another subdirectory `tests` under the project name, which contains the application tests.
- Another folder `v1` under the project directory, which contains the API endpoints and `v1` indicates version 1 of the API.

The best practices recommended to structure a **Python** project are:

- Use virtual envorinement for each project in order to avoid library clashes.
- Define a coding guidelines and sticking to it for the entire project.
- Use python 3 as python 2 is officially not supported starting from Jnauray 1st 2020.
- Use **List comprehensions** as they replace ugly for loops in order to fill a list.

## What **not** to do in python

- Avoid importing all from packages as it pollutes the namespace
- Avoid turning off error reporting during development
- Avoid implementing best practices from other practices languages