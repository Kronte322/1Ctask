import pygame
import Ui
import Data
import Constants


class App:
    def __init__(self):
        pygame.init()
        self.date = Data.Data()
        self.display = pygame.display.set_mode(Constants.SCREEN_SIZE)
        self.Ui = Ui.Ui(self.date)
        pygame.display.set_caption(Constants.NAME_OF_APP)

    def RunApp(self):
        clock = pygame.time.Clock()
        while True:
            events = pygame.event.get()
            for event in events:
                if event.type == pygame.QUIT:
                    pygame.display.quit()
                self.Ui.ProcessEvents(event)

            time_delta = clock.tick(Constants.TICK_RATE)
            self.Ui.Blit(time_delta, self.display)
            pygame.display.flip()
