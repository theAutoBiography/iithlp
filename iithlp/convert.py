# iithlp/convert.py

from iithlp.maps.tamil_map import TAMIL_MAP
from iithlp.maps.malayalam_map import MALAYALAM_MAP
from iithlp.maps.devanagari_map import DEVANAGARI_MAP
from iithlp.maps.kannada_map import KANNADA_MAP
from iithlp.maps.telugu_map import TELUGU_MAP
from iithlp.maps.bengali_map import BENGALI_MAP

SCRIPT_MAPS = {
    'tamil': TAMIL_MAP,
    'malayalam': MALAYALAM_MAP,
    'devanagari': DEVANAGARI_MAP,
    'kannada': KANNADA_MAP,
    'telugu': TELUGU_MAP,
    'bengali': BENGALI_MAP,
    # etc. add more scripts here...
}

def to_extended_slp1(text: str, script: str) -> str:
    """
    Convert `text` from the given `script` into the Extended SLP1 scheme.
    """
    script = script.lower()
    mapping = SCRIPT_MAPS.get(script)
    if mapping is None:
        raise ValueError(f"No mapping found for script '{script}'")

    output_chars = []
    for char in text:
        if char in mapping:
            output_chars.append(mapping[char])
        else:
            # Pass through unmapped chars as-is
            output_chars.append(char)

    return "".join(output_chars)


def file_to_extended_slp1(input_file: str, output_file: str, script: str) -> None:
    with open(input_file, 'r', encoding='utf-8') as fin:
        content = fin.read()
    converted = to_extended_slp1(content, script)
    with open(output_file, 'w', encoding='utf-8') as fout:
        fout.write(converted)
