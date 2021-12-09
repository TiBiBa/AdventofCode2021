class Valve:

    neighbours = {}

    def __init__(self):
        self.neighbours['up']: None
        self.neighbours['right']: None
        self.neighbours['down']: None
        self.neighbours['left']: None

    def set_neighbours(self, neighbours):
        pass

    def is_lowest_point(self):
        return False