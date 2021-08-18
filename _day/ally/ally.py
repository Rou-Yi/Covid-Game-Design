import pygame
from _day.tower.tower import Tower
from _day.level_setting import level_setting

pygame.init()


class AllyGroup:
    def __init__(self, level):
        self.tower = Tower.Player_tower(level_setting[level]['tower health'])
        self.__expedition = []
        self.hp_count = False  # used in self.advance() to check tower is dead
        self.cd_count = 0
        self.cd_max_count = 60
        self.cat_is_not_moving = True

    def advance(self, enemy_group):
        """check the movement and health of cats and their tower
           and return True when the tower is dead"""
        # Cats 移動 & 血量判斷
        for cat in self.__expedition:
            if cat.health <= 0:
                self.clear()
            if cat.check_moving(enemy_group):
                cat.move()
                self.cat_is_not_moving = False

        # Ally Tower 血量判斷
        if self.tower.health == 0:
            if self.hp_count is not True:
                self.hp_count = True
            else:
                print('lose')
                return True
        return False

    def clear(self):
        """
        Remove the enemy from the expedition
        :param cat: class Cats()
        :return: None
        """
        self.__expedition = []

    def get(self):
        return self.__expedition
