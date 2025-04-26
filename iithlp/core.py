"""
IITHLP - Indian Institute of Technology Hyderabad Language Processing
Version 0.2.2

A comprehensive transliteration scheme for Indian languages with a strict one-to-one character mapping.
"""

import os
import json
import re
from typing import Dict, List, Tuple, Optional, Union

class IITHLP:
    """
    A class for transliterating between Indian scripts and Roman characters using a strict
    one-to-one mapping scheme.
    """
    
    def __init__(self, script: str = None):
        """
        Initialize the transliterator with mappings for all supported scripts.
        
        Args:
            script: The default script to use for Roman to script conversion.
                   If None, will try to detect from context.
        """
        self.script = script
        self.mappings = {}
        self.reverse_mappings = {}
        self.script_patterns = {}
        
        # Load mappings for all supported scripts
        self._load_mappings()
        
        # Create reverse mappings for Roman to script conversion
        self._create_reverse_mappings()
        
        # Compile regex patterns for script detection
        self._compile_script_patterns()
    
    def _load_mappings(self):
        """Load character mappings for all supported scripts from JSON files."""
        # Define the base directory for mapping files
        base_dir = os.path.dirname(os.path.abspath(__file__))
        mappings_dir = os.path.join(base_dir, 'data', 'mappings')
        
        # List of supported scripts
        scripts = [
            'devanagari', 'bengali', 'tamil', 'malayalam', 'telugu',
            'kannada', 'gurmukhi', 'gujarati', 'odia'
        ]
        
        # Load each mapping file
        for script in scripts:
            mapping_file = os.path.join(mappings_dir, f'{script}.json')
            try:
                with open(mapping_file, 'r', encoding='utf-8') as f:
                    self.mappings[script] = json.load(f)
            except FileNotFoundError:
                print(f"Warning: Mapping file for {script} not found at {mapping_file}")
                self.mappings[script] = {}
            except json.JSONDecodeError:
                print(f"Warning: Error decoding JSON from {mapping_file}")
                self.mappings[script] = {}
    
    def _create_reverse_mappings(self):
        """Create reverse mappings for Roman to script conversion."""
        for script, mapping in self.mappings.items():
            self.reverse_mappings[script] = {v: k for k, v in mapping.items()}
    
    def _compile_script_patterns(self):
        """Compile regex patterns for script detection."""
        for script, mapping in self.mappings.items():
            # Create a pattern that matches any character in the script
            pattern = '|'.join(re.escape(char) for char in mapping.keys())
            self.script_patterns[script] = re.compile(f'[{pattern}]')
    
    def detect_script(self, text: str) -> Optional[str]:
        """
        Detect the script of the given text.
        
        Args:
            text: The text to detect the script of.
            
        Returns:
            The detected script, or None if no script could be detected.
        """
        script_counts = {}
        
        # Count characters from each script
        for script, pattern in self.script_patterns.items():
            script_counts[script] = len(pattern.findall(text))
        
        # Return the script with the most characters
        if not script_counts:
            return None
        
        max_script = max(script_counts.items(), key=lambda x: x[1])
        return max_script[0] if max_script[1] > 0 else None
    
    def transliterate_to_roman(self, text: str) -> str:
        """
        Transliterate text from an Indian script to Roman characters.
        
        Args:
            text: The text to transliterate.
            
        Returns:
            The transliterated text.
        """
        # Detect the script if not specified
        script = self.detect_script(text)
        if not script:
            return text
        
        # Get the mapping for the detected script
        mapping = self.mappings.get(script, {})
        if not mapping:
            return text
        
        # Sort the keys by length in descending order to handle multi-character sequences
        sorted_keys = sorted(mapping.keys(), key=len, reverse=True)
        
        # Replace each character with its Roman equivalent
        result = text
        for key in sorted_keys:
            result = result.replace(key, mapping[key])
        
        return result
    
    def transliterate_to_script(self, text: str, script: str = None) -> str:
        """
        Transliterate text from Roman characters to an Indian script.
        
        Args:
            text: The text to transliterate.
            script: The target script. If None, uses the default script.
            
        Returns:
            The transliterated text.
        """
        # Use the specified script or the default script
        target_script = script or self.script
        if not target_script:
            raise ValueError("No target script specified. Please specify a script or set a default script.")
        
        # Get the reverse mapping for the target script
        reverse_mapping = self.reverse_mappings.get(target_script, {})
        if not reverse_mapping:
            return text
        
        # Sort the keys by length in descending order to handle multi-character sequences
        sorted_keys = sorted(reverse_mapping.keys(), key=len, reverse=True)
        
        # Replace each Roman character with its script equivalent
        result = text
        for key in sorted_keys:
            result = result.replace(key, reverse_mapping[key])
        
        return result

# Create a default instance for easy import
transliterator = IITHLP()

# Convenience functions
def to_roman(text: str) -> str:
    """Transliterate text from an Indian script to Roman characters."""
    return transliterator.transliterate_to_roman(text)

def to_script(text: str, script: str = None) -> str:
    """Transliterate text from Roman characters to an Indian script."""
    return transliterator.transliterate_to_script(text, script)

def get_supported_scripts() -> List[str]:
    """Get a list of all supported scripts."""
    return list(transliterator.mappings.keys())

def get_script_info() -> Dict[str, Dict[str, str]]:
    """Get information about all supported scripts."""
    script_info = {
        'devanagari': {
            'languages': 'Hindi, Marathi, Sanskrit, Nepali, Konkani, Bodo, Maithili, Dogri',
            'region': 'Northern India',
            'unicode_block': 'U+0900–U+097F'
        },
        'bengali': {
            'languages': 'Bengali, Assamese',
            'region': 'Eastern India, Bangladesh',
            'unicode_block': 'U+0980–U+09FF'
        },
        'tamil': {
            'languages': 'Tamil',
            'region': 'Southern India, Sri Lanka, Singapore',
            'unicode_block': 'U+0B80–U+0BFF'
        },
        'malayalam': {
            'languages': 'Malayalam',
            'region': 'Kerala, India',
            'unicode_block': 'U+0D00–U+0D7F'
        },
        'telugu': {
            'languages': 'Telugu',
            'region': 'Andhra Pradesh, Telangana, India',
            'unicode_block': 'U+0C00–U+0C7F'
        },
        'kannada': {
            'languages': 'Kannada',
            'region': 'Karnataka, India',
            'unicode_block': 'U+0C80–U+0CFF'
        },
        'gurmukhi': {
            'languages': 'Punjabi',
            'region': 'Punjab, India',
            'unicode_block': 'U+0A00–U+0A7F'
        },
        'gujarati': {
            'languages': 'Gujarati',
            'region': 'Gujarat, India',
            'unicode_block': 'U+0A80–U+0AFF'
        },
        'odia': {
            'languages': 'Odia',
            'region': 'Odisha, India',
            'unicode_block': 'U+0B00–U+0B7F'
        }
    }
    return script_info

# Example usage
if __name__ == "__main__":
    # Create a transliterator instance
    transliterator = IITHLP()
    
    # Test with different scripts
    texts = {
        "Hindi (Devanagari)": "नमस्ते दुनिया",
        "Bengali": "নমস্কার বিশ্ব",
        "Tamil": "வணக்கம் உலகம்",
        "Malayalam": "ഹലോ ലോകം",
        "Telugu": "హలో ప్రపంచం",
        "Kannada": "ಹಲೋ ವರ್ಲ್ಡ್",
        "Punjabi (Gurmukhi)": "ਸਤਿ ਸ੍ਰੀ ਅਕਾਲ",
        "Gujarati": "નમસ્તે વિશ્વ",
        "Odia": "ନମସ୍କାର ବିଶ୍ୱ"
    }
    
    print("Script Detection and Transliteration Test:")
    print("----------------------------------------")
    
    for language, text in texts.items():
        # Detect script
        script = transliterator.detect_script(text)
        
        # Transliterate to Roman
        roman = transliterator.transliterate_to_roman(text)
        
        # Transliterate back to original script
        back_to_script = transliterator.transliterate_to_script(roman, script=script)
        
        # Check if round-trip conversion is successful
        success = text == back_to_script
        
        print(f"{language}:")
        print(f"  Original: {text}")
        print(f"  Detected script: {script}")
        print(f"  Roman: {roman}")
        print(f"  Back to script: {back_to_script}")
        print(f"  Round-trip success: {success}")
        print()
