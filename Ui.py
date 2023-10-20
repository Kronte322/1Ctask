import pygame_gui
import pygame
import Constants
import datetime


class Ui:
    def __init__(self, data):
        self.data = data
        self.manager = pygame_gui.UIManager(Constants.SCREEN_SIZE)
        self.add_button = pygame_gui.elements.UIButton(
            relative_rect=pygame.Rect(Constants.ADD_CHAR_BUTTON_PLACE, Constants.ADD_CHAR_BUTTON_SIZE),
            text="Add new character",
            manager=self.manager)
        self.text_box_for_name = pygame_gui.elements.ui_text_entry_line.UITextEntryLine(
            relative_rect=pygame.Rect(Constants.CHAR_NAME_PLACE, Constants.CHAR_NAME_SIZE), manager=self.manager)
        self.dropdown = pygame_gui.elements.ui_drop_down_menu.UIDropDownMenu(
            options_list=["None"],
            starting_option="None",
            relative_rect=pygame.Rect(Constants.CHOOSE_CHARACTER_PLACE, Constants.CHOOSE_CHARACTER_SIZE),
            manager=self.manager
        )
        self.add_cord_button = pygame_gui.elements.UIButton(
            relative_rect=pygame.Rect(Constants.ADD_CORDS_BUTTON_PLACE, Constants.ADD_CORDS_BUTTON_SIZE),
            text="Add New Coord",
            manager=self.manager)
        self.text_box_for_first_coord = pygame_gui.elements.ui_text_entry_line.UITextEntryLine(
            relative_rect=pygame.Rect(Constants.FIRST_COORD_ENTRY_PLACE, Constants.FIRST_COORD_ENTRY_SIZE),
            manager=self.manager)
        self.text_box_for_second_coord = pygame_gui.elements.ui_text_entry_line.UITextEntryLine(
            relative_rect=pygame.Rect(Constants.SECOND_COORD_ENTRY_PLACE, Constants.SECOND_COORD_ENTRY_SIZE),
            manager=self.manager)
        self.text_box_for_time_stamp = pygame_gui.elements.ui_text_entry_line.UITextEntryLine(
            relative_rect=pygame.Rect(Constants.TIMESTAMP_ENTRY_PLACE, Constants.TIMESTAMP_ENTRY_SIZE),
            manager=self.manager)
        self.switch_to_all = pygame_gui.elements.UIButton(
            relative_rect=pygame.Rect(Constants.SWITCH_TO_ALL_PLACE, Constants.SWITCH_TO_ALL_SIZE),
            text="Show all",
            manager=self.manager)
        self.switch_to_one = pygame_gui.elements.UIButton(
            relative_rect=pygame.Rect(Constants.SWITCH_TO_ONE_PLACE, Constants.SWITCH_TO_ONE_SIZE),
            text="Show one",
            manager=self.manager)
        self.text_box_for_first_time_stamp = pygame_gui.elements.ui_text_entry_line.UITextEntryLine(
            relative_rect=pygame.Rect(Constants.FIRST_TIMESTAMP_PLACE, Constants.TIMESTAMP_ENTRY_SIZE),
            manager=self.manager)
        self.text_box_for_second_time_stamp = pygame_gui.elements.ui_text_entry_line.UITextEntryLine(
            relative_rect=pygame.Rect(Constants.SECOND_TIMESTAMP_PLACE, Constants.TIMESTAMP_ENTRY_SIZE),
            manager=self.manager)
        self.delete_button = pygame_gui.elements.UIButton(
            relative_rect=pygame.Rect(Constants.DELETE_BUTTON_PLACE, Constants.ADD_CHAR_BUTTON_SIZE),
            text="Delete character",
            manager=self.manager)

    def ProcessEvents(self, event, drawer):
        if event.type == pygame_gui.UI_BUTTON_PRESSED:
            if event.ui_element == self.add_button:
                name = self.text_box_for_name.text
                self.data.AddChar(name)
                self.text_box_for_name.clear()
                self.dropdown.add_options([name])
            if event.ui_element == self.add_cord_button:
                try:
                    name = self.dropdown.selected_option
                    first_coord = int(self.text_box_for_first_coord.text)
                    second_coord = int(self.text_box_for_second_coord.text)
                    timestamp = datetime.datetime.strptime(self.text_box_for_time_stamp.text, Constants.DATE_FORMAT)
                    self.text_box_for_first_coord.clear()
                    self.text_box_for_second_coord.clear()
                    self.text_box_for_time_stamp.clear()
                    self.data.AddPoint(name, (first_coord, second_coord), timestamp)
                except:
                    self.text_box_for_time_stamp.set_text("Wrong Input!")
            if event.ui_element == self.delete_button:
                name = self.text_box_for_name.text
                self.data.DeleteChar(name)
            if event.ui_element == self.switch_to_all:
                drawer.SwitchToAll()
            if event.ui_element == self.switch_to_one:
                try:
                    first_timestamp = datetime.datetime.strptime(self.text_box_for_first_time_stamp.text,
                                                                 Constants.DATE_FORMAT)
                    second_timestamp = datetime.datetime.strptime(self.text_box_for_second_time_stamp.text,
                                                                  Constants.DATE_FORMAT)
                    drawer.SwitchToOne(self.dropdown.selected_option, first_timestamp, second_timestamp)
                except:
                    self.text_box_for_second_time_stamp.set_text("Wrong Input!")
                    self.text_box_for_first_time_stamp.set_text("Wrong Input!")
        self.manager.process_events(event)

    def Blit(self, time_delta, screen):
        self.manager.update(time_delta)
        self.manager.draw_ui(screen)
