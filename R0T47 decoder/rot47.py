#!/usr/bin/env python3
"""
ROT47 Challenge Decoder
=======================

Usage:
    python3 rot47.py
    python3 rot47.py "7=28Lx{@G6~776?D:G6$64FC:EJPN"
    echo "7=28Lx{@G6~776?D:G6$64FC:EJPN" | python3 rot47.py

ROT47 is symmetric: applying it twice returns the original text.
"""

import argparse
import sys


def rot47(text: str) -> str:
    """Encode or decode printable ASCII text using ROT47."""
    result = []

    for char in text:
        code = ord(char)

        if 33 <= code <= 126:
            code = 33 + ((code - 33 + 47) % 94)

        result.append(chr(code))

    return "".join(result)


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Encode/decode printable ASCII text using ROT47."
    )
    parser.add_argument(
        "text",
        nargs="*",
        help="ROT47 text. If omitted, input is read interactively or from stdin.",
    )
    parser.add_argument(
        "-q",
        "--quiet",
        action="store_true",
        help="Print only the decoded result.",
    )

    args = parser.parse_args()

    if args.text:
        text = " ".join(args.text)
    elif not sys.stdin.isatty():
        text = sys.stdin.read().rstrip("\r\n")
    else:
        print("=" * 56)
        print("                 ROT47 DECODER")
        print("=" * 56)
        print("Enter a ROT47 string, then press Enter.")
        print("Press Ctrl+C to exit.\n")

        try:
            text = input("ROT47 > ")
        except (KeyboardInterrupt, EOFError):
            print("\nExiting.")
            return

    if not text:
        print("Error: no input supplied.", file=sys.stderr)
        sys.exit(1)

    decoded = rot47(text)

    if args.quiet:
        print(decoded)
    else:
        print("\nDecoded:")
        print("-" * 56)
        print(decoded)


if __name__ == "__main__":
    main()
