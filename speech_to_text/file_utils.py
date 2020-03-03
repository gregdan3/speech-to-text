#!/usr/bin/env python3
import os
import logging
import yaml
import __main__


__all__ = [
    "here",
    "cwd",
    "load_token",
    "load_yml_file",
    "find_file_in_cwd",
    "write_output_in_cwd",
]

here = os.path.abspath(os.path.dirname(__main__.__file__))
cwd = os.getcwd()

_log = logging.getLogger(__name__)


def load_yml_file(filename):
    with open(filename, "r") as f:
        command = yaml.full_load(f)
    return command


def load_token(token_name):
    with open(os.path.join(here, token_name)) as f:
        token = f.readline().strip()
    return token


def find_file_in_cwd(filename):
    return os.path.join(cwd, filename)


def write_output_in_cwd(filename, output):
    with open(os.path.join(cwd, filename), "w") as f:
        f.write(output)


def main():
    print(load_yml_file(os.path.join(here, "local_config.yml")))


if __name__ == "__main__":
    main()
