# SQLite

---

The ```SQLite``` repository contains SQLite learning usage.


## Folder Structure Conventions

---

Although this layout is pretty straightforward, it has several drawbacks that arise as the app complexity increases.
For example, it will be hard for you to reuse the application logic in other projects because all the functionality is
bundled in ```webapp/__init__.py```.
If you split this functionality into modules instead, then you could reuse complete modules across different projects.

```
/
├── core                            # The core package
├── models                          # a models package
├── README.md                       # Instructions and helpful links
├── requirements.txt                # a list of package dependencies
├── robots.txt                      # tells which URLs the search engine crawlers can access on your site
└── /                               # 
```

## Python Projects Structures

| Folder           | Description                                   |
|:-----------------|:----------------------------------------------|
| /apidoc          | the doc-generated API docs                    |
| /code            | the project files                             |
| /doc             | the documentation                             |
| /lib             | the C-language libraries                      |
| /scripts or /bin | the that kind of command-line interface stuff |
| /tests           | the tests of the project                      |


# Building Application

---

## Local Development

### Check ```Python``` settings

```shell
python3 --version
python3 -m pip --version
python3 -m ensurepip --default-pip
```

### Setup a virtual environment

```
python3 -m pip install virtualenv
python3 -m venv venv
source deactivate
source venv/bin/activate
```

## Activate ```venv```

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
(venv) <UserName>@<HostName> SQLite %
```

The parenthesized ```(venv)``` in front of the prompt indicates that you’ve successfully activated the virtual
environment.

## Deactivate Virtual Env

```shell
deactivate
```

Output:

```
<UserName>@<HostName> SQLite %
```

## Upgrade ```pip``` release

```shell
pip install --upgrade pip
```

## Install Packages/Requirements (Dependencies)

- Install at the system level

```shell
brew install python-requests
```

- Install in specific Virtual Env

```shell
pip install requests
pip install beautifulsoup4
python -m pip install requests
```

## Install Requirements

```shell
pip install -r requirements.txt
```

## Save Requirements (Dependencies)

```shell
pip freeze > requirements.txt
```

## Build Python Project
```shell
python -m build
```

## Configuration Setup

Set a local configuration file.
Create or update local ```.env``` configuration file.

```shell
pip install python-dotenv
cp default.env .env
```

Now, update the default local configurations as follows:

```text
# App Configs
APP_HOST = 0.0.0.0
HOST = 0.0.0.0
APP_PORT = 8080
PORT = 8080
APP_ENV = develop
DEBUG = False
#
# Pool Configs
#
DEFAULT_POOL_SIZE = 1
RDS_POOL_SIZE = 1
#
# Logger Configs
#
LOG_FILE_NAME = 'SQLite.log'
#
# Database Configs
#
DB_HOSTNAME = 127.0.0.1
DB_PORT =
DB_NAME = SQLite
DB_USERNAME = SQLite
DB_PASSWORD = Password
```


**By default**, Flask will run the application on **port 5000**.

## Run Flask Application

```shell
python -m flask --app webapp run --port 8080 --debug
```


**By default**, Flask runs the application on **port 5000**.

```shell
python wsgi.py

OR

#flask --app wsgi run
python -m flask --app wsgi run
# http://127.0.0.1:5000/SQLite

OR

python -m flask --app wsgi run --port 8080 --debug
# http://127.0.0.1:8080/SQLite

OR

# Production Mode

# equivalent to 'from app import app'
gunicorn wsgi:app
# gunicorn -w <n> 'wsgi:app'
gunicorn -w 2 'wsgi:app'
# http://127.0.0.1:8000/SQLite

gunicorn -c gunicorn.conf.py wsgi:app
# http://127.0.0.1:8080/SQLite

```


**Note**:- You can stop the development server by pressing ```Ctrl+C``` in your terminal.

## Access Application

```shell
- [IWS on port 8080](http://127.0.0.1:8080/SQLite)
- [IWS on port 8000](http://127.0.0.1:8000/SQLite)
- [IWS on port 5000](http://127.0.0.1:5000/SQLite)
```

## Testing

### Unit Tests

```shell
python -m unittest
python -m unittest discover -s ./pytheorem/tests -p "test_*.py"
```

### Performance Testing

```shell
# Run this in a separate terminal
# so that the load generation continues and you can carry on with the rest of the steps
kubectl run -i --tty load-generator --rm --image=busybox:1.28 --restart=Never -- /bin/sh -c "while sleep 0.01; do wget -q -O- http://php-apache; done"
```


# Reference

- SQLite

# Author

---

- Rohtash Lakra
