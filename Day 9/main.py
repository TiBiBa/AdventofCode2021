class Valve:

    def __init__(self, height):
        self.height = height
        self.neighbours['up']: None
        self.neighbours['right']: None
        self.neighbours['down']: None
        self.neighbours['left']: None

    def set_neighbours(self, neighbours):
        pass

    def get_neighbours(self):
        return self.neighbours

    def is_lowest_point(self):
        return False

    def get_risk_level(self):
        return self.height + 1