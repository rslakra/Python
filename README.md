# PyServices

A collection of sample Python projects (web apps, tools and packaging examples) that help in learning the Python language.

## 🚀 Quick Start

Each sub-project is self-contained. Pick one (here `FlaskWebApp`), then create a virtual environment, install its
requirements, configure it, and run it:

```bash
cd FlaskWebApp

python3 -m venv venv
source venv/bin/activate          # Windows: venv\Scripts\activate
python3 -m pip install --upgrade pip
python3 -m pip install -r requirements.txt

cp default.env .env               # edit the values — see ⚙️ Build & Configuration
python -m flask --app webapp run --port 8081 --debug
```

For full prerequisites and configuration details, see **📋 Prerequisites & Dependencies** and
**⚙️ Build & Configuration** below.

### Usage

Most web-app sub-projects also ship a `Makefile` and helper scripts:

```bash
make setup               # create the virtual env
make install-packages    # install the requirements
make run                 # run the application
make test                # run the tests
make lint                # run flake8
./runUnitTests.sh        # run the unit tests
./runPylint.sh           # run pylint
./runGunicorn.sh         # run under gunicorn
```

Run `make help` inside a sub-project to list the targets it supports.

### Output

By default, Flask runs the application on **port 5000**. With the settings below, the app is served on port `8081`:

```text
http://localhost:8081/ecommerce-iws
```

**Note**:- You can stop the development server by pressing ```Ctrl+C``` in your terminal.

## ✨ Features

- **Web apps** — Flask and FastAPI servers with templates, static assets, config, routes and tests
- **Logging and log parsing** — web apps with a custom logger and log-parsing capabilities
- **Tools and scripts** — generators, data sync, database and web-crawler examples
- **Packaging** — a worked example of packaging a project for PyPI
- **Containers and CI** — `Dockerfile`, `compose.yaml`, gunicorn config and per-project GitHub Actions workflows

## 📋 Prerequisites & Dependencies

- Python 3 (the `Generator` project documents Python 3.9) and `pip`
- `virtualenv` / `venv` for isolated environments
- `make` (optional — most projects ship a `Makefile`)
- Docker (optional — for the projects that have a `Dockerfile` / `compose.yaml`)

| Source | Purpose |
| ------ | ------- |
| `requirements.txt` | Runtime and dev packages of each sub-project — installed in **⚙️ Build & Configuration** below |
| `default.env` | Default local configuration — copy it to `.env` |
| Sub-projects | See **📚 References → In this repository** for each project's README |

## ⚙️ Build & Configuration

### Build

#### Create Virtual Env

```shell
python3 -m pip install virtualenv
python3 -m venv venv
```

#### Activate ```venv```

```source``` is Linux/macOS command and doesn't work in Windows.

- Windows
```shell
venv\Scripts\activate
```

- Mac OS/Linux
```shell
source venv/bin/activate

OR

. ./venv/bin/activate
```

Output:
```
(venv) rslakra@YVXKPJV2CN Python %
```

The parenthesized ```(venv)``` in front of the prompt indicates that you’ve successfully activated the virtual environment.

#### Deactivate Virtual Env

```shell
deactivate
```

Output:
```
rslakra@YVXKPJV2CN %
```

#### Upgrade ```pip``` release

```shell
pip install --upgrade pip
```

#### Install Packages

- Install at system level
```shell
brew install python-requests
```

- Install in specific Virtual Env
```shell
pip install requests
pip install beautifulsoup4
python3 -m pip install requests
```

#### Install Requirements

```shell
python3 -m pip install --upgrade pip
python3 -m pip install -r requirements.txt
```

#### Save Requirements (Dependencies)

```shell
pip freeze > requirements.txt
```

### Environment variables

Set the local configuration file.

```shell
pip install python-dotenv
cp default.env .env
```

Now, update the default local configurations as follows:

```text
APP_HOST = 0.0.0.0
APP_PORT = 8081
```

| Variable | Required | Description | Default / example |
| -------- | -------- | ----------- | ----------------- |
| `APP_HOST` | No | Host the app binds to | `0.0.0.0` |
| `APP_PORT` | No | Port the app listens on (Flask defaults to `5000`) | `8081` |

**Note**:- Some sub-projects name these keys `HOST` and `PORT` in their `default.env`. Check the file of the project you run.

### Run Flask Application

```shell
python -m flask --app webapp run --port 8081 --debug
```

## 📁 Project Layout

```
Python/
├── Authentication/
│    └── jwt-authentication/        # JWT authentication project
├── Database/                       # Database project
├── DataSync/                       # Data sync project (LoadRunner, QueueWriter)
├── FastAPIWebApp/                  # FastAPI web server with logging capabilities
├── fastapi-webapp/                 # FastAPI + Jinja2 web app (app/ and webapp/ packages)
├── fastapi-webapp-poc/             # FastAPI + Jinja2 proof of concept (single main.py)
├── FlaskWebApp/                    # Flask web server with logging capabilities
├── Generator/                      # .xlsx to JSON payload generator
├── LogParserWebApp/                # Log-parser web server
├── LogWebApp/                      # Logging web server
├── Notebooks/                      # Jupyter notebooks (Beginner.ipynb)
├── PythonPackaging/                # Packaging Python projects (PyPI)
├── WebCrawler/                     # Web crawler
├── .github/workflows/              # One CI workflow per project
├── .gitignore                      # The .gitignore file
├── README.md                       ← you are here
└── robots.txt                      # tells which URLs the search engine crawlers can access on your site
```

### Python project structures

| Folder | Description |
|:---|:---|
|/apidoc|the doc-generated API docs|
|/code|the project files|
|/doc|the documentation|
|/lib|the C-language libraries|
|/scripts or /bin|the that kind of command-line interface stuff|
|/tests|the tests of the project|

## 🏗️ Architecture

### Capacity planning

#### CPU bound systems

- Formula
```text
RPS = TotalCore * (1/TaskDurationInSeconds)

i.e.:
4 * (1000/100) = 40
```

| Total Cores  | Task Duration | RPS |
|:------------:|:--------------|:----|
|      4       | 100ms         | 40  |
|      4       | 50ms          | 80  |
|      4       | 10ms          | 400 |

## 🧪 Testing

Run the tests from inside a sub-project:

```bash
python3 -m unittest      # or: ./runUnitTests.sh, make test
python3 -m pytest
```

## 🛠️ Troubleshooting

| Issue | Fix |
| ----- | --- |
| `source: command not found` on Windows | Use `venv\Scripts\activate` instead — `source` is a Linux/macOS command |
| Port already in use | Change `APP_PORT` in `.env` (Flask defaults to `5000`) or stop the conflicting process |
| `ModuleNotFoundError` | Activate the virtual env and run `python3 -m pip install -r requirements.txt` |

## 📚 References

### In this repository

| Module | Link | Description |
| ------ | ---- | ----------- |
| `Authentication/jwt-authentication` | [Authentication/jwt-authentication/README.md](Authentication/jwt-authentication/README.md) | JWT authentication project |
| `Database` | [Database/README.md](Database/README.md) | Database project |
| `DataSync` | [DataSync/README.md](DataSync/README.md) | Data sync project |
| `fastapi-webapp` | [fastapi-webapp/README.md](fastapi-webapp/README.md) | FastAPI web app with Jinja2 pages, static assets and a JSON API |
| `fastapi-webapp-poc` | [fastapi-webapp-poc/README.md](fastapi-webapp-poc/README.md) | FastAPI web app proof of concept |
| `FastAPIWebApp` | [FastAPIWebApp/README.md](FastAPIWebApp/README.md) | FastAPI web server with logging capabilities |
| `FlaskWebApp` | [FlaskWebApp/README.md](FlaskWebApp/README.md) | Flask web server with logging capabilities |
| `Generator` | [Generator/README.md](Generator/README.md) | Reads an .xlsx file and writes a JSON payload |
| `LogParserWebApp` | [LogParserWebApp/README.md](LogParserWebApp/README.md) | Web server with log-parsing capabilities |
| `LogWebApp` | [LogWebApp/README.md](LogWebApp/README.md) | Web server with logging capabilities |
| `PythonPackaging` | [PythonPackaging/README.md](PythonPackaging/README.md) | Packaging Python projects and uploading them to PyPI |
| `WebCrawler` | [WebCrawler/README.md](WebCrawler/README.md) | Simple web crawler built on `urllib` and `html.parser` |

### External Documentation

| Link | Description |
| ---- | ----------- |
| [Star Wars API](https://swapi.dev/) | Public API for practice |
| [developer testing tool](https://httpbin.org/) | HTTP request and response testing |
| [Inspect webhooks and HTTP requests](https://pipedream.com/requestbin) | Inspect webhooks and HTTP requests |
| [Gunicorn Architecture](https://docs.gunicorn.org/en/latest/design.html) | Gunicorn design |
| [How many concurrent requests does a single Flask process receive?](https://stackoverflow.com/questions/10938360/how-many-concurrent-requests-does-a-single-flask-process-receive?rq=4) | Flask concurrency |
| [Learn FastAPI](https://fastapi.tiangolo.com/learn/) | FastAPI tutorials |
| [Array](https://docs.python.org/3/library/array.html) | Python `array` module |
| [Beautiful Soup Documentation](https://beautiful-soup-4.readthedocs.io/en/latest/#quick-start) | HTML parsing |
| [Weather-App](https://github.com/israel-dryer/Weather-App/tree/master) | Sample weather app |
| [Web-Scraping-Projects](https://github.com/israel-dryer/Web-Scraping-Projects?tab=readme-ov-file) | Sample web-scraping projects |
| [Python Projects – Beginner to Advanced](https://www.geeksforgeeks.org/python-projects-beginner-to-advanced/) | Project ideas |
| [The HitchHiker's Guide to Python](https://docs.python-guide.org/writing/structure/) | Python project structure |

## 📄 License

`PythonPackaging` carries its own `LICENSE` file. The other projects have none of their own.

## 👤 Author

- **Rohtash Lakra** — [@rslakra](https://github.com/rslakra)
