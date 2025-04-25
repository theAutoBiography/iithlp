# IITHLP

A comprehensive transliteration scheme for Indian languages with a strict one-to-one character mapping.

## Overview

IITHLP is a Python package that provides a comprehensive transliteration scheme for 9 major Indian scripts covering 21 scheduled Indian languages. It ensures a strict one-to-one mapping between each Indic character and a single Roman character (with diacritics as needed), ensuring perfect reversibility while maintaining phonetic similarity.

## Supported Scripts

The package supports the following 9 scripts:

1. **Devanagari** (Hindi, Marathi, Sanskrit, Nepali, Konkani, Bodo, Maithili, Dogri)
2. **Bengali** (Bengali, Assamese)
3. **Tamil**
4. **Malayalam**
5. **Telugu**
6. **Kannada**
7. **Gurmukhi** (Punjabi)
8. **Gujarati**
9. **Odia**

Note: Urdu is currently not supported in this version.

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
| e     | ए          | এ       | எ     | എ         | ఎ      | ಎ       | ਏ        | એ        | ଏ    |
| ê     | ऐ          | ঐ       | ஐ     | ഐ         | ఐ      | ಐ       | ਐ        | ઐ        | ଐ    |
| o     | ओ          | ও       | ஒ     | ഒ         | ఒ      | ಒ       | ਓ        | ઓ        | ଓ    |
| ô     | औ          | ঔ       | ஔ     | ഔ         | ఔ      | ಔ       | ਔ        | ઔ        | ଔ    |

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

## Acknowledgements

This package is an extension of the original IITHLP package, with comprehensive support for 9 major Indian scripts and a strict one-to-one mapping scheme.
