import unittest

from hello_world import greet


class InitialisationTests(unittest.TestCase):
    def test_greeting(self):
        generated_text = greet()
        expected_text = "Please enter initial X, Y coordinates and direction for rover"
        self.assertEqual(generated_text, expected_text)


if __name__ == "__main__":
    unittest.main()
