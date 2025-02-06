# indic2slp/maps/tamil_map.py

TAMIL_MAP = {
    # -- Independent vowels --
    'அ': 'a',
    'ஆ': 'A',
    'இ': 'i',
    'ஈ': 'I',
    'உ': 'u',
    'ஊ': 'U',
    'எ': 'e',
    'ஏ': 'E',
    'ஒ': 'o',
    'ஓ': 'O',
    'ஐ': 'E',  # or some prefer splitting ai
    'ஔ': 'O',

    # -- Consonants --
    'க': 'k',
    'ங': 'N',
    'ச': 'c',
    'ஞ': 'Y',
    'ட': 'w',
    'ண': 'R',
    'த': 't',
    'ந': 'n',
    'ப': 'p',
    'ம': 'm',
    'ய': 'y',
    'ர': 'r',
    'ல': 'l',
    'வ': 'v',
    'ழ': 'Z',   # Retroflex approximant
    'ள': 'L',
    'ற': 'r2',  # Alveolar/trilled r
    'ன': 'n2',  # Alveolar n

    # Grantha letters for Sanskrit sounds in Tamil texts
    'ஸ': 's',
    'ஷ': 'z',  # conflict: 'z' = ṣ in SLP1, but used in Tamil for ś/ṣ
    'ஹ': 'h',
    'ஜ': 'j',

    # Aytham
    'ஃ': 'H2',  # Or some notation if you choose

    # You might include any additional signs or diacritics...
}
