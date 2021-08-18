import pygame
import os
import math
from settings import TOWER_WIDTH, TOWER_HEIGHT, TOWER_X, TOWER_Y, WIN_WIDTH
from color_settings import *
from all_image import *


class Tower:
    """守衛最終的塔，用繼承寫敵我雙方的塔"""
    def __init__(self, image, x, y, health):
        self.image = image  # image of the tower
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)  # center of the tower
        self.health = health
        self.max_health = health
        self.x = x
        self.y = y

    def draw(self, win):
        """
        Draw the tower
        :param win:
        :return:
        """
        # draw tower
        win.blit(self.image, self.rect)
        # draw health bar
        bar_width = self.rect.w * (self.health / self.max_health)
        max_bar_width = self.rect.w
        bar_height = 8
        pygame.draw.rect(win, RED, [self.rect.x, self.rect.y - 10, max_bar_width, bar_height])
        pygame.draw.rect(win, GREEN, [self.rect.x, self.rect.y - 10, bar_width, bar_height])

    # 用繼承寫出敵我雙方的塔
    @classmethod
    def Player_tower(cls):
        player_tower = cls(TOWER_IMG_PL, TOWER_X, TOWER_Y, 500)
        return player_tower

    @classmethod
    def Enemy_tower(cls):
        enemy_tower = cls(TOWER_IMG_CP, WIN_WIDTH-TOWER_X, TOWER_Y, 500)
        return enemy_tower



