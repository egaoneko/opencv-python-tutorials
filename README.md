# OpenCV Python Tutorials

## Installation

### Install virtualenv

```sh
# Install virtualenv & virtualenvwrapper
pip3 install virtualenv virtualenvwrapper
```
### Set virtualenvwrapper

```sh
# Set virtualenvwrapper environments
mkdir ~/.virtualenvs
vi ~/.zshrc # if you use bash shell, edit .bashrc
```

```sh
# python virtualenv settings
export WORKON_HOME=~/.virtualenvs
export VIRTUALENVWRAPPER_PYTHON='$(command \which python3)'  # Usage of python3
source /usr/local/bin/virtualenvwrapper.sh
```
### virtualenvwrapper command

* `mkvirtualenv -p=python3.x name` : make env
* `rmvirtualenv name`: remove env
* `workon name`: activate source
* `deactivate name`: deactivate source
