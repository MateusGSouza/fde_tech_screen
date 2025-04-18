import unittest
from main import *

class TestPackageSorter(unittest.TestCase):
    def test_standard_package(self):
        """Test packages that are neither bulky nor heavy (dimensions in cm, mass in kg)."""
        # Small dimensions, light mass
        self.assertEqual(sort(50, 50, 50, 10), "STANDARD")
        # Small volume, small dimensions
        self.assertEqual(sort(100, 100, 99, 15), "STANDARD")  # Volume = 990,000 cm³
        # Just below volume threshold
        self.assertEqual(sort(100, 100, 99.99, 19.9), "STANDARD")  # Volume = 999,900 cm³

    def test_special_bulky_only(self):
        """Test packages that are bulky but not heavy (dimensions in cm, mass in kg)."""
        # Bulky due to volume >= 1,000,000 cm³
        self.assertEqual(sort(100, 100, 100, 10), "SPECIAL")  # Volume = 1,000,000 cm³
        # Bulky due to volume (corrected test case)
        self.assertEqual(sort(149, 149, 149, 19.9), "SPECIAL")  # Volume = 3,307,949 cm³
        # Bulky due to one dimension >= 150 cm
        self.assertEqual(sort(150, 50, 50, 10), "SPECIAL")
        self.assertEqual(sort(50, 151, 50, 15), "SPECIAL")
        self.assertEqual(sort(50, 50, 152, 19.9), "SPECIAL")

    def test_special_heavy_only(self):
        """Test packages that are heavy but not bulky (dimensions in cm, mass in kg)."""
        # Heavy due to mass >= 20 kg
        self.assertEqual(sort(50, 50, 50, 20), "SPECIAL")
        self.assertEqual(sort(100, 100, 99, 25), "SPECIAL")  # Volume = 990,000 cm³
        # Just below bulky thresholds, heavy
        self.assertEqual(sort(100, 100, 99.99, 20), "SPECIAL")  # Volume = 999,900 cm³

    def test_rejected_package(self):
        """Test packages that are both bulky and heavy (dimensions in cm, mass in kg)."""
        # Bulky (volume) and heavy
        self.assertEqual(sort(100, 100, 100, 20), "REJECTED")  # Volume = 1,000,000 cm³
        # Bulky (dimension) and heavy
        self.assertEqual(sort(150, 50, 50, 25), "REJECTED")
        # Just at thresholds
        self.assertEqual(sort(150, 149, 149, 20), "REJECTED")  # Dimension = 150 cm

    def test_edge_cases(self):
        """Test edge cases for dimensions (cm) and mass (kg)."""
        # Exactly at volume threshold, not heavy
        self.assertEqual(sort(100, 100, 100, 19.9), "SPECIAL")  # Volume = 1,000,000 cm³
        # Exactly at dimension threshold, not heavy
        self.assertEqual(sort(150, 149, 149, 19.9), "SPECIAL")  # Dimension = 150 cm
        # Exactly at mass threshold, not bulky
        self.assertEqual(sort(99, 99, 99, 20), "SPECIAL")  # Volume = 970,299 cm³
        # Exactly at both thresholds
        self.assertEqual(sort(150, 149, 149, 20), "REJECTED")  # Dimension = 150 cm, mass = 20 kg
        # Input as strings
        self.assertEqual(sort("150", "149", "149", "20"), "REJECTED")


    def test_invalid_inputs(self):
        """Test input validation for negative dimensions or mass."""
        with self.assertRaises(ValueError):
            sort(-1, 50, 50, 10)  # Negative width
        with self.assertRaises(ValueError):
            sort(50, -50, 50, 10)  # Negative height
        with self.assertRaises(ValueError):
            sort(50, 50, -50, 10)  # Negative length
        with self.assertRaises(ValueError):
            sort(50, 50, 50, -10)  # Negative mass
        with self.assertRaises(ValueError):
            sort(-150, -150, -150, -20)  # All negative
        with self.assertRaises(TypeError):
            sort("Hello", "", None, 0)  # Wrong types input

if __name__ == "__main__":
    unittest.main()