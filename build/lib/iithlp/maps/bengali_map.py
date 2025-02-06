BENGALI_MAP = {
    # -- Vowels (independent) --
    'অ': 'a',
    'আ': 'A',
    'ই': 'i',
    'ঈ': 'I',
    'উ': 'u',
    'ঊ': 'U',
    'এ': 'e',
    'ঐ': 'E',
    'ও': 'o',
    'ঔ': 'O',
    'ঋ': 'f',
    'ঌ': 'x',   # rarely used

    # -- Consonants --
    'ক': 'k',
    'খ': 'K',
    'গ': 'g',
    'ঘ': 'G',
    'ঙ': 'N',
    'চ': 'c',
    'ছ': 'C',
    'জ': 'j',
    'ঝ': 'J',
    'ঞ': 'Y',
    'ট': 'w',  # retroflex t
    'ঠ': 'W',
    'ড': 'q',  # retroflex d
    'ঢ': 'Q',
    'ণ': 'R',  # retroflex n
    'ত': 't',  # dental t
    'থ': 'T',
    'দ': 'd',
    'ধ': 'D',
    'ন': 'n',
    'প': 'p',
    'ফ': 'P',  # aspirated p
    'ব': 'b',
    'ভ': 'B',
    'ম': 'm',
    'য': 'y',  # often merges with j; usage can vary
    'র': 'r',
    'ল': 'l',
    'শ': 'S',  # palatal s
    'ষ': 'z',  # retroflex s
    'স': 's',
    'হ': 'h',
    # ঳ does not exist in standard Bengali; if it appears, might map to L

    # ড়, ঢ় (if you want to keep them distinct from ড, ঢ):
    # 'ড়': ???  # often [ɽ], you could map to q' if you want
    # 'ঢ়': ??? # often [ɽʱ], map to Q' or something

    # Additional forms, nukta, etc. if used for Perso-Arabic sounds
    # 'য়', 'ড়', 'ঢ়' etc.

    # Anusvara, visarga, chandrabindu
    'ং': 'M',  # anusvara
    'ঃ': 'H',  # visarga
    'ঁ': 'M',  # chandrabindu can also map to M or a distinct marker
}
