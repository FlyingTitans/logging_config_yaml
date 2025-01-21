*******************
logging_config_yaml
*******************

A python package that provides a way to do logging configuration using a
YAML file.

=============
Prerequisites
=============

1. Required packages:

   1. `Python <https://www.python.com>`_ version 3.10
   2. `Pip <https://pip.pypa.io/en/stable/>`_ minimum version 24.0
   3. `Task (aka Taskfile) <https://taskfile.dev>`_ version 3.35
   4. `pre-commit <https://pre-commit.com>`_ minimum version 4.0

2. Recommended packages:

   1. `direnv <https://direnv.net>`_
   2. `virtualenv <https://virtualenv.pypa.io/en/latest/>`_


=================
Development Setup
=================

1. Clone this repository.
2. Create and activate a virtual environment (e.g. `python -m venv .venv`).
3. Run `task setup:dev` which will get all necessary python packages, setup
   git hooks, and add anything to docker (e.g. networks) necessary for the
   server to run.


direnv
======

It is recommended that `direnv` be installed and a `.envrc` file be created
in the local clone of the repository. This can handle setting the environment
when changing into the directory, and if a virtual environment is not
available, creating a new one so `task setup:dev` may be run.


pre-commit
==========

The [pre-commit](https://pre-commit.com) framework will check any changed
file for conformance to coding standards, formatting standards, and security
standards before allowing a commit to occur.

Each of these checks are done in GitHub Actions as part of the CI/CD chain.
So having pre-commit perform these checks before commit improves the chances
that a PR will pass its checks.
