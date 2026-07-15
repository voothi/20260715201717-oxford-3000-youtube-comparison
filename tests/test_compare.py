#!/usr/bin/env python3
"""
ZID: 20260715202031
Description: Unit tests for the dictionary comparison script functions.
"""

import sys
import os
import unittest

# Add scripts directory to path
scripts_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "scripts"))
sys.path.insert(0, scripts_dir)

import compare_dicts

class TestCompareDicts(unittest.TestCase):
    
    def test_parse_line_to_words(self):
        parse_fn = compare_dicts.parse_line_to_words
        
        # Test clean single word
        self.assertEqual(parse_fn("abandon"), ["abandon"])
        
        # Test parenthetical removal
        self.assertEqual(parse_fn("bank (river)"), ["bank"])
        self.assertEqual(parse_fn("bear (deal with)"), ["bear"])
        
        # Test comma-split
        self.assertEqual(parse_fn("a, an"), ["a", "an"])
        # Test comma-split
        self.assertEqual(parse_fn("word1 (comment), word2"), ["word", "word"])
        
        # Test slash-split
        self.assertEqual(parse_fn("and/or"), ["and", "or"])
        
        # Test homonym digits removal
        self.assertEqual(parse_fn("close1"), ["close"])
        self.assertEqual(parse_fn("bank2"), ["bank"])
        
        # Test lowercase normalization
        self.assertEqual(parse_fn("Apple"), ["apple"])

    def test_levenshtein_distance(self):
        lev_fn = compare_dicts.LevenshteinDistance
        
        self.assertEqual(lev_fn("cat", "bat"), 1)
        self.assertEqual(lev_fn("analyse", "analyze"), 1)
        self.assertEqual(lev_fn("colour", "color"), 1)
        self.assertEqual(lev_fn("same", "same"), 0)
        self.assertEqual(lev_fn("test", "tst"), 1)

if __name__ == '__main__':
    unittest.main()
