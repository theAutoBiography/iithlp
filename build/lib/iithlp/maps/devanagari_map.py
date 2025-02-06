# indic2slp/maps/devanagari_map.py

DEVANAGARI_MAP = {
    # -- Vowels --
    'अ': 'a',  'आ': 'A',
    'इ': 'i',  'ई': 'I',
    'उ': 'u',  'ऊ': 'U',
    'ए': 'e',  'ऐ': 'E',
    'ओ': 'o',  'औ': 'O',
    'ऋ': 'f',  'ॠ': 'F',
    'ऌ': 'x',  'ॡ': 'X',

    # -- Consonants --
    'क': 'k',  'ख': 'K',
    'ग': 'g',  'घ': 'G',
    'ङ': 'N',
    'च': 'c',  'छ': 'C',
    'ज': 'j',  'झ': 'J',
    'ञ': 'Y',
    'ट': 'w',  'ठ': 'W',
    'ड': 'q',  'ढ': 'Q',
    'ण': 'R',
    'त': 't',  'थ': 'T',
    'द': 'd',  'ध': 'D',
    'न': 'n',
    'प': 'p',  'फ': 'P',
    'ब': 'b',  'भ': 'B',
    'म': 'm',
    'य': 'y',
    'र': 'r',
    'ल': 'l',
    'व': 'v',
    'श': 'S',
    'ष': 'z',  # retroflex s
    'स': 's',
    'ह': 'h',

    # Marathi extra
    'ळ': 'L',

    # Nukta letters (Perso-Arabic)
    'क़': 'q\'',  # [q]
    'ख़': 'x\'',  # [x]
    'ग़': 'g\'',  # [ɣ]
    'ज़': 'z\'',  # [z]
    'फ़': 'f\'',  # [f]
    # Devanagari script might also have ड़ (ड़ = [ɽ])...
    # etc.

    # Other signs
    'ं': 'M',  # anusvara
    'ः': 'H',  # visarga
    'ँ': 'M',  # chandrabindu -> M or some anunasik marker
    'ऽ': '\'', # avagraha
}
