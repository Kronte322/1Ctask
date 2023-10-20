import random

class Data:
    def __init__(self):
        self.characters = {"None": []}
        self.colors = {}

    def AddChar(self, name):
        self.characters[name] = []
        first_color = random.randint(1, 255)
        second_color = random.randint(1, 255 - first_color)
        third_color = random.randint(1, 255 - first_color - second_color)
        self.colors[name] = (first_color, second_color, third_color)

    def AddPoint(self, name, point):
        self.characters[name].append(point)

    def GetNames(self):
        return list(self.characters.keys())
