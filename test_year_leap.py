import unittest
from main import is_year_leap

class test_is_year_leap(unittest.TestCase):
    def test_leap(self):
        self.assertEqual(is_year_leap(2024), 2024 % 4 == 0 and 2024 % 100 != 0 or 2024 % 400 == 0)
        self.assertEqual(is_year_leap(2022), 2022 % 4 == 0 and 2022 % 100 != 0 or 2022 % 400 == 0)