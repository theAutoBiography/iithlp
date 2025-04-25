import unittest
import os
import sys

# Add the parent directory to the path so we can import the package
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from iithlp import IITHLP, to_roman, to_script, get_supported_scripts

class TestIITHLP(unittest.TestCase):
    """Test cases for the IITHLP class."""
    
    def setUp(self):
        """Set up test fixtures."""
        self.transliterator = IITHLP()
        self.test_texts = {
            "devanagari": "नमस्ते दुनिया",
            "bengali": "নমস্কার বিশ্ব",
            "tamil": "வணக்கம் உலகம்",
            "malayalam": "ഹലോ ലോകം",
            "telugu": "హలో ప్రపంచం",
            "kannada": "ಹಲೋ ವರ್ಲ್ಡ್",
            "gurmukhi": "ਸਤਿ ਸ੍ਰੀ ਅਕਾਲ",
            "gujarati": "નમસ્તે વિશ્વ",
            "odia": "ନମସ୍କାର ବିଶ୍ୱ"
        }
    
    def test_script_detection(self):
        """Test script detection for all supported scripts."""
        for script, text in self.test_texts.items():
            detected_script = self.transliterator.detect_script(text)
            self.assertEqual(detected_script, script, f"Failed to detect {script} script")
    
    def test_to_roman(self):
        """Test transliteration to Roman for all supported scripts."""
        for script, text in self.test_texts.items():
            roman = self.transliterator.transliterate_to_roman(text)
            self.assertIsNotNone(roman, f"Failed to transliterate {script} to Roman")
            self.assertNotEqual(roman, "", f"Empty result for {script} to Roman")
    
    def test_to_script(self):
        """Test transliteration from Roman to script for all supported scripts."""
        for script, text in self.test_texts.items():
            roman = self.transliterator.transliterate_to_roman(text)
            back_to_script = self.transliterator.transliterate_to_script(roman, script=script)
            self.assertEqual(back_to_script, text, f"Round-trip conversion failed for {script}")
    
    def test_convenience_functions(self):
        """Test the convenience functions."""
        for script, text in self.test_texts.items():
            # Test to_roman function
            roman = to_roman(text)
            self.assertIsNotNone(roman, f"to_roman failed for {script}")
            
            # Test to_script function
            back_to_script = to_script(roman, script=script)
            self.assertEqual(back_to_script, text, f"to_script failed for {script}")
    
    def test_get_supported_scripts(self):
        """Test the get_supported_scripts function."""
        scripts = get_supported_scripts()
        self.assertIsInstance(scripts, list, "get_supported_scripts should return a list")
        self.assertGreaterEqual(len(scripts), 9, "Should support at least 9 scripts")
        
        # Check that all expected scripts are in the list
        expected_scripts = ["devanagari", "bengali", "tamil", "malayalam", "telugu", 
                           "kannada", "gurmukhi", "gujarati", "odia"]
        for script in expected_scripts:
            self.assertIn(script, scripts, f"{script} should be in supported scripts")

if __name__ == '__main__':
    unittest.main()
