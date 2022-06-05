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

# Best practices of Unit Tests

- Unit tests should be fast: It means that unit tests should run fast, as if they take too long to run, developers may not run them. In order to ensure that unit tests run fast, developers should make them as simple as possible, don't make them depend on other tests, and mock external dependencies.
- Unit tests should be simple: This can be achieved by having low cyclomatic complexity (a metric that indicates the number of possible execution paths), the low it is, the easier it is to understand and maintain the code.
- Unit tests should be readable: As they are part of the documentation. Also, if unit tests are unreadable, it makes it hard for developers to understand them and hence the risk of introducing bugs.
- Unit tests should be deterministic: This means that the test behavior should remain the same as long as the code does not change. In other words, if the test passes once, it should always passes if the code does not change, no matter how many times the unit tests are run.
- Unit tests should be isolated: That means that external dependencies should be mocked.
- Unit tests should have a naming convention: Unit tests should have  convention naming where the test class should be named after the test under test, and test class name should follow CamelCase convention.
- Unit tests should cover many tests cases: Including edge cases (not common inputs but they may cause problems).
- Using tools to check coverage: In order to check how effective are the test cases.

