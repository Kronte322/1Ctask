import random


class Data:
    def __init__(self):
        self.characters = {}
        self.colors = {}

    def AddChar(self, name):
        self.characters[name] = []
        first_color = random.randint(1, 255)
        second_color = random.randint(1, 255 - first_color)
        third_color = random.randint(1, 255 - first_color - second_color)
        self.colors[name] = (first_color, second_color, third_color)

    def AddPoint(self, name, point, timestamp):
        self.characters[name].append([point, timestamp])

    def GetNames(self):
        return list(self.characters.keys())

    def GetValues(self):
        return list(self.characters.values())

    def GetColor(self, char):
        return self.colors[char]

    def GetPositionsAndTimestamps(self, char):
        return self.characters[char]

    def GetPointPos(self, char):
        return self.characters[char][len(self.characters[char]) - 1][0]

    def HasPosition(self, char):
        return len(self.characters[char]) > 0

    def DeleteChar(self, char):
        if char in self.characters:
            self.characters.pop(char)
            self.colors.pop(char)
