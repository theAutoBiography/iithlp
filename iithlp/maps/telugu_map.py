TELUGU_MAP = {
    # -- Vowels (independent) --
    'అ': 'a',
    'ఆ': 'A',
    'ఇ': 'i',
    'ఈ': 'I',
    'ఉ': 'u',
    'ఊ': 'U',
    'ఎ': 'e',
    'ఏ': 'E',
    'ఒ': 'o',
    'ఓ': 'O',
    'ఐ': 'E',   # or split differently (ai)
    'ఔ': 'O',   # or split differently (au)
    'ఋ': 'f',   # vocalic r
    'ఌ': 'x',   # vocalic l (rarely used)
    # ... add the long forms if needed (ఘనాజా...)

    # -- Consonants --
    'క': 'k',
    'ఖ': 'K',
    'గ': 'g',
    'ఘ': 'G',
    'ఙ': 'N',  # velar nasal
    'చ': 'c',
    'ఛ': 'C',
    'జ': 'j',
    'ఝ': 'J',
    'ఞ': 'Y',
    'ట': 'w',  # retroflex t
    'ఠ': 'W',
    'డ': 'q',
    'ఢ': 'Q',
    'ణ': 'R',  # retroflex n
    'త': 't',  # dental t
    'థ': 'T',
    'ద': 'd',
    'ధ': 'D',
    'న': 'n',
    'ప': 'p',
    'ఫ': 'P',
    'బ': 'b',
    'భ': 'B',
    'మ': 'm',
    'య': 'y',
    'ర': 'r',
    'ల': 'l',
    'వ': 'v',
    'శ': 'S',  # palatal s
    'ష': 'z',  # retroflex s in SLP1
    'స': 's',
    'హ': 'h',
    'ళ': 'L',  # retroflex lateral

    # Sometimes there's a “ఱ” (r with a diacritic), alveolar/特殊
    # If you want it distinct from ర, you can map to r2:
    'ఱ': 'r2',

    # Other marks
    # Chandrabindu / Visarga / Anusvara, if used:
    'ం': 'M',  # anusvara
    'ః': 'H',  # visarga
    # 'ఁ': ???   # chandrabindu if it exists
}
