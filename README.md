# Python Template
This repository is my template for new Python 3 projects.

To get started, clone this repository to your device. When you want to start a new Python project, just copy the contents of the repository using `cp -r python-template your-project`. Then delete the `.git` folder with `rm -r .git`.

With the template copied, it is recommended that you should create a [virtual environment](https://virtualenv.pypa.io/en/latest/). Create a virtual development environment by using the `virtualenv` Python library. You can install this by executing `pip3 install virtualenv`. 

To create your environment, type `python3 -m virtualenv venv --prompt "(your-env) "`. Once created, you can activate it by using `source venv/bin/activate`. Once you are done developing, simply type `deactivate` in your terminal.

Next, run `pip install -r dev-requirements.txt` to collect the suggested Python libraries for linting, formatting, and running tests for your code.

Note that using `pip3` rather than `pip` to install your requirements may cause those libraries to be installed globally, rather than in your virtual environment.

## Contents
This repository contains a number of files.

### [.editorconfig](https://editorconfig.org/)
This is a file that enforces specific coding standards around indentation and use of whitespace. This includes the different types of whitespace. With this particular configuration, your Python files will be indented with spaces, and by 4 spaces with each indentation.

In order for this to work in your editor, you will likely need to install a plugin, though this may not be necessary. You can see which editors need a plugin [here](https://editorconfig.org/#download), and those that do not [here](https://editorconfig.org/#pre-installed).

### [.gitignore](https://git-scm.com/docs/gitignore)
The provided `.gitignore` file contains common folders and files you would want to exclude from version control that originate from Python files projects. You can read more about `.gitignore` files [here](https://git-scm.com/docs/gitignore).

### dev-requirements.txt
This is a Python [requirements file](https://pip.pypa.io/en/latest/user_guide/#requirements-files) that contains libraries for linting, formatting, and testing your code.

These libraries are [Flake8](https://flake8.pycqa.org/en/latest/), [Black](https://pypi.org/project/black/), and [pytest](https://docs.pytest.org/en/7.0.x/). These are orchestrated by [nox](https://nox.thea.codes/en/stable/).

### [noxfile.py](https://nox.thea.codes/en/stable/)
nox is an orchestration tool that is used to format, lint, and test code. `noxfile.py` contains the individual sessions to run when using the `nox` command. This version has sessions for linting, formatting, and testing code.

Once you have installed the `dev-requirements.txt` file, you can run the `nox` command to automatically lint, format, and test your code. This will fail if your code doesn't pass Flake8's linting paramters, if your code is reformatted by Black, or if your tests fail. You will get details about the failures at the end of each session.

### [setup.cfg](https://docs.python.org/3/distutils/configfile.html)
This is the setup file used to configure nox and Flake8. You can add more configuration options to this file as your project grows.

### LICENSE.md
This is a generic License that I provide with each of my personal projects. Read more about licenses [here](https://docs.github.com/en/repositories/managing-your-repositorys-settings-and-features/customizing-your-repository/licensing-a-repository)

### Makefile
This is a set of scripts used to build, test, and deploy a python library to Pypi.
