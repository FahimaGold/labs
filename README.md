# About this app -Update-

This is a simple fastapi app that displays current time in Moscow. When you hit the `/`, the current time will be redirected to a file. If you want to see the time on the browser, hit the endpoint `/visit`. In order to use it, fter you clone it from github, follow the following steps:

- Run `pip3 install fastapi` in order to install fastapi
- Run `pip3 install pytz` in order to install the package that helps us get timezone.
- Run `pip3 install "uvicorn[standard]"` in order to install the server where you'll run the app.

# Running the app

From your parent directory of the `app_python`, run the following command to launch the app: `uvicorn app_python.current_time:app --reload` . The app will be then accessible through your browser at http://127.0.0.1:8000/ (output redirected to the file `out.txt`).

If you want to see the time on the browser, you can access it via http://127.0.0.1:8000/visit

# Testing the app

Unit test is implemented for this app. It is under the `tests/` folder. In order to run it, from your parent directory, run:
`python3 -m pytest app_python/tests`

# Docker

This app can also be run in a docker container. In order to run it locally, run the following command: 
`docker run -d --name container_name -p 80:80 image_name`.

In order to run it from a web service such as [labs play with docker](https://docs.docker.com/get-started/04_sharing_app/), use the image from docker hub `fahima2019/lab2:lab2`, you can then run it by : `docker run -d -p 80:80 --name container fahima2019/lab2:lab2`.

# Github actions

Github Actions are used as CI/CD pipelines. the yaml file is located under `.github/workflows`. The `CI` workflow will install python dependencies, check python source file using `black` linter, test python files using `pytest`, and finally builds and pushes a docker image to the docker hub repository. Github caching is used in order to optimize uncessary installation of dependencies.