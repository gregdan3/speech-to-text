#!/usr/bin/env python3

import argparse


def BaseArgParser():
    """ Provides an argparse.ArgumentParser with some arguments pre-prepared.
        The object is provided, as opposed to the already parsed args, so that
        another user/script may configure the parser even further if necessary. """
    parser = argparse.ArgumentParser()

    parser.add_argument(
        "audio",
        metavar="AUDIO",
        type=str,
        help="The audio file to read from for speech recognition purposes",
    )
    parser.add_argument(
        "-e",
        "--engine",
        dest="engine",
        metavar="ENGINE",
        type=str,
        choices=[
            "azure",
            "bing",
            "google",
            "google_cloud",
            "houndify",
            "ibm",
            "sphinx",
            "wit",
        ],
        default="sphinx",
        help="The engine to use for your speech recognition process",
    )
    parser.add_argument(
        "-t",
        "--token",
        dest="token",
        metavar="TOKEN",
        type=str,
        default="token.txt",
        help="The location of the token file required by the API you chose, if\
        applicable.",
    )
    parser.add_argument(
        "-o",
        "--output",
        dest="output",
        metavar="OUTPUT",
        type=str,
        default="output.txt",
        help="The name of the file to output text content to",
    )
    parser.add_argument(
        "-c",
        "--config",
        dest="config",
        metavar="CONFIG_FILE",
        type=str,
        default="local_config.yml",
        help="The name of the configuration file [NOT IN USE]",
    )
    parser.add_argument(
        "-l",
        "--log-level",
        dest="log_level",
        metavar="LEVEL",
        type=str.upper,
        choices=["NOTSET", "DEBUG", "INFO", "WARNING", "ERROR", "CRITICAL"],
        default="WARNING",
        help="Logging level to stdout",
    )
    parser.add_argument(
        "--log-file",
        dest="log_file",
        metavar="LOG_FILE",
        type=str,
        default="errors.log",
        help="Log file to write to",
    )
    parser.add_argument(
        "--log-file-level",
        dest="log_file_level",
        metavar="LEVEL",
        type=str.upper,
        choices=["NOTSET", "DEBUG", "INFO", "WARNING", "ERROR", "CRITICAL"],
        default="WARNING",
        help="Logging level to file",
    )
    return parser  # allow user to configure later


def main():
    parser = BaseArgParser()
    argv = parser.parse_args()
    print("argv.token:          %s" % argv.token)
    print("argv.config:         %s" % argv.config)
    print("argv.log_level:      %s" % argv.log_level)
    print("argv.log_file:       %s" % argv.log_file)
    print("argv.log_file_level: %s" % argv.log_file_level)


if __name__ == "__main__":
    main()
