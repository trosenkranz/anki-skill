#!/usr/bin/env python3
"""Text-to-speech via the OpenRouter audio/speech API.

Usage:
    ./tts.py -i "Привіт, світе!" -o output.wav

The API key is read from the OPENROUTER_API_KEY environment variable.
"""

import argparse
import os
import sys
import wave

import requests

API_URL = "https://openrouter.ai/api/v1/audio/speech"
MODEL = "google/gemini-3.1-flash-tts-preview"
VOICE = "Leda"
RESPONSE_FORMAT = "pcm"  # Gemini TTS only supports "pcm" (raw 16-bit LE audio)


def parse_args():
    parser = argparse.ArgumentParser(
        description="Generate speech audio from text using the OpenRouter API."
    )
    parser.add_argument(
        "-i", "--input",
        required=True,
        help="Text to synthesize",
    )
    parser.add_argument(
        "-o", "--output",
        default="output.wav",
        help="Output audio file name (default: %(default)s)",
    )
    return parser.parse_args()


def main():
    args = parse_args()

    api_key = os.environ.get("OPENROUTER_API_KEY")
    if not api_key:
        sys.exit("Error: OPENROUTER_API_KEY environment variable is not set.")

    response = requests.post(
        url=API_URL,
        headers={
            "Authorization": f"Bearer {api_key}",
            "Content-Type": "application/json",
        },
        json={
            "model": MODEL,
            "input": args.input,
            "voice": VOICE,
            "response_format": RESPONSE_FORMAT,
        },
    )

    if response.status_code != requests.codes.ok:
        sys.exit(
            f"Error: API returned HTTP {response.status_code}: {response.text}"
        )

    rate, channels = parse_pcm_content_type(
        response.headers.get("Content-Type", "")
    )
    save_wav(response.content, args.output, rate, channels)
    print(
        f"Audio saved to {args.output} ({rate} Hz, {channels} ch). "
        f"Generation ID: {response.headers.get('X-Generation-Id')}"
    )


def parse_pcm_content_type(content_type):
    """Extract sample rate and channel count from e.g.
    'audio/pcm;rate=24000;channels=1'. Returns (rate, channels)."""
    rate, channels = 24000, 1
    for part in content_type.split(";")[1:]:
        key, _, value = part.strip().partition("=")
        if key == "rate":
            rate = int(value)
        elif key == "channels":
            channels = int(value)
    return rate, channels


def save_wav(pcm_data, path, rate, channels):
    """Wrap raw 16-bit little-endian PCM in a WAV container."""
    with wave.open(path, "wb") as wav_file:
        wav_file.setnchannels(channels)
        wav_file.setsampwidth(2)  # 16-bit
        wav_file.setframerate(rate)
        wav_file.writeframes(pcm_data)


if __name__ == "__main__":
    main()
