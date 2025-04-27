# IITHLP

A comprehensive transliteration scheme for Indian languages with a strict one-to-one character mapping.

## Overview

IITHLP is a Python package that provides a comprehensive transliteration scheme for 9 major Indian scripts covering 17 scheduled Indian languages. It ensures a strict one-to-one mapping between each Indic character and a single Roman character (with diacritics as needed), ensuring perfect reversibility while maintaining phonetic similarity.

## Supported Scripts and Languages

IITHLP v0.2.2 provides comprehensive transliteration support for 9 Indian scripts covering 17 of the 22 scheduled Indian languages:

| Script | Languages |
|--------|-----------|
| Devanagari | Hindi, Sanskrit, Marathi, Nepali, Konkani, Bodo, Maithili, Dogri |
| Bengali | Bengali, Assamese |
| Tamil | Tamil |
| Malayalam | Malayalam |
| Telugu | Telugu |
| Kannada | Kannada |
| Gurmukhi | Punjabi |
| Gujarati | Gujarati |
| Odia | Odia |

### Languages Not Covered

The following scheduled Indian languages are not currently supported:

- Urdu (uses Perso-Arabic script)
- Kashmiri (primarily uses Perso-Arabic script)
- Sindhi (uses Perso-Arabic script)
- Santli (uses Ol Chiki script)
- Manipuri (uses Meitei Mayek script)

All supported scripts feature a strict one-to-one mapping between each Indic character and a single Roman character (with diacritics as needed), ensuring perfect reversibility while maintaining phonetic similarity.

## Features

- **Strict one-to-one mapping**: Each Indic character maps to exactly one Roman character (with diacritics as needed)
- **Perfect reversibility**: Guaranteed round-trip conversion without information loss
- **Script detection**: Automatically detects the script of input text
- **Comprehensive coverage**: Supports all characters, including vowels, consonants, matras, and special symbols
- **Easy to use**: Simple API for both script-to-Roman and Roman-to-script conversion

## Installation

```bash
# You can install directly from the provided Python file
pip install iithlp
```

## Usage

### Basic Usage

```python
from iithlp import to_roman, to_script

# Transliterate from an Indian script to Roman
roman_text = to_roman("नमस्ते दुनिया")  # Devanagari
print(roman_text)  # "nmsⁿté dúníyā́"

# Transliterate from Roman to an Indian script
devanagari_text = to_script("nmsⁿté dúníyā́", script="devanagari")
print(devanagari_text)  # "नमस्ते दुनिया"
```

### Script Detection

```python
from iithlp import IITHLP

# Create a transliterator instance
transliterator = IITHLP()

# Detect script of text
text = "ಕನ್ನಡ"
detected_script = transliterator.detect_script(text)
print(detected_script)  # 'kannada'
```

### Getting Supported Scripts

```python
from iithlp import get_supported_scripts

# Get all supported scripts
scripts = get_supported_scripts()
print(scripts)  # ['devanagari', 'bengali', 'tamil', ...]
```

## Mapping Scheme

The mapping scheme follows these principles:

1. **Phonetic similarity**: Similar sounds have similar representations
2. **Diacritics for disambiguation**: Diacritics are used to distinguish between similar sounds
3. **Consistency**: Similar patterns across scripts are represented consistently
4. **Reversibility**: The scheme ensures perfect round-trip conversion

### Example Mappings

#### Vowels (Independent Form)

| Roman | Devanagari | Bengali | Tamil | Malayalam | Telugu | Kannada | Gurmukhi | Gujarati | Odia |
|-------|------------|---------|-------|-----------|--------|---------|----------|----------|------|
| a     | अ          | অ       | அ     | അ         | అ      | ಅ       | ਅ        | અ        | ଅ    |
| ā     | आ          | আ       | ஆ     | ആ         | ఆ      | ಆ       | ਆ        | આ        | ଆ    |
| i     | इ          | ই       | இ     | ഇ         | ఇ      | ಇ       | ਇ        | ઇ        | ଇ    |
| ī     | ई          | ঈ       | ஈ     | ഈ         | ఈ      | ಈ       | ਈ        | ઈ        | ଈ    |
| u     | उ          | উ       | உ     | ഉ         | ఉ      | ಉ       | ਉ        | ઉ        | ଉ    |
| ū     | ऊ          | ঊ       | ஊ     | ഊ         | ఊ      | ಊ       | ਊ        | ઊ        | ଊ    |
| e     | -          | এ       | எ     | എ         | ఎ      | ಎ       | ਏ        | એ        | ଏ    |
| ê     | ए          | ঐ       | ஐ     | ഐ         | ఐ      | ಐ       | ਐ        | ઐ        | ଐ    |
| o     | -          | ও       | ஒ     | ഒ         | ఒ      | ಒ       | ਓ        | ઓ        | ଓ    |
| ô     | ओ          | ঔ       | ஔ     | ഔ         | ఔ      | ಔ       | ਔ        | ઔ        | ଔ    |

#### Consonants (Sample)

| Roman | Devanagari | Bengali | Tamil | Malayalam | Telugu | Kannada | Gurmukhi | Gujarati | Odia |
|-------|------------|---------|-------|-----------|--------|---------|----------|----------|------|
| k     | क          | ক       | க     | ക         | క      | ಕ       | ਕ        | ક        | କ    |
| g     | ग          | গ       | -     | ഗ         | గ      | ಗ       | ਗ        | ગ        | ଗ    |
| c     | च          | চ       | ச     | ച         | చ      | ಚ       | ਚ        | ચ        | ଚ    |
| j     | ज          | জ       | ஜ     | ജ         | జ      | ಜ       | ਜ        | જ        | ଜ    |
| ṭ     | ट          | ট       | ட     | ട         | ట      | ಟ       | ਟ        | ટ        | ଟ    |
| t     | त          | ত       | த     | ത         | త      | ತ       | ਤ        | ત        | ତ    |
| p     | प          | প       | ப     | പ         | ప      | ಪ       | ਪ        | પ        | ପ    |
| m     | म          | ম       | ம     | മ         | మ      | ಮ       | ਮ        | મ        | ମ    |
| y     | य          | য       | ய     | യ         | య      | ಯ       | ਯ        | ય        | ଯ    |
| l     | ल          | ল       | ல     | ല         | ల      | ಲ       | ਲ        | લ        | ଲ    |

## License

MIT License

## Acknowledgements and Ownership

This package is a product of work from the department of Heritage Science and Technology, IIT Hyderabad. 
It provides comprehensive support for 9 major Indian scripts and a strict one-to-one mapping scheme. 
For any concerns please raise an issue on the github repository. You may reach out to the author at ramanan93'at'gmail'dot'com.
