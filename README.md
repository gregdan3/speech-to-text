# Python Speech to Text CLI
I got myself a personal voice recorder and wanted to see about converting audio
files it produced into text files. Existing libraries I found worked well, but
what was missing? A CLI tool for it, of course!



### Project goals
I want to be able to provide an arbitrary audio file to the script and have it
output the corresponding text into a file in the invoked directory.


### Work done so far
Currently, you can pass in a .wav file (others too, probably, but untested) and
that file will be "recorded" and "recognized" by the
[SpeechRecognition](https://github.com/Uberi/speech_recognition) library.
It's somewhat simplistic, and only supports the `pocketsphinx` engine thus far,
but it works decently. Currently only prints text to the terminal, but that can
be redirected (`>`) to a file at the user's leisure.

### Work to be done
In no particular order, and not comprehensively:
- Install as a CLI tool properly (for testing, in `/usr/local/bin/`)
- Collect specified audio file argument from working directory (for above)
- Set up the process of writing to a user-specified file in the current
  directory, and notify the user when that is done
- Allow output file to be omitted, instead printing the result to the terminal
- Make the ability to choose an engine useful by supporting the other engines'
  required arguments (tokens, login parameters)
- Fallback to pocketsphinx engine if there is no network connection
- Verify that the package can work relatively independently (user doesn't
  need to install extra packages) as just a python script
- Omit some dependencies, to be made optional, as SpeechRecognition itself does

### Concerns
The SpeechRecognition library is noted to be outdated in a
[few](https://github.com/Uberi/speech_recognition/issues/453)
[different](https://github.com/Uberi/speech_recognition/issues/455)
[ways](https://github.com/Uberi/speech_recognition/issues/385).

It may be necessary to seek out a different library entirely, or abandon the use
of a library at the cost of reduced support for a variety of engines.
