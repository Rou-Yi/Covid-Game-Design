import pygame
from _night.tower.tower import Tower
from sound import cat_dead_soundtrack

pygame.init()


class AllyGroup:
    def __init__(self):
        self.tower = Tower.Player_tower()
        self.__reserved_members = []
        self.__expedition = []
        self.hp_count = False  # used in self.advance() to check tower is dead
        self.cd_count = 0
        self.cd_max_count = 60

    def advance(self, enemy_group):
        """check the movement and health of cats and their tower
           and return True when the tower is dead"""
        # Cats 移動 & 血量判斷
        for cat in self.__expedition:
            if cat.check_moving(enemy_group):
                cat.move()
            cat.move_back()
            if cat.health <= 0:
                self.retreat(cat)
        # Ally Tower 血量判斷
        if self.tower.health < 0:
            self.tower.health = 0
        elif self.tower.health == 0:
            if self.hp_count is not True:
                self.hp_count = True
            else:
                return True
        return False

    def retreat(self, cat):
        """
        Remove the enemy from the expedition
        :param cat: class Cats()
        :return: None
        """
        self.__expedition.remove(cat)
        cat_dead_soundtrack()

    def get(self):
        """
        Get the enemy list
        """
        return self.__expedition

