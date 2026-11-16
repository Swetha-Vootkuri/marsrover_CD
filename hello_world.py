"""Minimal walking skeleton for a Hello World project."""

from rover import Rover

rover = Rover()

def initialise_rover(input):
    rover.initialise(input)
    (x,y) = rover.get_x_y()
    direction = rover.get_direction()
    direction_string_mapping = {"N": "north"}
    return f"The rover is at X={x}, Y={y}, facing {direction_string_mapping[direction]}. Please enter instructions..."

def greet() -> str:
    """Return a greeting which also serves as instructions for initialisation"""
    return f"Please enter initial X, Y coordinates and direction for rover"


def main() -> None:
    """Run the app entry point."""
    user_input =input(greet())
    print(initialise_rover(user_input))



if __name__ == "__main__":
    main()
