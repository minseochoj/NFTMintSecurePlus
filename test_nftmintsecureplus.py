# test_nftmintsecureplus.py
"""
Tests for NFTMintSecurePlus module.
"""

import unittest
from nftmintsecureplus import NFTMintSecurePlus

class TestNFTMintSecurePlus(unittest.TestCase):
    """Test cases for NFTMintSecurePlus class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = NFTMintSecurePlus()
        self.assertIsInstance(instance, NFTMintSecurePlus)
        
    def test_run_method(self):
        """Test the run method."""
        instance = NFTMintSecurePlus()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
