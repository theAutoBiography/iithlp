# iithlp/cli.py

import argparse
import sys
from iithlp.convert import to_extended_slp1, file_to_extended_slp1

def main():
    parser = argparse.ArgumentParser(description="iithlp CLI tool")

    # The script/language name
    parser.add_argument(
        "--script",
        required=True,
        help="Which script the input text is in (e.g., 'tamil', 'malayalam', 'devanagari')"
    )

    # Option 1: direct text
    parser.add_argument(
        "--text",
        help="The text to convert (if you don't want to use a file)."
    )

    # Option 2: file path
    parser.add_argument(
        "--file",
        help="Path to an input file containing text to convert"
    )

    # Optional output file
    parser.add_argument(
        "--output",
        help="If specified, write converted text to this file instead of stdout"
    )

    args = parser.parse_args()

    # Validate that we have either text or file
    if not args.text and not args.file:
        parser.error("You must provide either --text or --file.")

    # If user gave file, convert file contents
    if args.file:
        converted = file_to_extended_slp1(args.file, args.script)
    else:
        # Otherwise, just convert the inline text
        converted = to_extended_slp1(args.text, args.script)

    # If user specified an output file, write there; else print to stdout
    if args.output:
        with open(args.output, 'w', encoding='utf-8') as fout:
            fout.write(converted)
        print(f"Converted text written to {args.output}")
    else:
        print(converted)


if __name__ == "__main__":
    main()
