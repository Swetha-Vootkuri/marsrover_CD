import unittest

from hello_world import initialise_rover, greet
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


    def test_initalise_rover(self):
        generated_text = initialise_rover("1,1,N")
        expected_output_text = "The rover is at X=1, Y=1, facing north. Please enter instructions..."
        self.assertEqual(generated_text, expected_output_text)


if __name__ == "__main__":
    unittest.main()
