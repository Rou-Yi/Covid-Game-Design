import pygame
import random
from _night.tower.tower import Tower
from _night.enemy.virus import Virus
from sound import virus_dead_soundtrack
from _night.level_setting import level_setting


pygame.init()


class EnemyGroup:
    def __init__(self):
        self.__reserved_members = []
        self.__expedition = []
        self.tower = Tower.Enemy_tower()
        self.hp_count = False  # used in self.advance() to check tower is dead
        self.cd_count = 0
        self.cd_max_count = 80
        self.campaign_count = 0
        self.campaign_max_count = 60
        self.summon_cd = 70
        self.summon_max_cd = 80
        self.knocked_down_num = 0  # 計算病毒被打倒的總數量
        self.max_enemy_num = 50  # 設置停損點

    def advance(self, player_group):
        """check the movement and health of virus and their tower
           and return True when the tower is dead"""
        # Virus 移動 & 血量判斷
        for virus in self.__expedition:
            # Control the move
            if virus.check_moving(player_group):
                virus.move()
            virus.move_back()
            if virus.health <= 0:
                self.retreat(virus)
        # Enemy Tower 血量判斷
        if self.tower.health < 0:
            self.tower.health = 0
        elif self.tower.health == 0:
            if self.hp_count is not True:
                self.hp_count = True
            else:
                return True
        return False

    def campaign(self):
        """Enemy go on an expedition."""
        if self.campaign_count > self.campaign_max_count and self.__reserved_members:
            self.__expedition.append(self.__reserved_members.pop())
            self.campaign_count = 0
            self.campaign_max_count = random.choice([100, 120, 140])  # 隨機派兵速度
        else:
            self.campaign_count += 1

    def summon(self, level):
        """use summon_cd to add an enemy to enemy list automatically"""
        virus_list = [Virus.Normal_Virus(), Virus.Alpha_Virus(), Virus.Beta_Virus(),
                      Virus.Delta_Virus(), Virus.Theta_Virus()]
        # 限制敵人數量上限
        if self.knocked_down_num < self.max_enemy_num:
            if self.summon_cd > self.summon_max_cd:
                self.__reserved_members.extend(random.choices(virus_list, weights=level_setting[level]['virus_prob']))
                self.summon_max_cd = random.choice(level_setting[level]['virus summon cd'])  # 隨機派兵速度
                self.summon_cd = 0
            else:
                self.summon_cd += 1

    def retreat(self, cat):
        """
        Remove the enemy from the expedition
        :param cat: class Cats()
        :return: None
        """
        self.__expedition.remove(cat)
        virus_dead_soundtrack()
        self.knocked_down_num += 1

    def get(self):
        """
        To return the enemy list.
        """
        return self.__expedition

