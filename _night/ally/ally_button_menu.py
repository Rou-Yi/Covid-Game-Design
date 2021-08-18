import pygame
from _night.level_setting import level_setting
from button import Button
from all_image import *


class Button_menu:
    """
    Set on the button of the game screen. Let player choose the cat to fight virus.
    """
    def __init__(self, level):
        self.__buttons = level_setting[level]['cats_but']
        self.__buttons.append(Button(PAUSE_BTN_IMAGE, "pause game", 50, 50))

    def get_buttons(self):
        return self.__buttons


class Pause_menu:
    """
    Let user can pause game or back to the menu when playing.
    """
    def __init__(self):
        self.__buttons = [Button(CONTINUE_BTN_IMAGE, "continue game", 600, 250),
                          Button(BACK_BTN, "force end", 600, 400),
                          Button(PLAY_BTN, 'play music', 550, 500),
                          Button(MUTE_BTN, 'pause music', 650, 500)]

    def get_buttons(self):
        return self.__buttons


class User_guide_menu:
    """
    Display the game introduction / guide before the game starts.
    """
    def __init__(self):
        self.__buttons = [Button(NAVIGATION_PREV_BUTTON, "navigation_prev", 100, 650),
                          Button(NAVIGATION_NEXT_BUTTON, "navigation_next", 1100, 650)]

    def get_buttons(self):
        return self.__buttons

