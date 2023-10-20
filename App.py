import pygame
import Ui
import Data
import Constants
import Drawer
import pickle


class App:
    def __init__(self):
        pygame.init()
        self.data = Data.Data()
        with open(Constants.PATH_TO_SAVE_CHARS, 'rb') as file:
            self.data = pickle.load(file)
        self.display = pygame.display.set_mode(Constants.SCREEN_SIZE)
        self.display.fill(Constants.BACK_GROUND_COLOR)
        self.Ui = Ui.Ui(self.data)
        self.drawer = Drawer.Drawer(self.display, self.data)
        pygame.display.set_caption(Constants.NAME_OF_APP)

    def RunApp(self):
        clock = pygame.time.Clock()
        while True:
            events = pygame.event.get()
            for event in events:
                if event.type == pygame.QUIT:
                    with open(Constants.PATH_TO_SAVE_CHARS, 'wb') as file:
                        pickle.dump(self.data, file, protocol=pickle.HIGHEST_PROTOCOL)
                    pygame.display.quit()
                self.Ui.ProcessEvents(event, self.drawer)
            self.display.fill(Constants.BACK_GROUND_COLOR)
            time_delta = clock.tick(Constants.TICK_RATE)
            self.Ui.Blit(time_delta, self.display)
            self.drawer.Draw()
            pygame.display.update()
