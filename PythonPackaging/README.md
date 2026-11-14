# PythonPackaging

The ```PythonPackaging``` repository is created to learn ```Packaging Python Projects```.
This tutorial walks you through how to package a ```PythonPackaging``` Python project. 
It will show you how to add the necessary files and structure to create the package, how to build the package, and 
how to upload it to the ```Python Package Index (PyPI)```.


## Folder Structure Conventions

---

This layout is pretty straightforward and allows you to handle application complexity in various modules.

```
PythonPackaging/
├── scripts                         # scripts folder
│    ├── runUnitTests.sh            # Runs the unit tests
│    └── /
├── src                             # It's a placeholder for python files.
│    ├── rslakra                    # A unique package name that doesn’t conflict with packages uploaded by other people
│    │    ├── __init__.py           # The existence of an __init__.py file allows users to import the directory as a regular package.
│    │    ├── pair.py
│    │    ├── utils.py
│    │    └── /
│    └── /
├── tests                           # It's a placeholder for test files.
│    ├── __init__.py                # The package initializer
│    ├── base.py
│    ├── test_pair.py
│    ├── test_time_utils.py
│    └── /
├── LICENSE
├── README.md                       # Instructions and helpful links
├── pyproject.toml                  # Tells build frontend tools like pip and build which backend to use for your project.
├── requirements.txt                # a list of package dependencies
├── robots.txt                      # tells which URLs the search engine crawlers can access on your site
└── /                               # 
```


## Configuration & Building ```PyPI``` Package

---


- Clone the repository
```shell
# Clone the repository
git clone https://github.com/rslakra/PythonPackaging.git
cd PythonPackaging
```

- List all make file commands
```shell
make
```

- Check ```Python``` versioning
```shell
python3 --version
python3 -m pip --version
python3 -m ensurepip --default-pip
```

- Create a virtual environment:

```
make setup-venv

OR

python3 -m pip install virtualenv
python3 -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```


- Activate a virtual environment
```shell
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

Output:
```
(venv) <UserName>@<HostName> PythonPackaging %
```

The parenthesized ```(venv)``` in front of the prompt indicates that you’ve successfully activated the virtual environment.


- Upgrade ```pip``` & Install requirements/dependencies:

```
make install-packages

OR

pip install --upgrade pip
pip install -r ./requirements.txt
```

- Deactivate a virtual environment
```shell
deactivate
```

Output:
```
<UserName>@<HostName> PythonPackaging %
```

- Install individual packages
```shell
pip install requests
pip install beautifulsoup4
python -m pip install requests
```

- Install packages from ```requirements.txt``` file
```shell
pip install -r requirements.txt
```

### Save Requirements (Dependencies)
```shell
pip freeze > requirements.txt
```

### Build Project & Distribution Packages

The next step is to generate distribution packages for the package. These are archives that are uploaded to 
the ```Python``` Package Index and can be installed by ```pip```.

Make sure you have the latest version of PyPA’s build installed:

#### Generating distribution archives
```shell
python -m pip install build
python -m pip install --upgrade build
```

Now run this command from the same directory where ```pyproject.toml``` is located:

```shell
python -m build
```

This command should output a lot of text and once completed should generate two files in the dist directory:


```shell
dist/
├── pythonpackaging_rslakra-0.0.1-py3-none-any.whl
└── pythonpackaging_rslakra-0.0.1.tar.gz
```


#### Uploading the distribution archives

Finally, it’s time to upload your package to the Python Package Index!

To securely upload your project, you’ll need a PyPI API token. 

Create one at https://test.pypi.org/manage/account/#api-tokens, setting the “```Scope```” to “```Entire account```”. 
Don’t close the page until you have copied and saved the token — you won’t see that token again.

Now that you are registered, you can use twine to upload the distribution packages. You’ll need to install ```Twine```:
```shell
python -m pip install --upgrade twine
```

- Once installed, run ```Twine``` to upload all of the archives under ```dist```:
```shell
python -m twine upload --repository testpypi dist/*
```

You will be prompted for an API token. 
Use the **token** value, including the ```pypi-``` prefix. 

Note that the input will be hidden, so be sure to paste correctly.

After the command completes, you should see output similar to this:

```shell
(venv) <UserName>@<HostName> PythonPackaging % python3 -m twine upload --repository testpypi dist/*
Uploading distributions to https://test.pypi.org/legacy/
Enter your API token: 
Uploading pythonpackaging_rslakra-0.0.1-py3-none-any.whl
100% ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 15.3/15.3 kB • 00:00 • ?
Uploading pythonpackaging_rslakra-0.0.1.tar.gz
100% ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 15.4/15.4 kB • 00:00 • ?

View at:
https://test.pypi.org/project/PythonPackaging-rslakra/0.0.1/
(venv) <UserName>@<HostName> PythonPackaging %
```

### Installing your uploaded package:

You can use pip to install your package and verify that it works. 
Create a virtual environment and install your package from TestPyPI:
```shell
python -m pip install --index-url https://test.pypi.org/simple/ --no-deps example-package-YOUR-USERNAME-HERE
```

Example:
```shell
python -m pip install --index-url https://test.pypi.org/simple/ --no-deps PythonPackaging-rslakra

OR

pip install -i https://test.pypi.org/simple/ PythonPackaging-rslakra==0.0.1
```

- Installation Results:
```shell
(venv) <UserName>@<HostName> TestPackage % pip install -i https://test.pypi.org/simple/ PythonPackaging-rslakra==0.0.1
Looking in indexes: https://test.pypi.org/simple/
Collecting PythonPackaging-rslakra==0.0.1
  Downloading https://test-files.pythonhosted.org/packages/97/5a/05b50761d6ad780a4f7c5166f4135ed14976c8ad9249fdccc978e385adb1/pythonpackaging_rslakra-0.0.1-py3-none-any.whl.metadata (7.0 kB)
Downloading https://test-files.pythonhosted.org/packages/97/5a/05b50761d6ad780a4f7c5166f4135ed14976c8ad9249fdccc978e385adb1/pythonpackaging_rslakra-0.0.1-py3-none-any.whl (6.0 kB)
Installing collected packages: PythonPackaging-rslakra
Successfully installed PythonPackaging-rslakra-0.0.1
```

Make sure to specify your username in the package name!


### Uninstalling your packages
```shell
pip uninstall -r requirements.txt
```


### How to use this package?
```shell
from rslakra.utils import TimeUtils
import sys
from rslakra.pair import TokenPair, TokenList

print(f"sys.path={sys.path}")
print()
print(f"now_utc: {TimeUtils.now_utc()}")


tokens = TokenList()
print(f"tokens: {tokens}")
tokens.add_pairs("Name", "Rohtash")
print(f"tokens: {tokens}")
tokens_dict = tokens.as_dict()
print(f"tokens_dict: {tokens_dict}")
```


## Testing

### Unit Tests

```shell
python -m unittest
python -m unittest discover -s ./pytheorem/tests -p "test_*.py"
```


# Reference

- [The Python Package Index (PyPI)](https://pypi.org/)
- [Packaging Python Projects](https://packaging.python.org/en/latest/tutorials/packaging-projects/)
- [PyInstaller Manual](https://pyinstaller.org/en/stable/)



# Author

---

- Rohtash Lakra

