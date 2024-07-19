# tests/test_main.py
import unittest
from src.main import greet

class TestGreetFunction(unittest.TestCase):
    def test_greet(self):
        self.assertEqual(greet("World"), "Hello World!")

if __name__ == "__main__":
    unittest.main()