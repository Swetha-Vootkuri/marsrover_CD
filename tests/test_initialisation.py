import unittest

from hello_world import greet
from rover import Rover


class InitialisationTests(unittest.TestCase):
    def test_greeting(self):
        generated_text = greet()
        expected_text = "Please enter initial X, Y coordinates and direction for rover"
        self.assertEqual(generated_text, expected_text)

    def test_parse_user_input(self):
        rover = Rover()
        rover.initialise("1,1,N")
        (x, y) = rover.get_x_y()
        direction = rover.get_direction()
        self.assertEqual(x, 1)
        self.assertEqual(y, 1)
        self.assertEqual(direction, "N")


if __name__ == "__main__":
    unittest.main()
