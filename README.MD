# Slack Bot

This project aims to help the team at production support from MileZero and any other to enter all the slack channels that they need to.

## How to use it

There are a couple of dependencie that need to be installed first but the use itself is very simple and straightforward

When everything is ready, just drag a .xlsx file containing all the channels you need to join in into the project folder and rename it to `channels.xlsx`

This file must follow the structure found on `model.xlsx` that is also on the project folder

## Install Dependencies

### Python

This project uses Python 3.11.2. Click [here](https://www.python.org/downloads/release/python-3112/) to download and install it

### Pip

Pip is a python package manager just like npm. Usually, python already comes with Pip but if hasn't in your case, open the command prompt and run `python -m ensurepip --upgrade`

### Virtualenv

Virtualenv will take care to install the project dependencies only to the project folder.
To install virtualenv, open the command prompt and run `pip install virtualenv`

After that, open a command prompt at the project folder and run `virtualenv venv`

### Activate venv

On Unix or MacOS, using the bash shell run `source venv/bin/activate`

On Unix or MacOS, using the csh shell: run `source venv/bin/activate.csh`

On Unix or MacOS, using the fish shell: run `source venv/bin/activate.fish`

On Windows using the Command Prompt: run `source venv/bin/activate.bat`

On Windows using PowerShell: run `source venv/bin/Activate.ps1`

### Install dependencies

With the venv activated, run `pip install -r requirements.txt`

### Run

Now you should be able to run the project on the console with `python main.py`
