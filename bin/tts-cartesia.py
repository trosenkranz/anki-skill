#!/usr/bin/env python3
"""Text-to-speech via the Cartesia API (Sonic 3.6).

Usage:
    bin/.venv/bin/python bin/tts-cartesia.py -i "Привіт, світе!" -o output.mp3
    bin/.venv/bin/python bin/tts-cartesia.py --list-voices
    bin/.venv/bin/python bin/tts-cartesia.py --save-voice <voice-id>

The API key is read from the CARTESIA_API_KEY environment variable
(a .env file in the bin/ directory is honored as well).

The voice is taken from (--voice flag > CARTESIA_VOICE_ID env > .env file).
Run --list-voices to see Ukrainian voices, then --save-voice to persist one
to the .env file.

Must be run with the venv interpreter in bin/.venv (see bin/requirements.txt;
recreate with: python3 -m venv bin/.venv && bin/.venv/bin/pip install -r bin/requirements.txt).
"""

import argparse
import os
import sys

from dotenv import load_dotenv, set_key
from cartesia import Cartesia, APIConnectionError, APIStatusError, AuthenticationError

MODEL = "sonic-3.6"
DEFAULT_LANGUAGE = "uk"

# MP3: container + required rate/bitrate (see docs.cartesia.ai Output Format).
OUTPUT_FORMATS = {
    "mp3": {"container": "mp3", "sample_rate": 44100, "bit_rate": 128000},
    "wav": {"container": "wav", "encoding": "pcm_s16le", "sample_rate": 44100},
}

BIN_DIR = os.path.dirname(os.path.abspath(__file__))
DOTENV_PATH = os.path.join(BIN_DIR, ".env")


def parse_args():
    parser = argparse.ArgumentParser(
        description="Generate speech audio from text using the Cartesia Sonic API."
    )
    parser.add_argument(
        "-i", "--input",
        help="Text to synthesize",
    )
    parser.add_argument(
        "-o", "--output",
        default="output.mp3",
        help="Output audio file name (default: %(default)s)",
    )
    parser.add_argument(
        "--voice",
        help="Voice ID for this run (overrides CARTESIA_VOICE_ID)",
    )
    parser.add_argument(
        "--language",
        default=DEFAULT_LANGUAGE,
        help="Language code, e.g. uk, de, en (default: %(default)s)",
    )
    parser.add_argument(
        "--format",
        choices=sorted(OUTPUT_FORMATS),
        default="mp3",
        help="Output container format (default: %(default)s)",
    )
    parser.add_argument(
        "--list-voices",
        action="store_true",
        help=f"List available voices for language '{DEFAULT_LANGUAGE}' and exit",
    )
    parser.add_argument(
        "--save-voice",
        metavar="VOICE_ID",
        help="Persist a voice ID to .env as CARTESIA_VOICE_ID and exit",
    )
    args = parser.parse_args()

    if not args.list_voices and not args.save_voice and not args.input:
        parser.error("either -i/--input, --list-voices, or --save-voice is required")
    return args


def resolve_api_key():
    load_dotenv(DOTENV_PATH)
    api_key = os.environ.get("CARTESIA_API_KEY")
    if not api_key:
        sys.exit(
            "Error: CARTESIA_API_KEY environment variable is not set "
            f"(you can also put it in {DOTENV_PATH})."
        )
    return api_key


def resolve_voice_id(args):
    if args.voice:
        return args.voice
    load_dotenv(DOTENV_PATH)
    voice_id = os.environ.get("CARTESIA_VOICE_ID")
    if not voice_id:
        sys.exit(
            "Error: no voice configured. Run --list-voices to see options, "
            "then persist one with --save-voice <voice-id>."
        )
    return voice_id


def save_voice_id(voice_id):
    set_key(DOTENV_PATH, "CARTESIA_VOICE_ID", voice_id)
    print(f"Voice ID saved to {DOTENV_PATH}: CARTESIA_VOICE_ID={voice_id}")


def list_voices(client, language):
    page = client.voices.list(
        limit=100,
        extra_query={"language": language},
    )
    voices = [v for p in page.iter_pages() for v in p.data]
    # Safety net in case the server-side filter misses: keep voices that are
    # native in the language or have a matching locale among their locales.
    def matching_locales(v):
        return [l for l in (v.locales or []) if l.locale.startswith(language)]

    voices = [v for v in voices if v.language == language or matching_locales(v)]
    voices.sort(key=lambda v: (not any(l.is_native for l in matching_locales(v)), v.name.lower()))

    if not voices:
        print(f"No voices found for language '{language}'.")
        return

    print(f"Voices for language '{language}' ({len(voices)}):\n")
    for v in voices:
        native = ", ".join(
            l.locale for l in (v.locales or []) if l.is_native
        ) or v.language
        gender = v.gender or "?"
        print(f"  {v.id}")
        print(f"    {v.name}  [{gender}, native: {native}]")
        if v.description:
            print(f"    {v.description}")
        print()


def generate(client, args, voice_id):
    response = client.tts.generate(
        model_id=MODEL,
        transcript=args.input,
        voice=voice_id,
        language=args.language,
        output_format=OUTPUT_FORMATS[args.format],
    )
    response.write_to_file(args.output)
    size = os.path.getsize(args.output)
    print(f"Audio saved to {args.output} ({size} bytes, {args.format.upper()}, voice {voice_id}).")


def main():
    args = parse_args()
    api_key = resolve_api_key()
    client = Cartesia(api_key=api_key)

    try:
        if args.save_voice:
            save_voice_id(args.save_voice)
        elif args.list_voices:
            list_voices(client, args.language)
        else:
            generate(client, args, resolve_voice_id(args))
    except AuthenticationError as e:
        sys.exit(f"Error: authentication failed ({e.status_code}). Check CARTESIA_API_KEY.")
    except APIConnectionError as e:
        sys.exit(f"Error: connection to Cartesia API failed: {e.__cause__}")
    except APIStatusError as e:
        sys.exit(f"Error: API returned HTTP {e.status_code}: {e.message}")


if __name__ == "__main__":
    main()
