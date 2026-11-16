import unittest

from hello_world import greet


class HelloWorldTests(unittest.TestCase):
    def test_default_greeting(self):
        self.assertEqual(greet(), "Hello, World!")

    def test_custom_greeting(self):
        self.assertEqual(greet("Mars"), "Hello, Mars!")


if __name__ == "__main__":
    unittest.main()
