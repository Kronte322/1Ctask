import Constants
import pygame


class Drawer:
    def __init__(self, display, data):
        self.display = display
        self.data = data
        self.font = pygame.font.Font('OpenSans-Regular.ttf', Constants.LABEL_SIZE)
        self.flag = Constants.FLAG_FOR_ALL
        self.pivot = Constants.CORDS_OF_PIVOT
        self.modes = {Constants.FLAG_FOR_ALL: self.DrawAllMode, Constants.FLAG_FOR_ONE: self.DrawOneMode}
        self.first_timestamp = None
        self.second_timestamp = None
        self.name = None

    def DrawAllMode(self):
        for name in self.data.GetNames():
            if self.data.HasPosition(name):
                pos = (self.data.GetPointPos(name)[0] + self.pivot[0], self.pivot[1] - self.data.GetPointPos(name)[1])
                pos_for_label = (pos[0], pos[1] - Constants.LABEL_SIZE - 1)

                pygame.draw.circle(self.display, color=self.data.GetColor(name), center=pos,
                                   radius=Constants.SIZE_OF_POINT)
                text = self.font.render(name, True, Constants.COLOR_FOR_LABEL)
                text.set_alpha(128)
                textRect = text.get_rect()
                textRect.center = pos_for_label
                self.display.blit(text, textRect)
                pos_for_cords = (pos[0], pos[1] + Constants.LABEL_SIZE)
                text = self.font.render(
                    '(' + str(self.data.GetPointPos(name)[0]) + ', ' + str(self.data.GetPointPos(name)[1]) + ')', True,
                    Constants.COLOR_FOR_LABEL)
                text.set_alpha(128)
                textRect = text.get_rect()
                textRect.center = pos_for_cords
                self.display.blit(text, textRect)

    def DrawOneMode(self):
        if self.data.HasPosition(self.name):
            points = self.data.GetPositionsAndTimestamps(self.name)
            interm = []
            for elem in points:
                if self.first_timestamp <= elem[1] <= self.second_timestamp:
                    interm.append(elem)
            interm.sort(key=lambda x: x[1])

            for i in range(1, len(interm)):
                first_position = (interm[i - 1][0][0] + self.pivot[0], self.pivot[1] - interm[i - 1][0][1])
                second_position = (interm[i][0][0] + self.pivot[0], self.pivot[1] - interm[i][0][1])
                pygame.draw.circle(self.display, color=self.data.GetColor(self.name), center=first_position,
                                   radius=Constants.SIZE_OF_POINT + 3)

                pos_for_cords = (first_position[0], first_position[1] + Constants.LABEL_SIZE)
                text = self.font.render(
                    '(' + str(interm[i - 1][0][0]) + ', ' + str(interm[i - 1][0][1]) + ')', True,
                    Constants.COLOR_FOR_LABEL)
                text.set_alpha(128)
                textRect = text.get_rect()
                textRect.center = pos_for_cords
                self.display.blit(text, textRect)

                pygame.draw.line(self.display, self.data.GetColor(self.name), first_position, second_position,
                                 Constants.SIZE_OF_POINT)

    def Draw(self):
        self.modes[self.flag]()

    def SwitchToOne(self, name, first_timestamp, second_timestamp):
        self.name = name
        self.first_timestamp = first_timestamp
        self.second_timestamp = second_timestamp
        self.flag = Constants.FLAG_FOR_ONE

    def SwitchToAll(self):
        self.flag = Constants.FLAG_FOR_ALL
