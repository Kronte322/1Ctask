import pygame_gui
import pygame
import Constants


class Ui:
    def __init__(self, data):
        self.data = data
        self.manager = pygame_gui.UIManager(Constants.SCREEN_SIZE)
        self.add_button = pygame_gui.elements.UIButton(
            relative_rect=pygame.Rect(Constants.ADD_CHAR_BUTTON_PLACE, Constants.ADD_CHAR_BUTTON_SIZE),
            text="Add new character",
            manager=self.manager)
        self.text_box_for_name = pygame_gui.elements.ui_text_entry_line.UITextEntryLine(relative_rect=pygame.Rect(Constants.CHAR_NAME_PLACE, Constants.CHAR_NAME_SIZE), manager=self.manager)
        self.dropdown = pygame_gui.elements.ui_drop_down_menu.UIDropDownMenu(
            options_list=self.data.GetNames(),
            starting_option=self.data.GetNames()[0],
            relative_rect=pygame.Rect(Constants.CHOOSE_CHARACTER_PLACE, Constants.CHOOSE_CHARACTER_SIZE),
            manager=self.manager
        )
        self.add_cord_button = pygame_gui.elements.UIButton(
            relative_rect=pygame.Rect(Constants.ADD_CORDS_BUTTON_PLACE, Constants.ADD_CORDS_BUTTON_SIZE),
            text="Add New Coord",
            manager=self.manager)
        self.text_box_for_first_coord = pygame_gui.elements.ui_text_entry_line.UITextEntryLine(relative_rect=pygame.Rect(Constants.FIRST_COORD_ENTRY_PLACE, Constants.FIRST_COORD_ENTRY_SIZE), manager=self.manager)
        self.text_box_for_second_coord = pygame_gui.elements.ui_text_entry_line.UITextEntryLine(relative_rect=pygame.Rect(Constants.SECOND_COORD_ENTRY_PLACE, Constants.SECOND_COORD_ENTRY_SIZE), manager=self.manager)

    def ProcessEvents(self, event):
        if event.type == pygame_gui.UI_BUTTON_PRESSED:
            if event.ui_element == self.add_button:
                name = self.text_box_for_name.text
                self.data.AddChar(name)
                self.text_box_for_name.clear()
                self.dropdown.add_options([name])
            if event.ui_element == self.add_cord_button:
                name = self.dropdown.selected_option
                first_coord = self.text_box_for_first_coord.text
                second_coord = self.text_box_for_second_coord.text
                self.text_box_for_first_coord.clear()
                self.text_box_for_second_coord.clear()
                self.data.AddPoint(name, (first_coord, second_coord))
        self.manager.process_events(event)

    def Blit(self, time_delta, screen):
        self.manager.update(time_delta)
        self.manager.draw_ui(screen)
