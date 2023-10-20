import pygame

import Constants

class MouseEvents:
    def __init__(self):
        self.prev_dist = None

    def PrecessEvents(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            self.prev_dist = pygame.mouse.get_pos()
            self.pressed = True
        if event.type == pygame.MOUSEBUTTONUP:
            mouse_position = pygame.mouse.get_pos()
            Constants.CORDS_OF_PIVOT[0] -= (mouse_position[0] - self.prev_dist[0])
            Constants.CORDS_OF_PIVOT[1] -= (mouse_position[1] - self.prev_dist[1])
