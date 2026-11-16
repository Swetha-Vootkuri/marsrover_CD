class Rover:
    def __init__(self):
        pass

    def initialise(self, prompt: str):
        result = prompt.split(",", 2)
        self.x = int(result[0])
        self.y = int(result[1])
        self.direction = result[2]

    def get_x_y(self):
        return (self.x, self.y)

    def get_direction(self):
        return self.direction
