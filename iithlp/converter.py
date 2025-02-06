import pandas as pd

# Load the CSV file with character mappings
file_path = 'iithlp/data/mappings.csv'
df = pd.read_csv(file_path)

# Build mapping dictionaries for each script
script_mappings = {
    'devanagari': dict(zip(df['Devanagari'].dropna(), df['Roman'].dropna())),
    'tamil': dict(zip(df['Tamil'].dropna(), df['Roman'].dropna())),
    'telugu': dict(zip(df['Telugu'].dropna(), df['Roman'].dropna())),
    'malayalam': dict(zip(df['Malayalam'].dropna(), df['Roman'].dropna())),
}


def convert_to_iithlp(text: str, script: str) -> str:
    """
    Converts input text from a given script to the iithlp format.

    Args:
        text (str): The original script text.
        script (str): The script name ('devanagari', 'tamil', 'telugu', 'malayalam').

    Returns:
        str: The converted text in iithlp format.
    """
    if script.lower() not in script_mappings:
        raise ValueError(f"Unsupported script: {script}. Supported scripts: {list(script_mappings.keys())}")

    mapping = script_mappings[script.lower()]
    converted = []

    for char in text:
        if char in mapping:
            converted.append(mapping[char])
        else:
            converted.append(char)  # Pass through unmapped characters

    return ''.join(converted)


# Example usage
if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(description="Convert text from Indic scripts to iithlp format.")
    parser.add_argument("text", help="The input text to convert.")
    parser.add_argument("script", choices=['devanagari', 'tamil', 'telugu', 'malayalam'], help="The script of the input text.")
    args = parser.parse_args()

    converted_text = convert_to_iithlp(args.text, args.script)
    print(converted_text)