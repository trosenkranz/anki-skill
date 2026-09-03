---
name: ukrainian-example-audio
description: Generate an MP3 pronunciation recording for a Ukrainian example sentence on an Anki flash card using the project's bin/tts-cartesia.py script (Cartesia Sonic TTS). Use when creating or updating Ukrainian-language Anki cards and an audio file is explicitly requested to be generated.
---

# Ukrainian example audio

Generate an MP3 file for the Ukrainian example sentence associated with the current Anki card.

## Inputs

When this skill is invoked:

1. Get the Ukrainian example sentence from the current card/task context. This exact sentence is passed to `tts-cartesia.py` via `-i`.
2. Get the German or English translation/phrase that identifies the card. Convert it to UpperCamelCase (remove spaces and punctuation; preserve word boundaries by capitalizing each word), then append `_bsp.mp3`. For example:
   - `sich ins Zeug legen` → `SichInsZeugLegen_bsp.mp3`
   - `to make an effort` → `ToMakeAnEffort_bsp.mp3`
3. If either the Ukrainian sentence or the identifying phrase is unavailable or ambiguous, ask for it instead of guessing.

The output file must be written in the current working directory unless the user explicitly supplies another path. Do not overwrite an existing file without confirming first.

## Generate the audio

Run the project's TTS script from the project root with the venv interpreter (`bin/tts-cartesia.py` takes the sentence via `-i` and the output file via `-o`; it reads the API key from the `CARTESIA_API_KEY` environment variable and the voice ID from `CARTESIA_VOICE_ID` in the `bin/.env` file, and exits with an error message on failure):

```bash
bin/.venv/bin/python bin/tts-cartesia.py -i 'УКРАЇНСЬКЕ_РЕЧЕННЯ' -o 'GermanOrEnglishPhrase_bsp.mp3'
```

Single-quote the sentence. For a literal apostrophe inside it (common in Ukrainian, e.g. `ім'я`), use `'\''`.

Use the exact `-i` sentence from the card; do not translate, transliterate, or alter it. On success the script prints the output path; verify the file exists and is non-empty, then report it. The output is MP3 (Cartesia Sonic 3.6, voice "Oleh", the only native Ukrainian voice in the library — configurable via `.env`/`--save-voice`).
