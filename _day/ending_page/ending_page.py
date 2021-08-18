import pygame
from button import Button
from all_image import *


class Ending_page:
    """
    Construct the menu for the ending of a level.
    """
    def __init__(self, image, button_list):
        self.image = image
        self.__buttons = button_list
        self.response = 'main menu day'
        self.jump_page = False

    def draw(self, win):
        """
        Draw buttons on a transparent surface.
        :return: None
        """
        surface = pygame.Surface((WIN_WIDTH, WIN_HEIGHT), pygame.SRCALPHA)
        pygame.draw.rect(surface, (255, 255, 255, 170), [0, 0, WIN_WIDTH, WIN_HEIGHT], 0)
        surface.blit(self.image, (200, 120))
        for but in self.__buttons:
            surface.blit(but.image, but.rect)
        win.blit(surface, (0, 0))

    def update(self, events: dict):
        """
        Update for quit event and click button.
        :return: None
        """
        if events["mouse position"] is not None:
            x, y = events["mouse position"]
            for btn in self.__buttons:
                if btn.clicked(x, y):
                    self.response = btn.response
                    self.jump_page = True

    @classmethod
    def Win(cls):  # 主頁面
        btn_list = [Button(BACK_BTN, "main menu day", 600, 550)]
        winning = cls(WIN_IMAGE, btn_list)
        return winning

    @classmethod
    def Loss(cls):  # 主頁面
        btn_list = [Button(BACK_BTN, "main menu day", 600, 550)]
        loss = cls(LOSE_IMAGE, btn_list)
        return loss
