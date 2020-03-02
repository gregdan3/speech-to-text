#!/usr/bin/env python3
import logging
import sys  # TODO: use to read audio files from sys.stdin.buffer...

# pip
import speech_recognition as sr

# local
from speech_to_text.file_utils import load_token, load_yml_file, load_audio_file
from speech_to_text.log_utils import init_logger
from speech_to_text.arguments import BaseArgParser

__all__ = []

_log = logging.getLogger(__name__)


def main(argv):
    init_logger(argv.log_level, argv.log_file, argv.log_file_level)

    # token = load_token(argv.token)
    # config = load_yml_file(argv.config)

    try:
        recognizer = sr.Recognizer()

        engine = "recognize_" + argv.engine
        try:
            engine_func = recognizer.__getattribute__(engine)
        except AttributeError:
            _log.critical("Invalid engine %s provided! Shutting down...", argv.engine)
            sys.exit()

        with sr.AudioFile(argv.audio) as src:
            audio = recognizer.record(src)
            text = engine_func(audio)  # implicitly attached to recognizer
            # TODO: handle other engine funcs with other attributes?
            print(text)
    except KeyboardInterrupt:
        _log.info("Shutting down.")


if __name__ == "__main__":
    parser = BaseArgParser()
    ARGV = parser.parse_args()
    main(ARGV)
