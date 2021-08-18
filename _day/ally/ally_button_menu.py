import pygame
import os
from all_image import *
from _day.level_setting import level_setting


class Button:
    def __init__(self, image, name, x, y, virus_image, key_object):
        self.name = name    # name of the button
        self.image = image  # image of the button
        self.virus_image = virus_image
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)  # center of the menu image
        self.key_object = key_object

    def clicked(self, x, y):
        """
        Return Whether the button is clicked
        :return: bool
        """
        return True if self.rect.collidepoint(x, y) else False

    def pressed(self, key_request):
        return True if key_request == self.key_object else False

    @property
    def response(self):
        return self.name


button_list = (lambda y: [
    Button(NORMAL_CAT_BUTTON, "normal", y, 600, BLUE_VIRUS_IMAGE_S, "g"),
    Button(MASK_CAT_BUTTON, "mask", y+200, 600, BLACK_VIRUS_IMAGE_S, "h"),
    Button(SANI_CAT_BUTTON, "sanitizer", y+400, 600, YELLOW_VIRUS_IMAGE_S, "j"),
    Button(ALCOHOL_CAT_BUTTON, "alcohol", y+600, 600, ORANGE_VIRUS_IMAGE_S, "k"),
    Button(VACCINE_CAT_BUTTON, "vaccine", y+800, 600, RED_VIRUS_IMAGE_S, "l")
])


class Button_menu:
    """
    Set on the button of the game screen. Let player choose the cat to fight virus.
    """
    def __init__(self, level):
        self.but_num = level_setting[level]['button_num']
        y_pos = 300-100*(self.but_num-4)
        self.__buttons = button_list(y_pos)[:self.but_num]
        self.__buttons.append(Button(PAUSE_BTN_IMAGE, "pause game", 50, 50, None, None))

    def get_buttons(self):
        return self.__buttons


class Pause_menu:
    """
    Set on the button of the game screen. Let player choose the cat to fight virus.
    """
    def __init__(self):
        self.__buttons = [Button(CONTINUE_BTN_IMAGE, "continue game", 600, 250, None, None),
                          Button(BACK_BTN, "force end", 600, 400, None, None),
                          Button(PLAY_BTN, 'play music', 550, 500, None, None),
                          Button(MUTE_BTN, 'pause music', 650, 500, None, None)]

    def get_buttons(self):
        return self.__buttons


class User_guide_menu:
    """
    Display the game introduction / guide before the game starts.
    """
    def __init__(self):
        self.__buttons = [Button(NAVIGATION_PREV_BUTTON, "navigation_prev", 100, 650, None, None),
                          Button(NAVIGATION_NEXT_BUTTON, "navigation_next", 1100, 650, None, None)]

    def get_buttons(self):
        return self.__buttons

