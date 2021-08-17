import pygame
import os
import math
from settings import TOWER_WIDTH, TOWER_HEIGHT, TOWER_X, TOWER_Y, WIN_WIDTH
from color_settings import *
from all_image import *


class Tower:
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
        # draw health
        for hp in range(self.max_health):
            if hp < self.health:
                hp_img = HEART
            else:
                hp_img = HEART_DEAD
            win.blit(hp_img, (self.rect.left + 40*(hp % 5), 170 + 35*(hp // 5)))

    # 用繼承寫出敵我雙方的塔
    @classmethod
    def Player_tower(cls, tower_health):
        player_tower = cls(TOWER_IMG_PL, TOWER_X, TOWER_Y, tower_health)
        return player_tower

    @classmethod
    def Enemy_tower(cls):
        enemy_tower = cls(TOWER_IMG_CP, WIN_WIDTH-TOWER_X, TOWER_Y, 1)
        return enemy_tower



