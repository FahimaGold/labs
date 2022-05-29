# About this app

This is a simple fastapi app that displays current time in Moscow. In order to use it, fter you clone it from github, follow the following steps:

- Run `pip3 install fastapi` in order to install fastapi
- Run `pip3 install pytz` in order to install the package that helps us get timezone.
- Run `pip3 install "uvicorn[standard]"` in order to install the server where you'll run the app.

# Running the app

From your parent directory of the `app_python`, run the following command to launch the app: `uvicorn app_python.current_time:app --reload` . The app will be then accessible through your browser at http://127.0.0.1:8000/.

# Testing the app

Unit test is implemented for this app. It is under the `tests/` folder. In order to run it, from your parent directory, run:
`python3 -m unittest app_python/tests/current_time_test.py`